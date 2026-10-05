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
- Last swept: **2026-09-16** (initialised).

---

## Open — S1 (blocker / broken demo)

_(none yet)_

---

## Open — S2 (UX gap, polish, deferred decisions)

- **images-placeholder** — 8 image slots defined in `content/de.md` Anhang. All
  placeholders until real files land.

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

- **cv-bullet-nx-motion** — closed, won't-fix-here. CV `lebenslauf.json` line 44 already
  says "Gelenke in PTC Creo"; "NX Motion" does not appear. Site and CV agree.
- **ktmfk-application-unknown** — closed, confirmed absent. Read the full CV this
  session: no ski-roller, no named application; the bullets say "Baugruppen". The
  invented term stays out. Reopen only if the user supplies a real application.
- **profil-keywords-lost** — closed by user. `profil.html` carries the Kenntnisse
  table and language levels; the homepage intentionally does not.
- **weekly-digest-private** — closed. Entry dropped from `projekte.html` → Werkzeuge;
  replaced by two entries the user does want shown: Career-Ops (private Go dashboard +
  custom CV-writing skills) and the self-talk German coach. Both marked "Repository
  privat — gern zeige ich es im Gespräch."
- **palette-claude-tell** — user reaction: the cream `#F5F2EB` + terracotta `#B8473A`
  reads as "something Claude made". Replaced across all 7 pages with **Tinte &
  Zederngrün** (paper `#F3F4F1`, accent `#2F5D46` light / `#8FB8A3` dark; WCAG AA
  verified 5.8:1 minimum). Decision method: user reacted to a local comparison page
  with 4 directions rendered on real content — brief §6 method ("reacting is possible
  where specifying is not"), not hex codes in chat.
- **italic-serif-tell** — all display italics removed (claim, metric-line,
  section-note, jump-metric) — the "italic serif display" slop rule. Serif stays for
  headings, upright. Brand mark de-italicised and turned into a home link on every
  page (was a dead `<span>`; fixes the "can't get back home" complaint).
- **structure-strip-down** — homepage cut from 5 sections to hero + 3 case studies +
  Über mich + Kontakt (the "holes" complaint). Hackathons and Engagement moved to
  `projekte.html`, which also gained a Kontakt block so its nav link stops jumping to
  the bottom of the homepage. Two SVG/PNG assets (`mindmap`, `digidorf`, `tea-team`,
  `gokart`) moved with them.

---

## Archived (older sweeps, compressed)

_(empty — populates over time as one-line entries per sweep.)_
