---
type: source
title: "ICT3112 SVV — Lecture 5.0: Whitebox Testing Introduction"
source_file: "raw/ICT3112 Software Verification and Validation - L5_0_Whitebox_Testing_Intro.md"
domain: software-verification-validation
tags: [ict3112, svv, whitebox-testing, control-flow, data-flow]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 5.0: Whitebox Testing Introduction

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Definition

**Whitebox Testing**: "A procedure to derive and/or select test cases based on an analysis of the internal structure of a component or system."

Applied at **component (unit) testing** and **integration testing** levels.

---

## Two Categories of Whitebox Testing

| Category | Purpose | Techniques |
|----------|---------|-----------|
| **Control Flow** | Identify execution paths through a module/programme; design test cases to cover those paths | Statement testing, decision testing, condition testing, path testing, LCSAJ |
| **Data Flow** | Identify improper use of data values due to coding errors | Define-use pair analysis |

---

## Data Flow Testing

### Purpose
Identify defects caused by improper use of data values:
1. **Use before define** — referencing a variable's value without first assigning a value to it
2. **Define, never used** — declaring and assigning a variable that is never subsequently read
3. **Destroy then use** — a variable is freed/nulled, then accessed
4. **Redefine without use** — assigning a new value to a variable before the previous assignment has been used

### How it is done
- **Static testing**: reviewing and verifying the data flow graph
- **Dynamic testing**: designing and executing test cases where:
  - Every "define" is traced to each of its "uses"
  - Every "use" is traced from its corresponding "define"
  - For every variable, at least one test case is created for a define-use pair

**Note**: Modern IDEs perform much of this static checking automatically (e.g., "variable used before assignment" warnings), but understanding the underlying defect classes remains important.

---

## Control Flow Testing

### Purpose
A testing approach that identifies execution paths through code and creates test cases to cover those paths.

### Key Concerns

Exercising all control flows can be impractical or impossible:

```
for (x = 0; x < 100; x++)
    for (y = 0; y < 100; y++)
        for (z = 0; z < 100; z++)
            print("testing");
```

This nested loop alone has 100³ = 1,000,000 possible loop iterations.

Questions that must be answered:
- Should we execute all possible paths? (Usually: no)
- How many paths do we need to execute?
- What level of coverage is sufficient?

### Key Definitions

- **Control Flow Graph (CFG)**: a sequence of events (paths) to be followed in the execution of a component or system.
- **Control Flow Path**: a sequence of executable statements in a component or system, from its entry to its exit point.

---

## Whitebox Techniques Overview

| Technique | Category |
|-----------|---------|
| Statement testing | Control flow |
| Decision testing | Control flow |
| Condition testing | Control flow |
| Path testing | Control flow |
| LCSAJ coverage | Control flow |
| Data flow testing | Data flow |

---

## Linked Concepts

- [[concepts/whitebox-testing-techniques]] — full whitebox reference (CFG, coverage, complexity, LCSAJ)
- [[concepts/software-testing-fundamentals]] — testing levels (unit/integration/system/acceptance)
