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
| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-10-20 |
| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-10-20 |
| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-10-20 |

If a publish ever returns a different URL than the one listed here (for example, if an artefact was deleted), replace the affected row above with the new URL so future runs update the correct page. If a module is removed from `study-notes/index.md`, leave its row here untouched — never delete an Artefact page automatically.

> [!warning] This file was found out of sync with the live pages on 2026-10-07
> Before publishing on 2026-10-07, the live content at all three URLs above was read and found to differ from what the "Topic Rotation History" below had recorded — each page had already moved one run ahead of this file (likely from a run that published successfully but was never logged here). The actual live topics found at that point are recorded below as an "(unlogged run, found live)" entry per module, dated 2026-10-06 to match the gap, so future runs rotate away from them too. On 2026-10-08, the three live pages were re-read before topic selection and confirmed to match the "run 25" entries below exactly — the file is back in sync. **Future runs: always treat the actual live Artefact content as the source of truth for "what was covered most recently" if it ever disagrees with this file — read the live page via the Artifact tool's `read` action before finalising today's topic selection, not just this log.**

> [!warning] This file was found out of sync with the live pages again on 2026-10-15
> `study-notes/log.md` last recorded a run on 2026-10-12 ("run 28"), but no entry existed for 2026-10-13 or 2026-10-14. Before selecting today's topics, all three live Artefact pages were read (per the standing instruction above) and found to already be one run ahead of this file's "run 28" entries — a run had evidently published successfully on one of those two days without this file being updated afterwards (same self-healing gap pattern as 2026-10-07). The actual live topics found are recorded below as an "(unlogged run, found live — 2026-10-13/14)" entry per module, so today's and future runs rotate away from them too. The pending-log-update note for 2026-10-11 (run 27) in the Claude project, by contrast, was already reconciled into this file before this run (its topics appear below as the dated 2026-10-11 entry) and needed no further action.

> [!note] Checked against live pages on 2026-10-16
> Before selecting today's topics, all three live Artefact pages were read and confirmed to match this file's "run 30" (2026-10-15) entries exactly — no unlogged gap this time, file was in sync.

> [!note] Evening run (run 32) on 2026-10-16
> This file already recorded a "run 31" for 2026-10-16 (an earlier, unlogged manual run that day, per `last_fired_at`/mtime evidence — not from this scheduled task, which fires once daily at 22:00 SGT / 14:00 UTC). Before selecting this run's topics, all three live Artefact pages were re-read and confirmed to match the "run 31" entries exactly, so today's rotation correctly avoided those topics on top of the usual ~5-run history. This is the first time two runs have landed on the same calendar date — both are kept as separate dated entries below (run 31, run 32) rather than merged.

> [!note] Checked against live pages on 2026-10-18 (run 33)
> No run was recorded for 2026-10-17. Before selecting today's topics, all three live Artefact pages were read via the Artifact tool and confirmed to match this file's "run 32" (2026-10-16) entries exactly — no unlogged gap, file was in sync.

---


> [!note] Checked against live pages before run 34 on 2026-10-18
> Before selecting this run's topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file's "run 33" (2026-10-18) entries exactly. This scheduled run (trigger "Daily Readings", 09:36 UTC) is a second run on the same calendar date as the earlier manual/unlogged run 33 — both are kept as separate dated entries, following the same pattern as runs 31/32 on 2026-10-16.


> [!note] Checked against live pages before run 35 on 2026-10-18
> Before selecting this run’s topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file’s "run 34" (2026-10-18) entries exactly. This scheduled run (trigger "Daily Readings") is a third run on the same calendar date, following the same pattern as runs 31/32 on 2026-10-16 and runs 33/34 earlier today — all kept as separate dated entries.

> [!note] Checked against live pages before run 36 on 2026-10-19
> Before selecting this run's topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file's "run 35" (2026-10-18) entries exactly — no unlogged gap, file was in sync. This scheduled run (trigger "Daily Readings") is the first run on 2026-10-19.

