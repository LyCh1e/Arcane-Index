---
name: notes-maker
description: >
  Generates a fresh ~10-minute daily reading (3 lecture subtopics plus a
  lab/practical topic, when lab material exists) + 20-question MCQ quiz
  for every module listed in `study-notes/index.md`'s "Create Study Notes
  For" table, and publishes each straight to that module's permanent
  hosted Artifact page — no Markdown or HTML file is written to the
  vault. Topics rotate per module so no two consecutive runs repeat the
  same subtopics, and the persistent Artifact URLs stay the same forever —
  both are tracked in one file, `study-notes/log.md`. Every run
  republishes to those same links rather than creating new pages, and
  does a one-time first publish for any module newly added to the index.
  To change which courses get a daily read, edit the table in
  `study-notes/index.md` — nothing in this skill or the agent needs to
  change.
  Triggers on: "notes-maker", "tutor", "daily read", "create today's study
  note", "generate daily note", or called automatically by this project's
  scheduled task.
allowed-tools: Read Write Edit Glob Grep Bash Artifact
---

# notes-maker: Daily Study Note Generator

Produces an exam-focused daily reading + quiz session for every module
listed in the vault's course index — fresh reading content (3 lecture
subtopics, plus a lab/practical topic whenever that module has lab
material under `wiki/examples/`) followed immediately by a 20-question
MCQ quiz testing only that module's content. Each page targets roughly
10 minutes of reading, giving room for the lab section alongside the
usual lecture coverage. Runs on demand, or automatically via this
project's scheduled task.

There is no local file output. Each module has one permanent, bookmarkable
Artifact page; every run rebuilds that module's content and republishes it
to the same URL, so a phone bookmark never needs to change even though the
content behind it does.

Read-then-test is the whole point of the format: open a module's page, read
the reading section at the top, then answer the 20 questions underneath it —
one continuous scrollable page (reading notes, then all 20 questions, then
the results summary — no gated "Start quiz" screen, nothing hidden). It's
built to work on a phone: scroll, tap an answer, see instant feedback, keep
going. The notes and all 20 questions are written straight into the page's
HTML at build time, so they show up even in contexts that don't run
JavaScript — JavaScript only adds the tap-to-check interactivity on top.

---

## Which modules get a daily read

Tutor never hardcodes a module list. It reads the **"Create Study Notes
For"** table in `study-notes/index.md` at the start of every run and
generates one page per row. To add, remove, or rename a module:

> Edit the table in `study-notes/index.md` — add a row (Module, Title,
> Source Pattern, Notes File, Formula Sheet, Auto-Update) to start
> generating daily reads for it, or delete a row to stop. Nothing in
> `agents/tutor.md` or this skill needs to change.

Adding a new row means tutor will publish a **brand-new** Artifact page for
it on the next run (a fresh link, recorded automatically in
`study-notes/log.md`) — every module already in the index keeps its
existing link, refreshed in place as usual. Deleting a row just stops that
module's daily generation; its existing Artifact page and log entry are
left alone, not deleted.

---

## How It Works

This skill dispatches the **tutor** agent (defined in `agents/tutor.md`).
The agent handles: reading the course index, and then independently for
each module in it — topic selection (lecture subtopics plus a lab topic,
when available), content synthesis, quiz generation, Artifact page build,
and publishing (first-time or republish) to that module's URL. See
`agents/tutor.md` for the full step-by-step process.

---

## Quick Manual Run

To regenerate today's quiz pages immediately (outside the scheduled run):

> Tell Claude: **"create today's daily read"**, **"run tutor"**, or **"run notes-maker"**

Claude will invoke the tutor agent, which reads `study-notes/index.md` for
the current module list, then for each one reads its study notes (and any
lab/practical write-ups under `wiki/examples/`), selects 3 fresh lecture
subtopics plus 1 lab topic (when lab material exists for that module),
writes the reading + 20-question quiz content, and publishes it to that
module's Artifact URL (existing or newly created).

---

## Output — One Permanent Artifact Page Per Module (no vault files)

Nothing is written under `study-notes/daily-reads/` or anywhere else in the
vault for the daily content itself. The only persistent records are:

```
study-notes/index.md    ← the course list (read-only to tutor)
study-notes/log.md      ← one permanent Artifact URL + topic history, per module
```

Each module's Artifact page is a self-contained reading + quiz session,
rebuilt fresh every run:
- A notes section covering that module's 3 lecture subtopics for today
  (headings, worked examples, "Watch out" callouts, mnemonics), plus a
  lab/practical section drawn from that module's `wiki/examples/` write-ups
  whenever lab material exists for it. Together these target roughly 10
  minutes of reading.
- The full 20-question quiz rendered below it on the same page — every
  question visible, answerable in any order, with instant feedback per
  question, a live sticky score readout, and a results block at the bottom
  (score, percentage, a review of anything missed, and a "Retake quiz"
  button) that updates as you go.

No screens to switch between, and it's designed to be used comfortably on a
phone — that's the whole point of publishing to a permanent link rather
than a file: existing bookmarks work forever, and always show the latest
content.

---

## Topic Rotation Logic

For each module independently, the tutor reads the "Topic Rotation History"
section of `study-notes/log.md` to build a "recently covered" set (roughly
the last 5 runs). It then picks 3
subtopics for that module that have NOT been covered recently, rotating
through the full syllabus over time so all topics are revisited
periodically. Rotation is tracked per module — one module's history never
affects what another selects. After each run, today's selections are
appended to that same file (older entries pruned so it stays small). A
module that's new to the index simply starts with an empty history.

---

## Modules Covered

Not tracked here — see the live list in `study-notes/index.md`'s "Create
Study Notes For" table, which is the single source of truth for which
modules tutor generates daily reads for.
