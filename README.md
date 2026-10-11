# Sumanthreddy-DE.github.io

Source for [sumanthreddy-de.github.io](https://sumanthreddy-de.github.io), a single-page
professional summary: education, selected engineering projects, work experience and contact
details. Static HTML with no build step and no dependencies, served by GitHub Pages from the
`main` branch.

## Structure

- `index.html` holds the whole site. Content and styling are in one file; the CSS uses
  `prefers-color-scheme` so the page follows the visitor's light or dark setting.

## Editing

Edit `index.html` and push to `main`. GitHub Pages redeploys automatically, usually within a
minute. To preview locally, open the file in a browser, or run `python -m http.server` in this
directory and visit `localhost:8000`.

## Question assistant (fragen.html)

A grounded question-and-answer assistant ("Fragen an meinen Lebenslauf") answers visitor
questions about the projects listed here, drawn only from the CV and three case studies.
Backend: [resume-assistant](https://github.com/Sumanthreddy-DE/resume-assistant), live at
`https://api.sumanthreddy.de`. The model (Claude Sonnet 5) was chosen by an eval of 15 test
questions — refusal of invented facts, source citation, language mirroring, injection
resistance — graded in `resume-assistant/evals/results/`; the visible results table is in
`fragen.html`. The static summary stays as the primary content and loads regardless.
