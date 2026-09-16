---
type: study-notes
title: "ICT3112 SVV — Quick Reference Sheet"
tags: [study-notes, ict3112, formula-sheet, exam-prep]
created: 2026-09-14
updated: 2026-09-14
---

# ICT3112 Software Verification and Validation
## Quick Reference Sheet

> For derivations, diagrams, and full worked examples see [[study notes/ICT3112 - Software Verification and Validation Exam Notes]].

---

## Core Definitions (Always Start Here)

| Term | Definition |
|------|-----------|
| **Verification** | Building the product **right** — conformance to spec |
| **Validation** | Building the **right** product — fulfils user need |
| **Static V&V** | No code execution; prevention; reviews, SAST |
| **Dynamic V&V** | Code executed; detection; testing, simulation |
| **Error** | Human mistake |
| **Defect/Bug** | Flaw in code/design resulting from error |
| **Failure** | Visible deviation from expected behaviour when defect executes |

---

## Reliability Metrics

| Formula | Name |
|---------|------|
| MTBF = MTTF + MTTR | Mean Time Between Failures |
| Availability = MTTF / (MTTF + MTTR) | Proportion of uptime |
| Defect Density = Defects / KLOC | Defect rate per 1,000 LOC |
| PUM = Total Problems / Total User Months | Field problems per user-month |

---

## Basic Musa Model (Exponential)

$$\lambda(\tau) = \lambda_0 \times e^{-\lambda_0 \tau / \nu_0}$$

$$\mu(\tau) = \nu_0 \times \left[1 - e^{-\lambda_0 \tau / \nu_0}\right]$$

| Symbol | Meaning |
|--------|---------|
| λ(τ) | Failure intensity at time τ |
| μ(τ) | Expected total failures by τ |
| ν₀ | Total expected failures (fault count) |
| λ₀ | Initial failure intensity |

---

## Logarithmic Musa Model

$$\mu(\tau) = \frac{1}{\theta}\ln(\lambda_0\theta\tau + 1)$$

$$\lambda(\tau) = \lambda_0 \times e^{-\theta\mu(\tau)}$$

**Use when:** high-traffic bugs surface first; diminishing returns as testing continues.

---

## Cyclomatic Complexity (Whitebox)

$$\boxed{C = E - N + 2}$$

- **C** = complexity = minimum number of basis paths
- **E** = edges in CFG
- **N** = nodes in CFG

| C | Risk |
|---|------|
| 1–4 | Simple |
| 5–10 | Marginal |
| 11–20 | Moderate |
| 21–50 | **High** |
| > 50 | **Untestable** |

---

## Decision Table — Test Case Count

$$\text{Max rules} = 2^n \quad (n = \text{binary conditions})$$

- Collapse impossible/irrelevant combinations to reduce below 2ⁿ
- **One test case per column (rule)** in the final table

---

## State Transition — Coverage Count

| Level | Requirement | Total (Door Lock Example) |
|-------|------------|--------------------------|
| **0-switch** | 1 TC per unique transition | **6 TCs** |
| **1-switch** | 1 TC per consecutive pair (excl. self-loops) | **10 TCs** |

---

## Coverage Hierarchy

```
Path Coverage (impractical)
  ↑
Multiple Condition Coverage (2ⁿ per group)
  ↑
Decision & Condition Coverage
  ↑             ↑
Condition   Decision/Branch  ← subsumes Statement
  ⚠️ Condition does NOT subsume Decision!
  ↑
Statement Coverage (weakest)
```

---

## CFG — Factorial Reference

**Nodes:** 11 &nbsp; | &nbsp; **Edges:** 12 &nbsp; | &nbsp; **C = 3**

| Path | Sequence | Input |
|------|---------|-------|
| P1 | 1→2→3→4→11 | num < 0 |
| P2 | 1→2→3→6→10→11 | num = 0 |
| P3 | 1→2→3→6→7→8→9→6→10→11 | num > 0 |

---

## ISTQB Principles (7)

| # | Principle |
|---|-----------|
| 1 | Testing shows **presence** of defects |
| 2 | **Exhaustive** testing is impossible |
| 3 | **Early** testing saves cost |
| 4 | **Defect clustering** (Pareto: 20% of code, 80% of defects) |
| 5 | **Pesticide paradox** — refresh test suites |
| 6 | Testing is **context-dependent** |
| 7 | **Absence-of-errors** fallacy |

---

## Blackbox Techniques — When to Use

| Technique | Use When |
|-----------|---------|
| **Use Case Testing** | Testing end-to-end user journeys |
| **Equivalence Partitioning** | Large input domain; want minimum TCs |
| **Boundary Value Analysis** | Numeric/range inputs; defects at edges |
| **Decision Table** | Multi-condition logic; combinations matter |
| **State Transition** | FSMs, sessions, UI flows with state |

---

## BVA — Values to Test (Range Inputs)

For a valid range **[L, H]**:

| Value | Type |
|-------|------|
| L − 1 | Invalid lower boundary |
| **L** | Valid lower boundary |
| L + 1 | Extended BVA |
| H − 1 | Extended BVA |
| **H** | Valid upper boundary |
| H + 1 | Invalid upper boundary |

> For strings: keep ASCII boundary and length boundary in **separate test cases**.

---

## Static Review Formality Spectrum

Informal Review → Walkthrough (author-led) → Technical Review (moderator) → **Inspection / Fagan (highest — most cost-effective)**

---

## Famous Failures — Summary

| Failure | Root Cause | Impact |
|---------|-----------|--------|
| Therac-25 | Race condition; HW safety interlock bypassed by SW | 3 deaths |
| Ariane 5 (1996) | 64→16-bit overflow; Ariane 4 code not revalidated | $500M |
| CrowdStrike (2024) | Faulty kernel update with insufficient validation | $5.4B |

---

## DORA Root-Cause Categories (6)

1. People / Communication / Culture
2. Planning / Workload / Change Pressure
3. Requirements / Architecture / Design
4. Implementation / Maintainability
5. Configuration / Dependencies / Supply Chain
6. Verification / Delivery / Operational Feedback

---

## V-Model Alignment

| Left (Spec) | Right (Test) |
|-------------|-------------|
| Requirements | Acceptance Testing |
| System Design | System Testing |
| Architecture Design | Integration Testing |
| Detailed Design | Unit Testing |
| *Coding* | *(centre)* |
