---
type: concept
title: "Workload Identification"
aliases: ["workload estimation", "capacity planning", "arrival rate estimation", "peak demand", "workload mix", "workload decomposition"]
tags: [performance-engineering, workload, arrival-rate, capacity-planning, peak-demand, utilisation-law, ict3113]
created: 2026-09-07
updated: 2026-09-07
status: established
domain: performance-engineering
complexity: high
---

# Workload Identification

Workload identification is the practice of precisely characterising the demand placed on a system — what requests it receives, how many arrive per unit time, and how much work each one requires. It is the necessary first step before any capacity estimate, architecture comparison, or utilisation calculation can be made.

> **One-line definition:** Workload identification answers the question "what is this system actually being asked to do?" — in quantitative, challengeable terms — before the system is built.

---

## What Is a Workload?

A workload has three components:

| Component | Definition | Example |
|-----------|-----------|---------|
| **Transaction types** | The distinct categories of requests the system serves | Display refresh, API call, database write, queue pop |
| **Arrival rates (λ)** | How many of each type arrive per unit time | 740 refreshes per minute, 28 filings per second |
| **Service demand (S)** | How much resource each transaction requires to complete | 50 ms of CPU per refresh, 20 ms per HTTP request |

A complete workload statement covers all three:

> "740 displays across 185 stations, each refreshed once per minute, 50 ms of controller work per refresh."

**What a workload is not:** a benchmark score, a load-test setting, or a number chosen after the system is built. Those are descriptions of a system's behaviour under assumed load — they do not tell you whether the assumption matches reality.

---

## Motivation: The Pont des Arts Problem

In June 2014, a section of railing on the Pont des Arts (Paris) collapsed under ~45 tonnes of "love locks" added one padlock at a time over years. No single lock was the problem; the cumulative, unmeasured load exceeded what the structure was designed for.

Many capacity failures share this structure: the actual workload is different from the workload the system was designed for — specifically, the workload nobody identified.

---

## Workload Drivers

Arrival rates are **business numbers in disguise**. The first step is always to identify the business quantity that drives each transaction type:

| System | Business driver | Workload implication |
|--------|----------------|---------------------|
| MRT display system | Station count × displays × refresh frequency | 185 stations × 4 displays × 1/min = 740 display updates/min |
| Digital payments | Payday, billing cycles, campaign launches | End-of-month traffic looks nothing like mid-month |
| Tax filing system | Filing deadline | Most annual filings arrive in the final days |
| E-commerce flash sale | Push notification open rate × actions per user | Millions of arrivals in the opening minute |

> "The business calendar is the first performance document you should read."

The business calendar is a performance signal: deadlines, paydays, lunch peaks, and campaign launches are predictable. They should be in the workload model before a line of code is written.

---

## Estimation Methodology

Decompose from a quantity you can defend through this chain:

```
population → active fraction → actions per active user → time window → arrival rate
```

### Principles

**1. Order-of-magnitude estimates suffice at design time.**

Early in design, you are choosing between 1, 100, and 10,000 requests per second — not between 100 and 120. An estimate good to within a factor of 2–5 eliminates infeasible architectures. Refine as you approach SLO and capacity decisions where smaller differences matter.

**2. State every assumption explicitly.**

An estimate with hidden assumptions cannot be challenged, corrected, or improved. Every number in the decomposition chain should be visible and labelled as an assumption.

**3. Add headroom for growth and estimation error.**

Illustrative headroom: ×2 to ×5. The appropriate factor depends on:
- **Uncertainty** in the estimate
- **Burstiness** of arrivals (peak-to-average ratio)
- **Redundancy** strategy (N+1, N+2, active-active)
- **Scaling delay** (how fast can new capacity be provisioned?)
- **SLO** (how much degradation is acceptable before a breach?)

**4. Estimate at design time; measure in production.**

When measurement and estimate disagree, the measurement wins and the estimate is corrected. An estimate wrong by 10× caught at design time costs a meeting. The same error caught in production can be catastrophic.

---

## Worked Example: e-Filing Deadline

Decomposition from business numbers to server count:

| Step | Assumption | Result |
|------|------------|--------|
| Total filers | 2 million taxpayers file online | 2,000,000 |
| Deadline-day fraction | 20% file on the final day | 400,000 filings |
| Window | Spread over 12 hours | 33,333/hr ≈ **9.3 filings/s** average |
| Evening peak | 3× window average | **≈ 28 filings/s** peak |
| Request multiplier | 30 web requests per filing session | **≈ 830 requests/s** at web tier |
| Utilisation Law check | 830 req/s × 20 ms/req = 16.6 server-seconds/second | 16.6 units of continuously busy capacity |
| Server count (at 70% U target) | 16.6 / 0.70 | **≈ 24 servers** |

Every number above is an explicit assumption — each one can be independently challenged and refined. This is the purpose of making them visible.

---

## Peak vs Average Demand

> "A system averaging 100 requests per second with peaks of 1,000, sized for the average, is down precisely when the most users are watching."

| Concept | Meaning |
|---------|---------|
| **Design for peak** | Capacity must handle the worst credible sustained load within the SLO, not the long-run average |
| **Predictable peaks** | Payday, lunchtime, deadlines, product launches — often visible on the business calendar in advance |
| **Peak-within-peak** | When an event triggers a simultaneous rush (results released at 12:00 sharp), an hour's load does not spread across the hour; it lands in the first minute |

### Taylor Swift Eras Tour — A Case Study in Extreme Peaks

July 2023: approximately 330,000 seats at the Singapore National Stadium went on sale. Demand was estimated in the millions.

The real workload was not "sell 330,000 tickets." It was: **"absorb millions of arrivals in the opening minutes, hold them in a fair queue, and keep the queue itself responsive."**

