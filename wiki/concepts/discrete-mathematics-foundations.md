---
type: concept
title: "Discrete Mathematics Foundations"
domain: mathematics
course: INF1003
complexity: medium
tags: [sequences, number-theory, modular-arithmetic, gcd, primes, recurrence]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000014
---

# Discrete Mathematics Foundations

Foundational topics in discrete mathematics: sequences, series, and number theory. These form the mathematical backbone of algorithm analysis (see [[algorithm-complexity]]) and cryptography.

---

## Sequences

A **sequence** is an infinite, ordered list of numbers. Each term $a_n$ is indexed by $n$.

### Arithmetic Progression (AP)

First term $a$, common difference $d$:

$$a_n = a + (n-1)d$$

**Sum of first $n$ terms:**
$$S_n = \frac{n(a_1 + a_n)}{2} = \frac{n[2a + (n-1)d]}{2}$$

**Classic result:** $1 + 2 + \cdots + 100 = \frac{100 \times 101}{2} = 5050$

### Geometric Progression (GP)

First term $a$, common ratio $r$:

$$a_n = ar^{n-1}$$

**Sum of first $n$ terms** ($r \neq 1$):
$$S_n = \frac{a(1 - r^n)}{1 - r}$$

**Infinite sum** (only exists when $|r| < 1$):
$$S_\infty = \frac{a}{1 - r}$$

### Recurrence Relations

An equation expressing $a_n$ in terms of previous terms. A sequence is a **solution** if its terms satisfy the relation.

**Example:** $a_n = a_{n-1} + 3$, $a_1 = 2$ → generates $2, 5, 8, 11, \ldots$ (an AP with $d = 3$).

**Fibonacci sequence:** $f_1 = 0,\ f_2 = 1,\ f_n = f_{n-1} + f_{n-2}$ → $0, 1, 1, 2, 3, 5, 8, 13, \ldots$

Fibonacci recurrence appears in [[algorithm-complexity]] (naïve recursion runs in $O(2^n)$; memoised DP reduces this to $O(n)$).

### Compound Interest

$$\text{Balance after } n \text{ years} = P(1 + r)^n$$

A geometric progression with ratio $(1 + r)$. Illustrates the dramatic effect of exponential growth — a 1% daily improvement compounds to a 37.78× annual gain.

---

## Number Theory

### Divisibility

$a \mid b$ ("$a$ divides $b$") if $b = ac$ for some integer $c$.

**Division algorithm:** For any integer $a$ and positive integer $d$, there exist unique integers $q$ (quotient) and $r$ (remainder), $0 \leq r < d$, such that:
$$a = dq + r \qquad (r = a \bmod d)$$

### Modular Arithmetic

$$a \equiv b \pmod{m} \iff a \bmod m = b \bmod m$$

**Key properties:** If $a \equiv b$ and $c \equiv d \pmod{m}$, then:
- $a + c \equiv b + d \pmod{m}$
- $ac \equiv bd \pmod{m}$

**Useful trick:** $98^5 \bmod 97$. Since $98 \equiv 1 \pmod{97}$, we get $98^5 \equiv 1^5 = 1$.

Modular arithmetic is the foundation of **RSA cryptography** (1977): encryption uses $C \equiv M^e \pmod{n}$; decryption uses $M \equiv C^d \pmod{n}$, where $n = pq$ for large primes $p, q$.

### Primes & Fundamental Theorem of Arithmetic

An integer $p > 1$ is **prime** if its only positive factors are $1$ and $p$.

**Primality test:** Only check divisors up to $\lfloor\sqrt{n}\rfloor$.

**Fundamental Theorem:** Every integer $> 1$ has a unique prime factorisation.

### GCD and LCM

$$\gcd(a, b) = p_1^{\min(a_1, b_1)} \cdots p_k^{\min(a_k, b_k)}$$
$$\text{lcm}(a, b) = p_1^{\max(a_1, b_1)} \cdots p_k^{\max(a_k, b_k)}$$
$$\gcd(a, b) \times \text{lcm}(a, b) = a \times b$$

Integers are **coprime** (relatively prime) if $\gcd(a, b) = 1$.

### Euclidean Algorithm

Efficient GCD computation using the lemma $\gcd(a, d) = \gcd(d,\ a \bmod d)$. Repeat until remainder is 0.

**Example:** $\gcd(287, 91)$:
$$287 = 91 \times 3 + 14 \implies \gcd(287, 91) = \gcd(91, 14)$$
$$91 = 14 \times 6 + 7 \implies \gcd(91, 14) = \gcd(14, 7)$$
$$14 = 7 \times 2 + 0 \implies \gcd = 7$$

---

## Key Formulas at a Glance

| Formula | Use |
|---------|-----|
| $a_n = a + (n-1)d$ | AP $n$th term |
| $S_n = \frac{n(a_1 + a_n)}{2}$ | AP sum |
| $a_n = ar^{n-1}$ | GP $n$th term |
| $S_\infty = \frac{a}{1-r}$, $\|r\| < 1$ | GP infinite sum |
| $a = dq + r$ | Division algorithm |
| $\gcd \times \text{lcm} = a \times b$ | GCD–LCM relationship |

## Related Pages

- [[algorithm-complexity]] — recurrences and Big-Oh
- [[combinatorics]] — counting, another branch of discrete mathematics
- [[propositional-logic]] — formal logic, same course
- [[sets-functions-relations]] — set theory foundations
