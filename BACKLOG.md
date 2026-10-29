# Sumanthreddy-DE.github.io Backlog

Living list of open issues, deferred work, and known caveats. Updated each session.

**Severity rubric**
- **S1** — blocker / data loss / broken demo. Fix before next ship.
- **S2** — UX gap, missing polish, deferred decision.
- **S3** — tech debt, deprecations, low-impact polish, dead code.

**Conventions**
- New issue → append to correct severity section.
- Mention by short slug in commit body (e.g. "Closes: my-issue-slug").
- On close → move to **Done this session** with commit SHA.
- End of session → user sweeps **Done** → **Archived** (one-line compress).
- Last swept: **2026-10-22** (custom domain `sumanthreddy.de` + HTTPS enforced, 6 project image slots replaced, chatbot CORS fixed on VPS).

---

## Open — S1 (blocker / broken demo)

_(none yet)_

---

## Open — S2 (UX gap, polish, deferred decisions)

- **images-placeholder** — 1 placeholder SVG remains: `portrait`. All 6 project visual slots (`pinn-interface`, `pinn-fehler`, `simready-ui`, `simready-dashboard`, `simready-gnn`, `nx-simscape`, `nx-mapping`) plus `tea-team`, `gokart`, `digidorf` are now real figures/diagrams (updated 2026-10-22).
- **chat-demo-video** — 60–90 s demo of the live chat at the top of `README.md`: 10 s problem + audience,
  20 s the GitHub tool call ("Arbeitet er aktuell noch an SimReady?" → tool line + dated answer),
  15 s a grounded CV answer (Siemens trap), 15 s multi-turn chat, 5 s the live URL loading. Record
  with any screen recorder, upload via a GitHub issue comment, embed the user-attachments link.
  *(found 2026-10-29, claude-lab session: idea 1 from the "4 things that matter" portfolio video)*
- **en-toggle** — user asked for a DE/EN language toggle in the top bar. Deferred
  2026-10-05: the brief's decided line is "German-first, English later", and the
  positioning argument (Mittelstand reads German) still holds. Adding EN doubles the
  copy surface to maintain while the copy is still moving, and the English half is
  where AI tells creep back in. Revisit **after** the images land and the German copy
  has settled. Right shape when we do it: a static `en/` mirror or `lang` swap, not
  a JS toggle — and a session of its own.
  - Re-discussed 2026-10-14: still deferred for the same reasons. User is arranging
    images; this stays parked until they land.

---

## Open — S3 (tech debt, deprecations, low-impact polish)

- **stale-tests-site-css-and-focus** — `tests/test_fragen_static.py::test_shared_style_block_matches_case_study_pages` and `tests/test_index_chat.py::test_open_ask_and_close` still assert the pre-`305ba8c` inline style blocks and pre-`f4b1a6d` desktop textarea auto-focus. Update both tests to match the external `assets/site.css` and mobile-only focus behavior. *(found 2026-10-22, Sumanthreddy-DE.github.io session)*
- **og-urls-custom-domain** — `<meta property="og:url">` and `<meta property="og:image">` across the 8 HTML pages still reference `https://sumanthreddy-de.github.io/...`; update them to `https://sumanthreddy.de/...`. *(found 2026-10-22, Sumanthreddy-DE.github.io session)*
- **chat-copy-sofort** — "antwortet sofort" on the corner button sits next to "ab sofort
  verfügbar" on the homepage; user kept the wording, revisit if it reads oddly live.

- **dotted-folder-name** — whether to rename the *local* working folder from
  `Sumanthreddy-DE.github.io` to `Sumanthreddy-DE-github-io`. Dots in a path
  cause friction in some tooling; nothing is broken today.
  - The **GitHub repo name cannot change** — a Pages user site must be named
    `<username>.github.io` or the site stops resolving. Only the local folder
    name is on the table, and it need not match the remote.
  - Cost of renaming: a local folder name that no longer matches the repo or the
    live URL, plus updating whatever references the path.
  Verdict when filed 2026-09-16: **not worth doing.** The tooling friction was
  fixed at the source rather than dodged. Revisit only if dotted paths bite
  somewhere new.

