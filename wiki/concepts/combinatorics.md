---
type: concept
title: "Combinatorics"
domain: mathematics
course: INF1003
complexity: medium
tags: [combinatorics, counting, permutations, combinations, pigeonhole]
updated: 2026-05-11
---

# Combinatorics

Combinatorics is the mathematics of counting discrete objects. It underpins algorithm analysis (counting operations), probability, and cryptography.

---

## Counting Rules

### Product Rule

If a procedure has two sequential tasks — $n_1$ ways for the first and $n_2$ ways for the second — then there are $n_1 \times n_2$ total ways.

**Generalises** to $k$ tasks: multiply all task counts together.

**Example:** Licence plates with 3 letters then 3 digits: $26^3 \times 10^3 = 17{,}576{,}000$.

### Sum Rule

If a task can be done in $n_1$ ways **or** $n_2$ ways (mutually exclusive), there are $n_1 + n_2$ total ways.

**Example:** Choose from three project lists of 23, 15, and 19 items (no overlap): $23 + 15 + 19 = 57$.

### Division Rule

If $n$ arrangements exist but each distinct outcome is counted $d$ times, the number of distinct outcomes is $n / d$.

**Example:** 4 coloured balls in a circle — linear arrangements $= 4! = 24$, but each circular arrangement is counted 4 times (rotations), so $24 / 4 = 6$ distinct circular arrangements.

---

## Factorial

$$n! = n \times (n-1) \times \cdots \times 2 \times 1, \qquad 0! = 1$$

---

## Permutations

An **$r$-permutation** is an **ordered** arrangement of $r$ elements chosen from $n$.

$$P(n, r) = \frac{n!}{(n-r)!} = n(n-1)\cdots(n-r+1)$$

**Example:** Arrange 3 items from 5: $P(5, 3) = 5 \times 4 \times 3 = 60$.

---

## Combinations

An **$r$-combination** is an **unordered** selection of $r$ elements from $n$. Order does not matter.

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!\,(n-r)!}$$

**Symmetry:** $\binom{n}{r} = \binom{n}{n-r}$ — choosing $r$ items is equivalent to choosing which $n-r$ items to leave out.

**Relationship to permutations:**
$$\binom{n}{r} = \frac{P(n, r)}{r!}$$

**Example:** Select 5 players from 10: $\binom{10}{5} = 252$.

### Permutations vs Combinations

| | Permutations | Combinations |
|-|-------------|--------------|
| Order matters? | Yes | No |
| Formula | $\frac{n!}{(n-r)!}$ | $\frac{n!}{r!(n-r)!}$ |
| When to use | Arrangements, sequences | Selections, subsets |

---

## Pigeonhole Principle

### Basic Form

If $N + 1$ or more objects are placed into $N$ boxes, at least one box contains **2 or more** objects.

### Generalised Form

If $N$ objects are placed into $k$ boxes, at least one box contains $\geq \lceil N/k \rceil$ objects.

($\lceil x \rceil$ = ceiling function = smallest integer $\geq x$.)

**Example:** How many cards must be drawn from a 52-card deck to guarantee at least 3 of the same suit?
- 4 suits = 4 boxes. Want $\lceil N/4 \rceil \geq 3$, so $N > 8$. Answer: **9 cards**.

**Classic use in CS:** Pigeonhole proves that any lossless compression algorithm must make some files larger — there are more possible inputs than possible outputs.

---

## Related Pages

- [[discrete-mathematics-foundations]] — sequences and number theory (same course)
- [[algorithm-complexity]] — counting operations in algorithms
- [[propositional-logic]] — other INF1003 topic
