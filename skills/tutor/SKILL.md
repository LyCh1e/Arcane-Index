---
name: tutor
description: >
  Generates three separate daily study files — one per module (ICT3112,
  ICT3113, INF2005) — each with fresh reading content followed by its own
  full 20-question MCQ quiz, plus a companion interactive HTML quiz per
  module. Topics rotate per module so no two consecutive appearances of that
  module repeat the same subtopics. Output is saved to
  `study notes/daily-reads/YYYY-MM-DD-<MODULE>.md` and
  `study notes/daily-reads/YYYY-MM-DD-<MODULE>.html`.
  Triggers on: "tutor", "daily read", "create today's study note",
  "generate daily note", or called automatically by the 23:00 cron job.
allowed-tools: Read Write Edit Glob Grep Bash
---

# tutor: Daily Study Note Generator

Produces three exam-focused daily reading notes — one per active module —
each followed immediately by its own 20-question MCQ quiz testing only that
module's content, and a matching interactive HTML quiz. Runs automatically
at 23:00 each night, or on demand.

Read-then-test is the whole point of the format: open a module's `.md` file,
read the reading section at the top, then answer the 20 questions
underneath it — or open the module's `.html` file, which opens on the same
reading content first (a "Start the quiz →" button sits at the end of it)
and only then moves into the interactive quiz with instant right/wrong
feedback. The HTML file never skips straight to Q1.

---

## How It Works

This skill dispatches the **tutor** agent (defined in `agents/tutor.md`).
The agent handles, independently for each module: topic selection, content
synthesis, quiz generation, Markdown file writing, and the companion
interactive HTML build. See `agents/tutor.md` for the full step-by-step
process.

---

## Quick Manual Run

To generate today's three daily notes immediately (outside the scheduled
run):

> Tell Claude: **"create today's daily read"** or **"run tutor"**

Claude will invoke the tutor agent, which — for each of the three modules —
reads that module's study notes, selects 3 fresh subtopics, writes the
reading + 20-question quiz file, and builds the matching interactive HTML
quiz.

---

## Schedule

The tutor runs automatically every night at **23:00 local time** via the
scheduled cloud agent configured in this vault. The cron expression is
`0 23 * * *`.

If you need to change the time, update the schedule via `/schedule` and
modify the time in `agents/tutor.md`'s description.

---

## Output Location

All daily reads are saved in, one pair of files per module per day:

```
study notes/daily-reads/
  2026-09-27-ICT3112.md
  2026-09-27-ICT3112.html
  2026-09-27-ICT3113.md
  2026-09-27-ICT3113.html
  2026-09-27-INF2005.md
  2026-09-27-INF2005.html
  ...
```

Each `.md` file is a self-contained reading + quiz session for one module:
- Topics covered (frontmatter + summary line)
- Explanations for each of that module's 3 subtopics (~200–300 words each)
- A full 20-question MCQ quiz targeting only today's 3 subtopics for that
  module
- Collapsible answers callout

Each `.html` file is the interactive counterpart: it opens on the same
lecture-notes content as the `.md` file (headings, worked examples, "Watch
out" callouts, mnemonics), gated behind a "Start the quiz →" button, then
the same 20 questions one at a time, with instant feedback, a running
score, and a results screen with a review of anything missed plus controls
to retake the quiz or jump back to the notes.

---

## Topic Rotation Logic

For each module independently, the tutor reads that module's last 5 daily
files to build a "recently covered" set. It then picks 3 subtopics for that
module that have NOT been covered recently, rotating through the full
syllabus over time so all topics are revisited periodically. Rotation is
tracked per module — ICT3112's history never affects what INF2005 selects,
and vice versa.

---

## Modules Covered

| Module | Title | Topics |
|--------|-------|--------|
| ICT3112 | Software Verification and Validation | V&V fundamentals, V-Model, ISTQB, Reliability, Static analysis, Whitebox (CFG/coverage/cyclomatic), Blackbox (EP/BVA/decision tables/state transition) |
| ICT3113 | Performance Optimisation and Design | Performance metrics, Utilisation law, Little's Law, M/M/1, M/M/c, Operational laws, Bottleneck analysis, Kingman formula, Response Time Law, JMeter |
| INF2005 | Cyber Security Fundamentals | CIA triad, Symmetric crypto, Asymmetric crypto (RSA/DH), Hashing, Digital signatures, Cryptanalysis, Steganography, Access control, Ethical hacking |
