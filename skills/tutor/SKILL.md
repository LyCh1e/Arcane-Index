---
name: tutor
description: >
  Generates a daily study reading note for ICT3112, ICT3113, and INF2005 with a
  20-question MCQ quiz. Topics rotate each day so no two consecutive notes
  repeat the same subtopics. Output is saved to
  `study notes/daily-reads/YYYY-MM-DD.md`.
  Triggers on: "tutor", "daily read", "create today's study note",
  "generate daily note", or called automatically by the 23:00 cron job.
allowed-tools: Read Write Edit Glob Grep Bash
---

# tutor: Daily Study Note Generator

Produces one exam-focused daily reading note covering all three active modules,
plus a 20-question MCQ quiz. Runs automatically at 23:00 each night, or on
demand.

---

## How It Works

This skill dispatches the **tutor** agent (defined in `agents/tutor.md`).
The agent handles topic selection, content synthesis, quiz generation, and file
writing. See `agents/tutor.md` for the full step-by-step process.

---

## Quick Manual Run

To generate today's daily note immediately (outside the scheduled run):

> Tell Claude: **"create today's daily read"** or **"run tutor"**

Claude will invoke the tutor agent, which reads your study notes, selects fresh
topics, writes the reading note, and saves it to
`study notes/daily-reads/YYYY-MM-DD.md`.

---

## Schedule

The tutor runs automatically every night at **23:00 local time** via the
scheduled cloud agent configured in this vault. The cron expression is
`0 23 * * *`.

If you need to change the time, update the schedule via `/schedule` and
modify the time in `agents/tutor.md`'s description.

---

## Output Location

All daily reads are saved in:

```
study notes/daily-reads/
  2026-09-23.md
  2026-09-24.md
  ...
```

Each file is a self-contained daily reading session with:
- Topics covered (frontmatter + summary table)
- Explanations for each subtopic (~200–300 words each)
- 20-question MCQ quiz targeting today's topics
- Collapsible answers callout

---

## Topic Rotation Logic

The tutor reads the last 5 daily reads to build a "recently covered" set.
It then picks 2–3 subtopics per module that have NOT been covered recently,
rotating through the full syllabus over time so all topics are revisited
periodically.

---

## Modules Covered

| Module | Title | Topics |
|--------|-------|--------|
| ICT3112 | Software Verification and Validation | V&V fundamentals, V-Model, ISTQB, Reliability, Static analysis, Whitebox (CFG/coverage/cyclomatic), Blackbox (EP/BVA/decision tables/state transition) |
| ICT3113 | Performance Optimisation and Design | Performance metrics, Utilisation law, Little's Law, M/M/1, M/M/c, Operational laws, Bottleneck analysis, Kingman formula, Response Time Law, JMeter |
| INF2005 | Cyber Security Fundamentals | CIA triad, Symmetric crypto, Asymmetric crypto (RSA/DH), Hashing, Digital signatures, Cryptanalysis, Steganography, Access control, Ethical hacking |
