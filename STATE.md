# STATE — Sumanthreddy-DE.github.io

Type: project
Status: active
Last touched: 2026-10-28

<!-- Machine-maintained by /save-session Step 6b. Do not hand-edit rows or dates. -->
<!-- Set `Type: hub` if this folder only routes to sub-projects; hubs get their
     Last touched line bumped and nothing else. -->

## What

The public GitHub Pages site at https://sumanthreddy.de/ (`sumanthreddy-de.github.io` redirects) — a job-search
landing page for recruiters and hiring engineers at midsize German manufacturers.
Two workstreams: the static site (Phase A — shipped 2026-09-23 as a seven-page
German portfolio), and an "ask me anything" chat layer grounded in the CV
(Phase B — live since 2026-10-11).

## Doing

- Phase A — **shipped and live** (`7e571ff`, custom domain `https://sumanthreddy.de` with HTTPS enforced 2026-10-22, `f843347`). Visual overhaul committed 2026-10-05
  (`f3b0b71`, `8f0c130`, `1858ab0`): cream/terracotta → Tinte & Zederngrün after the
  user flagged the "Claude look"; italics and prose em-dashes swept (AI tells);
  homepage stripped to hero + 3 case studies + Über mich + Kontakt; figure breakout
  killed — 780px column aligns rules/figures/captions/text by construction; Contact
  heading is now a statement.
- **6 of 7 image slots replaced 2026-10-22 (`30950e5`).** Only `portrait` remains a placeholder (`assets/portrait.svg`, waiting on user photo). `pinn-interface`, `pinn-fehler`, `simready-ui`, `simready-dashboard`, `simready-gnn`, `nx-simscape`, and `nx-mapping` are now real figures/diagrams, and case-study pages use full 780 px column width without repeating homepage images.
- **EN toggle** — user asked for DE/EN switch; filed as backlog S2, deferred until
  the portrait lands and the German copy has settled.
- **Phase B chat — live on `https://sumanthreddy.de`.** `fragen.html` + homepage panel merged `05cf98b`.
  Backend `Projects/resume-assistant` on the VPS at `https://api.sumanthreddy.de` (CORS updated for `https://sumanthreddy.de` in `36d3803`, verified live 2026-10-22).
  **Prompt v5 deployed 2026-10-14** (`e0bb7c7`): document-voice ban, smoke-tested
  live; 15-question eval re-run still open (backlog `eval-v5-rerun`).
- **chat-layer step 7 (CV part) done 2026-10-14** — bot is a project line in the
  ml-preset CV (SimReady VLM bullet cut for space); Live-Demo routing for AI-job
  Anschreiben in `_strategy/selection-rules.md`. Myself/CV edit set needs a commit.
- **Shared CSS unified 2026-10-14** (`305ba8c`) — one external `assets/site.css`
  replaces four inline style variants; verified live 2026-10-22 (`site-css-live-verify` closed).
- **chat-layer `tool` event — built 2026-10-28, on branch `feat/tool-card`, not merged**
  (`e45343c`, `c836f81`). The client now ends the NDJSON stream only on `done`/`fallback`,
  so the backend's upcoming `{"type":"tool", …get_repo_activity…}` no longer looks like a
  terminator; an ok event renders a muted "GitHub live abgefragt: \<summary\>" line above the
  answer, error renders "GitHub gerade nicht erreichbar", and any fallback hides it again.
  Text only (`textContent`), styled off `--ink-muted`, verified in light/dark at 1280/360.
  Suite: 46 passed, 2 failed — the same known `stale-tests-site-css-and-focus` pair.
  **The backend does not emit `tool` yet** (`Projects/resume-assistant`), so the line only
  appears once that lands.
- Selector / gate idea — parked. Reorder filter, not a gate. Not specced.

## Resume here

1. Decide the `feat/tool-card` ship order: push and merge it as a no-op (the client
   ignores an absent event), or land the `resume-assistant` `tool` emitter first so the
   line is visible the moment the site deploys.
2. Commit the `Myself/CV` step-7 edit set (explicit paths — PII landmine).
3. Run the prompt-v5 eval: from `Projects/resume-assistant`,
   `.venv/Scripts/python.exe evals/run_eval.py --url https://api.sumanthreddy.de`
   (~16 min), hand-grade, commit the result file (backlog `eval-v5-rerun`).
4. Optional S3 polish: update the 2 stale pytest assertions (`stale-tests-site-css-and-focus`) and `og:url`/`og:image` tags (`og-urls-custom-domain`).

Portrait (parallel track, waiting on user): drop into `assets/` as `portrait.jpg`/`.png`, update `src` + `width`/`height` in `index.html`, lint, commit.

**Do not re-run `scratchpad/build_details.py`** — `projekte/pinn.html`, `simready.html`, and `nx-simscape.html` carry hand-edited layouts and figures the generator would destroy.

Live plans: chat spec (v4 block) + `docs/exec-plans/active/2026-10-09-chat-layer-implementation.md` (Tasks 1–14 done); `docs/exec-plans/active/2026-09-17-multipage-portfolio.md`
(only `portrait` in Task 1 open).

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

- 2026-10-28 — chat layer taught the backend's `tool` event: `readEvents` ends only on
  `done`/`fallback` (unknown types ignored), an ok event renders "GitHub live abgefragt:
  \<summary\>" above the answer body and an error renders "GitHub gerade nicht erreichbar",
  all `textContent`; any fallback hides and clears the line first. 9 new tests
  (incl. no-tool stream unchanged, escaped payload, 360 px overflow, index panel);
  suite 46 passed + the 2 pre-existing `stale-tests-site-css-and-focus` failures.
  Branch `feat/tool-card` (`e45343c`, `c836f81`), not merged — backend emitter still to come.
- 2026-10-22 — custom domain `sumanthreddy.de` connected (IONOS DNS `@` A/AAAA + `www` CNAME, GitHub Pages `CNAME` `f843347`, HTTPS enforced); replaced 6 project placeholders (`pinn-interface`, `pinn-fehler`, `simready-ui`, `simready-dashboard`, `simready-gnn`, `nx-simscape`, `nx-mapping`) with unified cedar-green SVGs and real thesis/Streamlit plates, expanded PINN & SimReady case studies, aligned case-study text to 780 px, removed duplicate homepage images, and linked project headings (`30950e5`); added `https://sumanthreddy.de` to `resume-assistant` CORS (`36d3803`), deployed on VPS, and verified live chatbot streaming; closed `site-css-live-verify` (`dc2518d`)
- 2026-10-14 — backlog day: anny-link-404, chat-panel-focus, state-md-private-path,
  eval-prescreen-nie closed; prompt v5 (document-voice ban) committed, deployed to
  VPS (repo-ownership fix on /opt), smoke-tested live; German-question handling
  verified live; chat-layer step 7 CV part (bot as ml-preset project line +
  selection-rules Live-Demo routing, SimReady VLM bullet cut); css-blocks-drift
  unified into external assets/site.css (DOM-verified); design-directions moved to
  completed/ in portfolio-private
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
