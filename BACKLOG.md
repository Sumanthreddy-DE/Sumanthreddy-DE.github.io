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

- **new-site-run** — execute `docs/exec-plans/active/2026-11-15-new-site.md` (approved 2026-11-15) with a cheaper agent via citadel delegation + Orca: worktree `~/projects/site-new-site`, branch `feat/new-site`, stop after Task 8. Then Claude reviews the 27 screenshots and the diff, Sumanth approves, merges and pushes. (found 2026-11-15, new-site session)
- **new-site-screenshots** — SimReady copilot recaptured at 200% zoom (current file 776×376 px, unreadable in a tile) and a Simufact result, both from `~/inbox`; KI-Telefonassistent image once Sumanth finishes it (tile 6). (found 2026-11-15, new-site session)

- **review-layout-mockups** — *superseded 2026-11-15 by `docs/exec-plans/active/2026-11-15-new-site.md` (round-1 variants rejected; new cream/black/white site planned).* Plan item B (`docs/exec-plans/active/2026-11-14-portfolio-review-fixes.md`).
  Sumanth asked for this first in the next session. Build 2–3 wider, borderless variants on copies of
  `index.html` plus one case study (pattern: memory `lessons_mockups.md`), screenshots at 1440/1920/390,
  Sumanth picks before any real page changes. Decided: prose stays near 680px, never full width;
  images/UI get wider (the SimReady copilot screenshot is hard to read at the current 780px column).
  Starting numbers from the review: drop `.page` side borders and the 1140px sheet; wrapper
  `min(100% - 96px, 1440px)`; visuals ~736px; metadata rail → one line above each title; under
  900px stack with 20px gutters. Also B3: the mobile chat launcher must not cover content
  (`assets/chat.css:66`, `:110`). *(decided 2026-11-14, review session)*
- **review-text-batch** — wording done together with Sumanth, not delegated:
  (1) key decision at the top of each case study (D2; drafts were in the 2026-11-14 session, sourced from
  `projekte/pinn.html:67`, `projekte/simready.html:72,83`, `projekte/nx-simscape.html:74`; not yet approved);
  (2) PINN caption: the plot's title shows G_eff mean error 10.0 % / pass 56 %, the homepage says
  "unter 5 % in 33 von 36", the caption gives the 500-sample medians (1,4 % / 4,0 %). Write a caption
  that names the two tests separately, so nothing looks contradictory (check the numbers against the
  pinn repo record first);
  (3) `projekte.html:45` "Die drei ausführlichen Fallstudien stehen auf der Startseite" → link the three
  case-study pages directly (A6). *(2026-11-14)*
- **blog-page** — plan D3. `blog.html` on shared CSS: reverse-chronological list (date, title,
  two-sentence summary, link out). First post: gist
  https://gist.github.com/Sumanthreddy-DE/71f8ae5471d102c6f274470281640c0a ("Claude Code on a VPS
  from your phone" guide). Needs from Sumanth: the two-sentence summary. Claude's view: the topic is
  off-message for Mittelstand mech+ML readers, so add one intro line saying why it is there. "Blog" nav
  entry on every page (nav differs per page today), must still fit at 390px. RSS later. *(2026-11-14)*
- **homepage-chat-demo-entry** — plan D1. In-flow project block on the homepage (brief §7.2: chat is a
  project, never the front door, no pop-up), reusing `automatisierung.html:61–69` copy: "Ausprobieren" →
  `fragen.html`, Code → resume-assistant repo. Build alongside the chosen layout. *(2026-11-14)*
- **case-page-green-diagrams** — plan C4/C5. `projekte/simready.html:75` (`simready-gnn.svg`) and
  `projekte/nx-simscape.html:68` (`nx-mapping.svg`) still use the green template Sumanth dislikes.
  Needs Sumanth's choice. Claude recommends: SimReady → HTML results table, NX → remove. Also switch the
  case pages' og:image from SVG to PNG/JPG (`projekte/*.html:15`). *(2026-11-14)*
- **accent-colour-decision** — *superseded 2026-11-15: the new site uses only cream, black and white, no accent (`2026-11-15-new-site.md`).* Plan C6. Decide after the new layout is on screenshots: keep `#2F5D46`,
  ink blue `#244C73` (8.07:1) or slate `#39424E` (9.22:1); dark mode needs its own value. *(2026-11-14)*
- **impeccable-hook-false-positives** — the impeccable Stop hook flags `tight-leading` (line-height 1.2
  on 28–30px serif headings, `assets/site.css:241`, `:391`) and `cramped-padding` (`.jump`; its links
  have 13px padding, `site.css:187`). Both are false positives that predate the session. Suppressing them
  creates a new `.impeccable/config.json` in the repo, a new-structure ask: Sumanth to say yes or no.
  *(2026-11-14)*
- **simready-face-render-all-green** — SimReady task, noted here because it shaped the homepage crop: the
  copilot's face-score render for `small_feature_hole.step` was all green while it reported two
  findings, so the render was cropped out of `assets/simready-copilot.png`. Fix in SimReady, then
  maybe re-shoot. *(2026-11-14)*
- **nx-image-own-render** — the homepage NX figure (`assets/nx-baugruppe.png`, added
  2026-11-14) is a 484×491 frame of the KTmfk render of the assembly Sumanth converted from NX
  to Simscape-ready XML; the KTmfk logo is projected on the floor under the frame. Replace it
  with an own image without the logo. Best: re-render or screenshot the assembly in NX (or
  the Simscape model) at 1200 px+ on a plain background, which also gives the "before/after"
  the review asked for. Avoid an AI-regenerated "replica": it would no longer be the real
  assembly, and under a case study that claims real engineering work that reads as fake.
  Keep the source file name, swap `index.html` src/width/height, rerun the screenshot check.
  *(found 2026-11-14, portfolio review session)*
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

- **simready-homepage-screenshot** — done 2026-11-14: `assets/simready-copilot.png`, a crop of Sumanth's copilot screenshot (German question on `small_feature_hole.step`, score 84/100, two findings, CalculiX citation). Full frame kept in `~/inbox/Simready-image.png`; the face-score render was all green, so it was cropped out. Text in the image is small at the current 780px column; the wider layout (plan item B) fixes that.
- **impressum-not-on-site-css** — done 2026-11-03 (merge `b362ac4`; `1f77124`, handoff `f416644`, review fix `2684b98`): impressum.html links `assets/site.css`, inline block keeps only page rules, test list includes it. Built on the VPS by opencode with GPT-6.1 Sol (it cannot view images); the laptop screenshot review found rows stacked with no spacing (brief's "site.css wins" rule dropped `.row` margins) and restored page-local spacing. Visible changes kept: side borders, 780px text column, as on the other pages. 51 passed.
- **og-urls-custom-domain** — done 2026-11-03 (`a43bdc0`, merge `5c05884`): 16 og:url/og:image lines in 8 pages moved to `https://sumanthreddy.de/`, only the domain changed. Built on the VPS by opencode with GPT-6.1 Sol via dlab (not an open-weight model), reviewed on the laptop.
- **stale-tests-site-css-and-focus** — done 2026-11-03 (`bfdf99e`, merge `5c05884`): style-block equality test → `test_pages_share_site_css_without_redefining_tokens` (fail-checked against impressum.html); desktop chat expects no textarea focus, mobile test now asserts focus. 51 passed on VPS and laptop. Same VPS run (GPT-6.1 Sol); handoff `docs/handoff-2026-11-03-og-tests.md`.
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
