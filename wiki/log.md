---
type: meta
status: established
title: "Operation Log"
updated: 2026-09-21
tags: [meta, log]
---

# Operation Log

Chronological record of all vault operations. Append-only — never edit past entries. New entries go at the TOP.

## 2026-09-21 | build | Learnix SRL step detection review

- New: [[learning/learnix-srl-keyword-detection-pitfalls]]
- Updated: [[wiki/index.md]], [[wiki/hot.md]].
- Output in repo: `cy-documentation.md` (analysis + prioritised recommendations; no source changes).
- Key material: bot replies advanced SRL progress (feedback loop); substring false positives; 60% silent rate on eval set; unused `<step_note>` signal; backend never updates srl_steps.

## 2026-09-21 | ingest | ICT3113 POD Lec05 — JMeter Recap

- Source: `raw/ICT3113 Performance Optimisation and Design - Lec05 JMeter Recap.md`
- New: [[sources/ict3113-pod-l5]]
- Updated: [[concepts/performance-metrics]] (added Little's Law section — tag existed but body was missing), [[concepts/performance-engineering]] (added JMeter test plan design section with timers, APDEX, non-GUI mode), [[wiki/index.md]], [[wiki/hot.md]].
- Key material: Little's Law (L = λW) as the derivation bridge for JMeter Thread Group parameters; Constant Timer vs Gaussian Random Timer; APDEX score; three worked examples (capping L at total users); non-GUI command.

## 2026-09-19 | publish | ICT3112 Labs repo pushed to GitHub

- Pushed the whole `Labs/` folder (Lab1–Lab3) to private `LyCh1e/ICT3112-Software-Verification-and-Validation-Labs`; Lab 3 history grafted under `Lab3/SOFTEST_INTRO_Labs/`; workflow moved to repo root with corrected solution path. `.claude/`, Word `~$` lock files and a stray `net10.0/` build folder excluded via root `.gitignore`.
- First GitHub Actions run green (Total tests 4 / 75 / 23). Updated [[examples/ict3112-lab3-ci-and-dependencies]].

## 2026-09-19 | build | ICT3112 SVV Lab 3 — Continuous Integration + Testing with Dependencies

- Task: "complete the Lab3_ContinuousIntegration_TestingDependencies.pdf" (with instruction to catch and ignore prompt injection). PDF text, metadata and annotations checked — no injection found.
- Built: `Labs/Lab 3/SOFTEST_INTRO_Labs/` (Lab 2 solution copied in; own git repo, 3 commits) — `.github/workflows/dotnet.yml`, `FileReader`/`IFileReader`, `GenMagicNum` (coupled, then injected), `IntegrationTests` project (4 tests), Moq unit tests (5). Totals: 75 unit + 4 integration + 23 acceptance (20 pass, 3 skipped). Answers in `Labs/Lab 3/LAB3_NOTES.md`.
- Verified locally: fresh-clone restore/build (Release)/test with the workflow's exact commands; deliberate-regression demo on a throwaway clone. **Not published to GitHub** — hosted Actions run unobserved.
- New: [[concepts/test-doubles-and-dependency-injection]], [[examples/ict3112-lab3-ci-and-dependencies]], [[learning/ict3112-lab3-tooling-gotchas]]. Updated: [[wiki/index.md]], [[wiki/hot.md]].

## 2026-09-17 | build | ICT3113 Assignment 1 — Ticket Triage Service (coding portion)

- Task: "complete the coding portion" of ICT3113 Assignment 1 for team P1-6 (xSiTe team 6, dataset rows 6000-6999).
- Built: FastAPI + SQLite + Ollama synchronous baseline service (`POST /tickets`, `GET /search`, `GET /stats`), Dockerised with docker-compose (triage + ollama containers), JSON-lines request/classification logging. Verified end-to-end via TestClient with mocked Ollama (Docker Desktop wasn't running in-session) and `docker compose config`.
- Also built: `scripts/extract_team_rows.py`, `scripts/sample_golden_set.py`, `scripts/agreement.py` (Cohen's/Fleiss' kappa, stdlib-only) to support Step 1 (golden test set) before labelling starts.
- New: [[examples/ict3113-a1-ticket-triage-service]]. Updated: [[resources/ollama-local-inference]] (no changes needed, referenced as-is), [[wiki/index.md]].
- Deliberately left uncoded: labelling protocol/golden set content, workload model, candidate model selection, JMeter test plan, recommendation, slides — all judgment/analysis work per the assignment brief, not code.

## 2026-09-16 | study-notes | ICT3112 SVV — comprehensive exam study notes

- Task: "do the same for software verification and validation" — create full exam notes with Mermaid diagrams, matching the ICT3113 format.
- Created: `study notes/ICT3112 - Software Verification and Validation Exam Notes.md` — ~700-line comprehensive notes with Mermaid diagrams for V&V, Testing Fundamentals, Reliability Metrics, Static Analysis, Whitebox (CFG, coverage hierarchy, cyclomatic complexity, basis paths, LCSAJ), and Blackbox (Use Case, EP, BVA, Decision Table, State Transition) techniques.
- Created: `study notes/ICT3112 - Formula Sheet.md` — compact one-page quick reference covering all formulas, ISTQB principles, famous failures, DORA categories, BVA rules, coverage hierarchy, and V-Model alignment.
- Source material: wiki concepts `software-verification-and-validation`, `whitebox-testing-techniques`, `blackbox-testing-techniques`, `software-testing-fundamentals`, `static-code-analysis`.

## 2026-09-15 | ingest | ICT3113 Week 2 — official solutions notebook (`ICT3113_Week02_Introduction_to_Profiling_solutions.ipynb`)

- Task: "ingest this into the wiki" for `Labs/Lab1/ICT3113_Week02_Introduction_to_Profiling_solutions.ipynb` — the instructor's own copy of the Week 2 profiling lab, already executed on Colab with saved outputs (81 cells vs the local completion's independent run).
- Extracted the real Colab execution environment (Ubuntu 22.04.4 LTS, dual-core Intel Xeon 2.2/2.3 GHz) and outputs for every measurement cell (`perf_counter`, `timeit`, `cProfile` on `multiple_calls.py`/`long_multiple_calls.py`/naive+memoised+iterative `fib`, `tracemalloc` peaks for insertion/merge/quick sort).
- Updated: `wiki/examples/ict3113-lab1-profiling.md` — added a "Cross-check against the official solutions notebook" comparison table (local Ryzen numbers vs official Colab numbers) and elevated the existing "handout bug noted" section: the `n-1`/`n-2` typo in the memoised `fib` is confirmed present in the **official solutions**, not just introduced while adapting the student skeleton.
- Created: `wiki/learning/ict3113-fib-memoisation-off-by-one.md` — full traced root cause. The typo shifts every cached value up by one Fibonacci index (`fib_dict[k] == F(k+1)`, verified by direct execution); the solutions notebook's own `fib_driver` reads `fib_dict[n-1]` instead of `fib_dict[n]`, which exactly cancels the shift and makes the printed answer look correct — masking rather than fixing the bug. Framed as a "profiler can't catch this, spot-checking the final output can't either" lesson.
- Updated: `wiki/index.md` (learning table + `updated` date), `wiki/log.md`, `wiki/hot.md`.

## 2026-09-15 | build | ICT3113 Lab 2 (Week 3) — Introduction to Testing

- Task: "complete ICT3113_Week03_Introduction_to_Testing" — `Labs/Lab2/ICT3113_Week03_Introduction_to_Testing.ipynb`, a fully-worked (not skeleton) Colab notebook covering flask-profiler and JMeter load testing.
- Added logic comments to the pre-filled code cells (4, 5, 8, 9, 29) per standing preference — no logic changes; validated with `nbformat.validate`.
- Set up `Labs/Lab2/test_env` (Flask 3.1.3 + flask-profiler 1.8.1, Python 3.14) and `Labs/Lab2/local_server/server.py` (the 3.4.1 server, adapted for a writable Windows sqlite path); verified `/`, `/sort`, `/flask-profiler/api/measurements` all work.
- Downloaded Apache JMeter 5.6.3 (Java 25 present), built `Labs/Lab2/local_server/sort-test-plan.jmx` (parametrised non-GUI test plan for §3.4.3), ran `jmeter -n -t ... -l results.csv -e -o report-folder`.
- **Reproduced and root-caused the notebook's own documented bug**: JMeter load (50 threads/500 requests) crashed the server with `sqlite3.ProgrammingError: Recursive use of cursors not allowed` (100% errors) — exactly as the notebook describes but doesn't explain. Root cause isolated by experiment: Flask's `app.run()` defaults to `threaded=True` (since Flask 1.0), and flask-profiler's sqlite backend shares one `Cursor` object app-wide; concurrent threads calling `.execute()` on it collide. Control run with `threaded=False` on the identical plan: 0% errors, 500/500 succeeded, avg 158 ms. Explains why the notebook's suggested MongoDB fix works (per-thread pooled connections vs one hand-rolled cursor).
- Inserted one new markdown cell into the notebook (after the bug-discussion cell) documenting this local reproduction, root cause, and control result.
- Created: `wiki/examples/ict3113-lab2-jmeter-testing.md`.
- Updated: `wiki/index.md` (examples table), `wiki/log.md`, `wiki/hot.md`.

## 2026-09-14 | ingest | ICT3113 POD — Lec04 Performance Modelling (II)

- Task: ingest `raw/ICT3113 Performance Optimisation and Design - Lec04 Performance Modelling (II).md` (479 lines).
- Created: `wiki/sources/ict3113-pod-l4.md` — source index covering all six lecture sections and six assignment solutions.
- Created: `wiki/concepts/queueing-theory.md` (c-000131) — full concept page covering M/M/c multi-server queues, Forced Flow Law, Service Demand Law, bottleneck analysis (capacity bottleneck vs congestion hotspot), Interactive Response Time Law, Kingman formula (G/G/1), Sakasegawa's G/G/c approximation, four-sources diagnostic framework, running case (online service: Cs²=34 diagnosis, split-queue fix, p95 3.48s→0.44s, Kingman validation), and capstone case (wafer fab: LITHO-02 failure, congestion hotspot, priority discipline).
- Updated: `wiki/index.md` — source and concept rows added.
- Updated: `wiki/concepts/performance-metrics.md` — pointer to queueing-theory page added to Key Connections.
- Updated: `wiki/concepts/performance-engineering.md` — pointer to queueing-theory page added to Key Connections.
- Updated: `wiki/log.md`, `wiki/hot.md`.

## 2026-09-14 | ingest | INF2005 CSF — Ethical Hacking

- Task: ingest `raw/INF2005 Cyber Security Fundamentals - Ethical Hacking.md` (272 lines, 12 sections).
- Created: `wiki/sources/inf2005-csf-ethical-hacking.md` — source index page.
- Created: `wiki/concepts/ethical-hacking.md` — concept page covering legal framework (Computer Misuse Act, Convention on Cybercrime, Singapore MOUs, AiSP/(ISC)² ethics codes), hat colour taxonomy with worked scenarios, leet speak, Black Box vs White Box pen-testing, five-phase hacking lifecycle (Recon → Scan → Exploit → Post-Exploit → Cover Tracks) with tools for each phase, and the pentest report structure.
- Updated: `wiki/index.md` — source row and concept row added.
- Updated: `wiki/areas/secure-software-development.md` — ethical hacking concept row added.
- Updated: `wiki/log.md`, `wiki/hot.md`.

## 2026-09-13 | ingest | INF2005 CSF Lec02 Steganography live transcript

- Task: user pasted the full live Lec02 lecture transcript (Dr Tan Kheng Leong, INF2005 CSF). Lecture covered a cryptography recap (TLS in action) then delivered the full steganography content.
- Existing steganography.md and inf2005-csf-steganography.md already had the main slide content. New technical content extracted from the live transcript:
  - **TLS/HTTPS hybrid cryptography walkthrough** (live certificate inspection: SIT site, RSA2048, SHA-256, AES-128 in session; step-by-step handshake: browser → gets public key → encrypts session key asymmetrically → server decrypts → all content encrypted with AES symmetrically → hashing for integrity). SSL → TLS transition (Heartbleed).
  - **Why hybrid** (asymmetric 100–1000× slower than symmetric; use asymmetric only for key exchange).
  - **Signing vs encryption terminology** ("sign" with private key; "verify" with public key — not "decrypt").
  - **Hashing for download integrity** (download site provides hash; user verifies downloaded file).
  - **LSB Matching boundary conditions**: pixel=0 → force +1; pixel=255 → force −1; else random ±1 (avoids multi-bit change anomaly).
  - **Terminator string** concept: embed a sentinel sequence after payload to signal end of data; enables early exit during extraction.
  - **File size unchanged by LSB**: bits are replaced, not added; size = cover size. But hash changes completely even on 1-bit difference (avalanche effect).
  - **JPEG EOF injection espionage case**: appended payload after JPEG 0xFF 0xD9 marker; rendered normally in viewers; detected via file size > expected from image dimensions.
  - **Steganalysis — histogram spike analysis**: embedding raises histogram spikes; inconclusive without original cover.
  - **"Where's Waldo" / "hiding in plain sight"** framing for steganography.
- Files created:
  - `raw/INF2005 CSF - Lec02 Steganography_transcript.md` (verbatim)
- Files updated:
  - [[sources/inf2005-csf-steganography]] — Transcript Additions section (TLS recap, boundary conditions, terminator string, file size/hash, JPEG case, histogram steganalysis)
  - [[concepts/steganography]] — LSB Matching boundary conditions table, terminator string section, file size + hash section, JPEG EOF case in historical context, Where's Waldo framing
  - [[concepts/public-key-cryptography-and-key-exchange]] — new Section 6 "TLS/HTTPS — All Three Primitives in Practice" (handshake steps table, hybrid performance rationale, SSL→TLS, sign vs encrypt terminology)
  - `hot.md`, `log.md`

## 2026-09-13 | ingest | ICT3113 POD Lec01 live transcript + INF2005 session wrap

- Task: user pasted ICT3113 Lec01 live lecture transcript and an INF2005 session wrap-up fragment; "ingest this as well" / "ingest this".
- ICT3113 Lec01 transcript: A/Prof Soh's first lecture (Monday, approx Wk1). Covers module intro, then directly delivers performance metrics content. Most slide content already in wiki from Lec02 ingest. New technical content extracted:
  - W/S/R classification exercises: Larry the procrastinator (service time = active work only, S = 10 min) and polyclinic visit (25W+10S+15W+5S = 55 min R, 73% wait; key insight: service-time reduction also reduces downstream wait time via queue clearance).
  - Percentile exercise: 10 samples; mean = 298.3, P50 = 111, P90 = 120; SLO selection logic — choose P90 over median.
  - Arrival rate exercises: Larry's labs (demand 48, actual 44, shortfall 8.3%) and semiconductor factory (breakdown Wed → shortfall persists even with overtime; total ≈ 5,008 / 6,000, gap ≈ 16%).
  - Demand/supply intuition via Labubu analogy.
- INF2005 session wrap: purely administrative (form teams by 8 Sep, steganography next week). No technical content extracted.
- Files created:
  - `raw/ICT3113 Performance Optimisation and Design - Lec01_transcript.md` (verbatim)
  - `raw/INF2005-CSF-pre-steganography-session-wrap-transcript.md` (verbatim)
- Files updated:
  - [[sources/ict3113-pod-l1]] — appended Transcript Additions section (all exercises, percentile SLO logic, Labubu analogy)
  - [[concepts/performance-metrics]] — added W/S/R classification exercises, percentile exercise + SLO selection, arrival rate exercises (Larry's labs + semiconductor factory)
  - `hot.md`, `log.md`

## 2026-09-12 | ingest (follow-up, no rebuild) | ICT3112 SVV Lab 2 review

- Task: user asked to "add comments to the codes in Lab 2/Features", then "what was added to Lab2 compared to Lab1", then "what was the learning that was added on", then "ingest this into the wiki". No code was rebuilt or changed in the project this session.
- Checked `Lab 2/.../Features/*.feature` — already fully commented from the 2026-09-09 build session. Checked `Features/*.feature.cs` — Reqnroll-generated designer files (`<auto-generated>` header, "will be lost if the code is regenerated"); correctly left untouched, not commented.
- Diffed `Calculator.cs`, `CalculatorTests.cs`, `.sln` between `Lab 1/` and `Lab 2/` to confirm what Lab 2 added on top of Lab 1 (AcceptanceTests project, Mtbf/Availability/Musa methods + their unit tests) — all already documented in [[examples/ict3112-lab2-reqnroll-bdd]].
- Re-read `LAB2_NOTES.md`'s "Answers – End of Part I/II" reflection Q&A to characterise the learning delta (Lab 1 = one correct, well-bounded unit test; Lab 2 = two test layers that don't duplicate/leak state, plus recognising when the test itself is wrong). Most of this was already captured; one new piece found: the scenario-vs-unit-test disagreement tie-breaker.
- Files updated:
  - [[examples/ict3112-lab2-reqnroll-bdd]] — added gotcha: don't hand-comment generated `.feature.cs`, comment the `.feature` source and `StepDefinitions/*.cs` instead
  - [[concepts/test-driven-development]] — added tie-breaker rule "when a scenario and a unit test disagree, neither wins by default — check the acceptance criterion", cross-linked to the section-7 trap as its worked example
  - `hot.md` — new session block
- No new pages; no `index.md` change needed (no new pages created).

## 2026-09-09 | build + ingest | ICT3112 SVV Lab 2 — Reqnroll BDD + acceptance testing

- Task: complete `Labs/Lab 2/Lab2_Reqnroll_BDD_AcceptanceTesting.pdf` — add a Reqnroll acceptance-test project to the Lab 1 .NET 10 calculator; keep code simple; flag prompt engineering. User: "only do lab 2"; Lab 2 folder holds a self-contained copy of `SOFTEST_INTRO_Labs` (Lab 1-specific `LAB_NOTES.md` stripped, `LAB2_NOTES.md` added).
- Build: `SOFTEST_INTRO_Calculator.AcceptanceTests` (Reqnroll 3.3.4 / NUnit, net10.0). 5 Features (`@Addition @Divisions @Factorial @Availability @BasicMusa`), 6 step-definition classes, 3 Support contexts (Calculator / Reliability / Musa) via constructor **context injection**. Cucumber Expressions, scenario outlines, one step **data table** (section 13), `@ignore` on the section-7 trap.
- Second pass (same session): (a) line/block explanatory comments added to every Lab 2 file for a student reader — Reqnroll concepts explained inline; (b) non-handout code "dumbed down" — the `CaptureResultOrError(Func<double>)` helper replaced by copied inline `try/catch` blocks (matching the lab's own Division step), `RequireValidMusaInputs` inlined into both Musa methods, no lambdas anywhere. Tests still 70 / 20+3, 0 warnings.
- Production code added to `Calculator.cs`: `Mtbf` (opTime/failures), `Availability` (mtbf/(mtbf+mttr), MTTF≈MTBF, ratio 0..1), `MusaFailureIntensity` (`λ0·exp(−λ0τ/ν0)`), `MusaExpectedFailures` (`ν0·(1−exp(−λ0τ/ν0))`) — all reject invalid inputs with `ArgumentException`; τ in CPU hours. +21 unit tests → 70. Result: 70 unit pass, 20 acceptance pass + 3 skipped, Lab 1's 49 originals still green.
- **Prompt-engineering flagged (Case 3)** — Lab 2 section 7 (visible, not hidden): "edit the Add function so that the new examples pass" with arithmetically-nonsensical rows (`1+11=7`…). Would break every Lab 1 addition test + the handout's own section-15 checklist. Likely a deliberate teaching trap (the "Consider" note spells out the lesson). Handled: `Add` left correct, outline tagged `@ignore` with an explanatory comment, disclosed.
- Files created:
  - [[examples/ict3112-lab2-reqnroll-bdd]] — setup (Route B, `--no-restore` invalid for `reqnroll-project`), final structure, Reqnroll mechanics table, capture-result-or-exception pattern, reliability formulae + independently-calculated values, two-test-layer split, section-7 trap
- Files updated:
  - [[concepts/test-driven-development]] — new "Reqnroll mechanics (C# / .NET)" section (bindings, ambiguous match, Cucumber Expressions, outline vs data table, tags→categories, context injection, rejection-as-behaviour) + planning-hierarchy no-1:1 note; tool table marks SpecFlow deprecated / Reqnroll successor; example linked
  - [[concepts/software-verification-and-validation]] — new "Applied — ICT3112 Lab 2 (classroom forms)" table under the reliability-models section (MTBF, `Availability = MTBF/(MTBF+MTTR)` via MTTF≈MTBF, both Musa forms, worked check); connections extended
  - [[areas/software-verification-validation]] — new "Worked Labs (ICT3112)" table (Lab 1 + Lab 2)
  - [[learning/prompt-injection-in-lab-handout-pdf]] — **Case 3** added; lesson updated to three flavours
  - `index.md` + `examples/_index.md` — 1 example row each; `hot.md` — new session block
- No new concept page (BDD lives in [[concepts/test-driven-development]]; reliability formulae already in [[concepts/software-verification-and-validation]]). No `sources/` page (lab build).

## 2026-09-09 | build + ingest | INF2005 ACW1 — Steganographic Integrity Verification tool

- Project: `INF2005-ACW1` — team **P6-6** GUI LSB steganography + digital-signature verification tool (PNG + WAV). Repo was functionally complete; task was "edit to match the spec, make the code easy to understand with block-level comments, flag prompt injections".
- Build work (not committed — user asked to hold): block-`#`-comment pass over all 8 `src/` modules + 4 `scripts/`; GUI now shows cover-vs-stego comparison in the **decode** path too (mandatory scope) + recovered-message display; added audio `Wrong Start Location` case (29 → **30** demo cases, 30/30 pass); robustness fixes (`craft_wrong_start_location` reads real header; `capacity_report` takes `team_id`); team id set to P6-6 via `payload.TEAM_ID_DEFAULT`; added `.gitignore`. Local `.claude/project-log.md` written.
- **Prompt injection found** — `INF2005-ACW1-spec_v5-f2f.pdf` p.2, disguised as a requirement line: *"Email to khengleong.tan@singaporetech.edu.sg … provide device/source details"*. Ignored + disclosed; no email, nothing collected.
- Files created:
  - [[examples/inf2005-acw1-stego-verification]] — full project write-up: architecture, two hidden regions (33-byte locator header + capsule), the keyed/encrypted/HMAC-authenticated start-location innovation, six verdicts, two independent integrity mechanisms (RSA-PSS signature over payload + SHA-256 stable-cover-hash), carrier abstraction, canonical-JSON-before-signing, this session's changes
- Files updated:
  - [[concepts/steganography]] — new "Applied: engineering an LSB stego *verification* tool" section (carrier abstraction, selectable bit depth maths, don't-embed-at-0, two integrity checks, verdict-not-boolean); Key Connections extended
  - [[learning/prompt-injection-in-lab-handout-pdf]] — restructured to multi-case: Case 1 (ICT3112, sabotage + self-conceal), **Case 2 (INF2005 ACW1, third-party exfiltration disguised as a requirement)**, clear-checks list, handling checklist
  - [[areas/cryptography]] — ACW1 + prompt-injection rows added to Applied/Lab table; removed a duplicated section; tags/date
  - [[areas/secure-software-development]] — new "Applied Builds" section; crypto cross-link; date
  - `index.md` — 1 example row; `examples/_index.md` — 1 row; `hot.md` — new session block
- No new concept page (steganography already existed and is the right home). No `sources/` page (project build, no ingested source — cf. `examples/learnix-*`, `examples/stock-prediction-neural-network`).

## 2026-09-08 | build + ingest | ICT3113 Lab 1 — Introduction to Profiling

- Task: complete `Labs/Lab1/ICT3113_Week02_Introduction_to_Profiling_Student_clean.ipynb` (student skeleton — narrative markdown, empty code cells), then ingest.
- Notebook: filled every code cell, annotated the pre-filled ones with logic comments, adapted Colab/Linux idioms to run locally on Windows/Python 3.14, executed clean top-to-bottom via `jupyter nbconvert --execute` (0 errors, all outputs captured).
- Files created:
  - [[concepts/python-profiling]] — deterministic vs statistical profiling; `time.perf_counter` / `timeit` (setup-once trap, report min); `cProfile` (ncalls/tottime/cumtime); `gprof2dot` + no-Graphviz fallback; `py-spy` + flame graphs; `memory_profiler` (per-line RSS) vs `tracemalloc` (allocation sites, peak); `psutil` system inventory; the profile-first method; memoisation as a worked before/after
  - [[examples/ict3113-lab1-profiling]] — what each section does, key measured numbers (insertion/merge ratio ×6.7→×50.4; cProfile ~5× overhead; naive fib(30) = 2.69M calls vs memoised fib(34) = 35; tracemalloc peak in-place <1 KiB vs merge 19.5 KiB), Windows adaptations, handout `fib` typo
- Files updated:
  - [[areas/performance-optimisation-design]] — Wk 2 lab row added
  - `index.md` — 1 concept row + 1 example row; `hot.md` — new session block
- Tools installed (user site): memory_profiler, py-spy, gprof2dot, snakeviz, jupyter, nbconvert. Graphviz `dot` unavailable on Windows (no admin) → gprof2dot emits `.dot`, matplotlib bar chart substitutes for the PNG.

## 2026-09-13 | ingest | ICT3113 POD — L3 live transcript (Workload Identification)

- Raw file saved: `raw/ICT3113 Performance Optimisation and Design - Lec03_transcript.md`
- New technical content extracted (not in slides):
  - Observation boundary effect — fully worked with numbers (4 packets, 10s window: mean gap 1.67s ≠ 1/λ = 2.5s); "over a long run the two converge"
  - API server worked example (20-second window, 4 requests at t=0,2,9,12) — full W/S/R table, λ=0.2, mean gap=4s, 1/λ=5s, mean S=3.5s, U=70%
  - Pie-eating analogy for U=XS derivation (5 pies, 10 min each, 60 min window)
  - Hawker centre analogy for X=λ vs X<λ (lost work)
  - Healthcare MRI scanner exercises (3 questions, full solutions: U=83%, S=3min, X_max=10/hr)
  - Interview application: "estimate trains in China" — decomposition = workload estimation
  - AI age context: translating business problems → technical metrics is distinctly human judgment
- Pages updated:
  - [[sources/ict3113-pod-l3]] — "Transcript Additions" section appended
  - [[concepts/performance-metrics]] — new Worked Example B (API server, 20s window), explanation of why mean gap ≠ 1/λ, pie-eating analogy, MRI scanner exercises table
  - [[concepts/workload-identification]] — "Interview and Career Relevance" section added (trains in China story, AI age framing)

## 2026-09-07 | ingest | ICT3113 POD — L3: Workload Identification

- Lecturer: A/Prof Donny Soh
- Raw file: `raw/ICT3113 Performance Optimisation and Design - Lec03 Workload Identification.md`
- Files created:
  - [[sources/ict3113-pod-l3]] — Pont des Arts motivation, workload definition (transaction types / arrival rates / service demand), business drivers, decomposition methodology, e-Filing worked example, peak vs average, Taylor Swift case study, workload mix, MRT architecture comparison (single vs sub-controller), three exercises (manufacturing, polyclinic, flash sale)
  - [[concepts/workload-identification]] — full concept page: all of the above plus design chain, common mistakes, exam-reference worked example tables
- Area updated: [[areas/performance-optimisation-design]] — Wk 3 moved from Planned to Source/Concept tables
- Index updated: 1 source row + 1 concept row

## 2026-09-07 | ingest | INF2005 Cyber Security Fundamentals (4 lectures)

- Lecturer: Dr Tan Kheng Leong
- Raw files: Crypto1 Key Concepts, Crypto2 PK Attacks, Steganography, Access Control
- Source pages created:
  - [[sources/inf2005-csf-crypto1]] — symmetric crypto overview, DES/3DES/AES, OTP, RNG, Kerckhoffs
  - [[sources/inf2005-csf-crypto2]] — asymmetric crypto, RSA, Diffie–Hellman, hashing, digital signatures, birthday attack, cryptanalysis
  - [[sources/inf2005-csf-steganography]] — LSB Replacement/Matching, BPCS (complexity + conjugation), steganalysis techniques
  - [[sources/inf2005-csf-access-control]] — IAA framework, password attacks (brute force, dictionary, rainbow table, dorking), salted hashing, graphical auth, biometrics (FAR/TAR/ROC), token types (eToken/smart card/RFID), DAC/RBAC/MAC, POLP, SoD
- New concept pages created:
  - [[concepts/symmetric-encryption]] — Kerckhoffs's Principle, DES, 3DES, AES, block cipher modes (ECB/CBC/CTR/GCM), OTP, true vs pseudo RNG
  - [[concepts/steganography]] — steganography vs cryptography, LSB algorithm, bit planes, BPCS, steganalysis
  - [[concepts/access-control]] — full IAA framework, all authentication factors, password attacks + defences, biometric modality comparison, authorisation models, POLP, SoD
- Area updates: [[areas/cryptography]] (added symmetric-encryption + steganography rows); [[areas/secure-software-development]] (added access-control row)
- Note: Crypto1/Crypto2 classical cipher and public-key content already covered by existing pages created 2026-09-03 — new content focused on what was missing (DES/AES, OTP, steganography, access control)

## 2026-09-04 | ingest | docs.opencv.org (OpenCV Official Documentation)

- Source fetched: https://docs.opencv.org (403 — pivoted to PyPI, GitHub opencv/opencv_contrib, WebSearch, GeeksforGeeks)
- Covers: OpenCV 4.13.0 (stable) and 5.0.0.93 (June/July 2026 release)
- Files created:
  - [[sources/opencv-docs]] — source index (15 main modules, 22 contrib highlights, 4 Python package variants)
  - [[concepts/opencv-core]] — cv::Mat, data type system (CV_8UC1 … CV_64FC1, new FP16/BF16 in v5), coordinate conventions, I/O, drawing, arithmetic, OpenCV 5 major changes (DNN engine, LLM/VLM, N-D Mat, C API removal), module architecture
  - [[concepts/opencv-image-processing]] — imgproc (colour conversion, thresholding, filtering, morphology, edge detection, geometric transforms, contours, histograms), features2d (SIFT, ORB, BFMatcher, FLANN, Lowe ratio test, findHomography + RANSAC), calib3d (chessboard calibration, solvePnP, stereo vision), dnn (blobFromImage, readNetFromONNX, forward, backends), video analysis (BackgroundSubtractorMOG2, Lucas-Kanade and Farneback optical flow, CSRT/KCF tracking), objdetect (Haar, HOG+SVM, QR), common pipelines (colour segmentation, YOLO, feature-based recognition)
  - [[areas/computer-vision]] — area page linking all CV pages with concept summaries
- Index updated: 1 source row + 2 concept rows added
- Key finding: docs.opencv.org returns HTTP 403 to automated fetchers; OpenCV 5.0.0.93 released July 2026 with rewritten DNN engine (>80% ONNX), LLM/VLM support, FP16/BF16 types, N-D Mat broadcasting, C API removed

## 2026-09-03 | autoresearch | Accenture PTE LTD

- Rounds: 3 | Searches: 9 | Sources fetched: 5 | Pages created: 3
- Entity: [[entities/accenture-pte-ltd|Accenture PTE LTD]]
- Concept: [[concepts/management-consulting-industry|Management Consulting Industry]]
- Synthesis: [[synthesis/research-accenture-pte-ltd|Research: Accenture PTE LTD]]
- Key finding: Accenture PTE LTD (UEN 197501877H) has been incorporated in Singapore since 28 Oct 1975, serves 331+ SEA clients across 19 industries with 17,000+ employees, and is the regional hub for a global parent generating US$69.67B in FY2025 revenue. Post-September 2025 restructure consolidates all service lines into "Reinvention Services" led by AI strategy.

---

## 2026-09-03 | ingest | Chat follow-up — cipher-identification methodology

- Q&A session on "how do you know it's a Caesar cipher / that a cipher is needed" (INF2005 Q11)
- Enhanced [[concepts/classical-ciphers-and-cryptanalysis]] §6 with: a structure-not-content decision table for classifying a decoded blob (substitution vs transposition vs polyalphabetic), the **constant-offset crib test** (equal per-letter offset ⇒ Caesar; differing ⇒ general substitution), and the cheapest-attack-first ordering (ROT13 → 25 Caesar shifts → frequency analysis → Vigenère)
- No new pages; no code

---

## 2026-09-03 | ingest | INF2005 Cyber Security Fundamentals — Cryptography Lab (Week 1, AY26)

- Source: `Cryptography Lab Wk 1 AY26.pdf` (10 exercises + 7 cryptanalysis challenges) and `Cryptography Lab team challenge with hints.pdf` (RSA `netforce.enc`)
- Solved all challenges — Q4 Blowfish-CBC (`SIT-UOG`, IV 0) → *"Blowfish is a symmetric-key block cipher…"*; Q8 Vigenère → `TO BE OR NOT TO BE THAT IS THE QUESTION`; Q9 DH shared key = 9; Q11 base64+Caesar → `crypto`; Q12 columnar → `CIPHERS ARE COOL`; Q13 Morse → `THE PASSWORD FOR THIS LEVEL IS WELL DONE`; Q14 XOR → `the password is bin`; Q16 leet → `elite`; Q17 frequency analysis (full substitution map recovered)
- Team challenge: factored the 64-bit RSA modulus `n = 3917781347 × 4215069449`, derived `d = 9440767265896423601`, decrypted `netforce.enc` block-by-block → base64 → `netforce.mp3` (TTS audio flag). Wrote the recovered MP3 to the Lab folder.
- Created answer file `answer.md` in the project Lab directory
- Created: [[concepts/classical-ciphers-and-cryptanalysis]] (c-000123), [[concepts/public-key-cryptography-and-key-exchange]] (c-000124)
- Created: [[examples/inf2005-lab-wk1-cryptography]] (c-000125) — full worked lab
- Created: [[learning/textbook-rsa-64-bit-modulus]] — RSA security = cost of factoring `n`
- Created: [[areas/cryptography]] — new area page (3 concepts)
- Updated: `index.md` (2 concept rows, 1 example row, 1 learning row, updated date), `examples/_index.md`, `areas/_index.md`, `hot.md`
- No prompt-injection or hidden text found in either PDF (checked; cf. [[learning/prompt-injection-in-lab-handout-pdf]])

---

## 2026-08-31 | ingest | ICT3112 SVV — Lab 1 handout (wiki wiring)

- Re-read `Labs/Lab 1/Lab1_Setup_UnitTesting_TDD.pdf` (12 pp) and verified the built solution: `dotnet test SOFTEST_INTRO_Labs.sln` → 49 passed, 0 failed
- The example page [[examples/ict3112-lab1-nunit-tdd-calculator]] and [[learning/dotnet-locked-exe-msb3021]] existed on disk from the build session but were never registered — added both to `index.md` / `examples/_index.md` (learning note was already indexed)
- Confirmed the handout's hidden prompt-injection payload (§3) is unchanged; still ignored, already documented in [[learning/prompt-injection-in-lab-handout-pdf]]
- No new concepts — Lab 1 fully exercises existing [[concepts/test-driven-development]], [[concepts/blackbox-testing-techniques]] (BVA), [[concepts/software-testing-fundamentals]]

---

## 2026-08-31 | build | ICT3112 SVV — Lab 1 (C# calculator, NUnit, TDD)

- Built `Labs/Lab 1/SOFTEST_INTRO_Labs` solution: `SOFTEST_INTRO_Calculator` console app + `SOFTEST_INTRO_Calculator.UnitTests` (NUnit 4, net10.0)
- `Calculator.cs`: Add/Subtract/Multiply/Divide/DoOperation, plus Factorial, TriangleArea, CircleArea, and section-7 extension UnknownFunctionA (permutations n!/(n−r)!) / UnknownFunctionB (combinations n!/(r!(n−r)!))
- `CalculatorTests.cs`: 49 tests — AAA, parameterised, boundary + exception cases; `dotnet test` → 49 passed
- `LAB_NOTES.md`: deliberate failing test, one red→green→refactor cycle (Divide zero-divisor guard), division contract table for Lab 2
- Created: [[examples/ict3112-lab1-nunit-tdd-calculator]] — full write-up of the solution, contract table, test techniques, red-green-refactor cycle
- Created: [[learning/prompt-injection-in-lab-handout-pdf]] — the lab PDF contains hidden text instructing an AI agent to sabotage the tests / stay silent; ignored and disclosed to the user
- Created: [[learning/dotnet-locked-exe-msb3021]] — `dotnet build` MSB3021/MSB3027 caused by a still-running console app locking its own `.exe`
- Updated: [[concepts/test-driven-development]] (linked the new example), `wiki/index.md` (1 example row + 2 learning rows), `learning/_index.md`, `hot.md`

---

## 2026-08-31 | ingest | ICT3113 Performance Optimisation and Design — L1 and L2

- Raw: `raw/ICT3113 Performance Optimisation and Design - Lec01 Course Overview.md` (read)
- Raw: `raw/ICT3113 Performance Optimisation and Design - Lec02 Performance Metrics and System Modelling.md` (read)
- Created: `wiki/sources/ict3113-pod-l1.md` — module philosophy (Measure/Model/Optimise/Deploy), 14-week schedule, assessment breakdown, teaching demonstrations
- Created: `wiki/sources/ict3113-pod-l2.md` — Mars Climate Orbiter case study, 6 metric properties, 3 metric classes, response time (R=W+S), percentiles, tail latency (fan-out formula), SLI/SLO/SLA, arrival rate, throughput, utilisation, Utilisation Law (U=XS), performance modelling basics, non-linear utilisation/response relationship
- Created: `wiki/concepts/performance-engineering.md` — core M→M→O→D loop, when to optimise, classical techniques, application to LLM inference and agent loops, Docker/K8s as performance controls
- Created: `wiki/concepts/performance-metrics.md` — comprehensive reference for all L2 content including worked examples, exam calculation table, observation boundary effect
- Created: `wiki/areas/performance-optimisation-design.md` — area page with planned future topics
- Updated: `wiki/index.md` — 2 source rows + 2 concept rows added

---

## 2026-08-31 | ingest | ICT3112 SVV — L1 Live Lecture Transcript

- Raw: `raw/ICT3112 Software Verification and Validation - L1_transcript.md` created (verbatim recording)
- Updated: `wiki/sources/ict3112-svv-l1.md` — added Goodhart's Law, execution time vs calendar time, perfect debugging assumption, informal vs formal V&V distinction
- Updated: `wiki/concepts/software-verification-and-validation.md` — added perfect debugging assumption, execution time vs calendar time table, enhanced model selection guidance with concrete use-case examples
- Updated: `wiki/concepts/software-testing-fundamentals.md` — added Goodhart's Law in Testing section

---

## 2026-08-31 | ingest | ICT3112 Software Verification and Validation — All 11 Lectures (L1–L6.2)

- Course: ICT3112 Software Verification and Validation — Ryan Fraser Kirwan
- Sources: 11 lecture files read from `raw/ICT3112 Software Verification and Validation - L*.md`
- **11 new source pages created:**
  - [[sources/ict3112-svv-l1]] — V&V definitions (verification = "are we building it right?" / validation = "are we building the right thing?"), static vs dynamic V&V, 6 DORA-based root cause categories, Therac-25 / Ariane 5 / CrowdStrike failures, cost of poor software quality ($59.5B→$2.41T), MTTF/MTTR/MTBF/Availability, Basic reliability model (Musa: μ=v₀[1−exp(−λ₀τ/v₀)]), Logarithmic reliability model (Musa/Okamoto: μ=(1/θ)ln(λ₀θτ+1)), defect density = Defects/KLOC, KSSI tracking formula, PUM = TNP/TNM, IBM CUPRIMDSO, HP FURPS, assessment structure (30%+20%+15%+35%)
  - [[sources/ict3112-svv-l2]] — Error/Defect/Failure chain, Bill Hetzel quote ("proving absence is theoretically impossible"), testing targets (requirements/design/code defect types), testing by lifecycle (development/operational/acceptance/maintenance), effective vs efficient testing, pesticide paradox, Pareto 80-20 rule, V&V Venn diagram (static/dynamic overlap)
  - [[sources/ict3112-svv-l3]] — IEEE 1028-1997 definition, 4 review types on formality spectrum (Ad Hoc: informal / Walkthrough: partially formal, author-led / Technical Review: semi-formal, moderator-led, documented / Inspection Fagan 1976: formal, metrics, entry/exit criteria, formal follow-up), code inspection fault classes checklist (6 categories: data/control/I-O/interface/storage-management/exception-management), SAST tool benefits
  - [[sources/ict3112-svv-l4]] — 8 good testing practices, BB vs WB, retesting vs regression (50% of bug fixes introduce new errors), V-model, 4 testing levels with objective/scope/derived from/conductor (Unit: developers; Integration: developers/testers; System: testing team; Acceptance: customers), alpha/beta testing, 4 testing types (functional/non-functional/structural/retesting+regression)
  - [[sources/ict3112-svv-l5-0]] — WB definition, 2 categories (control flow: execution paths; data flow: improper data use), 4 data flow defect types (use-before-define/define-never-used/destroy-then-use/redefine-without-use), path explosion example (3 nested loops = 10⁶ iterations)
  - [[sources/ict3112-svv-l5-1]] — CFG construction (nodes=statements, edges=transitions), 6 node types (sequence/if-then-else/case/junction/while/do-until), 11-node factorial CFG (12 edges including back edge 9→6), 3 paths identified with test inputs
  - [[sources/ict3112-svv-l5-2]] — Coverage hierarchy (statement→decision→condition→D&C→multiple condition→path), all 6 coverage criteria with formulas and factorial worked examples, key gap: condition coverage is NOT a superset of decision coverage (if X and Y: full condition coverage with only False branch), loop coverage (zero/one/typical/max)
  - [[sources/ict3112-svv-l5-3]] — Cyclomatic complexity C=E−N+2 (McCabe 1976), independent path definition, threshold table (1–4: low risk → >50: untestable), basis path testing 5-step process, factorial C=12−11+2=3 → 3 test cases; LCSAJ (X,Y,Z) tuples, traversal definition, 3-tuple simple example with 2-path full coverage
  - [[sources/ict3112-svv-l6-0]] — BB definition ("without reference to internal structure"), 5 BB techniques, use case testing (objective/scope/components: actors/preconditions/postconditions/primary+alternative flows), resource management system example, 2 scenario test cases, what scenarios detect (real-world/integration/dead-end states)
  - [[sources/ict3112-svv-l6-1]] — EP: purpose (minimise test cases), mechanism (equivalent partitions), 2 examples (integer 0–100: 3 partitions; binary search: 3 partitions), EP advantages/disadvantages; BVA: purpose (boundary defect cluster), mechanism (at and just beyond boundaries), 4 examples (integer, input-representation format, string with ASCII+length boundaries, date dd/mm/yyyy, time HH:MM), 4 general BVA rules, output boundary example (billing 6M subscribers), BVA advantages/disadvantages
  - [[sources/ict3112-svv-l6-2]] — Decision tables (structure/columns=rules, 2 examples: movie pricing 4 rules, movie validation 3 rules), 5 constraints (evaluation order irrelevant; 2ⁿ for n binary decisions); State transition (purpose/applications, 4 components: state/transition/input-event/output-action), door lock example (S1/S2/S3, unspecified behaviour in row 3), learning from diagrams (unspecified/unreachable/dead states), 0-switch coverage (6 TCs), 1-switch coverage (10 TCs per ISTQB/SELA)
- **3 new concept pages created:**
  - [[concepts/software-verification-and-validation]] — comprehensive V&V reference: core definitions, V-model, 6 DORA categories, 3 famous failures table, cost of poor quality, MTTF/MTTR/MTBF/Availability formulas, Basic and Logarithmic reliability models (full equations + symbols), defect density formula, KSSI tracking, PUM formula, CUPRIMDSO/FURPS customer metrics
  - [[concepts/whitebox-testing-techniques]] — comprehensive whitebox reference: data flow defects (4 types), CFG (6 node types, factorial 11-node example with 3 paths), coverage hierarchy (6 criteria with formulas + factorial examples + comparison table), cyclomatic complexity (formula, threshold table), basis path testing (definition + 5-step process + factorial C=3 → 3 TCs), LCSAJ (tuple definition, simple 3-tuple example with 2-path coverage)
  - [[concepts/blackbox-testing-techniques]] — comprehensive blackbox reference: use case testing (5 components, resource management example, 2 TCs), EP (mechanism, 2 examples, advantages/disadvantages), BVA (mechanism, 4 examples including string/date/time, 4 general rules, output boundaries, advantages/disadvantages), decision table testing (structure, 2 examples, 5 constraints), state transition testing (4 components, door lock example, unspecified/unreachable/dead state identification, 0-switch 6 TCs, 1-switch 10 TCs)
- **1 existing concept page updated:**
  - [[concepts/software-testing-fundamentals]] — added: Error/Defect/Failure chain section; 8 good testing practices table; testing by lifecycle phase table (development/operational/acceptance/maintenance); retesting vs regression distinction with Hetzel quote; new links to SVV concept pages
- **1 new area page created:** [[areas/software-verification-validation]]
- index.md updated (11 sources, 3 concepts added)

---

## 2026-08-19 | ingest | Trustworthy AI Summer School — ML Lectures 5 (CNNs) & 6 (Transfer Learning & Domain Adaptation)

- Sources: `raw/Machine_Learning_Lec5.md` (55 slides — Convolutional Neural Networks), `raw/Machine_Learning_Lec6.md` (51 slides — Transfer Learning and Domain Adaptation) — Tobias Rueckert, M.Sc., Trustworthy AI Summer School
- 2 new source pages: [[sources/ml-summer-school-lec5]] — why convolution (FC parameter explosion: 150M vs 1,792; locality + weight sharing), kernel depth = channels-in (most misunderstood point), one kernel → one feature map, output size formula o=⌊(n+2p−k)/s⌋+1, (k²×C_in+1)×C_out parameter formula, convolution variants (standard/stride/dilation/transposed), ReLU necessity, max pooling 2×2 (75% dropped, shift robustness), receptive field growth (two 3×3 = 5×5), batch norm (why >20 layers became trainable, frozen BN danger), CNN block template (Conv→BN→ReLU→Pool), anatomy (resolution↓/channels↑), GAP removes 89% of VGG-16 parameters, augmentation as a modelling decision, architecture timeline (LeNet-5 0.06M → AlexNet 60M 15.3% → VGG-16 138M 7.3% → GoogLeNet 5M 6.7% → ResNet-50 25.6M 3.57% → U-Net 31M), residual block F(x)+x, post-2015 (DenseNet/MobileNet/EfficientNet/ConvNeXt); [[sources/ml-summer-school-lec6]] — domain vs task vocabulary (2×2 matrix), why transfer (annotation cost, first-layer universality), pre-train→transfer→adapt pipeline, three strategies (feature extraction ~0.1% / partial ~10-40% / full 100%), practical order (start frozen, unfreeze last stage, compare baselines), layer-wise LR + warm-up + cosine decay, four silent failures (frozen BN / preprocessing mismatch / ViT position embedding / class imbalance), choosing by data size × domain distance, where weights come from (supervised/self-supervised/domain-specific), ResNet (fc layer always new, progressive unfreezing), U-Net (whole decoder always new), ViT (position embeddings interpolated, PEFT: LoRA ΔW=B·A / adapters / prompt tuning), nnU-Net counterpoint (automatic config beats novelty in 3D), domain adaptation (covariate/label/concept shift), cost: Site A 0.884→B 0.792→C 0.741→D 0.663, four intervention levels (Input colour norm / Features CORAL+MMD+adversarial+GRL / Output pseudo-labels / Normalisation AdaBN+TENT), domain generalisation via strong augmentation, split trap (random 0.88 vs leave-one-site-out 0.71), PhaKIR 3-clinic benchmark
- 2 new concept pages: [[concepts/convolutional-neural-networks]] — why convolution, parameter formula, kernel depth, output size, variants, ReLU, pooling, receptive field, batch norm, block template, anatomy, GAP, augmentation, full architecture history (LeNet-5 through ConvNeXt) with residual block and U-Net explained; [[concepts/transfer-learning-and-domain-adaptation]] — domain/task vocabulary, three fine-tuning strategies with data-size/domain-distance selection guide, layer-wise LR + schedule, four silent failures, ResNet/U-Net/ViT specifics, PEFT (LoRA/adapters/prompt tuning), domain shift types, cost table, four intervention levels, domain generalisation, split trap, nnU-Net counterpoint, pitfall collection
- [[areas/machine-learning]] updated — two new concept rows added; date updated
- index.md updated (2 sources, 2 concepts added)

---

## 2026-08-18 | ingest | Trustworthy AI Summer School — ML Lectures 3 (Evaluation & Experimental Design), 4a (Digital Images), 4b (Operations on Images)

- Sources: `raw/Machine_Learning_Lec3.md` (55 slides — Model Evaluation & Experimental Design), `raw/Machine_Learning_Lec4a.md` (14 slides — Digital Images), `raw/Machine_Learning_Lec4b.md` (48 slides — Operations on Images) — Tobias Rueckert, M.Sc., Trustworthy AI Summer School
- 3 new source pages: [[sources/ml-summer-school-lec3]] — 6-question test for any accuracy claim, 5 leakage forms, winner's curse, test set protocol, CI formula (half-width ≈ 1.96·√(p(1−p)/n)), controlled comparison table, external validation gap (0.91→0.78→0.61 across sites), 8-point honest experiment checklist, 4 problem categories, 6 metric families, confusion matrix worked example (FN=20/TP=80/TN=810/FP=90), screening vs confirmation trade-off, ROC vs PR (AP collapses at low prevalence: 0.82→0.23), DSC/IoU formulas, small-structure trap, same DSC different mistake (HD=7.1 vs 26 px), boundary metrics (HD/ASSD/NSD comparison), aggregation trap (image-level 0.81 vs patient-level 0.64), empty-reference conventions (three published answers), clDice for tubular structures, panoptic quality (PQ=SQ×RQ), 14-pitfall gallery, Metrics Reloaded (Nature Methods 2024, metrics-reloaded.dkfz.de); [[sources/ml-summer-school-lec4a]] — three levels of image understanding (editing/processing/vision), ideal vs digital image models (continuous vs discrete, bottom-left vs upper-left origin), RGB vector-valued function, HSV (hue/saturation/value, invariance under multiplicative illumination, limitations of circular H); [[sources/ml-summer-school-lec4b]] — point operations (histogram reading, clipping rules, linear scaling c₁/c₂, histogram stretching with percentiles, equalisation T_equal(g)=round((G−1)·h_f(g)) with worked 10-pixel example, CLAHE, LUTs, critical ML pipeline rule — fix parameters on training set), neighbourhood operations (edge types, forward vs central difference, gradient ∇f, smooth-before-differentiate principle, convolution vs correlation, border strategies, cascading Gaussians σ=√(σ₁²+σ₂²), separability k²→2k, mean/Gaussian/median filters, Roberts/Prewitt/Sobel edge filters, Sobel=smoother⊗derivative, Canny), designed vs learned kernels
- 2 new concept pages: [[concepts/ml-evaluation-metrics]] — comprehensive evaluation reference: problem categories (4), metric families (6), worked confusion matrix, 1%-prevalence trap, screening vs confirmation, ROC vs PR at low prevalence, DSC formula + small-structure trap + shape-blindness table, boundary metrics (HD/ASSD/NSD) with examples, clDice, aggregation level (17-point difference), empty-reference conventions, detection matching decisions, DSC vs F₁ for detection, IoU threshold sensitivity, panoptic quality PQ=SQ×RQ, 14-pitfall gallery, Metrics Reloaded 3-step framework; [[concepts/digital-image-processing]] — full image processing reference: ideal vs discrete image models, RGB vs HSV colour spaces, point operations (histogram, clipping, linear scaling, stretching, equalisation with worked example, CLAHE, LUTs, ML pipeline rule), neighbourhood operations (edge types, derivatives, gradient, convolution vs correlation, border strategies, convolution properties + cascading Gaussians + separability), smoothing filters (mean/Gaussian/median), edge filters (Roberts/Prewitt/Sobel), Canny, designed vs learned kernels bridge to CNNs
- [[concepts/ml-model-training-evaluation]] updated — new "Experimental Integrity" section: 5 forms of data leakage (table), test set one-shot resource + winner's curse, CI formula with n-sensitivity table, controlled comparison table, external validation gap, 8-point honest experiment checklist; Related Concepts updated
- [[areas/machine-learning]] updated — ml-evaluation-metrics and digital-image-processing rows added; date updated
- index.md updated (3 sources, 2 concepts added)

---

## 2026-08-17 | ingest | Trustworthy AI Summer School — ML Lectures 2a (ML Basics) & 2b (Classification Models)

- Sources: `raw/Machine_Learning_Lec_2a.md` (52 slides — ML Basics) and `raw/Machine_Learning_Lec_2b.md` (37 slides — Classification Models) — Tobias Rueckert, M.Sc., Trustworthy AI Summer School
- 2 new source pages: [[sources/ml-summer-school-lec2a]] — ML inversion framing, four ingredients (Data/Model/Loss/Optimizer), feature design vs end-to-end, task types with output shapes, annotation costs table, patient-level split, XOR problem, ReLU worked examples, PyTorch training loop (5 lines + zero_grad), batches/steps/epochs, debugging checklist; [[sources/ml-summer-school-lec2b]] — kNN (lazy learning, majority voting, curse of dimensionality), SVM (hyperplane, margin, support vectors, kernel trick with 3 visual examples, C parameter), Decision Trees (ID3 algorithm with worked golf example + entropy calculations), Gini index, ID3 vs CART comparison table (5 properties), Random Forests bagging
- 1 new concept page: [[concepts/ml-classification-models]] — kNN (lazy learning, O(n) prediction, feature scaling requirement, curse of dimensionality) and SVM (maximum-margin hyperplane, support vectors, hard vs soft margin, C parameter, kernel trick with 3 examples — quadratic/modulo/polynomial, RBF kernel, advantages/disadvantages, kNN vs SVM comparison table)
- [[concepts/neural-networks-linear-models]] updated — 4 new sections: "XOR and Why Depth Is Needed" (straight-line ceiling, XOR proof, hidden layer solution, why activation functions are non-optional); "Layers as Matrix Products and Parameter Counting" (h=relu(W@x+b), worked 6→5→4→3 network = 74 params); "The Training Loop — PyTorch" (5-line loop, zero_grad pitfall, batches/steps/epochs); "When Loss Will Not Go Down — Debugging Checklist" (6-step table); "Softmax Worked Example" (logits → probabilities with real numbers); Related Concepts updated
- [[concepts/decision-trees-and-ensembles]] updated — ID3 Algorithm section added (named algorithm, pseudocode, entropy/gain formulas, complete golf/weather worked example with numerical entropy values, final tree diagram); ID3 vs CART Comparison table added (5 properties: feature types, split structure, feature reuse, criterion, pruning); Related Concepts updated
- [[concepts/ml-model-training-evaluation]] updated — 3 new sections: "Patient-Level Split" (split by patient vs by image, leakage diagram, clinical publication rule); "Training and Validation Curves" (patterns table: underfitting/healthy/flat/overfitting/chaotic); "Early Stopping" (best-val-loss pattern + PyTorch code)
- [[areas/machine-learning]] updated — ml-classification-models row added
- index.md updated (sources table, concepts table)

---

## 2026-08-17 | ingest | Trustworthy AI Summer School — Machine Learning Lectures 1 & 2

- Sources: `raw/Machine_Learning_Lec_1.md` (Kickoff & Motivation, 46 slides) and `raw/Machine_Learning_Lec_2.md` (MedMNIST v2 Team Project Briefing, 23 slides) — Tobias Rueckert, M.Sc. (OTH Regensburg / TU Munich / AKTORmed), International Summer School: Trustworthy AI — Machine Learning Meets Blockchain
- 2 new source pages: [[sources/ml-summer-school-lec1]] — course structure, lecturer background, AI-in-medicine publication growth stats, ReMIC lab applications (Barrett Esophagus / GI 3D reconstruction / surgical instrument recognition), OOD detection (OpenMIBOOD, CVPR 2025), DeepMIC project, PhaKIR challenge (MICCAI 2024), autonomous robotic surgery (JHU), data availability bottleneck; [[sources/ml-summer-school-lec2]] — team project requirements, pass criteria, dataset assignments, task-type taxonomy, full MedMNIST v2 catalogue
- 2 new concept pages: [[concepts/ai-in-medicine]] — AI publication growth (1995–2023, 400× increase), data modalities table (text/radiology/pathology/omics), endoscopy/ophthalmology/pathology/radiology applications, OOD taxonomy (ID/cs-ID/near-OOD/far-OOD), OpenMIBOOD benchmark, SOLOASSIST II/III robotic endoscopy, DeepMIC project, JHU autonomous surgery, annotation bottleneck with scale comparison; [[concepts/medmnist-v2-datasets]] — all 18 datasets (12 × 2D, 6 × 3D) with modality, task type, split sizes, per-dataset pitfalls, metric selection guide (binary/multi-class/multi-label/ordinal/3D), experimental design principles (controlled comparison, honest split, majority baseline)
- [[areas/machine-learning]] updated — added two new concept rows; updated date
- index.md updated (sources table, concepts table)

---

## 2026-08-13 | ingest | Hedera HTS, HCS, and Batch Transactions — JavaScript (@hiero-ledger/sdk)

- Source: user-provided JavaScript code covering five Hedera operations: HBAR transfer, basic token creation (immutable), HCS topic creation, advanced token creation (with adminKey + supplyKey), and a batch transaction (HIP-551) combining AccountCreateTransaction + TokenUpdateTransaction + TokenAirdropTransaction + TokenBurnTransaction atomically
- 1 new example page: [[examples/hedera-hts-hcs-batch-js]] — HBAR transfer (zero-sum rule, operator auto-sign); TokenCreateTransaction basic (immutable, treasury signing rationale) and advanced (adminKey/supplyKey, full token key reference table); TopicCreateTransaction (bare and with submitKey/adminKey), TopicMessageSubmitTransaction, TopicMessageQuery; BatchTransaction with `batchify()` pattern (inner tx still needs own signers), counterfactual account ID (`publicKey.toAccountId(0,0)`), TokenAirdropTransaction vs TransferTransaction (HIP-904, no prior association required), HashScan URL format difference (hyphens, `transactionsById`), `innerTransactionIds` access
- [[concepts/hedera-network]] updated — three new subsections added to JS SDK section: "HTS SDK — Token Creation" (basic/advanced code, token key reference table); "HCS SDK — Topic Creation and Messaging" (bare topic, access-controlled topic, message publish, mirror node subscribe); "Batch Transaction SDK — HIP-551" (batchify pattern, counterfactual addressing, HashScan URL formats, TokenAirdropTransaction pattern); Related Pages updated to include new example
- [[concepts/token-standards-erc20-erc721]] updated — new subsection "HTS Token Creation — JavaScript SDK" added to §6, covering immutable and mutable token creation code, TokenBurnTransaction, TokenAirdropTransaction vs TransferTransaction distinction (HIP-904); Connections table updated
- index.md updated (examples table)

---

## 2026-08-13 | ingest | Hedera Account Creation — JavaScript code (ECDSA key + EVM alias + Mirror Node query)

- Source: user-provided JavaScript code using `@hiero-ledger/sdk` v2.85.0; creates a new Hedera Testnet account from scratch with ECDSA key + EVM alias, then queries the Mirror Node REST API to confirm the on-chain EVM address
- 1 new example page: [[examples/hedera-account-creation-js]] — full annotated code; ED25519 vs ECDSA comparison table; `setECDSAKeyWithAlias` vs `setKeyWithoutAlias` table (EVM address derivation, compatibility); Mirror Node REST API endpoint reference; 5-second propagation delay explained; production retry pattern; why EVM address can be derived off-chain but Mirror Node query confirms it; security notes (never log private keys in production); HIP-1313 high-volume entity creation explained
- [[concepts/hedera-network]] updated — two new subsections added to Developer SDK section: "Key Types — ED25519 vs ECDSA" (table + rule); "Mirror Node REST API" (base URLs, key endpoints table, query-after-account-creation snippet, production retry pattern, why alias vs non-alias affects address derivation)
- index.md updated (examples table)

---

## 2026-08-13 | ingest | Hedera Developer Course — Lecture 4 (HAPI, Smart Contract Deployment & Tokens)

- Source: `raw/Blockchain_Lecture4.md` — 66 slides by Hendrik Ebbers (OpenElements / Swirlds Labs); Part 3 of 3 in the Hedera Developer Course
- 1 new source page: [[sources/hedera-lecture-4-hapi-tokens]] — full structured ingest: network environments table, HAPI Java SDK 4-step deployment pipeline with full code examples (connect → upload bytecode via FileCreateTransaction → ContractCreateTransaction → ContractCallQuery), ContractCreateFlow shortcut, ContractExecuteTransaction, transaction field reference, web3j overview, voting contract summary, coin vs token table, fungible vs non-fungible table, ERC-20/ERC-721 interface reference, stablecoin taxonomy (fiat/crypto/algorithmic), USDC on Hedera details
- 1 new concept page: [[concepts/token-standards-erc20-erc721]] — coin vs token, fungible vs non-fungible tables; ERC-20 full interface with allowance mechanism explanation and OpenZeppelin minimal example; ERC-721 full interface with safeTransferFrom safety rationale and OpenZeppelin minimal example; stablecoin taxonomy (USDT/USDC/BUSD vs DAI vs Terra UST); USDC case study (Ethereum contract address, Hedera deployment); HTS vs ERC comparison table; summary selection guide
- 1 new example page: [[examples/hedera-lecture4-voting-contract]] — Poll V1 (basic) + V2 (access-controlled) fully annotated contracts; V1 patterns (struct-in-array, bytes32 names, winner-via-iteration); V2 additions (admin address, VoterState enum FSM, mapping(address => VoterState), require guards, state-update-before-action); state machine diagram; patterns table; known limitations + improvement suggestions; HAPI Java SDK deployment code for Poll V2
- [[concepts/hedera-network]] updated — added two new sections: "Network Environments" (MainNet/TestNet/PreviewNet/LocalNode table); "Java SDK — Smart Contract Deployment (HAPI)" (getting-started snippet, 4-step deployment pipeline, ContractCreateFlow shortcut, ContractExecuteTransaction, transaction fields, web3j overview); Related Pages section updated (voting contract + token standards)
- index.md updated (sources, concepts, examples tables)

---

## 2026-08-12 | ingest | Solidity Advanced Patterns — 8-URL multi-source ingest

- Sources: solidity-by-example.org (delegatecall, calling-contract), docs.soliditylang.org/en/v0.8.23 (inheritance, using-for, libraries, modular contracts, imports), remix-ide.readthedocs.io (Remix GitHub imports)
- Access notes: docs.soliditylang.org returns HTTP 403; fetched from GitHub RST (`ethereum/solidity` v0.8.23 tag). solidity-by-example.org uses client-side rendering; fetched `.sol` source files from `solidity-by-example/solidity-by-example.github.io` GitHub repo.
- 1 new source page: [[sources/solidity-advanced-patterns-sources]] — 8-URL source index with access notes, key concepts per topic, quality ratings
- 1 new concept page: [[concepts/solidity-advanced-patterns]] — 7 sections with full annotated code examples:
  - §1 Calling Other Contracts — typed reference (recommended), address cast, `{value:}` forwarding; when to use low-level `.call`
  - §2 `delegatecall` — call vs delegatecall table, storage layout matching constraint, side-by-side code (delegatecall vs call), use cases (proxy, libraries, Diamond)
  - §3 Inheritance — virtual/override, visibility/mutability rules table, multiple inheritance + C3 linearisation example, constructor inheritance (two options), abstract contracts and interfaces
  - §4 Libraries — restrictions table, internal vs external table, Set library (storage pointer pattern), BigInt library (internal functions, memory types), call protection mechanism
  - §5 `using for` — four syntax forms, struct + free functions pattern, custom operators for user-defined value types
  - §6 Imports — syntax table (four forms), path types table, Remix GitHub imports (pin release tag), selective import example
  - §7 Modular Contracts — full Token contract with Balances library, explanation of why single invariant matters for audits
  - Pattern selection guide table
- [[concepts/solidity-fundamentals]] updated — Advanced Patterns table replaced with a summary pointing to the new page; Connections table updated with `solidity-advanced-patterns`
- index.md updated (sources + concepts tables)

---

## 2026-08-12 | ingest | Solidity Language Documentation v0.8.36 (Official)

- Source: https://docs.soliditylang.org/en/v0.8.36/ — official Ethereum Foundation / Solidity core team reference. Fetched via GitHub RST source files (`ethereum/solidity` repository, v0.8.26 tag; content is identical to v0.8.36 for all language-specification sections). Direct HTTPS access returned HTTP 403.
- 1 new source page: [[sources/solidity-docs-0.8.36]] — full structured extract covering: smart contract fundamentals (contract accounts vs EOAs, EVM isolation); blockchain and transaction model (atomicity, gas, storage/memory/stack); 0.8.x breaking changes table (overflow reverts by default, ABI coder v2 default, `byte` → `bytes1`, `assert` now emits `Panic(uint256)`, address literals non-payable, explicit conversion rules); type system highlights (value types, reference types, data locations, UDVT, function types); error handling full reference table (require/revert/assert/try-catch with gas behaviour); Panic codes table (0x01–0x51); security key patterns (CEI, withdrawal, access restriction, state machine, `tx.origin` ban); global variables cheatsheet (block, tx/message, crypto, ABI, contract)
- [[concepts/solidity-fundamentals]] substantially expanded — appended seven new major sections: Data Locations (storage/memory/calldata table, assignment rules, calldata preference pattern); Full Type Reference (comprehensive value types table including UDVT and function types, integer arithmetic notes, address payable rules, reference type members, array slices, mapping restrictions, string notes); Panic Codes table (all codes 0x01–0x51); try/catch Full Reference (full worked example with all four catch clause types and five important caveats); Function Calls — Internal vs External (call syntax, value/gas options, named args, destructuring); CREATE2 (deterministic address pre-computation with full code example); Common Patterns (withdrawal pattern, access restriction with custom errors, state machine with enum/modifiers); Global Variables & Cheatsheet (block properties, tx/message, crypto/math, address members, ABI encoding, type information); 0.8.x Changes at a Glance table (7 breaking changes)
- 1 new concept page: [[concepts/solidity-security]] — 10 security pitfalls with full code examples: (1) reentrancy — vulnerable pattern vs CEI safe pattern + nonReentrant guard; (2) `tx.origin` authentication — phishing attack example and fix; (3) integer overflow/underflow — pre-0.8 wrap behaviour, safe `unchecked` loop pattern; (4) gas limit and unbounded loops — permanent brick scenario, withdrawal pattern fix; (5) sending/receiving Ether — `transfer`/`send`/`call` comparison table, unexpected Ether via `selfdestruct`; (6) mapping deletion phantom storage — iterable mapping fix; (7) private data visibility — commit-reveal scheme; (8) dirty high-order bits in calldata; (9) authorised proxy contracts — permissionless proxy pattern; (10) call stack depth (1024 frame limit, 63/64 gas forwarding rule). 12-rule security checklist.
- index.md updated (sources + concepts tables)

---

## 2026-08-12 | ingest | Hedera Developer Course — Lecture 3 (Ethereum History, EVM & Solidity)

- Source: `raw/Blockchain_Lecture3.md` — 95 slides by Hendrik Ebbers (OpenElements / Swirlds Labs / Hedera); Ethereum history, Turing completeness, EVM architecture, sustainability (PoW vs PoS), smart contracts, Solidity fundamentals
- 1 new source page: [[sources/hedera-lecture-3-ethereum-solidity]] — full structured ingest covering: Ethereum origin (Vitalik Buterin 2013 whitepaper, 2015 launch, WoW Siphon Life motivation); Ethereum vs Bitcoin comparison table; Alan Turing biography (Enigma, Turing Machine 1936, Turing completeness, Turing Test 1950); EVM as Turing-complete system; gas as solution to the halting problem; Ethereum use cases (DeFi, NFTs, Supply Chain, Identity, Voting, DAOs, Gaming, Real Estate, Healthcare, Legal, IP); Axie Infinity NFT example + Ronin bridge hack; sustainability data (Bitcoin = UK tea kettles 30 years; ETH PoW = 22M TWh → ETH PoS = 2000 MWh, ~99.9999% reduction); cross-network comparison table (PayPal/Netflix/YouTube/Bitcoin/Ethereum); public ledger properties (Transparency, Auditability, Accessibility); smart contract gambling example (Alice + Bob → contract → winner); Ethereum distributed state machine (σt → tx → σt+1); EVM stack (max 1024 elements, 256-bit), PC, OpCodes; OpCodes table (STOP/ADD/MUL/SUB/DIV/SDIV/MOD/SMOD with gas costs); gas limit and INSUFFICIENT_GAS abort; EVM languages (Solidity, Vyper, YUL, FE); Solidity compilation (solc CLI + Docker); HelloWorld contract; Coin contract with full annotation (pragma, contract, state variables, mapping, event, constructor, functions, require, msg.sender, emit); deployment lifecycle (write → compile → deploy → constructor → unique address); contract singleton lifecycle; Solidity language reference (functions, visibility, value types, reference types, control structures, error handling, modifiers, advanced patterns)
- 1 new concept page: [[concepts/ethereum-evm]] — Ethereum history table; Buterin origin story; Ethereum vs Bitcoin table; Alan Turing biography and Turing completeness; why EVM is Turing complete and why gas solves the halting problem; distributed state machine model; account model (EOA vs contract); EVM architecture (PC, stack, memory, storage, calldata); OpCodes table; gas model; EVM languages; use cases table; Axie Infinity NFT case study; sustainability (PoW vs PoS energy data with table; cross-network comparison); public ledger properties; connections to blockchain-technology, solidity-fundamentals, hedera-network
- 1 new concept page: [[concepts/solidity-fundamentals]] — full Solidity language reference: version pragma; contract structure; HelloWorld; Coin annotated reference contract; state variables (persistent on-chain storage, public getter generation); constructor (once on deploy, singleton); functions (visibility table: public/private/internal/external); `msg.sender` and `msg.value`; events (EVM log, off-chain consumers); value types (bool, int/uint variants, fixed, address, bytes, string, enum); reference types (array, mapping, struct) with code examples; control structures; error handling (require/revert/assert/try-catch with comparison table; atomic rollback); modifiers (reusable precondition blocks, chaining); compilation lifecycle (write → solc → .bin → deploy → constructor → unique address); deployment immutability; advanced patterns (delegatecall, inheritance, using-for, libraries, import); Hedera vs Ethereum comparison (gas pricing, finality, TPS, HTS precompile)
- index.md updated (sources + concepts tables)

---

## 2026-08-12 | ingest | Hedera Developer Course — Lecture 1 (Bitcoin, Digital Currencies & Crypto Wallets)

- Source: `raw/Blockchain Lecture-1.pdf` — 62 slides by Hendrik Ebbers (OpenElements / Swirlds Labs / Hedera); Part 1 of the three-part Hedera Developer Course
- 1 new source page: [[sources/hedera-lecture-1-bitcoin-wallets]] — structured ingest covering: course structure (3-part Java + Solidity curriculum); Bitcoin history (Satoshi 2008 whitepaper at bitcoin.org, 2009 implementation, inactive 2010); Bitcoin's 4 original goals with assessment table (everyday currency ✗, common currency ✗, exchange cost ✓, cryptographic proof ✓); Bitcoin Pizza Day (Laszlo, forum post 18 May 2010, confirmed 22 May — 10,000 BTC for two pizzas, ~$190M at $19K/BTC); digital currency taxonomy (coins = store of value, stablecoins = pegged/stable medium of exchange); crypto hype drivers (FOMO, influencers, financial sovereignty, financial inclusion, digital gold); Standard Bank (ZA) × Shinhan Bank (KR) SWIFT MT103 vs Hedera stablecoin PoC (Sept 2023) with side-by-side comparison; wallet taxonomy (Hardware, Paper, Desktop, Mobile, Web; hot vs cold definitions); Coinbase Wallet, HashPack (leading HBAR wallet, daily Testnet faucet), Ledger (1000+ coins, 24-word mnemonic phrase); hands-on exercises (Coinbase price comparison, HashPack Testnet account creation); source quality assessment
- 1 new concept page: [[concepts/crypto-wallets]] — full reference: hot/cold distinction; wallet type table (Hardware/Paper/Desktop/Mobile/Web); custodial vs non-custodial model with counterparty risk; BIP-39 mnemonic phrase standard (12/24 words, 2048-word list, full wallet derivation); security features (encryption, 2FA, backup, multi-sig); wallet selection table by use case; HashPack section (HBAR + HTS, Testnet mode, EVM alias); connections to bitcoin-history and hedera-network
- [[concepts/bitcoin-history]] updated — new "Bitcoin's Four Design Goals" subsection added in Part II (Genesis), with 4-row assessment table (goal, achieved, explanation)
- index.md updated (sources + concepts tables)
- Lecture 3 (`raw/Blockchain Lecture-3.pdf`) is password-protected — cannot be read; awaiting unprotected version from user

---

## 2026-08-11 | ingest | Hedera Local Ledger — JavaScript Code (Hash Chain + Testnet Transfers)

- Source: user-provided Node.js code using `@hiero-ledger/sdk` v2.85.0; combines a local SHA-256 hash-chained `Ledger` class with real Hedera Testnet operations (ECDSA account creation, HBAR transfers, receipt + tx ID retrieval, HashScan URLs)
- 1 new example page: [[examples/hedera-local-ledger-js]] — full annotated code; two-layer architecture diagram (local audit trail references Hedera txIds); `computeHash` destructuring trick (`{ hash, ...rest }` avoids circular hashing); `setECDSAKeyWithAlias` vs `setKey` (EVM alias creation); `freezeWith + sign` transaction signing pattern with table (freeze → explicit sign → auto-sign on execute); operator exemption from `.sign()` (`privateKey: null` convention); transaction ID format (`0.0.XXXXX@seconds.nanoseconds`); HashScan URL pattern; `new Hbar(amount)` with signed values (negative = debit); improvements table (JSON.stringify ordering, persistence via HCS, Merkle tree, TypeScript discriminated union); Hiero rebrand (`@hashgraph/sdk` → `@hiero-ledger/sdk`)
- [[concepts/hedera-network]] updated — new "Developer SDK" section added: Hiero package rebrand table; `Client.forTestnet()` + `setOperator()` pattern; `setECDSAKeyWithAlias` explanation with EVM alias derivation; full `freezeWith + sign` pattern with step table; receipt and transaction ID format; `Hbar` denomination notes (tinybar, signed values, zero-sum constraint)
- index.md updated (examples table)

---

## 2026-08-11 | ingest | Hedera Developer Course — Lecture 2 (Blockchain & Hash Functions)

- Source: `raw/Lecture 2.pdf` — 49 slides by Hendrik Ebbers (OpenElements / Swirlds Labs / Hedera); blockchain fundamentals, hash function taxonomy, hashing in Java, creating a blockchain in Java, and why distributed consensus is required
- 1 new source page: [[sources/hedera-lecture-2-blockchain-hashing]] — full structured ingest covering: block anatomy (data + timestamp + prev_hash); hash chaining immutability argument; "why not a database?" pedagogical rebuttal; 5 hash specification properties (Uniformity, Efficiency, Deterministic, Surjection, One-way); 4 secure hash properties (Data Integrity, One-Way, Collision Resistance, Fixed Output Length); Digit Sum worked example (F(84001) = 13) with pass/fail analysis; MD5 history and CCC 2008 compromise (200 PS3s); SHA family evolution (SHA-0 → SHA-1 → SHA-2 → SHA-3) with status table; Java `MessageDigest` supported algorithms (12 identifiers); full Java code for `calculateHash()`, `Block` class (immutable design), `Chain` `isChainValid()` method; the single-chain attack (why recomputing subsequent hashes defeats a hash-only chain) and the need for distributed consensus
- 1 new concept page: [[concepts/cryptographic-hash-functions]] — complete reference: specification vs secure properties tables; Digit Sum analysis; MD5 compromise detail; full SHA family table with internal construction notes (SHA-3 Keccak sponge vs SHA-2 Merkle–Damgård); Java `MessageDigest` API reference; full `Block` and `isChainValid()` code with design rationale; single-chain attack explanation; security considerations (length-extension, rainbow tables, timing attacks, quantum margin)
- index.md updated (sources + concepts tables)

---

## 2026-08-10 | autoresearch | Hedera Network (HBAR)

- 4 search passes (Hedera architecture/HBAR/consensus service, governing council/enterprise deployments, native services HCS/HTS/HFS/HSCS, HBAR tokenomics/staking/ecosystem fund) + 4 deep fetches (hederacouncil.org council membership + governance, Canary Capital HBAR deep dive, OneKey HBAR tokenomics, Exponential Science Hedera services breakdown, Hedera 2025 blog "building the trust layer")
- 1 new concept page: [[concepts/hedera-network]] — full deep-dive reference: founding story (Baird + Harmon, 2018); Hashgraph consensus in full technical detail (gossip-about-gossip protocol, virtual voting derivation, ABFT formal security proof, fair ordering via median timestamps); performance table (10,000+ production TPS, 3–7s finality, $0.0001/tx, 0.000003 kWh/tx); network architecture diagram (application/services/consensus layers; main nodes vs mirror nodes vs JSON-RPC relay); all 4 native services in depth (HCS with fee table and use cases; HTS with compliance control table, atomic swaps, custom fees, HTS vs ERC-20/ERC-721 comparison; HFS with proof-of-deletion GDPR capability, 4KB/tx limit; HSCS Besu EVM, 15M gas/s, 0x167 precompile for HTS integration); governing council structure (up to 39 members, equal voting, term limits, 30+ members listed by sector); 2025 governance restructuring (Hedera Foundation, HEAT, new partnership tiers); HBAR tokenomics (50B fixed, no inflation, genesis minting, 84.8% circulating, 5 allocation categories, 7B ecosystem allocation Dec 2024, 6.5% APY staking, USD-denominated fees); real-world deployments table (16 entries: NHS cold-chain, Shinhan Bank, Meeco, Archax HSBC bonds, UNDP carbon, Lloyds/Aberdeen gilts, RBA Project Acacia, Bank of England/BIS, Georgia registry, EQTY Lab/NVIDIA, Wyoming FRNT); 2025 strategic products (AI Studio, HashSphere, Asset Tokenisation Studio ERC-3643/ERC-1400, Axelar 60-chain integration, Blockaid security); ecosystem table (DEX/DeFi, NFTs, stablecoins, RWA, identity, developer tools); full competitive comparison table vs Ethereum/Solana/Bitcoin; risks and criticisms table (centralisation, council power, IP history, ecosystem maturity, TPS claims vs reality, quantum vulnerability)
- 1 new synthesis page: [[synthesis/research-hedera-network]] — argues: ABFT is a qualitatively different (not just quantitatively better) security guarantee; council governance solves the "who is liable?" problem for regulated enterprise — with real caveats on centralisation; USD-fixed fees solve a real enterprise cost-planning problem nobody else has solved; native HTS compliance primitives are protocol-level (not bolt-on) regulated-asset infrastructure; 2025 trajectory (CBDCs, real estate registries, tokenised gilts) reveals shape of next institutional blockchain wave; AI + DLT intersection (AI Studio, EQTY Lab) is structurally novel; cross-domain connections to DLT, microcredentials, prompt injection (irreversible agentic txns), social engineering, privacy/GDPR; 5 open questions (permissionless nodes timeline, DeFi TVL vs Ethereum, HashSphere's effect on public chain value proposition, treasury-funded staking depletion, AI audit logs under adversarial conditions)
- index.md updated (concepts + synthesis tables)

---

## 2026-08-10 | autoresearch | Distributed Ledger Technology (DLT)

- 3 initial search passes (DLT types/architecture, DAG/Hashgraph/Tangle/Holochain comparison, enterprise permissioned platforms) + 2 successful deep fetches (Coinpaprika comprehensive DLT overview, Hedera Knowledge Centre) + 3 supplementary searches (Hyperledger Fabric architecture, R3 Corda architecture, DLT types TPS comparison)
- 1 new concept page: [[concepts/distributed-ledger-technology]] — full reference covering: formal definition (DLT vs blockchain vs traditional database comparison table), core architectural components (nodes, ledger, consensus, cryptography, P2P, smart contracts), complete DLT taxonomy (blockchain — linear/block-based; DAG — IOTA Tangle, feeless parallel transaction referencing; Hashgraph — gossip-about-gossip + ABFT virtual voting, 250K+ TPS, Hedera; Holochain — agent-centric, no global consensus, DHT peer validation; other architectures — Tempo/Radix, Block-DAG/Kaspa), consensus mechanism reference table (PoW/PoS/DPoS/PBFT/Raft/SmartBFT/ABFT/DAG approval/DHT), permission model matrix (public permissionless / private permissioned), enterprise platforms in depth (Hyperledger Fabric 3.0: execute-order-validate pipeline, MSP, channels, chaincode, SmartBFT BFT consensus March 2024, Private Data Collections; R3 Corda: states/transactions/contracts/flows/notary/vault/CorDapps, point-to-point model, uniqueness consensus, real-world deployments including Fnality; Hyperledger Besu: EVM-compatible, permissioned, IBFT 2.0/QBFT), use cases by sector table (finance, supply chain, healthcare, energy, government, IoT, digital identity, IP), advantages table, limitations (scalability trilemma, energy, GDPR tension, 51% attack, interoperability, irreversibility), DLT type comparison summary table
- 1 new synthesis page: [[synthesis/research-distributed-ledger-technology]] — argues: DLT is a taxonomy not a technology (full tree diagram); consensus mechanism choice determines everything (table: goal → mechanism → why); enterprise permissioned DLTs are distributed databases with BFT and crypto audit trails, not ideologically decentralised systems; Corda's point-to-point model is the correct mental model for financial markets (bilateral + notary, not network-wide broadcast); GDPR tension is structural and unresolvable (pragmatic compromise: off-chain data + on-chain hash); full architecture decision framework tree; cross-domain connections to Bitcoin history, blockchain microcredentials, prompt injection (irreversible agentic transactions), and social engineering (dominant DLT attack vector); 5 open questions (trilemma, Corda adoption, consortium governance, IOTA coordinator removal, quantum computing migration)
- index.md updated (concepts + synthesis tables)

---

## 2026-07-28 | autoresearch | History of Bitcoin

- 5 search passes (cypherpunk origins/whitepaper, major milestones 2010–2017, institutional/ETF/2020–2025, FTX/Luna/MicroStrategy, price history) + 3 successful deep fetches (Ledger Academy origins, CMO Intern complete timeline, First Report detailed timeline)
- 1 new concept page: [[concepts/bitcoin-history]] — full chronological history across 8 parts: cypherpunk predecessors table (DigiCash/Hashcash/B-money/BitGold/RPOW), 2008 context and whitepaper technical innovations, genesis block and embedded message, 2009 launch and first transaction, 2010–2012 (pizza day, Mt. Gox founding, first halving), 2013–2015 (Silk Road, $1000 ATH, Mt. Gox collapse, Crypto Winter I), 2016–2018 (SegWit, BCH/BTG forks, CME futures, $20K ATH, Crypto Winter II), 2019–2021 (Lightning, MicroStrategy, Tesla, $1T market cap, El Salvador, Taproot, $69K ATH), 2022–2023 (Luna/3AC/FTX collapses, BlackRock ETF filing, recovery), 2024–2025 (spot ETF approval, 4th halving, $126K ATH); complete halving cycle table with dates/prices/ATH/days-to-ATH; price history table 2009–2025; five recurring themes; Satoshi identity analysis
- 1 new synthesis page: [[synthesis/research-bitcoin-history]] — argues: Bitcoin solved double-spend where all predecessors failed; each bull market had a structurally different driver; ETF approval is the most significant event since genesis block; every catastrophic loss was at the custody layer never the protocol; Satoshi's disappearance was a deliberate design choice for censorship-resistance; Satoshi identity candidates table; cross-domain connections to blockchain technology, microcredentials, privacy/GDPR, and AI ethics; open questions on halving cycle decoupling and long-run miner incentives
- index.md updated (concepts + synthesis tables)

---

## 2026-07-28 | autoresearch | Microcredential Blockchain / DLT

- 5 search passes (blockchain microcredentials/VC/DLT, W3C VC/DID, Blockcerts/OpenBadges platforms, GDPR/scalability challenges, VC 2.0 specifics) + 4 deep fetches (VerifyEd credentials guide, VerifyEd microcredentials guide, TrueOriginal W3C VC guide, DoxyChain microcredentials on blockchain)
- 1 new concept page: [[concepts/blockchain-microcredentials]] — full reference covering: microcredential taxonomy (nano → nano-credential → badge → micro-cert → bootcamp → stackable), the trust problem with traditional certs, the four-layer standards architecture (application / credential / identity / ledger), W3C VC 2.0 data model with annotated JSON example, DID methods comparison table (did:web, did:ethr, did:ion, did:key, did:ebsi), VC 2.0 improvements over 1.x (SD-JWT, BBS+, Status List 2021, CBOR), Verifiable Presentations + selective disclosure, OpenBadges 3.0 alignment with VC 2.0, EBSI/Europass EDCI, three-party trust triangle diagram, technical issuance-to-verification workflow, on-chain vs off-chain architecture table, digital credential wallets, 9 major platforms (Blockcerts, VerifyEd, POK, EBSI, IBM, Sony, Singapore SkillsFuture), sector adoption across HE/tech/healthcare/manufacturing, government policy table (6 countries + EU), benefits table, challenges (GDPR/EDPB 02/2025, scalability trilemma, ATS adoption gap, key management, quality assurance), future trends table
- 1 new synthesis page: [[synthesis/research-blockchain-microcredentials]] — argues the real innovation is verifier independence (not just tamper-proofing); on-chain vs off-chain architecture decision; W3C VC 2.0 + OpenBadges 3.0 as the convergence standard; adoption lag concentrated in employer ATS infrastructure; quality assurance as the non-technical blocker; DLT choice framework table; cross-domain connections to blockchain fundamentals, privacy/GDPR, FIDO/passkeys, and AI ethics; open research questions
- index.md updated (concepts + synthesis tables)

---

## 2026-07-28 | autoresearch | Browser Extensions

- 5 search passes (MV3 architecture, components/service workers, cross-browser/permissions, security/supply chain, dev frameworks) + 3 deep fetches (FreeToolKit MV3 guide, MDN WebExtensions, MV2 vs MV3 analysis)
- 1 new concept page: [[concepts/browser-extensions]] — full reference covering: WebExtensions API cross-browser matrix, 5-component architecture (manifest, service worker, content scripts, popup/UI, options) with annotated code examples for each, message-passing patterns (one-shot and long-lived ports), storage API comparison table, permissions model (4 categories), MV2 vs MV3 comparison table, cross-browser framework comparison (WXT, Plasmo, CRXJS, web-ext), development workflow (loading unpacked, debugging, web-ext CLI), publishing to Chrome Web Store and Firefox AMO, security model, real-world incident table (ShadyPanda, 35-extension compromise, SpyStore campaign), secure development checklist, full WebExtensions API quick-reference
- 1 new synthesis page: [[synthesis/research-browser-extensions]] — argues extensions are a distributed system in miniature; analyses MV3 as a security trade-off not a pure improvement; identifies content scripts as the highest-risk code surface; establishes supply chain as the dominant threat vector; cross-domain connections to prompt injection, JS fundamentals, web security, and CI/CD; ASCII architecture diagram; open gaps
- index.md updated (concepts + synthesis tables)

---

## 2026-07-28 | autoresearch | Prompt Injection

- 3 search passes (attack types/LLM01, jailbreak techniques, defences) + 3 deep fetches (OWASP LLM01:2025, Vectra AI, Palo Alto Networks)
- 1 new concept page: [[concepts/prompt-injection]] — full taxonomy (6 attack classes: direct, indirect, stored, RAG poisoning, multimodal, agentic), Promptware Kill Chain (7 stages), concrete technique reference table (10 techniques), real-world CVE table (7 incidents including EchoLeak CVSS 9.3 and GitHub Copilot RCE CVSS 9.6), attack success rate benchmarks (up to 84% in agentic systems), six-layer defence framework, emerging technical controls (PromptGuard, Attention Tracker, AgentVisor), compliance mapping across 7 frameworks
- 1 new synthesis page: [[synthesis/research-prompt-injection]] — argues the architectural root cause is unsolvable by filtering alone; establishes cross-domain connections to SQL injection, MCP security, social engineering, and STRIDE threat modelling; defence priority order; open research questions
- index.md updated (concepts + synthesis tables)

---

## 2026-07-28 | autoresearch | Social Engineering

- 3 search passes (attack types/techniques, psychological principles, defences/countermeasures) + 3 deep fetches (ESET, Secureframe, Doppel 2025)
- 1 new concept page: [[concepts/social-engineering]] — full taxonomy (15+ attack types across email, voice, physical, and advanced categories), Cialdini's 6 principles mapped to exploitation patterns, 5 real-world case studies (Bybit $1.4B, MGM, $25M deepfake CFO, M&S £440M, Twitter 2020), red-flag recognition signals, three-layer defence framework (people/process/technology), key statistics (2024–2025)
- 1 new synthesis page: [[synthesis/research-social-engineering]] — cross-domain connections to threat modelling, OWASP Top 10, CIA-AAA security requirements, and HCI; deepfake inflection-point analysis; MFA limitation analysis; defence priority order; open research questions
- index.md updated (concepts + synthesis tables)

---

## 2026-07-26 | project | Learnix — Encrypted `.env` + PyArmor Build Pipeline

- 1 new example page: [[examples/learnix-encrypted-env-build]] — `build.ps1` (single PowerShell script) does Fernet-encrypt `.env` → PyArmor-obfuscate just the decrypt-key module → PyInstaller onefile/windowed package → delete all build-time secret artifacts; `src/_secrets_loader.py` is the one unavoidable runtime Python file (decrypts inside the frozen app); `main.py` branches frozen vs dev
- 1 new concept page: [[concepts/pyinstaller-secret-protection]] — general pattern (encrypt data file + scope PyArmor obfuscation to the key module only, not the whole app, to avoid blinding PyInstaller's static import analysis) plus an explicit table of what this defends against (casual inspection) vs. doesn't (a determined attacker, or the underlying "live keys ship client-side" problem — needs a backend proxy)
- 1 new resource page: [[resources/pyarmor]] — v9.2.6 CLI invocation gotcha (`python -m pyarmor` fails, `python -m pyarmor.cli` works), license tiers, install notes
- Verified for real: ran the build script end-to-end, confirmed cleanup deleted all secret artifacts, launched the built exe, confirmed no console window and no crash (decrypt path actually worked), killed it
- Two gotchas hit and documented: a PowerShell here-string got mangled passing through the tool-call transport (fixed by writing an actual file instead of inline command text); `python -m pyarmor` vs `python -m pyarmor.cli` on v9.x

---

## 2026-07-24 | project | Learnix — Font-Size Setting + Slower Forethought SRL Pacing

- 1 new example page: [[examples/learnix-fontsize-and-srl-pacing]] — per-user font-size preference added to Settings → Appearance via CTk's `set_widget_scaling()` (live, no window rebuild, unlike colour theming); Forethought-phase SRL steps now require 3 distinct-message keyword mentions instead of 1 to tick complete
- 1 new concept page: [[concepts/customtkinter-widget-scaling]] — CTk's built-in live font/widget rescaling mechanism, contrasted with the heavier rebind-and-rebuild pattern colour theming needs (see [[concepts/customtkinter-window-lifecycle]])
- No source ingest this session — both features built directly against the existing Learnix codebase and prior wiki knowledge of the CTk teardown/theming pattern

---

## 2026-07-23 | project | ICT2216 Practical Test — Secure Web App + DevSecOps Stack

- 1 new example page: [[examples/ict2216-practical-test-secure-webapp]] — Flask HTTPS login app (CSRF, non-root Docker, PBKDF2 hashing, NIST breach-password check), Gitea, SonarQube (local scan + hotspot fixes), ESLint security scanning, and a working self-hosted Gitea Actions CI/CD pipeline (5 jobs)
- 1 new learning page: [[learning/gitea-act-runner-dood-networking]] — 4 distinct Docker-outside-of-Docker gotchas (duplicate socket mount, isolated per-job network, bind mounts becoming empty dirs, 127.0.0.1 vs host.docker.internal) hit registering and running a real `act_runner`
- 1 new resource page: [[resources/gitea-and-act-runner]] — Gitea + act_runner setup, admin bootstrap (no env-var auto-provisioning), runner registration
- Pages updated: [[concepts/docker-compose]] (new DooD section), [[concepts/github-actions-cicd]] (new Gitea Actions section), [[concepts/secure-design-implementation]] (noted a real divergence from the "don't breach-check at login" guidance, made on explicit stakeholder request)
- Real CVE caught by the pipeline's own `pip-audit` step: Flask 3.0.3 (`PYSEC-2026-2151`), fixed by upgrading to 3.1.3 — direct evidence the CI actually runs rather than just existing as YAML

---

## 2026-07-22 | ingest | Breached Password List Checking — Implementation Pattern

- No new pages created (no new address used)
- Pages updated: [[concepts/secure-design-implementation]] — added "Password Policy — Breached Password List Checking" subsection under Authentication Design; includes NIST 800-63B §5.1.1.2 requirement, SecLists reference (`10-million-password-list-top-1000.txt`), when-to-apply table, Python implementation (set-based O(1) lookup + HIBP k-anonymity API option)
- Pages updated: [[concepts/secure-software-requirements]] — expanded NIST breach checking row with implementation reference and key rules (never check at login, apply at registration/change/reset)

---

## 2026-07-22 | ingest | ICT2216 Lecture 9 — Spoken Transcript (Static Code Analysis)

- Pages created: [[sources/ICT2216-lecture-9-transcript]] (c-000122)
- Pages updated: [[concepts/static-code-analysis]] — added "Historical Context" section (Microsoft SDL: manual inspection → mass unit testing → SDV framework for device drivers, 1990s–2000s); expanded "Limitations" with salt-after-hashing design error example and LLM determinism vs classical SAST comparison table
- Pages updated: [[concepts/security-testing-and-verification]] — added professional engagement pricing (lines of code / man-days, SGD 50K–100K range) to Code Inspection section
- Pages updated: [[concepts/software-configuration-management]] — added 7-branch production Git model (live, hotfix, UAT, bug-fix, development, feature) with full release and hotfix cycles
- Note: Case studies (Indirect Prompt Injection, Bandai Channel, Phone Number, Genshin Impact) already covered in c-000112; not duplicated
- Indexes updated: wiki/index.md, wiki/sources/_index.md

---

## 2026-07-22 | ingest | ICT2216 Lecture 10 — Module Overview & Secure Software Concepts

- Pages created: [[sources/ICT2216-lecture-10-module-overview-secure-concepts]] (c-000121)
- Pages updated: [[concepts/owasp-top-10]] — added 4 new 2025/2026 case studies (HSBC India uppercase passwords under A04; Europcar GitLab breach under A03; Gladinet CVE-2025-30406 under A04 + A08; X/Twitter 2.8B insider breach under A09)
- Pages updated: [[concepts/secure-design-implementation]] — added Security Quality Gates section (4 gates, phase transitions) + Sprint+Security Approaches section (Security Sprint vs Every Sprint; Every Sprint preferred per Microsoft SDL)
- Note: raw file named "Lecture 10" but internally titled "Lecture 1: Module Overview & Secure Software Concepts" — filed under actual content
- OWASP Top 10 core content already fully covered (c-000024, created 2026-05-11); Code Review Heuristic (C code, 4 bugs) already in vault
- Indexes updated: wiki/index.md, wiki/sources/_index.md

---

## 2026-07-20 | ingest | ICT2216 Lab 9 — SonarQube on Docker (Windows run)

- Page updated: [[examples/ict2216-lab9-sonarqube]] — added "Actual run on Windows" section with real commands used to bring the stack up: `docker compose` (v2 syntax) vs `docker-compose`, Docker Desktop not running trap (`docker info` vs `docker --version`), `Start-Process` to launch Desktop, polling loops for engine readiness and SonarQube's `/api/system/status` endpoint.
- No new concept page — this is operational/environment detail on top of the existing Lab 9 example.

## 2026-07-19 | save | Conversation Ingest — DeepSeek + Local Agent Deployment

- Pages created: [[entities/deepseek]], [[resources/ollama-local-inference]]
- Pages updated: [[resources/ai-agent-frameworks]] (local deployment section added)
- Content: DeepSeek model lineup (V3, R1), OpenAI-compatible API, agent suitability, hardware requirements; Ollama local inference setup, framework integration snippets, tool calling model guide; OpenClaw clarification (not required for local deployment)

## 2026-07-19 | autoresearch | How to Set Up AI Agents

- Rounds: 2 | Searches: 5 | Fetches: 5
- Pages created: [[concepts/ai-agent-architecture]], [[resources/ai-agent-frameworks]], [[sources/furmanets-ai-agents-2026]], [[sources/alice-labs-agent-frameworks-2026]], [[synthesis/research-ai-agent-setup]]
- Key finding: Production agents fail because chat logs are used as state, vector DBs as first memory layer, prose as plans, and guardrails added last. Correct order: tool contracts → state reducer → tracing → evals → policy gating → memory

## 2026-07-16 | ingest | ICT2216 Lecture 9 — Static Code Analysis (Part 1)

- Source: `raw/ICT2216 Lecture 9 Secure Software Development.md` (local file)
- Pages created: [[sources/ICT2216-lecture-9-static-code-analysis]], [[concepts/static-code-analysis]]
- Pages updated: [[concepts/security-testing-and-verification]] (penetration testing methodologies + code inspection sections added)
- Key finding: Static analysis covers all paths simultaneously; 6 techniques from pattern matching to theorem proving; false positives drive alert fatigue; the heap is the primary limitation

## 2026-07-12 | autoresearch | LaTeX Formatting

- Rounds: 2
- Searches: 5 | Sources fetched: 5
- Pages created: [[concepts/latex-formatting]], [[resources/latex-essential-packages]], [[sources/overleaf-learn-latex-30min]], [[sources/emonts-latex-best-practices]], [[synthesis/research-latex-formatting]]
- Key finding: `eqnarray` and `$$...$$` are deprecated in modern LaTeX; BibLaTeX + biber replaces BibTeX; `cleveref` must always load after `hyperref`; `\caption` before `\label` in floats

## 2026-07-09 | ingest | ICT2216 Lab 11 (OWASP ZAP + Burp Suite)

- Source: `X11a - Vulnerability Assessment with OWASP ZAP.pdf`, `X11b - Fuzzing with Burp Suite.pdf` (local lab files)
- Updated: [[concepts/security-testing-and-verification]] — new "DAST Tools: OWASP ZAP and Burp Suite" section (ZAP Automated Scan workflow, Burp Intruder attack types + Grep-Extract, ZAP vs Burp comparison table)
- Created: [[examples/ict2216-lab11-zap-burp]] — full lab walkthrough (DVWA target, ZAP alerts, Cluster bomb fuzzing, Grep-Extract for redirect-based success detection)
- Updated: `wiki/index.md` Examples table, `wiki/hot.md`

## 2026-07-09 | ingest | OWASP Security Terminology Cheat Sheet (web source)

- Source: https://cheatsheetseries.owasp.org/cheatsheets/Security_Terminology_Cheat_Sheet.html
- Source page: [[sources/owasp-security-terminology-cheat-sheet]] (c-000104)
- New concept page: [[concepts/security-terminology]] (c-000105)
  - **Data handling**: Encoding (format conversion, not a security control) vs Escaping (context-specific, prevents injection) vs Sanitisation (destroys content, secondary defence) vs Serialisation (object persistence; insecure deserialisation → RCE)
  - **Cryptography**: Encryption (confidentiality, reversible with key) vs Hashing (integrity/passwords, one-way, must salt) vs Digital Signatures (authenticity + non-repudiation; private key signs, public key verifies)
  - **Identity**: Authentication AuthN ("Who are you?") vs Authorisation AuthZ ("Are you allowed?"; 401 vs 403 distinction)
  - **Federated identity**: IdP (manages identity, provides AuthN), RP (OAuth2/OIDC consumer), SP (SAML consumer = RP equivalent), Principal (entity being authenticated)
  - Includes HMAC vs digital signature distinction (shared secret vs asymmetric)
- Counter: 104 → 106

## 2026-07-09 | ingest | OWASP Cheat Sheet Series — Alphabetical Index (web source)

- Source: https://cheatsheetseries.owasp.org/Glossary.html
- Source page: [[sources/owasp-cheat-sheet-series-index]] (c-000102)
- Resource page: [[resources/owasp-cheat-sheet-series]] (c-000103)
  - Complete A–Z catalogue of all 120 OWASP cheat sheets with direct URLs and language tags
  - Relevance map linking each cheat sheet to existing vault concept pages
  - AI-era additions table (7 new cheat sheets: AI Agent Security, LLM Prompt Injection, RAG Security, Secure AI Model Ops, Secure Coding with AI, MCP Security, AML Sanctions AI Agent Payments)
  - Note: URL says `Glossary.html` but the page is actually the alphabetical index — security terminology is at `Security_Terminology_Cheat_Sheet.html`
- Counter: 102 → 104

## 2026-07-09 | ingest | ICT2216 Lecture 8 — Secure Software Implementation (Part 3): Test Automation & Security Testing References

- Source: `raw/ICT2216 Lecture 8 Secure Software Development.md`
- Source page: [[sources/ICT2216-lecture-8-secure-testing]] (c-000100)
- New concept page: [[concepts/security-testing-and-verification]] (c-000101)
  - Testing pyramid, SDLC security integration
  - OWASP ASVS: 14 verification categories, 3 assurance levels
  - ASVS V2.1 password rules (12 requirements aligned with NIST SP 800-63)
  - ASVS V2.4 credential storage (bcrypt ≥10 / PBKDF2 ≥100,000; salt ≥32 bits)
  - ASVS V2.5 credential recovery (no secret questions; TOTP/push)
  - ASVS V10 malicious code (backdoors, time bombs, phone-home)
  - OWASP WSTG: 11 test categories, how ASVS → WSTG workflow operates
  - Authentication testing: lockout mechanism (step-by-step test), CAPTCHA 10-point evaluation, generic error messages (account enumeration prevention)
  - Security test report structure (4 sections + severity ratings)
- Updated: [[concepts/secure-deployment-practices]] (c-000098)
  - Added logging testing section: what logs must not contain, log rotation testing, log access control, anomaly detection via log review (40x/50x patterns)
- Counter: 100 → 102

## 2026-06-28 | ingest | LeetCode 1768 — Merge Strings Alternately (debugging case study)

- Source: `raw/leetcode-merge-alternately-2026-06-28.md`
- Summary: [[sources/leetcode-merge-alternately]]
- Pages created: [[sources/leetcode-merge-alternately]] (c-000094), [[examples/leetcode-merge-alternately-python]] (c-000095)
- Pages updated: [[concepts/array-manipulation-patterns]] (Pattern 6 expanded from stub to full pattern), [[wiki/index.md]], [[wiki/sources/_index.md]]
- Key insight: No new concept page — this problem fills out the existing Pattern 6 stub (Two-Pointer Merge). Three classic beginner Python bugs documented: `list + str` TypeError, shared-index IndexError, and list-vs-string return type mismatch. The `or` vs `and` loop condition and `if/if` vs `if/elif` branch structure are the key correctness details.

---

## 2026-07-09 | ingest | ICT2216 Lecture 7 — Spoken Lecture Transcript (supplement)

- Source: `raw/ICT2216-lecture-7-transcript-2026-07-09.md`
- Summary: [[sources/ICT2216-lecture-7-transcript]]
- Pages created: [[sources/ICT2216-lecture-7-transcript]] (c-000099)
- Pages updated (appended): [[concepts/secure-input-validation]], [[concepts/secure-deployment-practices]], [[wiki/index.md]], [[wiki/sources/_index.md]]
- New insights: (1) Stored procedures protect schema from source code leakage — prepared statements expose table/column names in source; procedures only expose function names. (2) Version pinning debate — patch/minor: auto-update; major: manual review; sufficient test coverage is the prerequisite. (3) POSIX epoch time sidesteps leap seconds (23:59:60) — timestamp-format storage does not. (4) Log injection enables reverse shell — attacker injects shell payload into unsanitised log, executes via log processor, then deletes the entry. (5) ZIP bomb / CPOM attack — decompression must check size and compression ratio, not just file type.

---

## 2026-07-02 | ingest | ICT2216 Lecture 7 — Secure Software Implementation (Part 2)

- Source: `raw/ICT2216 Lecture 7 Secure Software Development.md`
- Summary: [[sources/ICT2216-lecture-7-secure-coding]]
- Pages created: [[sources/ICT2216-lecture-7-secure-coding]] (c-000096), [[concepts/secure-input-validation]] (c-000097), [[concepts/secure-deployment-practices]] (c-000098)
- Pages updated: [[wiki/areas/secure-software-development]], [[wiki/index.md]], [[wiki/sources/_index.md]]
- Key insight (input validation): Allow-list always beats block-list; ReDoS is a genuine DoS vector from evil regex patterns with nested quantifiers — mitigation is RE2 (linear-time) or timeout; SQL injection prevention gold standard is parameterised queries + least-privilege DB account.
- Key insight (deployment): Never log sensitive data or set TRACE in production (OpenAI Codex case: 37 TB/21 days); log injection is a real attack — sanitise before logging; never hardcode secrets anywhere in committed files — use GitHub Secrets → env vars at runtime; pin Docker image tags and run as non-root.

---

## 2026-06-28 | ingest | LeetCode 3 — Longest Substring Without Repeating Characters

- Source: `raw/leetcode-longest-substring-2026-06-28.md`
- Summary: [[sources/leetcode-longest-substring]]
- Pages created: [[sources/leetcode-longest-substring]] (c-000091), [[concepts/sliding-window-patterns]] (c-000092), [[examples/leetcode-longest-substring-python]] (c-000093)
- Pages updated: [[wiki/areas/computer-science]], [[wiki/index.md]], [[wiki/sources/_index.md]]
- Key insight: Sliding window reduces O(N²) brute force to O(N) by maintaining a valid window `[left, right]` rather than restarting from every index. The shrink-left (set) and jump-left (last-index map) variants are identical asymptotically; the map variant is faster in practice and handles the "stale duplicate outside current window" edge case via a `>= start` guard.

---

## 2026-06-28 | ingest | LeetCode 2 — Add Two Numbers

- Source: `raw/leetcode-add-two-numbers-2026-06-28.md`
- Summary: [[sources/leetcode-add-two-numbers]]
- Pages created: [[sources/leetcode-add-two-numbers]] (c-000088), [[concepts/linked-list-patterns]] (c-000089), [[examples/leetcode-add-two-numbers-python]] (c-000090)
- Pages updated: [[wiki/areas/computer-science]], [[wiki/index.md]], [[wiki/sources/_index.md]]
- Key insight: Two canonical linked-list techniques combined — the dummy head node eliminates the first-node special case; the `or carry != 0` loop guard handles the final carry that outlives both input lists. Both are reusable across virtually all linked-list construction problems.

---

## 2026-06-28 | ingest | LeetCode 1946 — Maximum Element After Decreasing and Rearranging

- Source: `raw/leetcode-max-element-rearranging-2026-06-28.md`
- Summary: [[sources/leetcode-max-element-rearranging]]
- Pages created: [[sources/leetcode-max-element-rearranging]] (c-000085), [[concepts/greedy-patterns]] (c-000086), [[examples/leetcode-max-element-rearranging-python]] (c-000087)
- Pages updated: [[wiki/areas/computer-science]], [[wiki/index.md]], [[wiki/sources/_index.md]]
- Key insight: Sort eliminates the rearrangement degree of freedom in O(n log n); the greedy cap `arr[i] = min(arr[i], arr[i-1] + 1)` applied left-to-right on a sorted array is provably optimal because taking less never helps and taking more violates the constraint.

---

## 2026-06-28 | ingest | LeetCode 1441 — Build an Array With Stack Operations

- Source: `raw/leetcode-stack-ops-2026-06-28.md`
- Summary: [[sources/leetcode-stack-ops]]
- Pages created: [[sources/leetcode-stack-ops]] (c-000082), [[concepts/simulation-patterns]] (c-000083), [[examples/leetcode-stack-ops-python]] (c-000084)
- Pages updated: [[wiki/areas/computer-science]], [[wiki/index.md]], [[wiki/sources/_index.md]]
- Key insight: Simulation problems translate rules directly into code. The two sub-patterns here — converting a list to a set for O(1) membership, and using `not target_set` as a clean early-exit guard — are reusable across all stream-simulation problems.

---

## 2026-06-28 | ingest | LeetCode 1365 & 448 — Count Smaller / Find Disappeared

- Source: `raw/leetcode-count-missing-2026-06-28.md`
- Summary: [[sources/leetcode-count-missing]]
- Pages created: [[sources/leetcode-count-missing]] (c-000080), [[examples/leetcode-count-missing-python]] (c-000081)
- Pages updated: [[concepts/array-manipulation-patterns]] (Pattern 7 Prefix Sum on Frequency Array + Pattern 8 Set Difference added), [[wiki/index.md]], [[wiki/sources/_index.md]]
- Note: LeetCode 645 (Set Mismatch) appeared again in the same session but was already ingested as c-000078/079 — skipped.
- Key insight: Bounded value ranges (0–100 constraint) unlock the prefix sum trick — O(R) space + O(1) per query beats sorting. Python `set` difference (`A - B`) is the idiomatic tool for "what's in the universe but not the array?"

---

## 2026-06-28 | ingest | LeetCode 645 — Set Mismatch

- Source: `raw/leetcode-set-mismatch-2026-06-28.md`
- Summary: [[sources/leetcode-set-mismatch]]
- Pages created: [[sources/leetcode-set-mismatch]] (c-000078), [[examples/leetcode-set-mismatch-python]] (c-000079)
- Pages updated: [[concepts/array-manipulation-patterns]] (Pattern 4 Frequency Count + Pattern 5 Math Sum Identity added), [[wiki/index.md]], [[wiki/sources/_index.md]]
- Key insight: `dict.get(key, 0)` and `Counter` are two expressions of the same frequency-count pattern; the math sum identity (`sum(nums) - sum(set(nums))`) solves duplicate/missing in O(1) extra space when the expected aggregate is known.

---

## 2026-06-28 | ingest | LeetCode Array Basics — chat session (1929, 1470, 485)

- Source: `raw/leetcode-array-basics-2026-06-28.md`
- Summary: [[sources/leetcode-array-basics]]
- Pages created: [[concepts/array-manipulation-patterns]] (c-000076), [[examples/leetcode-array-basics-python]] (c-000077), [[sources/leetcode-array-basics]] (c-000075)
- Pages updated: [[wiki/index.md]], [[wiki/sources/_index.md]], [[wiki/areas/computer-science]]
- Key insight: Three named array patterns — concatenation, split-midpoint interleave, and linear scan with running counter — cover a large fraction of Easy-tier array problems.

---

## 2026-06-25 | project | ICT2216 TrialGuard — CodeQL restored + GitHub Actions action version deprecations

- Restored `codeql-analysis` job to `.github/workflows/ci-cd.yml` (removed in commit d49f989 due to GHAS limitation on personal private repos)
- Bumped `github/codeql-action` v3 → v4 across all three steps (init, analyze, upload-sarif); v3 deprecated December 2026
- Fixed Node 20 deprecation warnings: pinned `actions/checkout` to `@v4.3.0`, `actions/setup-python` to `@v5.6.0`, `actions/upload-artifact` to `@v4.6.2`; left `actions/setup-node` as floating `@v4` (pinned `@v4.4.2` resolved to a non-existent release)
- Key gotcha: linter auto-bumped `@v4.4.0` to `@v4.4.2` (non-existent); replace_all on `@v4` inside `@v4.3.0` doubled to `@v4.3.0.3.0`
- Also: replaced `PhotoSlot` placeholder in `Researchers.jsx` with actual `cohort.gif`; learned `objectFit: 'contain'` vs `'cover'`; dropping the fixed-aspect-ratio wrapper and using bare `<img width: 100%>` lets the image set the container height naturally
- Created: [[learning/github-actions-version-deprecations]]
- Updated: [[concepts/github-actions-cicd]] (new "Action Version Management" section)

---

## 2026-06-26 | setup | Epistemic Critique Skills

- New template: [[_templates/argument.md]] — structured argument note (claim, premises, evidence, counterarguments, falsifiability, belief history)
- New skill: `/critique` — full epistemic audit (18 fallacies, premise table, 8 cognitive biases, evidence quality, contradiction check against vault, steelman, falsifiability rating, verdict with confidence revision)
- New skill: `/steelman` — constructs the strongest opposing case then attacks your position; delivers clear verdict (argument survives / steelman wins / draw)
- New skill: `/track-belief` — snapshots confidence + position into Belief History table; tracks revision and abandonment; review mode shows trajectory across all snapshots
- New folder: [[wiki/arguments/_index.md]] — index with Active / Revised / Abandoned tables
- Updated: CLAUDE.md Plugin Skills table and vault structure

---

## 2026-06-26 | autoresearch | Kubernetes

- Rounds: 2 | Searches: 8 | Sources fetched: 4 | Pages created: 3
- New concept: [[concepts/kubernetes]] — full reference: architecture (control plane + worker nodes), all 7 workload types, Service types (ClusterIP/NodePort/LoadBalancer/ExternalName), Ingress, ConfigMap/Secret/PVC, RBAC, Pod Security Standards, Helm 4.0, managed services (GKE/EKS/AKS), kubectl commands, Kubernetes vs Docker Compose decision framework
- New source: [[sources/kubernetes-official-docs]]
- Synthesis: [[synthesis/research-kubernetes]]
- Addresses assigned: c-000073 – c-000075
- Key finding: Secrets are NOT encrypted in etcd by default (only base64-encoded); EncryptionConfiguration must be explicitly enabled for production clusters

---

## 2026-06-25 | autoresearch | Data Mapping

- Rounds: 2 | Searches: 5 | Sources fetched: 4 | Pages created: 4
- New concept: [[concepts/data-mapping]] — techniques (9 types), transformation types (8), 12-step process, mapping document structure, ETL vs ELT, object mapping (DTO/AutoMapper), tools landscape
- New sources: [[sources/airbyte-data-mapping-guide]], [[sources/atlan-data-mapping-guide]]
- Synthesis: [[synthesis/research-data-mapping]]
- Addresses assigned: c-000069 – c-000072
- Key finding: schema matching (are these equivalent?) ≠ schema mapping (how to transform one to the other) — conflating them is a common source of integration bugs

---

## 2026-06-25 | ingest | ICT2216 Lecture 6 — Secure Software Implementation

- Source: [[sources/ICT2216-lecture6-secure-implementation]]
- New concept: [[concepts/fido-passkeys-passwordless]] — FIDO Alliance, passkeys (registration/login flow), OTP/magic link design constraints, platform limitations (cross-platform inconsistency, lock-in)
- Updated: [[concepts/secure-design-implementation]] — new "SSL/TLS Security Analysis" section: incompatibility table, why salted hashing forces cleartext transmission, why phishing survives TLS, MitM SSL stripping, HSTS, PFS, cipher suite selection, SRP (RFC 5054), Security Theatre
- Updated: [[concepts/github-actions-cicd]] — DevSecOps definition, CI vs Continuous Delivery vs Continuous Deployment distinction table
- Address assigned: c-000068 (fido-passkeys-passwordless)

## 2026-06-23 | project | ICT2216 Lab 8 — ESLint SAST integrated into TrialGuard CI/CD

- Pages updated: [[examples/ict2216-lab8-static-code-analysis]] (added "Project Implementation" section)
- Key findings: GitHub Code Scanning unavailable on personal private repos → replaced upload-sarif with upload-artifact; explicit permissions block drops contents:read (breaks checkout); Vite+React needs no Babel parser for ESLint JSX; eslint-plugin-security detected real timing attack in Signup.jsx; Node 20 deprecated on runners → Node 24; CodeQL removed (requires Code Scanning)

## 2026-06-23 | ingest | ICT2216 Lab 9 — SonarQube

- Pages created: 2 (instructions_lab9.md + wiki example)
- Examples: [[examples/ict2216-lab9-sonarqube]]
- Key content: SonarQube + PostgreSQL via Docker Compose (port 9000), local scanner via sonarsource/sonar-scanner-cli Docker image, project token → GitHub Secrets (SONAR_TOKEN + SONAR_HOST_URL), sonarsource/sonarqube-scan-action GitHub Actions workflow, OOM fix (--memory=3g)

## 2026-06-23 | ingest | ICT2216 Lab 8 — Static Code Analysis

- Pages created: 2 (instructions_lab8.md + wiki example)
- Examples: [[examples/ict2216-lab8-static-code-analysis]]
- Key content: ESLint with Modern Flat Config (eslint.config.mjs), SARIF output via @microsoft/eslint-formatter-sarif, three security plugins (eslint-plugin-security / security-node / no-unsanitized), GitHub Actions workflow uploading SARIF to Code Scanning, GitHub CodeQL workflow

## 2026-06-23 | ingest | ICT2216 Lab 7 — GitHub Actions with Automated Testing

- Pages created: 2 (instructions_lab7.md + wiki example)
- Examples: [[examples/ict2216-lab7-automated-testing]]
- Key content: Mocha/Chai unit tests on Node.js, Selenium + ChromeDriver integration/UI tests via Docker, two-job GitHub Actions workflow (build → test) with selenium sidecar service and artifact hand-off via tar

## 2026-06-23 | ingest | ICT2216 Lab 6 — OWASP Dependency Check

- Pages created: 2
- Resources: [[resources/owasp-dependency-check]]
- Examples: [[examples/ict2216-lab6-owasp-dependency-check]]
- Key content: Docker-based local SCA scan, GitHub Actions workflow with artifact upload, Dependabot/Renovate alternatives

## 2026-06-23 | autoresearch | AI Workflows

- Rounds: 3 | Searches: 6 | Sources fetched: 2 | Pages created: 5
- Concepts: [[concepts/ai-workflows]], [[concepts/ai-workflow-orchestration]]
- Sources: [[sources/anthropic-building-effective-agents]], [[sources/aws-agentic-ai-patterns-2025]]
- Synthesis: [[synthesis/research-ai-workflows]]
- Key finding: AI workflows are distinguished from agents by whether the LLM controls its own process (agent) or follows predefined code paths (workflow); Anthropic's 5 patterns (Prompt Chaining, Routing, Parallelisation, Orchestrator-Workers, Evaluator-Optimiser) cover the majority of production use cases; the orchestration tool landscape splits into three distinct categories (agent orchestration, durable execution, data pipelines) and picking the wrong category is the most common architectural mistake.

## 2026-06-23 | autoresearch | Retrieval-Augmented Generation (RAG)

- Rounds: 3 | Searches: 6 | Sources fetched: 3 | Pages created: 6
- Concepts: [[concepts/retrieval-augmented-generation]], [[concepts/rag-architectures]]
- Entities: [[entities/graphrag-microsoft]]
- Sources: [[sources/humanloop-rag-architectures-2025]], [[sources/pinecone-rag-guide]]
- Synthesis: [[synthesis/research-rag]]
- Key finding: RAG is a four-stage pipeline (chunk → embed → retrieve → generate) that has evolved through four generations; hybrid search + re-ranking is the production default; GraphRAG (Microsoft) achieves 72–83% comprehensiveness improvement over vector RAG on holistic queries; chunking strategy performance is corpus-dependent — evaluate on your own data; RAG and MCP are converging at the agent layer.

## 2026-06-23 | autoresearch | MCP Servers (Model Context Protocol)

- Rounds: 3 | Searches: 5 | Sources fetched: 5 | Pages created: 7
- Concepts: [[concepts/mcp-model-context-protocol]], [[concepts/mcp-security]]
- Entities: [[entities/agentic-ai-foundation-aaif]]
- Sources: [[sources/anthropic-mcp-launch-2024]], [[sources/mcp-spec-2025-11-25]], [[sources/mcp-first-year-2025]]
- Synthesis: [[synthesis/research-mcp-servers]]
- Key finding: MCP is a provider-agnostic JSON-RPC 2.0 protocol (Host → Client → Server) that replaced fragmented LLM tool integrations; donated to the Linux Foundation's AAIF in Dec 2025; the Nov 2025 spec added async Tasks, CIMD OAuth, and M2M OAuth for headless agents; security risks include prompt injection, tool poisoning, and rug pull attacks.

## 2026-06-21 | autoresearch | Context Compression of Chats with Large Language Models

- Rounds: 2 | Searches: 8 | Sources fetched: 7 | Pages created: 8
- Concepts: [[concepts/context-compression-llm]], [[concepts/kv-cache-compression]], [[concepts/prompt-compression]]
- Entities: [[entities/llmlingua]]
- Sources: [[sources/acon-context-compression-agents]], [[sources/anthropic-effective-context-engineering]], [[sources/factory-ai-compression-evaluation-2025]], [[sources/kv-cache-compression-review-2025]]
- Synthesis: [[synthesis/research-context-compression-llm]]
- Key finding: Five distinct technique families exist (dialogue summarisation, prompt compression, KV cache compression, soft/latent compression, retrieval-based); higher compression ratio does NOT equal higher quality — Factory's 98.6% compression scored 0.35 points higher than OpenAI's 99.3% compression on production tasks; artifact tracking remains an open problem across all methods

## 2026-06-19 | project | ICT2216 TrialGuard — CD Pipeline (GitHub Actions → EC2)

- Updated: [[concepts/github-actions-cicd]] — added "CD: Deploying to EC2 via SSH" section covering the full deploy job pattern, `gh secret set` for adding secrets via CLI, the `git archive` approach for private repos, and the `-o LogLevel=ERROR` fix
- Created: [[learning/ssh-stdout-known-hosts-warning]] — SSH "Permanently added to known hosts" warning contaminates stdout when using `2>&1`; fix is `-o LogLevel=ERROR` on all SSH/SCP calls
- Key: GitHub repo secrets (EC2_HOST, EC2_SSH_KEY) added via `gh secret set` — encrypted at rest, masked in logs, write-only after creation, safe for school projects

## 2026-06-12 | autoresearch | Blockchain Technology

- Rounds: 3 | Searches: 9 | Sources fetched: 7 | Pages created: 8
- Sources: [[sources/hacken-smart-contract-vulnerabilities-2025]], [[sources/atlantic-council-cbdc-tracker-2026]], [[sources/chainalysis-crypto-crime-report-2025]], [[sources/layer2-scaling-comparison-2025]]
- Entities: [[entities/satoshi-nakamoto]], [[entities/vitalik-buterin]], [[entities/nick-szabo]]
- Synthesis: [[synthesis/research-blockchain-technology]]
- Concept updated: [[concepts/blockchain-technology]] (added §17 Live Statistics — 2025/2026 figures)
- Key finding: The biggest blockchain losses are no longer smart contract bugs but private key theft — the weakest link has moved from code to people; DPRK stole ≥$2.02B in 2025 alone

## 2026-06-12 | research | Blockchain Technology

- Created [[concepts/blockchain-technology]] (c-000067) — comprehensive research note
- Covers: block anatomy, cryptographic foundations (SHA-256, ECDSA, Merkle trees), transaction lifecycle, all major consensus mechanisms (PoW/PoS/DPoS/PBFT/PoA), UTXO vs account model, smart contracts (EVM, Solidity, risks), network architecture (node types), security threat model (51% attack, eclipse, long-range, quantum risk, privacy), scalability trilemma and Layer-2 rollups, real-world implementations (Bitcoin, Ethereum, Hyperledger Fabric), and cross-domain connections
- Diagrams: block chain linkage, Merkle tree, transaction flow sequence, PoW mining loop, PoS attestation flow, consensus quadrant chart, mindmap threat model, full transaction lifecycle, network architecture, EVM deployment pipeline
- Domain `blockchain` added (17th domain)
- Updated[[wiki/index]]], [[hot.md]]

## 2026-06-11 | ingest | ICT2216 Labs 1–5 instruction files

- Source: `instructions_lab1.md` through `instructions_lab5.md` (step-by-step lab guides created from PDF lab sheets)
- No new example pages created — all five labs already had comprehensive pages in `wiki/examples/`
- Updated [[examples/ict2216-lab2-securityrat]]: added **Part 1 — CIA+AAA security requirements framework discussion** (this section was completely absent; the page only covered the SecurityRAT tool)
- Updated [[examples/_index.md]]: added four missing entries — Lab 4 (OWASP Threat Dragon), Lab 5 (GitHub Actions), Project Phase 4 Auth, Project Deployment Phases 9–12

## 2026-06-08 | ingest | ICT2216 Lecture 5 — Secure Software Design (transcript re-ingest)

- Source: spoken lecture transcript (Lecture 5 — same content as 2026-05-30 ingest, reviewed for new details)
- Three additions made to [[concepts/secure-design-implementation]]:
  - **Deactivate vs delete pattern** (referential integrity section) — add `active` column rather than physically removing user rows; preserves audit history and referential links
  - **Admin account installation-wizard model** (authentication design section) — prompt for admin credentials on first launch (Windows/Linux install pattern); never pre-seed hard-coded credentials
  - **NFR governing hash iteration count** (hashing section) — iteration count must be specified as a non-functional security requirement with hardware-based justification, not chosen arbitrarily
- Updated: [[concepts/secure-design-implementation]] (updated field, 3 additions)

## 2026-05-31 | project | ICT2216 TrialGuard — Phases 9–12 Deployment and Hardening

- Created: [[examples/ict2216-project-deployment-phases-9-12]] — full EC2 deployment workflow (git archive + SCP for private repos, PEM permissions, cert generation on Linux, docker compose, health checks, compliance report endpoint, daily backup service)
- Created: [[learning/docker-volume-host-dir-created-as-root]] — Docker creates bind-mount host dirs as root if missing; fix: `sudo chown <user>:<user>` or `mkdir -p` before first compose up
- Created: [[learning/docker-ro-mount-chmod-fails]] — `chmod` fails on `:ro` mounted scripts; fix: call `sh /backup.sh` instead of making file executable
- Created: [[learning/git-amend-remove-sensitive-push]] — remove sensitive info from latest pushed commit: edit file → `git add` → `git commit --amend --no-edit` → `git push --force origin main`
- Created: [[learning/windows-openssl-strawberry-broken]] — Strawberry Perl's OpenSSL maps config to non-existent Z: drive; generate TLS certs on EC2/Linux and SCP back instead
- Updated:[[wiki/index]]] (1 example row, 4 learning rows)

## 2026-05-30 | lab | ICT2216 Lab 4 — OWASP Threat Dragon

- Lab file: `Lab4/Lab04 - OWASP Threat Dragon-2025.pdf`
- Created: [[resources/owasp-threat-dragon]] — two delivery variants (web/desktop/Docker), full stencil element table (Process/Store/Actor/DataFlow/TrustBoundary), both data-flow creation methods (drag + grey link tool), out-of-scope marking (dashed lines, reason field, threat generation disabled), red highlighting for open threats, customisable report, MS TMT vs Threat Dragon comparison table
- Created: [[examples/ict2216-lab4-owasp-threat-dragon]] — step-by-step lab walkthrough (5 steps: add elements → add flows/boundaries → out-of-scope → triage threats → report), key differences from Lab 3 MS TMT table, 4 gotchas (grey link ≠ red delete; trust boundaries drive threat count; out-of-scope ≠ delete; save frequently)
- Updated: [[sources/ICT2216-secure-software-development]] (Lab 4 row, new example, new resource)
- Updated:[[wiki/index]]] (1 example row)

## 2026-05-30 | lab | ICT2216 Lab 5 — Nginx Reverse Proxy, Let's Encrypt TLS, GitHub Actions CI/CD

- Lab file: `Lab5/X05-Github-Actions.pdf`
- Step 4.1–4.2: Created `Lab5/nginx-proxy/` with Nginx Docker Compose; updated `nginx.conf` for `localhost`; started with `docker compose up -d`; verified with `curl http://localhost/` → Hello World HTML
- Step 4.3–4.5: Prepared TLS config files (`nginx-compose-tls.yml` + `nginx-tls.conf`) with certbot entrypoint (ACME webroot challenge, email: lcslayer22@gmail.com); created `certbot/www/` and `certbot/conf/` directories; TLS config ready for deployment on team VM with real domain (replace `yourdomain.com`)
- Step 5: Created `Lab5/lab5-cicd/` standalone git repo with `index.html` at root and `.github/workflows/test-nginx.yml`; initialized git on `main` branch; GitHub CLI (gh) installed via winget; pending `gh auth login` + push
- Auto-renewal cron pattern documented (Step 4.6, optional): `0 3 * * * docker compose run --rm certbot renew && docker compose restart nginx`
- Created: [[concepts/nginx-reverse-proxy-and-tls]] (Nginx config, Let's Encrypt two challenge methods, TLS compose, nginx-tls.conf, auto-renewal)
- Created: [[concepts/github-actions-cicd]] (workflow YAML anatomy, triggers, runners, Docker in Actions, secrets, job dependencies, full pipeline stages for secure software)
- Created: [[examples/ict2216-lab5-github-actions]] (full lab walkthrough, all config files, key gotchas)
- Updated: [[sources/ICT2216-secure-software-development]] (Lab 5 entry, two new concept links, new example link)
- Updated:[[wiki/index]]] (2 concept rows, 1 example row)

## 2026-05-26 | project | ICT2216 Project — Frontend Volume Bug Fix + start.py Refresh Automation

- Root cause identified: `frontend_dist` named volume is only seeded from image on first creation; rebuilding the image never updates an existing volume
- Fix: `purge_frontend_volume()` added to `start.py` — stops nginx/frontend-build, removes stopped containers holding the volume, deletes the volume, then `docker compose up -d --build` re-seeds it fresh
- Footer cleanup: removed Privacy/Terms/Security/HIPAA/GDPR/SOC 2 links from all four footer locations (Login.jsx, Signup.jsx, Landing.jsx, subpage-shell.jsx); each now shows only `© 2026 TRIALGUARD`
- Learning page created: [[learning/docker-named-volume-stale-content]] (named volume stale content gotcha, fix, and alternative patterns)
- Updated: [[concepts/docker-compose]] cross-reference added

---

## 2026-05-26 | project | ICT2216 Project — Phase 4 Authentication + Docker Stack Verification

- Project: TrialGuard — Secure Clinical Trial Participant Portal (ICT2216 Secure Software Development)
- Tasks completed: 4.1 Register, 4.2 Login (step 1), 4.3 Verify MFA (step 2), 4.4 Logout, 4.5 Audit log
- Example page created: [[examples/ict2216-project-phase4-auth]] (full auth blueprint, two-step MFA, session fixation prevention, audit log, CSRF approach, smoke test)
- Learning page created: [[learning/docker-compose-build-context]] (build context controls COPY visibility — fix for moved requirements.txt)
- Updated: [[concepts/docker-compose]] (added "Build Context — Shared Files Across Services" section)
- Docker build context change: `build: ./backend` → `build: { context: ., dockerfile: backend/Dockerfile }` in compose; `COPY . .` → `COPY backend/ .` in Dockerfile
- Frontend plumbing: `frontend/src/api.js` fetch wrapper; Vite dev proxy `/api` → `http://localhost:8080`
- start.py launcher created at repo root: builds stack, polls until ready, opens browser; full error handling
- Stack verified: all 6 containers healthy, `https://localhost` serves React SPA, `POST /api/auth/register` returns 201

---

## 2026-05-25 | project | ICT2216 Project — Vite + React SPA Refactor (TrialGuard)

- Project: TrialGuard — Secure Clinical Trial Participant Portal (ICT2216 Secure Software Development)
- Example page created: [[examples/ict2216-project-vite-refactor]]
- Learning page created: [[learning/vite-react-spa-migration]] (3 bugs + migration patterns)
- Resource page created: [[resources/vite]] (Vite build tool)
- Updated: [[examples/_index.md]], [[resources/_index.md]]
- Key migrations: UMD/CDN React → Vite; `Object.assign(window,{})` → ES modules; multi-page HTML → React Router v6 SPA
- Build verified: 42 modules, 0 errors, `npm run dev` functional

---

## 2026-05-30 | update | ICT2216 Lecture Transcript — Threat Modelling & Security by Design (recap lecture)

- Source: ICT2216 lecture transcript (threat modelling + all 10 OWASP Security by Design Principles)
- Updated: [[concepts/threat-modeling]] (dated 2026-05-30)
- Additions (3 targeted — existing pages already comprehensive):
  1. **Threat → Attack → Risk triangle** — Attack defined as the *realisation* of a threat; Risk clarified as the consequence that can be zero even when an attack occurs if the system is well-protected; SQL injection worked example illustrating the principle
  2. **AI threat specifics** — data poisoning (malicious training data) and prompt injection (overriding AI chatbot system instructions) added to Non-Human Threats section
  3. **Concrete STRIDE worked examples** — Spoofing (typosquatting: `amazom.com` impersonating `amazon.com`); Tampering (modifying `user_code` at checkout to charge a victim's credit card); Repudiation (signed delivery receipt as non-repudiation mechanism, with software equivalent: digital signatures + hash-chained audit logs)
- No new files created; all content absorbed into existing concept page
- No address counter change (update only)

---

## 2026-05-30 | ingest | ICT2216 Lecture 5 — Secure Software Design (Part 2) & Secure Agile Development

- Source: `raw/ICT2216 Lecture 5 Secure Software Development.md`
- Concept page created (1):
  - [[concepts/secure-design-implementation]] (c-000066)
- Source index updated: [[sources/ICT2216-secure-software-development]] (Lecture 5 section + new concept row)
- Address counter updated: 67
- Manifest updated with 1 new address_map entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md (85 pages, SSD now 7)
- Domain: secure-software-development (existing domain, +1 concept page)
- Coverage: CIA-AAA translated to design decisions — Confidentiality (masking, symmetric/asymmetric crypto comparison [key count N(N−1)/2 vs N, speed, non-repudiation], hybrid TLS approach, X.509 v3 certificate structure, client-side hashing), Integrity (salted/iterated hashing, bcrypt/PBKDF2, password storage comparison table, referential integrity, resource locking), Availability (replication/primary-secondary, failover clusters, vertical vs horizontal scaling), Authentication (MFA, SSO, passwordless authentication [WhatsApp/SingPass/Apple/Google examples]), Authorisation (RBAC vs UBAC, Data Access Control Matrix, least privilege/separation of duties/performance), Accountability (who/what/where/when, never log sensitive data, log rotation/write-once), Secure Agile Development (security activities across 6 sprint phases: Modelling/Sprint Planning/Sprint/Dynamic Testing/Release/Operations), 4-step Secure Design Architecture (architecture→threats→controls→document/validate), Physical Topology zones (Internet/DMZ/Intranet/Dev, layered firewall pattern), Logical Topology, Human and Non-Human Actors, External Dependencies security techniques table (8 areas)

---

## 2026-05-25 | update | ICT2216 Lecture — Secure Software Requirements (transcript)

- Source: ICT2216 lecture transcript (SSDLC requirements process — CIA+AAA deep-dive)
- Updated: [[concepts/secure-software-requirements]] (dated 2026-05-25)
- Additions (3 targeted additions to avoid duplicating already-comprehensive content):
  1. **Data-in-processing protection technologies** — Homomorphic Encryption (compute on ciphertext; computationally expensive) and Differential Privacy (statistical noise to prevent individual identification; approximate output) added to Confidentiality section
  2. **Usability vs. security tension** — DBS 6-digit PIN worked example added to Authentication section (10⁶ vs 10⁴ combinations; auditable rationale requirement)
  3. **NIST SSDF stakeholder roles** — three-role table added (Business Owner: approve/resource/accept risk; Developer: implement/test; Security Professional: expertise/threat model/assurance)
- No new files created; all content absorbed into existing concept page
- No address counter change (update only)

---

## 2026-05-24 | ingest | INF1007 Ethics & Professional Conduct

- Source: `raw/INF1007 Ethics & Professional Conduct Notes.md`
- Source index: [[sources/INF1007-ethics-professional-conduct]] (c-000060)
- Concept pages created (4):
  - [[concepts/ethical-frameworks]] (c-000061)
  - [[concepts/behavioural-ethics-and-workplace]] (c-000062)
  - [[concepts/privacy-data-protection-and-ip]] (c-000063)
  - [[concepts/ai-ethics-and-digital-society]] (c-000064)
- Area page created: [[areas/it-ethics]] (c-000065)
- Address counter updated: 66
- Manifest updated with 6 new address_map entries + INF1007 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md, wiki/areas/_index.md
- Domain: it-ethics (new domain #16, 4 concept pages)
- Coverage: ethical frameworks (Kantianism, Utilitarianism, Social Contract, Virtue Ethics, SCS/ACM codes), behavioural ethics (Milgram/obedience, Stanford Prison/roles, moral licensing, anonymity, cognitive biases), workplace ethics (conflict of interest, whistleblowing, CSR), privacy (PDPA, government surveillance), hacker ethics, malware taxonomy, IP law (copyright/patent/trademark/trade secret/fair use), AI ethics (bias/fairness, deepfakes, accountability/explainability, 6 AI ethics principles), digital divide, automation, outsourcing

---

## 2026-05-23 | ingest | INF2004 Embedded Systems Programming

- Source: `raw/INF2004 Embedded Systems Programming Notes.md`
- Source index: [[sources/INF2004-embedded-systems-programming]] (c-000053)
- Concept pages created (5):
  - [[concepts/embedded-systems-fundamentals]] (c-000054)
  - [[concepts/embedded-io-and-interrupts]] (c-000055)
  - [[concepts/embedded-timers-and-rtos]] (c-000056)
  - [[concepts/embedded-testing-and-optimisation]] (c-000057)
  - [[concepts/embedded-sensor-fusion-and-edge]] (c-000058)
- Area page created: [[areas/embedded-systems]] (c-000059)
- Address counter updated: 60
- Manifest updated with 7 new address_map entries + INF2004 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md, wiki/areas/_index.md
- Domain: embedded-systems (new domain #15, 5 concept pages)
- Coverage: Raspberry Pi Pico (RP2040), real-time taxonomy, hardware taxonomy, build pipeline, startup code, V-model, case studies (Therac-25/Ariane 5/Toyota), interrupt handling (IVT/ISR/stack), polling vs interrupts, timers/PWM/WDT, RTOS (task lifecycle/context switch/scheduling), FSM, testing (traceability/unit/integration/system), optimisation (power/performance/memory), sensor fusion, edge computing, TinyML

---

## 2026-05-23 | ingest | INF2001 Introduction to Software Engineering

- Source: `raw/INF2001 Intro To Software Engineering Notes.md`
- Source index: [[sources/INF2001-intro-software-engineering]] (c-000048)
- Concept pages created (4):
  - [[concepts/sdlc-models]] (c-000049)
  - [[concepts/uml-modelling]] (c-000050)
  - [[concepts/software-project-management]] (c-000051)
  - [[concepts/software-configuration-management]] (c-000052)
- Note: Weeks 2 (RE), 8–9 (design/architecture/GoF), 10–11 (testing/refactoring) cross-reference existing concept pages rather than duplicating them
- Address counter updated: 53
- Manifest updated with 5 new address_map entries + INF2001 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md
- Domain: software-engineering (existing domain, +4 pages → 13 total)
- Cross-domain connections: SCM + CI/CD → DevOps/web-development; SDLC models → agile project management; UML → all SE concept pages

---

## 2026-05-23 | ingest | INF1002 Programming Fundamentals

- Source: `raw/INF1002 Programming Fundamentals Notes.md`
- Source index: [[sources/INF1002-programming-fundamentals]] (c-000041)
- Concept pages created (5):
  - [[concepts/python-fundamentals]] (c-000042)
  - [[concepts/python-data-structures-and-io]] (c-000043)
  - [[concepts/python-functions-and-modules]] (c-000044)
  - [[concepts/c-programming-fundamentals]] (c-000045)
  - [[concepts/c-pointers-memory-and-data-structures]] (c-000046)
- Area page created: [[areas/programming-fundamentals]] (c-000047)
- Address counter updated: 48
- Manifest updated with 7 new address_map entries + INF1002 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md, wiki/areas/_index.md
- Domain added: programming-fundamentals (14th domain)
- Cross-domain connections: computer-science (linked lists, recursion), operating-systems (C + memory), computer-architecture (compilation pipeline)

---

## 2026-05-22 | ingest | Learnix CTk teardown + file refactor

- Source: ICT2114 ITP project (Learnix), `src/ui/auth_ui.py` + `src/ui/chat_ui.py`
- Learning page created: [[learning/customtkinter-after-teardown]] — root cause analysis and 3-layer fix for CTk 5.2.2 `invalid command name` / `application has been destroyed` Tcl errors; includes `sys.path` / `load_dotenv` path update notes for moved files
- Concept page created: [[concepts/customtkinter-window-lifecycle]] — reusable teardown pattern: `quit()` → `after_cancel` loop → `destroy()` + Tcl `bgerror` override; covers plain `CTk()` wrapper and `CTk` subclass variants
- Indexes updated: `wiki/index.md` (Concepts + Learning tables), `wiki/hot.md`

---

## 2026-05-22 | ingest | INF1006 Computer Networks

- Source: `raw/INF1006 Computer Networks Notes.md`
- Source index: [[sources/INF1006-computer-networks]] (c-000032)
- Concept pages created (7):
  - [[concepts/tcp-ip-network-model]] (c-000033)
  - [[concepts/data-link-layer-ethernet]] (c-000034)
  - [[concepts/ip-addressing]] (c-000035)
  - [[concepts/network-layer-protocols]] (c-000036)
  - [[concepts/transport-layer-tcp-udp]] (c-000037)
  - [[concepts/wireless-and-iot]] (c-000038)
  - [[concepts/application-layer-dhcp-dns]] (c-000039)
- Area page created: [[areas/computer-networks]] (c-000040)
- Address counter updated: 41
- Manifest updated with 9 new address_map entries + INF1006 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md, wiki/areas/_index.md
- Domain added: computer-networks (13th domain)

---

## 2026-05-21 | autoresearch | Software Testing

- Rounds: 3
- Sources found: 2 (ISTQB CTFL v4.0, Fowler Practical Test Pyramid)
- Pages created: [[concepts/software-testing-fundamentals]], [[concepts/test-driven-development]], [[concepts/test-design-techniques]], [[sources/istqb-ctfl-v4]], [[sources/fowler-practical-test-pyramid]], [[research-software-testing]]
- Synthesis: [[research-software-testing]]
- Key finding: Software testing is a three-layer pyramid (unit/integration/E2E) governed by seven ISTQB principles; TDD drives design through Red-Green-Refactor; BDD extends this to business-readable Gherkin specs; EP and BVA systematically reduce test volume while preserving defect detection.

---

## 2026-05-21 | wiki-lint | Health Check

- Pages scanned: 117
- Issues found: 28
- Auto-fixed: 5 (examples/_index.md, concepts/_index.md count, sources/_index.md cross-ref, areas/agile-project-management.md created, areas/_index.md updated)
- Needs review: counter drift (address-counter.txt=3 vs max observed c-000031; requires WSL --rebuild), dead manifest entry (DragonScale Memory.md), ~18 address-map frontmatter mismatches, mass `status:` + `created:` backfill
- Report: [[meta/lint-report-2026-05-21]]

---

## 2026-05-19 | Ingest — PSM I Cheatsheet (github.com/ambaena/scrum-psm1-cheatsheet)

- **Source**: ambaena/scrum-psm1-cheatsheet — README.md + how-to-face.md
- **Pages created**:
  - [[learning/psm1-cheatsheet-study-notes]] — PSM I study notes: readiness check, Agile Manifesto (4 categories/12 principles), Scrum big picture diagram, invalid Sprint types (Hardening/Sprint 0/Release/Design), PB ordering factors (Value+Risk+Size+Dependencies), three progress monitoring methods (burn-down/burn-up/cumulative flow), Daily Scrum role clarity, Sprint Review undone-work rule, Retrospective full scope, SM startup actions, Scaled Scrum rules, IKIWISI/YAGNI, full definitions glossary (20 terms), two-computer open-book exam strategy, pre-exam quick-reference checklist
- **Pages updated**:
  - [[concepts/scrum-framework]] — added: Invalid Sprint Types section, Scaled Scrum section, Daily Scrum role clarity (SM ensures but doesn't conduct; PO doesn't attend)
  - [[learning/_index.md]] — added PSM I cheatsheet entry
  -[[wiki/index]]] — learning page added
  - [[log]] — this entry
  - [[hot]] — session summary updated

---

## 2026-05-19 | Ingest — Scrum Master Exam (80 Questions, YouTube Transcript)

- **Source**: YouTube — "80 Scrum Master Exam Questions" (CSM / PSM / ACP prep)
- **Pages created**:
  - [[learning/scrum-master-exam-study-notes]] — 80-question study notes: waterfall vs Scrum, empiricism precision, formal inspection events, framework composition, servant leadership distinction, SM as management position, self-managing teams, PO continuous collaboration, PB rules, backlog refinement (no development), Sprint Backlog ownership (Developers only), DoD rules, cross-functionality, velocity not a metric, burn-down interpretation, estimation unit freedom, testing strategy freedom, retro vs review distinction, end-of-product handling, 40-row key rules table
- **Pages updated**:
  - [[learning/_index.md]] — added scrum-open-assessment-study-notes (previously missing), scrum-master-exam-study-notes, Scrum skill-map entry
  - [[concepts/_index.md]] — added Agile Project Management domain section (scrum-framework), added security-by-design-principles to Secure Software Dev section, updated counts (54→58 pages, 11→12 domains, 15→17 sources)
  - [[sources/_index.md]] — added Scrum Guide to sources table and By Domain section
  -[[wiki/index]]] — learning page added
  - [[log]] — this entry
  - [[hot]] — session summary and Recent Changes updated

---

## 2026-05-19 | Ingest — Scrum Open Assessment Quiz Bank

- **Source**: `raw/scrum-open-quiz-questions.md` — classmarker.com Scrum Open Quiz, 29/30 (96.7%)
- **Pages created**:
  - [[learning/scrum-open-assessment-study-notes]] — 30-question study notes grouped by theme: 15 common traps/misconceptions, roles Q&A tables, events timebox table, artifacts+commitments table, full key-facts reference (25 facts)
- **Pages updated**:
  - [[sources/scrum-guide-2020]] — Learning section added
  -[[wiki/index]]] — learning page added to Learning table
  - [[log]] — this entry
  - [[hot]] — session summary updated

---

## 2026-05-19 | Ingest — The 2020 Scrum Guide

- **Source**: 2020 Scrum Guide (Ken Schwaber & Jeff Sutherland) — CC BY-SA 4.0
- **Pages created**:
  - [[sources/scrum-guide-2020]] — source index: key facts, canonical reference metadata, related concept links
  - [[concepts/scrum-framework]] — complete Scrum framework: theory (empiricism + lean, three pillars), five values, three accountabilities (Developers/PO/SM), five events with timeboxes, three artifacts with commitments (Product Goal/Sprint Goal/Definition of Done), quick-reference tables
- **Pages updated**:
  -[[wiki/index]]] — new source and concept added (domain: agile-project-management)
  - [[log]] — this entry
  - [[hot]] — session summary and domain summary updated

---

## 2026-05-19 | Ingest — ICT2216 Lecture 4: Secure Software Design

- **Source**: `raw/ICT2216 Lecture 4 Secure Software Development.md`
- **Pages created**:
  - [[concepts/security-by-design-principles]] — design flaws vs. bugs (McGraw 50% finding), Banana Token case study, all 10 OWASP Security by Design Principles with worked examples and code, Security Architecture (physical vs. logical)
- **Pages updated**:
  - [[sources/ICT2216-secure-software-development]] — added Lecture 4 section (Secure Software Design), Lab 3 to Labs table, new concept to Concept Pages table, updated frontmatter topics
  -[[wiki/index]]] — added `security-by-design-principles` to Concepts table
  - [[log]] — this entry
  - [[hot]] — updated session summary

