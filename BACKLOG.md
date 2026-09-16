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

_(none yet)_

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

## Done this session (2026-09-16)

_(none yet — items move here on close, sweep to Archived at end of session.)_

---

## Archived (older sweeps, compressed)

_(empty — populates over time as one-line entries per sweep.)_
