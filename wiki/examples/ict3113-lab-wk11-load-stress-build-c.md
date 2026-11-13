---
type: example
status: established
created: 2026-11-13
updated: 2026-11-13
name: ict3113-lab-wk11-load-stress-build-c
description: ICT3113 Week 11 lab (Lecture 07) — method, formulas and expected figures for the load test and stress test on the order API Build C, including the count reconciliation and the lock-serialisation diagnosis; not yet run, so no measured results
metadata:
  type: example
domain: performance-engineering
course: ICT3113
tags: [ict3113, lab, load-test, stress-test, pyload, littles-law, knee, ceiling, serialisation, lock, pbkdf2]
---

# ICT3113 Week 11 Lab — Load and Stress Test on Build C

**Source:** [[sources/ict3113-pod-lab-wk11-load-stress]]
**Concept pages:** [[concepts/performance-engineering]] §Performance Testing · [[concepts/queueing-theory]] · [[concepts/connection-pool-diagnosis]]

> **Status: not yet run.** The handout has blank tables and `lab07.zip` is not in the vault. Every figure below is either the handout's own number, arithmetic from it, or an illustration marked as such. Add the measured r1, r2 and r3 rows to the tables at the end after running the lab.

---

## What is being tested

The lecture's order API (`POST /orders`): verify a token with PBKDF2 (100,000 rounds of SHA-256), check items against `catalogue.json`, store the order in an in-memory dictionary. PBKDF2 is almost all of the service time S. Build C is Build A with one hidden change to `app.py`.

## Run order

| Step | Window | Command |
|---|---|---|
| Start service | A | `cd C:\lab07\service` · `del orders.log` · `set ORDERS_BUILD=C` · `python app.py` |
| Check S and c | C | `echo %NUMBER_OF_PROCESSORS%` · `python single_request.py --n 20` |
| Monitor | B | `python monitor.py --out ../results/demo1-r1-mem.csv --interval 10` |
| Load test | C | `python pyload.py open --rate 5 --minutes 3 --out ../results/demo1-r1.jtl` |
| Analyse | C | `python analyse.py --results ../results` |
| Count check | C | `find /c "POST /orders" ..\results\demo1-r1.jtl` · `find /c "order=" ..\service\orders.log` |
| Stress test | C | `python pyload.py open --rate 5,10,15,20,25,30,40 --minutes 1 --timeout 20 --out ../results/demo2-r1.jtl` |
| Analyse | C | `python analyse.py --results ../results --step 60 --rates 5,10,15,20,25,30,40` |

Mac or Linux: `export` for `set`, `rm` for `del`, `grep -c` for `find /c`; turn off AirPlay Receiver if it holds port 5000.

## Load test (LAB-01)

Requirement: 95% of `POST /orders` complete within 200 ms at 5 req/s (open loop) for 3 minutes. Decide pass or fail from p95 against 200 ms, not from a chart.

**Expected counts (arithmetic from the settings):**

| Quantity | Expected |
|---|---|
| Requests sent in 3 minutes | 5 req/s × 180 s ≈ 900 |
| Samples after the 20 s warm-up drop | 5 × 160 s ≈ 800 |
| Lines in `orders.log` | `.jtl` count + 21 ≈ 921 |

Why 21: one body-check order plus 20 service-time orders from `single_request.py` are in the server log but not the `.jtl`. A short log means requests timed out or hit a stale server. A long log means another sender, or an old log not deleted. This is the Lecture 07 Demo 6 protection ([[sources/ict3113-pod-l7]]).

## Stress test — reading by column

| Column | Question | Reading |
|---|---|---|
| p95 | Where is the knee? | First step where p95 stops being flat and climbs |
| thr | Where is the ceiling? | Throughput that stops rising however much more is offered |
| err | What is the failure mode? | When errors start, and whether they are timeouts (20 s) or refusals |
| cpu_pct | What is the machine doing? | Whole-machine; one busy core reads about 100/c % |

## Section 4 — from numbers to code

| Quantity | Formula | Unit |
|---|---|---|
| Ceiling if every core works | c / S (S in seconds) | req/s |
| Machine CPU if every core is busy | 100 % (whole machine) | % |
| Requests in service at once | measured ceiling × S (Little's Law) | requests |

**Illustration only (the lecture's laptop, not the student's run):** [[sources/ict3113-pod-l7]] records S = 64 ms on an 8-core laptop.

| Quantity | Working | Value |
|---|---|---|
| c / S | 8 / 0.064 s | 125 req/s |
| Ceiling if one request at a time | 1 / 0.064 s | about 15.6 req/s |
| Whole-machine CPU with one core busy | 100 / 8 | about 12.5% |
| Requests in service at the 15.6 req/s ceiling | 15.6 × 0.064 | about 1 request |

This is the shape the handout describes: **ceiling near 1/S, CPU near idle, about one request in service**. Lecture 07 Demo 2 (one core pinned) showed a ceiling of 13–15 req/s, the same order of magnitude. The stress steps of 5 to 40 req/s reach past that ceiling for this reason.

**Diagnosis, in the handout's order:**

1. Name the shape: requests are waiting for one another.
2. List the candidates in a threaded Flask app: a lock held around slow work, a single worker, one shared connection, or pure-Python CPU work under the interpreter lock. `hashlib` releases the interpreter lock, which leaves a lock or a single worker.
3. Read `create_order` in `app.py`: find the `verify()` call, see what encloses it, and ask whether the comment justifying it is true.
4. Change one thing: the lock covers only the write to the store.

The handout does not show the code, so the exact lock and comment are for the student to find.

## Proving the fix

| Run | Steps (req/s) | Purpose |
|---|---|---|
| r1 | 5, 10, 15, 20, 25, 30, 40 | Build C baseline |
| r2 | same as r1 | Differs from r1 only in the code |
| r3 | 10, 20, 40, 80, 120, 160, 200 | r2 probably never reached the knee, so a stress test that has not found it has found only a lower bound; r3 finds where the new ceiling is |

**Expected after the fix (*inference*):** throughput follows offered load through r2; in r3 the ceiling rises towards c / S (about 125 req/s with the lecture's figures), and CPU rises towards 100%. If r3 stays far below c / S, suspect the generator sharing the machine, then a synced folder.

`analyse.py` reports the highest run number it finds. To see r1 again, copy `demo2-r1.jtl` and `demo2-r1-mem.csv` into `results\r1\` and point `--results` there.

## Gotchas

- Do not unzip under OneDrive, Google Drive, Dropbox or a synced Desktop or Documents folder: the service reads a file on every request and a sync client changes every result.
- Delete `orders.log` before every service restart; the count check depends on it.
- Do the count check before restarting for the stress test, because the restart deletes the log.
- Leave the laptop alone during the 3-minute and 7-minute runs; the generator and service share the machine.

## Results to add after running

| Item | r1 (Build C) | r3 (fixed) |
|---|---|---|
| Core count c, S (ms), laptop | | |
| LAB-01 p95 and verdict | | |
| Count check (`.jtl`, `.jtl` + 21, log) | | |
| Knee (req/s) | | |
| Ceiling (req/s) | | |
| cpu_pct at the ceiling | | |
| Where errors start | | |
| Line changed in `app.py` | | |