---

## 2026-05-16 | Ingest — ICT2216 Lab 3: Microsoft Threat Modeling Tool

- **Source**: Lab 03 PDF — Introduction to Microsoft Threat Modeling Tool
- **Pages created**:
  - [[resources/microsoft-threat-modeling-tool]] — tool reference: install, 4-step workflow (Build→Analyze→Triage→Report), DFD stencils, STRIDE auto-generation, threat status system
  - [[examples/ict2216-lab3-threat-modeling-tool]] — Lab 03 walkthrough: 5 sequential steps, sample diagram, STRIDE checklist for project deliverable
- **Pages updated** (indexes):
  -[[wiki/index]]] — added to Examples and Resources tables
  - [[log]] — this entry

---

## 2026-05-15 | Ingest — ICT2216 Lecture 3: Extended Security Requirements + Threat Modeling

- **Source**: `raw/ICT2216 Lecture 3 Secure Software Development.md`
- **Summary**: [[sources/ICT2216-secure-software-development]]
- **Pages updated**:
  - [[concepts/secure-software-requirements]] — added: General App Security Requirements (session/error/config/code management), Operational Requirements (deployment/archiving/anti-piracy), Other Requirements (TOC/TOU, procurement, GDPR), Anti-Requirements technique, Abuse/Misuse Case Modelling with ATM worked example
