---
type: source
title: "ICT3113 POD — L5: JMeter Recap"
source_file: "raw/ICT3113 Performance Optimisation and Design - Lec05 JMeter Recap.md"
module: ICT3113 Performance Optimisation and Design
domain: performance-engineering
tags: [ict3113, performance-engineering, jmeter, load-testing, littles-law, test-plan-design, apdex, think-time, concurrent-users]
created: 2026-09-21
updated: 2026-09-21
lecturer: "Donny Soh"
---

# Source Index — ICT3113 POD: Lecture 5 — JMeter Recap

**Module:** ICT3113 Performance Optimisation and Design  
**Lecturer:** Donny Soh  
**Raw file:** [[raw/ICT3113 Performance Optimisation and Design - Lec05 JMeter Recap.md]]  
**Concept pages:** [[concepts/performance-engineering]] · [[concepts/performance-metrics]]

Recap lecture bridging Lec01–Lec04 theory to practice. The single learning outcome is: *write a proper JMeter test plan from a given number of concurrent users, average session time, and arrival rate.* The primary vehicle is Little's Law (L = λW) applied backwards — from a target concurrency level to JMeter Thread Group parameters.

---

## Section Coverage

| Section | Key Content |
|---------|-------------|
| Flask App to Profile | `/sort` endpoint with `flask_profiler.profile()` decorator; verify in browser before loading with JMeter |
| JMeter Thread Group | Number of Threads, Ramp-up Period, Loop Count, Same user on each iteration |
| HTTP Request Sampler | Protocol, Server/IP, Port, Method, Path, Parameters — wired to `127.0.0.1:5000/sort` |
| Non-GUI Mode | `jmeter -n -t lab03.jmx -l test-results.csv -e -o report`; command-line execution for real test runs |
| Constant Timer | Fixed think time (e.g. 3 000 ms) between consecutive HTTP requests within one thread |
| Gaussian Random Timer | Random think time: `mean = Deviation + Constant Delay Offset`; models realistic user pacing |
| Timer Timing Diagram | U1–U5 each fire T1→T2 staggered by ramp-up; sleep between T1 and T2 is the think time |
| Objective: Concurrent User Replication | Goal is to reproduce N simultaneous users; each user's session spans W seconds |
| Little's Law for Test Plans | L = λ × W → Threads = (N_users / Ramp_up) × avg_session_time; cap by total user count |
| 30 Users in 5 Seconds | Six-user-per-second batch; peak concurrent = 30 (all groups overlapping in centre) |
| Parameter Derivation | Given target L and known W, solve for ramp-up: T = N_users × W / L |
| APDEX | Application Performance Index: 0.000 when every request exceeds the 500 ms toleration threshold (e.g. 5-second artificial sleep) |
| Worked Example 1 | 100 users, 5 s window, 10 s session → L = 200 > 100 → cap at 100 concurrent |
| Worked Example 2 | 100 users, 5 s window, 500 s session (150+50+300) → L = 10 000 > 100 → cap at 100 concurrent |
| Worked Example 3 | 20 users/s arrival rate, 500 s session → L = 10 000; no cap (no total user count given) |

---

## Core Formula

**Little's Law applied to test plan sizing:**

```
L = λ × W

where:
  L = number of concurrent users (Threads in JMeter)
  λ = arrival rate (users/second)
  W = average session time (seconds)

For a batch arrival scenario:
  λ = N_total_users / Ramp_up_period_seconds
  L = (N_total_users / Ramp_up_period) × W

Rule: L is capped by N_total_users — you cannot have more concurrent users than you have users.

Inverse (solve for Ramp-up given target L and known W):
  Ramp_up = N_total_users × W / L
```

---

## JMeter Thread Group Parameters — Mapping to Little's Law

| JMeter Field | Little's Law Mapping | Notes |
|---|---|---|
| Number of Threads | N_total_users (upper bound) | Total users across the test run |
| Ramp-up Period (s) | Arrival window T | One user added per T/N seconds on average |
| Loop Count | Controls whether each user makes 1 or many requests | Set to 1 for a single-pass session test |
| Constant Timer delay | W per-request component | Fixed think time (dwell) between actions in a session |
| Gaussian Random Timer deviation+offset | W per-request component | Realistic think time centred on `deviation + offset` ms |

---

## Timers

| Timer Type | Behaviour | Use Case |
|---|---|---|
| **Constant Timer** | Delays execution by a fixed millisecond value | Scripted workflows with known fixed pauses |
| **Gaussian Random Timer** | Delay drawn from Gaussian distribution: mean = Deviation + Constant Delay Offset | Simulating realistic user think time that varies around an average |

Timers are placed *between* two HTTP Request samplers within the same Thread to model think time between page loads.

---

## APDEX

The **Application Performance Index** is a standardised 0–1 satisfaction score:

| Score | Interpretation |
|---|---|
| 1.0 | All requests within toleration threshold (T) |
| 0.5–1.0 | Mixed; some requests in frustration zone |
| 0.0 | Every request exceeds the toleration threshold |

Default JMeter thresholds: T = 500 ms (Tolerated), F = 1 500 ms (Frustrated).

A 5-second artificial `time.sleep(5)` in the Flask route → **APDEX = 0.000** (every request exceeds T by 10×) — this is intentional in the lab to demonstrate what a saturated system looks like in the report.

---

## Worked Examples

### Example 1 — Concurrent Users Capped by Total

- 100 users arrive within 5 seconds; average session time 10 seconds.
- L = (100 / 5) × 10 = **200 → capped at 100** (cannot exceed total user count).
- JMeter: Threads = 100, Ramp-up = 5, Loop = 1.

### Example 2 — Long Session with Think Time Gap

- 100 users arrive within 5 seconds.
- Session: 150 s (active browsing) + 50 s (delay) + 300 s (second page) = 500 s.
- L = (100 / 5) × 500 = **10 000 → capped at 100**.
- JMeter: Threads = 100, Ramp-up = 5, Loop = 1.

### Example 3 — Arrival Rate Given, No Cap

- Arrival rate: 20 users/second; session: 500 s.
- L = 20 × 500 = **10 000 concurrent users** (no cap — no total user count given).
- JMeter: Threads = 10 000, Ramp-up chosen to give λ = 20 users/s → Ramp-up = 500 s.

---

## Connections

- [[concepts/performance-metrics]] — Little's Law (L = λW); arrival rate; utilisation law
- [[concepts/performance-engineering]] — JMeter test plan design; load generation as the Measure phase
- [[concepts/workload-identification]] — arrival rate and session time come from workload characterisation (Lec03)
- [[concepts/queueing-theory]] — Little's Law is also the basis of the Interactive Response Time Law (R = N/X − Z)
- [[examples/ict3113-lab2-jmeter-testing]] — practical JMeter lab (Lab 2) that precedes this lecture
- [[sources/ict3113-pod-l4]] — Lec04: queueing theory and operational laws
- [[areas/performance-engineering]] — parent area
