---
type: source
title: "ICT3112 SVV — Lecture 4: Dynamic Analysis / Software Testing"
source_file: "raw/ICT3112 Software Verification and Validation - L4_Dynamic_Analysis.md"
domain: software-verification-validation
tags: [ict3112, svv, dynamic-analysis, testing-levels, v-model, unit-testing, integration-testing, system-testing, acceptance-testing]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 4: Dynamic Analysis

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Core Framing

> "You can hope your software works or you can know it works — through software testing."
> — *Software Testing Primer*, Nick Jenkins

- **Testing**: the process of executing a programme with the intent of finding errors.
- Testing can show the **presence** of bugs but never their **absence** (Bill Hetzel / Dijkstra).

---

## 8 Good Testing Practices

| # | Practice |
|---|---------|
| 1 | A good test case has a **high probability of detecting undiscovered defects**, not just showing the programme works correctly |
| 2 | It is insufficient to be the **only one testing your own code** |
| 3 | Every test case should have a description of the **expected result** |
| 4 | Write test cases for **valid as well as invalid input** conditions |
| 5 | Thoroughly **inspect the results** of each test |
| 6 | Ensure **testability** is a key objective in your software design |
| 7 | **Never alter the programme** to make testing easier |
| 8 | Testing, like almost every other activity, must start with **objectives** |

---

## Core Testing Types: Black-Box vs White-Box

| Dimension | Black-Box | White-Box |
|-----------|-----------|-----------|
| What is considered | Inputs and outputs only | Inputs, outputs, and internal structure |
| Internal workings | Unknown or ignored | Specifically considered |
| Examples | Requirements, specification-based | Code coverage, path testing |

---

## Retesting vs Regression Testing

| Type | Definition |
|------|-----------|
| **Retesting** | Rerunning tests that previously found defects to confirm the defect has been fixed |
| **Regression testing** | Repeating tests in **parallel areas** of code to ensure fixes do not introduce new errors elsewhere |

> "In empirical studies it's estimated that up to 50% of bug fixes actually introduce additional errors into the code."
> — *Software Testing Primer*, Nick Jenkins

---

## V-Model of Testing

```
Requirements ──────────────────────────── Acceptance Testing
    System Design ──────────────────── System Testing
        Architecture Design ──────── Integration Testing
            Detailed Design ──── Unit Testing
                      Code
```

Left side = Verification (specification-focused)  
Right side = Validation (user-needs-focused)

---

## Four Testing Levels

### Unit Testing (Component Testing)

| Field | Detail |
|-------|--------|
| **Objective** | Verify functionality; search for defects in separately testable software components (e.g., classes, functions) |
| **Scope** | Functional and non-functional characteristics (performance, memory leaks, usability) |
| **Derived from** | Component specifications, requirements, detailed design documents |
| **Conductor** | **Developers** |

### Integration Testing

| Field | Detail |
|-------|--------|
| **Objective** | Test programme interfaces; confirm programmes/components are linked together correctly |
| **Scope** | Functional and non-functional characteristics of integration (e.g., performance between components) |
| **Derived from** | Software and system design, interface specification, use cases |
| **Conductor** | **Developers, testing team** (depending on integration level) |

### System Testing

| Field | Detail |
|-------|--------|
| **Objective** | Test system behaviour as defined by project scope; verify readiness for acceptance testing |
| **Scope** | Functional and non-functional system requirements |
| **Derived from** | System requirement specifications, use cases, functional specification, risk analysis |
| **Conductor** | **Testing team** (depending on company size, sometimes developers) |

### Acceptance Testing

| Field | Detail |
|-------|--------|
| **Objective** | Establish confidence in the system; assess readiness for deployment |
| **Scope** | System functional and performance requirements, reliability, and usability |
| **Derived from** | User requirements, system requirements, business processes, use cases, risk analysis |
| **Conductor** | **Customer or users** |

#### Acceptance Testing Sub-types

| Sub-type | Description |
|----------|------------|
| **Alpha (α) testing** | Simulated or actual operational testing by users/customers or an independent test team *on site*, not by developers. Used as a form of internal acceptance testing for mainstream software. |
| **Beta (β) testing** | Operational testing by potential or existing users/customers at an *external site*. Used as external acceptance testing to acquire market feedback. |

---

## Four Main Testing Types

| Type | What it tests | Testing Approach |
|------|--------------|------------------|
| **Functional** | Functionality performed by the system — *what* the system does | Predominantly black-box |
| **Non-functional** | Characteristics of the software product — *how well* it works (reliability, efficiency, usability, maintainability, portability) | Usually black-box; considers external behaviour |
| **Structural** | Internal structure of components/systems | White-box |
| **Retesting & Regression** | Changes made to the software | Both black-box and white-box |

---

## Linked Concepts

- [[concepts/software-testing-fundamentals]] — testing overview, V-model, ISTQB principles
- [[concepts/software-verification-and-validation]] — V&V definitions and context
- [[concepts/whitebox-testing-techniques]] — white-box methods (CFG, coverage, complexity)
- [[concepts/blackbox-testing-techniques]] — black-box methods (EP, BVA, decision tables, state transition)
