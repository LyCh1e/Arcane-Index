---
type: meta
title: "Hot Cache"
updated: 2026-05-11T00:00:00
tags: [meta, hot-cache]
---

# Recent Context

## Last Updated

2026-05-11. Session: ICT2216 Labs 1 & 2 fully ingested — Docker Compose, SecurityRAT, secure software requirements framework.

## Key Recent Facts

- **ICT2216 Lab 1**: Docker Compose fundamentals — four-service stack (Nginx port 80, MySQL 8.0 with bind-mount volume, Git HTTP server port 3000, Selenium Grid hub port 4444 + Chrome/Firefox nodes). Compose file structure: services, networks, volumes, configs, secrets. Default bridge network lets services reach each other by service name.
- **ICT2216 Lab 2**: SecurityRAT (OWASP) — Docker Compose stack (MariaDB 10.7.3 + Spring Boot v1.8.5); runs at `localhost:9002`; default creds `admin/admin`. Loads OWASP ASVS 3.0.1 SQL dump via `dumpRequirements.sh`. Declare artifact type → get tailored ASVS requirement list → mark Fulfilled/Not/N/A → export to issue tracker.
- **Secure requirements framework**: CIA triad (Confidentiality, Integrity, Availability) + AAA triad (Authentication, Authorisation, Accountability). Each pillar: identify asset/actor → identify risk → define requirement.
- **CRLF gotcha**: Windows git checkout adds `\r\n` to shell scripts; Linux containers read `#!/bin/sh\r` as invalid interpreter → "file not found". Fix: `docker exec ... sed -i 's/\r$//'` — must use PowerShell, not Git Bash (Git Bash translates `/var/` → `C:/Git/var/`).

## Domain Summaries

**Secure Software Development** (ICT2216): Security requirements derived from CIA + AAA pillars. OWASP ASVS provides tiered verification (Level 1–3). SecurityRAT automates requirement selection. Docker Compose is the primary deployment tool across all labs. Windows Docker deployments require CRLF-to-LF conversion for shell scripts; use PowerShell for `docker exec` with Linux paths.

**Software Engineering** (ICT2113 + INF1009): Requirements Engineering covers the full RE lifecycle — BCIC analysis, PS/SRS documents, McCall's quality model (3 perspectives, 11 features), iRTM for traceability. Lightweight RCM covers User Stories (3C's, INVEST, Connextra) and UseCase 2.0 (parent-UC, Stories, Slices, 8-step process). OOP covers the 4 pillars with Java/C++ comparison, OOP relationships (Association/Aggregation/Composition), and UML class diagrams.

**Computer Science** (INF1008): Algorithm complexity from Big-Oh through Master Theorem. Data structures from arrays to B-Trees with a full complexity comparison table. Sorting (Bubble/Selection/Insertion/Merge/Quick) and string algorithms (Brute Force/KMP/Boyer-Moore) with when-to-use guidance. Graph algorithms: DFS/BFS/Topological Sort, MST (Prim's vs Kruskal's), shortest paths (Dijkstra vs Bellman-Ford).

**Mobile Development** (INF2007): Android OS stack, 4 app components, Activity lifecycle. Jetpack Compose declarative UI with recomposition and state hoisting. Full MVVM architecture (UI → ViewModel → Repository → Room/Retrofit). Kotlin coroutines (launch/async, Dispatchers, Structured Concurrency), Flow/StateFlow, Hilt DI, Retrofit, WorkManager.

**HCI** (INF2002): Definition, UI vs UX distinction. History from Memex (1945) to ubiquitous computing (Weiser 1991) to touchscreens. Real-world design failures (Air Inter 148, Anton Yelchin, Hawaii missile alert). UCD principles, personas, paper prototyping. Needfinding methods (observation, ethnography, surveys/Likert/Semantic Differential, interviews, focus groups). Task analysis (HTA, TDH with XOR/AND/OR, knowledge-based / declarative vs procedural).

## Recent Changes

- Created: `wiki/sources/ICT2216-secure-software-development.md`
- Created: `wiki/concepts/secure-software-requirements.md`
- Created: `wiki/concepts/docker-compose.md`
- Created: `wiki/resources/securityrat.md`
- Created: `wiki/learning/docker-windows-crlf.md`
- Created: `wiki/examples/ict2216-lab1-docker-compose.md`
- Created: `wiki/examples/ict2216-lab2-securityrat.md`
- Updated: `wiki/examples/_index.md`, `wiki/index.md`, `wiki/log.md`

## Active Threads

- ICT2216 Lab 2 Steps 5–7 (browser UI / artifact exploration) — user to complete independently
- Next: create learning/study notes (flashcard-style summaries for exam prep)
- Gap: no synthesis page connecting ICT2113 RE elicitation ↔ ICT2216 CIA+AAA (McCall's Integrity maps directly to CIA Integrity)
- Gap: no synthesis page connecting ICT2113 RE elicitation ↔ INF2002 HCI needfinding
- Gap: no page on SOLID + Android architecture synthesis (how DIP enables Hilt)
