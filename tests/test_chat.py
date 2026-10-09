import re

import pytest
from playwright.sync_api import expect

from chatmock import Backend, answer

STATUS = {
    "rate": "Gerade viele Fragen – hier die vorbereitete Antwort.",
    "upstream_busy": "Gerade viele Fragen – hier die vorbereitete Antwort.",
    "cap": "Der Assistent pausiert für heute – hier die vorbereitete Antwort.",
    "off": "Der Assistent ist gerade abgeschaltet – hier die vorbereitete Antwort.",
    "error": "Vorbereitete Antwort – der Assistent startet gerade.",
}
UNREACHABLE = "Der Assistent ist gerade nicht erreichbar. Schreiben Sie mir: sumanthreddy.settipalli@gmail.com"


def open_page(page, site_url, timeout_ms=None):
    backend = Backend(page)
    page.goto(f"{site_url}/fragen.html")
    if timeout_ms is not None:
        page.evaluate(f"document.querySelector('.chat').dataset.timeoutMs = '{timeout_ms}'")
    return backend


def chip(page, key):
    return page.locator(f".chat .chip[data-key={key}]")


def last_answer(page):
    return page.locator(".turn.a").last


def ask_free(page, text):
    page.locator(".chat textarea").fill(text)
    page.locator(".chat .ask button").click()


def test_chip_streams_answer_and_moves_source_line(page, site_url):
    b = open_page(page, site_url)
    b.reply = answer("Er hat drei Systeme gebaut.", "Quelle: Lebenslauf · Fallstudie PINN")
    chip(page, "gebaut").click()
    expect(last_answer(page).locator(".source")).to_have_text("Quelle: Lebenslauf · Fallstudie PINN")
    expect(last_answer(page).locator(".text")).to_have_text("Er hat drei Systeme gebaut.")
    expect(chip(page, "gebaut")).to_have_class(re.compile(r"\bused\b"))
    assert b.requests == [{"question": "Was hat er konkret gebaut?", "history": []}]


def test_model_output_renders_as_text_never_html(page, site_url):
    b = open_page(page, site_url)
    payload = '<img src=x onerror="window.__xss=1">'
    b.reply = answer(payload)
    ask_free(page, "Test")
    expect(last_answer(page).locator(".text")).to_have_text(payload)
    assert page.locator(".thread img").count() == 0
    assert page.evaluate("window.__xss") is None


def test_follow_up_sends_history(page, site_url):
    b = open_page(page, site_url)
    b.reply = answer("Antwort eins.")
    ask_free(page, "Frage eins")
    expect(last_answer(page).locator(".source")).to_be_visible()
    ask_free(page, "Frage zwei")
    expect(page.locator(".turn.a")).to_have_count(2)
    expect(page.locator(".turn.a").nth(1).locator(".source")).to_be_visible()
    assert b.requests[1]["history"] == [
        {"role": "user", "content": "Frage eins"},
        {"role": "assistant", "content": "Antwort eins.\nQuelle: Lebenslauf"},
    ]


def test_history_sent_is_capped_at_six_messages(page, site_url):
    b = open_page(page, site_url)
    for i in range(5):
        ask_free(page, f"Frage {i}")
        expect(page.locator(".turn.a .source")).to_have_count(i + 1)
    history = b.requests[4]["history"]
    assert len(history) == 6
    assert history[0] == {"role": "user", "content": "Frage 1"}
    assert b.requests[4]["question"] == "Frage 4"


def test_question_over_500_characters_is_not_sent(page, site_url):
    b = open_page(page, site_url)
    assert page.locator(".chat textarea").get_attribute("maxlength") == "500"
    page.evaluate("const t = document.querySelector('.chat textarea'); t.value = 'x'.repeat(501);"
                  "t.dispatchEvent(new Event('input'))")
    page.locator(".chat .ask button").click()
    expect(page.locator(".chat .count")).to_have_text("501 / 500")
    page.wait_for_timeout(300)
    assert b.requests == []