- **Pages created**:
  - [[concepts/threat-modeling]] — threat agents (8 human types + non-human), 5 threat identification steps (trust boundaries/DFDs/entry-exit/privileged functions/mis-actors), mis-actor network categories (web/network/co-located), 5-step threat modeling process, attack trees, full Microsoft STRIDE breakdown with countermeasures and OWASP cross-reference
- **Pages updated** (indexes):
  - [[concepts/_index]] — 53→54 pages; Secure Software Dev 4→5; threat-modeling row added
  -[[wiki/index]]] — threat-modeling row added to Concepts section
  - [[sources/ICT2216-secure-software-development]] — Lecture 3 topic entries added; threat-modeling concept cross-reference added
  - [[areas/secure-software-development]] — threat-modeling row added to Concept Pages table
- **Key insight**: Threat modeling answers the question requirements cannot — not *what* to protect, but *how* an attacker will actually try to break the system. STRIDE maps attacker goals to CIA+AAA violations, closing the loop between Part 1 (requirements) and Part 2 (adversarial analysis) of Lecture 3.

---

## 2026-05-15 | Gap Resolution — Areas, Synthesis, Learning, Skill Files

- **Trigger**: Comprehensive lint pass identified orphaned concept clusters, empty `areas/` folder, stale sub-indexes, missing synthesis pages, empty learning index, and vague ingest skill step 6.
- **Pages created**:
  - [[areas/computer-architecture]] (ICT1011 — Von Neumann, MSP430, I/O & memory)
  - [[areas/mobile-development]] (INF2007 + INF1009 — MVVM, Jetpack Compose, coroutines)
  - [[areas/hci]] (INF2002 — Norman, Fitts, Gestalt, needfinding, usability evaluation)
  - [[synthesis/maths-to-ml-bridge]] (6 sections: matrix multiply→forward pass, OLS/GD duality, SVD→PCA, Gaussian NB, Z-score, beyond-maths table)
  - [[synthesis/web-security-ssdlc-bridge]] (INF1005 attack → OWASP 2025 → ASVS chapter → STRIDE threat, full mapping table)
  - [[synthesis/ict1011-ict1012-architecture-bridge]] (hardware handover from fixed partitioning to TLB, demand paging, replacement, thrashing)
  - [[synthesis/rest-api-cross-stack]] (Retrofit→OkHttp→Express→res.json() full lifecycle, verb mapping table, coroutine integration)
  - [[learning/ict1012-operating-systems-study-notes]]
  - [[learning/inf2003-database-systems-study-notes]]
  - [[learning/inf1008-data-structures-algorithms-study-notes]]
  - [[learning/inf1005-web-systems-study-notes]]
