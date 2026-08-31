---
type: source
title: "ICT3112 SVV — Lecture 5.1: Whitebox Testing — CFGs and Paths"
source_file: "raw/ICT3112 Software Verification and Validation - L5_1_Whitebox_Testing_CFGs_and_Paths.md"
domain: software-verification-validation
tags: [ict3112, svv, whitebox-testing, control-flow-graph, cfg, paths]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 5.1: Whitebox Testing — CFGs and Paths

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Control Flow Graph (CFG) — Overview

**Goal**: model a programme/function as a series of **nodes** and **edges** to identify execution paths.

- **Node**: represents a statement or block of statements
- **Edge**: represents a transition between statements

### Three-Step Process

1. **Select the test paths** you wish to exercise (based on chosen coverage level)
2. **Design test cases** for selected paths (create specific unit tests)
3. **Run the test cases** to verify code meets its specification

---

## CFG Node Types

| Node Type | Description |
|-----------|------------|
| **Sequence** | Linear sequence of statements |
| **If-then-else** | Binary decision (true/false branches) |
| **Case / Switch** | Multiple branches from a single decision |
| **Junction** | Merge point where multiple paths converge |
| **While loop** | Condition checked before loop body |
| **Do-until loop** | Loop body executes at least once; condition checked after |

---

## Factorial Example — CFG

### Pseudo-code

```
1.  int i=1, facto=1
2.  input num
3.  if (num < 0)
4.    print "nope"      ← true branch
5.  else                ← false branch entry
6.    while (i <= num)
7.      facto = facto * i
8.      i++
9.    end-while         ← back edge to node 6
10.   print(facto)
11. end-if
```

### CFG Structure

```
1 → 2 → 3 → 4 → 11          (num < 0 path)
             ↓
             5 → 6 → 10 → 11  (num = 0, loop skipped)
                  ↓
                 7 → 8 → 9 → 6  (loop back edge)
```

- **Nodes**: 11 total (nodes 1–11, where 9 is the end-while back edge)
- **Edges**: 12 total (including the loop back edge 9→6)

### Three Identified Paths

| Path | Node Sequence | Input Condition |
|------|--------------|-----------------|
| **Path 1** | 1→2→3→4→11 | `num < 0` |
| **Path 2** | 1→2→3→5→6→10→11 | `num = 0` (loop skipped) |
| **Path 3** | 1→2→3→5→6→7→8→9→6→10→11 | `num > 0` (loop executes) |

---

## Linked Concepts

- [[concepts/whitebox-testing-techniques]] — full whitebox reference: CFG construction, coverage criteria, cyclomatic complexity, LCSAJ
