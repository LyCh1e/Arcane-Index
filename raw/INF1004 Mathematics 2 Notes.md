# INF1004 Mathematics 2 Notes
**Singapore Institute of Technology (SIT)**
**Lecturer: Ryan Fraser Kirwan**

---

## Module Overview

**Mathematics II (Part 1) — Statistics and Probability**
**Mathematics II (Part 2) — Linear Algebra**

### Module Schedule (Trimester 2)

| Week | Topic |
|------|-------|
| 1 | Descriptive Statistics |
| 2 | Probability Theory |
| 3 | Discrete Probability Distributions |
| 4 | Continuous Probability Distributions |
| 5 | Continuous and Sampling Distributions |
| 6 | Continuation and Combination of Topics + Revision Sessions |
| 7 | **Recess Week** |
| 8 | Linear Equations and Matrices |
| 9 | Vectors and Geometry |
| 10 | Linear Transformations / Regression |
| 11 | Linear Systems + Homogeneous Systems and Null Spaces |
| 12 | Matrix Decomposition + Eigenvalues |
| 13 | Singular Value Decomposition (SVD) + Application of SVD to Machine Learning |
| 14 | **Exam Week** |

### Assessment
- **iRATs and tRATs** (Weeks 8–13, Assessments 1–5): 25% total (5% each: 3% iRAT, 2% tRAT)
- **Exam** (Week 14): 50% (half will be on first-half content, worth 25%)

### Optional Resources
- *OpenIntro Statistics* 2nd Ed. by David Diez, Christopher Barr and Mine Cetinkaya-Rundel
- *Mind on Statistics* 5th Ed. by J. M. Utts and R. F. Heckard, Cengage Learning, 2015
- *Introduction to Probability and Statistics* 14th Ed. by W. Mendenhall, R. J. Beaver and B. M. Beaver, Cengage Learning, 2013

---

# PART 1: STATISTICS AND PROBABILITY

---

## Week 1 — Descriptive Statistics (L1)

### 1.1 Introduction to Statistics

**What is Statistics?**
Statistics enables us to **collect** and **discover patterns in data** so as to **predict** and **make wiser decisions** for our questions.

**Two Types of Statistics:**

| Type | Description |
|------|-------------|
| **Descriptive** | Collecting, Organizing, Summarizing, Presenting data |
| **Inferential** | Making inferences, Hypothesis testing, Making predictions, Determining relationships |

**Probability Theory** is the basis to link Descriptive Statistics with Inferential Statistics.

- **Descriptive**: Turning data into information — organize, summarize, and describe the data (outcomes from sample data).
- **Inferential**: Making decision from data — given the outcomes, we can infer for the population in order to make decisions.

**Learning Outcomes for Statistics:**
1. **Turning Data into Information in life** — Use descriptive statistical techniques to organize, summarize and present data with graphical and numerical measures.
2. **Understanding Uncertainty in life** — Apply probability theory and distribution models to calculate probabilities of real-world events.
3. **Making Decisions from Data in life** — Conduct inferential statistical analysis and testing to draw conclusions from data.

**Important note:** Statistics should not be used to mislead. Ambiguous comparisons (e.g., "Our interest rates are 1% lower" — lower than which bank? By how much exactly?) can be deceptive.

---

### 1.2 Data and Samples

#### Population versus Sample

To be **accurate**, we need to conduct a census to collect all the data. But to be **practical**, sampling is commonly done instead.

- **Population**: The whole population which is usually large, is being measured (census), which can be costly and may be impractical/impossible.
- **Sample**: A small subset of the population that is measured, which is then used to **infer** the population.

The data collected from the population or sample are then used to compute the **population parameter** or **sample statistic** respectively.

| | Population | Sample |
|--|------------|--------|
| Mean | μ | x̄ |
| Variance | σ² | s² |
| Standard Deviation | σ | s |
| Proportion | p | p̂ |

> **Note:** Do not confuse "Statistics" as a branch of mathematics and "statistic" to mean a summary number of a sample.

---

### 1.3 Types of Data and Data Presentation

#### Types of Data

In Statistics, it is important to differentiate data/variables as **qualitative** (categorical or non-numeric) or **quantitative** (numeric) because they are treated differently.

```
Data
├── Quantitative (numeric)
│   ├── Discrete (countable) — Possible values form a set of separate numbers
│   └── Continuous (non-countable) — Possible values can take an infinite continuum of possible real number values
└── Qualitative (Categorical)
    ├── Ordinal (Hierarchical) — Pain severity, satisfaction rating
    └── Nominal (Non-hierarchical) — Eye colour, blood type
```

**Quantitative/Numerical variable** (scale for measurement is numerical values that differ in magnitude):
- Examples: Age, height, weight, BMI = weight(kg)/[height(m)]², GPA, time spent on Internet yesterday, reaction time to a stimulus

**Qualitative/Categorical variable** (scale for measurement is a set of categories):
- Examples: Racial-ethnic group (Asian, White, Black, Latino), political party identification, vegetarian? (yes, no), mental health evaluation, happiness (very happy, pretty happy, not too happy)

---

#### Representing Categorical Data

Qualitative (categorical) data are often summarized in a table using **frequency** or **relative frequency**.

**Frequency table example (M&Ms by colour):**

