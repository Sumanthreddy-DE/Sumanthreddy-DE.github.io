# STATE — Sumanthreddy-DE.github.io

Type: project
Status: active
Last touched: 2026-10-10

<!-- Machine-maintained by /save-session Step 6b. Do not hand-edit rows or dates. -->
<!-- Set `Type: hub` if this folder only routes to sub-projects; hubs get their
     Last touched line bumped and nothing else. -->

## What

The public GitHub Pages site at https://sumanthreddy-de.github.io/ — a job-search
landing page for recruiters and hiring engineers at midsize German manufacturers.
Two workstreams: the static site (Phase A — shipped 2026-09-23 as a seven-page
German portfolio), and an "ask me anything" chat layer grounded in the CV
(Phase B — deferred, not cancelled).

## Doing

- Phase A — **shipped and live** (`7e571ff`). Visual overhaul committed 2026-10-05
  (`f3b0b71`, `8f0c130`, `1858ab0`): cream/terracotta → Tinte & Zederngrün after the
  user flagged the "Claude look"; italics and prose em-dashes swept (AI tells);
  homepage stripped to hero + 3 case studies + Über mich + Kontakt; figure breakout
  killed — 780px column aligns rules/figures/captions/text by construction; Contact
  heading is now a statement. Werkzeuge gained Career-Ops + self-talk-coach (private).
- **Waiting on the user for 7 images.** Placeholders remain for `portrait`,
  `pinn-interface`, `pinn-fehler`, `simready-ui`, `simready-gnn`, `nx-simscape`,
  `nx-mapping`. `pinn-fehler` matters most — the "unter 5 %" claim sits above the
  fold with nothing evidencing it.
- **EN toggle** — user asked for DE/EN switch; filed as backlog S2, deferred until
  the images land and the German copy has settled.
- **Phase B chat — built and deployed, not launched.** Branch `chat-layer` (unpushed,
  unmerged) holds `fragen.html`, the homepage corner button + panel, self-hosted fonts,
  Werkzeuge entry and Datenschutz. Backend `Projects/resume-assistant` live at
  `https://api.sumanthreddy.de` (VPS, Caddy + systemd). Model eval in progress: Haiku 4.5
  ~11/15, Haiku 5.5 14/15, Sonnet 5 14/15 (older prompt); Sonnet on prompt v3 pending.
  Steps in `BACKLOG.md` → Doing → chat-layer.
- Selector / gate idea — parked. Reorder filter, not a gate. Not specced.

## Resume here

Free laptop memory, then from `Projects/resume-assistant` run
`.venv/Scripts/python.exe evals/run_eval.py --url https://api.sumanthreddy.de` (server on
Sonnet 5, prompt v3). Grade with the user, pick the model, then `BACKLOG.md` → Doing →
chat-layer steps 3–7 (fill eval table, `DEBUG_IP=false`, launch gate, merge, CV follow-ups).

Images (parallel track, waiting on user): drop into `assets/` under the existing
base names, update `src` + `width`/`height`, `class="plate"` for plots and
screenshots, `<figure class="inset">` under ~700 px. Re-render, lint, commit.

**Do not re-run `scratchpad/build_details.py`** — `projekte/pinn.html` carries a
hand-added figure the generator would destroy.

Live plans: chat spec (v4 block) + `docs/exec-plans/active/2026-10-09-chat-layer-implementation.md` (Tasks 1–14 done); `docs/exec-plans/active/2026-09-17-multipage-portfolio.md`
(only Task 1, the images, open).

## Pipeline

- Ideas not started yet.

## Landmines

- **This repo is PUBLIC and cannot be made private** — a Pages user site must be named
  `<username>.github.io`. `.gitignore` excludes `docs/exec-plans/` and `Archive/` for
  that reason; its comments carry the reasoning. Stage explicit paths, never
  `git add -A`.
- The redesign brief (`docs/exec-plans/design-docs/2026-09-16-redesign-brief.md`)
  contains competitive self-assessment that must not be published under a real name.
  It lives in the private nested repo since 2026-10-09; never copy it back into the
  public `docs/design-docs/`.
- A parallel `claude-lab` session works in this repo. It has reset history here once
  (`reset: moving to 0a247c4`). Check `git reflog`, not just `git log`, before
  committing.
- **The CV contradicts the site.** The CV's master data (kept in a private repo
  outside this one) says joints "in NX Motion"; PTC Creo is correct and the site now
  says so. The user fixes the CV himself — do not edit it unasked.
- **An earlier copy pass invented a fact that reached production**: the site claimed the
  NX→Simscape work was for "elektrische Ski-Rollen", an application in no CV or repo.
  Removed 2026-09-23. Verify concrete specifics in inherited copy before republishing.
- **`docs/exec-plans/` is its own private git repo** (`portfolio-private`, since
  2026-10-09), holding plans, `design-docs/` and `Archive/`. The site repo ignores it.
  Run git for plans **inside that folder**; a commit from the site root never sees them.
- The CV PDF at repo root **contains the user's phone number**, published deliberately
  on his explicit call after the exposure was flagged. Do not silently strip it.

## Done

- 2026-10-10 — chat layer: mockups → placement (own page + corner panel) → plan →
  Tasks 1–14 built and reviewed (corpus, backend, site, VPS deploy at api.sumanthreddy.de);
  fonts self-hosted; Kontakt e-mail + LinkedIn only; Datenschutz added
- 2026-09-16 — scaffolded via new-project-init.sh
- 2026-09-16 — chat layer brainstormed and specced end to end (corpus source, model,
  rate limiting, grounding rules, eval set, error handling); scope then widened to a
  full site redesign after an audit found a live factual error plus missing CV PDF,
  `og:` tags and favicon. Spec reconciled against the parallel session's redesign brief.
- 2026-09-16 — Phase A built in Direction 1 (Libre Bodoni / Public Sans / paper base
  / brick-red accent). German-first B1 copy, three case studies (PINN, SimReady,
  KTMFK promoted from work experience), Impressum (§ 5 DDG). Impeccable audit clean
  except the em-dash advisory. Commits `d203b51` through `9c591f9`.
- 2026-09-23 — rebuilt as a seven-page site and shipped (`7e571ff`, 24 files,
  +4450/−671). Copy rewritten from B1 to native technical German, fixing two real
  term errors (`Grenzschicht`→`Grenzfläche`, `Graph-Netzwerk`→`Graph Neural
  Network`). Added Hackathons, Engagement, Über mich, a Festanstellung contact CTA,
  `projekte.html`, three detail pages and `profil.html`. Nav "Lebenslauf" now opens a
  page instead of firing a download. Fixed a real print-palette bug (dark-mode tokens
  printed onto white at 3.4:1). Verified live.
- 2026-10-09 — housekeeping: brief ignored + index rows reverted (`98a0fd7`), multipage plan
  Task 1/5 refreshed, superseded plan moved to `completed/`. Chat spec rewritten v1 → v3
  (German corpus, chatbot-first, eval-picked model, prior-art rules). Created
  `portfolio-private` (private, nested at `docs/exec-plans/`; brief, directions, Archive
  moved in; `81dd4a7`, `b496849`) and `resume-assistant` (public, empty).
