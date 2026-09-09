---
type: concept
title: "Software Verification and Validation"
domain: software-verification-validation
complexity: high
status: established
created: 2026-08-31
updated: 2026-08-31
tags: [svv, verification, validation, software-quality, reliability-metrics, defect-density, v-and-v, ict3112]
---

# Software Verification and Validation

Software V&V is the discipline of confirming that software is built correctly and that the right software is being built. It operates across the entire software development lifecycle, combining static and dynamic techniques to detect and prevent defects.

---

## Core Definitions

| Term | Question Answered | Focus |
|------|-------------------|-------|
| **Verification** | "Are we building the product right?" | Conformance to specification |
| **Validation** | "Are we building the right product?" | Fulfilment of user needs and intended purpose |
| **V&V combined** | "Does the software meet its specifications and fulfil its intended purpose?" | Both |

---

## Static vs Dynamic V&V

| Dimension | Static V&V | Dynamic V&V |
|-----------|-----------|-------------|
| Code executed | No | Yes |
| Focus | **Prevention** of defects | **Detection** of defects |
| Methods | Reviews, inspections, walkthroughs, static analysis tools | Testing, simulation, model checking |
| Lifecycle phase | Requirements, design, code review (early) | After implementation |
| Cost to find defects | Lower (defects caught before they embed) | Higher (defects found after code is written) |

---

## The V-Model

```
Requirements  ───────────────────────────────  Acceptance Testing (Validation)
    System Design  ──────────────────────  System Testing (Verification)
        Architecture Design  ──────────  Integration Testing (Verification)
            Detailed Design  ──────────  Unit Testing (Verification)
                        Coding
```

Left side (specification) maps directly to right side (testing level). The horizontal arrows show which test level validates each specification artefact.

---

## Root Causes of Poor Software Quality — Six DORA Categories

| Category | Common Examples |
|----------|----------------|
| **1. People / Communication / Organisational Culture** | Siloed teams, blame culture, poor knowledge sharing |
| **2. Planning / Workload / Change Pressure** | Unrealistic deadlines, scope creep, corners cut under pressure |
| **3. Requirements / Architecture / Design** | Wrong or ambiguous requirements, poor architectural decisions |
| **4. Implementation / Maintainability** | Spaghetti code, no coding standards, uninitialised variables |
| **5. Configuration / Dependencies / Software Supply Chain** | Unmanaged dependencies, supply chain attacks, missing pinned versions |
| **6. Verification / Delivery / Operational Feedback** | Inadequate testing, no feedback loops, poor production monitoring |

---

## Famous Software Failures

| Incident | Year | Root Cause | Impact |
|---------|------|-----------|--------|
| **Therac-25** | 1980s | Race condition + missing hardware safety interlock; software override of fail-safes | 3 deaths from radiation overdose; paradigm case for safety-critical software V&V |
| **Ariane 5** | 1996 | 64-bit floating-point → 16-bit integer overflow; reuse of Ariane 4 code without revalidation | $500M rocket destroyed 37 seconds after launch |
| **CrowdStrike** | 2024 | Faulty kernel-level sensor update pushed to millions of Windows endpoints without sufficient validation | $5.4B economic impact; global outages across airlines, hospitals, banks |

---

## Cost of Poor Software Quality

| Year | Study | Cost |
|------|-------|------|
| 2002 | US NIST — Economic Impact of Inadequate Infrastructure for Software Testing | $59.5 billion/year |
| 2021 | CISQ estimate | $2.08 trillion/year |
| 2022 | CISQ report | $2.41 trillion/year |

**Key insight**: bug-fix cost rises sharply the later in the SDLC a defect is discovered. Defects caught in requirements phase cost ~10× less to fix than those found in production.

---

## Software Reliability Metrics

### Core Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| **MTTF** | (measured empirically) | Mean Time To Failure — average time between system start and first failure |
| **MTTR** | (measured empirically) | Mean Time To Repair — average time to restore the system after a failure |
| **MTBF** | MTTF + MTTR | Mean Time Between Failures — average time from one failure to the next |
| **Availability** | MTTF / MTBF = MTTF / (MTTF + MTTR) | Proportion of time the system is operational |
| **Failure intensity** | λ(τ) | Number of failures per time unit at time τ |

**Example**: if MTTF = 9 hours and MTTR = 1 hour, then MTBF = 10 hours, Availability = 0.9 (90%).

---

## Software Reliability Growth Models

Reliability growth models describe how failure intensity decreases as faults are found and fixed during testing.

### Foundational Assumption — Perfect Debugging

All Musa reliability models assume **perfect debugging**: each time a fault is found and corrected, failure intensity decreases by a fixed amount. In practice, bug fixes can introduce new bugs, but the models treat this as an idealisation. Formally: *correcting a fault responsible for an observed failure reduces expected failure intensity.*

### Execution Time vs Calendar Time

When τ appears in any reliability formula, "time" must be defined precisely:

| Type | Also called | Definition | Differs from the other when… |
|------|------------|-----------|------------------------------|
| **Execution time** | CPU time | Cumulative processor time consumed while executing software | Multi-threaded: many CPU-seconds fit into fewer wall-clock seconds |
| **Calendar time** | Wall-clock time, elapsed time | Real-world time elapsed from test start to end | I/O-bound: CPU sits idle; wall time > CPU time |

