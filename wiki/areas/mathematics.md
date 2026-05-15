---
type: area
title: "Mathematics"
domain: mathematics
sources: [[[sources/INF1003-mathematics-1]], [[sources/INF1004-mathematics-2]]]
updated: 2026-05-14
tags: [area, mathematics]
---

# Mathematics

**Sources**: INF1003 (Mathematics 1 — discrete maths, logic, combinatorics) and INF1004 (Mathematics 2 — statistics, probability, linear algebra), SIT.

---

## What I Know

Two modules cover the mathematical foundations of computing. INF1003 focuses on discrete mathematics (logic, sets, proofs, combinatorics). INF1004 focuses on continuous mathematics for data science and ML (statistics, probability distributions, linear algebra, SVD).

---

## Concept Pages

| Page | Source | What It Covers |
|------|--------|---------------|
| [[concepts/discrete-mathematics-foundations\|Discrete Mathematics Foundations]] | INF1003 | Number systems, sequences, recurrences, graph theory basics |
| [[concepts/combinatorics\|Combinatorics]] | INF1003 | Permutations, combinations, binomial theorem, pigeonhole principle |
| [[concepts/propositional-logic\|Propositional Logic]] | INF1003 | Connectives, truth tables, logical equivalences, CNF/DNF |
| [[concepts/predicate-logic-and-proofs\|Predicate Logic & Proof Methods]] | INF1003 | Quantifiers, proof by contradiction/induction/contrapositive |
| [[concepts/sets-functions-relations\|Sets, Functions & Relations]] | INF1003 | Set operations, function types, equivalence/partial-order relations |
| [[concepts/descriptive-statistics\|Descriptive Statistics]] | INF1004 | Mean/median/mode, variance/std dev, quartiles, outlier detection |
| [[concepts/probability-theory\|Probability Theory]] | INF1004 | Sample space, conditional probability, Bayes' theorem, independence |
| [[concepts/probability-distributions\|Probability Distributions]] | INF1004 | Binomial, Poisson, Normal (CLT, Z-score), exponential |
| [[concepts/linear-algebra-matrices\|Linear Algebra & Matrices]] | INF1004 | Matrix operations, inverse, determinant, linear systems, rank |
| [[concepts/eigenvalues-and-svd\|Eigenvalues, Diagonalisation & SVD]] | INF1004 | Eigenvalues/vectors, characteristic polynomial, diagonalisation, SVD decomposition |

---

## Key Ideas (INF1003 — Discrete)
- **Proof by induction**: base case + inductive step → universally true for all n ≥ base
- **Combinatorics**: when order matters → permutation (nPr); when order doesn't → combination (nCr)
- **Graph theory**: degree sum = 2|E|; Euler path requires 0 or 2 odd-degree vertices

## Key Ideas (INF1004 — Continuous)
- **CLT**: sample means of any distribution approach Normal as n → ∞; Z = (X̄ − μ)/(σ/√n)
- **Bayes' theorem**: P(A|B) = P(B|A)·P(A)/P(B) — posterior from prior + likelihood
- **SVD**: any matrix A = UΣVᵀ; singular values in Σ capture variance; PCA uses the top-k singular vectors

---

## Cross-Domain Connections

- [[synthesis/maths-to-ml-bridge|Mathematics → Machine Learning]] — explicit mapping of every maths topic to its ML application
- [[concepts/algorithm-complexity|Algorithm Complexity]] — recurrence relations (INF1003) feed directly into Master Theorem analysis
- [[concepts/data-structures-fundamentals|Data Structures]] — combinatorics and graph theory underpin tree/graph data structures

---

## Study Notes

*(none yet — INF1003 and INF1004 study-notes pages not yet created)*
