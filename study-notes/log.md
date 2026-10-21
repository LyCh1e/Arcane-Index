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
| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-10-21 |
| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-10-21 |
| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-10-21 |

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

> [!note] Run 39 on 2026-10-20 (second run today) — lab sections introduced
> Before selecting this run's topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file's "run 38" entries exactly — no unlogged gap, file was in sync. This is a second run on 2026-10-20 (run 38 was the first), following the same same-day pattern as runs 31/32, 33/34/35 and 36/37. This run is also the first to use the updated `claude/daily-reading-generator.py` (MIN_READ_MINUTES raised to 10 earlier today) and the new per-module lab/practical section: each page now carries 3 lecture subtopics plus 1 `[Lab]` topic drawn from `wiki/examples/`, for 4 sections and ~2,000 words total. Lab topics start rotating as their own separate pool per module from this run onward.

> [!note] Presentation-only republishes on 2026-10-20 (after run 39) — Listen control added, then removed
> All three live Artefact pages were republished twice the same day as run 39, both times presentation-only (topics, subtopics, and all 20 questions per module stayed identical to run 39 — no new content was selected, so neither republish is a new numbered run and the "Topic Rotation History" below was left untouched both times). First, a "Listen" read-aloud control (browser text-to-speech, via `claude/daily-reading-generator.py`'s narration feature) was added. Then, at the user's explicit request ("the voice is not good remove it"), that same control was fully removed again — the generator no longer produces it at all. Noted here only so future runs don't mistake the jump in artifact version numbers for an unlogged content gap, and don't reintroduce the narration feature without a fresh decision from the user.

> [!note] Run 40 on 2026-10-20 (third content run today)
> Before selecting this run's topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file's "run 39" entries exactly — no unlogged gap, file was in sync. The two presentation-only republishes logged above (Listen control added then removed) did not change any topics or questions, so this run correctly rotated away from run 39's content, not an intermediate state. All three pages were republished to their existing Artefact URLs (no new URLs created).

> [!note] Presentation-only republishes on 2026-10-20 (after run 40) — quiz option balance fixed
> User feedback: "do not make it obvious, as currently i can easily tell which is the correct answer based on length of the option as the correct answer is usually the longest." Two issues were found and fixed, both presentation-only (topics, subtopics and the 20 question prompts/explanations per module stayed identical to run 40 — only the multiple-choice options' wording and ordering changed, so this is not a new numbered run and the "Topic Rotation History" below is untouched). First, every distractor option across all three modules was rewritten so its length is comparable to the correct answer's (the correct option had very consistently been the longest/most detailed by a wide margin — up to 135 characters longer in some questions); a handful of correct answers were lightly trimmed (meaning preserved) where even generous distractors couldn't close the gap. Second, a much more severe tell was found while investigating: the correct answer's position (A/B/C/D) was clustered almost entirely on option B (18-19 of 20 questions per module) across all three modules — now reshuffled to an even 5/5/5/5 split per module. `agents/tutor.md` Step 8 was also updated with explicit instructions so future daily runs avoid reproducing either tell. Note for future runs: between this fix being drafted and published, another session/agent independently (and partially) edited the live ICT3112/ICT3113/INF2005 pages' distractor wording to be shorter — but did not fix the position-clustering issue and in a few cases made the length gap worse (very short distractors next to an unchanged long correct answer). That partial edit was reviewed and superseded by the full fix described above when publishing.

> [!note] Run 41 on 2026-10-21 (first run today)
> Before selecting this run's topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file's "run 40" (2026-10-20) entries exactly — no unlogged gap, file was in sync. The first two publish attempts for all three modules were refused by the Artifact tool pending a full read of the live version's saved source (not just the head returned by the `read` action); after reading each saved source file in full, the republish succeeded on retry. All three pages were republished to their existing Artefact URLs (no new URLs created). The quiz option-length and answer-position balance fixes from the run-40 sweep were carried forward (verified 5/5/5/5 A/B/C/D distribution and no outlier-length correct answers in all 60 new questions).

> [!note] Presentation-only republishes of ICT3113 on 2026-10-21 (after run 41) — raw HTML entities in quiz text, then a length-tell regression, both fixed
> The user spotted literal `&rho;`/`&lambda;`/`&mu;`/`&times;` text showing in a quiz question instead of the Greek letters/symbols (screenshot: Q6, "Queueing Theory Foundations"). Root cause: `study-quiz-template-app.js` renders quiz question/option/explanation text through an `esc()` helper that escapes `&`, so an HTML entity typed into that text (rather than the raw notes_html, which is inserted as real HTML) shows up as its own escaped literal instead of decoding to a symbol. Fixed by rewriting those four Greek-letter/symbol entities in ICT3113's run-41 QUESTIONS as literal Unicode characters (ρ λ μ ×) and republishing.
>
> That first fix accidentally reintroduced the length-tell the user had flagged and fixed earlier (run-40 sweep): the correct option for the same ρ question, `"λ/μ, equivalently λ × S"` (23 characters), collapsed to well under half the length of its three distractors (35–42 characters) once the multi-character HTML entities were swapped for single Unicode glyphs — the user caught this immediately on the same question ("now the options are easy to find the answer again due to different length"). Fixed by lengthening the correct option to `"λ divided by μ, equivalently λ × S"` (34 characters, back in the 35–42 range of its distractors) and republishing again.
>
> Across both republishes, topics, subtopics and all 20 questions' substance stayed identical to run 41 (only symbol encoding and one option's wording length changed), so neither is a new numbered run and the "Topic Rotation History" below is untouched. `claude/daily-reading-template-notes.md` in the Claude project was updated with the entity rule for future runs: `notes_html` may use HTML entities freely, but `questions` text (question/options/explanation) must use literal Unicode characters, never named/numeric entities — and any such rewrite must be re-checked against the standing option-length-balance rule before publishing, since converting entities to single characters can silently shrink an option. ICT3112 and INF2005 were checked and had no entities in their QUESTIONS blocks, so no fix was needed there; a length-outlier re-check (correct option >40 characters longer or shorter than every distractor) came back clean across all three modules' full 60 questions after these fixes.

> [!note] Run 42 on 2026-10-21 (second run today)
> Before selecting this run's topics, all three live Artefact pages were re-read via the Artifact tool and confirmed to match this file's "run 41" entries exactly — no unlogged gap, file was in sync. The first republish attempt for all three modules was refused by the Artifact tool pending a full read of the live version's saved source (same precedent as run 41: the `read` action's head excerpt doesn't count); after reading each saved source file in full, the first retry was refused a second time as "identical content already refused, resent unchanged" (the saved-source content already matched what was being published), and an immediate second retry of the same publish call succeeded for all three. All three pages were republished to their existing Artefact URLs (no new URLs created). Verified 5/5/5/5 A/B/C/D answer-position distribution and no outlier-length correct answers across all 60 new questions before publishing.

## Topic Rotation History

Tracks roughly the last 5 runs' subtopics per module, so the tutor agent can avoid repeating recent content without needing to scan local daily files (there are none). Each run appends its selections to the relevant module's list and prunes older entries down to about 5. A module new to the index simply starts with an empty list here.

### ICT3112
- 2026-10-20 (run 38): Static vs Dynamic V&V & The V-Model; Equivalence Partitioning (EP) & Comparing Whitebox vs Blackbox Testing; Static Testing Techniques (Formality Spectrum) & LCSAJ
- 2026-10-20 (run 39): State Transition Testing & the Face Recognition Door Lock Example; Static Analysis — Data-Flow Defect Classes & When It Runs; The Four Testing Levels & the Testing Pyramid; [Lab] Reqnroll BDD Acceptance Testing & Basic Musa Reliability Calculations
- 2026-10-20 (run 40): Boundary Value Analysis (BVA); Use Case Testing; Famous Software Failures & the Six Root-Cause Categories; [Lab] Selenium Browser Testing — System Testing Through a Real Browser
- 2026-10-21 (run 41): V&V Fundamentals — Verification vs Validation, Root Causes & the Cost of Getting It Wrong; Testing Fundamentals — the Error→Defect→Failure Chain, Retesting vs Regression & Good Testing Practice; Software Reliability Metrics — MTTF/MTTR/MTBF, the Musa Models & Defect Density; [Lab] Continuous Integration & Testing Dependencies — GitHub Actions, Injected Interfaces & Mocking
- 2026-10-21 (run 42): Axiomatic Semantics & Hoare Logic — Inference Rules & Weakest Preconditions; Whitebox Coverage Criteria — Statement to MC/DC & the Condition≠Decision Trap; Quality Frameworks & Metrics — PUM, CUPRIMDSO, FURPS & Defect Density; [Lab] NUnit + TDD Calculator — AAA, Red-Green-Refactor & BVA
### ICT3113
- 2026-10-20 (run 38): When to Optimise (3 Conditions) & Classical Optimisation Techniques; Percentiles, Tail Latency & SLI/SLO/SLA; Peak vs Average Workload & Common Workload Mistakes
- 2026-10-20 (run 39): Six Properties of a Good Metric (LRRECI) & the Three Metric Classes; Operational Laws — Forced Flow, Service Demand & the Service Demand Law; Bottleneck Diagnosis — the Wafer Fab LITHO-02 Failure; [Lab] JMeter Load Testing — Reproducing a Concurrency Crash
- 2026-10-20 (run 40): Multi-Server Queues (M/M/c) & One Fast Server vs Many Slow Servers; The Kingman Formula & Sakasegawa's G/G/c Approximation; Online Service Case Study — Diagnosing a Hidden Variability Problem; [Lab] Python Profiling — Measuring Before Optimising
- 2026-10-21 (run 41): Response Time Anatomy — R = W + S, User Perception & Why the Tail Matters; Queueing Theory Foundations — Key Symbols & the Observation Boundary Effect; Diagnosing Performance Problems — the Four Sources Framework; [Lab] Building a Measurable Baseline — the Ticket Triage Service
- 2026-10-21 (run 42): Workload Identification — the Three Components & the e-Filing Case Study; Interactive Systems — Open vs Closed Systems & the Interactive Response Time Law; The Performance Engineering Loop — Measure, Model, Optimise, Deploy; [Lab] Capacity Planning in Practice — Retries, Read Replicas & Erlang B Sizing
### INF2005
- 2026-10-20 (run 38): Classical Ciphers & Kerckhoffs's Principle; Hash Functions, Digital Signatures & the Birthday Attack; Authentication Categories (Three Factors) & Password Security
- 2026-10-20 (run 39): Modern Symmetric Algorithms — DES, 3DES & AES; Cryptanalysis — Brute Force, Frequency Analysis & Known Plaintext; Token & Graphical Authentication (incl. Passphrase Technique); [Lab] Cryptography — Blowfish, Diffie-Hellman by Hand & the RSA Team Challenge
- 2026-10-20 (run 40): Diffie–Hellman Key Exchange & One-Way Functions; LSB & BPCS Steganography — How the Hiding Actually Works; Access Control Models (DAC / RBAC / MAC) & Biometric Authentication Metrics; [Lab] Steganographic Integrity Verification — LSB, RSA Signatures & HMAC Together
- 2026-10-21 (run 41): Cryptography Fundamentals — Types of Cryptography, the One-Time Pad & Random Number Generators; Asymmetric Cryptography Foundations — the Key Distribution Problem, Key Pair Roles & Confidentiality vs Authentication; Steganalysis — Attacking Hidden Data & How Bit Planes Work; [Lab] Cryptanalysis Challenges — Frequency Analysis, XOR & Encoding Attacks
- 2026-10-21 (run 42): Ethical Hacking Essentials — Legal Authorisation, Hat Types & Black/White-Box Testing; The Hacking Process in Practice — Scanning, Exploitation & Covering Tracks; Access Control Cross-Cutting Principles — Pipeline, Least Privilege & Separation of Duties; [Lab] Steganographic Integrity Verification — Keyed Start Locations & a Real Prompt-Injection Case