| Colour | Frequency | Relative Frequency | Percent |
|--------|-----------|-------------------|---------|
| Red | 3 | 3/25 = .12 | 12% |
| Blue | 6 | 6/25 = .24 | 24% |
| Green | 4 | 4/25 = .16 | 16% |
| Orange | 5 | 5/25 = .20 | 20% |
| Brown | 3 | 3/25 = .12 | 12% |
| Yellow | 4 | 4/25 = .16 | 16% |

Graphically, qualitative (categorical) data are commonly presented using **bar chart** or **pie chart**.
- Bar chart: Height of rectangle ∝ Frequency
- Pie chart: Slice size ∝ Relative Frequency

---

#### Representing Quantitative Data

**Small or discrete datasets** are often represented using:
- **Dot plot**: Each observation is a dot on a number line
- **Stem-and-leaf display**: Separates data into stems and leaves

**Large or continuous datasets** — Classes (covering continuous non-overlapping range of values) are commonly used to group data together.
- Use enough classes (usually 5–14) to show variation in data, but not too many that many contain only a few data items.
- Interval notation: 10 to < 13 (includes 10 but not 13)

**Histogram**: A bar graph where:
- X-axis: Class intervals
- Y-axis: Frequency or Relative Frequency
- Bars touch each other (no gaps)

**Cumulative relative frequency polygon (Ogive)**: A line graph showing cumulative relative frequency vs class boundaries.

**Crosstabulation (Contingency Tables)**: Can be used for both qualitative data, both quantitative data, or one qualitative vs one quantitative data. Entries can be converted into row percentages or column percentages for more insight.

---

### 1.4 Measures of Location (Central Tendency)

#### Mean

The sum of data values divided by the number of values.

**Population Mean:**
$$\mu = \frac{x_1 f_1 + x_2 f_2 + \ldots + x_k f_k}{f_1 + f_2 + \ldots + f_k} = \frac{\sum x_i f_i}{N}$$

**Sample Mean:**
$$\bar{x} = \frac{\sum x_i f_i}{n}$$

#### Median

Defined as the **middle data value** when the dataset has been ordered from the smallest to largest.

- If n is odd: Median = middle value
- If n is even: Median = average of the two middle values

**Grouped Data Median:**
$$Q = L_m + \left(\frac{\frac{n}{2} - cf_{m-1}}{f_m}\right) w_m$$

where:
- $L_m$ = lower class boundary of the median class
- $cf_{m-1}$ = cumulative frequency before the median class
- $f_m$ = frequency of the median class
- $w_m$ = class width

#### Mode

Defined as the **data value that has the highest frequency**.

**Comparison of Mean, Median, Mode:**
- Skewed right distribution: Mode < Median < Mean
- Symmetric distribution: Mode = Median = Mean
- Skewed left distribution: Mean < Median < Mode

---

### 1.5 Measures of Relative Standing

**Quartiles**: Values that divide the number of data points into four equal parts (quarters).
- Q1: 25th percentile
- Q2: 50th percentile (Median)
- Q3: 75th percentile
- Interquartile Range (IQR) = Q3 − Q1

**Box-and-Whisker Plot (Boxplot)**:
- Box spans from Q1 to Q3
- Line inside box = Median (Q2)
- Whiskers extend to the smallest/largest values within 1.5(IQR) of Q1/Q3
- Points beyond whiskers = Outliers (> 1.5 × IQR from Q1 or Q3)

**Percentiles**: The pth percentile is a value such that at least p% of the data fall at or below it and at least (100 − p)% fall at or above it.

---

### 1.6 Measures of Spread (Variability)

#### Range

Range = Largest data value − Smallest data value

#### Variance and Standard Deviation

Variance is defined as the **average of the squared deviations** ("distance") from the mean, where deviation is the difference between each data $x_i$ and the mean.

| | Population | Sample |
|--|------------|--------|
| Variance | $\sigma^2 = \frac{\sum(x_i - \mu)^2}{N}$ | $s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$ |
| Standard Deviation | $\sigma = \sqrt{\sigma^2}$ | $s = \sqrt{s^2}$ |

