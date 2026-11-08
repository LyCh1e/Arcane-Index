---
type: source
title: "ICT3113 POD Lec07 — Performance Testing"
domain: performance-engineering
source-type: lecture-notes
course: ICT3113
status: ingested
created: 2026-10-06
updated: 2026-11-08
tags: [ict3113, performance-testing, load-test, stress-test, soak-test, regression-test, benchmark, pipe-clean, open-loop, closed-loop, test-environment, playbook, bondi, jmeter]
---

# Source: ICT3113 POD Lec07 — Performance Testing

**File:** `raw/ICT3113 Performance Optimisation and Design - Lec07 Performance Testing.md`
**Presenter:** A/Prof Donny Soh
**Scope:** Types of performance test, test environment, load generation (65 slides)

---

## Summary

Lec07 closes the model-to-measurement arc by showing how to check queueing-model predictions against a real running system. It covers four documents that carry performance work from requirement to operations, six distinct test types with recorded demos on a small order API, the open-loop vs closed-loop distinction, test environment principles, and a playbook that another person can follow to reproduce any result.

---

## Learning Outcomes

- Distinguish six types of performance test and state which question each one answers.
- Set up a test environment that stands in for production, and know when it cannot.
- Build a load model and generate load correctly, including the open/closed-loop difference.
- Write a performance requirement and a playbook another person can execute.
- Read a results table and distinguish saturation from a bug.

---

## Key Concepts Introduced

| Concept | Where developed in wiki |
|---|---|
| Six performance test types | [[concepts/performance-engineering]] §Performance Testing |
| Open-loop vs closed-loop load | [[concepts/performance-engineering]] §Performance Testing |
| Bondi's 10-field requirement structure | [[concepts/performance-engineering]] §Performance Testing |
| Eckhardt sentence patterns | [[concepts/performance-engineering]] §Performance Testing |
| Test environment principles (scale-up/out, observer effect) | [[concepts/performance-engineering]] §Performance Testing |
| Playbook structure | [[concepts/performance-engineering]] §Performance Testing |

---

## Demos (Recorded Runs, Order API)

| Demo | Test type | Setup | Key finding |
|---|---|---|---|
| Demo 1 | Load test | 10 req/s, 3 min × 3 runs, 8 cores | p50 40 ms ≈ S = 34 ms; p95 100–120 ms; CPU 16% ≈ predicted 15%; no errors. Model held. |
| Demo 2 | Stress test | Stepped 5→30 req/s, 1 core pinned | Knee between 5 and 10; ceiling 13–15/s; ungraceful: 50% errors at 30/s; p50 drops when failures are fast |
| Demo 3 | Soak test | 8 req/s, 10 min | Memory: 33→68 MB, +3.4 MB/min (straight line); p95 flat; predicted 1.9, observed 3.4 due to Python object overhead |
| Demo 4 | Regression test | 5 req/s, Build A vs Build B (O(n) duplicate check), 8 min | Build B: p50 +30%, p95 +45% — regression detected; slope only visible at higher load/longer run |
| Demo 5 | Benchmark | 5 req/s, 25k / 100k / 400k PBKDF2 iterations | 25k→100k: p50 ×4; 400k: near-total collapse (83% timeouts, throughput 0.8 < ceiling 2.5) — ghosts waste CPU |
| Demo 6 | Pipe-clean | Broken catalogue path, no body assertion | 100% "success" reported, 0 orders created; p95 39 ms vs expected 360 ms — test measured error overhead, not service |
| Demo 7 | Observer effect | Demo 1 with/without cProfile | p95 100 ms → 110 ms; small here because PBKDF2 is a C call; pure Python handlers can double under cProfile |

---

## Concrete Numbers (Reference)

| Quantity | Value | Context |
|---|---|---|
| S (laptop, 8 cores) | 64 ms | Demo 1 single-request check |
| S (sandbox, 1 core) | 34 ms | Demo 1 sandbox |
| S (sequential, 1 core, fresh connection) | 112 ms | Demo 2 setup |
| Inferred S from CPU (8 cores) | ~35 ms | 8% of 8 cores ÷ λ |
| Actual S from stress ceiling (1 core) | ~70 ms | ceiling ≈ 1/S |
| Store bytes per order (predicted) | 4 kB | 4 kB × ~4,900 = 20 MB |
| Store bytes per order (observed) | ~7 kB | Python object overhead |
| Memory growth rate (soak) | 3.4 MB/min | Demo 3 |
| Time to 16 GB at soak rate | ~3.3 days | Extrapolation |

---

## References Cited

- Bondi (2015), Table 7.2 — 10-field performance requirement structure
- Eckhardt et al. (2016) — sentence patterns for performance requirements
- Miller (1968), Nielsen (1993) — response time thresholds (100 ms / 1 s)
- Molyneaux (2014), Chapter 3 — test environment setup
- Google Cloud blog (2016) — Pokémon Go launch: planned 5×, got 50×

