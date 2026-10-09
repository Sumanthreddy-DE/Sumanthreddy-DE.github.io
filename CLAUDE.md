# Sumanthreddy-DE.github.io

[One sentence: what this system does.]

## Navigation

| Resource | Purpose |
|---|---|
| `ARCHITECTURE.md` | Domain model, layers, dependency rules |
| `docs/design-docs/core-beliefs.md` | Non-negotiable operating principles |
| **`docs/exec-plans/design-docs/2026-09-16-redesign-brief.md`** | **Audience, positioning and content spine for the redesign. Read before any design work.** Private: lives in the nested `portfolio-private` repo, not published. |
| `docs/design-docs/index.md` | All design docs + verification status |
| `docs/exec-plans/active/` | In-progress execution plans |
| `docs/exec-plans/completed/` | Finished plans (historical record) |
| `docs/references/` | External API docs, vendor llms.txt |

## Stack

- **Language**: 
- **Framework**: 
- **Database**: 
- **Package manager**: 

## Dev commands

```bash
# Dev:    
# Test:   
# Lint:   
# Build:  
```

## Rules (project overrides)

- **Redesign work**: Before any layout, palette, typography or copy decision, read `docs/exec-plans/design-docs/2026-09-16-redesign-brief.md`. Audience, positioning and content spine are already decided there — do not re-derive them, and do not design against a different audience. Its §7 lists three conflicts that are still open. The brief was written from session context, not from this repo — treat its `[verified]` claims as leads and re-check them on disk.
- **Design plugin order**: `ui-ux-pro-max` first (chooses the direction), `impeccable` second (audits what was built). Not the reverse.
- **exec-plans**: Plans save to `docs/exec-plans/active/YYYY-MM-DD-<slug>.md`. This overrides the write-plan skill default (`docs/superpowers/plans/`). Move to `docs/exec-plans/completed/` when task is done. `docs/exec-plans/` is its own private git repo (`portfolio-private`): commit plans from inside that folder; the site repo ignores it.
- **lint**: Before committing, run `bash scripts/lint-arch.sh`. Do not suppress violations without an inline comment explaining why.
- **design-docs/index.md**: Add a row whenever a new design doc is created. Keep Status column current (✓ current / ⚠ needs review / ✗ outdated).
