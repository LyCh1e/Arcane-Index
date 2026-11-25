---
type: concept
title: "Probability Theory"
domain: mathematics
course: INF1004
complexity: medium
address: c-000020
tags: [probability, bayes, conditional-probability, independence]
updated: 2026-05-11
status: established
created: 2026-05-11
---

# Probability Theory

Probability theory provides the mathematical framework for quantifying **uncertainty**. It acts as the bridge between descriptive statistics (describing observed data) and inferential statistics (drawing conclusions about populations).

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Sample space S** | The set of all possible outcomes of a random experiment |
| **Event A** | A subset of S — the outcomes we are interested in |
| **P(S)** | Always equals 1 |
| **P(A)** | Probability that event A occurs; 0 ≤ P(A) ≤ 1 |

Visualised using **Venn diagrams** (rectangle = S, circles = events).

---

## Interpretations of Probability

### Classical (Objective) Probability

Assumes all outcomes are equally likely:
$$P(A) = \frac{\text{Number of outcomes in A}}{\text{Total number of possible outcomes}}$$

> Limitation: not practical when outcomes are not equally likely.

### Frequency (Empirical) Probability

Based on observed data from repeated experiments:
$$P(A) = \frac{\text{Number of times A occurred}}{\text{Total number of trials}}$$

### Subjective Probability

Based on personal judgement or expert opinion (e.g., "70% chance of rain tomorrow").

---

## Single-Event Rules

| Rule | Formula |
|------|---------|
| Complement | $P(\bar{A}) = 1 - P(A)$ |
| Union | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Mutually exclusive union | $P(A \cup B) = P(A) + P(B)$ when $P(A \cap B) = 0$ |

---

## Conditional Probability

The probability of A occurring **given** that B has already occurred:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Note: $P(A \mid B) \neq P(B \mid A)$ in general.

**Tree diagrams** represent successive conditional events:
- Multiply probabilities along branches to get the probability of a sequence of events.
- Each set of branches from a node sums to 1.

---

## Independence vs Mutual Exclusivity

### Independent Events

Knowing B occurred does **not** change the probability of A:
$$P(A \mid B) = P(A) \quad \Longleftrightarrow \quad P(A \cap B) = P(A) \times P(B)$$

- Sampling **with replacement** → independent events.
- Sampling **without replacement** → dependent events.

### Mutually Exclusive Events

A and B cannot both occur:
$$P(A \cap B) = 0$$

> **Critical distinction:** Mutually exclusive events with non-zero probabilities are **dependent** — the occurrence of one guarantees the non-occurrence of the other. Independent ≠ Mutually exclusive.

---

## Law of Total Probability

For mutually exclusive and exhaustive events $B_1, B_2, \ldots, B_k$ (they partition S):

$$P(A) = \sum_{i=1}^{k} P(A \mid B_i)\, P(B_i)$$

---

## Bayes' Theorem

Reverses conditional probability — given A occurred, what is the probability it came from partition $B_i$?

$$P(B_i \mid A) = \frac{P(A \mid B_i)\, P(B_i)}{P(A)}$$

### Classic Example — Medical Testing

- 1% of population is allergic to cats: P(C) = 0.01
- Test sensitivity (true positive rate): P(T | C) = 0.80
- False positive rate: P(T | C̄) = 0.10

$$P(T) = P(T \mid C)\,P(C) + P(T \mid \bar{C})\,P(\bar{C}) = (0.80)(0.01) + (0.10)(0.99) = 0.107$$

$$P(C \mid T) = \frac{(0.80)(0.01)}{0.107} \approx 0.075 = 7.5\%$$

A positive test result still only corresponds to a 7.5% probability of actually having the allergy — because the base rate is very low. This is the **base-rate fallacy** if ignored.

---

## Probability Rules — Summary

| Rule | Formula |
|------|---------|
| Complement | $P(\bar{A}) = 1 - P(A)$ |
| Addition | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Mutually exclusive | $P(A \cup B) = P(A) + P(B)$ |
| Conditional | $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ |
| Independence | $P(A \cap B) = P(A)\,P(B)$ |
| Bayes' theorem | $P(B_i \mid A) = \frac{P(A \mid B_i)\,P(B_i)}{P(A)}$ |

---

## Related Concepts

- [[descriptive-statistics]] — context for why probability matters
- [[probability-distributions]] — applying probability to named distributions
- [[combinatorics]] — counting methods used in classical probability
- [[predicate-logic-and-proofs]] — formal reasoning that underpins probability logic
