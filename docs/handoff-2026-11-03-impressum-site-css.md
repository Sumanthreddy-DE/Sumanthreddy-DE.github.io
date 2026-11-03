# Impressum shared-CSS migration — handoff

Branch: `fix/impressum-site-css`. Brief: claude-lab's
`docs/exec-plans/active/2026-11-03-portfolio-impressum-site-css.md` (Status: active).
Starting HEAD: `e761095`.

## Files and commits

- `impressum.html`: links `assets/site.css` immediately after `fonts.css`, without
  a query suffix; removes tokens and shared-selector rules; starts the remaining
  inline styles with the specified page-specific comment.
- `tests/test_fragen_static.py`: includes Impressum in `SITE_CSS_PAGES` and removes
  the obsolete migration-exception sentence.
- `docs/handoff-2026-11-03-impressum-site-css.md`: this handoff.
- Migration + test commit: `1f77124` (`impressum-site-css: migrate legal page to shared stylesheet`).
- Handoff commit: the commit introducing this file, with subject
  `impressum-site-css: document verification and browser findings`. Its SHA is
  reported in the final response; a commit cannot contain its own SHA.

No changes to page text, links, existing head metadata, other pages, or
`assets/site.css`. A scripted comparison against starting HEAD verified the
entire HTML outside the inline style and the added stylesheet link is identical.

## Verification

First command, before any edit: `~/.venvs/site/bin/python -m pytest -q`.
Baseline output:

```text
...................................................                      [100%]
51 passed in 33.81s
```

After extending the list, before editing `impressum.html`, ran:
`~/.venvs/site/bin/python -m pytest -q tests/test_fragen_static.py::test_pages_share_site_css_without_redefining_tokens`.
It failed as intended: `AssertionError: impressum.html`, `assert 0 == 1`
(no shared stylesheet link), `1 failed in 0.06s`.

Final full pytest run (the entire pytest output was only two lines, so there
are fewer than five lines to reproduce):

```text
...................................................                      [100%]
51 passed in 24.10s
```

`bash scripts/lint-arch.sh`: `lint-arch: PASS — all checks clean`.
`git diff --check`: passed. Self-review of the diff found no additional code
issues; no independent reviewer was dispatched, consistent with the instruction
to use agents only when the user asks. No new workflow scratch files were created:
the brief permits only this new handoff file, which also records the decisions.

## Shared-selector drift removed

Every differing declaration or declaration set is listed below. “Absent” means
the shared selector does not declare it; removing the inline rule lets the
reset/inheritance apply rather than retaining a page override.

| Selector / context | Inline value → shared value / resulting behavior |
| --- | --- |
| `body` | `line-height: 1.6` → `1.55` |
| `.page` | No side borders → `border-left` and `border-right: 1px solid var(--rule-soft)` |
| `.lnk` | `transition: color .15s` → `color .15s, border-color .15s` |
| `.row` | `grid-template-columns: 180px minmax(0, 660px)` → `180px minmax(0, 780px)` |
| `.row` | `margin-bottom: 36px` → absent, reset to `0` |
| `footer` | `margin-top: 72px` → `88px` |
| `footer` | `padding-top: 32px` → `40px` |
| `footer` | `font-size: 0.8125rem` → absent, inherits body `16px` |
| `footer` | `color: var(--ink-muted)` → absent, inherits body `var(--ink)` |
| `.row` at max-width 900px (shared grouped selector `.row, .hero-inner`) | `gap: 10px` → `24px` |
| `.row` at max-width 900px | `margin-bottom: 32px` → absent, reset to `0` |

Footer link font size and color remain defined by `.lnk`, so removal of footer
font/color declarations does not change that link's appearance. Other removed
same-selector rules were identical. Light/dark token values were identical;
the shared sheet additionally supplies `--figure-bg`. Newly inherited shared
behavior also includes smooth scrolling and print rules (black-on-white palette,
hidden topbar, 11pt body and print grid); print rendering was not separately tested.

## Page-only decisions

- Keep `h1` and its mobile override: shared `.hero h1` is structurally different
  and does not match the standalone legal-page heading; its heading border and
  margins still belong here.
- Keep `.row h2` and its mobile padding override: `.rail` / `.rail dt` are close
  editorial-label styles but do not match this page's heading markup.
- Keep `.row p` and `.row p:last-child`: shared `.entry p` and `.about p` do not
  match these legal-content rows; preserve paragraph spacing within a row.
- Keep `.row a` and `.row a:hover`: shared `.lnk` and other scoped link selectors
  do not match the plain content anchors; preserve their underline and hover.
- Keep `.row strong`: shared `.job li b` / `.minor b` do not match legal emphasis.
- Remove the entire base/mobile `.row` rules and the entire `footer` rule,
  including declarations absent from the shared versions: the brief says to
  remove rules for selectors already defined, rather than salvaging individual
  declarations. This sacrifices old inter-row spacing, as explicitly requested
  by the shared-styles-win decision.
- Treat `.row` inside the shared grouped responsive selector as a shared rule,
  rather than preserving a 10px gap on a literal-selector technicality.
- Work on the already checked-out, clean requested branch in this repo;
  no extra worktree or plan files were needed for this constrained task.

## Browser check

Used `~/.venvs/site/bin/python` with installed Playwright Chromium and a temporary
local HTTP server. Waited for `document.fonts.ready`; captured full-page PNGs
with viewport 1280×900 and 375×812, each with explicit light/dark color scheme,
before the first edit and after the final HTML edit. Servers were shut down.
Screenshots are not committed:

`/tmp/impressum-check/{before,after}-{1280x900,375x812}-{light,dark}.png`

**Limitation:** this session's model cannot accept image input. All eight PNGs
were captured and opened through the read tool, but the harness reported that
image input is unsupported. Therefore no visual inspection is claimed. The
following are browser-measured layout changes and CSS-derived appearance
changes, provided per requested viewport/scheme for the human visual reviewer.

| Viewport / scheme | Measured changes and expected visible effect |
| --- | --- |
| 1280×900 light | Content left edge 110→111px and width 1060→1058px from the new soft side borders. Text column expands 660→780px, reducing wrapping; body line spacing tightens. Row margins disappear; Datenschutz starts at y=636.64→459.88px. Footer border y=1090.95→869.44px, with larger top gap and inner padding. Light palette unchanged. |
| 1280×900 dark | Same measured geometry and wrapping changes as desktop light. Side borders use the dark soft-rule token; dark paper/ink/accent values unchanged. |
| 375×812 light | Content left edge 28→29px and width 319→317px. Label-to-body grid gap increases 10→24px while 32px inter-row margins disappear; body line spacing tightens. Datenschutz y=821.39→735.30px; footer border y=1687.20→1607.45px. New side borders remain visible in CSS at this width. Light palette unchanged. |
| 375×812 dark | Same measured geometry changes as mobile light. Side borders use the dark token; dark palette unchanged. |

After migration, all four browser configurations passed
`document.documentElement.scrollWidth <= innerWidth` (no horizontal overflow).
The layout is intentionally denser, especially on desktop; human screenshot
comparison remains necessary to judge the resulting inter-row readability.

## Not done

- Visual screenshot comparison remains pending because image input is unsupported;
  screenshot capture and browser geometry checks are complete.
- No push, merge, BACKLOG/STATE/memory edits, or session-save was performed.
