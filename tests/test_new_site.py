import re

from conftest import ROOT, PAGES

ALL_PAGES = PAGES + ["automatisierung.html", "fragen.html", "blog.html", "blog/agenten-delegieren.html"]
ALLOWED = {"#f2ece0", "#121110", "#ffffff", "#fff"}


def test_site_css_uses_only_the_three_colours():
    css = (ROOT / "assets/site.css").read_text(encoding="utf-8").lower()
    found = set(re.findall(r"#[0-9a-f]{3,8}\b", css))
    assert found <= ALLOWED, found - ALLOWED
    assert "rgb(" not in css and "hsl(" not in css
    assert "prefers-color-scheme" not in css
    assert "border-radius" not in css


def test_legacy_tokens_exist_for_chat_css():
    css = (ROOT / "assets/site.css").read_text(encoding="utf-8")
    root = css[css.index(":root"):css.index("}", css.index(":root"))]
    for token in ["--paper", "--ink", "--ink-muted", "--rule-soft", "--rule-strong", "--accent", "--figure-bg"]:
        assert token + ":" in root, token


def test_every_page_has_the_black_header_band(page, site_url):
    for name in ALL_PAGES:
        page.goto(f"{site_url}/{name}")
        band = page.locator("header.band").first
        assert band.evaluate("e => getComputedStyle(e).backgroundColor") == "rgb(18, 17, 16)", name


def test_no_page_scrolls_sideways(browser, site_url):
    for width in (390, 1440, 1920):
        ctx = browser.new_context(viewport={"width": width, "height": 900})
        pg = ctx.new_page()
        for name in ALL_PAGES:
            pg.goto(f"{site_url}/{name}")
            over = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
            assert over <= 0, (name, width, over)
        ctx.close()


TILES = ["projekte/simready.html", "projekte/pinn.html", "projekte/nx-simscape.html",
         "projekte.html#lebenslauf-assistent", "projekte.html#engagement", "projekte.html#telefonassistent"]


def test_homepage_grid_has_six_linked_tiles(page, site_url):
    page.goto(f"{site_url}/index.html")
    hrefs = page.locator("#projekte .tiles > a.tile").evaluate_all("els => els.map(e => e.getAttribute('href'))")
    assert len(hrefs) == 6
    for want, got in zip(TILES, hrefs):
        if want:
            assert got == want


def test_homepage_tiles_are_square_on_desktop_and_text_fits(browser, site_url):
    for width in (390, 700, 1024, 1440, 1920):
        ctx = browser.new_context(viewport={"width": width, "height": 900})
        pg = ctx.new_page()
        pg.goto(f"{site_url}/index.html")
        cut = pg.evaluate("[...document.querySelectorAll('.tile .txt')].map(t => t.scrollHeight - t.clientHeight)")
        assert max(cut) <= 0, (width, cut)
        if width >= 1440:
            r = pg.locator(".tile").first.bounding_box()
            assert abs(r["width"] - r["height"]) < 2, (width, r)
        ctx.close()


def test_hero_says_the_decided_line(page, site_url):
    page.goto(f"{site_url}/index.html")
    assert page.locator(".hero h1").inner_text() == "Hallo, ich bin Sumanth."
    assert page.locator(".hero .sub").inner_text() == "Maschinenbauingenieur, der KI-Systeme baut."


def test_nav_lebenslauf_links_directly_to_pdf_on_every_page(page, site_url):
    for name in ALL_PAGES:
        page.goto(f"{site_url}/{name}")
        expected = "../Sumanth-Reddy-Settipalli-Lebenslauf.pdf" if "/" in name else "Sumanth-Reddy-Settipalli-Lebenslauf.pdf"
        href = page.locator(".nav a", has_text="Lebenslauf").get_attribute("href")
        assert href == expected, (name, href)