---

## Related Pages

- [[concepts/performance-engineering]] — primary concept page; §Performance Testing added from this lecture
- [[concepts/performance-metrics]] — metric definitions, utilisation law
- [[concepts/queueing-theory]] — M/M/1, knee curve, bounds
- [[sources/ict3113-pod-l2]] — metrics and modelling fundamentals
- [[sources/ict3113-pod-l3]] — workload identification and estimation
- [[sources/ict3113-pod-l5]] — performance bounds, Erlang B
- [[sources/ict3113-pod-l6]] — JMeter test plan sizing, Little's Law


---

## Transcript Additions (Re-recorded Live Lecture)

*Source: `raw/ICT3113 Performance Optimisation and Design - Lec07_transcript.md`*

The lecturer re-recorded the lecture after a viewer reported audio problems. It has three parts: (1) performance requirements documents, (2) the six test types with demos, and (3) the test plan. The speech-to-text output is noisy ("Genita" and "Geometer" are JMeter; "soken" and "soup test" are the soak test), so only points clear enough to rely on are recorded below.

### Why this lecture matters (AI framing)

> "These are some tests that AI cannot run for us."

- AI can help **write** a test and help **analyse** results, but its own sandbox is a different environment from yours, so results produced there are typically not accurate.
- Letting an agent run tests on the real test environment would require a level of control that the lecturer does not expect to be common by the time students graduate. Students are therefore expected to **run their own tests** and **judge the results**.
- Judgement stays human: deciding whether a test really assesses what is wanted, and which parts of the system need improvement.
- A human must provision hardware, software and tools, and should **review the results after every script run** rather than let an agent run script after script without analysis.

### Part 1 — Requirements documents

- Four documents exist, but **this module covers only three**: the requirements plan, the measurement plan and the test plan.
- Bondi's template has 10 fields. The lecturer calls **field 3 (the statement) the most critical**; the other fields exist to support it. His reading of the supporting fields:
  - Field 4: supporting commentary.
  - Field 5: **precedent** (reference papers, or another company with a similar response time).
  - Field 6: **derivation** (back-calculate from the workload and the compute resources, for example "I expect 10 requests per second").
  - Field 9: the tools used to measure the requirement.
- Sentence patterns are assembled by choosing one entry per column. Examples given:
  - Response time: during the first 10 minutes of 11.11, the add-to-cart operation shall have a **mean** response time of no more than **200 ms**; the checkout operation shall have a **95th-percentile** response time of no more than **50 ms** (as spoken).
  - Throughput: the checkout operation shall have a **mean throughput of no less than 1,000 orders per second**.
- **Worked exercise:** *"The ordering system shall be fast and scalable, and shall handle peak loads without noticeable slowdown."* Answer: split it into at least two requirements.
  - "Fast" has no quantifiable meaning, so it becomes an **order-creation response-time** requirement ("95% of requests shall complete within 200 ms").
  - "Handle peak loads without noticeable slowdown" becomes a **throughput** requirement (a minimum order rate at peak load, at a stated error rate, with response time rising by no more than a stated amount).
  - "Scalable" is a possible **third** requirement, but it is harder to write and **fits neither template**, so it was deliberately left out.
- Performance requirements must pass the same quality checks as functional requirements.

### Part 2 — Test types: points that differ from, or add to, the slides

