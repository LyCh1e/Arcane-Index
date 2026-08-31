---
type: source
title: "ICT3112 SVV — Lecture 1: Software Verification and Validation Introduction"
source_file: "raw/ICT3112 Software Verification and Validation - L1_Software_VV_Intro.md"
domain: software-verification-validation
tags: [ict3112, svv, verification, validation, reliability-metrics, defect-density, software-quality]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 1: Software V&V Introduction

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Core Definitions

**Software Verification**: "Are we building the product right?" — checking that the software conforms to its specification.

**Software Validation**: "Are we building the right product?" — checking that the software fulfils its intended purpose and meets user needs.

**V&V combined**: "Checking software meets specifications and fulfils its intended purpose."

---

## Static vs Dynamic V&V

| Dimension | Static V&V | Dynamic V&V |
|-----------|-----------|-------------|
| Code execution | No | Yes |
| Focus | Prevention of defects | Detection of defects |
| Methods | Reviews, inspections, walkthroughs, static analysis | Testing, simulation, model checking |
| When | Early phases (requirements, design, code review) | After implementation |

---

## Six Root Cause Categories for Poor Software Quality (DORA-based)

| # | Category | Examples |
|---|----------|---------|
| 1 | People / Communication / Organisational Culture | Poor communication, siloed teams, blame culture |
| 2 | Planning / Workload / Change Pressure | Unrealistic deadlines, scope creep, cut corners |
| 3 | Requirements / Architecture / Design | Wrong or ambiguous requirements, poor design decisions |
| 4 | Implementation / Maintainability | Spaghetti code, no coding standards, uninitialised variables |
| 5 | Configuration / Dependencies / Software Supply Chain | Unmanaged dependencies, supply chain attacks |
| 6 | Verification / Delivery / Operational Feedback | Inadequate testing, no feedback loops, poor monitoring |

---

## Famous Software Failures

| Failure | Year | Cause | Impact |
|---------|------|-------|--------|
| **Therac-25** | 1980s | Race condition + software defect | 3 deaths from radiation overdose |
| **Ariane 5** | 1996 | 64-bit → 16-bit integer overflow | $500M rocket destroyed seconds after launch |
| **CrowdStrike** | 2024 | Faulty software update | $5.4B economic impact, global outages |

---

## Cost of Poor Software Quality

- **2002 (US NIST)**: $59.5 billion/year — testing infrastructure inadequacy
- **2021**: $2.08 trillion/year
- **CISQ 2022**: $2.41 trillion/year

Bug fix cost rises sharply the later in the SDLC a defect is found (early detection is orders of magnitude cheaper).

---

## Software Reliability Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| **MTTF** | — | Mean Time To Failure |
| **MTTR** | — | Mean Time To Repair |
| **MTBF** | MTTF + MTTR | Mean Time Between Failures |
| **Availability** | MTTF / MTBF | Proportion of time system is operational |
| **Failure intensity** | λ(τ) = failures/time unit | Rate of failure occurrences |

---

## Reliability Growth Models

### Basic Reliability Model (Musa)

Assumes faults are fixed as they are found; failure intensity decreases linearly over test time.

```
μ(τ) = v₀ × [1 − exp(−λ₀τ/v₀)]
λ(τ) = λ₀ × [1 − μ(τ)/v₀]
```

- μ(τ) = expected total failures in time τ  
- v₀ = total expected failures (initial fault count)  
- λ₀ = initial failure intensity  
- Constant rate of decrease in failure intensity  
- Suited for stable releases with even fault exposure

### Logarithmic Reliability Model (Musa/Okamoto)

Assumes faults encountered early (frequently triggered) are fixed first — diminishing returns.

```
μ(τ) = (1/θ) × ln(λ₀θτ + 1)
λ(τ) = λ₀ × exp(−θ × μ(τ))
```

- θ = per-fault decrease in intensity  
- Suited for systems where common code paths are tested first

---

## Defect Density Metrics

```
Defect Density = Defects / KLOC
```

- **KLOC** = Kilo Lines of Code
- **SSI** = Shipped Source Instructions — total delivered LOC
- **CSI** = Changed Source Instructions — new and modified LOC

```
KSSI(current) = KSSI(previous) + KCSI − deleted − changed
```

Used to track quality across software releases.

---

## Customer-Facing Quality Metrics

**PUM (Problems per User Month)**:
```
PUM = Total Number of Problems / Total Number of User Months
```

**Customer Satisfaction Frameworks**:
- **IBM CUPRIMDSO**: Capability, Usability, Performance, Reliability, Installability, Maintainability, Documentation, Service, Overall satisfaction
- **HP FURPS**: Functionality, Usability, Reliability, Performance, Supportability

---

## Assessment Structure

| Component | Weight |
|-----------|--------|
| Final Examination | 30% |
| iRAT + tRAT (in-class quizzes) | 20% |
| Lab Assessments | 15% |
| Continuous Assessment (CA) | 35% |

---

## Additional Insights from Live Lecture (Transcript)

### Goodhart's Law Applied to Testing

> "When a measure becomes a target, it ceases to be a good measure."
> — Goodhart's Law, paraphrased by Edwards Deming

**Testing application**: if the team is evaluated on the *number of passing tests*, developers will add redundant or trivial tests to inflate the count without increasing real coverage. The goal of testing is to *find defects*, not to produce passing tests. Passing tests are a measurement of that goal, not the goal itself.

Real example from the lecture: a student's capstone employer used "number of passing tests" as a quality KPI — this incentivised adding redundant tests rather than meaningful coverage.

---

### Execution Time vs Calendar Time

When calculating failure intensity (λ), "time" must be defined precisely:

| Type | Definition | When larger than the other |
|------|-----------|---------------------------|
| **Execution time** (CPU time) | Cumulative processor time consumed while executing software | Multi-threaded systems — many CPU-seconds compress into fewer wall-clock seconds |
| **Calendar time** (wall-clock time) | Elapsed real-world time from start to finish | I/O-bound systems — CPU sits idle; clock time > CPU time |

For ICT3112 assessments, assume "time is time" unless told otherwise. In practice, always specify the environment and hardware when reporting time-based reliability metrics to ensure reproducibility.

---

### Perfect Debugging Assumption

All Musa reliability growth models assume **perfect debugging**: every time a fault is identified and fixed, the failure intensity decreases. In reality, bug fixes can introduce new bugs — but the models treat this as an idealisation.

Formal statement: *correcting a fault responsible for an observed failure reduces the expected failure intensity by a fixed amount.*

---

### Informal vs Formal V&V (Module Structure)

| Half | Weeks | Approach | Techniques |
|------|-------|----------|-----------|
| **Informal V&V** (Ryan Kirwan) | 1–6 | Limited-coverage verification through testing | Software testing, reviews, static analysis |
| **Formal V&V** (David Sana) | 7–13 | Mathematical proof of system properties | Hoare logic, FRAMAC, model checking |

Informal ≠ unrigorous — it means the coverage is inherently partial (exhaustive testing is impossible). Formal methods can *prove* properties exhaustively but require mathematical specification of the system.

---

## Linked Concepts

- [[concepts/software-verification-and-validation]] — comprehensive V&V reference
- [[concepts/software-testing-fundamentals]] — testing overview and levels
- [[concepts/static-code-analysis]] — static analysis tooling