> **Note:** Sample variance uses (n−1) in the denominator (Bessel's correction) to give an unbiased estimate of the population variance.

**Coefficient of Variation (CV)**: A measure of relative variability.

$$CV = \frac{\sigma}{\mu} \times 100\% \quad \text{(population)} \qquad CV = \frac{s}{\bar{x}} \times 100\% \quad \text{(sample)}$$

- CV is often used as a measure of **risk**.
- Useful for comparing two or more variables having **different means** and **different standard deviations**.

---

## Week 2 — Probability Theory (L2)

### 2.1 The Probability Process

**Key Terms:**
- **Probability** (of an outcome): The frequency of occurrence of that outcome
- **Probability of a random outcome A** is P(A)
- **Sample space S**: The set of all possible outcomes of a random phenomenon; typically drawn using a Venn diagram with a rectangle
- **Probability of sample space**: P(S) = 1

**Visualization**: Through a Venn Diagram

**Data Collection:**
- Total experiments, Sample, Event
- Statistical interpretations (Relative freq.)
- Classical/Objective probability (Addition rule of prob.)
- Multi-Event Experiments (Multiplication rule of prob.)

---

### 2.2 Single-Event Probabilities

**Given a single event A, in sample space S:**
- Probability of sample space occurring is 1: P(S) = 1
- **Event A**: Defined as the set of outcomes that we are interested in, typically drawn using a circle or ellipse inside the rectangle.
- **Complementary event Ā**: Defined as the complementary event of A — the probability that A does **not** happen.
  - $P(\bar{A}) = 1 - P(A)$
- The sum of all probabilities is 1.

---

### 2.3 Interpretation of Probability

#### Classical (Objective) Probability

In classical interpretation, all random outcomes are considered to be **equally likely**.

$$P(A) = \frac{\text{Number of different outcomes in A}}{\text{Total number of possible outcomes}}$$

> This definition is not very practical for everyday life because it assumes the outcomes are equally likely.

#### Frequency (Empirical) Probability

Based on observed outcomes from repeated experiments.

$$P(A) = \frac{\text{Number of times A occurred}}{\text{Total number of trials}}$$

#### Subjective Probability

Based on personal judgment or expert opinion (e.g., "There is a 70% chance of rain tomorrow").

---

### 2.4 Probability of Events

**Given an additional event B:**
- **P(A ∩ B)**: Probability of intersection of events A and B = probability that both A and B occurring
- **P(A ∩ B) = 0** if A and B are **mutually exclusive** events
- **P(A ∪ B)**: Probability of union of events A and B = probability of either A or B or both occurring

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

For mutually exclusive events:
$$P(A \cap B) = 0 \implies P(A \cup B) = P(A) + P(B)$$

---

### 2.5 Multi-Event Experiment Probabilities

**Given two successive events A and B:**
- **P(A|B)**: Probability of event A occurring **given** B occurred first
- **P(B|A)**: Probability of event B occurring **given** A occurred first

$$P(A|B) = \frac{P(A \cap B)}{P(B)} \qquad P(B|A) = \frac{P(B \cap A)}{P(A)}$$

Note: $P(A|B) \neq P(B|A)$ in general.

---

### 2.6 Tree Diagrams

Tree diagrams are a useful representation of successive events:
- Each node represents an event and its branch is associated with a conditional probability.
- **Sum** of probability of each set of sibling branches is 1.
- **Multiply** along branches to get probability of the series of events.
- **Summing** probability across entire column also equals 1.

---

### 2.7 Conditional Probabilities

In practice, the probability of an event A can be **changed if additional information is available**, which leads to the discovery/creation of **conditional probability**.

**Formal Definition:**
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

**Example:** If P(E ∩ M) = 0.52, P(M) = 0.57:
$$P(E|M) = \frac{0.52}{0.57} = 0.91$$

---

### 2.8 Independent vs Mutually Exclusive Events

**Independent Events:** Two events A and B are independent if knowing that B has occurred does not change the probability of A occurring.

$$P(A|B) = P(A) \quad \text{or equivalently} \quad P(A \cap B) = P(A) \times P(B)$$

**Mutually Exclusive Events:** Two events A and B cannot occur at the same time.
$$P(A \cap B) = 0$$

> **Important distinction:** Independent ≠ Mutually Exclusive. In fact, mutually exclusive events (with non-zero probabilities) are **dependent** events.

**With replacement**: Events are independent (probability remains the same each draw).
**Without replacement**: Events are dependent (probability changes with each draw).

---

### 2.9 Bayes' Theorem and Law of Total Probability

**Law of Total Probability:** For mutually exclusive and exhaustive events $B_1, B_2, \ldots, B_k$:
$$P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + \ldots + P(A|B_k)P(B_k)$$

**Bayes' Theorem:**
$$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{P(A)}$$

**Classic Example:** 1% of population is allergic to cats. A medical test has 80% correct detection rate (sensitivity) and 10% false positive rate (1-specificity).

Let C = allergic to cat, T = test positive:
- P(C) = 0.01, P(T|C) = 0.80, P(T|C̄) = 0.10
- P(T) = P(T|C)P(C) + P(T|C̄)P(C̄) = (0.80)(0.01) + (0.10)(0.99) = 0.107
- P(C|T) = P(T|C)P(C) / P(T) = (0.80)(0.01) / 0.107 ≈ 0.075

So if a person tests positive, there is only ~7.5% probability they truly have the allergy.

---

## Week 3 — Discrete Probability Distributions (L3)

### 3.1 Random Variables

A **random variable (RV)** may be classified as **discrete** or **continuous**.

**Discrete Random Variable**: Can take one of a countable list of distinct values. We can find probabilities for exact outcomes.

**Continuous Random Variable**: Can take an infinite number of values (non-countable). We find probabilities for ranges of values.

---

### 3.2 Discrete Probability Distributions

A **probability distribution** for a discrete RV lists the probabilities for each possible value.

**Requirements:**
1. $0 \leq P(X = x_i) \leq 1$ for all $x_i$
2. $\sum P(X = x_i) = 1$

#### Expected Value (Mean)

$$\mu = E(X) = \sum x_i P(X = x_i)$$

**Law of Large Numbers**: As the number of trials increases, the mean outcome will tend to become equal to the expected value.

#### Variance and Standard Deviation

$$\sigma^2 = Var(X) = \sum (x_i - \mu)^2 P(X = x_i)$$
$$\sigma = \sqrt{\sigma^2}$$

---

### 3.3 Binomial Distribution

The **Binomial Distribution** assumes an experiment with:
- n identical trials
- Each trial has only two possible outcomes (success or failure)
- Each trial is **independent** of the previous ones
- Probability of success p is constant across trials

$$X \sim Bin(n, p)$$

**Probability distribution:**
$$P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x = 0, 1, 2, \ldots, n$$

where $\binom{n}{x} = \frac{n!}{x!(n-x)!}$

**Mean:** $\mu = np$

**Variance:** $\sigma^2 = np(1-p)$

**Identifying Binomial Distribution:**
1. Fixed number of trials n
2. Each trial results in one of two outcomes (success/failure)
3. Probability of success p is constant
4. Trials are independent

---

## Week 4 — Continuous Probability Distributions (L4)

### 4.1 Continuous Spaces

For a continuous random variable, the sample space contains an infinite number of possible values forming a continuum (e.g., angles from 0° to 360°).

$$P(0 \leq X \leq 180) = \frac{180-0}{360} = \frac{1}{2} = 0.5$$

---

### 4.2 Probability Density Functions (PDF)

Since there are **infinitely many values** (outcomes) for a continuous random variable, the probability for a **particular outcome** to occur is negligible:

$$P(X = x) = \int_x^x f(x)\,dx = 0$$

Instead, we find probability over **intervals**:

$$P(a \leq X \leq b) = \int_a^b f(x)\,dx$$

**Requirements for PDF $f(x)$:**
1. $f(x) \geq 0$ for all x
2. $\int_{-\infty}^{\infty} f(x)\,dx = 1$ (total area under curve = 1)

#### Mean and Variance of Continuous RV:
$$\mu = \int_{-\infty}^{\infty} x f(x)\,dx$$
$$\sigma^2 = \int_{-\infty}^{\infty} (x - \mu)^2 f(x)\,dx$$
$$\sigma = \sqrt{\sigma^2}$$

---

### 4.3 Uniform Distribution

$$X \sim Uniform(a, b)$$

$$f(x) = \frac{1}{b-a}, \quad a \leq x \leq b$$

**Mean:** $\mu = \frac{a+b}{2}$

**Variance:** $\sigma^2 = \frac{(b-a)^2}{12}$

---

### 4.4 Normal (Gaussian) Distribution

The **Normal distribution** is a model for continuous RVs that have a **bell-shaped curve** with thin tails.

$$X \sim N(\mu, \sigma^2)$$

**PDF:**
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty$$

**Properties:**
- Symmetric about mean μ
- Mean = Median = Mode = μ
- 68% of data within μ ± σ
- 95% of data within μ ± 2σ
- 99.7% of data within μ ± 3σ

---

### 4.5 Standard Normal Distribution

It is difficult to calculate probabilities of a normal distribution directly. To simplify, all normal distributions can be **transformed into a standard normal**.

$$Z \sim N(0, 1)$$

**PDF:**
$$f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}x^2}, \quad -\infty < x < \infty$$