Always specify the environment and hardware when reporting time-based reliability metrics. For examination calculations, treat time as a single value unless the question states otherwise.

### Basic Reliability Model (Musa)

Assumes a constant rate of decrease in failure intensity — each fault fixed reduces the failure rate by the same amount.

```
μ(τ) = v₀ × [1 − exp(−λ₀τ / v₀)]
λ(τ) = λ₀ × [1 − μ(τ) / v₀]
```

| Symbol | Meaning |
|--------|---------|
| μ(τ) | Expected total failures by time τ |
| λ(τ) | Failure intensity at time τ |
| v₀ | Total expected failures (initial fault count) |
| λ₀ | Initial failure intensity |

**Suited for**: stable or mature releases where faults are evenly distributed across the codebase. Each fix contributes an equal, constant reduction in failure intensity — a reasonable approximation when no single code path dominates usage.

### Logarithmic Reliability Model (Musa / Okamoto)

Assumes frequently-triggered faults are found and fixed first — diminishing returns as testing continues.

```
μ(τ) = (1/θ) × ln(λ₀θτ + 1)
λ(τ) = λ₀ × exp(−θ × μ(τ))
```

| Symbol | Meaning |
|--------|---------|
| θ | Per-fault decrease in intensity (higher θ = more skewed fault distribution) |

**Suited for**: early stages of a system where fault exposure is uneven — a small number of heavily-used code paths accumulate most failures first. Fixing those high-traffic faults produces a large initial drop in failure intensity (the log curve drops steeply), followed by diminishing returns as progressively rarer paths are exercised.

**Example**: a system with 10 use cases where 2 are used 90% of the time. Bugs on those 2 paths surface and are fixed quickly, causing a rapid fall in λ. Remaining bugs in rarely-used paths contribute little to ongoing failure intensity.

**Key distinction**: the logarithmic model tends towards zero but never reaches it, making it arguably more realistic for systems that always have some residual fringe-case failures.

### Applied — ICT3112 Lab 2 (classroom forms)

[[examples/ict3112-lab2-reqnroll-bdd]] implements a subset of these as calculator methods, with the simplifications the lab states explicitly:

| Method | Classroom form used | Notes |
|--------|--------------------|-------|
| `Mtbf(operatingTime, failures)` | `operatingTime / failures` | both inputs must be positive; "an observed average, not a prediction" |
| `Availability(mtbf, mttr)` | `mtbf / (mtbf + mttr)` | uses the approximation **MTTF ≈ MTBF** (so it substitutes MTBF for MTTF in `MTTF/(MTTF+MTTR)`); inputs non-negative, denominator positive; returns 0–1 |
| Basic Musa `λ(τ)` | `λ₀ · exp(−λ₀τ / ν₀)` | equivalent to `λ₀ · [1 − μ(τ)/ν₀]`; starts at λ₀, decays to 0 |
| Basic Musa `μ(τ)` | `ν₀ · [1 − exp(−λ₀τ / ν₀)]` | starts at 0, rises to ν₀; domain `λ₀>0, ν₀>0, τ≥0`, τ in stated execution-time units (CPU hours) |

Worked check: `λ₀=2, ν₀=10, τ=5` → exponent `−1` → `λ = 2·e⁻¹ ≈ 0.7358`, `μ = 10·(1−e⁻¹) ≈ 6.3212`.

---

## Defect Density

```
Defect Density = Defects / KLOC
```

- **KLOC** = Kilo Lines of Code (1,000 LOC)
- **SSI** = Shipped Source Instructions — total delivered LOC across all modules
- **CSI** = Changed Source Instructions — new + modified LOC in a release

### Tracking KSSI Across Releases

```
KSSI(current) = KSSI(previous) + KCSI − deleted_lines − changed_lines
```

Used to normalise defect counts across releases of different sizes.

---

## Customer-Facing Quality Metrics

### PUM — Problems per User Month

```
PUM = Total Number of Problems / Total Number of User Months
```

**Total User Months** = number of users × number of months in the period. Measures reliability from the customer's operational perspective.

### Customer Satisfaction Frameworks

| Framework | Dimensions |
|-----------|-----------|
| **IBM CUPRIMDSO** | Capability, Usability, Performance, Reliability, Installability, Maintainability, Documentation, Service, Overall satisfaction |
| **HP FURPS** | Functionality, Usability, Reliability, Performance, Supportability |

---

## Assessment Context (ICT3112)

| Component | Weight |
|-----------|--------|
| Final Examination | 30% |
| iRAT + tRAT | 20% |
| Lab Assessments | 15% |
| Continuous Assessment | 35% |

---

## Related Concepts

- [[concepts/software-testing-fundamentals]] — testing overview, V-model, ISTQB principles, testing levels
- [[concepts/whitebox-testing-techniques]] — structure-based testing (CFG, coverage, complexity)
- [[concepts/blackbox-testing-techniques]] — specification-based testing (EP, BVA, decision tables, state transition)
- [[concepts/static-code-analysis]] — SAST tooling and analysis techniques
- [[concepts/test-design-techniques]] — test design methods overview
- [[concepts/test-driven-development]] — TDD/BDD; how these calculations were built test-first
- [[examples/ict3112-lab2-reqnroll-bdd]] — MTBF / Availability / Basic Musa implemented as calculator methods with BDD scenarios
