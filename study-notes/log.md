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
| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-10-01 |
| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-10-01 |
| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-10-01 |

If a publish ever returns a different URL than the one listed here (for example, if an artefact was deleted), replace the affected row above with the new URL so future runs update the correct page. If a module is removed from `study-notes/index.md`, leave its row here untouched — never delete an Artefact page automatically.

---

## Topic Rotation History

Tracks roughly the last 5 runs' subtopics per module, so the tutor agent can avoid repeating recent content without needing to scan local daily files (there are none). Each run appends its selections to the relevant module's list and prunes older entries down to about 5. A module new to the index simply starts with an empty list here.

### ICT3112
- 2026-09-29 (run 7): Famous Software Failures & Retesting vs Regression Testing; Error→Defect→Failure Chain & Static Testing Techniques (Formality Spectrum); Customer-Facing Metrics & Goodhart's Law in Testing
- 2026-09-30 (run 8): Static vs Dynamic V&V & The V-Model; Cyclomatic Complexity, Basis Path Testing & LCSAJ; Static Analysis — Why It Matters & When It Runs
- 2026-09-30 (run 9): MTTF, MTTR, MTBF & Availability; Equivalence Partitioning; Decision Table Testing
- 2026-10-01 (run 10): Four Testing Levels & The Testing Pyramid; Whitebox Coverage — Control Flow Graphs & the Coverage Criteria Hierarchy; Use Case Testing & State Transition Testing
- 2026-10-01 (run 11): Root Causes of Poor Quality (DORA) & the Cost of Getting It Wrong; Logarithmic Musa Reliability Model & Defect Density; Coverage Criteria in Detail — Condition, D&C, Multiple Condition & Path/Loop Coverage

### ICT3113
- 2026-09-29 (run 7): User Perception Thresholds & Queueing Theory Foundations (Key Symbols, Observation Boundary Effect); Worked Examples — API Tier (M/M/c) & Bottleneck Diagnosis (Running Case, Wafer Fab); Case Study Summaries — Online Service Three Windows & Wafer Fab LITHO-02
- 2026-09-30 (run 8): Utilisation Law (U = X×S) & the Utilisation–Response Time Curve; Little's Law & the M/M/1 Single-Server Queue; Bottleneck Analysis — Capacity Bottlenecks, Congestion Hotspots & the Three Levers
- 2026-09-30 (run 9): Workload Identification — Components, the Estimation Chain & Peak vs Average; The Kingman Formula (G/G/1) & Coefficient of Variation; SLI/SLO/SLA & the Fan-Out Tail-Latency Problem
- 2026-10-01 (run 10): Performance Engineering Philosophy — The Core Loop & When to Optimise; Metrics Fundamentals — Six Properties of a Good Metric (LRRECI) & Three Classes of Metrics; Interactive Systems — Open vs Closed Systems & the Interactive Response Time Law
- 2026-10-01 (run 11): Classical Optimisation Techniques; The Four Sources Framework; Sakasegawa's G/G/c Approximation & Variability in Practice

### INF2005
- 2026-09-29 (run 7): Types of Cryptography & The Key Distribution Problem; One-Way Functions & Confidentiality vs Authentication (Key Pair Roles); Cross-Cutting Access Controls & The Defining Line in Ethical Hacking
- 2026-09-30 (run 8): Classical Ciphers (Substitution & Transposition) & Kerckhoffs's Principle; RSA — Asymmetric Key Generation; Steganography vs Cryptography, the Core Process & Bit Planes
- 2026-09-30 (run 9): The CIA Triad & the Threat Model (Alice, Bob, Eve); Hash Functions, Digital Signatures & the Birthday Attack; Password Storage & Password-Specific Attacks
- 2026-10-01 (run 10): Modern Symmetric Algorithms (DES/3DES/AES) & the One-Time Pad; Cryptanalysis — Brute Force, Frequency Analysis & Known Plaintext Attacks; Ethical Hacking — Legal Framework, Vulnerability Scanning vs Penetration Testing & The Pentest Report
- 2026-10-01 (run 11): LSB Algorithms, BPCS & Steganalysis; Authorisation Models — DAC, RBAC, MAC & Role Creep; Hacker Types, Pen Testing Approaches & Reconnaissance/Scanning
