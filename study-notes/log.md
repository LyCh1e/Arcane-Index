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
| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-10-12 |
| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-10-12 |
| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-10-12 |

If a publish ever returns a different URL than the one listed here (for example, if an artefact was deleted), replace the affected row above with the new URL so future runs update the correct page. If a module is removed from `study-notes/index.md`, leave its row here untouched — never delete an Artefact page automatically.

> [!warning] This file was found out of sync with the live pages on 2026-10-07
> Before publishing on 2026-10-07, the live content at all three URLs above was read and found to differ from what the "Topic Rotation History" below had recorded — each page had already moved one run ahead of this file (likely from a run that published successfully but was never logged here). The actual live topics found at that point are recorded below as an "(unlogged run, found live)" entry per module, dated 2026-10-06 to match the gap, so future runs rotate away from them too. On 2026-10-08, the three live pages were re-read before topic selection and confirmed to match the "run 25" entries below exactly — the file is back in sync. **Future runs: always treat the actual live Artefact content as the source of truth for "what was covered most recently" if it ever disagrees with this file — read the live page via the Artifact tool's `read` action before finalising today's topic selection, not just this log.**

---

## Topic Rotation History

Tracks roughly the last 5 runs' subtopics per module, so the tutor agent can avoid repeating recent content without needing to scan local daily files (there are none). Each run appends its selections to the relevant module's list and prunes older entries down to about 5. A module new to the index simply starts with an empty list here.

### ICT3112

- 2026-10-07 (run 24): Root Causes of Poor Software Quality — The Six DORA Categories; Verification vs Validation — Core Definitions & Static vs Dynamic V&V; Whitebox vs Blackbox at a Glance — Control/Data Flow Categories & the Five Blackbox Techniques Overview
- 2026-10-07 (run 25): The Seven ISTQB Principles & the Error → Defect → Failure Chain; Cyclomatic Complexity, Basis Path Testing & LCSAJ; Equivalence Partitioning & Decision Table Testing
- 2026-10-08 (run 26): The V-Model, Famous Software Failures (Therac-25, Ariane 5, CrowdStrike) & the Cost of Poor Software Quality; Static Analysis — Why It Matters, Data Flow Defect Classes & When It Runs; Retesting vs Regression Testing & Comparing Whitebox vs Blackbox Testing
- 2026-10-11 (run 27): Four Testing Levels & the Testing Pyramid; Reliability Core Metrics (MTTF/MTTR/MTBF) & Execution vs Calendar Time; State Transition Testing
- 2026-10-12 (run 28): Control Flow Graphs (CFGs) & the Coverage Criteria Hierarchy; Use Case Testing & Boundary Value Analysis (BVA); The Musa Reliability Models — Basic & Logarithmic

### ICT3113

- 2026-10-07 (run 24): Workload Identification — Components, Estimation Methodology (Decomposition Chain) & Common Workload Mistakes; Worked Examples — Bottleneck Analysis (Wafer Fab E.4.3/E.4.4) & the Kingman Formula in Numbers (E.4.6); Worked Examples — Forced Flow, Service Demand & Interactive Response Time (E.4.1/E.4.2/E.4.5)
- 2026-10-07 (run 25): Little's Law & the Queueing Theory Foundations (Key Symbols, Observation Boundary Effect, M/M/1); Utilisation Law & the Utilisation–Response-Time Curve; Bottleneck Analysis — Capacity Bottlenecks, Congestion Hotspots & the Three Levers
- 2026-10-08 (run 26): Percentiles, Tail Latency & SLI/SLO/SLA; Peak vs Average — Workload Planning for the Worst Credible Load (incl. the Taylor Swift Case); The Running Case Variability Diagnosis (Cs² ≈ 34) & Wafer Fab LITHO-02
- 2026-10-11 (run 27): Six Properties of a Good Metric (LRRECI) & Three Classes of Metrics; One Fast Server vs Many Slow Servers & the API Tier Worked Example; The Operational Laws — Forced Flow & Service Demand
- 2026-10-12 (run 28): Response Time (R = W + S) & Why the Tail Matters — the Fan-Out Formula; Multi-Server Queues — M/M/c Structure & the Key Formula; Variability — Coefficient of Variation, the Kingman Formula & Sakasegawa's G/G/c Approximation

### INF2005

- 2026-10-07 (run 24): Steganography vs Cryptography & The Core Process (Payload/Cover/Stego Object); Access Control Fundamentals — The Three-Stage Pipeline & the Three Factors (KTB); Common Exam Mistakes — A Cross-Topic Revision Round-Up
- 2026-10-07 (run 25): Foundations — The CIA Triad, the Threat Model (Alice/Bob/Eve) & Types of Cryptography; The Six-Stage Ethical Hacking Process & Hacker Types; RSA & One-Way Functions — Asymmetric Crypto Core
- 2026-10-08 (run 26): Classical Ciphers (Substitution & Transposition) & Kerckhoffs's Principle; Hash Functions, Digital Signatures & the Birthday Attack; Password Security — Secure Storage, Password Attacks & the Passphrase Technique
- 2026-10-11 (run 27): Modern Symmetric Algorithms — DES, 3DES & AES; Cryptanalysis — Attacking Ciphers; Graphical & Token Authentication
- 2026-10-12 (run 28): Diffie–Hellman Key Exchange & the Key Distribution Problem; Steganography in Depth — LSB Algorithms, Bit Planes & BPCS; Biometric Authentication & Authorisation Models (DAC/RBAC/MAC)
