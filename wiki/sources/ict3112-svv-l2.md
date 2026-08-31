---
type: source
title: "ICT3112 SVV — Lecture 2: Introduction to Testing Concepts"
source_file: "raw/ICT3112 Software Verification and Validation - L2_Intro_to_Testing.md"
domain: software-verification-validation
tags: [ict3112, svv, software-testing, defect, failure, pesticide-paradox]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 2: Introduction to Testing

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Definitions

| Term | Definition |
|------|-----------|
| **Error / Mistake** | A human action that produces an incorrect result |
| **Fault / Bug / Defect** | A flaw in a component that can cause it to fail to perform its required function (e.g., incorrect requirement or data definition) |
| **Failure** | Critical deviation of the component/system from its expected delivery, service, or result |

**Chain**: Human makes an error → error creates a defect in code → defective code is executed → system fails

---

## Testing Limitations

> "If the objective of testing was to prove that a program is free of bugs, then not only would testing be practically impossible, but it would also be theoretically impossible."
> — Bill Hetzel, *The Complete Guide for Software Testing*, 1988

Two core tenets:
1. Testing can show defects are **present**, but cannot prove there are **no** defects.
2. Testing reduces the probable presence of undiscovered defects, but finding no defects does not prove faultlessness.

---

## What Testing Targets

| Target | Common Defects |
|--------|---------------|
| **Requirements** | Wrong, missing, inconsistent, incomplete, ambiguous, implementation assumptions |
| **Design** | Wrong logic, wrong algorithm, conflicting interfaces, inconsistency with requirements |
| **Code** | Coding standard violations, uninitialised variables, deep nesting, assignment errors, wrong conditions, no exception handling, poor documentation |

---

## Testing by Lifecycle Phase

| Phase | Performer | Objective |
|-------|-----------|-----------|
| **Development testing** | Developers / testers (controlled environment) | Identify defects by causing as many failures as possible and fixing them |
| **Operational testing** | Testing team / operations | Evaluate system in its operational environment; assess reliability and availability |
| **Acceptance testing** | Customer / users | Verify that business requirements are met; determine whether to accept the system |
| **Maintenance testing** | Testers | Ensure no new defects manifest after a change is introduced |

---

## Effective vs Efficient Testing

- **Effective testing**: focuses on producing a desired result that answers the business goals for the system.
- **Efficient testing**: focuses on achieving the largest amount of test coverage with the smallest number of tests.

---

## Testing vs Debugging

Traditionally separate roles — testers locate errors, developers fix them. Modern practice: developers are increasingly responsible for testing their own code. Debugging refers to the process developers use while writing code (unit testing / IDE integration).

---

## Pesticide Paradox

The more you test a software programme, the more immune it becomes to your tests.

**Solution**: tests must be continually developed and executed across different parts of the programme to find new bugs.

---

## Pareto / 80-20 Rule

**Principle**: 80% of bugs are found in 20% of the code. Tests should focus on the areas where testers expect (and observe) high defect density.

---

## Defect Distribution Graph

Cost per defect is lowest at the requirements/design phase and rises steeply toward post-production release. This reinforces the importance of early testing (shift-left).

**Source**: National Institute of Standards and Technology — *The Economic Impact of Inadequate Infrastructure for Software Testing*, May 2002.

---

## V&V Venn Diagram

Static and dynamic V&V overlap substantially. Key items by side:

| Verification (Static focus) | Both | Validation (Dynamic focus) |
|-----------------------------|------|---------------------------|
| Proofs of correctness | Automated testing | Acceptance testing |
| Style checkers | Regression testing | Usability testing |
| Consistency checking | System testing | Prototyping |
| Model/spec inspection | Integration testing | Goal analysis |
| Static analysis (code inspections, reviews) | Unit testing | |

---

## Linked Concepts

- [[concepts/software-verification-and-validation]] — V&V fundamentals
- [[concepts/software-testing-fundamentals]] — testing overview (ISTQB principles, testing pyramid, V-model)
- [[concepts/whitebox-testing-techniques]] — structure-based testing
- [[concepts/blackbox-testing-techniques]] — specification-based testing