- **Closed vs open loop:** JMeter's standard Thread Group is closed-loop (offered load = N ÷ (response time + think time)). The remaining tests use **open-loop** arrivals, which is also how real traffic behaves: customers do not stop arriving because the previous request is pending.
- **Pokémon Go (2016):** planned for 5× the expected load and received 50×. Answer to the pause-the-video question: the **stress test**. A load test, even at several times the expected load, would still have passed.
- **Load test:** set the arrival rate from the workload model, run long enough to be stable, record p50, p95, p99, CPU and memory, and judge pass or fail against the Part 1 requirement. The demo uses four terminals (server, load generator, monitor script writing CSV, live CSV tail) and a **single-request check** first to get the unloaded response time.
- **Stress test:** step the arrival rate up (5, 10, 15, 20, 25, 30 req/s, one minute each) and look for the knee. In the spoken walk-through, throughput reached a ceiling of about 12, with roughly one in three requests refused at 20 req/s, about 40% at 25 and about 50% at 30. **p50 falls as errors rise because fast refusals are counted in the median**, so a falling p50 is not a good sign.
- **Soak test:** hold a load **below the knee** for a long time, so any failure comes from something like memory and not from saturation. The demo service keeps orders in **process memory**, so memory rises in a straight line while p50 stays flat over 10 minutes. Key point: **neither the load test nor the stress test would have caught this**, because both ran too briefly and focused on response time and not memory.
- **Regression test:** compare Build A and Build B under an identical load (5 req/s for 8 minutes). Throughputs matched; p50 rose slightly; **p95 and p99 rose a lot**, which warrants digging deeper. Motivation: if a regression is found only after everything is built, it is hard to tell which component is responsible, so test after each change.
- **Benchmark:** the same request at a fixed 5 req/s with 25,000, 100,000 and 400,000 hash iterations. Spoken p95 values: about 110 ms, about 480 ms and about 20 s; throughput held at 5 for the first two and dropped sharply at 400,000. The lecturer suspects the ~20 s figure is a **client timeout** (requests abandoned after waiting), which matches the slides' 83% timeouts.
- **Pipe-clean:** a missing file path makes the server catch the error and return **HTTP 200**, so the generator shows 100% success and healthy p50, p95 and p99. A hint that something is wrong: during a stress test the system seems to scale far but never takes on additional requests. The fix is an **assertion on the response body**, which exposes the hidden "no such file or directory" error.
- This is the lecturer's **first time including these demos**; he invites feedback. The next lecture is expected to show stepwise **diagnosis and resolution** of the issues the demos expose.

### Part 3 — The test plan

- A test plan is an **experiment**. It must be **reproducible** ("it can be bad all the time, but at least it must be consistently bad"), **unambiguous** (different readers interpret it the same way), **controlled** (a dedicated machine with nothing else running), built on **validated instruments** (the pipe-clean test), and **traceable** for audit.
- **Repeat each experiment** 3, 4 or 5 times; consistent results show reproducibility.
- **Observer effect**, linked back to Lab 1: profiling made code run several times slower, because the measuring tool competes with the system under test.
- **Lab caveat:** running client and server on one laptop in the JMeter lab is **normally not the right setup**. It was chosen for convenience, because earlier cohorts spent a whole session configuring two laptops, which turned the lab into a networking exercise. In practice the load generator and server belong on different machines (the earlier Google Cloud experiment was the more realistic setup).
- **Scaling vocabulary:**

| Direction | Name | What changes |
|---|---|---|
| Scale **up / down** | Vertical | Machine power (cores, RAM); number of machines unchanged |
| Scale **out / in** | Horizontal | Number of identical machines; per-machine power unchanged |

- **Worked scaling example** (3 identical web servers, each 12 cores, one shared database; production per-core load 8.3 req/s):
  - **Option A, scale in** to one 12-core server taking 100 req/s: per-core load stays **100 ÷ 12 = 8.3 req/s**, so it is a good estimate of production.
  - **Option B, scale in and down** to one 4-core server still taking 100 req/s: per-core load becomes **25 req/s**, which is **wrong**. The offered load must be cut to **about 33.3 req/s** so that per-core load is again **8.3 req/s**.
  - Rule: whatever you shrink, keep the **per-resource load** equal to production.
  - *Inference:* the transcript gives only the 100 req/s figure for the single-server case; a production total of 300 req/s follows from 3 × 100 and agrees with the slides' "L/3" wording.
- **Playbook:** a step-by-step written procedure so someone else can run the whole test with little supervision from its author.
- **Load generators to know:** JMeter (used in the module); **Locust** (the lecturer's engineering team prefers it as easier; not covered this term); **LoadRunner** (never used by the lecturer).
- **User types and load model:** before building a load model, find out what users actually do on the site (browsing, buying, comparing prices) and segment them. From each segment derive **think time**, **pacing** and **load profile** (when they come: lunchtime browsing, office-hours buying, after hours, the 08:00–09:00 commute). Scripts then describe each user type's behaviour.
- **Functional vs performance mindset:** a functional test asks whether the software works correctly; a performance test asks whether it performs well *every time*. The lecturer's maxim: *"Don't practise until you get it right; practise until you don't get it wrong."*
- **Roadmap:** one or two more lectures on performance testing (including databases); the final assignment covers **diagnostics** (after measuring, how to improve).

### Discrepancies with the slide deck

The spoken figures differ from the slides' recorded runs, so the slides remain the authoritative numbers. The lecturer may have been describing an earlier set of runs.

| Item | Slides (above) | Spoken in re-recording |
|---|---|---|
| Demo 1 latency at 10 req/s | p50 40 ms, p95 100–120 ms | p50 about 70 ms, p95 about 120 ms, p99 about 150 ms |
| Demo 2 ceiling | 13–15 req/s | about 12 req/s |
| Demo 3 load | 8 req/s | not stated ("below the knee") |
| Number of demos | 7 (includes observer effect) | 6 test types; observer effect discussed in Part 3 only |
