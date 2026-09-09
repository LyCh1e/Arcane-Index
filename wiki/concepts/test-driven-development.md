---
type: concept
title: "Test-Driven Development (TDD) and Behaviour-Driven Development (BDD)"
domain: software-engineering
complexity: high
status: established
created: 2026-05-21
updated: 2026-08-31
tags: [tdd, bdd, test-driven-development, behaviour-driven-development, red-green-refactor, gherkin, unit-testing, design, agile]
---

# Test-Driven Development (TDD) and Behaviour-Driven Development (BDD)

TDD and BDD are development practices that use tests to drive design. They differ in scope: TDD operates at the code level and guides implementation; BDD operates at the behaviour level and drives collaboration between technical and non-technical stakeholders.

---

## Test-Driven Development (TDD)

### Core Idea

Write a failing test before writing any production code. The test defines what the code must do. Implementation is driven by the tests, not the other way around.

Popularised by Kent Beck as part of Extreme Programming (XP); described in *Test-Driven Development: By Example* (2002).

### The Red-Green-Refactor Cycle

```
  ┌──────────────────────────────────────────────────────┐
  │                                                      │
  │   1. RED  → Write a small failing test               │
  │      ↓                                               │
  │   2. GREEN → Write the minimum code to pass it       │
  │      ↓                                               │
  │   3. REFACTOR → Clean up; all tests must still pass  │
  │      ↓                                               │
  │   (repeat for the next behaviour)                    │
  │                                                      │
  └──────────────────────────────────────────────────────┘
```

| Phase | Goal | Rule |
|-------|------|------|
| **Red** | Confirm the test harness works; define the expected behaviour | The test must fail for the right reason |
| **Green** | Make the test pass | Write the *minimum* code; no more |
| **Refactor** | Improve code quality | Do not add new behaviour; all tests must stay green |

### Why TDD Is a Design Activity

Writing the test first forces the developer to think about:
- The public interface of the unit (what inputs/outputs)
- Dependencies (which must be injected or stubbed)
- The contract the unit must fulfil

Tightly coupled, hard-to-test code surfaces immediately. The pain of writing the test is a signal to improve the design.

### Rules for Good TDD Tests

- **Test observable behaviour, not implementation details** — if refactoring breaks tests without changing behaviour, the tests are too coupled to internals
- **Arrange-Act-Assert (AAA)** — set up state (Arrange), execute the unit under test (Act), verify the outcome (Assert)
- **One logical assertion per test** — a test that asserts one thing produces clear failure messages
- **Tests must be deterministic** — randomness, real clocks, and network calls must be replaced with test doubles
- **Do not test trivial code** — skip getters and setters; focus on logic

### When Not to Use TDD

- Exploratory spikes where requirements are unknown
- UI layouts driven by visual feedback
- Highly algorithmic code where the algorithm itself must be researched before its contract is stable

> [!gap] Empirical evidence on TDD's defect reduction rate varies across studies. A commonly cited figure is 40–90% defect reduction vs. no TDD, but study conditions differ significantly.

---

## Behaviour-Driven Development (BDD)

### Core Idea

BDD extends TDD by using business-readable language to express test scenarios. Where TDD tests are written by and for developers, BDD scenarios are co-authored by product owners, developers, and testers in a shared language. The test suite becomes living documentation.

Introduced by Dan North (2006) as a response to TDD's developer-centricity.

### Gherkin and Given-When-Then

Gherkin is the domain-specific language used in BDD frameworks (Cucumber, SpecFlow, Behave). Scenarios follow the **Given-When-Then** structure:

```gherkin
Feature: Sprint completion

  Scenario: Sprint ends when the timebox expires
    Given a Sprint was started on 2026-05-01 with a two-week duration
    When the date reaches 2026-05-15
    Then the Sprint Review should be scheduled
    And the Sprint Backlog is closed to new items
```

| Keyword | Meaning |
|---------|---------|
| **Given** | System state / preconditions before the action |
| **When** | The action or event under test |
| **Then** | The expected observable outcome |
| **And / But** | Additional conditions chained to the above |

### The Three Amigos

BDD scenarios are produced collaboratively in a **Three Amigos** session:

| Role | Contribution |
|------|-------------|
| **Product Owner** | Defines the business need and acceptance criteria |
| **Developer** | Confirms technical feasibility and identifies edge cases |
| **Tester** | Challenges scenarios, adds negative cases, flags ambiguities |

The output is a set of Gherkin scenarios agreed by all three before implementation begins.

### BDD Tools