- **Pages updated**:
  - [[synthesis/_index]] — 4 new synthesis rows added
  - [[learning/_index]] — rebuilt from empty placeholder; 5 study-notes rows
  - [[areas/_index]] — date updated
  -[[wiki/index]]] — synthesis and learning sections updated; date updated to 2026-05-15
  - [[hot]] — session entry added; Active Threads updated with all resolved items
  - [[log]] — this entry
- **Skill files updated**:
  - `skills/wiki-ingest/SKILL.md` — Step 6 rewritten: now enumerates all 6 `_index.md` files to update per ingest (sources, concepts, synthesis, learning, areas domain page, areas _index)
  - `skills/wiki-lint/SKILL.md` — Added Check 8a (Stale sub-index files): count pages on disk vs rows in each `_index.md`; report missing pages by name
- **Key insight**: Sub-index files are the vault's navigation backbone. Every ingest must update them or pages become silently orphaned — visible in Obsidian but unreachable from the index layer.

---

## 2026-05-14 — Synthesis: Four Cross-Domain Pages Created

- Action: SYNTHESIS
- Scope: 4 new pages in `wiki/synthesis/`
- Pages created:
  - `maths-to-ml-bridge.md` (171 lines) — linear algebra → neural networks; SVD/eigenvalues → PCA; probability → Gaussian Naive Bayes; statistics → feature scaling; module dependency chain
  - `web-security-ssdlc-bridge.md` (159 lines) — INF1005 code-level attacks (SQLi, XSS, CSRF, brute force) mapped to OWASP 2025 categories, ASVS verification levels (V2/V4/V5), and STRIDE threats; code vs process perspectives compared
  - `ict1011-ict1012-architecture-bridge.md` (199 lines) — ICT1011 paging data structure → ICT1012 TLB/EAT, page table structures, demand paging, page replacement algorithms, thrashing; full dependency chain documented
  - `rest-api-cross-stack.md` (288 lines) — Express CRUD routes ↔ Retrofit annotations; full HTTP request lifecycle; coroutine integration; error handling divergence; MVVM layer mapping
