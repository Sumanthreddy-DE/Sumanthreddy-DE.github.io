# OG URLs and stale tests — handoff, 2026-11-03

Branch: `fix/og-urls-stale-tests`.

## Item 1 — og-urls-custom-domain

Commit: `a43bdc0b8e7de4fccb00b02a82d448e20fc2d078`

Changed only the `og:url` and `og:image` metadata lines, replacing
`https://sumanthreddy-de.github.io/` with `https://sumanthreddy.de/`, in:

- `index.html`
- `fragen.html`
- `profil.html`
- `projekte.html`
- `automatisierung.html`
- `projekte/nx-simscape.html`
- `projekte/pinn.html`
- `projekte/simready.html`

The requested check, `grep -rn "sumanthreddy-de.github.io" --include=*.html .`,
printed nothing (exit 1: no matches). Architecture lint passed.

## Item 2 — stale-tests-site-css-and-focus

Commit: `bfdf99ee1360d135b5b6aed24a685aa4322e16c5`

Files changed:

- `tests/test_fragen_static.py`: replaced the shared-style-block equality test
  with the supplied shared CSS link and no-redefined-root-tokens test.
- `tests/test_index_chat.py`: changed the desktop textarea expectation to
  unfocused and added the mobile textarea focus assertion immediately after
  the page-inert assertion.

No HTML or asset files changed in this item.

### Impressum fail-check

Temporarily added `impressum.html` to `SITE_CSS_PAGES` and ran
`~/.venvs/site/bin/python -m pytest -q`.

Result: **1 failed, 50 passed in 29.58s**. The failing test was
`test_pages_share_site_css_without_redefining_tokens`, with
`AssertionError: impressum.html` at the CSS-link count assertion: `assert 0 == 1`.
Removed `impressum.html` again before the final run and commit.

### Final pytest output — last five lines

The final pytest run emitted only two lines, reproduced in full below; there
were no additional pytest lines to include. Harness hook notices are separate
from pytest output.

```text
...................................................                      [100%]
51 passed in 28.95s
```

All test runs used exactly `~/.venvs/site/bin/python -m pytest -q`.
The initial baseline was **2 failed, 49 passed in 31.63s**.
Architecture lint and `git diff --check` also passed before the item 2 commit.

## Handoff file and limitations

This handoff adds `docs/handoff-2026-11-03-og-tests.md` in a separate commit.
All requested task work was completed. No push was attempted.
`BACKLOG.md`, `STATE.md`, and memory files were not edited; no save-session ran.

The environment reported that the Citadel PowerShell push-block hook was
unavailable (`pwsh: ENOENT`) and used its fallback matcher. This did not block
the requested checks or commits. An ancillary read of the global harness
backlog at `citadel/harness/memory/claude-lab/BACKLOG.md` returned file-not-found;
it was unrelated to these changes.
