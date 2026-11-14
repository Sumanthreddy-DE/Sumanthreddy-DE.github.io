import re

from conftest import ROOT, PAGES

# Fixes from the 2026-11-14 portfolio review: colour portrait, no placeholder
# share image, no template diagrams on the homepage, CV PDF before the CV.

ALL_PAGES = PAGES + ["automatisierung.html", "fragen.html"]


def test_portrait_is_shown_in_colour(page, site_url):
    page.goto(f"{site_url}/index.html")
    assert page.locator(".portrait").evaluate("e => getComputedStyle(e).filter") == "none"


def test_no_page_shares_the_placeholder_portrait():
    for name in ALL_PAGES:
        html = (ROOT / name).read_text(encoding="utf-8")
        assert "portrait.svg" not in html, name


def test_homepage_shows_no_template_diagrams():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    for svg in ["pinn-interface.svg", "simready-ui.svg", "nx-simscape.svg"]:
        assert f'src="assets/{svg}"' not in html, svg
    assert 'src="assets/pinn-fehler.png"' in html
    assert 'src="assets/simready-copilot.png"' in html


def test_homepage_links_sit_under_the_result_line():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    for art in ["pinn", "simready", "nx"]:
        seg = html[html.index(f'id="{art}"'):]
        seg = seg[:seg.index("</article>")]
        assert re.search(r'class="metric-line">.*?</p>\s*<div class="entry-links">', seg, re.S), art


def test_cv_download_comes_before_the_experience(page, site_url):
    page.goto(f"{site_url}/profil.html")
    order = page.evaluate(
        "() => [...document.querySelectorAll('section[id]')].map(s => s.id)")
    assert order.index("download") < order.index("berufserfahrung")


def test_digidorf_mascot_is_small(page, site_url):
    page.goto(f"{site_url}/projekte.html")
    width = page.locator('img[src="assets/digidorf.png"]').evaluate(
        "e => e.getBoundingClientRect().width")
    assert width <= 200