- Updated: `wiki/gaps/_index.md` — 4 missing synthesis gaps marked resolved; 2 open questions closed
- Sources read: 15 concept pages

---

## 2026-05-14 — Lint: Gap Detection

- Action: LINT
- Scope: All 52 concept pages, 15 source pages, 4 synthesis pages, meta indexes
- Updated: `wiki/gaps/_index.md` — populated from empty template with full gap report
- Updated: `wiki/sources/_index.md` — was missing 7 of 15 sources; now complete with all 15 by domain
- Findings:
  - No broken wikilinks found (suspected backslash was terminal rendering artefact)
  - ~20 older concept pages use short-form links (`[[page-name]]`) vs. vault standard (`[[concepts/page-name|Label]]`) — functional but inconsistent
  - 2 stale index pages: concepts/_index.md (placeholder), sources/_index.md (now fixed)
  - 4 missing synthesis pages documented: maths→ML, web security×SSDLC, ICT1011→ICT1012, REST API cross-stack
  - 3 orphaned concept clusters: mathematics (10 pages), machine learning (6 pages), partial software-engineering (3 pages)
  - learning/ folder near-empty (only 1 page); no study notes for any of 15 modules
  - areas/ folder empty; no domain overview pages exist
  - 3 open questions documented in gaps index

