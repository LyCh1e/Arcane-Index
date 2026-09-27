---
name: tutor
description: >
  Generates a fresh daily reading + 20-question MCQ quiz for each of three
  modules (ICT3112, ICT3113, INF2005) and publishes each straight to that
  module's permanent hosted Artifact page — no Markdown or HTML file is
  written to the vault. Topics rotate per module so no two consecutive runs
  repeat the same subtopics (tracked in `agents/tutor-topic-history.md`).
  The three persistent Artifact URLs (recorded in
  `agents/tutor-artifact-links.md`) stay the same forever; every run
  republishes to those same links rather than creating new pages.
  Triggers on: "tutor", "daily read", "create today's study note",
  "generate daily note", or called automatically by the 23:00 cron job.
allowed-tools: Read Write Edit Glob Grep Bash Artifact
---

# tutor: Daily Study Note Generator

Produces three exam-focused daily reading + quiz sessions — one per active
module — each with fresh reading content followed immediately by its own
20-question MCQ quiz testing only that module's content. Runs automatically
at 23:00 each night, or on demand.

There is no local file output. Each module has one permanent, bookmarkable
Artifact page; every run rebuilds that module's content and republishes it
to the same URL, so the three phone bookmarks never change even though the
content behind them does, every night.

Read-then-test is the whole point of the format: open a module's page, read
the reading section at the top, then answer the 20 questions underneath it —
one continuous scrollable page (reading notes, then all 20 questions, then
the results summary — no gated "Start quiz" screen, nothing hidden). It's
built to work on a phone: scroll, tap an answer, see instant feedback, keep
going. The notes and all 20 questions are written straight into the page's
HTML at build time, so they show up even in contexts that don't run
JavaScript — JavaScript only adds the tap-to-check interactivity on top.

---

## How It Works

This skill dispatches the **tutor** agent (defined in `agents/tutor.md`).
The agent handles, independently for each module: topic selection, content
synthesis, quiz generation, Artifact page build, and republishing to that
module's existing URL. See `agents/tutor.md` for the full step-by-step
process.

---

## Quick Manual Run

To regenerate today's three quiz pages immediately (outside the scheduled
run):

> Tell Claude: **"create today's daily read"** or **"run tutor"**

Claude will invoke the tutor agent, which — for each of the three modules —
reads that module's study notes, selects 3 fresh subtopics, writes the
reading + 20-question quiz content, and republishes it to that module's
existing Artifact URL.

---

## Schedule

The tutor runs automatically every night at **23:00 local time** via the
scheduled cloud agent configured in this vault. The cron expression is
`0 23 * * *`.

If you need to change the time, update the schedule via `/schedule` and
modify the time in `agents/tutor.md`'s description.

---

## Output — Three Permanent Artifact Pages (no vault files)

Nothing is written under `study-notes/daily-reads/` or anywhere else in the
vault for the daily content itself. The only persistent record is:

```
agents/tutor-artifact-links.md    ← the 3 permanent URLs, one per module
agents/tutor-topic-history.md     ← last ~5 runs' subtopics, per module
```

Each module's Artifact page is a self-contained reading + quiz session,
rebuilt fresh every run:
- A lecture-notes card covering that module's 3 subtopics for today
  (headings, worked examples, "Watch out" callouts, mnemonics).
- The full 20-question quiz rendered below it on the same page — every
  question visible, answerable in any order, with instant feedback per
  question, a live sticky score readout, and a results block at the bottom
  (score, percentage, a review of anything missed, and a "Retake quiz"
  button) that updates as you go.

No screens to switch between, and it's designed to be used comfortably on a
phone — that's the whole point of publishing to a permanent link rather
than a file: the same three bookmarks work forever, and always show
tonight's content.

---

## Topic Rotation Logic

For each module independently, the tutor reads `agents/tutor-topic-history.md`
to build a "recently covered" set (roughly the last 5 runs). It then picks 3
subtopics for that module that have NOT been covered recently, rotating
through the full syllabus over time so all topics are revisited
periodically. Rotation is tracked per module — ICT3112's history never
affects what INF2005 selects, and vice versa. After each run, today's
selections are appended to that same file (older entries pruned so it stays
small).

---

## Modules Covered

| Module | Title | Topics |
|--------|-------|--------|
| ICT3112 | Software Verification and Validation | V&V fundamentals, V-Model, ISTQB, Reliability, Static analysis, Whitebox (CFG/coverage/cyclomatic), Blackbox (EP/BVA/decision tables/state transition) |
| ICT3113 | Performance Optimisation and Design | Performance metrics, Utilisation law, Little's Law, M/M/1, M/M/c, Operational laws, Bottleneck analysis, Kingman formula, Response Time Law, JMeter |
| INF2005 | Cyber Security Fundamentals | CIA triad, Symmetric crypto, Asymmetric crypto (RSA/DH), Hashing, Digital signatures, Cryptanalysis, Steganography, Access control, Ethical hacking |
