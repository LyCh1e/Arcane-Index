# INF1003 Mathematics 1 — Complete Study Notes

**Singapore Institute of Technology**
**Prepared from lecture slides and tutorials (Academic Year 2024/25)**

---

## Table of Contents

1. [Topic 1: Sequences and Summation](#topic-1-sequences-and-summation)
2. [Topic 2: Number Theory](#topic-2-number-theory)
3. [Topic 3: Combinatorics](#topic-3-combinatorics)
4. [Topic 4: Propositional Logic](#topic-4-propositional-logic)
5. [Topic 5: Predicate Logic](#topic-5-predicate-logic)
6. [Topic 6: Rules of Inference](#topic-6-rules-of-inference)
7. [Topic 7: Proof Methods](#topic-7-proof-methods)
8. [Topic 8: Sets (Tutorial)](#topic-8-sets)
9. [Topic 9: Functions (Tutorial)](#topic-9-functions)
10. [Topic 10: Relations (Tutorial)](#topic-10-relations)

---

## Topic 1: Sequences and Summation

### 1.1 Key Notation

| Symbol | Meaning |
|---|---|
| $\infty$ | Infinity |
| $\in$ | "is an element of" |
| $\mathbb{N} = \{0,1,2,3,\ldots\}$ | Natural numbers (includes 0 in this module) |
| $\mathbb{Z} = \{\ldots,-2,-1,0,1,2,\ldots\}$ | Integers |
| $\mathbb{Z}^+ = \{1,2,3,\ldots\}$ | Positive integers |
| $\mathbb{Z}^- = \{\ldots,-3,-2,-1\}$ | Negative integers |

### 1.2 Sequences

**Definition:** A sequence of numbers $(a_1, a_2, a_3, \ldots)$ is an **infinite and ordered list** of numbers. Each $a_n$ is a number and the subscript $n$ indicates its index. If we start with $a_1$, then $a_n$ is the $n$th term. 

**Notation for sequences:**
- $(a_i)_{i=2}^{12}$: terms $a_i$ from index 2 to 12
- $(b_j)_{j=0}^{\infty}$: terms $b_j$ from index 0 to $\infty$
- $(c_k)_{k \geq 5}$: terms $c_k$ for all indices $\geq 5$
- $(d_l)_{l \in \mathbb{Z}^+}$ or $(d_l)_{l \geq 1}$: terms $d_l$ for all positive integer indices

### 1.3 Sequence Specified by a Formula

A sequence can be defined **explicitly by a formula**. For example:
- $a_n = n^2$ generates $1, 4, 9, 16, \ldots$
- $a_n = 2n + 3, \; n \geq 1$ generates $5, 7, 9, 11, \ldots$

### 1.4 Recurrence Relations

**Definition:** A recurrence relation for the sequence $(a_n)_{n \geq 1}$ is an equation that expresses $a_n$ in terms of one or more of the previous terms $a_1, a_2, \ldots, a_{n-1}$, for all integers $n \geq n_0$, where $n_0$ is a positive integer.

A sequence is called a **solution** of a recurrence relation if its terms satisfy it.

**Example 1:** Let $a_n = a_{n-1} + 3$ for $n = 1, 2, 3, \ldots$ with $a_1 = 2$.
$$a_2 = a_1 + 3 = 5, \quad a_3 = a_2 + 3 = 8, \quad a_4 = a_3 + 3 = 11$$

**Example 2:** Let $a_n = a_{n-1} - a_{n-2}$ for $n = 3, 4, \ldots$ with $a_1 = 3, a_2 = 5$.
$$a_3 = a_2 - a_1 = 5 - 3 = 2, \quad a_4 = a_3 - a_2 = 2 - 5 = -3$$

**Practice Question:** Let $a_n = 3a_{n-1} + 2a_{n-2}$ with $a_1 = 1, a_2 = 1$. Find $a_5$.
> $a_3 = 3(1)+2(1)=5$, $a_4 = 3(5)+2(1)=17$, $a_5 = 3(17)+2(5)=61$

### 1.5 Fibonacci Sequence

**Definition:** The Fibonacci sequence $(f_1, f_2, \ldots)$ is defined by:
$$f_1 = 0, \quad f_2 = 1, \quad f_n = f_{n-1} + f_{n-2} \text{ for } n \geq 3$$

**First terms:** $0, 1, 1, 2, 3, 5, 8, 13, 21, \ldots$

*Note: Some texts start with $f_0 = 0, f_1 = 1$; this module uses $f_1 = 0, f_2 = 1$.*

### 1.6 Arithmetic Progression (AP)

**Definition:** An arithmetic progression has **first term** $a$ and **common difference** $d$, with:
$$a_n = a + (n-1)d$$

**Remark:** Equivalently, $a_n = a_{n-1} + d$, or $a_n - a_{n-1} = d$.

**Example:** AP with first term 5 and common difference 3: $5, 8, 11, 14, \ldots$

**Example:** AP with $a_1 = 13, d = 7$. Find $a_{21}$:
$$a_{21} = 13 + (21-1)(7) = 13 + 140 = 153$$

### 1.7 Geometric Progression (GP)

**Definition:** A geometric progression has **first term** $a$ and **common ratio** $r$, with:
$$a_n = ar^{n-1}$$

**Remark:** Equivalently, $a_n = r \cdot a_{n-1}$, or $\dfrac{a_n}{a_{n-1}} = r$.

**Example:** GP with first term 3 and common ratio $\frac{1}{2}$: $3, \frac{3}{2}, \frac{3}{4}, \frac{3}{8}, \ldots$

**Example:** GP with $a_1 = 1024, r = \frac{1}{2}$. Find $a_9$:
$$a_9 = 1024 \cdot \left(\frac{1}{2}\right)^8 = 1024 \cdot \frac{1}{256} = 4$$

### 1.8 Compound Interest

If $\$P$ is deposited at annual interest rate $R\%$, then the interest rate is $r = \frac{R}{100}$, and after $n$ years:
$$\text{Balance} = P(1+r)^n$$

*This is compounding — interest is paid on interest.*

**Example:** $\$10{,}000$ at 11% per year for 30 years:
$$10{,}000 \times (1.11)^{30} = \$228{,}922.97$$

**Sense of Scale:**
- $(1)^{365} = 1.00$ (no change)
- $(1.01)^{365} = 37.78$ (1% daily improvement → 37.78× growth)
- $(0.99)^{365} = 0.03$ (1% daily decline → almost nothing)

**Investor Savings Formula:** If $\$P$ is added at the beginning of each year with interest rate $k$, then at year $t$:
$$S_t = \frac{P[(1+k)^t - 1]}{k}$$

### 1.9 Summation

**Notation:** $\displaystyle\sum_{i=m}^{n} a_i = a_m + a_{m+1} + \cdots + a_n$

The variable $i$ is the **index of summation** (choice of letter is arbitrary). The index runs from lower limit $m$ to upper limit $n$.

**Partial sum:** Given sequence $(a_1, a_2, a_3, \ldots)$, define:
$$S_n := a_1 + a_2 + \cdots + a_n$$

**Examples:**
- $\displaystyle\sum_{j=1}^{5} j^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1+4+9+16+25 = 55$
- $\displaystyle\sum_{k=4}^{8} (-1)^k = 1-1+1-1+1 = 1$

### 1.10 Summation of an Arithmetic Progression

For AP $a_n = a + (n-1)d$, the sum of the first $n$ terms:
$$S_n = \frac{n[2a + (n-1)d]}{2} = \frac{n(a_1 + a_n)}{2}$$

**Example:** Sum of all positive integers from 1 to 100:
$$S_{100} = \frac{100(1 + 100)}{2} = 5050$$

### 1.11 Summation of a Geometric Progression

For GP $a_n = ar^{n-1}$ with $r \neq 1$, the sum of the first $n$ terms:
$$S_n = \frac{a(1-r^n)}{1-r} = \frac{a(r^n - 1)}{r - 1}$$

*When $r = 1$: $S_n = na$.*

### 1.12 Infinite Series (Geometric)

If $-1 < r < 1$, then $\lim_{n \to \infty} r^n = 0$, so the sum to infinity exists:
$$S_\infty = \lim_{n \to \infty} S_n = \frac{a}{1-r}$$

**Example:** For $a_n = \frac{1}{2^{n-1}}$ (GP with $a=1, r=\frac{1}{2}$):
$$S_N = 2\left[1 - \left(\frac{1}{2}\right)^N\right] \to 2 \text{ as } N \to \infty$$

**Example:** Find $\displaystyle S_\infty = \sum_{n=1}^{\infty} \frac{1}{3^n}$:
$$a = \frac{1}{3}, \; r = \frac{1}{3}, \quad S_\infty = \frac{1/3}{1 - 1/3} = \frac{1}{2}$$

---

## Topic 2: Number Theory

### 2.1 Division

**Definition:** If $a \neq 0$ and $b$ are integers, we say $a$ **divides** $b$ (written $a \mid b$) if there exists an integer $c$ such that $b = ac$ (equivalently, $\frac{b}{a}$ is an integer).

- When $a \mid b$: $a$ is a **factor/divisor** of $b$, and $b$ is a **multiple** of $a$
- $a \nmid b$ means $a$ does not divide $b$

**Example:** $3 \nmid 7$ (since $7/3$ is not an integer), but $3 \mid 12$ (since $12/3 = 4$).

### 2.2 Division Algorithm

**Theorem:** Let $a$ be an integer and $d$ a positive integer. Then there exist **unique** integers $q$ (quotient) and $r$ (remainder), with $0 \leq r < d$, such that:
$$a = dq + r$$

**Notation:** $r = a \bmod d$

**Examples:**
- $101 = 11 \times 9 + 2$ → quotient 9, remainder 2
- $-11 = 3 \times (-4) + 1$ → quotient $-4$, remainder 1

### 2.3 Modular Arithmetic

**Definition:** $a \equiv b \pmod{m}$ means $a$ is **congruent to** $b$ **modulo** $m$.

$$a \equiv b \pmod{m} \iff a \bmod m = b \bmod m$$

**Theorem (Modular Arithmetic Properties):** If $a \equiv b \pmod{m}$ and $c \equiv d \pmod{m}$, then:
$$a + c \equiv b + d \pmod{m} \quad \text{and} \quad ac \equiv bd \pmod{m}$$

**Example:** Given $7 \equiv 2 \pmod 5$ and $11 \equiv 1 \pmod 5$:
$$18 = 7 + 11 \equiv 2 + 1 = 3 \pmod 5$$
$$77 = 7 \times 11 \equiv 2 \times 1 = 2 \pmod 5$$

**Practice MCQ examples:**
- $9800 \bmod 97$: $9800 = 97 \times 101 + 3$, so answer is **3**
- $98^5 \bmod 97$: $98 \equiv 1 \pmod{97}$, so $98^5 \equiv 1^5 = 1 \pmod{97}$, answer is **1**
- $123 \bmod 97$: $123 = 97 \times 1 + 26$, answer is **26**

### 2.4 Application: RSA Cryptography

RSA (Rivest–Shamir–Adleman, 1977) is a public-key cryptosystem based on the difficulty of factoring large integers. Key size: 1024–4096 bits.

**Steps:**
1. Bob chooses two distinct primes $p, q$ and computes $n = p \cdot q$
2. Bob chooses $e$ with $\gcd(e, (p-1)(q-1)) = 1$
3. Bob solves $d \cdot e \equiv 1 \pmod{(p-1)(q-1)}$
4. Bob makes $(e, n)$ **public** and keeps $(p, q, d)$ **secret**
5. Alice encrypts message $M$ as $C \equiv M^e \pmod{n}$
6. Bob decrypts by computing $M \equiv C^d \pmod{n}$

### 2.5 Primes

**Definition:** An integer $p > 1$ is **prime** if its only positive factors are 1 and $p$. An integer $> 1$ that is not prime is **composite**.

**Examples:** 7 is prime (factors: 1 and 7). 9 is composite ($9 = 3 \times 3$).

**Primality test:** To test if $n$ is prime, check divisibility only up to $\lfloor\sqrt{n}\rfloor$.

**Example:** To test if 101 is prime: primes $\leq \sqrt{101} \approx 10.05$ are 2, 3, 5, 7. Since 101 is not divisible by any of these, 101 is prime.

### 2.6 Fundamental Theorem of Arithmetic

**Theorem:** Every integer greater than 1 can be written **uniquely** as a prime or as the product of two or more primes in non-decreasing order.

**Examples:**
$$100 = 2^2 \times 5^2, \quad 641 = 641, \quad 999 = 3^3 \times 37, \quad 1024 = 2^{10}$$

### 2.7 Greatest Common Divisor (GCD)

**Definition:** The **greatest common divisor** of integers $a$ and $b$ (not both zero) is the largest integer $d$ such that $d \mid a$ and $d \mid b$. Denoted $\gcd(a, b)$.

**Example:** $\gcd(24, 36) = 12$ (common divisors: 1, 2, 3, 4, 6, 12).

**Example:** $\gcd(17, 22) = 1$ (no common divisors other than 1 → **relatively prime/coprime**).

**GCD via prime factorisation:** If $a = p_1^{a_1} p_2^{a_2} \cdots p_n^{a_n}$ and $b = p_1^{b_1} p_2^{b_2} \cdots p_n^{b_n}$, then:
$$\gcd(a,b) = p_1^{\min(a_1,b_1)} p_2^{\min(a_2,b_2)} \cdots p_n^{\min(a_n,b_n)}$$

**Example:** $120 = 2^3 \times 3 \times 5$, $500 = 2^2 \times 5^3$:
$$\gcd(120, 500) = 2^{\min(3,2)} \times 3^{\min(1,0)} \times 5^{\min(1,3)} = 2^2 \times 3^0 \times 5^1 = 20$$

**Relatively prime:** Integers $a$ and $b$ are relatively prime if $\gcd(a,b) = 1$.
**Pairwise relatively prime:** Integers $a_1, a_2, \ldots, a_n$ are pairwise relatively prime if $\gcd(a_i, a_j) = 1$ for all $i \neq j$.

**Example:** $\gcd(10,17)=1$, $\gcd(10,21)=1$, $\gcd(17,21)=1$ → 10, 17, 21 are pairwise relatively prime.
**Example:** $\gcd(10,24)=2 > 1$ → 10, 19, 24 are **not** pairwise relatively prime.

### 2.8 Least Common Multiple (LCM)

**LCM via prime factorisation:**
$$\text{lcm}(a,b) = p_1^{\max(a_1,b_1)} p_2^{\max(a_2,b_2)} \cdots p_n^{\max(a_n,b_n)}$$

**Example:** $\text{lcm}(2^3 3^5 7^2,\; 2^4 3^3) = 2^{\max(3,4)} \times 3^{\max(5,3)} \times 7^{\max(2,0)} = 2^4 3^5 7^2 = 190{,}512$

**Key relationship:**
$$\gcd(a,b) \times \text{lcm}(a,b) = a \times b$$

### 2.9 The Euclidean Algorithm

**Lemma:** Let $a = dq + r$. Then $\gcd(a, d) = \gcd(d, r)$.

This gives an efficient method: repeatedly apply the division algorithm, reducing until the remainder is 0.

**Example:** Find $\gcd(287, 91)$:
$$287 = 91 \times 3 + 14 \implies \gcd(287,91) = \gcd(91,14)$$
$$91 = 14 \times 6 + 7 \implies \gcd(91,14) = \gcd(14,7)$$
$$14 = 7 \times 2 + 0 \implies \gcd(14,7) = 7$$

Therefore $\gcd(287, 91) = 7$.

---

## Topic 3: Combinatorics

### 3.1 Introduction

**Combinatorics** (Counting Theory) is the area of mathematics concerned with counting discrete objects. Applications in computer science, physics, and systems management.

### 3.2 The Product Rule

If a procedure can be broken into a sequence of two tasks, with $n_1$ ways to do the first task and $n_2$ ways to do the second task (for each way of doing the first), then there are $n_1 \cdot n_2$ ways to do the procedure.

**Generalisation:** If tasks 1 through $k$ have $n_1, n_2, \ldots, n_k$ ways respectively, then the total is $n_1 \times n_2 \times \cdots \times n_k$.

**Example:** How many license plates with 3 uppercase letters followed by 3 digits?
$$26 \times 26 \times 26 \times 10 \times 10 \times 10 = 17{,}576{,}000$$

### 3.3 The Sum Rule

If a task can be done in $n_1$ ways **or** in $n_2$ ways (disjoint), then there are $n_1 + n_2$ ways total.

**Example:** A student chooses from 3 lists with 23, 15, and 19 projects (no overlap):
$$23 + 15 + 19 = 57 \text{ possible projects}$$

### 3.4 The Division Rule (Subtraction/Inclusion-Exclusion)

If a task can be carried out in $n$ ways, and for every way $w$, exactly $d$ of the $n$ ways correspond to the same outcome as $w$, then there are $\dfrac{n}{d}$ distinct ways.

**Example (Division Rule):** 4 coloured balls arranged in a circle. Total arrangements = $\frac{4!}{4} = 6$.

### 3.5 Factorial

$$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1, \quad 0! = 1$$

### 3.6 Permutations

**Definition:** An **$r$-permutation** of a set with $n$ elements is an ordered arrangement of $r$ elements from the set.

**Formula:**
$$P(n,r) = {}_nP_r = \frac{n!}{(n-r)!} = n(n-1)(n-2)\cdots(n-r+1)$$

**Remark:** ${}_nP_0 = 1$ (one way to order zero elements).

**Example:** How many ways to arrange 3 items from a set of 5?
$$P(5,3) = \frac{5!}{2!} = 5 \times 4 \times 3 = 60$$

### 3.7 Combinations

**Definition:** An **$r$-combination** of a set with $n$ elements is an **unordered** selection of $r$ elements. (Order does not matter.)

**Theorem:**
$$C(n,r) = {}_nC_r = \binom{n}{r} = \frac{n!}{r!\,(n-r)!}$$

**Corollary:** ${}_nC_r = {}_nC_{n-r}$ (symmetry).

**Example:** Select 5 players from a 10-member team:
$$\binom{10}{5} = \frac{10!}{5!\,5!} = 252$$

**Key difference:** Permutations care about order; combinations do not.
$$\binom{n}{r} = \frac{P(n,r)}{r!}$$

### 3.8 The Pigeonhole Principle

**Basic Pigeonhole Principle:** If $N+1$ (or more) objects are placed into $N$ boxes, then at least one box contains at least 2 objects.

**Generalised Pigeonhole Principle (Theorem):** If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least $\lceil N/k \rceil$ objects.

($\lceil x \rceil$ is the **ceiling** function — smallest integer $\geq x$.)

**Example:** How many cards must be selected from a 52-card deck to guarantee at least 3 of the same suit?
- 4 suits = 4 boxes. Want $\lceil N/4 \rceil \geq 3$, so $N > 8$, meaning **9 cards**.

---

## Topic 4: Propositional Logic

### 4.1 Introduction

**Propositional Logic** (also called Propositional Calculus or Zeroth-Order Logic) deals with true/false propositions and logical connectives. Applications in computer systems, telecommunications, cryptography, and AI.

**Proposition:** A declarative statement that is either **true** (T or $\top$) or **false** (F or $\bot$).

- "How old are you?" — **Not** a proposition (it's a question)
- "2 + 2 = 4" — Proposition (true)
- "Singapore is in China" — Proposition (false)

**Propositional variables:** conventionally $p, q, r, s, \ldots$

### 4.2 Negation (NOT)

**Definition:** The **negation** of $p$, denoted $\neg p$ (read "not $p$"), is:

| $p$ | $\neg p$ |
|:---:|:---:|
| $\bot$ | $\top$ |
| $\top$ | $\bot$ |

Logic gate: NOT gate $(\triangleright\!\!\circ)$

### 4.3 Conjunction (AND)

**Definition:** The **conjunction** of $p$ and $q$, denoted $p \wedge q$ (read "$p$ and $q$"), is true only when both $p$ and $q$ are true.

| $p$ | $q$ | $p \wedge q$ |
|:---:|:---:|:---:|
| $\bot$ | $\bot$ | $\bot$ |
| $\bot$ | $\top$ | $\bot$ |
| $\top$ | $\bot$ | $\bot$ |
| $\top$ | $\top$ | $\top$ |

Logic gate: AND gate

### 4.4 Disjunction (OR)

**Definition:** The **disjunction** of $p$ and $q$, denoted $p \vee q$ (read "$p$ or $q$"), is false only when both $p$ and $q$ are false.

| $p$ | $q$ | $p \vee q$ |
|:---:|:---:|:---:|
| $\bot$ | $\bot$ | $\bot$ |
| $\bot$ | $\top$ | $\top$ |
| $\top$ | $\bot$ | $\top$ |
| $\top$ | $\top$ | $\top$ |

Logic gate: OR gate

### 4.5 Exclusive Disjunction (XOR)

**Definition:** The **exclusive disjunction** of $p$ and $q$, denoted $p \oplus q$, is true when exactly one of $p$, $q$ is true (but not both).

| $p$ | $q$ | $p \oplus q$ |
|:---:|:---:|:---:|
| $\bot$ | $\bot$ | $\bot$ |
| $\bot$ | $\top$ | $\top$ |
| $\top$ | $\bot$ | $\top$ |
| $\top$ | $\top$ | $\bot$ |

### 4.6 Material Conditional (Implication)

**Definition:** The **material conditional** $p \to q$ (read "if $p$ then $q$", or "$p$ implies $q$") is false only when $p$ is true and $q$ is false. $p$ is the **antecedent** (hypothesis/premise), $q$ is the **consequent** (conclusion).

| $p$ | $q$ | $p \to q$ |
|:---:|:---:|:---:|
| $\bot$ | $\bot$ | $\top$ |
| $\bot$ | $\top$ | $\top$ |
| $\top$ | $\bot$ | $\bot$ |
| $\top$ | $\top$ | $\top$ |

**Key insight:** When $p$ is false, $p \to q$ is **vacuously true** regardless of $q$.

**Alternative notation:** $p \Rightarrow q$

**Other ways to express $p \to q$:**
- "if $p$, then $q$" / "$p$ only if $q$"
- "$q$ if $p$" / "$q$ whenever $p$"
- "$p$ is sufficient for $q$" / "$q$ is necessary for $p$"

### 4.7 Converse, Contrapositive, and Inverse

For the conditional $p \to q$:

| Statement | Form | Logically equivalent to |
|---|---|---|
| Original | $p \to q$ | itself |
| Converse | $q \to p$ | inverse |
| Contrapositive | $\neg q \to \neg p$ | **$p \to q$** (same truth table!) |
| Inverse | $\neg p \to \neg q$ | converse |

**Important:** Only the **contrapositive** is logically equivalent to the original.

**Example:** "The home team wins whenever it is raining" ($p$: raining, $q$: home team wins):
- Contrapositive: "If the home team does not win, then it is not raining."
- Inverse: "If it is not raining, then the home team does not win."
- Converse: "If the home team wins, then it is raining."

### 4.8 Biconditional

**Definition:** The **biconditional** $p \leftrightarrow q$ (read "$p$ if and only if $q$") is true exactly when $p$ and $q$ have the same truth value.

| $p$ | $q$ | $p \leftrightarrow q$ |
|:---:|:---:|:---:|
| $\bot$ | $\bot$ | $\top$ |
| $\bot$ | $\top$ | $\bot$ |
| $\top$ | $\bot$ | $\bot$ |
| $\top$ | $\top$ | $\top$ |

**Note:** $p \leftrightarrow q \equiv (p \to q) \wedge (q \to p)$

**Key equivalence:** $p \to q \equiv \neg p \vee q$

### 4.9 Tautologies and Contradictions

**Tautology:** A compound proposition that is **always true** regardless of truth values of its components. Example: $p \vee \neg p$.

**Contradiction:** A compound proposition that is **always false**. Example: $p \wedge \neg p$.

**Contingency:** Neither a tautology nor a contradiction.

### 4.10 Logical Equivalence

Two propositions are **logically equivalent** if they have the same truth table, written $p \equiv q$.

**Key Logical Equivalence Laws:**

| Law | Conjunction form | Disjunction form |
|---|---|---|
| **Identity** | $p \wedge \top \equiv p$ | $p \vee \bot \equiv p$ |
| **Domination** | $p \wedge \bot \equiv \bot$ | $p \vee \top \equiv \top$ |
| **Idempotent** | $p \wedge p \equiv p$ | $p \vee p \equiv p$ |
| **Double Negation** | $\neg(\neg p) \equiv p$ | — |
| **Commutative** | $p \wedge q \equiv q \wedge p$ | $p \vee q \equiv q \vee p$ |
| **Associative** | $(p \wedge q) \wedge r \equiv p \wedge (q \wedge r)$ | $(p \vee q) \vee r \equiv p \vee (q \vee r)$ |
| **Distributive** | $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$ | $p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)$ |
| **De Morgan's** | $\neg(p \wedge q) \equiv \neg p \vee \neg q$ | $\neg(p \vee q) \equiv \neg p \wedge \neg q$ |

**Additional useful equivalences:**
$$p \to q \equiv \neg p \vee q$$
$$p \leftrightarrow q \equiv (p \to q) \wedge (q \to p)$$

---

## Topic 5: Predicate Logic

### 5.1 Overview

Predicate Logic extends propositional logic by adding **predicates** and **quantifiers**, enabling statements about objects and their properties. Used to translate English to formal logic and back.

### 5.2 Predicates

A **predicate** $P(x)$ is a property that a variable $x$ may or may not have. Once $x$ is assigned a value from a **domain**, $P(x)$ becomes a proposition with a truth value.

**Example:** Let $P(x)$ denote "$x > 0$" with domain = integers.
- $P(-3)$: False (since $-3 > 0$ is false)
- $P(0)$: False
- $P(3)$: True

Predicates can have multiple variables: $Q(x, y)$ means "x speaks language y".

### 5.3 Universal Quantifier ($\forall$)

**$\forall x \, P(x)$** (read "for all $x$, $P(x)$") asserts that $P(x)$ is true for **every** element $x$ in the domain.

**Example:** $\forall x \, (x > 0)$ over $\mathbb{Z}^+$ is **True**.
$\forall x \, (x > 0)$ over $\mathbb{Z}$ is **False** (fails for $x = -1$).

### 5.4 Existential Quantifier ($\exists$)

**$\exists x \, P(x)$** (read "there exists $x$ such that $P(x)$") asserts that $P(x)$ is true for **at least one** element $x$ in the domain.

**Example:** $\exists x \, (x > 0)$ over $\mathbb{Z}$ is **True** (e.g., $x = 1$).
$\exists x \, (x > 0)$ over $\mathbb{Z}^-$ is **False**.

### 5.5 Negation of Quantifiers (De Morgan's Laws for Predicate Logic)

| Statement | Equivalent negation |
|---|---|
| $\neg \forall x \, P(x)$ | $\exists x \, \neg P(x)$ |
| $\neg \exists x \, P(x)$ | $\forall x \, \neg P(x)$ |

**Visual aid (class of 4 students wearing red shirts):**

| Scenario | $\forall x P(x)$ | $\exists x P(x)$ |
|---|---|---|
| All 4 wear red | True | True |
| Some but not all wear red | False | True |
| None wear red | False | False |

### 5.6 Multiple Quantifiers

Statements can combine multiple quantifiers; order matters!

**Example:** "Every student speaks at least 2 languages"
$$\forall s \, \exists l_1 \exists l_2 \, (l_1 \neq l_2 \wedge \text{Speaks}(s, l_1) \wedge \text{Speaks}(s, l_2))$$

**System specification example:** "If a user is active, at least one network link will be available."
$$\exists u \, A(u) \to \exists n \, S(n, \text{available})$$

### 5.7 Translation Examples

| English | Predicate Logic |
|---|---|
| All humans are mortal | $\forall x \, (H(x) \to M(x))$ |
| Some students study hard | $\exists x \, (S(x) \wedge H(x))$ |
| No student fails | $\forall x \, (S(x) \to \neg F(x))$ |
| Not all birds can fly | $\exists x \, (B(x) \wedge \neg F(x))$ |

---

## Topic 6: Rules of Inference

### 6.1 Overview

Rules of inference are valid argument forms used as steps in proofs. They allow us to derive new truths from known truths in a systematic way.

**Argument form:** A sequence of propositions, where all but the last are **premises** and the last is the **conclusion**.
**Valid argument:** The conclusion follows necessarily from the premises (the argument is a tautology).

### 6.2 Inference Rules in Propositional Logic

| Rule Name | Form | Tautology |
|---|---|---|
| **Modus Ponens** | $p$, $p \to q \;\therefore q$ | $(p \wedge (p \to q)) \to q$ |
| **Modus Tollens** | $\neg q$, $p \to q \;\therefore \neg p$ | $(\neg q \wedge (p \to q)) \to \neg p$ |
| **Hypothetical Syllogism** | $p \to q$, $q \to r \;\therefore p \to r$ | $((p \to q) \wedge (q \to r)) \to (p \to r)$ |
| **Disjunctive Syllogism** | $p \vee q$, $\neg p \;\therefore q$ | $((p \vee q) \wedge \neg p) \to q$ |
| **Addition** | $p \;\therefore p \vee q$ | $p \to (p \vee q)$ |
| **Simplification** | $p \wedge q \;\therefore p$ | $(p \wedge q) \to p$ |
| **Conjunction** | $p$, $q \;\therefore p \wedge q$ | $(p) \wedge (q) \to (p \wedge q)$ |
| **Resolution** | $p \vee q$, $\neg p \vee r \;\therefore q \vee r$ | $((p \vee q) \wedge (\neg p \vee r)) \to (q \vee r)$ |

### 6.3 Modus Ponens — Detailed Explanation

**Modus Ponens** ("affirming the antecedent"):
$$\frac{p \quad p \to q}{\therefore\, q}$$

**Real-world example:**
- "I am tired" (premise $p$)
- "When I'm tired, I make mistakes" (premise $p \to q$)
- Therefore: "I make mistakes" (conclusion $q$)

Truth table verification — $p \wedge (p \to q) \to q$ is always **True**.

### 6.4 Rules of Inference for Quantifiers

| Rule | Form |
|---|---|
| **Universal Instantiation** | $\forall x \, P(x) \;\therefore P(c)$ for arbitrary $c$ |
| **Universal Generalisation** | $P(c)$ for arbitrary $c \;\therefore \forall x \, P(x)$ |
| **Existential Instantiation** | $\exists x \, P(x) \;\therefore P(c)$ for some element $c$ |
| **Existential Generalisation** | $P(c)$ for some $c \;\therefore \exists x \, P(x)$ |

### 6.5 Applying Rules in Proofs

**Example:** Show that "Linda is a student" follows from:
1. "All CS students take discrete mathematics." [$\forall x (C(x) \to D(x))$]
2. "Linda is a CS student." [$C(\text{Linda})$]
3. "All students taking discrete math know logic." [$\forall x (D(x) \to L(x))$]
4. "Whoever knows logic is a student." [$\forall x (L(x) \to S(x))$]

Step 1: By Universal Instantiation on (1): $C(\text{Linda}) \to D(\text{Linda})$
Step 2: By Modus Ponens with (2): $D(\text{Linda})$
Step 3: By Universal Instantiation on (3): $D(\text{Linda}) \to L(\text{Linda})$
Step 4: By Modus Ponens: $L(\text{Linda})$
Step 5: By Universal Instantiation on (4): $L(\text{Linda}) \to S(\text{Linda})$
Step 6: By Modus Ponens: $S(\text{Linda})$ ✓

---

## Topic 7: Proof Methods

### 7.1 Overview of Methods and Strategies

**For proving conditional statements $p \to q$:**
- Direct Proof
- Proof by Contraposition
- Vacuous and Trivial Proof

**Not specific to $p \to q$:**
- Proof by Contradiction (direct and indirect)
- Counterexamples
- Exhaustive Proof
- Proof by Cases
- Existence and Uniqueness Proofs

Multiple methods can be combined in a single proof.

### 7.2 Direct Proof

**Strategy:** Assume $p$ is true; use rules of inference, axioms, and logical equivalences to show $q$ must be true.

**Useful definitions:**
- Integer $n$ is **even** if $n = 2k$ for some integer $k$
- Integer $n$ is **odd** if $n = 2k + 1$ for some integer $k$

**Example:** Prove "If $n$ is an odd integer, then $n^2$ is odd."

*Proof:*
1. Assume $n$ is odd, so $n = 2k + 1$ for some integer $k$.
2. Then $n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$.
3. Let $r = 2k^2 + 2k$ (an integer). Then $n^2 = 2r + 1$, which is odd. $\blacksquare$

### 7.3 Proof by Contraposition

**Strategy:** Prove the contrapositive $\neg q \to \neg p$ instead of $p \to q$ (they are logically equivalent).

**Example:** Prove "If $n^2$ is odd, then $n$ is odd" (equivalently, if $n$ is even, then $n^2$ is even).

*Proof by contraposition:*
Assume $n$ is even (i.e., $\neg q$), so $n = 2k$ for some integer $k$.
Then $n^2 = (2k)^2 = 4k^2 = 2(2k^2)$, which is even (i.e., $\neg p$). $\blacksquare$

**Choosing between direct proof and contraposition:**
- "If $(x-1)$ is even, then $x$ is odd": direct proof assumes $(x-1)$ is even → show $x$ is odd. Contraposition: assume $x$ is even → show $(x-1)$ is odd.

### 7.4 Vacuous and Trivial Proofs

**Vacuous Proof:** If $p$ is false, then $p \to q$ is true regardless of $q$. Used when the hypothesis is provably false.

**Trivial Proof:** If $q$ is true (regardless of $p$), then $p \to q$ is true.

### 7.5 Proof by Contradiction

**Strategy (to prove $p$ is true):** Assume $\neg p$ is true and derive a contradiction (a statement known to be false). Since $\neg p$ leads to a contradiction, $p$ must be true.

$$\frac{\neg p \to \text{False}}{\therefore\, p}$$

**Example:** Prove $\sqrt{2}$ is irrational.

*Proof:*
Assume $\sqrt{2}$ is rational, so $\sqrt{2} = \frac{a}{b}$ with $\gcd(a,b) = 1$.
Then $2 = \frac{a^2}{b^2}$, so $a^2 = 2b^2$. This means $a^2$ is even, so $a$ is even. Write $a = 2c$.
Then $4c^2 = 2b^2$, so $b^2 = 2c^2$, meaning $b$ is even.
But then $\gcd(a,b) \geq 2$, contradicting $\gcd(a,b) = 1$. $\blacksquare$

**Indirect approach (for $p \to q$):** Assume $p \wedge \neg q$ and derive a contradiction.

### 7.6 Counterexamples

To disprove $\forall x \, P(x)$, find a single **counterexample** — one value of $x$ for which $P(x)$ is false.

**Example:** Disprove "Every positive integer is the sum of three squares."
Counterexample: $7 = ?$. We check: $4+1+1=6$, $4+4+1=9$. Cannot make 7. So the statement is false.

### 7.7 Proof by Cases

Break the domain into cases and prove the statement for each case.

**Example:** Prove "For any integer $n$, $n^2 \geq n$."
- Case 1: $n \geq 1$. Then $n^2 \geq n \cdot 1 = n$. ✓
- Case 2: $n = 0$. Then $n^2 = 0 = n$. ✓
- Case 3: $n \leq -1$. Then $n^2 \geq 1 > 0 \geq n$ (since $n$ is negative). ✓

### 7.8 Existence Proofs

**Constructive:** Exhibit a specific element satisfying the property.
**Non-constructive:** Show existence without finding the element explicitly.

**Uniqueness:** To prove there is exactly one element with a property, show existence and then show any two elements with the property must be equal.

---

## Topic 8: Sets

*(Covered in Tutorial; no dedicated lecture slides — key concepts)*

### 8.1 Basic Definitions

**Set:** An unordered collection of distinct objects (elements/members).

**Notation:**
- Roster: $A = \{1, 2, 3\}$
- Set-builder: $A = \{x \mid P(x)\}$ ("the set of all $x$ such that $P(x)$")
- $x \in A$: $x$ is an element of $A$
- $x \notin A$: $x$ is not an element of $A$

**Special sets:**
- $\emptyset$ or $\{\}$: the **empty set** (no elements)
- $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$: natural numbers, integers, rationals, reals, complex numbers

### 8.2 Subsets and Equality

- $A \subseteq B$: $A$ is a **subset** of $B$ — every element of $A$ is in $B$
- $A \subset B$: $A$ is a **proper subset** of $B$ — $A \subseteq B$ and $A \neq B$
- $A = B$ iff $A \subseteq B$ and $B \subseteq A$
- $\emptyset \subseteq A$ for every set $A$

### 8.3 Cardinality

The **cardinality** $|A|$ is the number of (distinct) elements in $A$.

| Set | Cardinality |
|---|---|
| $\{a\}$ | 1 |
| $\{\{a\}\}$ | 1 |
| $\{a, \{a\}\}$ | 2 |
| $\emptyset$ | 0 |
| $\{\emptyset\}$ | 1 |

### 8.4 Power Set

The **power set** $\mathcal{P}(A)$ is the set of all subsets of $A$.

$$|\mathcal{P}(A)| = 2^{|A|}$$

**Example:** $\mathcal{P}(\{a,b\}) = \{\emptyset, \{a\}, \{b\}, \{a,b\}\}$, which has $2^2 = 4$ elements.

### 8.5 Set Operations

| Operation | Symbol | Definition |
|---|---|---|
| Union | $A \cup B$ | $\{x \mid x \in A \text{ or } x \in B\}$ |
| Intersection | $A \cap B$ | $\{x \mid x \in A \text{ and } x \in B\}$ |
| Difference | $A - B$ | $\{x \mid x \in A \text{ and } x \notin B\}$ |
| Complement | $\overline{A}$ or $A^c$ | $\{x \mid x \notin A\}$ (relative to a universal set $U$) |

### 8.6 Cartesian Product

$$A \times B = \{(a,b) \mid a \in A \text{ and } b \in B\}$$

**Example:** $A = \{a,b,c,d\}$, $B = \{y,z\}$:
$$A \times B = \{(a,y),(a,z),(b,y),(b,z),(c,y),(c,z),(d,y),(d,z)\}$$

$|A \times B| = |A| \times |B|$

### 8.7 Set Identities

| Identity | Law |
|---|---|
| $A \cup \emptyset = A$, $A \cap U = A$ | Identity |
| $A \cup U = U$, $A \cap \emptyset = \emptyset$ | Domination |
| $A \cup A = A$, $A \cap A = A$ | Idempotent |
| $(A^c)^c = A$ | Double complement |
| $A \cup B = B \cup A$, $A \cap B = B \cap A$ | Commutative |
| $\overline{A \cup B} = \overline{A} \cap \overline{B}$ | De Morgan's |
| $\overline{A \cap B} = \overline{A} \cup \overline{B}$ | De Morgan's |

---

## Topic 9: Functions

*(Covered in Tutorial)*

### 9.1 Definition

A **function** $f: A \to B$ assigns to each element $a \in A$ exactly one element $f(a) \in B$.

- $A$ = **domain**, $B$ = **codomain**
- **Range/Image** of $f$ = $\{f(a) \mid a \in A\} \subseteq B$

### 9.2 Types of Functions

**Injective (one-to-one):** $f(a) = f(b) \implies a = b$ (no two inputs map to the same output).

**Surjective (onto):** Every element of $B$ is $f(a)$ for some $a \in A$ (range = codomain).

**Bijective:** Both injective and surjective (one-to-one correspondence).

### 9.3 Function Operations

- $(f_1 + f_2)(x) = f_1(x) + f_2(x)$
- $(f_1 f_2)(x) = f_1(x) \cdot f_2(x)$
- **Composition:** $(f_1 \circ f_2)(x) = f_1(f_2(x))$
- **Note:** Composition is generally not commutative: $f_1 \circ f_2 \neq f_2 \circ f_1$

### 9.4 Floor and Ceiling Functions

- **Floor** $\lfloor x \rfloor$: greatest integer $\leq x$ (e.g., $\lfloor 2.7 \rfloor = 2$, $\lfloor -2.7 \rfloor = -3$)
- **Ceiling** $\lceil x \rceil$: smallest integer $\geq x$ (e.g., $\lceil 2.1 \rceil = 3$, $\lceil -2.7 \rceil = -2$)

### 9.5 Tutorial Questions Summary

1. Let $f_1(x) = x^2 + 1$ and $f_2(x) = (x+2)^2$. Find $f_1 + f_2$, $f_1 f_2$, $f_1 \circ f_2$, $f_2 \circ f_1$.
2. Determine one-to-one and onto for various explicit function definitions on $\{a,b,c,d\}$.
3. Determine if $f: \mathbb{Z} \to \mathbb{R}$ is a function for $f(n) = \pm n$, $f(n) = +\sqrt{n^2 - 1}$, $f(n) = \frac{1}{n^2 - 4}$ (note: $f$ fails when undefined for some input — e.g., $n = \pm 2$ for the last case).
4. Determine one-to-one and onto for $f(n) = n-1$, $f(n) = n^2 + 1$, $f(n) = n^3$, $f(n) = \lceil n/2 \rceil$, $f(n) = \lfloor n \rfloor$ on $\mathbb{Z} \to \mathbb{Z}$.

---

## Topic 10: Relations

*(Covered in Tutorial)*

### 10.1 Binary Relations

A **binary relation** $R$ on a set $A$ is a subset of $A \times A$. We write $aRb$ or $(a,b) \in R$ to say $a$ is related to $b$.

### 10.2 Properties of Relations

**Reflexive:** $\forall a \in A, \; (a,a) \in R$ (every element relates to itself; diagonal of matrix is all 1s)

**Symmetric:** $\forall a,b \in A, \; (a,b) \in R \implies (b,a) \in R$ (matrix $M_R$ equals its transpose)

**Antisymmetric:** $\forall a,b \in A, \; (a,b) \in R \wedge (b,a) \in R \implies a = b$

**Transitive:** $\forall a,b,c \in A, \; (a,b) \in R \wedge (b,c) \in R \implies (a,c) \in R$

### 10.3 Equivalence Relations

A relation is an **equivalence relation** if it is reflexive, symmetric, and transitive.

**Equivalence class** of $a$: $[a] = \{b \in A \mid aRb\}$

**Example from tutorial:** On SIT students:
- $\{(a,b) \mid a \text{ and } b \text{ study in the same programme}\}$ — equivalence relation ✓ (reflexive, symmetric, transitive)
- $\{(a,b) \mid \text{GPA of } a \geq \text{GPA of } b\}$ — **not** symmetric (if GPA(a) > GPA(b), then b is not related to a)

### 10.4 Matrix Representation

A relation $R$ on $A = \{a_1, \ldots, a_n\}$ can be represented by an $n \times n$ boolean matrix $M_R$ where $M_R[i][j] = 1$ iff $(a_i, a_j) \in R$.

**Example from tutorial:** Given $M_R = \begin{pmatrix} 1&0&1&0 \\ 1&1&0&1 \\ 1&1&1&0 \\ 1&1&0&1 \end{pmatrix}$

- **Reflexive?** Check diagonal (1,1), (2,2), (3,3), (4,4): all 1 → **Yes**
- **Symmetric?** Check if $M_R = M_R^T$: Row 1 = $(1,0,1,0)$, Col 1 = $(1,1,1,1)$ → **No**
- **Antisymmetric?** Check if $(i,j) \in R$ and $(j,i) \in R$ implies $i=j$: $(1,3) \in R$ and $(3,1) \in R$ but $1 \neq 3$ → **No**
- **Transitive?** Check if $M_R^2$ (boolean product) has no 1 where $M_R$ has 0 in off-diagonal sense → check case-by-case.

### 10.5 Partial Orders

A relation that is reflexive, **antisymmetric**, and transitive is a **partial order**.

**Total order:** A partial order where every pair of elements is comparable.

---

## Quick Reference: Key Formulas

### Sequences
| Type | $n$th term | Sum of first $n$ terms | Sum to $\infty$ |
|---|---|---|---|
| Arithmetic | $a + (n-1)d$ | $\dfrac{n[2a+(n-1)d]}{2} = \dfrac{n(a_1+a_n)}{2}$ | — |
| Geometric ($r \neq 1$) | $ar^{n-1}$ | $\dfrac{a(1-r^n)}{1-r}$ | $\dfrac{a}{1-r}$ (if $|r|<1$) |

### Combinatorics
$$P(n,r) = \frac{n!}{(n-r)!}, \qquad C(n,r) = \frac{n!}{r!(n-r)!}$$

**Generalised Pigeonhole:** $N$ objects into $k$ boxes → at least one box has $\geq \lceil N/k \rceil$ objects.

### Number Theory
$$a = dq + r, \quad 0 \leq r < d \qquad (r = a \bmod d)$$
$$\gcd(a,b) \times \text{lcm}(a,b) = a \times b$$

Euclidean Algorithm: $\gcd(a,d) = \gcd(d, a \bmod d)$ (repeat until remainder = 0)

### Logic Connectives Summary
| Symbol | Name | True when |
|---|---|---|
| $\neg p$ | Negation | $p$ is false |
| $p \wedge q$ | Conjunction | both true |
| $p \vee q$ | Disjunction | at least one true |
| $p \oplus q$ | Exclusive OR | exactly one true |
| $p \to q$ | Conditional | not ($p$ true and $q$ false) |
| $p \leftrightarrow q$ | Biconditional | both same truth value |

### Rules of Inference (Summary)
- **Modus Ponens:** $p,\; p\to q \;\therefore q$
- **Modus Tollens:** $\neg q,\; p\to q \;\therefore \neg p$
- **Hypothetical Syllogism:** $p\to q,\; q\to r \;\therefore p\to r$
- **Disjunctive Syllogism:** $p\vee q,\; \neg p \;\therefore q$
- **Addition:** $p \;\therefore p \vee q$
- **Simplification:** $p \wedge q \;\therefore p$

### Proof Methods (When to Use)
| Goal | Method |
|---|---|
| Prove $p \to q$ | Direct proof: assume $p$, derive $q$ |
| Prove $p \to q$ (hard directly) | Contraposition: assume $\neg q$, derive $\neg p$ |
| Prove $p$ (not conditional) | Contradiction: assume $\neg p$, derive False |
| Disprove $\forall x\, P(x)$ | Find a counterexample |
| Prove for all cases | Cases: split domain, prove each |

---

*End of INF1003 Mathematics 1 Notes*
*Singapore Institute of Technology — Academic Year 2024/25*
