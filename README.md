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

## Planned

A grounded question-and-answer section, so a visitor can ask about the projects listed here and
get answers drawn from the repositories rather than from an unconstrained model. The static
summary above stays as the primary content and loads regardless.
