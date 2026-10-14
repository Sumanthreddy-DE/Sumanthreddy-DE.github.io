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
- Last swept: **2026-10-14** (anny-link-404, chat-panel-focus, state-md-private-path,
  eval-prescreen-nie closed; prompt v5 deployed).

---

## Open — S1 (blocker / broken demo)

_(none yet)_

---

## Open — S2 (UX gap, polish, deferred decisions)

- **images-placeholder** — 7 placeholder SVGs remain: `portrait`, `pinn-interface`,
  `pinn-fehler`, `simready-ui`, `simready-gnn`, `nx-simscape`, `nx-mapping`. `tea-team`, `gokart`, `digidorf` are already real
  files. Count corrected 2026-10-08 (was "8 slots").
- **eval-v5-rerun** — prompt v5 (document-voice ban) is deployed and smoke-tested live,
  but the 15-question eval has not been re-run on it. From `Projects/resume-assistant`:
  `.venv/Scripts/python.exe evals/run_eval.py --url https://api.sumanthreddy.de`
  (~16 min, rate limit), then hand-grade, fill the Urteil column and commit the result
  file. *(opened 2026-10-14, user decision to defer)*
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
- **css-blocks-drift** — the shared inline `<style>` is no longer one block: four
  variants (index, projekte, impressum, and case studies + profil + fragen). Decide:
  re-unify into one block, or document the drift as intended. *(found 2026-10-10,
  Sumanthreddy-DE.github.io session)*
- **design-directions-status** — `docs/exec-plans/active/2026-09-16-design-directions.md`
  has no `**Status:**` line; set done/abandoned and move it to `completed/` (private
  plans repo). *(found 2026-10-10, Sumanthreddy-DE.github.io session)*

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

## Done this session (2026-10-14)

- **anny-link-404** — Anny repo link replaced with the private-repo no-link span in
  `automatisierung.html` and `content/de.md` (repo private since 2026-10-07).
  *(commit: f4b1a6d)*
- **chat-panel-focus** — panel open no longer force-focuses the textarea on desktop
  (close button reachable by Tab); mobile (modal) still focuses it for the inert page.
  *(commit: f4b1a6d)*
- **state-md-private-path** — STATE.md landmine no longer names the private CV path.
  *(commit: f4b1a6d)*
- **eval-prescreen-nie** — `must_not_match` regexes in `evals/questions.json` now accept
  nie/niemals/kein-/keine/keinen as negations; regression tests added (41 pass).
  *(resume-assistant commit: e0bb7c7)*
- **chat-voice-doc-speak** — prompt v5 bans document voice ("sein Lebenslauf sagt",
  "laut Lebenslauf", "aus seiner Tätigkeit bei", "in seiner Funktion als") in rule 13.
  Deployed to the VPS 2026-10-14 (`e0bb7c7`, service restarted, `/health` OK) and
  smoke-tested live: the KTmfk answer now states facts directly. Eval re-run still
  open → **eval-v5-rerun**. *(resume-assistant commit: e0bb7c7)*
- German questions: verified live — the bot answers German questions in German
  (prompt rule 10, language of the question). No change needed.

---

## Done this session (2026-10-11)

- **chat-voice-human** — prompt v4 (tone rules: paraphrase, varied openers, light
  human touch, refusals exempt) deployed and re-evaled: Sonnet 5 15/15 on prompt v3
  AND v4 (german-row C1 flag = recurring false positive, hand-graded pass both times).
  Cache prefix 7363 → 7726 tokens. Graded files committed in resume-assistant.
  User approved the live tone. *(commits: 1a7c6d9→5246045 prompt v4, 79dce67 eval)*

- **site restructure day** — DigiDorf before DEHN; contact section rewritten twice
  (collaboration invite → plain search statement, no location narrowing, no
  "ab sofort"); dash density pass (43 replaces, ranges kept); new page
  `automatisierung.html` (KI-Automatisierung: Resume-Assistant, Self-Talk-Coach,
  Anny-Booking-Bot, SmartRecruiters — full entries, Anny format); `projekte.html`
  retitled „Simulation und Machine Learning"; KI-Automatisierung link in topbars;
  hackathon one-liner + TEA paragraph on homepage; ICAMES talk in profil Ausbildung;
  thesis repo link relabeled (LaTeX + PDF); CV PDF rebuilt from master (KTmfk fix);
  duplicate link line removed. Career-Ops removed from public site (user decision).
  *(commits: 1a4fcea, 4a861c7, f46e8ff, ca32223, e38901e, 744cb34, 4a523ed, fe3ed21)*

- **chat-layer steps 1–6** — Sonnet 5 eval on prompt v3: 15/15 (german-row C1 flag =
  false positive, hand-graded pass). Model pick: Sonnet 5 per spec rule (Haiku 5.5
  14/15). `fragen.html` results filled, rail model name, README eval section, spec §10
  row, graded eval file committed. VPS clean-up done (`DEBUG_IP=false`, localhost origin
  removed, restart verified in journal). Launch gate passed (pytest 39, lint-arch PASS).
  Merged `chat-layer` → `main` `--no-ff` (`05cf98b`), pushed, live site verified
  (fragen.html + chat.js + API health 200). *(commits: 89c0f5f, 05cf98b)*

---

## Archived (older sweeps, compressed)

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
