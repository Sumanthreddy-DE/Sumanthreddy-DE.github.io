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
- Last swept: **2026-10-11** (chat-layer steps 1–6 closed).

---

## Open — S1 (blocker / broken demo)

_(none yet)_

---

## Open — S2 (UX gap, polish, deferred decisions)

- **anny-link-404** — `projekte.html` links `github.com/Sumanthreddy-DE/anny-booking-bot`,
  which is private since 2026-10-07 (history purge, waiting on GitHub Support), so
  visitors hit a 404. Remove or unlink it until the repo is public again.
  *(found 2026-10-10, Sumanthreddy-DE session)*

- **images-placeholder** — 7 placeholder SVGs remain: `portrait`, `pinn-interface`,
  `pinn-fehler`, `simready-ui`, `simready-gnn`, `nx-simscape`, `nx-mapping`. `tea-team`, `gokart`, `digidorf` are already real
  files. Count corrected 2026-10-08 (was "8 slots").
- **en-toggle** — user asked for a DE/EN language toggle in the top bar. Deferred
  2026-10-05: the brief's decided line is "German-first, English later", and the
  positioning argument (Mittelstand reads German) still holds. Adding EN doubles the
  copy surface to maintain while the copy is still moving, and the English half is
  where AI tells creep back in. Revisit **after** the images land and the German copy
  has settled. Right shape when we do it: a static `en/` mirror or `lang` swap, not
  a JS toggle — and a session of its own.

---

## Open — S3 (tech debt, deprecations, low-impact polish)

- **chat-panel-focus** — the homepage chat panel puts focus in the textarea, so the
  close button is reached with Shift+Tab. Desktop panel is non-modal by design.
- **chat-copy-sofort** — "antwortet sofort" on the corner button sits next to "ab sofort
  verfügbar" on the homepage; user kept the wording, revisit if it reads oddly live.
- **eval-prescreen-nie** — auto pre-screen misses "nie"/"keine/keinen" as negations
  (false flags on Haiku 5.5 / Sonnet 5 answers). Hand grading decides; tidy the regexes.
- **state-md-private-path** — `STATE.md` on `main` names a path inside the private CV
  repo; reword on the next STATE edit (public repo).
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

---

## Doing

- **chat-voice-human** — answers read like a recital of the CV: "B2, Zertifikat in
  Vorbereitung" comes back word-for-word from the document, so it feels hardcoded /
  AI-ish rather than a person talking. Want: prompt tweaks so answers paraphrase
  instead of quoting, with a *little* warmth or wit — sparingly, not quirky every
  answer. Constraint: must still pass all 15 eval questions (re-run eval after the
  prompt change; add eval assertions for "not a verbatim CV quote" where feasible).
  *(opened 2026-10-11, post-launch feedback)*

- **chat-layer step 7** — remaining after launch (needs user approval, CV repo): add
  the bot as a CV project line and a "Live-Demo" link in AI-job Anschreiben (spec
  §14). Rebuild the CV PDFs: the master now says "KTmfk" but the published PDF still
  says "KTMFK".

## Done this session (2026-10-11)

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
