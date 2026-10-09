import json

CORS = {"Access-Control-Allow-Origin": "*"}
PREFLIGHT = {**CORS, "Access-Control-Allow-Methods": "GET, POST", "Access-Control-Allow-Headers": "Content-Type"}


def answer(text, source="Quelle: Lebenslauf"):
    full = f"{text}\n{source}"
    return [{"type": "delta", "text": full[:6]}, {"type": "delta", "text": full[6:]},
            {"type": "done", "model": "claude-haiku-4-5", "cache_read": 0}]


class Backend:
    """Stands in for the server: records requests and replays scripted NDJSON."""

    def __init__(self, page):
        self.requests, self.health, self.held = [], 0, []
        self.reply = answer("Antwort.")
        page.route("**/health", self._health)
        page.route("**/chat", self._chat)

    def _health(self, route):
        self.health += 1
        route.fulfill(status=200, content_type="application/json", body='{"ok": true}', headers=CORS)

    def _chat(self, route):
        request = route.request
        if request.method == "OPTIONS":
            route.fulfill(status=204, headers=PREFLIGHT)
            return
        self.requests.append(json.loads(request.post_data))
        if self.reply == "hold":
            self.held.append(route)
            return
        if self.reply == "abort":
            route.abort()
            return
        status, events = self.reply if isinstance(self.reply, tuple) else (200, self.reply)
        route.fulfill(status=status, content_type="application/x-ndjson", headers=CORS,
                      body="".join(json.dumps(e, ensure_ascii=False) + "\n" for e in events))