**Z-transformation (standardisation):**
$$Z = \frac{X - \mu}{\sigma}$$

After finding Z, use Z-table to read off the probability.

**Example:** X ~ N(298, 3²), find P(X < 295):
$$P(X < 295) = P\left(Z < \frac{295-298}{3}\right) = P(Z < -1) = 0.1587$$

---

## Week 5 — Continuous and Sampling Distributions (L5)

### 5.1 Additional Continuous Distributions

**Combining Random Variables:**
If X and Y are **independent** random variables:
$$E(X + Y) = E(X) + E(Y)$$
$$Var(X + Y) = Var(X) + Var(Y)$$

**Example:** Time to travel home X ~ N(25, 3²) and time to clear airport screening Y ~ N(15, 2²). Let T = X + Y:
$$E(T) = 25 + 15 = 40$$
$$Var(T) = 9 + 4 = 13 \implies T \sim N(40, 13)$$

---

### 5.2 Statistical Studies

**Formulating a question into a parameter:**

| Study Type | Population Parameter | Sample Statistic |
|------------|---------------------|-----------------|
| One population mean | μ | x̄ |
| Population Mean of paired differences (dependent) | μ_d | d̄ |
| Population Mean of paired differences (independent) | μ₁ - μ₂ | x̄₁ - x̄₂ |

---

## Week 6 — Sampling Distribution (L6)

### 6.1 Sampling Methods

**Probability Sampling Methods:**

1. **Simple Random Sampling**: Every member of the population has an equal chance of being selected. Can be done with or without replacement.

2. **Systematic Sampling**: Members are placed in a certain order. Researcher selects a **random starting point** for the first sample member, then **skips a constant interval** to select other members.

3. **Stratified Random Sampling**: Population is divided into distinct sub-groups (strata) based on characteristics. A sample is taken from each stratum proportionally.

4. **Cluster Sampling**: Population is divided into clusters (usually by geography). All members within randomly selected clusters are sampled.

**Non-Probability Sampling Methods** (prone to bias): Convenience, Voluntary Response, Purposive, Snowball sampling.

---

### 6.2 Sampling Distribution of the Sample Mean