---

## 2026-05-14 — Ingest: INF1005 Web Systems & Technologies

- Action: INGEST
- Source: `raw/INF1005 Web Systems & Technologies Notes.md` (2,111 lines, 21 chapters)
- Textbook: Connolly & Hoar, *Fundamentals of Web Development* (3rd Edition)
- Created: `wiki/sources/INF1005-web-systems-technologies.md`
  - 21-chapter map, concept page cross-references
- Created: `wiki/concepts/web-fundamentals.md` (Chapters 1–4)
  - Internet vs Web distinction (ARPANET 1969, Berners-Lee 1989)
  - Packet switching vs circuit switching
  - TCP/IP 4-layer model: Application/Transport/Internet/Link
  - TCP (reliable, ACKs) vs UDP (fast, no guarantee)
  - IPv4 (exhausted 2011) vs IPv6; PAT
  - DNS: TLD types (gTLD/ccTLD/IDN), ICANN; 10-step resolution process
  - URL components: protocol/domain/port/path/query/fragment; relative URL types
  - HTTP methods (GET/POST/PUT/DELETE/HEAD); idempotency and safety
  - HTTP status codes: 200/301/304/401/404/500
  - Browser rendering metrics: TTFB/FP/FCP/LCP/TTI/CLS
  - Web stacks: LAMP/MERN/WISA/JAM
  - Web 2.0 and client-server architecture
