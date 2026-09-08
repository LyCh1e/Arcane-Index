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

## Linked Concepts

- [[concepts/workload-identification]] — full concept page: methodology, decomposition, peak vs average, mix, architecture influence, all worked examples
- [[concepts/performance-metrics]] — Utilisation Law (U = XS) used in every workload sanity check; arrival rate λ; throughput X