When we repeatedly sample from a population and compute the sample mean x̄, the **sampling distribution of x̄** describes the distribution of all possible x̄ values.

**Properties:**
- $E(\bar{x}) = \mu$ (the mean of sampling distribution equals the population mean)
- $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$ (Standard Error of the Mean)

---

### 6.3 Central Limit Theorem (CLT)

**Central Limit Theorem**: For a random sample of size n taken from a population with mean μ and standard deviation σ, when **n is large** (typically n ≥ 30), the sampling distribution of $\bar{x}$ is approximately normal:

$$\bar{x} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{approximately}$$

This applies **regardless of the shape of the original population distribution**.

**Standardisation for sampling distribution:**
$$Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}$$

**Example:** Cola filling machine fills cans with mean 12.1oz and standard deviation 0.2oz. For a 36-pack (n = 36):
$$P(\bar{x} < 12) = P\left(Z < \frac{12 - 12.1}{0.2/\sqrt{36}}\right) = P(Z < \frac{-0.1}{0.0\overline{3}}) = P(Z < -3) = 0.0013$$

---

# PART 2: LINEAR ALGEBRA

---

## Week 8 — Linear Equations and Matrices (L1)

### 8.1 System of Linear Equations (SLE)

A **System of Linear Equations** consists of multiple linear equations with multiple unknowns.

**Example:**
$$2x + 3y = -2 \quad (1)$$
$$3x + 4y = -6 \quad (2)$$

The coefficients of the variables can be shown in **matrix form**:
$$\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$$

For three equations:
$$1.3p - 2.0q + r = 7 \quad (1)$$
$$3.7p + 4.8q - 7r = 3 \quad (2)$$
$$4.1p + 3.8q + 12r = -6 \quad (3)$$

Matrix form:
$$\begin{pmatrix} 1.3 & -2.0 & 1 \\ 3.7 & 4.8 & -7 \\ 4.1 & 3.8 & 12 \end{pmatrix}$$

---

### 8.2 Introduction to Matrices

A **matrix** is a rectangular array of numbers arranged in rows and columns.

An m × n matrix has **m rows** and **n columns**:
$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$

**Special Matrices:**
- **Square matrix**: m = n
- **Column vector**: m × 1
- **Row vector**: 1 × n
- **Identity matrix (I)**: Square matrix with 1s on diagonal and 0s elsewhere
- **Zero matrix**: All entries are 0
- **Diagonal matrix**: Non-zero entries only on diagonal
- **Symmetric matrix**: $A = A^T$

---

### 8.3 Matrix Operations

#### Addition and Subtraction
Two matrices must have the **same dimensions** (same m and n).
$$(A + B)_{ij} = a_{ij} + b_{ij}$$

**Properties:**
- $A + B = B + A$ (Commutative)
- $(A + B) + C = A + (B + C)$ (Associative)
- $A + 0 = A$

#### Scalar Multiplication
$$kA = k \begin{pmatrix} a_{11} & \cdots \\ \vdots & \ddots \end{pmatrix} = \begin{pmatrix} ka_{11} & \cdots \\ \vdots & \ddots \end{pmatrix}$$

#### Transpose
The **transpose** of an m × n matrix A is an n × m matrix $A^T$ where $(A^T)_{ij} = a_{ji}$.

**Properties:**
- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(kA)^T = kA^T$
- $(AB)^T = B^T A^T$

#### Matrix Multiplication
The product **AB** is defined only if the number of **columns of A** = number of **rows of B**.

If A is m × n and B is n × p, then AB is m × p.

$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$

**Properties:**
- NOT commutative: AB ≠ BA in general
- Associative: (AB)C = A(BC)
- Distributive: A(B + C) = AB + AC
- $AI = IA = A$

---

### 8.4 Determinants

The **determinant** is crucial to the solution of linear equations.

#### 2×2 Determinant

For a square matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:

$$|A| = \det(A) = ad - bc$$

#### 3×3 Determinant (Cofactor Expansion)

Expanding along the first row:
$$\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11} \begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} - a_{12} \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} + a_{13} \begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}$$

**Example:**
$$\begin{vmatrix} 2 & 1 & 3 \\ -1 & 1 & 1 \\ 0 & 4 & 5 \end{vmatrix} = 0\begin{vmatrix} 1 & 3 \\ 1 & 1 \end{vmatrix} - 4\begin{vmatrix} 2 & 3 \\ -1 & 1 \end{vmatrix} + 5\begin{vmatrix} 2 & 1 \\ -1 & 1 \end{vmatrix}$$
$$= -4[2(1) - (-1)(3)] + 5[2(1) - (-1)(1)] = -4(5) + 5(3) = -20 + 15 = -5$$

**Properties of Determinants:**
- $\det(AB) = \det(A)\det(B)$
- $\det(A^T) = \det(A)$
- $\det(kA) = k^n \det(A)$ for n×n matrix
- If any row/column is all zeros, det = 0
- If two rows/columns are identical, det = 0
- If A is singular (non-invertible), det(A) = 0

---

### 8.5 The Inverse Matrix

The **inverse** of a square matrix A (denoted A⁻¹) satisfies:
$$AA^{-1} = A^{-1}A = I$$

**A is invertible (non-singular) if and only if det(A) ≠ 0.**

#### Inverse of 2×2 Matrix

