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
- Last swept: **2026-10-05** (palette + alignment session archived).

---

## Open — S1 (blocker / broken demo)

_(none yet)_

---

## Open — S2 (UX gap, polish, deferred decisions)

- **images-placeholder** — 8 image slots defined in `content/de.md` Anhang. All
  placeholders until real files land.
- **en-toggle** — user asked for a DE/EN language toggle in the top bar. Deferred
  2026-10-05: the brief's decided line is "German-first, English later", and the
  positioning argument (Mittelstand reads German) still holds. Adding EN doubles the
  copy surface to maintain while the copy is still moving, and the English half is
  where AI tells creep back in. Revisit **after** the images land and the German copy
  has settled. Right shape when we do it: a static `en/` mirror or `lang` swap, not
  a JS toggle — and a session of its own.

---

## Open — S3 (tech debt, deprecations, low-impact polish)

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

_(items currently being worked — move from Open when started, back to Open if paused.)_

---

## Done this session (2026-10-05)

_(empty — swept to Archived below.)_

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
