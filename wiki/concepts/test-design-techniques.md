---
type: concept
title: "Test Design Techniques"
domain: software-engineering
complexity: high
status: established
created: 2026-05-21
updated: 2026-05-21
tags: [test-design, equivalence-partitioning, boundary-value-analysis, black-box-testing, white-box-testing, statement-coverage, branch-coverage, mutation-testing, software-testing]
---

# Test Design Techniques

Test design techniques are systematic methods for deriving test cases from specifications (black-box) or source code (white-box). Without them, test design is ad hoc and leaves predictable defect classes undetected.

---

## Black-Box (Specification-Based) Techniques

Black-box techniques derive test cases from the requirement or specification, without knowledge of how the code is implemented.

### Equivalence Partitioning (EP)

**Principle**: divide the input domain into classes (partitions) where all values in a class are expected to behave identically. Test one representative value per class.

**Why it works**: if one value in a partition fails, all values in that partition should fail; testing every single value gives no extra confidence.

**Partitions include**:
- Valid partitions (the system should accept and process correctly)
- Invalid partitions (the system should reject gracefully)

**Example — a form field that accepts age 18–65**:

| Partition | Range | Representative value |
|-----------|-------|---------------------|
| Below valid | < 18 | 10 |
| Valid | 18–65 | 40 |
| Above valid | > 65 | 80 |
| Invalid type | Non-integer | "abc" |

**Minimum test set**: one test per partition = 4 tests.

### Boundary Value Analysis (BVA)

**Principle**: defects cluster at the edges of input ranges. Test the values *at* and *just outside* each boundary.

BVA is applied *on top of* equivalence partitioning — at the boundary between two adjacent partitions.

**For the age example (18–65)**:

| Boundary point | Value to test |
|---------------|--------------|
| Just below lower bound | 17 |
| At lower bound | 18 |
| Just above lower bound | 19 |
| Just below upper bound | 64 |
| At upper bound | 65 |
| Just above upper bound | 66 |

**Combining EP + BVA**: EP selects partitions; BVA sharpens the test values within and at the edges of those partitions.

### Decision Table Testing

For systems with complex combinations of conditions, a decision table maps every combination of conditions to the correct action. Tests are derived — one column per rule.

### State Transition Testing

For systems with defined states and transitions (finite state machines), test every valid transition and attempt invalid transitions. Common in protocol testing, UI flows, and embedded systems.

---

## White-Box (Structure-Based) Techniques

White-box techniques derive test cases from the internal structure of the code. They measure **coverage** — the proportion of structural elements exercised by the test suite.

### Statement Coverage

Ensures every executable statement is executed at least once.

```
Coverage = (Statements executed) / (Total executable statements) × 100%
```

**Limitation**: a test suite with 100% statement coverage may still miss branches. A single test that flows through all statements once achieves 100% statement coverage but does not test alternative paths.

### Branch Coverage (Decision Coverage)

Ensures every branch outcome (true/false for each condition) is taken at least once. **Subsumes** statement coverage — 100% branch coverage implies 100% statement coverage.

```python
if x > 0:      # Branch 1: x > 0 (True)
    y = x      # Branch 2: x > 0 (False)
else:
    y = -x
```

A test suite needs at least one test where `x > 0` and one where `x ≤ 0` to achieve branch coverage.

### Condition Coverage

Ensures every individual boolean sub-expression in a compound condition takes both true and false values. Stronger than branch coverage for complex conditions like `if (A and B)`.

### Path Coverage

Ensures every distinct path through the code is executed. The most comprehensive but often impractical: cyclomatic complexity grows exponentially with nested conditions and loops. Used selectively in safety-critical code.

**McCabe Cyclomatic Complexity (V(G))** quantifies the number of independent paths:
```
V(G) = Edges − Nodes + 2
```
High cyclomatic complexity → many paths → hard to test → refactor first.

### Mutation Testing

**Principle**: artificially introduce small defects (mutations) into the code and verify that the test suite detects them.

**Common mutation operators**:
- Arithmetic operator replacement: `+` → `-`
- Relational operator replacement: `>` → `>=`
- Statement deletion: remove a line

**Metrics**:
- **Mutation score** = (mutants killed by tests) / (total mutants) × 100%
- A high mutation score indicates the test suite is sensitive to defects
- **Surviving mutants** reveal test gaps

> [!gap] Mutation testing is computationally expensive at scale. Tools (PIT for Java, mutmut for Python) make it feasible but it is rarely run in every CI cycle — typically used periodically or on critical modules.

---

## Coverage as a Quality Metric

| Coverage Type | Subsumes | Industry Typical Target |
|--------------|----------|------------------------|
| Statement | — | 80–90% |
| Branch | Statement | 70–80% |
| Condition | — | project-specific |
| Path | Branch | Safety-critical only |
| Mutation score | — | 60–80% (high effort) |

**Coverage is necessary but not sufficient.** 100% branch coverage does not guarantee correctness — it only confirms the covered paths were exercised. Tests can pass with 100% coverage and still miss semantic defects if assertions are weak.

---

## Key Connections

- [[concepts/software-testing-fundamentals]] — these techniques populate the black-box (system/acceptance layer) and white-box (unit layer) positions in the Testing Pyramid
- [[concepts/test-driven-development]] — TDD implicitly drives toward high branch coverage as each Red cycle adds a test for a new behaviour
- [[concepts/algorithm-complexity]] — McCabe's cyclomatic complexity connects directly to algorithm control flow analysis; high complexity demands more test paths
- [[concepts/secure-software-requirements]] — equivalence partitioning and BVA are used in security testing to probe boundary inputs for injection and overflow vulnerabilities
- [[concepts/owasp-top-10]] — fuzzing (random input generation) is a black-box technique that aggressively targets input validation (OWASP A03: Injection)
