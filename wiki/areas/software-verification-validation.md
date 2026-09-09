---
type: area
title: "Software Verification and Validation"
domain: software-verification-validation
status: established
created: 2026-08-31
updated: 2026-08-31
tags: [svv, software-testing, verification, validation, ict3112]
---

# Area: Software Verification and Validation

This area covers the ICT3112 course content and related knowledge on software V&V — the systematic process of confirming software is built correctly and fulfils its intended purpose.

---

## Core Concept Pages

| Page | Description | Complexity |
|------|------------|------------|
| [[concepts/software-verification-and-validation\|Software V&V]] | V&V definitions, static vs dynamic, DORA categories, famous failures, reliability metrics (MTTF/MTTR/MTBF), reliability models, defect density, customer metrics | high |
| [[concepts/software-testing-fundamentals\|Software Testing Fundamentals]] | ISTQB principles, error/defect/failure chain, 8 best practices, testing levels, testing pyramid, BB vs WB, regression | high |
| [[concepts/whitebox-testing-techniques\|Whitebox Testing Techniques]] | Control flow graphs, data flow defects, coverage hierarchy (statement/decision/condition/MC/path), cyclomatic complexity, basis path testing, LCSAJ | high |
| [[concepts/blackbox-testing-techniques\|Blackbox Testing Techniques]] | Use case testing, equivalence partitioning, boundary value analysis, decision table testing, state transition testing | high |
| [[concepts/test-design-techniques\|Test Design Techniques]] | EP, BVA overview, statement/branch/condition/path coverage overview, mutation testing, cyclomatic complexity | high |
| [[concepts/static-code-analysis\|Static Code Analysis]] | SAST tools, taint analysis, control flow tools, abstract interpretation | high |

---

## Source Pages (ICT3112)

| Page | Content |
|------|---------|
| [[sources/ict3112-svv-l1\|L1: Software V&V Intro]] | V&V definitions, DORA categories, famous failures, cost of poor quality, reliability metrics, defect density, PUM |
| [[sources/ict3112-svv-l2\|L2: Intro to Testing]] | Error/defect/failure chain, testing limitations, pesticide paradox, Pareto rule, V&V Venn diagram |
| [[sources/ict3112-svv-l3\|L3: Static Analysis]] | Four review types (ad hoc/walkthrough/technical/inspection), code inspection checklist (6 fault classes), tool benefits |
| [[sources/ict3112-svv-l4\|L4: Dynamic Analysis]] | 8 testing best practices, BB vs WB, retesting vs regression, V-model, 4 testing levels (unit/integration/system/acceptance), alpha/beta, 4 testing types |
| [[sources/ict3112-svv-l5-0\|L5.0: Whitebox Intro]] | WB definition, data flow vs control flow categories, 4 data flow defect types |
| [[sources/ict3112-svv-l5-1\|L5.1: CFGs and Paths]] | CFG construction, 6 node types, factorial example (11 nodes/12 edges), 3 paths |
| [[sources/ict3112-svv-l5-2\|L5.2: Code Coverage]] | Coverage hierarchy, formulas and factorial examples for all 6 levels, loop coverage |
| [[sources/ict3112-svv-l5-3\|L5.3: Complexity and LCSAJ]] | Cyclomatic complexity C=E−N+2, threshold table, basis path testing, LCSAJ tuples (X,Y,Z) |
| [[sources/ict3112-svv-l6-0\|L6.0: Blackbox + Use Case]] | BB definition, use case components, resource management example, scenario-to-test-case mapping |
| [[sources/ict3112-svv-l6-1\|L6.1: EP and BVA]] | EP examples (integer, binary search), advantages/disadvantages; BVA examples (integer, string, date, time), 4 general rules |
| [[sources/ict3112-svv-l6-2\|L6.2: Decision Tables and State Transition]] | Decision table structure, pricing and movie examples, state diagram components, door lock example, 0-switch/1-switch coverage |

---

## Worked Labs (ICT3112)

| Page | Content |
|------|---------|
| [[examples/ict3112-lab1-nunit-tdd-calculator\|Lab 1: NUnit + TDD Calculator]] | C#/.NET 10 console calculator + NUnit 4 test project; Arrange-Act-Assert, parameterised tests, exception assertions, boundary values, one red-green-refactor cycle on `Divide` |
| [[examples/ict3112-lab2-reqnroll-bdd\|Lab 2: Reqnroll BDD + Acceptance Testing]] | Adds a Reqnroll acceptance-test project to the Lab 1 calculator; Gherkin features, Cucumber Expressions, scenario outlines, step data tables, tags, context injection; MTBF / Availability / Basic Musa reliability calculations as production code |

---

## Related Areas

- [[areas/machine-learning]] — ML evaluation and experimental design (testing as applied to ML models)
- Software Engineering area (ICT2113, ICT2112, INF2001)
