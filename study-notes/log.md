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
| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-10-04 |
| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-10-04 |
| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-10-04 |

If a publish ever returns a different URL than the one listed here (for example, if an artefact was deleted), replace the affected row above with the new URL so future runs update the correct page. If a module is removed from `study-notes/index.md`, leave its row here untouched — never delete an Artefact page automatically.

---

## Topic Rotation History

Tracks roughly the last 5 runs' subtopics per module, so the tutor agent can avoid repeating recent content without needing to scan local daily files (there are none). Each run appends its selections to the relevant module's list and prunes older entries down to about 5. A module new to the index simply starts with an empty list here.

### ICT3112
- 2026-10-03 (run 17): Static vs Dynamic V&V & the Six DORA Root-Cause Categories; Static Testing Techniques (Formality Spectrum) & Goodhart's Law in Testing; Logarithmic Musa Reliability Model & Defect Density
- 2026-10-04 (run 18): Boundary Value Analysis (BVA) — Rules & Worked Examples; Basic Musa Reliability Model; Whitebox vs Blackbox Testing & Eight Good Testing Practices
- 2026-10-04 (run 19): The Seven ISTQB Principles; The Error–Defect–Failure Chain; Retesting vs Regression Testing
- 2026-10-04 (run 20): V&V Fundamentals — Verification, Validation & the V-Model (incl. Famous Software Failures); Cyclomatic Complexity & Basis Path Testing; LCSAJ — Linear Code Sequence and Jump
- 2026-10-04 (run 21): Static Analysis — Why It Matters, Data Flow Defect Classes & When It Runs; Equivalence Partitioning (EP) & Decision Table Testing; Comparing Whitebox vs Blackbox Testing & the Cost of Poor Software Quality

### ICT3113
- 2026-10-03 (run 17): Classical Optimisation Techniques & the Four Sources Framework; Sakasegawa's G/G/c Approximation & Variability in Practice; Case Study — the Online Service "Three Windows" Diagnosis
- 2026-10-04 (run 18): Multi-Server Queues (M/M/c) — Structure, Formula & One Fast vs Many Slow Servers; Response Time Decomposition (R = W + S) & the Wait vs Service Classification Trick; Workload Sizing Worked Problems — Manufacturing, Healthcare & IT Flash Sale
- 2026-10-04 (run 19): Queueing Notation & the Observation Boundary Effect; Operational Laws — Forced Flow Law & Service Demand Law; Case Study — Wafer Fab LITHO-02 Failure
- 2026-10-04 (run 20): The Utilisation Law (U = X×S) — Derivation, the MRI Scanner Exercises & the Non-linear U-vs-R Relationship; Little's Law & the M/M/1 Single-Server Queue; Bottleneck Analysis — Capacity Bottleneck vs Congestion Hotspot & the Three Levers to Fix a Bottleneck
- 2026-10-04 (run 21): Percentiles, Tail Latency & the SLI/SLO/SLA Hierarchy; Workload Identification & Sizing for Peak; The Kingman Formula (G/G/1) & Coefficient of Variation

### INF2005
- 2026-10-03 (run 17): Random Number Generators & the Key Distribution Problem; LSB Algorithms, Bit Planes & Steganalysis; Authorisation Models (DAC/RBAC/MAC) & Cross-Cutting Controls
- 2026-10-04 (run 18): Diffie–Hellman Key Exchange; BPCS Steganography — Complexity Measure & Algorithm; Biometric Authentication — UDPC Requirements, FAR/TAR & Modality Comparison
- 2026-10-04 (run 19): Asymmetric Crypto Key Roles — Confidentiality vs Authentication (Combined Signing + Sealing); Access Control Fundamentals — The Three-Stage Pipeline, Three Factors & Graphical/Token Authentication; The 6-Stage Ethical Hacking Process
- 2026-10-04 (run 20): Classical Ciphers — Substitution, Transposition & Kerckhoffs's Principle; RSA Key Generation & the One-Way Functions Behind Asymmetric Crypto; Ethical Hacking — Hacker Types (White/Gray/Black Hat) & Pen Testing Approaches (Black Box vs White Box)
- 2026-10-04 (run 21): Foundations — the CIA Triad, Threat Model & Types of Cryptography; Hash Functions, Digital Signatures & the Birthday Attack; Password Security — Storage, Attacks & Passphrases