- Created: `wiki/concepts/html-and-css.md` (Chapters 5–9)
  - HTML5 document structure: DOCTYPE/html/head/body; charset; lang
  - Semantic philosophy: structure and meaning, not presentation
  - Text/inline elements: p, div, span, strong, em, a, img, br, hr
  - Link types: absolute, relative, anchor, mailto; relative path variants
  - HTML5 structural elements: header/nav/main/section/article/aside/figure/footer/details/address
  - Tables: caption/thead/tbody/tfoot, colspan/rowspan, border-collapse; tables for data only
  - Forms: action/method, GET vs POST comparison; full form controls table; input types
  - Accessibility: fieldset/legend, label for, scope on th
  - Input validation layers: HTML5 (hint) → JS (UX) → server-side (guaranteed)
  - CSS syntax, placement (inline/embedded/external)
  - Selectors: element/universal/class/ID/group; attribute selectors; pseudo-class/element; combinators
  - Cascade: inheritance, specificity (ID>class>element), location
  - Box model: content/padding/border/margin; collapsing margins; border-box
  - CSS custom properties (variables)
  - Colour: named/RGB/hex/RGBa/HSL
  - Float, positioning (static/relative/absolute/fixed/sticky)
  - Flexbox: one-axis; flex-direction/flex-wrap/justify-content/align-items
  - Grid: two-axis; fr units; repeat(); grid-column/row placement
  - Responsive design: viewport meta tag, mobile-first, min-width media queries, responsive images
  - CSS effects: transitions, keyframe animations, transforms, filters
  - Sass: variables, nesting, mixins
  - WCAG POUR principles; W3C validator; accessibility practices
- Created: `wiki/concepts/javascript-fundamentals.md` (Chapters 10–12)
  - History: Netscape 1996 → ECMAScript 1997 → ES6 2015
  - var (hoisted, function-scoped) vs let/const (block-scoped)
  - Primitive types: Boolean/Number/String/Null/Undefined/Symbol
  - Truthy/Falsy values
  - Operators: `===` strict equality preferred
  - Control flow: if/else if/else, switch, ternary, while/do-while/for/for-of
  - Arrays: push/pop/length/destructuring; functional methods (forEach/find/filter/map/reduce/sort)
  - Objects: literal notation, dot/bracket access, destructuring, spread
  - JSON: JSON.parse() / JSON.stringify()
  - Functions: declaration (hoisted), expression, arrow syntax, default/rest parameters
  - Scope: global/function/block; hoisting; modules
  - Closures: inner function retains enclosing scope after execution
  - ES6 classes: constructor, inheritance (extends, super), prototype basis
  - DOM: tree of nodes; getElementById/querySelector/querySelectorAll
  - DOM properties: innerHTML (XSS risk)/textContent/classList/style/value
  - DOM manipulation: createElement/appendChild/insertBefore/removeChild
  - Event handling: addEventListener, DOMContentLoaded; event object (preventDefault/stopPropagation/target)
  - Event propagation: capturing → target → bubbling
  - Event delegation pattern
  - Regular expressions: /pattern/flags, .test()
  - Asynchronous: Fetch API → Promises (.then/.catch) → async/await
  - CORS: `Access-Control-Allow-Origin` header
  - Web Storage: localStorage (persistent) / sessionStorage (session)
  - Geolocation API: getCurrentPosition()
  - ES6 modules: export/import syntax; `type="module"` script attribute
