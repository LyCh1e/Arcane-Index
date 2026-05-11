---
type: concept
title: "Propositional Logic"
domain: mathematics
course: INF1003
complexity: medium
tags: [logic, propositional-logic, truth-tables, de-morgan, logical-equivalence]
updated: 2026-05-11
---

# Propositional Logic

Propositional logic (propositional calculus) studies true/false statements and their combinations using logical connectives. It is foundational to digital circuits, programming language semantics, and formal verification.

---

## Propositions

A **proposition** is a declarative statement that is either true ($\top$) or false ($\bot$) — never both, never neither.

- "2 + 2 = 4" → proposition (true)
- "Singapore is in China" → proposition (false)
- "How old are you?" → **not** a proposition (a question has no truth value)

Propositional variables are conventionally written $p, q, r, s$.

---

## Logical Connectives

| Symbol | Name | Read as | True when |
|--------|------|---------|-----------|
| $\neg p$ | Negation | "not $p$" | $p$ is false |
| $p \wedge q$ | Conjunction | "$p$ and $q$" | both $p$ and $q$ are true |
| $p \vee q$ | Disjunction | "$p$ or $q$" | at least one is true |
| $p \oplus q$ | Exclusive OR | "$p$ xor $q$" | exactly one is true |
| $p \to q$ | Conditional | "if $p$ then $q$" | not ($p$ true and $q$ false) |
| $p \leftrightarrow q$ | Biconditional | "$p$ iff $q$" | $p$ and $q$ have the same truth value |

### The Conditional $p \to q$

The most commonly misunderstood connective. It is **only false** when $p$ is true and $q$ is false.

| $p$ | $q$ | $p \to q$ |
|:---:|:---:|:---------:|
| F | F | **T** (vacuously true) |
| F | T | **T** (vacuously true) |
| T | F | **F** |
| T | T | **T** |

**Key insight:** When the premise $p$ is false, the implication is vacuously true — a false hypothesis can imply anything.

**Alternative phrasings of $p \to q$:**
- "$p$ only if $q$"
- "$q$ whenever $p$"
- "$p$ is sufficient for $q$"
- "$q$ is necessary for $p$"

### Converse, Contrapositive, Inverse

For $p \to q$:

| Variant | Form | Equivalent to |
|---------|------|---------------|
| Original | $p \to q$ | itself |
| **Contrapositive** | $\neg q \to \neg p$ | **$p \to q$** ← same truth table |
| Converse | $q \to p$ | inverse |
| Inverse | $\neg p \to \neg q$ | converse |

Only the **contrapositive** is logically equivalent to the original.

---

## Tautologies and Contradictions

- **Tautology:** Always true, regardless of variable assignments. Example: $p \vee \neg p$.
- **Contradiction:** Always false. Example: $p \wedge \neg p$.
- **Contingency:** Neither — truth depends on variable values.

---

## Logical Equivalence Laws

Two propositions are **logically equivalent** ($p \equiv q$) if they have identical truth tables.

| Law | Conjunction | Disjunction |
|-----|-------------|-------------|
| Identity | $p \wedge \top \equiv p$ | $p \vee \bot \equiv p$ |
| Domination | $p \wedge \bot \equiv \bot$ | $p \vee \top \equiv \top$ |
| Idempotent | $p \wedge p \equiv p$ | $p \vee p \equiv p$ |
| Double Negation | $\neg(\neg p) \equiv p$ | — |
| Commutative | $p \wedge q \equiv q \wedge p$ | $p \vee q \equiv q \vee p$ |
| Associative | $(p \wedge q) \wedge r \equiv p \wedge (q \wedge r)$ | similarly |
| Distributive | $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$ | similarly |
| **De Morgan's** | $\neg(p \wedge q) \equiv \neg p \vee \neg q$ | $\neg(p \vee q) \equiv \neg p \wedge \neg q$ |

### Key Derived Equivalences

$$p \to q \equiv \neg p \vee q$$
$$p \leftrightarrow q \equiv (p \to q) \wedge (q \to p)$$

**De Morgan's laws** are especially important: negation distributes over $\wedge$ and $\vee$ but flips the connective. Used extensively in both logic proofs and programming (e.g. negating an `if` condition).

---

## Logic Gates

Each connective corresponds directly to a digital logic gate:

| Gate | Connective |
|------|------------|
| NOT | $\neg$ |
| AND | $\wedge$ |
| OR | $\vee$ |
| XOR | $\oplus$ |
| NAND | $\neg(p \wedge q)$ |
| NOR | $\neg(p \vee q)$ |

---

## Related Pages

- [[predicate-logic-and-proofs]] — extends propositional logic with quantifiers and inference rules
- [[discrete-mathematics-foundations]] — sequences and number theory (same course)
- [[sets-functions-relations]] — set identities mirror logical equivalence laws
