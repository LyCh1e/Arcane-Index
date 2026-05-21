---
type: synthesis
title: "Research: Software Testing"
created: 2026-05-21
updated: 2026-05-21
tags: [research, software-testing, quality-assurance, TDD, BDD, testing-pyramid]
status: developing
related:
  - "[[concepts/software-testing-fundamentals]]"
  - "[[concepts/test-driven-development]]"
  - "[[concepts/test-design-techniques]]"
  - "[[concepts/scrum-framework]]"
  - "[[concepts/software-design-process]]"
  - "[[concepts/owasp-top-10]]"
  - "[[synthesis/web-security-ssdlc-bridge]]"
sources:
  - "[[sources/istqb-ctfl-v4]]"
  - "[[sources/fowler-practical-test-pyramid]]"
---

# Research: Software Testing

## Overview

Software testing is the empirical verification that a system behaves correctly and satisfies its requirements. It cannot prove correctness — it reveals defects. The field is structured around a pyramid of test granularity, a set of seven foundational principles (ISTQB), two complementary design practices (TDD and BDD), and a family of techniques for deriving effective test cases systematically. Modern testing integrates into CI/CD pipelines through "shift-left" — running tests earlier and more frequently.

---

## Key Findings

- **Testing shows presence, not absence, of defects** — the most misunderstood principle; teams that stop testing because "no defects were found" commit the absence-of-errors fallacy (Source: [[sources/istqb-ctfl-v4]])
- **The Testing Pyramid prevents pipeline rot** — teams that invest primarily in E2E/UI tests acquire slow, brittle suites; the 70/20/10 (unit/integration/E2E) heuristic prevents this (Source: [[sources/fowler-practical-test-pyramid]])
- **TDD is primarily a design practice** — the red phase forces interface and dependency decisions before implementation; the refactor phase drives SOLID compliance emergently (Source: [[sources/fowler-practical-test-pyramid]])
- **BDD bridges the specification gap** — Gherkin scenarios authored by the Three Amigos (PO + Dev + Tester) become executable acceptance tests, eliminating the "requirements telephone" problem
- **Equivalence Partitioning + BVA reduce test volume without losing coverage** — EP identifies partitions; BVA sharpens test values at boundaries where defects cluster
- **Mutation testing measures test sensitivity** — coverage metrics only confirm code was executed, not that tests would catch defects; mutation score reveals this gap
- **Contract testing replaces E2E tests in microservice architectures** — Consumer-Driven Contracts (CDC) let services deploy independently without integration regressions (Source: [[sources/fowler-practical-test-pyramid]])
- **Shift-left reduces defect cost** — the later a defect is found (unit → integration → system → production), the more expensive it is to fix; early automated testing is the primary cost lever

---

## Key Entities

- **Mike Cohn** — originated the Testing Pyramid in *Succeeding with Agile* (2009)
- **Kent Beck** — popularised TDD as part of Extreme Programming (XP); *Test-Driven Development: By Example* (2002)
- **Dan North** — introduced BDD (2006) as an evolution of TDD to improve stakeholder communication
- **Martin Fowler / Ham Vocke** — formalised the Practical Test Pyramid on martinfowler.com
- **ISTQB** — International Software Testing Qualifications Board; maintains the CTFL v4.0 (2024) global certification standard

---

## Key Concepts

- [[concepts/software-testing-fundamentals]] — four levels, seven principles, pyramid, static/dynamic, black/white box
- [[concepts/test-driven-development]] — TDD (Red-Green-Refactor), BDD (Gherkin, Three Amigos), tools
- [[concepts/test-design-techniques]] — EP, BVA, statement/branch/path coverage, mutation testing

---

## Connections to Existing Wiki

| Existing Concept | Testing Connection |
|-----------------|-------------------|
| [[concepts/scrum-framework]] | Definition of Done includes passing tests; shift-left aligns with Sprint cadence; BDD Three Amigos mirrors Sprint refinement |
| [[concepts/software-design-process]] | TDD drives emergent design; testability is a design quality metric |
| [[concepts/solid-and-design-patterns]] | SOLID principles improve testability; DIP enables dependency injection needed for unit testing |
| [[concepts/requirements-engineering]] | BDD scenarios are executable specifications; acceptance tests operationalise BCIC requirements |
| [[concepts/owasp-top-10]] | DAST is dynamic black-box security testing; fuzzing targets injection (A03) |
| [[synthesis/web-security-ssdlc-bridge]] | SAST = static testing of code; DAST = dynamic security testing; penetration testing = system-level black-box |

---

## Contradictions

- [[sources/fowler-practical-test-pyramid]] advocates minimising E2E tests. Some teams argue contract testing is only viable at scale with mature API boundaries. For small monolithic systems, a broader integration test layer may be more practical than Consumer-Driven Contracts.

---

## Open Questions

- What is the optimal mutation score threshold for a production codebase? Published guidance varies; no single authoritative benchmark exists.
- How does testing strategy change for AI/ML models where outputs are probabilistic rather than deterministic?
- How do organisations implement the Testing Pyramid when significant portions of the system are third-party integrations (legacy APIs, SaaS)?

---

## Sources

- [[sources/istqb-ctfl-v4]]: ISTQB, 2024
- [[sources/fowler-practical-test-pyramid]]: Ham Vocke / Martin Fowler, martinfowler.com
