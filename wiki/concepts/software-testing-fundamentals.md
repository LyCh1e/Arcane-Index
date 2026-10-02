---
type: concept
title: "Software Testing Fundamentals"
domain: software-engineering
complexity: high
status: established
created: 2026-05-21
updated: 2026-10-02
tags: [software-testing, quality-assurance, unit-testing, integration-testing, system-testing, acceptance-testing, testing-pyramid, regression-testing, static-testing, dynamic-testing]
---

# Software Testing Fundamentals

Software testing is the systematic process of evaluating a software system to determine whether it satisfies specified requirements and to identify defects. Testing does not prove software is correct; it reveals defects that exist.

---

## The Seven ISTQB Principles

The International Software Testing Qualifications Board (ISTQB) formalises seven foundational principles that govern all testing activity:

| # | Principle | Meaning |
|---|-----------|---------|
| 1 | **Testing shows presence of defects** | Testing can confirm defects exist; it cannot prove a system is defect-free |
| 2 | **Exhaustive testing is impossible** | All input combinations cannot be tested; use risk analysis and prioritisation to focus effort |
| 3 | **Early testing saves cost** | The cost of fixing a defect rises exponentially the later it is discovered; shift testing left |
| 4 | **Defect clustering** | A small number of modules contain the majority of defects (Pareto principle: ~80% of defects in ~20% of code) |
| 5 | **Pesticide paradox** | Repeated identical tests stop finding new defects; test suites must be regularly revised and extended |
| 6 | **Testing is context-dependent** | A safety-critical system requires different testing to a marketing website |
| 7 | **Absence-of-errors fallacy** | A system with no detected defects is not necessarily useful; testing must verify the right things are built |

Source: ISTQB Certified Tester Foundation Level v4.0 (2024)

---

## Static vs Dynamic Testing

| Dimension | Static Testing | Dynamic Testing |
|-----------|---------------|-----------------|
| Code executed? | No | Yes |
| When | Early (design, code review) | After implementation |
| Techniques | Reviews, inspections, walkthroughs, static analysis | All levels of test execution |
| Finds | Logic errors, standard violations, security flaws, dead code | Runtime failures, performance issues, integration errors |

### Static Testing Techniques

- **Informal review** — author walks peers through work; no formal output required
- **Walkthrough** — author leads meeting; participants ask questions and note issues; low formality
- **Technical review** — led by a moderator; produces a defect list; peers verify conformance to standards
- **Inspection** — the most formal; trained moderator, checklist-driven, metrics collected; formally proven most cost-effective (Fagan inspections)

---

## The Four Testing Levels

Testing is structured in four levels, each building on the previous:

```
  ┌──────────────────────────────┐
  │   Acceptance Testing (UAT)   │  ← Do we have the right product?
  ├──────────────────────────────┤
  │      System Testing          │  ← Does the complete system work?
  ├──────────────────────────────┤
  │    Integration Testing       │  ← Do the parts work together?
  ├──────────────────────────────┤
  │       Unit Testing           │  ← Do individual parts work in isolation?
  └──────────────────────────────┘
```

### Unit Testing

Tests an individual unit (function, method, class) in isolation from its dependencies. Dependencies are replaced with **test doubles** (mocks, stubs, fakes, spies). Unit tests run in milliseconds, are numerous, and form the base of the Testing Pyramid.

**Goal**: verify that each unit of code behaves correctly for a variety of inputs.

### Integration Testing

Tests that two or more components work correctly together. Common integration points include databases, APIs, file systems, and external services. Slower than unit tests; fewer in number.

**Key variant — Contract testing**: Consumer-Driven Contract (CDC) tests establish formal agreements between a service provider and its consumers. Each consumer publishes expected interactions; the provider runs those expectations as tests. Enables independent deployment in microservice architectures.

### System Testing

Tests the complete, integrated application against requirements. Black-box in nature — testers focus on behaviour, not internal structure. Includes functional verification, performance, security, and usability.

### Acceptance Testing

The final gate before release. Verifies the system meets business requirements and user needs. Subtypes:

- **User Acceptance Testing (UAT)** — end users test real scenarios against real business rules
- **Alpha testing** — internal users test the pre-release system
- **Beta testing** — external users test a near-final release in production-like conditions

### Labels depend on the boundary (ICT3112 Lab 4)

| Test | Primary evidence | Does not establish alone |
|---|---|---|
| Unit | Focused rule correct under controlled inputs | System works through its external interface |
| Integration | Selected components / real dependency cooperate | Every component and journey works as a whole |
| Acceptance | Agreed example of required behaviour satisfied | A technical layer — need not use a browser |
| Browser UI / system | Integrated local system behaves via the browser | Every production service is present |
| End-to-end | Representative journey across the production-like boundary | All journeys, failures or qualities |

Browser test ≠ automatically end-to-end; acceptance ≠ browser ≠ UAT; test *level* (scope) and *technique* (white/black-box derivation) are separate axes. Detail: [[concepts/browser-based-system-testing]].

---

## The Testing Pyramid

Coined by Mike Cohn (*Succeeding with Agile*, 2009); formalised by Martin Fowler:

```
         ▲
        /E2E\          ← Few; slow; expensive; flaky
       /──────\
      /  Integ. \      ← Some; moderately fast
     /────────────\
    /   Unit Tests  \  ← Many; fast; cheap
   /──────────────────\
```

**Recommended distribution**: 70% unit — 20% integration — 10% end-to-end.

> ICT3112 Lab 4 caveat: the pyramid is a *guiding model*, not a required ratio — the right balance depends on the system, its risks and the evidence needed ([[sources/ict3112-svv-lab4]]).

