import pytest

from conftest import PAGES


@pytest.mark.parametrize("path", PAGES)
def test_fonts_are_self_hosted_and_load(page, site_url, path):
    hosts = []
    page.on("request", lambda r: hosts.append(r.url.split("/")[2]))
    page.goto(f"{site_url}/{path}")
    page.evaluate("document.fonts.ready")
    loaded = page.evaluate("[...document.fonts].filter(f => f.status === 'loaded').map(f => f.family)")
    assert not [h for h in hosts if "googleapis" in h or "gstatic" in h]
    assert any("Libre Bodoni" in f for f in loaded), loaded
    assert any("Public Sans" in f for f in loaded), loaded