> [!note] Checked against live pages before run 37 on 2026-10-19
> Before selecting this run's topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file's "run 36" (2026-10-19) entries exactly — no unlogged gap, file was in sync. This scheduled run (trigger "Daily Readings") is a second run on 2026-10-19, following the same same-day pattern as runs 31/32 on 2026-10-16 and runs 33/34/35 on 2026-10-18.


> [!note] Checked against live pages before run 38 on 2026-10-20
> Before selecting this run's topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file's "run 37" (2026-10-19) entries exactly — no unlogged gap, file was in sync. This scheduled run (trigger "Daily Readings") is the first run on 2026-10-20.

## Topic Rotation History

Tracks roughly the last 5 runs' subtopics per module, so the tutor agent can avoid repeating recent content without needing to scan local daily files (there are none). Each run appends its selections to the relevant module's list and prunes older entries down to about 5. A module new to the index simply starts with an empty list here.

### ICT3112
- 2026-10-18 (run 34): The Error → Defect → Failure Chain & Retesting vs Regression Testing; Boundary Value Analysis (BVA) & Use Case Testing; Software Reliability Metrics — Core Metrics & the Musa Reliability Models
- 2026-10-18 (run 35): Control Flow Graphs (CFGs) & the Factorial Reference Example; Eight Good Testing Practices & Goodhart's Law in Testing; Reliability Metrics Extras — Execution Time vs Calendar Time, Defect Density & Customer-Facing Metrics
- 2026-10-19 (run 36): Axiomatic Semantics (Hoare Logic) — Hoare Triples & the Six Inference Rules; Weakest Precondition (WP) Calculus & Loop Invariants; Coverage Criteria — the Hierarchy
- 2026-10-19 (run 37): The Seven ISTQB Principles; Cyclomatic Complexity (McCabe) & Basis Path Testing; Decision Table Testing
- 2026-10-20 (run 38): Static vs Dynamic V&V & The V-Model; Equivalence Partitioning (EP) & Comparing Whitebox vs Blackbox Testing; Static Testing Techniques (Formality Spectrum) & LCSAJ
### ICT3113
- 2026-10-18 (run 34): Response Time Fundamentals (R = W + S) & the Fan-Out Formula; Multi-Server Queues — M/M/c: Structure, Key Formula & One Fast Server vs Many Slow Servers; The Kingman Formula (G/G/1) & Sakasegawa's G/G/c Approximation
- 2026-10-18 (run 35): The Core Loop & User Perception Thresholds; Open vs Closed Systems; The Four Sources Framework & the Observation Boundary Effect
- 2026-10-19 (run 36): Workload Identification — Three Components & the Estimation Methodology; Interactive Systems — Open vs Closed & the Interactive Response Time Law; Variability in Practice — the Coefficient of Variation
- 2026-10-19 (run 37): The Utilisation Law (U = X×S) & the Utilisation–Response Time Curve; Little's Law & the M/M/1 Single-Server Queue; Bottleneck Analysis — Capacity Bottleneck vs Congestion Hotspot & the Three Levers
- 2026-10-20 (run 38): When to Optimise (3 Conditions) & Classical Optimisation Techniques; Percentiles, Tail Latency & SLI/SLO/SLA; Peak vs Average Workload & Common Workload Mistakes
### INF2005
- 2026-10-18 (run 34): Diffie–Hellman Key Exchange; Steganography Techniques — LSB Algorithms, Bit Planes & BPCS; Biometric Authentication & Authorisation Models (DAC/RBAC/MAC)
- 2026-10-18 (run 35): One-Time Pad (OTP) & Random Number Generators; Asymmetric Crypto Foundations — Key Pair Roles & Confidentiality vs Authentication; Steganalysis & Hacker Types
- 2026-10-19 (run 36): Ethical Hacking — the Defining Line & Legal Framework; Pen Testing Approaches & the Pentest Report; Steganography vs Cryptography — the Core Process
- 2026-10-19 (run 37): The CIA Triad & the Threat Model (Alice, Bob, Eve); RSA & One-Way Functions; The 6-Stage Hacking Process
- 2026-10-20 (run 38): Classical Ciphers & Kerckhoffs's Principle; Hash Functions, Digital Signatures & the Birthday Attack; Authentication Categories (Three Factors) & Password Security
