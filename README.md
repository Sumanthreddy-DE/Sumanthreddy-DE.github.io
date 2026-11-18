# Sumanthreddy-DE.github.io

Source for [sumanthreddy.de](https://sumanthreddy.de), a German-language portfolio for
simulation and machine-learning engineering roles: CV, three case studies, and a question
assistant that answers from the CV. Static HTML and CSS with no build step, served by GitHub
Pages from the `main` branch (custom domain set in `CNAME`).

## Pages

| File | Content |
|---|---|
| `index.html` | Start page: summary, selected projects, contact |
| `projekte.html` | Project overview |
| `projekte/pinn.html`, `projekte/simready.html`, `projekte/nx-simscape.html` | Case studies |
| `Sumanth-Reddy-Settipalli-Lebenslauf.pdf` | CV (Lebenslauf) linked from top navigation (`profil.html` remains as fallback page) |
| `fragen.html` | Question assistant and its eval results |
| `automatisierung.html`, `blog.html` | AI automation work, blog |
| `impressum.html` | Legal notice |

Shared styling lives in `assets/site.css` (one light colour scheme, no dark mode) and
`assets/fonts.css` (self-hosted IBM Plex in `assets/fonts/`). The chat widget is
`assets/chat.js` and `assets/chat.css`, used by `index.html` and `fragen.html`. When you change
`site.css`, bump its `?v=` query in every page so browsers drop the cached copy.

## Question assistant

`fragen.html` ("Fragen an meinen Lebenslauf") answers visitor questions only from the CV and
the three case studies, and names its source. The backend is
[resume-assistant](https://github.com/Sumanthreddy-DE/resume-assistant), live at
`https://api.sumanthreddy.de`. The model (Claude Sonnet 5) was picked by an eval of 18 test
questions covering invented facts, source citation, language mirroring and prompt injection; the
results table is on `fragen.html`, the full answers in the backend repo. If the API is down the
pages still load, and the chat falls back to prepared answers.

## Working on it

```bash
python -m http.server          # preview at localhost:8000
pip install pytest playwright  # test dependencies (needs a Chromium for Playwright)
pytest tests/                  # page, chat, font and privacy checks against a local server
bash scripts/lint-arch.sh      # run before every commit
```

Push to `main` and GitHub Pages redeploys, usually within a minute.
