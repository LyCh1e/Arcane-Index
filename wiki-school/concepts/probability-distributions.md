---
type: concept
title: "Probability Distributions"
domain: mathematics
course: INF1004
complexity: high
address: c-000021
tags: [probability, distributions, binomial, normal, CLT, sampling]
updated: 2026-05-11
status: established
created: 2026-05-11
---

# Probability Distributions

A **probability distribution** describes all possible values of a random variable and their associated probabilities. Distributions are either **discrete** (countable outcomes) or **continuous** (infinite continuum of outcomes).

---

## Random Variables

| Type | Description |
|------|-------------|
| **Discrete** | Takes one of a countable list of distinct values; probabilities for exact values exist |
| **Continuous** | Takes values on an infinite continuum; only probabilities over *intervals* are meaningful |

---

## Discrete Distributions

### Requirements for a Valid Discrete Distribution

1. $0 \leq P(X = x_i) \leq 1$ for all $x_i$
2. $\sum P(X = x_i) = 1$

### Expected Value (Mean)

$$\mu = E(X) = \sum x_i\, P(X = x_i)$$

**Law of Large Numbers:** As the number of trials increases, the sample mean converges to the expected value.

### Variance and Standard Deviation

$$\sigma^2 = \text{Var}(X) = \sum (x_i - \mu)^2\, P(X = x_i)$$
$$\sigma = \sqrt{\sigma^2}$$

---

## Binomial Distribution

$$X \sim \text{Bin}(n,\, p)$$

**Four conditions (FINS):**
1. **F**ixed number of trials n
2. **I**ndependent trials
3. **N**ominal outcomes (only success or failure)
4. **S**ame probability of success p per trial

$$P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x = 0, 1, \ldots, n$$

| Parameter | Value |
|-----------|-------|
| Mean | $\mu = np$ |
| Variance | $\sigma^2 = np(1-p)$ |

---

## Continuous Distributions

### Probability Density Functions (PDF)

For a continuous RV, $P(X = x) = 0$ for any single value. Instead:

$$P(a \leq X \leq b) = \int_a^b f(x)\,dx$$

**Requirements for a valid PDF:**
1. $f(x) \geq 0$ for all x
2. $\int_{-\infty}^{\infty} f(x)\,dx = 1$

**Mean and Variance:**
$$\mu = \int_{-\infty}^{\infty} x\,f(x)\,dx \qquad \sigma^2 = \int_{-\infty}^{\infty} (x-\mu)^2 f(x)\,dx$$

---

### Uniform Distribution

$$X \sim \text{Uniform}(a,\, b)$$

$$f(x) = \frac{1}{b-a}, \quad a \leq x \leq b$$

| Parameter | Value |
|-----------|-------|
| Mean | $\frac{a+b}{2}$ |
| Variance | $\frac{(b-a)^2}{12}$ |

---

### Normal (Gaussian) Distribution

$$X \sim N(\mu,\, \sigma^2)$$

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

**Properties:**
- Bell-shaped; symmetric about μ
- Mean = Median = Mode = μ
- Empirical rule:
  - 68% of data within μ ± σ
  - 95% of data within μ ± 2σ
  - 99.7% of data within μ ± 3σ

---

### Standard Normal Distribution

All normal distributions are transformed to $Z \sim N(0,\, 1)$ for table lookup:

$$Z = \frac{X - \mu}{\sigma}$$

**PDF:** $f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$

**Example:** $X \sim N(298,\, 3^2)$; find $P(X < 295)$:
$$P\!\left(Z < \frac{295 - 298}{3}\right) = P(Z < -1) = 0.1587$$

---

### Combining Independent Random Variables

For independent X and Y:
$$E(X + Y) = E(X) + E(Y)$$
$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$$

**Example:** $X \sim N(25,\, 9)$, $Y \sim N(15,\, 4)$, $T = X + Y$:
$$T \sim N(40,\, 13)$$

---

## Sampling Distributions

When the sample mean x̄ is computed across many repeated samples, its behaviour follows the **sampling distribution of x̄**:

$$E(\bar{x}) = \mu \qquad \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \quad \text{(Standard Error)}$$

### Central Limit Theorem (CLT)

For a sample of size n from **any** population with mean μ and standard deviation σ:

$$\bar{x} \sim N\!\left(\mu,\, \frac{\sigma^2}{n}\right) \quad \text{approximately, when } n \geq 30$$

**Z-statistic for sample mean:**
$$Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}$$

**Example:** Cola machine, μ = 12.1 oz, σ = 0.2 oz, n = 36:
$$P(\bar{x} < 12) = P\!\left(Z < \frac{12 - 12.1}{0.2/6}\right) = P(Z < -3) = 0.0013$$

---

## Sampling Methods

| Method | Description |
|--------|-------------|
| **Simple Random** | Every member has equal chance; with or without replacement |
| **Systematic** | Random start, then every kth member |
| **Stratified Random** | Divide into strata; sample proportionally from each |
| **Cluster** | Divide into clusters; sample all members from selected clusters |
| **Non-probability** | Convenience, voluntary response, purposive, snowball — all prone to bias |

---

## Distributions Summary Table

| Distribution | PMF / PDF | Mean | Variance |
|-------------|-----------|------|----------|
| Discrete RV | $P(X=x_i)$ | $\sum x_i P(X=x_i)$ | $\sum (x_i-\mu)^2 P(X=x_i)$ |
| Binomial | $\binom{n}{x}p^x(1-p)^{n-x}$ | $np$ | $np(1-p)$ |
| Uniform | $\frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| Normal | $\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |
| Standard Normal | $\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ | 0 | 1 |

---

## Related Concepts

- [[probability-theory]] — probability rules underpinning all distributions
- [[descriptive-statistics]] — summary statistics that distributions model
- [[combinatorics]] — factorials and combinations appear in binomial PMF
