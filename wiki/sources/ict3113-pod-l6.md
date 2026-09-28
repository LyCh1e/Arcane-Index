---
type: source
title: "ICT3113 POD — L6: JMeter Recap"
source_file: "raw/ICT3113 Performance Optimisation and Design - Lec06 JMeter Recap.md"
module: ICT3113 Performance Optimisation and Design
domain: performance-engineering
tags: [ict3113, performance-engineering, jmeter, load-testing, littles-law, test-plan-design, apdex, think-time, concurrent-users]
created: 2026-09-24
updated: 2026-09-24
lecturer: "Donny Soh"
address: c-000123
---

# Source Index — ICT3113 POD: Lecture 6 — JMeter Recap

**Module:** ICT3113 Performance Optimisation and Design  
**Lecturer:** Donny Soh  
**Raw file:** `raw/ICT3113 Performance Optimisation and Design - Lec06 JMeter Recap.md`  
**Concept pages:** [[concepts/performance-engineering]] · [[concepts/performance-metrics]]

Practical recap bridging Lec01–Lec05 theory to JMeter test plan design. The single learning outcome is: *derive Thread Group parameters from a workload description using Little's Law (L = λW)*. The lecture works through three progressively harder examples and demonstrates timer placement for think-time modelling.

> [!note] Previous wiki entry
> This content was previously attributed to Lec05 in the wiki (source page `ict3113-pod-l5.md`). That page has been corrected to cover the real Lec05 (Estimating Performance and Lost Work). This page supersedes the old Lec05 JMeter entry.

---

## Section Coverage

| Section | Key Content |
|---------|-------------|
| Flask App to Profile | `/sort` endpoint with `flask_profiler.profile()` decorator; verify in browser before loading with JMeter |
| JMeter Thread Group | Number of Threads, Ramp-up Period, Loop Count, Same user on each iteration |
| HTTP Request Sampler | Protocol, Server/IP, Port, Method, Path, Parameters — wired to `127.0.0.1:5000/sort` |
| Non-GUI Mode | `jmeter -n -t lab03.jmx -l test-results.csv -e -o report`; command-line execution for real test runs |
| Constant Timer | Fixed think time (e.g. 3 000 ms) between consecutive HTTP requests within one thread |
| Gaussian Random Timer | Random think time: mean = Deviation + Constant Delay Offset; models realistic user pacing |
| Timer Timing Diagram | U1–U5 each fire T1→T2 staggered by ramp-up; sleep between T1 and T2 is the think time |
| Objective: Concurrent User Replication | Goal is to reproduce N simultaneous users; each user's session spans W seconds |
| Little's Law for Test Plans | L = λ × W → Threads = (N_users / Ramp_up) × avg_session_time; cap by total user count |
| 30 Users in 5 Seconds | Six-user-per-second batch; peak concurrent = 30 (all groups overlapping) |
| Parameter Derivation | Given target L and known W, solve for ramp-up: T = N_users × W / L |
| APDEX | Application Performance Index: 0.000 when every request exceeds the 500 ms toleration threshold |
| Worked Example 1 | 100 users, 5 s window, 10 s session → L = 200 > 100 → cap at 100 concurrent |
| Worked Example 2 | 100 users, 5 s window, 500 s session (150+50+300) → L = 10 000 > 100 → cap at 100 concurrent |
| Worked Example 3 | 20 users/s arrival rate, 500 s session → L = 10 000; no cap (no total user count given) |

---

## Core Formula

```
Little's Law applied to test plan sizing:
  L = λ × W

  L = number of concurrent users (= Threads in JMeter)
  λ = arrival rate (users/second)
  W = average session time (seconds)

Batch arrival:
  λ = N_total_users / Ramp_up_period
  L = (N_total_users / Ramp_up_period) × W

Cap rule:
  L ≤ N_total_users (cannot have more concurrent users than total users)

Inverse — solve for Ramp-up given target L and W:
  Ramp_up = N_total_users × W / L
```

---

## JMeter Thread Group — Mapping to Little's Law

| JMeter Field | Little's Law Mapping | Notes |
|---|---|---|
| Number of Threads | N_total_users (upper bound) | Total users across the test run |
| Ramp-up Period (s) | Arrival window T | One user added per T/N seconds on average |
| Loop Count | Controls single vs multi-pass sessions | Set to 1 for a single-pass session test |
| Constant Timer delay | Think time W component | Fixed dwell between actions in a session |
| Gaussian Random Timer deviation+offset | Think time W component | Realistic think time centred on deviation+offset ms |

---

## Timers

| Timer Type | Behaviour | Use Case |
|---|---|---|
| **Constant Timer** | Fixed millisecond delay | Scripted workflows with known fixed pauses |
| **Gaussian Random Timer** | Delay ~ Gaussian(mean = Deviation + Offset) | Realistic user think time that varies around an average |

---

## APDEX

| Score | Interpretation |
|---|---|
| 1.0 | All requests within toleration threshold T |
| 0.5–1.0 | Mixed — some requests in frustration zone |
| 0.0 | Every request exceeds toleration threshold |

Default JMeter thresholds: T = 500 ms, F = 1 500 ms. A deliberate `time.sleep(5)` in the Flask route → APDEX = 0.000 (expected — demonstrates a saturated system).

---

## Worked Examples

### Example 1 — Concurrent Users Capped by Total

100 users arrive within 5 s; W = 10 s.  
L = (100 / 5) × 10 = **200 → capped at 100.** JMeter: Threads = 100, Ramp-up = 5.

### Example 2 — Long Session with Think Time Gap

100 users arrive within 5 s; W = 150 + 50 + 300 = 500 s.  
L = (100 / 5) × 500 = **10 000 → capped at 100.** JMeter: Threads = 100, Ramp-up = 5.

### Example 3 — Arrival Rate Given, No Cap

λ = 20 users/s; W = 500 s; no total user count.  
L = 20 × 500 = **10 000.** JMeter: Threads = 10 000, Ramp-up = 500 s.

---

## Connections

- [[concepts/performance-metrics]] — Little's Law (L = λW); arrival rate; utilisation law
- [[concepts/performance-engineering]] — JMeter as load generation in the Measure phase
- [[sources/ict3113-pod-l5]] — Lec05: performance bounds and Erlang B (prerequisite)
- [[examples/ict3113-lab2-jmeter-testing]] — practical JMeter lab that precedes this lecture
- [[areas/performance-engineering]] — parent area
