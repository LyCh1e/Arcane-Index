---
type: source
title: "ICT3112 SVV — Lecture 5.3: Whitebox Testing — Code Complexity and LCSAJ"
source_file: "raw/ICT3112 Software Verification and Validation - L5_3_Whitebox_Testing_Code_Complexity_and_LCSAJ.md"
domain: software-verification-validation
tags: [ict3112, svv, whitebox-testing, cyclomatic-complexity, basis-path-testing, lcsaj]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 5.3: Code Complexity and LCSAJ

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Cyclomatic Complexity (McCabe, 1976)

Measures the complexity of a programme by counting the number of **independent paths** in its source code.

### Formula

```
C = E − N + 2
```

- **E** = number of edges in the CFG
- **N** = number of nodes in the CFG
- C = the **minimum** number of basis paths

### Independent Path

Any path in a programme that introduces at least one new set of statements or a new conditional (i.e., a new edge that has not been traversed before).

### Upper Bound

Cyclomatic complexity provides a calculation for an upper bound on the number of test cases required to guarantee coverage of all programme statements and decisions.

---

## Threshold Values (McCabe et al., 1994)

| Range | Interpretation |
|-------|---------------|
| 1–4 | Simple module, low risk |
| 5–10 | Marginal module, low risk |
| 11–20 | Complex module, moderate risk |
| 21–50 | Complex module, high risk |
| > 50 | Untestable module, very high risk |

Originally, complexity > 10 required justification (e.g., use of a large switch statement).

---

## Basis Path Testing

### Definition

**Basis paths** are independent, non-looping paths that can be used to generate all possible paths through a module in linear combinations. Note: basis paths do not necessarily cover *all* possible paths, but they guarantee at least full branch coverage.

### Five-Step Process

1. Model the software code as a Control Flow Graph (CFG)
2. Compute the cyclomatic complexity C
3. Select a set of C basis paths
4. Create a test case for each basis path
5. Execute the test cases

**Advantage**: avoids redundant path testing while guaranteeing at least full branch coverage in the worst case.

### Factorial Example

CFG: 11 nodes, 12 edges → C = 12 − 11 + 2 = **3 basis paths**

| Path # | Input | Expected Result | Node Sequence |
|--------|-------|-----------------|---------------|
| 1 | num = −1 | "nope" | 1→2→3→4→11 |
| 2 | num = 0 | '1' | 1→2→3→5→6→10→11 |
| 3 | num = 3 | '6' | 1→2→3→5→6→7→8→9→6→10→11 |

---

## LCSAJ — Linear Code Sequence and Jump

### Definition

**LCSAJ (Linear Code Sequence and Jump)**: a white-box testing technique to identify code coverage. Code is broken into sections (tuples) from the beginning of the programme or a branch, terminating at the end of the programme or a branch.

An LCSAJ unit is represented as a **tuple (X, Y, Z)** where:
- **X** = location of the first statement in the unit
- **Y** = location of the last statement in the unit
- **Z** = location to which the statement at Y jumps (or `exit`)

When executing from X to Y and then jumping to Z, the LCSAJ `(X, Y, Z)` is said to be **traversed** or **exercised**.

**LCSAJ provides 100% decision coverage.**

---

## LCSAJ — Simple Example

### Pseudo-code

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

### Tuples

| Tuple | (X, Y, Z) | Meaning |
|-------|-----------|---------|
| 1 | (1, 4, 7) | Start at 1, reach decision at 4 (false: num ≥ 0), jump to 7 |
| 2 | (1, 6, exit) | Start at 1, reach decision at 4 (true: num < 0), execute 5, jump to exit |
| 3 | (7, 8, exit) | Start at 7, execute 7–8, jump to exit |

### Coverage

```
Path 1 (X = −5): covers LCSAJ tuple (1, 6, exit)
Path 2 (X = 5):  covers tuples (1, 4, 7) and (7, 8, exit)
```

Two paths achieve full LCSAJ coverage — this is an alternative metric to CFG-based path analysis.

---

## Linked Concepts

- [[concepts/whitebox-testing-techniques]] — comprehensive whitebox reference (CFG, coverage hierarchy, cyclomatic complexity, LCSAJ)
- [[sources/ict3112-svv-l5-1]] — CFG construction (11-node factorial example)
- [[sources/ict3112-svv-l5-2]] — code coverage criteria (statement/decision/condition/path)
