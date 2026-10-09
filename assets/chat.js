/* Chat layer for fragen.html and the side panel on index.html.
   Model output is attacker-influenced: it is only ever written with textContent. */
(function () {
  'use strict';

  const MAX_TURNS = 6;
  const MAX_CHARS = 500;
  const EMAIL = 'sumanthreddy.settipalli@gmail.com';
  const STARTING = 'Vorbereitete Antwort – der Assistent startet gerade.';
  const BUSY = 'Gerade viele Fragen – hier die vorbereitete Antwort.';
  const PREPARED_STATUS = {
    timeout: STARTING,
    error: STARTING,
    truncated: STARTING,
    rate: BUSY,
    upstream_busy: BUSY,
    cap: 'Der Assistent pausiert für heute – hier die vorbereitete Antwort.',
    off: 'Der Assistent ist gerade abgeschaltet – hier die vorbereitete Antwort.'
  };
  const UNREACHABLE = 'Der Assistent ist gerade nicht erreichbar. Schreiben Sie mir: ' + EMAIL;
  const INVALID = 'Diese Frage ließ sich nicht senden. Bitte kürzer fassen – höchstens 500 Zeichen.';
  const SOURCE_LINE = /^(Quelle|Source):/;

  document.documentElement.classList.add('js');

  function el(tag, cls, text) {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text) node.textContent = text;
    return node;
  }

  function splitSource(full) {
    const lines = full.replace(/\s+$/, '').split('\n');
    const last = lines[lines.length - 1].trim();
    if (lines.length > 1 && SOURCE_LINE.test(last)) {
      return { body: lines.slice(0, -1).join('\n').trim(), source: last };
    }
    return { body: full.trim(), source: '' };
  }

  function preparedAnswer(key) {
    const block = key && document.getElementById('antwort-' + key);
    if (!block) return null;
    const body = Array.from(block.querySelectorAll('p:not(.source)'))
      .map((p) => p.textContent.trim()).join('\n\n');
    const source = block.querySelector('p.source');
    return { body: body, source: source ? source.textContent.trim() : '' };
  }

  function statusLine(text) {
    const p = el('p', 'chat-status', text);
    p.setAttribute('role', 'status');
    return p;
  }

  function initChat(root) {
    const endpoint = root.dataset.endpoint.replace(/\/$/, '');
    const thread = root.querySelector('.thread');
    const form = root.querySelector('.ask');
    const input = form.querySelector('textarea');
    const sendButton = form.querySelector('button[type=submit]');
    const count = root.querySelector('.count');
    const history = [];
    let busy = false;
    let warmed = false;

    // Contact the server only once the visitor interacts, never on page load.
    function warm() {
      if (warmed) return;
      warmed = true;
      fetch(endpoint + '/health').catch(() => {});
    }
    root.addEventListener('focusin', warm);
    root.addEventListener('pointerdown', warm);

    function addTurn(kind, text) {
      const li = el('li', 'turn ' + kind);
      li.appendChild(el('div', 'who', kind === 'q' ? 'Ihre Frage' : 'Assistent'));
      const body = el('div', 'text', text);
      li.appendChild(body);
      thread.appendChild(li);
      li.scrollIntoView({ block: 'nearest' });
      return { li: li, body: body };
    }

    function finish(turn, full) {
      const parts = splitSource(full);
      turn.body.textContent = parts.body;
      if (parts.source) turn.li.appendChild(el('div', 'source', parts.source));
    }

    function fallback(turn, reason, key) {
      turn.li.classList.add('fallback');
      turn.body.textContent = '';
      if (reason === 'invalid') {
        turn.li.appendChild(statusLine(INVALID));
        return;
      }
      const prepared = preparedAnswer(key);
      if (prepared) {
        turn.body.textContent = prepared.body;
        if (prepared.source) turn.li.appendChild(el('div', 'source', prepared.source));
        turn.li.appendChild(statusLine(PREPARED_STATUS[reason] || STARTING));
        return;
      }
      turn.li.appendChild(statusLine(UNREACHABLE));
      if (root.dataset.preparedUrl) {
        const link = el('a', 'lnk', 'Vorbereitete Antworten lesen');
        link.href = root.dataset.preparedUrl;
        turn.li.appendChild(link);
      }
    }

    async function readEvents(response, onDelta) {
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      let end = null;
      for (;;) {
        const chunk = await reader.read();
        if (chunk.done) break;
        buffer += decoder.decode(chunk.value, { stream: true });
        let newline;
        while ((newline = buffer.indexOf('\n')) >= 0) {
          const line = buffer.slice(0, newline).trim();
          buffer = buffer.slice(newline + 1);
          if (!line) continue;
          const event = JSON.parse(line);
          if (event.type === 'delta') onDelta(event.text);
          else end = event;
        }
      }
      return end;
    }

    async function ask(question, key) {
      question = question.trim();
      if (busy || !question || question.length > MAX_CHARS) return;
      busy = true;
      sendButton.disabled = true;
      addTurn('q', question);
      const turn = addTurn('a', '');
      const controller = new AbortController();
      let full = '';
      let started = false;
      let end = null;
      const timer = setTimeout(() => { if (!started) controller.abort(); },
        Number(root.dataset.timeoutMs) || 8000);
      try {
        const response = await fetch(endpoint + '/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question: question, history: history.slice(-MAX_TURNS) }),
          signal: controller.signal
        });
        if (response.status === 413 || response.status === 422) {
          end = { type: 'fallback', reason: 'invalid' };
        } else if (!response.ok || !response.body) {
          end = { type: 'fallback', reason: 'error' };
        } else {
          end = await readEvents(response, (text) => {
            started = true;
            full += text;
            turn.body.textContent = full;
          });
        }
      } catch (err) {
        end = { type: 'fallback', reason: started ? 'error' : 'timeout' };
      }
      clearTimeout(timer);
      if (end && end.type === 'done') {
        finish(turn, full);
        history.push({ role: 'user', content: question }, { role: 'assistant', content: full.trim() });
      } else {
        fallback(turn, end ? end.reason : 'error', key);
      }
      busy = false;
      sendButton.disabled = false;
    }

    function updateCount() {
      count.textContent = input.value.length + ' / ' + MAX_CHARS;
    }

    input.addEventListener('input', updateCount);
    input.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        form.requestSubmit();
      }
    });
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      if (busy) return;
      updateCount();
      if (input.value.length > MAX_CHARS) return;
      const question = input.value;
      input.value = '';
      updateCount();
      ask(question, null);
    });
    root.querySelectorAll('.chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        if (busy) return;
        chip.classList.add('used');
        ask(chip.textContent, chip.dataset.key);
      });
    });
  }

  function initPanel(openButton) {
    const panel = document.getElementById(openButton.getAttribute('aria-controls'));
    const closeButton = panel.querySelector('.panel-close');
    function open() {
      panel.hidden = false;
      openButton.setAttribute('aria-expanded', 'true');
      panel.querySelector('textarea').focus();
    }
    function close() {
      panel.hidden = true;
      openButton.setAttribute('aria-expanded', 'false');
      openButton.focus();
    }
    openButton.addEventListener('click', () => (panel.hidden ? open() : close()));
    closeButton.addEventListener('click', close);
    panel.addEventListener('keydown', (event) => { if (event.key === 'Escape') close(); });
  }

  document.querySelectorAll('.chat').forEach(initChat);
  document.querySelectorAll('.chat-open').forEach(initPanel);
  const prepared = document.getElementById('vorbereitet');
  if (prepared) prepared.open = false;
})();