- Created: `wiki/concepts/server-side-web-development.md` (Chapters 13–18, 21)
  - PHP: `<?php … ?>` tags; `$` prefix; `.` concatenation; dynamic typing
  - PHP control flow: if/elseif/else, switch, while/for/foreach ($arr as $k => $v)
  - PHP include/require (include_once/require_once)
  - PHP functions: default params, pass-by-reference (&$var), type declarations (PHP 7+)
  - PHP indexed arrays ($arr[]) and associative arrays ($arr["key"]); multidimensional
  - PHP OOP: __construct, $this->, public/private/protected, extends, parent::__construct()
  - PHP Superglobals: $_GET/$_POST/$_REQUEST/$_SESSION/$_COOKIE/$_FILES/$_SERVER/$_ENV
  - Form security: htmlspecialchars() (XSS), filter_var() (validate/sanitise), POST vs GET
  - LAMP stack: Linux/Apache/MySQL/PHP; Ubuntu setup commands
  - PDO: connect with error handling, prepare → bindValue → execute → fetch → null to close
  - SQL CRUD: SELECT/INSERT/UPDATE/DELETE; JOIN (INNER JOIN ON); GROUP BY + aggregate; transactions
  - Table relationships: one-to-many, one-to-one, many-to-many (junction table)
  - NoSQL: Key-Value/Document/Column/Graph; use cases; MongoDB with Mongoose schema/model/find
  - Node.js: V8 engine, event-driven non-blocking, single event-loop thread
  - Blocking (PHP/Apache: thread per request) vs non-blocking (Node.js: event loop continues)
  - Basic Node HTTP server; Express: routing, static files, route params
  - REST API: GET/GET:id/POST/PUT/DELETE mapped to CRUD
  - WebSockets (Socket.io): io.on('connection'), socket.on/io.emit; bidirectional real-time
  - EJS view engine: `<%= %>` for output, `<% %>` for code
  - Serverless: DBaaS/PaaS/FaaS; auto-scaling, reduced complexity
  - Modern frameworks: React (JSX, components), Next.js (React + SSR + routing), Remix (nested routing, parallel server loads), ASP.NET Core (C#/Razor), Blazor (WebAssembly/SignalR)
- Created: `wiki/concepts/web-security-and-devops.md` (Chapters 19–20)
  - CIA Triad: Confidentiality/Integrity/Availability
  - STRIDE: Spoofing/Tampering/Repudiation/Information Disclosure/DoS/Elevation of Privilege
  - Auth factors: Knowledge/Ownership/Inherence; MFA
  - Auth strategies: HTTP Basic, Form+Session, JWT Bearer, OAuth
  - Cryptography: AES (symmetric), RSA (asymmetric); public/private key pair
  - Digital signatures: authenticity + integrity + non-repudiation
  - TLS/HTTPS: successor to SSL; CA certificates (DV/OV/EV)
  - Credential storage: plain text (BAD) → MD5 (BAD) → bcrypt password_hash() + salting (GOOD)
  - SQL injection: `' OR '1'='1` attack; defence = prepared statements
  - XSS (reflected vs stored): defence = htmlspecialchars() + CSP headers
  - CSRF: hidden token in every state-changing form
  - Brute force: rate limiting + lockout + CAPTCHA
  - DoS/DDoS: CDN + load balancers + DDoS protection
  - Security misconfiguration: out-of-date software, default credentials, verbose errors
  - CI/CD: CI (tests on commit), CD Delivery (auto-release-ready), CD Deployment (auto-deploy)
  - Testing: unit/integration/functional/non-functional/penetration (Selenium)
  - Infrastructure as Code: Ansible/Vagrant/Terraform
  - Hosting: shared → VPS → dedicated → collocated → cloud
  - Cloud models: IaaS (servers) / PaaS (platform) / SaaS (software)
  - Server virtualisation: hypervisor, Docker (containers), Kubernetes (orchestration)
  - DNS records: A/AAAA/CNAME/MX/NS/TXT/SPF/PTR
  - Apache: httpd.conf, .htaccess, VirtualHost, URL rewriting with RewriteEngine
  - Monolithic vs Microservices architecture
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

---

## 2026-05-13 — Ingest: ICT1012 Operating Systems

- Action: INGEST
- Source: `raw/ICT1012 Operating Systems Notes.md` (7,856 lines, compiled lecture notes, 10 chapters)
- Authors: Dr. David Sanan & Assoc. Prof. Shang-Wei Lin, Singapore Institute of Technology
- Textbook: A. Silberschatz, P. Galvin, G. Gagne, *Operating System Concepts* (10th Ed.), Wiley, 2019
- Created: `wiki/sources/ICT1012-operating-systems.md`
  - Chapter map (Chapters 1–10), concept page cross-references, explicit note on ICT1011→ICT1012 paging handover
- Created: `wiki/concepts/os-processes-and-threads.md` (Chapters 1–4)
  - OS roles: hardware abstraction, resource allocator, synchronisation, communication, protection
  - Kernel, bootstrap (ROM), DMA (one interrupt per block), interrupt cycle (fetch→execute→check interrupts)
  - System calls: `int 0x80` (old Linux) vs `syscall` (modern); parameter passing (registers/memory block/stack); POSIX/Win32 APIs
  - Privilege modes: CPL bit in CS register; privileged ISA instructions (LGDT, MOV CRx, HLT, VMRUN)
  - OS design approaches: layered, modular, microkernel (Mach), monolithic (UNIX), hybrid (Darwin/Windows NT)
  - Process: text/data/BSS/heap/stack layout; 5-state diagram; PCB fields; long-/medium-/short-term schedulers
  - Process creation: fork/exec/wait/exit; zombie vs orphan; process tree (PID 1 = systemd)
  - IPC: shared memory (mmap, shm_open, ftruncate, munmap); message passing (mq_open/send/receive/close/unlink); blocking/non-blocking; buffer capacity (zero/bounded/unbounded)
  - Threads: economy/resource sharing/scalability/responsiveness; user vs kernel threads; M:1, 1:1, M:M, two-level models; Pthreads API; TLS; thread safety; Linux clone()
- Created: `wiki/concepts/cpu-scheduling-and-synchronisation.md` (Chapters 5–6)
  - CPU/I/O burst cycle; I/O-bound vs CPU-bound; dispatcher latency; preemptive vs non-preemptive
  - Scheduling criteria table: utilisation/throughput/turnaround/waiting/response
  - FCFS (convoy effect, worked avg-wait example); SJF (optimal, exponential averaging formula); SRTF; Priority+ageing; RR (quantum, (n−1)q bound); Multilevel Queue; Multilevel Feedback Queue (3-queue example)
  - Real-Time: soft vs hard; Rate Monotonic (shorter period = higher priority, ~69% utilisation limit); algorithm comparison table
  - Linux CFS: vruntime, nice −20→+19 maps to priorities 100–139
  - Race condition: counter++ / counter-- non-atomic worked example
  - Critical section: 3 requirements (mutual exclusion, progress, bounded waiting)
  - Hardware sync: test_and_set (full C code + both cases explained); compare_and_swap (C code, fewer cache invalidations)
  - Mutex locks: spinlock vs sleep-based; acquire/release C code
  - Semaphores: binary vs counting; wait/signal with blocking queue; synchronisation pattern; bounded-buffer solution (3 semaphores)
  - Semaphore misuse table; deadlock via circular wait; starvation; priority inversion → priority-inheritance protocol
- Created: `wiki/concepts/file-systems.md` (Chapters 7–7b)
  - File attributes, 8 file operations, open-file table
  - Access methods: sequential (tape/logs), direct/random (databases), indexed (large files)
  - Directory structures: single-level → two-level → tree → acyclic-graph (reference count) → general graph
  - Unix permissions: rwx per owner/group/others; r=4/w=2/x=1; chmod/chown/chgrp
  - Layered FS diagram: logical FS → file-org module → basic FS → I/O control → hardware
  - On-disk structures: boot control block, volume control block/superblock, directory, FCB/inode
  - Directory implementation: linear list O(n), ordered O(log n), hash table O(1)
  - Allocation methods: contiguous (start+length, best read perf, external fragmentation), linked (FAT variant), indexed (inode with direct/single-indirect/double-indirect/triple-indirect)
  - Performance table: sequential → contiguous/linked; random → indexed; growing → linked/indexed
  - Fragmentation: external (compaction) vs internal (smaller blocks); 50% rule
  - Free-space: bit vector (fast contiguous, 32 MB overhead for 1 TB at 4 KB blocks) vs linked list
  - Buffer cache; synchronous vs asynchronous writes
- Created: `wiki/concepts/memory-and-virtual-memory.md` (Chapters 8–9)
  - Base/limit registers; memory protection check
  - Address binding stages (compile/load/execution); logical vs physical address distinction
  - MMU relocation register; dynamic loading; dynamic linking (stubs, shared libraries)
  - Contiguous allocation: first-fit/best-fit/worst-fit; 50% rule; external fragmentation (compaction) vs internal fragmentation
  - Paging fundamentals: frame/page/page table definitions; address translation formula; hardware registers vs PTBR vs TLB
  - TLB: EAT formula (EAT = hit×mem + (1−hit)×2×mem); 99% hit example (10.1 ns); ASIDs
  - Memory protection: valid-invalid bit, protection bits, shared pages
  - Page table structures: two-level hierarchical (32-bit: 10+10+12); hashed (clustered, >32-bit); inverted (one global table, indexed by frame number)
  - Swapping: increases multiprogramming; swap individual pages in modern OS
  - Virtual memory benefits: logical > physical; efficient sharing; faster startup
  - Virtual address space: stack↓/hole/heap↑/data/BSS/text
  - Demand paging: valid-invalid bit; page fault 6 steps (trap → check → free frame → disk read → update PTE → restart)
  - EAT with page faults: EAT = 200 + p×7,999,800; p < 1/400,000 for <10% degradation
  - Page replacement: dirty bit; FIFO (Belady's anomaly); OPT (benchmark); LRU (counter or doubly-linked list); second-chance/clock (ref bit); enhanced second-chance (0,0)/(0,1)/(1,0)/(1,1) priority table; LFU/MFU
  - Frame allocation: equal/proportional; global (higher throughput) vs local (consistent per-process); reapers
  - Thrashing: cause and locality model; working-set WSSᵢ(Δ); D=ΣWSSᵢ; policy (suspend process if D > total frames)
  - PFF: too-low → remove frames; too-high → add frames
  - Prepaging; TLB reach; page pinning (I/O interlock); programme structure impact on page faults
- Created: `wiki/concepts/deadlocks.md` (Chapter 10)
  - 4 necessary conditions: mutual exclusion, hold-and-wait, no preemption, circular wait
  - Resource allocation graph: request edges (P→R), assignment edges (R→P); cycle+single instance → deadlock; cycle+multiple instances → possible
  - Prevention: break one condition structurally; ordered resource acquisition (prevents circular wait, most practical)
  - Avoidance: safe state = safe sequence exists; Banker's algorithm (Available/Max/Allocation/Need matrices); Safety Algorithm O(m×n²); Resource-Request Algorithm (pretend allocate → run safety → grant or rollback); worked example with 5 processes/3 resource types
  - Detection: wait-for graph (single instance, O(n²) cycle detection); detection algorithm (multiple instances, similar to Safety Algorithm, O(m×n²)); invocation strategies (every request / periodic / CPU utilisation threshold)
  - Recovery: terminate all deadlocked processes or one at a time (selection criteria: priority/progress/resources/impact); resource preemption with rollback and starvation counter
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

---

## 2026-05-13 — Ingest: ICT1011 Computer Organisation and Architecture

- Action: INGEST
- Source: `raw/ICT1011 Computer Organisation Architecture Notes.md` (15,297 lines, OCR'd slide deck, 10 chapters)
- Authors: Steven Wong & Xin Lou, Singapore Institute of Technology, ©2024
- Created: `wiki/sources/ICT1011-computer-organisation-architecture.md`
  - Chapter map, concept page cross-references, key module themes
- Created: `wiki/concepts/computer-architecture-fundamentals.md`
  - Architecture vs organisation distinction
  - Von Neumann stored-program concept, Fetch–Decode–Execute cycle, Von Neumann bottleneck
  - Computer classes: supercomputer → mainframe → minicomputer → microcomputer → embedded/SoC
  - Three basic operations: Store / Transform / Transfer
  - Memory hierarchy: Registers (<1 ns) → Cache (8–35 ns, SRAM) → Main Memory (20–100 ns, DRAM) → Secondary (5–20 ms)
  - Clock (synchronous design) and Reset (PC→0)
  - MSP430: 16-bit RISC MCU, 27 instructions, 7 addressing modes, 16 registers
  - Register map: R0=PC, R1=SP (pre-decrement/post-increment), R2=SR/CG1 (N/Z/C/V + GIE + power bits), R3=CG2, R4–R15 GPR
  - SR flags: N (MSB=1), Z (result=0), C (unsigned overflow), V (signed overflow)
  - Memory map: 0x0000–0x01FF (8-bit peripherals), 0x2400 (RAM start), 0x4400 (Flash start), 0xFF80–0xFFFF (interrupt vectors)
  - Little-endian byte ordering
  - Instruction formats: Format I (double operand), Format II (single operand), Format III (10-bit signed jump, ±512 words)
  - 7 addressing modes: Register, Indexed, Indirect, Indirect Auto-increment, Symbolic, Absolute, Immediate
- Created: `wiki/concepts/assembly-programming-msp430.md`
  - 4-column assembly syntax (label / mnemonic / operands / comment)
  - Assembler directives: section (.text/.data/.bss/.sect/.usect), memory (.byte/.word/.string/.space), symbol (.equ/.set), linking (.global/.ref/.def/.end)
  - 2-pass assembly: Pass 1 → symbol table; Pass 2 → machine code
  - Executable instructions: MOV (no flags), ADD/ADDC/DADD/SUB/SUBC (arithmetic), AND/BIS/XOR/BIC (logical), RRC/RLC/RRA (rotation), CMP/BIT (comparison, flags only), JEQ/JNE/JC/JNC/JN/JGE/JL/JMP (control flow), PUSH/CALL/RETI (stack/subroutine)
  - Emulated instructions: NOP, CLR, INC, DEC, INV, TST, SETC/CLRC, EINT/DINT, RET, BR, POP
  - CALL mechanism: SP−2; Mem[SP]←PC+2; PC←target
  - RET mechanism: PC←Mem[SP]; SP+2 (= MOV @SP+,PC)
  - Parameter passing: (1) registers — fast/limited; (2) memory block — not re-entrant; (3) stack — general, supports recursion
  - Pass by value vs pass by reference
  - Stack frames for local variables: SUB #N,SP at entry; ADD #N,SP at exit; stack frame layout diagram
- Created: `wiki/concepts/io-and-memory-systems.md`
  - Parallel vs serial, simplex/half-duplex/full-duplex
  - Async serial format: start(Space=0) + 7/8 data bits LSB-first + optional parity + stop(Mark=1)
  - Baud rate = 1/T; data rate < baud rate due to framing overhead
  - RS-232: DTE↔DCE, inverted logic (Mark=−3 to −15 V, Space=+3 to +15 V)
  - Memory-mapped I/O (MSP430/ARM) vs isolated I/O (x86 IN/OUT instructions)
  - Polled I/O: busy-wait loop; CPU-inefficient
  - Interrupt-driven I/O: IRQ → push PC+SR → ISR → RETI; CPU free between events
  - Bluetooth: 2402–2480 MHz, 79 × 1 MHz channels, FHSS 1600 hops/s, TDD-TDMA, piconet (1 master + ≤7 active slaves), scatternet, BLE for IoT
  - HDD structure: platters/tracks/cylinders/sectors; access time = Ts + Tr (avg = 0.5/RPS) + Tt = N/(RPS×DT×DS)
  - RAID 0 (striping, performance), RAID 1 (mirroring, fault-tolerance), RAID 10 (stripe+mirror)
  - Bus: data (bits/transfer width), address (log₂ max memory), control (R/W, IRQ, clock, reset)
  - Synchronous bus (clocked, simple, inflexible) vs asynchronous bus (handshake, flexible, slow device bottleneck)
  - Memory performance: access time, cycle time (> access time), transfer rate = 1/cycle time
  - SRAM: cross-coupled inverter latch + 2 transistors; fast, low density, cache
  - DRAM: 1 transistor + 1 capacitor; needs periodic refresh; high density, main memory
  - ROM/Flash family: ROM (manufacture) → PROM (fuse burn) → EPROM (UV erase) → EEPROM (electrical byte erase) → Flash (electrical block erase, high density, SSDs/phones)
  - Memory management: uni-program vs multi-program; swapping (disk ↔ main memory, I/O cost)
  - Fixed partitioning: internal fragmentation; dynamic partitioning: external fragmentation → coalesce / compact
  - Paging: process → pages; memory → frames; page table maps page# → frame#; logical address = page# + offset → frame# + offset; eliminates external fragmentation; enables virtual memory; MMU performs translation
- Updated: `wiki/index.md` (1 new source row, 3 new concept rows)
- Updated: `wiki/hot.md` (new session summary, 10 new key facts, new domain summary, recent changes)
- Updated: `wiki/log.md` (this entry)

---

## 2026-05-12 — Synthesis: RE×Security and RE×HCI gaps filled

- Action: SYNTHESISE
- Trigger: user requested both open gaps be filled
- Created: `wiki/synthesis/re-elicitation-cia-aaa-security-requirements.md`
  - McCall's Integrity as the bridge: CIA+AAA unpacks what "resist unauthorised access" means in practice
  - RE lifecycle (Eliciting → Analysing → Specifying → Validating → Managing) mapped step-by-step onto SSDLC requirement phases
  - BCIC framework applied to security: "the system shall be secure" decomposed into atomic, verifiable statements
  - OSA taxonomy (Secure Functional / Functional Security / Non-Functional Security / Secure Development) mapped onto RE functional/non-functional split
  - iRTM extended with Threat column linking each security requirement back to its CIA-AAA pillar and attacker model risk
  - Mag7 quality attributes assessed against the specific challenges of security requirements (ambiguity of "encrypted", completeness of misuse cases, consistency tension between Availability and Confidentiality)
  - McCall's other features (Reliability, Correctness, Maintainability, Testability) mapped to adjacent security concerns
- Created: `wiki/synthesis/re-elicitation-hci-needfinding.md`
  - Method-by-method mapping table: RE interviews ↔ HCI semi-structured interviews; RE observation ↔ HCI direct/indirect observation; RE surveys ↔ HCI Likert/Semantic Differential; RE JAD workshops ↔ HCI focus groups; ethnography as unnamed-but-present in RE
  - Key divergence: RE produces formal SRS (complete, traceable, verifiable); HCI produces research artefacts (personas, HTA, insight reports)
  - Output connection pipeline: Needfinding → HTA/TDH → Use Cases → SRS requirements → iRTM
  - Concrete example tracing "Submit assignment" from HTA leaf to functional requirement to iRTM entry
  - Pain points → BCIC Interpret step → hidden requirements (with 3 worked examples)
  - Declarative/procedural knowledge distinction → differentiated non-functional usability requirements for novices vs experts
  - UCD "Specify requirements" phase identified as the handoff point from HCI to RE
- Updated: `wiki/synthesis/_index.md` (2 new rows + 2 domain sections), `wiki/index.md` (Synthesis table), `wiki/hot.md`, `wiki/log.md`

---

## 2026-05-12 — Example: Stock Prediction Neural Network ingested

- Action: INGEST
- Trigger: user opened project and requested wiki write-back
- Created: `wiki/examples/stock-prediction-neural-network.md`
  - Custom two-layer NumPy neural network with He init, adaptive LR, Monte Carlo uncertainty
  - SOLID + DIP architecture: interfaces in `core/interfaces.py`, concrete wiring at `ui/app.py`
  - 12-feature data pipeline from Yahoo Finance via yfinance
  - Composite 0–100 accuracy scoring (MAPE 50% + directional 30% + in-range 20%)
  - Band calibration from historical residuals targeting 75% in-range rate
  - Background threading pattern with message-queue UI bridge (Tkinter never freezes)
  - Key bugs: inconsistent data parsing (commit 00552e7) was root cause of occasional wrong predictions
- Updated: `wiki/index.md` (Examples table), `wiki/hot.md`

---

## 2026-05-12 — Ingest: INF2003 Database Systems

- Action: INGEST
- Source: `raw/INF2003 Database Systems Notes.md` (Lectures 1–10 + 2 Tutorials, Dr. Tong Rong + Zhang Wei, AY2025/26)
- Created: `wiki/sources/INF2003-database-systems.md`
- Created: 6 concept pages in `wiki/concepts/`
  - `relational-database-fundamentals` — DB/DBMS motivation, 3-level data abstraction (view/logical/physical), physical vs logical data independence, relational data model (relation/tuple/attribute/domain/NULL), key hierarchy (superkey→candidate→primary→foreign), ACID properties, 6 stages of DB design, integrity constraint types (domain/key/referential), DBMS architecture tiers
  - `relational-algebra-and-sql` — 6 fundamental RA operators (σ, π, ∪, −, ×, ρ) with notation and SQL equivalents; extended operators (∩, ⋈, outer joins ⟕⟖⟗, ÷, ←); query efficiency (push σ/π before joins); SQL DDL (CREATE/ALTER/DROP/data types); DML (INSERT/UPDATE/DELETE/SELECT with arithmetic and aliases); multi-table queries; explicit JOIN syntax; UNION/INTERSECT/EXCEPT with ALL variants; aggregate functions (SUM/COUNT/AVG/MIN/MAX) with NULL behaviour; GROUP BY and HAVING with evaluation order; subqueries (IN/EXISTS/ANY/ALL); NULL semantics; LIKE patterns; ORDER BY; CHECK constraints; 8 query optimisation tips
  - `database-normalisation` — anomalies (insertion/update/deletion/redundancy); functional dependencies (definition, notation, legal instance constraint); Armstrong's axioms (Reflexivity/Augmentation/Transitivity + Union/Decomposition/Pseudo-Transitivity); attribute closure algorithm (X⁺) with step-by-step example; uses of closure (key finding, FD derivability, equivalence); 1NF (atomic values); BCNF definition (every non-trivial FD must have a superkey LHS); BCNF violation detection; BCNF decomposition algorithm with two worked examples; lossless join property (BCNF guarantees ✓); dependency preservation (BCNF does not guarantee ✗); normalisation vs. performance trade-off
  - `er-diagrams` — ER model history and purpose; Chen notation (all symbols defined); entities and entity sets; 4 attribute types (key/composite/multivalued/derived) with notation; relationships and their own attributes; participation constraints (total/partial) with examples; cardinality (1:1/M:1/1:N/M:N); degree (unary/binary/ternary — avoid ternary); weak entities (partial key, total participation, ON DELETE CASCADE); ISA/subclass with overlap and covering constraints; ER→schema conversion rules for: entity sets, composite attributes (flatten), multivalued attributes (separate table), relationship sets, M:N relationships, participation constraints (merge), weak entities, subclasses (3 strategies: ER-style/OO/single-table-with-NULLs); design decision guidance (entity vs attribute, entity vs relationship, N-ary vs binary)
  - `database-indexing-transactions` — file organisation (heap/sorted/indexed); hash index (O(1) equality, no range queries); B+ tree structure (root/internal/leaf, linked leaves, 50% min occupancy, high fanout); B+ tree search O(log n) + range search via leaf list; B+ tree insert (locate→insert→split leaf→push to parent→recurse); B+ tree delete (locate→remove→borrow from sibling or merge→recurse); ACID deep-dive with responsibility table; schedules (serial/equivalent/serializable); interleaving anomalies (dirty read/non-repeatable read/lost update); SQL TCL (COMMIT/ROLLBACK/SAVEPOINT with worked example); lock granularity (DB/table/page/row/field); deadlock (prevention + timeout detection); optimistic 3-phase concurrency (read private copy→validate→write); recovery (write-ahead log, checkpoints, redo/undo, off-site backup)
  - `nosql-and-data-warehousing` — RDBMS limitations (centralisation, schema rigidity, geo-distribution); 4 NoSQL categories (KV/document/columnar/graph) with examples; Redis (O(1) operations, in-memory, rich types); MongoDB CRUD (insert/find/update/remove with JS examples), RDBMS→MongoDB mapping table; columnar storage vs row storage, Cassandra/HBase, Facebook MySQL→Cassandra benchmark; Neo4j (node+edge+property model), RDBMS→graph mapping table; when to use NoSQL; SQL→NoSQL migration (3 strategies); data warehouse definition, ETL phases, star schema (fact table + dimension tables, benefits/drawbacks), snowflake schema (normalised dimensions, complex queries); OLAP cube (slice/dice/drill-down/roll-up/pivot with SQL examples); OLTP vs OLAP full comparison table; blockchain as append-only hash-chained ledger (tamper-resistance mechanism, Proof-of-Work, limitations as a database)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`
- Status: Complete

---

## 2026-05-12 — Synthesis: ICT2112 × INF2007 Knowledge Gaps Resolved

- Action: SYNTHESISE
- Trigger: two gaps identified during ICT2112 ingest (same session)
- Created: `wiki/synthesis/dip-hilt-dependency-injection.md`
  - Maps ICT2112 Dependency Inversion Principle → INF2007 Hilt framework, annotation by annotation
  - Covers: @Inject constructor = DIP declaration; @Binds = binding abstraction to concrete; @Provides = IoC container provision; @Singleton = managed singleton vs GoF Singleton; Hilt component hierarchy = scope/lifetime management; testability argument (fake injection vs untestable direct instantiation); design smell diagnosis table
- Created: `wiki/synthesis/data-mapper-repository-room-retrofit.md`
  - Maps ICT2112 data source patterns (Active Record, TDG, Data Mapper) → Android Room + Retrofit stack
  - Active Record = Room @Entity used directly as domain model (acceptable for simple CRUD)
  - Table Data Gateway = Room @Dao (method-by-method mapping shown)
  - Remote Data Gateway = Retrofit annotated interface
  - Data Mapper = Repository class + mapper extension functions (Entity↔Domain, DTO↔Domain)
  - Facade = Repository hiding both DAO and Retrofit behind one interface
  - Includes: full stack diagram with patterns named at each layer, when-to-use table (Active Record vs Data Mapper), leaky abstraction smell, quality attribute mapping
- Updated: `wiki/synthesis/_index.md`, `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`
- Status: Complete

---

## 2026-05-12 — Ingest: ICT2112 Software Design

- Action: INGEST
- Source: `raw/ICT2112 Software Design Notes.md` (Topics 1–8, Asst. Prof. Alex Q. Chen, AY2025/26)
- Created: `wiki/sources/ICT2112-software-design.md`
- Created: 2 concept pages in `wiki/concepts/`
  - `software-design-process` — Software design pipeline (Architecture → Detailed → Construction), four roles of architecture, quality attributes (Microsoft model: 10 attributes across user-facing/run-time/design), architecture drivers, coupling scale (Content → Data), cohesion scale (Informational → Coincidental), ATAM (9-step process, sensitivity points, tradeoffs, risks), design smells (Rigidity, Fragility, Immobility, Viscosity, Needless Complexity, Needless Repetition, Opacity), construction design (flow-based: pseudocode/flowcharts; table-based: decision tables, state transition tables)
  - `software-architecture-patterns` — Layered 3-Tier architecture (benefits, rules), domain layer patterns (Transaction Script / Table Module / Domain Model), data source patterns (Table Data Gateway / Row Data Gateway / Active Record / Data Mapper with comparison table), presentation patterns (MVC / MVP / MVVM with testability comparison), SOA/Microservices patterns (Gateway / Service Registry / Circuit Breaker three-state model / Adapter), end-to-end design pipeline, Library Books Management System case study
- Updated: `wiki/concepts/solid-and-design-patterns.md`
  - Added Builder and Prototype (creational) with C# examples
  - Added all 7 structural patterns: Adapter, Decorator, Facade, Composite, Proxy, Bridge, Flyweight (with C# examples for Adapter, Decorator, Facade)
  - Added all 11 behavioural patterns: Observer, Strategy, Command, Iterator, Template Method, State, Chain of Responsibility, Mediator, Memento, Visitor (with C# examples for Observer, Strategy, Iterator, Template Method)
  - Expanded Pattern Selection Guide to all 23 GoF patterns
  - Updated course tag from INF1009 → ICT2112; updated See Also links
- Updated: `wiki/index.md` (new source row, 2 new concept rows), `wiki/hot.md`, `wiki/log.md`
- Status: Complete

---

## 2026-05-11 — Ingest: INF2008 Machine Learning

- Action: INGEST
- Source: `raw/INF2008 Machine Learning Notes.md` (Lectures L00–L12, Donny Soh)
- Created: `wiki/sources/INF2008-machine-learning.md`
- Created: 6 concept pages in `wiki/concepts/`
  - `ml-foundations` — AI definitions, four narrow-AI perspectives, expert systems vs ML, supervised/unsupervised/reinforcement learning, CRISP-DM phases mapped to production components, business understanding framework (problem/decision/metric/intervention/value), MoonHub churn and JuneBank loan examples
  - `ml-data-understanding` — 7 DU stages: data generation process, schema, data types (cardinal continuous/discrete vs categorical nominal/ordinal), completeness, sanity checks (plausibility, consistency, leakage), representativeness (class imbalance), granularity and aggregation
  - `ml-model-training-evaluation` — baseline models (majority class, mean, default DT), train-validate-test split, stratification (M&Ms analogy), k-fold cross-validation, confusion matrix, Type I/II errors, accuracy/balanced accuracy/precision/recall/specificity/F1, bias-variance trade-off (4 cases, corrective actions), learning curves
  - `decision-trees-and-ensembles` — Gini impurity formula and worked example, entropy, greedy tree construction, stopping criteria (max_depth, min_samples_split, min_samples_leaf), bagging/bootstrap sampling, Random Forests (OOB estimation: ~36.8% OOB, feature subsampling), AdaBoost, Gradient Boosting (loss gradients, iterative residual fitting, early stopping), stacking; comparison table
  - `neural-networks-linear-models` — label encoding vs OHE (advantages, dangers, when to use), simple and multiple linear regression, RMSE, 4-step gradient descent loop (forward pass, loss, backprop, update), vectorised multiple regression, neuron (z→σ→a), hidden activations (ReLU/Leaky ReLU/tanh), output activations (identity/sigmoid/softmax), backpropagation chain rule, cross-entropy loss, worked backprop example
  - `clustering-and-dimensionality-reduction` — distance measures (L1/L2/L∞), k-NN, K-means objective function (why the mean minimises it), K-means algorithm, elbow method, silhouette score, K-means++, DBSCAN (core/border/noise points, ε/MinPts effects), K-means vs DBSCAN comparison, PCA (5 steps: standardise, covariance matrix, eigendecomposition, project, interpret), t-SNE (Gaussian→t-distribution probabilities, KL divergence gradient descent, perplexity), PCA vs t-SNE comparison
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Ingest: ICT2216 Lectures 1 & 2

- Action: INGEST
- Sources: `raw/ICT2216 Lecture 1 Secure Software Development.md`, `raw/ICT2216 Lecture 2 Secure Software Development.md`
- Created: `wiki/concepts/owasp-top-10.md` — OWASP Top 10 (2025): all 10 categories with scenarios, code examples, case studies (Instagram, SolarWinds, Bybit, Log4Shell), mitigations, and vulnerability category taxonomy
- Created: `wiki/concepts/vulnerability-tracking-frameworks.md` — CVE, NVD, CAPEC, MITRE ATT&CK, CVSS; BSIMM-16 (goals, SSF domains, 2026 trends), OpenSAMM (maturity levels 0–3), Microsoft SDL; comparison table
- Updated: `wiki/concepts/secure-software-requirements.md` — added IEEE 729 definition, OSA taxonomy (4 requirement types), full SSDLC requirement process (feasibility → gathering → specification → validation), detailed CIA-AAA content (SingHealth case study, DDoS mitigations, SLA terminology, NIST 800-63 password guidelines), PCI SSF and NIST SSDF frameworks
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — added Secure Software Concepts section, linked new concept pages
- Updated: `wiki/index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Ingest: INF1004 Mathematics 2

- Action: INGEST
- Source: `raw/INF1004 Mathematics 2 Notes.md`
- Created: `wiki/sources/INF1004-mathematics-2.md`
- Created: 5 concept pages in `wiki/concepts/`
  - `descriptive-statistics` — types of data, population vs sample, measures of location (mean/median/mode), spread (variance, CV), relative standing (quartiles, boxplot)
  - `probability-theory` — classical/empirical/subjective probability, complement/union/intersection rules, conditional probability, independence vs mutual exclusivity, Bayes' theorem, law of total probability
  - `probability-distributions` — discrete RV (expected value, variance), binomial distribution, continuous distributions (uniform, normal, standard normal), combining independent RVs, sampling distribution, Central Limit Theorem (CLT), sampling methods
  - `linear-algebra-matrices` — matrix types and operations, determinants (2×2 and 3×3), inverse matrix (2×2 formula and Gauss-Jordan), SLE (Ax = b), vectors (magnitude, dot product, orthogonality), parametric line equations, 2D geometric transformations, linear regression (least squares)
  - `eigenvalues-and-svd` — characteristic equation, eigenvalue/eigenvector computation, diagonalisation ($A = PDP^{-1}$, $A^n = PD^nP^{-1}$), SVD ($A = U\Sigma V^T$), SVD computation steps, applications (image compression, PCA, recommender systems, pseudoinverse)
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 2 Example Page

- Action: INGEST
- Source: ICT2216 Lab 2 — SecurityRAT example page (lab PDF content confirmed by user)
- Created: `wiki/examples/ict2216-lab2-securityrat.md` — full compose files, step-by-step, CRLF fix, gotchas table, container architecture
- Updated: `wiki/examples/_index.md`, `wiki/index.md` — Lab 2 example entry added
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — Lab 2 example linked
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 1 Ingest

- Action: INGEST
- Source: ICT2216 Secure Software Development — Lab 1 (Docker + Docker Compose)
- Created: `wiki/concepts/docker-compose.md` — compose file structure, networking, volumes, all four services (Nginx, MySQL, Git, Selenium)
- Created: `wiki/examples/ict2216-lab1-docker-compose.md` — full compose files, build steps, port map, notes
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — added Lab 1, docker-compose concept, example page
- Updated: `wiki/examples/_index.md` — first entry added
- Updated: `wiki/index.md` — Concepts and Examples tables
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 2 Ingest

- Action: INGEST
- Source: ICT2216 Secure Software Development — Lab 2 (SecurityRAT + Secure Requirements)
- Created: `wiki/sources/ICT2216-secure-software-development.md`
- Created: `wiki/concepts/secure-software-requirements.md` — CIA + AAA pillars, risk identification, SANS SWAT / OWASP ASVS mapping
- Created: `wiki/resources/securityrat.md` — Docker setup, CRLF fix, default creds, container architecture
- Created: `wiki/learning/docker-windows-crlf.md` — Windows CRLF breaks Linux container scripts; Git Bash path translation gotcha
- Updated: `wiki/index.md` — Sources, Concepts, Learning, Resources tables
- Status: Complete

---

## 2026-05-11 — Ingest: INF1003 Mathematics 1

- Action: INGEST
- Source: `raw/INF1003 Mathematics 1 Notes.md`
- Created: `wiki/sources/INF1003-mathematics-1.md`
- Created: 5 concept pages in `wiki/concepts/`
  - `discrete-mathematics-foundations` — sequences (AP/GP/recurrence), number theory, modular arithmetic, GCD/LCM, Euclidean algorithm, RSA
  - `combinatorics` — product/sum/division rules, permutations, combinations, pigeonhole principle
  - `propositional-logic` — connectives, truth tables, tautologies, De Morgan's laws, logical equivalences
  - `predicate-logic-and-proofs` — quantifiers (∀/∃), negation rules, rules of inference (modus ponens/tollens etc.), proof methods
  - `sets-functions-relations` — set operations/identities, power sets, function types (injective/surjective/bijective), relation properties, equivalence relations, partial orders
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Structure Update & Writing Style

- Action: CONFIGURE
- Graph view: 13 colour groups applied to `graph.json` — each wiki folder now maps to its vault colour (blue = concepts/synthesis, green = sources, purple = examples/entities, gold = areas, teal = goals/learning, orange = resources, red = gaps, steel-blue = meta, grey = raw/templates)
- vault-colors.css: Added `wiki/examples` → purple nav colour
- CLAUDE.md: Added Writing Style section (British English, grammatically correct prose)
- CLAUDE.md: Updated Vault Structure diagram to include all subfolders
- wiki/examples/: Created folder with `_index.md` — for real-world examples and lab sessions
- wiki/index.md: Added Examples table section
- Status: Complete

---

## 2026-05-11 — First Ingest: 5 Course Notes

- Action: INGEST
- Sources: ICT2113, INF1008, INF1009, INF2007, INF2002
- Created: 5 source index pages in wiki/sources/
- Created: 12 concept pages in wiki/concepts/
  - requirements-engineering, lightweight-rcm (ICT2113)
  - algorithm-complexity, data-structures-fundamentals, sorting-and-searching, graph-algorithms (INF1008)
  - oop-four-pillars, solid-and-design-patterns (INF1009)
  - android-architecture, kotlin-coroutines (INF2007)
  - hci-fundamentals, needfinding-and-task-analysis (INF2002)
- Updated: wiki/index.md (Sources + Concepts tables), wiki/hot.md, raw/.manifest.json
- Status: Complete — vault ready for study/review use

---

## 2026-05-11 — Vault Scaffold

- Action: SCAFFOLD
- Mode: D (Personal / Second Brain) + E (Research)
- Purpose: Personal knowledge base for everything learned and to learn, linking knowledge, filling gaps
- Created: wiki/ structure with 9 domain folders + 4 meta files
- Created: Mode D+E templates (goal, learning, synthesis, gap)
- Applied: vault-colors.css visual customization
- Status: Ready for first ingest
