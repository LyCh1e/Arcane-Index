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
| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-10-15 |
| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-10-15 |
| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-10-15 |

If a publish ever returns a different URL than the one listed here (for example, if an artefact was deleted), replace the affected row above with the new URL so future runs update the correct page. If a module is removed from `study-notes/index.md`, leave its row here untouched — never delete an Artefact page automatically.

> [!warning] This file was found out of sync with the live pages on 2026-10-07
> Before publishing on 2026-10-07, the live content at all three URLs above was read and found to differ from what the "Topic Rotation History" below had recorded — each page had already moved one run ahead of this file (likely from a run that published successfully but was never logged here). The actual live topics found at that point are recorded below as an "(unlogged run, found live)" entry per module, dated 2026-10-06 to match the gap, so future runs rotate away from them too. On 2026-10-08, the three live pages were re-read before topic selection and confirmed to match the "run 25" entries below exactly — the file is back in sync. **Future runs: always treat the actual live Artefact content as the source of truth for "what was covered most recently" if it ever disagrees with this file — read the live page via the Artifact tool's `read` action before finalising today's topic selection, not just this log.**

> [!warning] This file was found out of sync with the live pages again on 2026-10-15
> `study-notes/log.md` last recorded a run on 2026-10-12 ("run 28"), but no entry existed for 2026-10-13 or 2026-10-14. Before selecting today's topics, all three live Artefact pages were read (per the standing instruction above) and found to already be one run ahead of this file's "run 28" entries — a run had evidently published successfully on one of those two days without this file being updated afterwards (same self-healing gap pattern as 2026-10-07). The actual live topics found are recorded below as an "(unlogged run, found live — 2026-10-13/14)" entry per module, so today's and future runs rotate away from them too. The pending-log-update note for 2026-10-11 (run 27) in the Claude project, by contrast, was already reconciled into this file before this run (its topics appear below as the dated 2026-10-11 entry) and needed no further action.

---

## Topic Rotation History

Tracks roughly the last 5 runs' subtopics per module, so the tutor agent can avoid repeating recent content without needing to scan local daily files (there are none). Each run appends its selections to the relevant module's list and prunes older entries down to about 5. A module new to the index simply starts with an empty list here.

### ICT3112

- 2026-10-08 (run 26): The V-Model, Famous Software Failures (Therac-25, Ariane 5, CrowdStrike) & the Cost of Poor Software Quality; Static Analysis — Why It Matters, Data Flow Defect Classes & When It Runs; Retesting vs Regression Testing & Comparing Whitebox vs Blackbox Testing
- 2026-10-11 (run 27): Four Testing Levels & the Testing Pyramid; Reliability Core Metrics (MTTF/MTTR/MTBF) & Execution vs Calendar Time; State Transition Testing
- 2026-10-12 (run 28): Control Flow Graphs (CFGs) & the Coverage Criteria Hierarchy; Use Case Testing & Boundary Value Analysis (BVA); The Musa Reliability Models — Basic & Logarithmic
- 2026-10-13/14 (unlogged run, found live): Eight Good Testing Practices & Goodhart's Law; Defect Density & Customer-Facing Metrics; Coverage Criteria in Detail
- 2026-10-15 (run 30): Static Testing Techniques — The Formality Spectrum; Coverage Criteria — The Complete Hierarchy at a Glance; Axiomatic Semantics (Hoare Logic) — Hoare Triples & the Six Inference Rules

### ICT3113

- 2026-10-08 (run 26): Percentiles, Tail Latency & SLI/SLO/SLA; Peak vs Average — Workload Planning for the Worst Credible Load (incl. the Taylor Swift Case); The Running Case Variability Diagnosis (Cs² ≈ 34) & Wafer Fab LITHO-02
- 2026-10-11 (run 27): Six Properties of a Good Metric (LRRECI) & Three Classes of Metrics; One Fast Server vs Many Slow Servers & the API Tier Worked Example; The Operational Laws — Forced Flow & Service Demand
- 2026-10-12 (run 28): Response Time (R = W + S) & Why the Tail Matters — the Fan-Out Formula; Multi-Server Queues — M/M/c Structure & the Key Formula; Variability — Coefficient of Variation, the Kingman Formula & Sakasegawa's G/G/c Approximation
- 2026-10-13/14 (unlogged run, found live): Performance Engineering Philosophy; User Perception & Open vs Closed Systems; The Four Sources Framework
- 2026-10-15 (run 30): The Interactive Response Time Law; Workload Identification — Three Components & Estimation Methodology (Decomposition Chain); Variability in Practice

### INF2005

- 2026-10-08 (run 26): Classical Ciphers (Substitution & Transposition) & Kerckhoffs's Principle; Hash Functions, Digital Signatures & the Birthday Attack; Password Security — Secure Storage, Password Attacks & the Passphrase Technique
- 2026-10-11 (run 27): Modern Symmetric Algorithms — DES, 3DES & AES; Cryptanalysis — Attacking Ciphers; Graphical & Token Authentication
- 2026-10-12 (run 28): Diffie–Hellman Key Exchange & the Key Distribution Problem; Steganography in Depth — LSB Algorithms, Bit Planes & BPCS; Biometric Authentication & Authorisation Models (DAC/RBAC/MAC)
- 2026-10-13/14 (unlogged run, found live): One-Time Pad & Random Number Generators; Confidentiality vs Authentication — Key Pair Roles; Steganalysis & Cross-Cutting Access Controls
- 2026-10-15 (run 30): The Key Distribution Problem — Why Asymmetric Crypto Exists; Ethical Hacking — The Defining Line & Legal Framework; Pen Testing Approaches
