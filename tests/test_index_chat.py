from playwright.sync_api import expect

from chatmock import Backend, answer


def open_index(page, site_url):
    backend = Backend(page)
    page.goto(f"{site_url}/index.html")
    return backend


def test_button_visible_panel_closed_no_backend_contact(page, site_url):
    b = open_index(page, site_url)
    expect(page.locator(".chat-open")).to_be_visible()
    expect(page.locator(".chat-open")).to_contain_text("Fragen zu meinem Lebenslauf?")
    expect(page.locator("#chat-panel")).to_be_hidden()
    page.wait_for_timeout(500)
    assert b.health == 0


def test_open_ask_and_close(page, site_url):
    b = open_index(page, site_url)
    b.reply = answer("Er ist sofort verfügbar.")
    page.locator(".chat-open").click()
    expect(page.locator("#chat-panel")).to_be_visible()
    expect(page.locator(".chat-open")).to_have_attribute("aria-expanded", "true")
    expect(page.locator("#chat-panel textarea")).to_be_focused()
    page.locator("#chat-panel .chip[data-key=verfuegbar]").click()
    expect(page.locator("#chat-panel .turn.a .source")).to_have_text("Quelle: Lebenslauf")
    assert b.health == 1
    page.keyboard.press("Escape")
    expect(page.locator("#chat-panel")).to_be_hidden()
    expect(page.locator(".chat-open")).to_be_focused()


def test_panel_fallback_links_to_prepared_answers(page, site_url):
    b = open_index(page, site_url)
    b.reply = [{"type": "fallback", "reason": "off"}]
    page.locator(".chat-open").click()
    page.locator("#chat-panel .chip[data-key=deutsch]").click()
    answer_turn = page.locator("#chat-panel .turn.a").last
    expect(answer_turn.locator(".chat-status")).to_contain_text("sumanthreddy.settipalli@gmail.com")
    expect(answer_turn.locator("a.lnk")).to_have_attribute("href", "fragen.html#vorbereitet")


def test_button_hidden_without_javascript(browser, site_url):
    context = browser.new_context(java_script_enabled=False)
    pg = context.new_page()
    pg.goto(f"{site_url}/index.html")
    assert not pg.locator(".chat-open").is_visible()
    context.close()


def test_kontakt_offers_email_and_linkedin_only(page, site_url):
    for path in ("index.html", "projekte.html"):
        page.goto(f"{site_url}/{path}")
        links = page.locator("#kontakt .foot-links a")
        assert links.all_inner_texts() == ["E-Mail schreiben", "LinkedIn"], path
