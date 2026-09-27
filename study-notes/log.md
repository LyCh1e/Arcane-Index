---
type: log
title: "Tutor Agent — Log"
tags: [tutor, log, artifacts, rotation]
---

# Tutor Agent — Log

Single tracking file for the tutor agent's daily-read pipeline: each module's permanent Artifact URL, when it was last published, and its recent topic rotation history (so subtopics aren't repeated across runs). This is the only place the daily content's ongoing state lives — no Markdown or HTML file is written to the vault for it, and `study-notes/index.md` (the course list) is only ever read, never written to.

Every tutor run reads this file first, then updates it at the end: republishing existing links, adding a row for any module newly added to `study-notes/index.md`, and appending today's topic selections.

---

## Artefact Links

Each link is a persistent URL: republishing to the same URL updates the page's content without creating a new artifact or changing the link. Bookmark these on your phone's home screen for one-tap access — the bookmarks never need to change, only the content behind them does.

| Module | Artefact URL | Last Published |
|---|---|---|
| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-09-27 |
| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-09-27 |
| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-09-27 |

If a publish ever returns a different URL than the one listed here (for example, if an artefact was deleted), replace the affected row above with the new URL so future runs update the correct page. If a module is removed from `study-notes/index.md`, leave its row here untouched — never delete an Artefact page automatically.

---

## Topic Rotation History

Tracks roughly the last 5 runs' subtopics per module, so the tutor agent can avoid repeating recent content without needing to scan local daily files (there are none). Each run appends its selections to the relevant module's list and prunes older entries down to about 5. A module new to the index simply starts with an empty list here.

### ICT3112

- 2026-09-27: The Seven ISTQB Principles; Boundary Value Analysis (BVA); Basic Musa Reliability Model

### ICT3113

- 2026-09-27: Response Time, Percentiles and the Tail; Multi-Server Queues (M/M/c); Operational Laws — Forced Flow and Service Demand

### INF2005

- 2026-09-27: Diffie–Hellman Key Exchange; Authentication Factors; Biometric Authentication