$$A^{-1} = \frac{1}{|A|} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

#### Inverse using Row Reduction (Gauss-Jordan Method)

To find A⁻¹, set up augmented matrix [A | I] and row reduce to get [I | A⁻¹].

**Row Operations:**
1. Multiply a row by a non-zero scalar
2. Add a multiple of one row to another
3. Swap two rows

**Properties:**
- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$
- $\det(A^{-1}) = \frac{1}{\det(A)}$

---

### 8.6 Solving Systems of Linear Equations

#### Matrix Form: Ax = b

A system of equations Ax = b has a unique solution when:
- A is invertible (det(A) ≠ 0)
- Solution: **x = A⁻¹b**

#### Augmented Matrix and Row Reduction (Gauss-Jordan Elimination)

To solve [A | b], apply row operations to obtain row echelon form or reduced row echelon form.

**Row Operations:**
- Swap rows: $R_i \leftrightarrow R_j$
- Scale: $R_i \leftarrow kR_i$
- Add multiple: $R_i \leftarrow R_i + kR_j$

**Example:** Solving augmented matrix $\begin{pmatrix} 1 & 2 & | & 8 \\ 0 & 1 & | & 7 \end{pmatrix}$:

This gives: $0x + 1y = 7$ → $y = 7$, $1x + 2y = 8$ → $x = 8 - 14 = -6$

#### Types of Solutions:
- **Unique solution**: det(A) ≠ 0, unique x = A⁻¹b
- **Infinite solutions**: Underdetermined system (more unknowns than equations or redundant equations)
- **No solution**: Inconsistent system (contradiction like 0 = 5)

---

## Week 9 — Vectors and Geometry (L2)

### 9.1 Introduction to Vectors

A **vector** is a mathematical object that has both **magnitude** and **direction**.

**Notation:** $\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix}$ or $\mathbf{v} = (v_1, v_2, \ldots, v_n)$

**Magnitude (length):**
$$|\mathbf{v}| = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}$$

**Direction:** The angle θ that the vector makes with the positive x-axis (in 2D).

**Unit vector**: A vector with magnitude 1. To normalise a vector:
$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|}$$

---

### 9.2 Vector Operations

#### Addition and Subtraction
$$\mathbf{u} + \mathbf{v} = (u_1 + v_1, u_2 + v_2, \ldots, u_n + v_n)$$

#### Scalar Multiplication
$$k\mathbf{v} = (kv_1, kv_2, \ldots, kv_n)$$

---

### 9.3 Dot Product (Inner Product / Scalar Product)

$$\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \ldots + u_n v_n = \sum_{i=1}^{n} u_i v_i$$

**Geometric interpretation:**
$$\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos\theta$$

**Properties:**
1. Commutative: $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$
2. Distributive: $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$
3. Scalar multiplication: $(k\mathbf{u}) \cdot \mathbf{v} = k(\mathbf{u} \cdot \mathbf{v})$
4. $\mathbf{0} \cdot \mathbf{u} = 0$
5. $\mathbf{u} \cdot \mathbf{u} = |\mathbf{u}||\mathbf{u}|\cos 0 = |\mathbf{u}|^2$

**Orthogonality:** Two vectors are **perpendicular** (orthogonal) if and only if $\mathbf{u} \cdot \mathbf{v} = 0$.

---

### 9.4 Vectors in Higher Dimensions

Similar rules apply to vectors in 3D and above.

**Exercise:** Determine the magnitude, direction and components of vector V = (3, 2, 5):
$$|\mathbf{V}| = \sqrt{3^2 + 2^2 + 5^2} = \sqrt{38}, \quad \theta_V = 0.946 \text{ rad}$$

---

### 9.5 Vector Representation of a Line

**Line in ℝ² (Parametric form):**
$$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x_0 \\ y_0 \end{pmatrix} + t \begin{pmatrix} d_1 \\ d_2 \end{pmatrix}, \quad t \in \mathbb{R}$$

where $(x_0, y_0)$ is a point on the line and $(d_1, d_2)$ is the direction vector.

**Line in ℝ³ (Symmetric form):**
$$\frac{x - x_0}{d_1} = \frac{y - y_0}{d_2} = \frac{z - z_0}{d_3}$$

**Example:** Line $L_2$: $\frac{x-1}{2} = y + 1 = z$

Vector equation: $\mathbf{r} = (1, -1, 0) + t(2, 1, 1)$

---

## Week 10 — Linear Transformations (L3)

### 10.1 Transformation of an Image

Matrices can be used to **transform geometric objects** (translate, rotate, reflect, scale, shear).

If a triangle has vertices represented as columns of matrix A, and a transformation matrix B is applied:

$$BA = \text{transformed triangle}$$

**Common 2D Transformations:**

| Transformation | Matrix |
|----------------|--------|
| Reflect about x-axis | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ |
| Reflect about y-axis | $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ |
| Rotate by θ | $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ |
| Scale by factor k | $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ |
| Shear along x | $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ |

---

### 10.2 Row Transformations (Gaussian Elimination)

To solve a system of equations by using matrices, we use **row transformations** to obtain new matrices that have the same solution as the original system.

We use row transformations to obtain an **augmented matrix** whose numbers to the left of the vertical bar are the same as the multiplicative identity matrix.

