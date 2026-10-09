import re
from pathlib import Path

from conftest import ROOT

KEYS = ["gebaut", "berechnung", "deutsch", "verfuegbar", "siemens"]


def style_blocks(rel):
    return re.findall(r"<style>.*?</style>", (ROOT / rel).read_text(encoding="utf-8-sig"), re.S)


def test_shared_style_block_matches_case_study_pages():
    assert style_blocks("fragen.html")[0] == style_blocks("projekte/pinn.html")[0]


def test_every_chip_has_a_prepared_answer_with_source(page, site_url):
    page.goto(f"{site_url}/fragen.html")
    for key in KEYS:
        assert page.locator(f".chip[data-key={key}]").count() == 1
        prepared = page.locator(f"#antwort-{key}")
        assert prepared.locator("p.source").inner_text().startswith("Quelle:")


def test_eval_table_lists_fifteen_questions(page, site_url):
    page.goto(f"{site_url}/fragen.html")
    assert page.locator(".evaltab tbody tr").count() == 15


def test_without_javascript_prepared_answers_are_readable(browser, site_url):
    context = browser.new_context(java_script_enabled=False)
    pg = context.new_page()
    pg.goto(f"{site_url}/fragen.html")
    assert pg.locator("#vorbereitet").get_attribute("open") is not None
    assert pg.locator("#antwort-siemens").is_visible()
    assert not pg.locator(".chat-live").is_visible()
    context.close()
    # Playwright's java_script_enabled=False does not switch the HTML parser to
    # "scripting disabled", so <noscript> content never renders there. Check the
    # notice in the source instead.
    html = (ROOT / "fragen.html").read_text(encoding="utf-8-sig")
    noscript = re.search(r"<noscript>(.*?)</noscript>", html, re.S).group(1)
    assert "Der Assistent braucht JavaScript" in noscript


def test_no_prose_em_dash_and_no_italics():
    html = (ROOT / "fragen.html").read_text(encoding="utf-8-sig")
    body = html[html.index("<body>"):]
    assert "—" not in body
    assert "<em>" not in body and "<i>" not in body
