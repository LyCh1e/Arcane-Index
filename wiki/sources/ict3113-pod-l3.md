---
type: source
title: "ICT3113 POD — L3: Workload Identification"
source: "raw/ICT3113 Performance Optimisation and Design - Lec03 Workload Identification.md"
domain: performance-engineering
tags: [ict3113, performance-engineering, workload, arrival-rate, capacity-planning, utilisation-law, peak-demand]
created: 2026-09-07
lecturer: "A/Prof Donny Soh"
---

# Source Index — ICT3113 POD: Lecture 3

**Module:** ICT3113 Performance Optimisation and Design  
**Lecturer:** A/Prof Donny Soh  
**Topic:** Workload Identification  
**Raw file:** `raw/ICT3113 Performance Optimisation and Design - Lec03 Workload Identification.md`

---

## Learning Outcomes

- Define a workload in terms of transaction types, arrival rates, and service demand per transaction
- Identify the business drivers behind a system's workload
- Estimate arrival rates from business quantities using order-of-magnitude decomposition
- Distinguish peak from average demand, and explain how peak demand influences capacity planning
- Apply workload estimates to the Utilisation Law to sanity-check a proposed design

---

## Motivation — Pont des Arts (Paris, June 2014)

A railing section collapsed under ~45 tonnes of "love locks" added one padlock at a time over years — no single lock mattered, but nobody was measuring cumulative load. Many capacity failures occur because the actual workload is different from the one the system was designed for.

---

## What Is a Workload?

Three components:

| Component | Definition | Example |
|-----------|-----------|---------|
| **Transaction types** | Categories of requests the system serves | Display refresh, gate tap, tax submission |
| **Arrival rates** | How many of each type arrive per unit time | 740 refreshes per minute |
| **Service demand** | How much work each transaction requires | 50 ms of controller time per refresh |

> "A workload statement reads like this: '740 displays across 185 stations, each refreshed once per minute, 50 ms of controller work per refresh.'"

What a workload is **not**: a benchmark score, a load-test setting, or a number invented after the system is built.

---

## Workload Drivers (Business Quantities)

Arrival rates are **business numbers in disguise**:

| System | Business driver | Resulting workload spike |
|--------|----------------|--------------------------|
| MRT display system | Station count, refresh frequency, ridership | Constant display updates; ridership peaks drive gate activity |
| Digital payments | Payday, billing cycles, major campaigns | End-of-month load looks nothing like mid-month |
| Tax filing | Filing deadline | Most annual submissions arrive in the final weeks |

> "The business calendar is the first performance document you should read."

---

## Estimation Methodology

Decompose from a number you can defend:

```
population → active fraction → actions per active user → time window → arrival rate
```

Principles:
- **Order-of-magnitude suffices early** — at design time, you are choosing between 1, 100, and 10,000 RPS; architecture choices, not server counts
- **State every assumption** — hidden assumptions cannot be challenged or corrected
- **Add headroom** for growth and estimation error (×2 to ×5 illustrative; actual factor depends on uncertainty, burstiness, redundancy, scaling delay, SLO)
- Refine as you approach capacity/SLO decisions where 100 vs 120 RPS can matter

---

## Worked Example: e-Filing Deadline

| Step | Calculation | Result |
|------|-------------|--------|
| 1. Population filing on deadline day | 2M taxpayers × 20% | 400,000 filings |
| 2. Spread over 12-hour window | 400,000 / 12 | ≈ 33,000 filings/hr ≈ 9.3/s average |
| 3. Evening peak (3× window average) | 9.3 × 3 | ≈ 28 filings/s |
| 4. Web requests per filing session | 28 × 30 requests/session | ≈ 830 requests/s at web tier |
| 5. Utilisation Law sanity check | 830 × 0.02 s = 16.6 units busy | At 70% target utilisation: ≈ 24 servers |

Each number is an explicit, challengeable assumption.

---

## Peak vs Average

| Concept | Meaning |
|---------|---------|
| **Design for peak, not average** | A system sized for 100 RPS average fails exactly when peak (1,000 RPS) arrives — when users are watching |
| **Predictable peaks** | Payday, lunchtime, deadlines, launches; often visible on the business calendar in advance |
| **Peak-within-peak** | When results release at 12:00 sharp, an hour's load does not spread across the hour — it lands in the first minute |

