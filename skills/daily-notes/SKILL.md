---
name: daily-notes
description: >
  Creates a dated daily study-session note for every module tracked in `study-notes/index.md`.
  Reads the index to discover which courses exist, then generates one focused daily note per
  module under `study-notes/daily-reads/`. Each daily note contains a revision agenda, blank
  worked-example slots, and a self-assessment grid — ready to fill in during a study session.
  Triggers on: "create daily notes", "daily study notes", "/daily-notes", "start study session",
  "where are the daily reads".
allowed-tools: Read Write Edit Glob Grep Bash
---

# daily-notes: Generate Daily Study-Session Notes

One command creates a focused, dated study file for every module you are tracking — no manual copying, no lost content.

---

## Step 1 — Read the Module List from the Index

**Always start here.** Read `study-notes/index.md` and locate the **Modules** table (the second table in the file). Extract every row:

| Column | Use |
|--------|-----|
| Module | module code, e.g. `ICT3112` |
| Title  | human-readable name |
| Notes  | path to the full exam-notes file |
| Formula Sheet | path to the formula sheet |

> If the user asks to generate daily notes for a *specific* module only, filter to that row. Otherwise process every row.

---

## Step 2 — Resolve Today's Date

Use the date provided in the system context (`currentDate`). Format as `YYYY-MM-DD`. All output filenames and frontmatter use this date.

---

## Step 3 — Determine the Output Folder

Daily notes live in `study-notes/daily-reads/`. Create the folder if it does not exist:

```bash
mkdir -p "C:/Arcane-Index/study-notes/daily-reads"
```

---

## Step 4 — Check for an Existing Daily Note

For each module, check whether `study-notes/daily-reads/<YYYY-MM-DD>-<MODULE>.md` already exists.

- **Exists** → skip creation, report "already exists" in the summary.
- **Does not exist** → proceed to Step 5.

---

## Step 5 — Read Source Material for the Daily Agenda

Before generating the note, skim the module's exam-notes file to extract:

1. The list of top-level section headings (§1, §2, …).
2. The last three headings — these are the most recently added content and likely the weakest area.

Use these to populate the **Today's Focus** section of the daily note.

---

## Step 6 — Generate the Daily Note

Create the file at `C:/Arcane-Index/study-notes/daily-reads/<YYYY-MM-DD>-<MODULE>.md` using the template below.
Substitute all `<placeholders>` with real values.

```markdown
---
type: daily-note
module: <MODULE_CODE>
title: "<MODULE_CODE> — Daily Study Note"
date: <YYYY-MM-DD>
tags: [daily-note, study-notes, <module-code-lowercase>]
---

# <MODULE_CODE> — Daily Study Note
### <YYYY-MM-DD>

---

## Today's Focus

Suggested based on recently added content — adjust freely.

| Priority | Topic | Source Section |
|----------|-------|---------------|
| 1 | <topic from §N-2> | [[<notes file>]] §N-2 |
| 2 | <topic from §N-1> | [[<notes file>]] §N-1 |
| 3 | <topic from §N>   | [[<notes file>]] §N   |

---

## Revision Checklist

- [ ] Re-read Today's Focus sections in the exam notes
- [ ] Attempt at least two worked examples per topic (see below)
- [ ] Update Self-Assessment grid at the end of this note

---

## Worked Examples

### Example 1 — <topic>

**Question:**

**Working:**

**Answer:**

---

### Example 2 — <topic>

**Question:**

**Working:**

**Answer:**

---

## Quick-Recall Drills

Write the answer from memory, then check against [[<formula sheet>]].

| Formula / Concept | Written from Memory | Correct? |
|-------------------|--------------------:|:--------:|
| | | ☐ |
| | | ☐ |
| | | ☐ |

---

## Self-Assessment

Rate each topic covered today (1 = shaky, 3 = solid):

| Topic | Rating (1–3) | Notes |
|-------|:------------:|-------|
| <topic 1> | | |
| <topic 2> | | |
| <topic 3> | | |

**Session duration:** _____ min  
**Overall confidence:** ☐ Low  ☐ Medium  ☐ High

---

## Open Questions

Things that came up during this session that need follow-up:

- 
```

> **Important — no wiki back-links in daily notes.**  
> Daily note files must **not** contain links to `wiki/index`, `wiki/hot`, `wiki/log`, or any other top-level wiki meta page. Links to the module's own exam-notes and formula sheet (within `study-notes/`) are the only cross-references permitted.

---

## Step 7 — Update the Index (Coverage Log)

After creating all daily notes, append a one-line entry to the **Coverage Summary** date column (if one exists) in `study-notes/index.md`. Do **not** add or modify any wiki back-links in that file beyond those that already exist in the See Also section.

---

## Step 8 — Report

Output a concise summary, e.g.:

```
Daily notes created (2026-09-24):
  ✅ ICT3112 — study-notes/daily-reads/2026-09-24-ICT3112.md
  ✅ ICT3113 — study-notes/daily-reads/2026-09-24-ICT3113.md
  ✅ INF2005 — study-notes/daily-reads/2026-09-24-INF2005.md
```

---

## Rules

- **Always read `study-notes/index.md` first** — this is the sole source of truth for which modules exist.
- **One file per module per date** — never overwrite an existing daily note.
- **No wiki meta back-links** — daily notes link only to files within `study-notes/`. No `[[wiki/index]]`, `[[wiki/hot]]`, or `[[wiki/log]]` links.
- **British English** spelling and grammar throughout.
- **Do not read or modify** anything in `raw/` or `wiki/` — this skill is scoped to `study-notes/` only.
- Keep the daily note lightweight — it is a session worksheet, not a duplicate of the exam notes.
