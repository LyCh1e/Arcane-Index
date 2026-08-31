---
type: source
title: "ICT3112 SVV — Lecture 5.2: Whitebox Testing — Control Flow Code Coverage"
source_file: "raw/ICT3112 Software Verification and Validation - L5_2_Whitebox_Testing_Code_Coverage.md"
domain: software-verification-validation
tags: [ict3112, svv, whitebox-testing, code-coverage, statement-coverage, branch-coverage, condition-coverage, path-coverage]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 5.2: Whitebox Testing — Code Coverage

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Coverage Hierarchy

From weakest to strongest (each level generally subsumes levels below it):

```
Path Coverage
    └── Multi-Condition Coverage
            └── Decision & Condition Coverage
                    └── Condition Coverage
                            └── Decision Coverage
                                    └── Statement Coverage
```

**Important caveat**: Condition coverage is *not necessarily* a superset of decision coverage — see the `if (X and Y)` example below.

---

## 1. Statement Coverage

**Definition**: every executable statement is exercised at least once.

```
Coverage (%) = (num statements executed / num statements executable) × 100
```

**Factorial example**: to achieve 100% statement coverage, only 2 paths are needed:
- TC#1: `num > 0` (covers nodes 1,2,3,5,6,7,8,9,10,11)
- TC#2: `num < 0` (covers nodes 1,2,3,4,11)

The `num = 0` case (loop skipped) is not required but could reveal defects.

---

## 2. Decision (Branch) Coverage

**Definition**: every decision/branch that has a True or False outcome is evaluated at least once. Statement coverage is guaranteed.

```
Coverage (%) = (num decision outcomes executed / num decision outcomes possible) × 100
```

**Example**: 2 decisions in factorial code — `if (num < 0)` and `while (i <= num)`:
- Path 1: `num < 0` → tests if-true and while-false
- Path 2: `num > 0` → tests if-false and while-true

The `num = 0` case is *not* required because the while's false outcome is already exercised implicitly through Path 2 (when `i > num` terminates the loop).

**Note**: Every decision with a True and False outcome must be evaluated; cases with multiple exits need test cases for each exit.

---

## 3. Condition Coverage

**Definition**: each individual condition (sub-expression within a compound decision) is exercised for both True and False at least once.

```
Coverage (%) = (num conditions executed for both true and false / num possible conditions) × 100
```

**Example condition**: `if (clouds < 5 && daytime == true)`
- Must test: `clouds < 5` → True and False
- Must test: `daytime == true` → True and False
- Each condition is tested independently

**Critical gap**: Condition coverage is **not** necessarily a superset of decision coverage.

```
if (X and Y)
    print("tested");
```

| Test | X | Y | Condition covered | Branch covered |
|------|---|---|-------------------|----------------|
| TC1 | T | F | Both X and Y tested | Only False branch |
| TC2 | F | T | Both X and Y tested | Only False branch |

Result: full condition coverage achieved, but True branch (`X=T, Y=T`) is never executed!

---

## 4. Decision & Condition Coverage

**Definition**: every condition AND every decision are both exercised — combines the two criteria to close the gap above.

---

## 5. Multiple Condition Coverage

**Definition**: all possible combinations of True and False within multi-conditional expressions are exercised.

```
Subsumes: statement coverage, condition coverage, decision coverage, and decision & condition coverage.
```

**Example**: `if (cloudy == F && daytime == T && shade == F)` → 2³ = 8 test cases required:

| TC | cloudy | daytime | shade |
|----|--------|---------|-------|
| 1 | T | T | T |
| 2 | F | F | F |
| 3 | T | F | F |
| 4 | T | T | F |
| 5 | F | T | F |
| 6 | F | F | T |
| 7 | F | T | T |
| 8 | T | F | T |

Decision coverage only needs 2 cases; condition coverage only needs 2 cases; MCC needs all 8.

---

## 6. Path Coverage

**Definition**: all possible control paths are exercised, including loops (at zero, minimum, typical, and maximum iterations).

### Loop Coverage Strategy

Exhaustive path testing is impractical for loops. Limit loop execution to:

| Iteration | Description |
|-----------|------------|
| **Zero** | Loop body never executes (`i > num` immediately) |
| **One** | Loop executes exactly once |
| **Typical** | Normal number of iterations (e.g., 10) |
| **Max** | Maximum feasible iterations (or a very large int) |

**Factorial example with loop coverage**:
- Zero: `num = 0`, `i > num`, zero executions
- Min: `num = i = 1`, loop executes once
- Typical: `num = i + 10`, 10 executions
- Max: assign `num` the maximum practical integer

---

## Linked Concepts

- [[concepts/whitebox-testing-techniques]] — full whitebox reference: all coverage criteria, cyclomatic complexity, LCSAJ
- [[sources/ict3112-svv-l5-1]] — CFG and paths (factorial example CFG)
- [[sources/ict3112-svv-l5-3]] — cyclomatic complexity and LCSAJ