---

## Case Study: Taylor Swift Eras Tour (July 2023)

~330,000 seats at the National Stadium, Singapore; demand estimated in the millions.

- The real workload was not "sell 330,000 tickets" — it was "absorb millions of arrivals in the opening minutes, hold them in a fair queue, and keep the queue itself responsive"
- **During an extreme peak, the queueing system is the product** — if the queue page falls over, the checkout speed is irrelevant
- Workload identification changed the architecture: a virtual waiting room is a design response to an arrival-rate estimate

---

## Workload Mix

Total volume can remain constant while the workload changes entirely:

- A checkout costs many times more than a page view (database writes, inventory checks, payment gateway round trip)
- A campaign that doubles checkouts without changing total traffic has changed the workload
- **When stating a workload, state the mix, not just the total volume**

---

## Workload and Architecture (MRT Example)

185 stations; 4 displays per station; each display refreshes once per minute; 50 ms service demand per update.

**Single central controller:**
- Controller serves all 185 × 4 = 740 display updates per minute directly
- Utilisation: `740 × (50ms/60,000ms) = 0.617` (62%)

**Sub-controllers at each station:**
- Each station controller serves 4 displays/minute → U = `4 × (50ms/60,000ms) ≈ 0.33%` per station
- Central controller only sends one update per station per minute → 185 updates/minute
- Central controller U = `185 × (50ms/60,000ms) ≈ 15%`
- Sub-controller architecture distributes load and dramatically reduces central-controller utilisation

Workload identification drives the architectural choice.

---

## Three Exercises

### Manufacturing
- 120,000 units/month; 20 days × 1 shift × 8 hr; bottleneck: 4 s/unit
- Average rate = 120,000 / (160 h) = 750 units/hr ≈ 208 units/shift-hour
- U = 750 × (4/3600) ≈ 83%
- Final week: 40% of 120,000 = 48,000 units in 5 days × 8 hr = 40 hr → 1,200 units/hr
- U at 1,200 units/hr = 1,200 × (4/3600) = 133% → single shift **cannot cope**; overtime or second shift required

### Healthcare (Polyclinic)
- 60 appointment slots/hr; 70% booked → 42 booked patients; 25 walk-ins/hr
- Total arrivals: 42 + 25 = **67 patients/hr**
- Registration: 45 s/patient → service rate μ = 3600/45 = 80 patients/hr
- U = 67/80 = **83.8%** — busy but coping
- With flu-vaccination drive (+15 walk-ins): 82 patients/hr; U = 82/80 = **102.5%** — counter **overloaded**; one counter no longer sufficient

### IT Flash Sale (e-Commerce)
- 500,000 users notified; 4% open in first minute → **20,000 arrivals in 60 s ≈ 333 arrivals/s**
- 6 requests/user at 10 ms each → **333 × 6 = 2,000 requests/s at product service**
- Servers at 70% U: each server handles 1/(0.01) = 100 req/s at 100%; at 70% → 70 req/s/server
- Servers needed: ⌈2,000 / 70⌉ = **29 servers**
- Peak-to-average ratio: 2,000 / 40 = **50×** → implies auto-scaling, pre-warming, or over-provisioning strategy

---

## The Design Chain

```
business driver → arrival rate × service demand → utilisation → capacity decision
```

> "Estimate at design time; measure in production. When they disagree, the measurement wins and the estimate gets corrected."
>
> "An estimate wrong by 10× caught at design time costs a meeting. The same error caught in production is the Pont des Arts railing."

---

---

## Transcript Additions (Live Lecture)

*Source: `raw/ICT3113 Performance Optimisation and Design - Lec03_transcript.md`*

The live lecture opened by revisiting a Lec02 item before proceeding to Lec03 content. Key additions not in the slides:

### Revisit: Observation Boundary Effect (fully worked)

Previous worked example (Lec02): 4 packets arrive over [0, 10] s.