- **availability-contradiction** — the CV PDF says „Sofort verfügbar"; the site
  contact section (rewritten 2026-10-11) says nothing about availability. Decide one
  position: keep availability public (add one quiet line to the site) or drop it from
  the master before the next PDF rebuild. *(found 2026-10-11, Sumanthreddy-DE.github.io session)*

---

## Doing

- **chat-layer step 7 (partial)** — remaining after launch (needs user approval, CV
  repo): add the bot as a CV project line and a "Live-Demo" link in AI-job Anschreiben
  (spec §14). ~~Rebuild the CV PDFs~~ done 2026-10-11: site PDF rebuilt from master,
  KTmfk fix verified in the shipped PDF.

## Done this session

- **eval-v5-rerun** — superseded: the prompt-v6 run (all v5 rules + tool rules 15–17) ran 2026-10-28 on a local server with claude-sonnet-5 and was hand-graded 18/18 bestanden on 2026-10-29 (`resume-assistant` `5e27d2d`). *(closed 2026-10-29, claude-lab session)*

---

## Archived (older sweeps, compressed)

- **2026-10-22 · custom domain `sumanthreddy.de`, project figures & case studies, chatbot CORS** (4 items) — see commits `f843347`, `30950e5`, `dc2518d` (and `resume-assistant` `36d3803`). Connected IONOS DNS (`@` A/AAAA + `www` CNAME) and enforced HTTPS on `https://sumanthreddy.de`; replaced all 6 project image placeholders (`pinn-interface`, `pinn-fehler`, `simready-ui`, `simready-dashboard`, `simready-gnn`, `nx-simscape`, `nx-mapping`) with unified cedar-green SVGs and real thesis/Streamlit plates; expanded PINN and SimReady case-study copy, aligned case-study text to 780 px, removed duplicate homepage figures, and linked project headings; added `https://sumanthreddy.de` to `resume-assistant` CORS and verified live streaming on the VPS; closed `site-css-live-verify`.
- **2026-10-14 · prompt v5 deploy, external `site.css`, CV step-7 line** (7 items) — see commits `f4b1a6d`..`537744e` (and `resume-assistant` `e0bb7c7`, `portfolio-private` `a2f5496`). Unified 4 inline `<style>` variants into external `assets/site.css` (`css-blocks-drift`); deployed prompt v5 banning document voice (`chat-voice-doc-speak`); added `resume-assistant` project line to ml-preset CV (`chat-layer step 7`); closed `anny-link-404`, `chat-panel-focus`, `state-md-private-path`, `eval-prescreen-nie`, `design-directions-status`.
- **2026-10-11 · chat-layer launch, prompt v4 eval, KI-Automatisierung page** (3 items) — see commits `89c0f5f`, `05cf98b`, `1a4fcea`..`fe3ed21` (and `resume-assistant` `1a7c6d9`..`79dce67`). Shipped `fragen.html` + homepage chat panel (`05cf98b`), evaluated Sonnet 5 15/15 on prompts v3 and v4, added `automatisierung.html`, rebuilt CV PDF from master.

- **2026-10-05 · palette, structure, alignment, AI-tell sweep** (7 items) — see commits
  `f3b0b71`..`1858ab0`. Cream/terracotta replaced with Tinte & Zederngrün after user
  flagged the "Claude look" (`palette-claude-tell`). All display italics removed
  (`italic-serif-tell`); brand mark became a home link, later dropped from the
  homepage nav as an H1 duplicate. Homepage stripped to hero + 3 cases + Über mich +
  Kontakt; Hackathons/Engagement/Werkzeuge moved to `projekte.html`
  (`structure-strip-down`). Figure breakout killed; 780px column aligns rules,
  figures, captions, text by construction. All prose em-dashes → en-dash
  Gedankenstrich per rulebook lesson 9/10. Contact heading question → statement.
  Werkzeuge gained Career-Ops + self-talk-coach (private). Closed:
  `cv-bullet-nx-motion` (CV already correct), `ktmfk-application-unknown` (confirmed
  absent from CV), `profil-keywords-lost` (user call), `weekly-digest-private`
  (dropped). Opened: `en-toggle` (S2, deferred until after images land).
