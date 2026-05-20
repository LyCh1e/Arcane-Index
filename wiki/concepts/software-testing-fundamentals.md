---
type: concept
title: "Software Testing Fundamentals"
domain: software-engineering
complexity: high
status: established
created: 2026-05-21
updated: 2026-05-21
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

## Key Connections

- [[concepts/test-driven-development]] — TDD keeps the unit-test layer dense and current by writing tests before code
- [[concepts/test-design-techniques]] — black-box and white-box design techniques that populate each layer
- [[concepts/scrum-framework]] — testing is continuous across each Sprint; the Definition of Done typically requires passing tests before an Increment is accepted
- [[concepts/software-design-process]] — testability is a design quality; highly coupled code is hard to unit-test
- [[concepts/owasp-top-10]] — security testing (DAST, SAST) maps directly to OWASP vulnerability categories
- [[synthesis/web-security-ssdlc-bridge]] — SAST is static testing of code; DAST is dynamic security testing of the running system
