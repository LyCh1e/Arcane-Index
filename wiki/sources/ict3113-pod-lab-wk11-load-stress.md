---
type: source
title: "ICT3113 POD — Week 11 Lab (Lec07): Performance Testing, Load and Stress"
domain: performance-engineering
source-type: lab-handout
course: ICT3113
status: ingested
created: 2026-11-13
updated: 2026-11-13
tags: [ict3113, lab, load-test, stress-test, pyload, little-law, knee, ceiling, serialisation, lock]
---

# Source: ICT3113 Week 11 Lab (Lecture 07) — Performance Testing, Load and Stress

**File:** `raw/ICT3113 Performance Optimisation and Design - Lec07 Week 11 Lab Performance Testing Load and Stress.md`
**Type:** lab handout with blank answer tables (no measured results are included)
**Companion lecture:** [[sources/ict3113-pod-l7]]
**Worked write-up:** [[examples/ict3113-lab-wk11-load-stress-build-c]]

---

## Summary

The lab runs two of the Lecture 07 tests, a **load test** and a **stress test**, against **Build C** of the lecture's order API. Build C is the lecture's Build A with one undisclosed change to `app.py`. The student reads the results by column, then works from the numbers to the code and finds the fault. The stated aim is "knowing which test answers which question, and reading the table by column", not the service itself.

## Learning outcomes (as stated)

1. Run a load test and a stress test with `pyload.py` and read the one-row result from `analyse.py`.
2. Decide pass or fail against a written requirement, not against a chart.
3. Read a stress table by column: knee, ceiling, failure mode, and which resource is the ceiling.

## Structure

| Section | Content |
|---|---|
| 0. Environment | Python 3.10+, `flask requests psutil pandas matplotlib`; `lab07.zip` unzipped to a plain local folder (**not** OneDrive, Google Drive, Dropbox or a synced Desktop/Documents); three Command Prompt windows (A service, B monitor, C commands) |
| 1. Start the service | Order API: `POST /orders` verifies a token with PBKDF2 (100,000 rounds of SHA-256), checks items against the catalogue, stores the order in an in-memory dictionary. Record core count c, mean service time S and the laptop |
| 2. Load test | Requirement **LAB-01** (95% of `POST /orders` within 200 ms at 5 req/s open loop for 3 minutes); then reconcile the generator's count with the server's log |
| 3. Stress test | Seven one-minute steps at 5, 10, 15, 20, 25, 30 and 40 req/s with a 20 s timeout; read knee, ceiling, failure mode, `cpu_pct` |
| 4. What the numbers say | Compare the measured ceiling with c/S; use `cpu_pct` and Little's Law to find how many requests are in service at once; read `app.py`; fix; rerun as r2 (same steps) and r3 (higher steps) |

## Tools and files

- `pyload.py` is a roughly 60-line **open-loop** generator at a fixed arrival rate, with the same body checks as the JMeter plans, writing a JMeter-format `.jtl`. It stands in for JMeter (the module's tool); the results files are interchangeable with JMeter's Open Model Thread Group.
- `analyse.py` turns `.jtl` and monitor CSVs into the results table. It **drops the first 20 seconds** as warm-up and reports the **highest run number** it finds.
- `monitor.py` writes whole-machine CPU and memory every 10 seconds.
- `single_request.py` sends one order to check the body, then `--n` more to measure S.
- File names `demo1-r1` (load) and `demo2-r1` (stress) match what `analyse.py` expects.

## Key teaching points

- **Pass or fail comes from the written requirement (field 3), not the chart.**
- **Count reconciliation:** `.jtl` count + 21 must equal the server log count (1 body check + 20 service-time requests are in the log but not the `.jtl`). A mismatch means requests timed out, hit a stale server, or something else was sending. This protects against Lecture 07 Demo 6, where the generator reported 100% success and the server logged only errors.
- **`samples` in the table is smaller than both counts** because of the 20 s warm-up drop.
- **A load test cannot name a fault; a stress test can.** The remark says: a service that had every core available but behaves like one core has code that forces it to.
- **`cpu_pct` is whole-machine.** One fully busy core reads about 100/c percent, so a low reading does not always mean spare capacity.
- **Diagnosis path:** ceiling near 1/S plus near-idle CPU means one request at a time, so something makes requests wait for one another. The candidates in a threaded Flask app are a lock held around slow work, a single worker, one shared connection, or pure-Python CPU work under the interpreter lock. `hashlib` releases the interpreter lock, which leaves a **lock or a single worker**.
- **Fix:** the lock should cover only the part that must not run in two threads at once, the write to the store.
- **Prove it twice:** r2 repeats the same steps so r1 and r2 differ only in code; r3 goes higher (10 to 200 req/s) because a stress test that never reaches the knee has found only a lower bound.
- **If the r3 ceiling is still far below c/S:** suspect the generator sharing the machine first, a synced folder second.

## What the file does not contain

- No measured values: every answer table is blank.
- No `app.py` source and no statement of Build C's change. The fix described above is the handout's own hint (narrow the lock to the store write); the actual line is not shown.

## Related pages

- [[examples/ict3113-lab-wk11-load-stress-build-c]] — method, formulas and expected figures
- [[sources/ict3113-pod-l7]] — Demos 1, 2 and 6 that this lab repeats
- [[concepts/performance-engineering]] §Performance Testing — test types, open and closed loop; §Reading a stress table
- [[concepts/queueing-theory]] — Utilisation Law, ceilings (X ≤ c/D)
- [[concepts/connection-pool-diagnosis]] — the same c/S arithmetic applied to a connection pool (Week 12)
- [[sources/ict3113-pod-lab-wk12-slow-endpoint]] — the following week's lab
