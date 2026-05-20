---
type: source-index
title: "The Practical Test Pyramid — Martin Fowler"
domain: software-engineering
authors: [Ham Vocke, Martin Fowler]
ingested: 2026-05-21
source: "https://martinfowler.com/articles/practical-test-pyramid.html"
topics: [testing-pyramid, unit-testing, integration-testing, contract-testing, end-to-end-testing, TDD, CI/CD]
status: established
created: 2026-05-21
updated: 2026-05-21
tags: [source, software-testing, testing-pyramid, martin-fowler]
---

# The Practical Test Pyramid — Martin Fowler / Ham Vocke

An authoritative article on martinfowler.com detailing the Test Pyramid, written by Ham Vocke and published under Fowler's editorial umbrella. Expands Mike Cohn's original pyramid concept (from *Succeeding with Agile*, 2009) with concrete implementation guidance.

---

## Key Claims

- **Pyramid structure**: write many unit tests, some integration tests, few end-to-end tests
- **"Push tests down"**: if a lower-level test provides the same confidence as a higher-level one, delete the higher-level one
- **Anti-pattern — Ice Cream Cone**: over-investing in UI/E2E tests; produces slow, brittle, expensive pipelines
- **Anti-pattern — Hourglass**: thin middle (integration) layer; common when teams skip service/API layer tests
- **Unit under test**: a "unit" is context-dependent — a single function, a class, or a cohesive module; the key is isolation
- **Contract testing (CDC)**: Consumer-Driven Contracts enable independent deployment in microservice architectures
- **E2E tests are "notoriously flaky"**: minimise to only critical user journeys; prefer contract tests over E2E where possible
- **TDD**: framed as "potentially beneficial but no silver bullet"; value comes from continuous delivery pipelines, not the test methodology alone

---

## Key Concepts Extracted

| Concept | Covered In |
|---------|-----------|
| Testing Pyramid structure and proportions | [[concepts/software-testing-fundamentals]] |
| Ice cream cone and hourglass anti-patterns | [[concepts/software-testing-fundamentals]] |
| Contract testing (CDC) | [[concepts/software-testing-fundamentals]] |
| Arrange-Act-Assert unit test structure | [[concepts/test-driven-development]] |
