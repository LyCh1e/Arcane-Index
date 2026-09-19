---
type: concept
status: established
created: 2026-09-19
updated: 2026-09-19
name: test-doubles-and-dependency-injection
description: Dependencies, coupling and test scope; parameter/constructor/property/container injection; the test-double roles (dummy, stub, fake, mock) and how Moq plays stub or mock depending on the assertion; drivers vs stubs in integration testing
metadata:
  type: concept
  domain: software-engineering
  course: ICT3112
  tags: [dependency-injection, test-doubles, moq, mock, stub, fake, driver, integration-testing, unit-testing, coupling, csharp]
---

# Test doubles and dependency injection

Worked example: [[examples/ict3112-lab3-ci-and-dependencies]]. Related: [[concepts/test-driven-development]], [[concepts/github-actions-cicd]], [[concepts/solid-and-design-patterns]] (dependency inversion).

## The core idea

A **dependency** is anything code needs to do its work: other classes, libraries, but also the **file system, databases, web services, clocks, RNGs, queues**. If a method does `new FileReader()` internally it is **tightly coupled** — the caller can choose *inputs* but not *how the collaborator behaves*, so the logic cannot be tested without the real resource.

**Test scope follows from which dependency is real:**

| Test scope | Dependency | What it can establish |
|---|---|---|
| Unit | controlled test double | the logic reacts correctly to *known* dependency behaviour |
| Integration | real component + real resource | the components work *together* in this environment |

Keep **both** even when input values overlap — different evidence, different failure localisation.

## Injection forms

| Form | Trade-off |
|---|---|
| Method/parameter | simple, explicit; changes the signature (all callers break at compile time — useful feedback) |
| Constructor | most common for *required* collaborators; object can't exist without them (Reqnroll context injection uses this) |
| Property | for optional dependencies; allows a half-configured object |
| DI container (`Microsoft.Extensions.DependencyInjection`) | container builds the object graph; beyond a first lab |

An interface is not mandatory for DI, but it is the contract that lets one implementation replace another.

## Test-double roles (a role in a test, not a library feature)

| Double | Purpose |
|---|---|
| Dummy | fills a required parameter, unused by the behaviour under test |
| Stub | returns predetermined data → controls an **indirect input** |
| Fake | simplified *working* implementation (in-memory repository instead of a DB) |
| Mock | records interactions → test **verifies** an expected call happened |

**Moq's `Mock<T>` is not "a mock" by name.** The same object is a *stub* when you `Setup(...).Returns(...)` and assert only the result, and a *mock* when you `Verify(..., Times.Once())`. The role is decided by what the test asserts.

## Drivers vs stubs (integration order)

- **Driver** — stand-in for a missing **caller**; invokes the lower component (bottom-up integration).
- **Stub** — stand-in for a missing **called** component; supplies the responses the upper component needs (top-down).
- Modern alternative: start real dependencies in test containers — stronger evidence, slower, more complex.

## Practical rules

- Add Moq to the **test project only**, never production code.
- Null-guard the injected dependency (`ArgumentNullException.ThrowIfNull`).
- One result assertion *or* one interaction verification per focused test.
- Don't over-verify interactions: asserting *how* code calls a collaborator couples the test to the implementation.
