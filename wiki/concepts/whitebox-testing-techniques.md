---
type: concept
title: "Whitebox Testing Techniques"
domain: software-verification-validation
complexity: high
status: established
created: 2026-08-31
updated: 2026-08-31
tags: [whitebox-testing, control-flow, data-flow, cfg, code-coverage, cyclomatic-complexity, lcsaj, basis-path, ict3112]
---

# Whitebox Testing Techniques

Whitebox testing derives test cases from the **internal structure** of the code. It is applied primarily at unit and integration testing levels and is the primary means of measuring structural coverage. Two broad categories exist: **control flow** (execution paths) and **data flow** (proper use of data values).

---

## Definition

> "A procedure to derive and/or select test cases based on an analysis of the internal structure of a component or system."

---

## Two Categories

| Category | Purpose |
|----------|---------|
| **Control Flow** | Identify execution paths through a module/programme; design test cases to cover those paths |
| **Data Flow** | Identify the improper use of data values due to coding errors |

---

## Data Flow Testing

### Defect Classes Detected

| Defect | Description |
|--------|------------|
| **Use before define** | A variable's value is referenced before any value has been assigned to it |
| **Define, never used** | A variable is declared and assigned but never subsequently read |
| **Destroy then use** | A variable is freed, nulled, or destroyed, then accessed |
| **Redefine without use** | A variable is assigned a new value before its previous assignment has been consumed |

### How It Is Done

**Static**: review and verification of the data flow graph.

**Dynamic**: design and execute test cases where:
- Every "define" is traced to each of its "uses"
- Every "use" is traced from its corresponding "define"
- For every variable, at least one test case covers a define–use pair

*Note*: Modern IDEs automatically flag many data flow defects (e.g., "variable used before assignment"). Understanding the underlying classes remains important for code inspection.

---

## Control Flow Graphs (CFGs)

A CFG models a programme as a directed graph where:
- **Nodes** represent statements or blocks of statements
- **Edges** represent transitions between statements

### Node Types

| Type | Description |
|------|------------|
| **Sequence** | Linear execution of statements |
| **If-then-else** | Binary decision → two outgoing edges (true/false) |
| **Case / Switch** | Multiple outgoing edges, one per case |
| **Junction** | Merge point where multiple paths converge |
| **While loop** | Condition checked before body executes |
| **Do-until loop** | Body executes at least once; condition checked after |

### Three-Step Testing Process

1. **Select test paths** (based on desired coverage level)
2. **Design test cases** for each selected path
3. **Run the test cases** and verify output against specification

---

## Factorial Example (Reference throughout)

```
1.  int i=1, facto=1
2.  input num
3.  if (num < 0)
4.    print "nope"
5.  else
6.    while (i <= num)
7.      facto = facto * i
8.      i++
9.    end-while
10.   print(facto)
11. end-if
```

**CFG**: 11 nodes, 12 edges (including back edge 9→6).

**Three paths**:

| Path | Node Sequence | Condition |
|------|--------------|-----------|
| 1 | 1→2→3→4→11 | `num < 0` |
| 2 | 1→2→3→5→6→10→11 | `num = 0` (loop skipped) |
| 3 | 1→2→3→5→6→7→8→9→6→10→11 | `num > 0` (loop executes) |

---

## Control Flow Coverage Criteria

Coverage criteria form a hierarchy from weakest to strongest. Higher levels generally subsume lower levels.

```
Path Coverage
    └── Multiple Condition Coverage
            └── Decision & Condition Coverage
                    └── Condition Coverage  ←─ does NOT subsume Decision (see below)
                            └── Decision Coverage  ←─ subsumes Statement
                                    └── Statement Coverage
```

### 1. Statement Coverage

Every executable statement is executed at least once.

```
Coverage (%) = (statements executed / total executable statements) × 100
```

**Factorial**: 2 test cases cover all statements:
- TC#1: `num > 0` (covers nodes 1,2,3,5,6,7,8,9,10,11)
- TC#2: `num < 0` (covers nodes 1,2,3,4,11)

*`num = 0` path not required but could reveal defects.*

---

### 2. Decision (Branch) Coverage

Every decision's True and False outcomes are each executed at least once. Decision coverage **subsumes** statement coverage.

```
Coverage (%) = (decision outcomes executed / total decision outcomes) × 100
```