| Packet arrivals | Gaps between arrivals |
|---|---|
| t = 0, 1, 3, 5 | Gap 1 = 1 s; Gap 2 = 2 s; Gap 3 = 2 s |

- Mean observed gap = (1 + 2 + 2) / 3 = **1.67 s**
- λ = 4/10 = 0.4 → 1/λ = **2.5 s**
- **1.67 ≠ 2.5** — they diverge because the observed gaps only cover until the last arrival (t = 5), not the full observation window (t = 10).
- "Over a very long run, the two will converge."

### New Worked Example: API Server (20-second window)

Single-server system. Four requests arrive at t = 0, 2, 9, 12 (over a 20-second observation window).

| Request | Arrives | Starts | Ends | W | S | R |
|---------|---------|--------|------|---|---|---|
| A | 0 | 0 | 3 | 0 | 3 | 3 |
| B | 2 | 3 | 8 | 1 | 5 | 6 |
| C | 9 | 9 | 13 | 0 | 4 | 4 |
| D | 12 | 13 | 15 | 1 | 2 | 3 |

| Metric | Calculation | Value |
|--------|-------------|-------|
| λ | 4 / 20 s | **0.2 jobs/s** |
| Mean observed gap | (2 + 7 + 3) / 3 | **4 s** |
| 1/λ | 1 / 0.2 | **5 s** ← not equal to mean gap |
| Mean S | 14 / 4 | **3.5 s** |
| μ | 1 / 3.5 | **2/7 jobs/s** |
| U | 14 / 20 | **70%** |

The gap mean (4 s) and 1/λ (5 s) differ because the gaps only span t = 0 to t = 12, not the full 20-second window.

### Utilisation Law — Pie-Eating Analogy

Intuitive first-principles derivation:

> "Let's say you are given 60 minutes in a pie-eating contest. You eat 5 pies, each taking 10 minutes."

- Busy time = 5 × 10 = 50 min → U = 50/60 ≈ **83%**
- X = 5 / 60 pies per minute
- U = X × S = (5/60) × 10 = 50/60 ✓

Dividing the total busy time equation `(jobs × service time)` by the observation interval yields U = X × S. The analogy makes the law immediately intuitive.

### Hawker Centre Analogy — λ vs X

> "If you go to buy noodle and there's no queue, you always get served — X = λ. But at a famous hawker centre, you queue for so long you decide to eat somewhere else — that's lost work, so X < λ."

### Healthcare Utilisation Law Exercises (MRI Scanner)

| Question | Given | Find | Working | Answer |
|----------|-------|------|---------|--------|
| 1 | 2 scans/hr, S = 25 min | U | Busy = 2 × 25 = 50 min; U = 50/60 | **≈ 83%** |
| 2 | U = 60%, λ = 12/hr | S | λ = 12/60 = 0.2/min; S = 0.6/0.2 | **3 min** |
| 3 | S = 6 min/patient | X_max | U = 1; X = 1/S = 60/6 | **10 patients/hr** |

Key insight from Q1: at 83% utilisation, a small demand increase will start forming a queue. Use this to sanity-check whether a department can meet demand before purchasing another machine.

### Interview Application: "Estimate the Number of Trains in China"

> "One of my first interview questions was to estimate the number of trains in China. I started with the number of provinces, then the number of train stations per province, then trains per station schedule, then trains required per schedule. My rough estimate was in the ballpark of the actual number."

This is exactly workload estimation: decompose from a defensible top-level quantity, work down through multiplicative factors, arrive at an order-of-magnitude answer. The skill is domain-independent.

### AI Age Context

> "AI can code; AI can do many things. But AI can't really understand, at least for now, business problems and translate them into good solutions for users. That is where our value still comes in."

Workload identification is one of the distinctly human-judgment activities — recognising what business quantity drives a technical metric is not an exercise in code generation.

---

## Linked Concepts

- [[concepts/workload-identification]] — full concept page: methodology, decomposition, peak vs average, mix, architecture influence, all worked examples
- [[concepts/performance-metrics]] — Utilisation Law (U = XS) used in every workload sanity check; arrival rate λ; throughput X; API server worked example; MRI scanner exercises