| Tool | Language | Framework |
|------|----------|-----------|
| Cucumber | JVM (Java, Kotlin), JS, Ruby | Gherkin-native |
| **Reqnroll** | C# / .NET | Gherkin-native; the maintained successor to SpecFlow (SpecFlow retired 2024) |
| SpecFlow | C# / .NET | Gherkin-native; **deprecated** — projects migrate to Reqnroll |
| Behave | Python | Gherkin-native |
| Robot Framework | Python | Keyword-driven (similar to BDD) |

---

## Reqnroll mechanics (C# / .NET)

Practical points from a worked lab ([[examples/ict3112-lab2-reqnroll-bdd]]):

- **Project shape.** `dotnet new install Reqnroll.Templates.DotNet`, then
  `dotnet new reqnroll-project -t nunit -f net10.0`. A **separate** acceptance-test project keeps
  readable scenarios apart from focused unit tests; it holds one `ProjectReference` to the app.
  Do not hand-pin package versions — the template selects a compatible Reqnroll/NUnit/adapter set.
- **Step definition = binding.** A `[Given]`/`[When]`/`[Then]` method whose **attribute text**
  (not the method or file name) matches the Gherkin step. Matching is **project-wide** — the same
  step text defined in two classes is an *ambiguous binding* error. Put shared wording in one class.
- **Cucumber Expressions.** `{int}`, `{long}`, `{double}`, `{string}`, `{word}` placeholders in the
  binding text are converted to typed method arguments.
- **Scenario Outline vs step data table.** An `Examples:` table belongs to a Scenario Outline and
  produces **one test per row**. A step **data table** is a single `DataTable` argument to **one
  step** — the scenario still runs once. Different tools for different jobs.
- **Tags → categories.** `@Foo` on a Feature/Scenario becomes NUnit `TestCategory=Foo`; run with
  `dotnet test --filter "TestCategory=Foo"` (drop the `@`). `@ignore` skips a scenario. Always
  finish a focused run with the complete suite; zero executed tests is not a pass.
- **Context injection.** Instead of `static` fields or globals, define plain C# context classes and
  request them in each binding's **constructor**. Reqnroll supplies the **same instance to every
  binding within one scenario** and a fresh instance for the next — shared state, safely scoped, so
  parallel/reordered scenarios cannot leak into each other.
- **Rejection as behaviour.** When "the operation is rejected" is an observable requirement, catch
  the expected exception in the `When` binding and assert it in `Then`. The scenario still describes
  the outcome in domain language; the exception type stays out of the Gherkin.

### Planning hierarchy — no universal 1:1 mapping

Epic → product Feature → User Story → acceptance criteria/rules → Gherkin Scenarios → executable
acceptance tests. One Feature may span several Stories; one Story usually needs several Scenarios
(normal / alternative / boundary / rejected). A `.feature` file is a readable home for related
scenarios, **not** a mirror of one Story. A *product Feature* (a planning capability) is distinct
from a *Gherkin Feature* (the `.feature` document keyword).

---

## TDD vs BDD — Comparison

| Dimension | TDD | BDD |
|-----------|-----|-----|
| Written by | Developers | Developers + Product Owners + Testers |
| Language | Code (assertions) | Natural language (Gherkin) |
| Scope | Individual unit / class | Feature / user journey |
| Audience | Technical team | Whole team including business |
| Output | Fast unit tests | Living documentation + acceptance tests |
| Starting point | "Does this function work?" | "Does the system behave as the business expects?" |

**They are complementary, not competing.** TDD drives the unit layer of the pyramid; BDD drives the integration and acceptance layers.

---

## Key Connections

- [[concepts/software-testing-fundamentals]] — TDD/BDD populate the lower layers of the Testing Pyramid; BDD scenarios become acceptance tests
- [[concepts/scrum-framework]] — BDD "Three Amigos" maps naturally to Sprint Backlog refinement; Definition of Done may require passing BDD scenarios
- [[concepts/software-design-process]] — TDD is a design practice as much as a testing practice; drives emergent design through refactoring
- [[concepts/solid-and-design-patterns]] — well-designed, SOLID-compliant code is easier to unit-test; TDD enforces dependency injection (DIP)
- [[concepts/requirements-engineering]] — BDD scenarios are a form of executable specification; they bridge the gap between requirements (SRS) and code
- [[examples/ict3112-lab1-nunit-tdd-calculator]] — worked example: C#/NUnit calculator, a full red-green-refactor cycle on `Divide`, AAA, parameterised tests, boundary values
- [[examples/ict3112-lab2-reqnroll-bdd]] — worked example: adding a Reqnroll acceptance project to that calculator — Cucumber Expressions, scenario outlines, step data tables, tags, context injection
