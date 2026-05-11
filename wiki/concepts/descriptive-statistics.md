---
type: concept
title: "Descriptive Statistics"
domain: mathematics
course: INF1004
complexity: medium
address: c-000019
tags: [statistics, data, descriptive, measures]
updated: 2026-05-11
---

# Descriptive Statistics

Descriptive statistics is the branch of statistics concerned with **collecting, organising, summarising, and presenting data**. It converts raw data into meaningful information without drawing broader conclusions (that is the role of inferential statistics). Probability theory bridges the two.

> **Ethics note:** Statistics should not be used to mislead. Ambiguous comparisons (e.g., "Our interest rates are 1% lower" — lower than which bank?) are a common form of deception.

---

## Types of Statistics

| Type | Purpose |
|------|---------|
| **Descriptive** | Organise, summarise, and describe outcomes from sample data |
| **Inferential** | Draw conclusions and make predictions about a population from sample data |

---

## Population vs Sample

| Concept | Description |
|---------|-------------|
| **Population** | The entire group of interest; measuring it fully (a census) is often impractical |
| **Sample** | A measurable subset used to infer population characteristics |

| Parameter / Statistic | Population | Sample |
|----------------------|------------|--------|
| Mean | μ | x̄ |
| Variance | σ² | s² |
| Standard Deviation | σ | s |
| Proportion | p | p̂ |

---

## Types of Data

```
Data
├── Quantitative (numeric)
│   ├── Discrete   — countable, distinct values (e.g., number of students)
│   └── Continuous — infinite possible values on a continuum (e.g., height, weight)
└── Qualitative (categorical)
    ├── Ordinal    — ordered categories (e.g., pain severity, satisfaction rating)
    └── Nominal    — unordered categories (e.g., eye colour, blood type)
```

---

## Data Presentation

### Categorical Data

- **Frequency table** — counts and relative frequencies per category
- **Bar chart** — bar height ∝ frequency
- **Pie chart** — slice size ∝ relative frequency

### Quantitative Data

| Dataset | Representation |
|---------|----------------|
| Small / discrete | Dot plot, stem-and-leaf display |
| Large / continuous | Histogram, ogive (cumulative relative frequency polygon) |
| Two variables | Crosstabulation (contingency table) — can show row % or column % |

**Histogram:** bars touch (no gaps); x-axis = class intervals, y-axis = frequency or relative frequency.

**Class selection:** use 5–14 classes; interval notation: 10 to < 13 (includes 10, excludes 13).

---

## Measures of Location (Central Tendency)

### Mean

**Population:**
$$\mu = \frac{\sum x_i f_i}{N}$$

**Sample:**
$$\bar{x} = \frac{\sum x_i f_i}{n}$$

### Median

The middle value when data are ordered. For grouped data:
$$\text{Median} = L_m + \left(\frac{\frac{n}{2} - cf_{m-1}}{f_m}\right) w_m$$

- $L_m$ = lower class boundary of the median class
- $cf_{m-1}$ = cumulative frequency before the median class
- $f_m$ = frequency of the median class
- $w_m$ = class width

### Mode

The data value with the highest frequency.

### Skewness and Central Tendency

| Distribution Shape | Relationship |
|--------------------|--------------|
| Skewed right | Mode < Median < Mean |
| Symmetric | Mode = Median = Mean |
| Skewed left | Mean < Median < Mode |

---

## Measures of Relative Standing

**Quartiles** divide data into four equal parts:
- Q1 = 25th percentile
- Q2 = 50th percentile (Median)
- Q3 = 75th percentile
- **IQR** = Q3 − Q1

**Boxplot (Box-and-Whisker Plot):**
- Box spans Q1 to Q3; line inside = Median
- Whiskers extend to the furthest values within 1.5 × IQR of Q1/Q3
- Points beyond whiskers = **outliers**

---

## Measures of Spread (Variability)

### Range

$$\text{Range} = \text{max} - \text{min}$$

### Variance and Standard Deviation

| | Population | Sample |
|--|------------|--------|
| Variance | $\sigma^2 = \frac{\sum(x_i - \mu)^2}{N}$ | $s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$ |
| Standard Deviation | $\sigma = \sqrt{\sigma^2}$ | $s = \sqrt{s^2}$ |

> Sample variance uses **n − 1** (Bessel's correction) to give an unbiased estimate of population variance.

### Coefficient of Variation (CV)

$$CV = \frac{\sigma}{\mu} \times 100\% \quad \text{(population)} \qquad CV = \frac{s}{\bar{x}} \times 100\% \quad \text{(sample)}$$

CV measures **relative variability** and is used as a measure of risk. It is particularly useful when comparing variables with different means and different standard deviations.

---

## Related Concepts

- [[probability-theory]] — probability as the bridge to inferential statistics
- [[probability-distributions]] — models for quantitative random variables
- [[sets-functions-relations]] — mathematical foundations for data structures
