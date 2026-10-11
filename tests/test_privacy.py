from playwright.sync_api import expect


def test_impressum_has_datenschutz_covering_the_chat(page, site_url):
    page.goto(f"{site_url}/impressum.html")
    section = page.locator(".row", has=page.locator("h2", has_text="Datenschutz"))
    expect(section).to_contain_text("meinen eigenen Server")
    expect(section).to_contain_text("Anthropic")
    expect(section).to_contain_text("GitHub Pages")
    expect(section).to_contain_text("keine Schriften oder Skripte von fremden Servern")