@pytest.mark.parametrize("reason", sorted(STATUS))
def test_backend_fallback_shows_prepared_answer_and_status(page, site_url, reason):
    b = open_page(page, site_url)
    b.reply = [{"type": "fallback", "reason": reason}]
    chip(page, "deutsch").click()
    expect(last_answer(page).locator(".chat-status")).to_have_text(STATUS[reason])
    expect(last_answer(page).locator(".text")).to_contain_text("B2")
    expect(last_answer(page).locator(".source")).to_have_text("Quelle: Lebenslauf")


def test_truncated_stream_replaces_partial_text(page, site_url):
    b = open_page(page, site_url)
    b.reply = [{"type": "delta", "text": "Halber Sa"}, {"type": "fallback", "reason": "truncated"}]
    chip(page, "siemens").click()
    expect(last_answer(page).locator(".chat-status")).to_be_visible()
    expect(last_answer(page).locator(".text")).to_contain_text("Kooperationspartner")
    expect(last_answer(page).locator(".text")).not_to_contain_text("Halber Sa")


def test_cold_start_times_out_to_prepared_answer(page, site_url):
    b = open_page(page, site_url, timeout_ms=300)
    b.reply = "hold"
    chip(page, "verfuegbar").click()
    expect(last_answer(page).locator(".chat-status")).to_have_text(
        "Vorbereitete Antwort – der Assistent startet gerade.", timeout=3000)
    expect(last_answer(page).locator(".text")).to_contain_text("sofort verfügbar")


def test_free_text_with_unreachable_backend_shows_email(page, site_url):
    b = open_page(page, site_url)
    b.reply = "abort"
    ask_free(page, "Hat er Erfahrung mit Abaqus?")
    expect(last_answer(page).locator(".chat-status")).to_have_text(UNREACHABLE)


def test_invalid_request_status(page, site_url):
    b = open_page(page, site_url)
    b.reply = (422, [])
    ask_free(page, "Frage")
    expect(last_answer(page).locator(".chat-status")).to_have_text(
        "Diese Frage ließ sich nicht senden. Bitte kürzer fassen – höchstens 500 Zeichen.")


def test_no_backend_contact_before_interaction(page, site_url):
    b = open_page(page, site_url)
    page.wait_for_timeout(500)
    assert b.health == 0 and b.requests == []
    page.locator(".chat textarea").focus()
    page.wait_for_timeout(300)
    assert b.health == 1
    page.locator(".chat textarea").blur()
    page.locator(".chat textarea").focus()
    page.wait_for_timeout(300)
    assert b.health == 1


def test_prepared_answers_collapse_when_javascript_runs(page, site_url):
    open_page(page, site_url)
    assert page.locator("#vorbereitet").get_attribute("open") is None


def test_final_line_without_newline_is_still_parsed(page, site_url):
    b = open_page(page, site_url)
    page.route("**/chat", lambda route: route.fulfill(
        status=200, content_type="application/x-ndjson",
        headers={"Access-Control-Allow-Origin": "*"},
        body='{"type": "delta", "text": "Er ist sofort verfügbar.\\nQuelle: Lebenslauf"}\n'
             '{"type": "done", "model": "m", "cache_read": 0}'))
    ask_free(page, "Frage")
    expect(last_answer(page).locator(".source")).to_have_text("Quelle: Lebenslauf")
    expect(last_answer(page).locator(".text")).to_have_text("Er ist sofort verfügbar.")


def test_mid_stream_stall_ends_in_fallback_and_unlocks(page, site_url):
    open_page(page, site_url)
    page.evaluate("""() => {
        document.querySelector('.chat').dataset.stallMs = '300';
        window.fetch = async (url) => {
            if (String(url).endsWith('/health')) return new Response('{"ok":true}');
            const enc = new TextEncoder();
            const body = new ReadableStream({ start(c) { c.enqueue(enc.encode('{"type":"delta","text":"Halber Sa"}\\n')); } });
            return new Response(body, { status: 200 });
        };
    }""")
    chip(page, "siemens").click()
    expect(last_answer(page).locator(".chat-status")).to_have_text(
        "Vorbereitete Antwort – der Assistent startet gerade.", timeout=3000)
    expect(last_answer(page).locator(".text")).not_to_contain_text("Halber Sa")
    expect(page.locator(".chat .ask button")).to_be_enabled()
