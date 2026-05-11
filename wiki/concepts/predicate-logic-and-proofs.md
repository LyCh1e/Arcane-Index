---
type: concept
title: "Predicate Logic & Proof Methods"
domain: mathematics
course: INF1003
complexity: high
tags: [predicate-logic, quantifiers, rules-of-inference, proof-methods, modus-ponens]
updated: 2026-05-11
---

# Predicate Logic & Proof Methods

Predicate logic extends [[propositional-logic]] by adding **predicates** (properties of objects) and **quantifiers** (statements over ranges of objects). Proof methods provide the systematic tools to establish mathematical truths.

---

## Predicates

A **predicate** $P(x)$ is a property that variable $x$ may or may not have. It becomes a proposition once $x$ is assigned a value from a **domain**.

**Example:** Let $P(x)$ denote "$x > 0$" with domain $\mathbb{Z}$:
- $P(-3)$ → False
- $P(3)$ → True

Predicates may have multiple variables: $\text{Speaks}(s, l)$ = "student $s$ speaks language $l$".

---

## Quantifiers

### Universal Quantifier ($\forall$)

$\forall x\, P(x)$ — "for **all** $x$, $P(x)$ holds" — true only if $P(x)$ is true for every element in the domain.

### Existential Quantifier ($\exists$)

$\exists x\, P(x)$ — "there **exists** an $x$ such that $P(x)$" — true if $P(x)$ holds for at least one element.

### Negation of Quantifiers (De Morgan's for Predicate Logic)

| Statement | Equivalent negation |
|-----------|---------------------|
| $\neg \forall x\, P(x)$ | $\exists x\, \neg P(x)$ |
| $\neg \exists x\, P(x)$ | $\forall x\, \neg P(x)$ |

**Intuition:** To disprove "all birds can fly", find one that cannot. To disprove "some bird is immortal", show none are.

### Common Translation Patterns

| English | Predicate Logic |
|---------|-----------------|
| All humans are mortal | $\forall x\,(H(x) \to M(x))$ |
| Some students study hard | $\exists x\,(S(x) \wedge H(x))$ |
| No student fails | $\forall x\,(S(x) \to \neg F(x))$ |
| Not all birds can fly | $\exists x\,(B(x) \wedge \neg F(x))$ |

---

## Rules of Inference

Rules of inference are valid argument forms used as steps in formal proofs.

### Propositional Inference Rules

| Rule | Premises | Conclusion |
|------|----------|------------|
| **Modus Ponens** | $p$; $p \to q$ | $q$ |
| **Modus Tollens** | $\neg q$; $p \to q$ | $\neg p$ |
| **Hypothetical Syllogism** | $p \to q$; $q \to r$ | $p \to r$ |
| **Disjunctive Syllogism** | $p \vee q$; $\neg p$ | $q$ |
| **Addition** | $p$ | $p \vee q$ |
| **Simplification** | $p \wedge q$ | $p$ |
| **Conjunction** | $p$; $q$ | $p \wedge q$ |
| **Resolution** | $p \vee q$; $\neg p \vee r$ | $q \vee r$ |

**Modus Ponens** is the fundamental rule — if you know $p$ is true and $p$ implies $q$, then $q$ must be true.

### Quantifier Inference Rules

| Rule | Form |
|------|------|
| Universal Instantiation | $\forall x\,P(x) \;\therefore P(c)$ for any specific $c$ |
| Universal Generalisation | $P(c)$ for arbitrary $c \;\therefore \forall x\,P(x)$ |
| Existential Instantiation | $\exists x\,P(x) \;\therefore P(c)$ for some element $c$ |
| Existential Generalisation | $P(c)$ for some $c \;\therefore \exists x\,P(x)$ |

---

## Proof Methods

### Direct Proof

Assume $p$ is true; use inference rules and logical steps to derive $q$.

**Example:** Prove "if $n$ is odd, then $n^2$ is odd."
1. Assume $n = 2k + 1$ for some integer $k$.
2. Then $n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$.
3. This has the form $2r + 1$, so $n^2$ is odd. $\blacksquare$

### Proof by Contraposition

Prove $\neg q \to \neg p$ instead of $p \to q$ (they are logically equivalent — see [[propositional-logic]]).

**Use when:** Assuming $\neg q$ gives something more tractable to work with than assuming $p$.

**Example:** Prove "if $n^2$ is even, then $n$ is even."
*Contrapositive:* "if $n$ is odd, then $n^2$ is odd" — proved directly above. $\blacksquare$

### Proof by Contradiction

Assume $\neg p$ is true and derive a contradiction (a known falsehood). Since $\neg p$ leads to a contradiction, $p$ must be true.

**Classic example:** Prove $\sqrt{2}$ is irrational.
1. Assume $\sqrt{2} = a/b$ with $\gcd(a, b) = 1$.
2. Then $2b^2 = a^2$, so $a$ is even. Write $a = 2c$.
3. Then $2b^2 = 4c^2$, so $b^2 = 2c^2$, meaning $b$ is even.
4. But then $\gcd(a, b) \geq 2$ — contradiction. $\blacksquare$

### Proof by Cases

Split the domain into exhaustive, non-overlapping cases and prove the statement holds in each.

**Example:** Prove $n^2 \geq n$ for all integers $n$.
- Case $n \geq 1$: $n^2 \geq n \cdot 1 = n$. ✓
- Case $n = 0$: $0 \geq 0$. ✓
- Case $n \leq -1$: $n^2 \geq 1 > 0 \geq n$. ✓

### Counterexample

To **disprove** $\forall x\,P(x)$, exhibit one value for which $P(x)$ is false.

### Choosing a Proof Method

| Goal | Recommended method |
|------|--------------------|
| Prove $p \to q$ (hypothesis usable directly) | Direct proof |
| Prove $p \to q$ (conclusion negation easier) | Contraposition |
| Prove $p$ is true | Contradiction |
| Disprove $\forall x\,P(x)$ | Counterexample |
| Statement holds for several distinct cases | Proof by cases |

---

## Related Pages

- [[propositional-logic]] — connectives and equivalences that underpin inference rules
- [[sets-functions-relations]] — sets, where many of these proof techniques are applied
- [[discrete-mathematics-foundations]] — number theory proofs (odd/even, primes) use these methods
