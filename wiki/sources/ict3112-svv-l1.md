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

## Linked Concepts

- [[concepts/software-verification-and-validation]] — comprehensive V&V reference
- [[concepts/software-testing-fundamentals]] — testing overview and levels
- [[concepts/static-code-analysis]] — static analysis tooling