### Anti-Pattern: Ice Cream Cone

Teams that rely primarily on manual or UI-based tests and have few unit tests produce an inverted pyramid (or "ice cream cone"). Consequences: slow CI pipelines, brittle tests, high maintenance cost, slow feedback loops.

**Principle**: push tests as far down the pyramid as possible. If a high-level test duplicates confidence already provided by a lower-level test, delete the high-level one.

---

## Black-Box vs White-Box Testing

| Dimension | Black-Box | White-Box |
|-----------|-----------|-----------|
| Knowledge of internals | None — tests specification only | Full — tests code structure |
| Typical level | System, acceptance | Unit, integration |
| Key techniques | Equivalence partitioning, boundary value analysis, decision tables | Statement coverage, branch coverage, path coverage, mutation testing |
| Also called | Specification-based, functional | Structure-based, code-based |

---

## Regression Testing

Re-running previously passing tests after a code change to confirm no previously working functionality has broken. In CI/CD pipelines, the full regression suite runs automatically on every commit or before every release.

**Regression testing and the Pesticide Paradox**: over time, a static regression suite catches fewer new defects. New test cases must be added for each new feature and each defect discovered.

---

---

## Error → Defect → Failure Chain

Understanding the distinction between these three terms is foundational to precise communication in testing:

| Term | Definition |
|------|-----------|
| **Error / Mistake** | A human action that produces an incorrect result (e.g., a developer misunderstands a requirement) |
| **Fault / Bug / Defect** | A flaw in a component that can cause the system to fail to perform its required function (e.g., incorrect code resulting from the error) |
| **Failure** | Critical deviation of the system from its expected delivery, service, or result (when defective code is executed) |

**Chain**: Human makes an error → error creates a defect in code → defective code is executed → system exhibits a failure.

> "Testing can show that defects are present, but cannot prove that there are no defects."
> — Bill Hetzel, *The Complete Guide for Software Testing*, 1988

---

## Eight Good Testing Practices

| # | Practice |
|---|---------|
| 1 | A good test case has a **high probability of detecting undiscovered defects**, not just showing the programme works |
| 2 | It is insufficient to be the **only one testing your own code** — peer review is essential |
| 3 | Every test case should specify the **expected result** before execution |
| 4 | Write test cases for **valid and invalid input** conditions |
| 5 | Thoroughly **inspect the results** of each test |
| 6 | Ensure **testability** is a key objective in software design |
| 7 | **Never alter the programme** to make testing easier |
| 8 | Testing must start with clear **objectives** |

---

## Testing by Lifecycle Phase

Testing takes different forms depending on where in the software lifecycle it occurs:

| Phase | Who Performs | Objective |
|-------|-------------|-----------|
| **Development testing** | Developers / testers (controlled environment) | Identify defects by causing failures; fix them |
| **Operational testing** | Testing / operations teams | Evaluate the system in its operational environment; assess reliability and availability |
| **Acceptance testing** | Customer or users | Verify business requirements are met; decide whether to accept the system |
| **Maintenance testing** | Testers | Ensure no new defects manifest after a change is introduced |

---

## Retesting vs Regression Testing

These are subtly but importantly different:

| Type | Definition |
|------|-----------|
| **Retesting** | Rerunning tests that previously *found* defects to confirm the fix is effective |
| **Regression testing** | Running tests in *parallel areas* of code to confirm fixes do not introduce new defects elsewhere |

> "In empirical studies it's estimated that up to 50% of bug fixes actually introduce additional errors into the code."
> — *Software Testing Primer*, Nick Jenkins

---

## Goodhart's Law in Testing

> "When a measure becomes a target, it ceases to be a good measure."
> — Goodhart's Law (paraphrased by Edwards Deming)

**Applied to software testing**: when teams are evaluated on the *number of passing tests*, the incentive structure shifts from finding defects to inflating test counts with trivial or redundant tests. The metric appears healthy whilst coverage is superficial.

The goal of testing is to **find defects and assess software quality** — passing tests are a *measurement* of that goal, not the goal itself. If passing-test count becomes the target, developers game it by adding tests designed to pass rather than to probe for failures.

This applies equally to other testing metrics (code coverage %, bug count, etc.) — once any metric is used to evaluate performance, the behaviour it was meant to measure degrades. Sound testing practice requires keeping the *purpose* (finding defects, revealing risk) in view, not the proxy metric.

---

## Key Connections

- [[concepts/browser-based-system-testing]] — Selenium system tests at the top of the pyramid: explicit waits, Page Objects, hosting ownership, CI orchestration (ICT3112 Lab 4)
- [[concepts/test-driven-development]] — TDD keeps the unit-test layer dense and current by writing tests before code
- [[concepts/test-design-techniques]] — black-box and white-box design techniques that populate each layer
- [[concepts/whitebox-testing-techniques]] — detailed CFG, coverage criteria, cyclomatic complexity, LCSAJ (ICT3112)
- [[concepts/blackbox-testing-techniques]] — detailed EP, BVA, decision tables, state transition, use case testing (ICT3112)
- [[concepts/software-verification-and-validation]] — V&V fundamentals; reliability metrics; defect density
- [[concepts/scrum-framework]] — testing is continuous across each Sprint; the Definition of Done typically requires passing tests before an Increment is accepted
- [[concepts/software-design-process]] — testability is a design quality; highly coupled code is hard to unit-test
- [[concepts/owasp-top-10]] — security testing (DAST, SAST) maps directly to OWASP vulnerability categories
- [[synthesis/web-security-ssdlc-bridge]] — SAST is static testing of code; DAST is dynamic security testing of the running system