**Factorial**: 2 decisions (`if` and `while`), 2 paths sufficient (same as statement coverage here):
- Path 1 (`num < 0`): if→True, while→False
- Path 2 (`num > 0`): if→False, while→True (while's False covered when loop terminates)

Every decision with a True and False outcome must be evaluated; multiple-exit cases need a test case for each exit.

---

### 3. Condition Coverage

Each **individual condition** within a compound decision (sub-expression) takes both True and False values at least once.

```
Coverage (%) = (conditions executed for both T and F / total conditions) × 100
```

**Example**: `if (clouds < 5 && daytime == true)` has two conditions:
- `clouds < 5` → must be True and False
- `daytime == true` → must be True and False

**Critical gap**: Condition coverage is **NOT** a superset of decision coverage.

```
if (X and Y)
    print("tested")
```

| TC | X | Y | Conditions covered | Branch covered |
|----|---|---|--------------------|----------------|
| 1 | T | F | X=T, Y=F | False branch only |
| 2 | F | T | X=F, Y=T | False branch only |

Both conditions exercised both ways → 100% condition coverage — but the **True branch** (`X=T, Y=T`) is never taken!

---

### 4. Decision & Condition Coverage

Both condition coverage and decision coverage must be satisfied simultaneously — closes the gap above.

---

### 5. Multiple Condition Coverage

All possible **combinations** of True and False within multi-conditional expressions are exercised.

For `if (A && B && C)`: 2³ = 8 test cases required (every T/F combination of A, B, C).

This subsumes statement, decision, condition, and decision & condition coverage.

---

### 6. Path Coverage

Every distinct control flow path is exercised. For loops, exhaustive coverage is impractical — use **Loop Coverage**:

| Iteration | Description |
|-----------|------------|
| **Zero** | Loop body never executes |
| **One** | Loop executes exactly once |
| **Typical** | Normal number of iterations |
| **Max** | Maximum feasible iterations |

---

### Coverage Summary Table

| Criterion | Subsumes | Practical Use |
|-----------|----------|---------------|
| Statement | — | Minimum baseline (80–90% industry target) |
| Decision/Branch | Statement | Standard CI target (70–80%) |
| Condition | — | Used where compound conditions are common |
| Decision & Condition | Decision + Condition | Better practice than either alone |
| Multiple Condition | D&C + Condition + Decision + Statement | Safety-critical systems |
| Path | Multiple Condition | Safety-critical only; impractical for most code |

---

## Cyclomatic Complexity (McCabe, 1976)

Measures programme complexity by counting **independent paths**.

### Formula

```
C = E − N + 2
```

- **E** = number of edges in the CFG
- **N** = number of nodes in the CFG
- C = minimum number of **basis paths**

**Factorial example**: C = 12 − 11 + 2 = **3**

### Threshold Values (McCabe et al., 1994)

| Range | Interpretation |
|-------|---------------|
| 1–4 | Simple module, low risk |
| 5–10 | Marginal module, low risk |
| 11–20 | Complex module, moderate risk |
| 21–50 | Complex module, high risk |
| > 50 | Untestable module, very high risk |

---

## Basis Path Testing

### What are Basis Paths?

**Basis paths** are independent, non-looping paths that can linearly generate all other paths through a module. They guarantee **at least full branch coverage** (not necessarily all possible paths).

**Independent path**: any path that introduces at least one new statement or conditional (new edge) not seen in previous paths.

### Five-Step Process

1. Model the code as a CFG
2. Compute cyclomatic complexity C
3. Select C basis paths (each must introduce at least one new edge)
4. Create a test case for each basis path
5. Execute test cases

**Advantage**: avoids redundant path testing; guarantees branch coverage as a minimum.

### Factorial — Basis Paths

C = 3, so 3 basis paths:

| Path # | Input | Expected Output |
|--------|-------|----------------|
| 1 | num = −1 | "nope" |
| 2 | num = 0 | 1 |
| 3 | num = 3 | 6 |

---

## LCSAJ — Linear Code Sequence and Jump

An alternative whitebox coverage metric. Code is broken into linear segments (**tuples**) from the start of the programme or branch point to its next jump or exit.

### Tuple Definition

```
(X, Y, Z)
```

- **X** = first statement in the linear sequence
- **Y** = last statement in the sequence (where the jump occurs)
- **Z** = target of the jump (another statement, or `exit`)

When executing from X to Y and then jumping to Z, the LCSAJ tuple `(X, Y, Z)` is **traversed**.

**LCSAJ provides 100% decision coverage.**

### Simple Example

```
1.  //begin-code
2.  int num
3.  input(num)
4.  if (num < 0)
5.    print "less"
6.  else
7.    print "more"
8.  //end-of-code
```

| Tuple | (X, Y, Z) | Traversed by |
|-------|-----------|--------------|
| 1 | (1, 4, 7) | Path 2: `num ≥ 0` |
| 2 | (1, 6, exit) | Path 1: `num < 0` |
| 3 | (7, 8, exit) | Path 2: `num ≥ 0` |

**Full coverage with 2 paths** (X = −5 and X = 5).

---

## Comparison: Coverage Criteria at a Glance

| Criterion | What it requires | Min TCs (Factorial) | Strength |
|-----------|-----------------|---------------------|---------|
| Statement | Every statement once | 2 | Lowest |
| Decision | Every T/F branch once | 2 | Low |
| Condition | Every sub-condition T and F | 2+ | Medium (see gap) |
| D & C | Every decision and condition | 2+ | Medium-high |
| Multiple Condition | All T/F combinations | 2ⁿ per condition group | High |
| Path | All paths (with loop limits) | 3+ | Highest |
| Basis Path (C=3) | 3 independent paths | 3 | Guaranteed branch coverage |
| LCSAJ | All (X,Y,Z) tuples | 2 | 100% decision coverage |

---

## Related Concepts

- [[concepts/test-design-techniques]] — coverage criteria overview, cyclomatic complexity formula (brief)
- [[concepts/software-testing-fundamentals]] — testing levels; unit/integration testing (where whitebox is applied)
- [[concepts/software-verification-and-validation]] — V&V context; static vs dynamic V&V
- [[concepts/static-code-analysis]] — automated static analysis tooling for data flow and control flow defects