**Three Elementary Row Operations:**
1. Swap two rows: $R_i \leftrightarrow R_j$
2. Multiply a row by a non-zero constant: $R_i \leftarrow kR_i$
3. Add a multiple of one row to another: $R_i \leftarrow R_i + kR_j$

**Example:**
$$\begin{pmatrix} 1 & 2 & | & 8 \\ 0 & 1 & | & 7 \end{pmatrix}$$
→ $y = 7$, $x + 2(7) = 8$ → $x = -6$

---

### 10.3 Linear Regression

Linear regression finds the best-fit line through data points.

**Simple Linear Regression Model:**
$$y = \beta_0 + \beta_1 x + \epsilon$$

where $\beta_0$ is the y-intercept, $\beta_1$ is the slope, and $\epsilon$ is the error term.

**In matrix form:**
$$\mathbf{y} = X\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

**Least Squares Solution:**
$$\hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y}$$

This minimises the sum of squared residuals: $\sum_{i=1}^n (y_i - \hat{y}_i)^2$.

---

### 10.4 Applications of Linear Transformations in Deep Learning

Linear transformations (matrix multiplications) are the core operation in neural networks.

**Convolution (CNN):** Applying a filter/kernel to an input volume using matrix operations to produce an output (activation map).

Example: A 7×7 input volume with 2 filters of size 3×3 produces a 3×3×2 output volume.

---

## Week 11 — Eigenvalues and Eigenvectors (L4)

### 11.1 Definition

Let A be an n×n matrix. A scalar λ is an **eigenvalue** of A if there exists a non-zero vector **e** (called an **eigenvector**) such that:

$$A\mathbf{e} = \lambda\mathbf{e}$$

**Interpretation:** An eigenvector is a special direction that is only scaled (not rotated) by the transformation A. The eigenvalue λ is the scaling factor.

**Example:**
$$A = \begin{pmatrix} 1 & 6 \\ 5 & 2 \end{pmatrix}, \quad \mathbf{u} = \begin{pmatrix} 6 \\ -5 \end{pmatrix}$$

$$A\mathbf{u} = \begin{pmatrix} 1 & 6 \\ 5 & 2 \end{pmatrix}\begin{pmatrix} 6 \\ -5 \end{pmatrix} = \begin{pmatrix} -24 \\ 20 \end{pmatrix} = -4\begin{pmatrix} 6 \\ -5 \end{pmatrix} = -4\mathbf{u}$$

So **u** is an eigenvector corresponding to eigenvalue **λ = -4**.

---

### 11.2 Finding Eigenvalues

**Characteristic Equation:**
$$(A - \lambda I)\mathbf{e} = \mathbf{0}$$

For non-trivial solutions (e ≠ 0):
$$\det(A - \lambda I) = 0$$

This is the **characteristic polynomial** of A. Solving for λ gives the eigenvalues.

**Example (3×3):** For $A = \begin{pmatrix} -1 & -1 & 2 \\ 1 & 2 & -1 \\ 0 & 1 & -1 \end{pmatrix}$:

$$\det(A - \lambda I) = 0 \implies (\lambda - 1)(\lambda + 1)^2 = 0$$
$$\lambda_1 = 1, \quad \lambda_2 = \lambda_3 = -1$$

---

### 11.3 Finding Eigenvectors

Once eigenvalues are found, substitute each λ back into $(A - \lambda I)\mathbf{e} = \mathbf{0}$ and solve the homogeneous system.

**Example:** For λ = -1 in the above:
$$2e_1 + e_2 - 2e_3 = 0 \quad (1)$$
$$-e_1 + 3e_2 + e_3 = 0 \quad (2)$$
$$e_2 = 0 \quad (3)$$

From (3): $e_2 = 0$; from (1): $2e_1 = 2e_3$ → $e_1 = e_3$.

Set $e_3 = 1$, then $e_1 = 1$: $\mathbf{e}^{(3)} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$

---

### 11.4 Eigendecomposition / Diagonalization

A matrix A can be **diagonalized** if it has n linearly independent eigenvectors.

$$A = PDP^{-1}$$

where:
- P = matrix of eigenvectors (columns)
- D = diagonal matrix of corresponding eigenvalues

**Benefit:** A diagonalized form is easy to manipulate in math operations.

$$A^2 = AA = (PDP^{-1})(PDP^{-1}) = PD(P^{-1}P)DP^{-1} = PD^2P^{-1}$$

In general: $A^n = PD^nP^{-1}$

Since D is diagonal, $D^n$ just means raising each diagonal element to the nth power.

---

## Week 12 — Singular Value Decomposition (L5)

### 12.1 Definition and Theorem

**Singular Value Decomposition (SVD)**: Any m×n matrix A can be decomposed as:

$$A_{(m \times n)} = U_{(m \times m)} \Sigma_{(m \times n)} V^T_{(n \times n)}$$

where:
- **U** = m×m matrix of **orthonormal** column vectors (left singular vectors): $\mathbf{u}_i = \frac{1}{\sigma_i} A\mathbf{v}_i$
- **Σ** = m×n matrix with **singular values** $\sigma_i = \sqrt{\lambda_i}$ on the diagonal (and zeros elsewhere)
- **V^T** = Transpose of n×n matrix of **orthonormal eigenvectors of A^TA** (right singular vectors)