During an extreme peak, the queueing system is the product. If the queue page fails, the checkout speed is irrelevant.

**Architectural implication:** workload identification drove a design decision — a virtual waiting room was not an optimisation added later; it was a structural response to the arrival-rate estimate.

---

## Workload Mix

Total request volume is not the same as total work. The proportions of transaction types — the **workload mix** — determine the resource demand:

- A checkout involves database writes, inventory reads, payment gateway round trips
- A page view reads cached HTML
- A campaign that doubles the checkout fraction without changing total traffic has fundamentally changed the workload

**When stating a workload, always state the mix alongside the volume.** A server handling 1,000 read requests per second is in a completely different situation from one handling 1,000 write requests per second, even though the arrival rate is identical.

Common mix dimensions:
- Read vs write
- Interactive vs batch
- Foreground (user-facing) vs background (scheduled jobs, analytics)
- Normal entries vs end-of-period reports (e.g. monthly billing run)

---

## Workload and Architecture

Workload estimates do not just size hardware — they determine architecture. The MRT display system illustrates this directly.

**Single central controller architecture:**

```
Controller → [185 × 4 = 740 displays] directly
```

- Central controller: 740 updates/min, 50 ms each
- U = 740 × (50 / 60,000) = **61.7%** — at this load alone, with no headroom

**Sub-controller architecture (one controller per station):**

```
Central controller → 185 station controllers → 4 displays each
```

- Each station controller: 4 updates/min
  - U = 4 × (50 / 60,000) ≈ **0.33%** per station controller
- Central controller: 185 updates/min (one per station)
  - U = 185 × (50 / 60,000) ≈ **15.4%**

The sub-controller architecture distributes load, reduces central-controller utilisation from ~62% to ~15%, and provides headroom for growth. The workload calculation is what makes this comparison possible before either system is built.

---

## Worked Examples (Exam Reference)

### Manufacturing

**Given:** 120,000 units/month; 20 working days; 1 shift/day × 8 hr; bottleneck: 4 s/unit.

| Question | Working | Answer |
|----------|---------|--------|
| Average production rate? | 120,000 / (20 × 8) = 120,000 / 160 | **750 units/hr** |
| Bottleneck utilisation? | 750 × (4/3600) | **≈ 83%** |
| Final-week rate? (40% of volume, 5 days) | 48,000 / (5 × 8) | **1,200 units/hr** |
| Can one shift cope at 1,200/hr? | 1,200 × (4/3600) = 1.33 | **No — U = 133%; overloaded** |

### Healthcare (Polyclinic)

**Given:** 60 appointment slots/hr; 70% booked; 25 walk-ins/hr; registration = 45 s/patient; single counter.

| Question | Working | Answer |
|----------|---------|--------|
| Total arrivals 8–10 am? | (60 × 0.70) + 25 = 42 + 25 | **67 patients/hr** |
| Counter utilisation? | μ = 3600/45 = 80/hr; U = 67/80 | **83.8%** — coping |
| With flu drive (+15 walk-ins)? | 82/80 | **102.5% — overloaded; one counter insufficient** |

### IT Flash Sale (E-Commerce)

**Given:** 500,000 notified users; 4% open in first minute; 6 requests/user at 10 ms each; normal traffic = 40 req/s.

| Question | Working | Answer |
|----------|---------|--------|
| User arrivals in first minute? | 500,000 × 4% = 20,000 users / 60 s | **≈ 333 arrivals/s** |
| Request rate at product service? | 333 × 6 | **2,000 req/s** |
| Servers needed (≤70% U)? | Each server: 1/0.01 s = 100 req/s max; at 70% → 70 req/s; ⌈2,000/70⌉ | **29 servers** |
| Peak-to-average ratio? | 2,000 / 40 | **50×** — implies auto-scaling or significant pre-warming |

---

## The Design Chain

Every workload identification exercise follows the same sequence:

```
business driver
    → arrival rate × service demand
        → utilisation (Utilisation Law: U = λS)
            → capacity decision
```

This chain connects business intent to engineering specification. Without it, capacity decisions are guesses. With it, each assumption is traceable and correctable.

---

## Interview and Career Relevance

Workload estimation is a classic systems design interview skill. The same decomposition chain — start from a defensible top-level quantity and work downward multiplicatively — applies to estimation questions such as:

> "How many trains are there in China?"

A/Prof Donny Soh answered this in a real interview by decomposing: number of provinces → train stations per province → train schedules per station → trains required per schedule. His rough estimate landed in the ballpark of the actual number.

This is structurally identical to: taxpayers → filing fraction → filings per hour → requests per second → servers.

**Why this is a human skill in the AI age**: AI can generate code and optimise algorithms, but translating a business problem into a defensible quantitative model — understanding which business calendar events drive which technical metrics, what assumptions to make, what headroom to add — requires judgment that bridges domain knowledge and systems thinking. This is where engineers continue to add irreplaceable value.

---

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Sizing for average, not peak | System fails exactly when users need it most |
| Ignoring workload mix | A read-heavy model undersizes writes and vice versa |
| Hidden assumptions in estimates | Errors cannot be found or corrected |
| No headroom | First growth spike breaches the SLO |
| Confusing arrival rate (λ) with throughput (X) | In a stable system these are equal; at overload, X is capped at μ while λ exceeds it — the system queues or drops |

---

## Key Connections

- [[concepts/performance-metrics]] — Utilisation Law `U = XS`; arrival rate λ vs throughput X; all three metric classes (outcome, demand, supply)
- [[concepts/performance-engineering]] — the Measure → Model → Optimise → Deploy loop; workload identification is Step 0 (before even measuring)
- [[sources/ict3113-pod-l3]] — lecture source with all worked examples and case studies
- [[sources/ict3113-pod-l2]] — foundational metrics and operational laws