The singular values $\sigma_1 \geq \sigma_2 \geq \ldots \geq \sigma_r > 0$ (where r = rank(A)).

---

### 12.2 Steps to Compute SVD

1. Compute $A^TA$ (an n×n symmetric matrix)
2. Find eigenvalues $\lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_n \geq 0$ of $A^TA$
3. Compute singular values $\sigma_i = \sqrt{\lambda_i}$
4. Find eigenvectors of $A^TA$ → these form the columns of V (normalise them!)
5. Compute $\mathbf{u}_i = \frac{1}{\sigma_i} A\mathbf{v}_i$ for each $\sigma_i \neq 0$
6. Assemble U, Σ, V^T

> **Important:** Always normalize eigenvectors when computing V and U, otherwise $U\Sigma V^T \neq A$.

---

### 12.3 Non-Uniqueness of U

The columns of U corresponding to zero singular values in Σ do not affect the product $U\Sigma V^T$. So any orthonormal vector can be used in those columns.

---

### 12.4 Applications of SVD

**1. Image Compression:**
A rank-r matrix can be approximated by a rank-k matrix (k < r) using the first k singular values and vectors:
$$A \approx \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^T + \ldots + \sigma_k \mathbf{u}_k \mathbf{v}_k^T$$

The larger singular values capture the most important features, so using only the largest k singular values gives a good approximation with less data.

**2. Dimensionality Reduction (PCA):**
SVD is the backbone of Principal Component Analysis. The columns of V (or rows of V^T) are the principal components, and the singular values indicate the importance of each component.

**3. Recommender Systems / Collaborative Filtering:**
SVD can decompose a user-item rating matrix into latent features of users and items.

**4. Solving Linear Systems:**
SVD provides the pseudoinverse $A^+ = V\Sigma^+U^T$, useful when A is not square or not invertible:
$$\hat{\mathbf{x}} = A^+\mathbf{b}$$

**5. Machine Learning / Deep Learning:**
- Weight matrix decomposition for model compression
- Data preprocessing and whitening
- Noise reduction in data

---

## Summary Tables

### Statistics Formula Sheet

| Measure | Population | Sample |
|---------|------------|--------|
| Mean | $\mu = \frac{\sum x_i f_i}{N}$ | $\bar{x} = \frac{\sum x_i f_i}{n}$ |
| Variance | $\sigma^2 = \frac{\sum(x_i-\mu)^2}{N}$ | $s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}$ |
| Std. Deviation | $\sigma = \sqrt{\sigma^2}$ | $s = \sqrt{s^2}$ |
| CV | $CV = \frac{\sigma}{\mu} \times 100\%$ | $CV = \frac{s}{\bar{x}} \times 100\%$ |

### Probability Rules Summary

| Rule | Formula |
|------|---------|
| Complement | $P(\bar{A}) = 1 - P(A)$ |
| Addition | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Mutually Exclusive | $P(A \cup B) = P(A) + P(B)$ |
| Conditional | $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ |
| Independence | $P(A \cap B) = P(A)P(B)$ |
| Bayes' | $P(B_i\|A) = \frac{P(A\|B_i)P(B_i)}{P(A)}$ |

### Probability Distributions Summary

| Distribution | PMF/PDF | Mean | Variance |
|-------------|---------|------|----------|
| Discrete RV | $P(X=x_i)$ | $\sum x_i P(X=x_i)$ | $\sum (x_i-\mu)^2 P(X=x_i)$ |
| Binomial | $\binom{n}{x}p^x(1-p)^{n-x}$ | $np$ | $np(1-p)$ |
| Uniform | $\frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| Normal | $\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |
| Standard Normal | $\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ | 0 | 1 |

### Sampling Distribution

| | Value |
|--|-------|
| Mean of $\bar{x}$ | $\mu$ |
| Std. Error | $\frac{\sigma}{\sqrt{n}}$ |
| CLT applies when | $n \geq 30$ |
| Z for $\bar{x}$ | $Z = \frac{\bar{x}-\mu}{\sigma/\sqrt{n}}$ |

### Linear Algebra Key Formulas

| Operation | Formula |
|-----------|---------|
| 2×2 Determinant | $ad - bc$ |
| 2×2 Inverse | $\frac{1}{\|A\|}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ |
| Solving SLE | $\mathbf{x} = A^{-1}\mathbf{b}$ |
| Dot Product | $\mathbf{u}\cdot\mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ |
| Eigenvalue eq. | $\det(A - \lambda I) = 0$ |
| Diagonalisation | $A = PDP^{-1}$, $A^n = PD^nP^{-1}$ |
| SVD | $A = U\Sigma V^T$ |
| Singular values | $\sigma_i = \sqrt{\lambda_i(A^TA)}$ |
| Left sing. vectors | $\mathbf{u}_i = \frac{1}{\sigma_i}A\mathbf{v}_i$ |
| Pseudoinverse | $A^+ = V\Sigma^+U^T$ |
| Least squares | $\hat{\mathbf{x}} = (X^TX)^{-1}X^T\mathbf{y}$ |

---

*Notes compiled from INF1004 Mathematics 2 lecture slides and summaries, SIT, Weeks 1–13.*
