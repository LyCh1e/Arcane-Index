---
type: concept
title: "ML Data Understanding"
domain: machine-learning
course: INF2008
complexity: medium
address: c-000027
tags: [machine-learning, EDA, data-types, leakage, feature-engineering, data-quality]
updated: 2026-05-11
---

# ML Data Understanding

Data Understanding (DU) is the second phase of CRISP-DM. It is about **meaning**, not cleaning — the goal is to determine what this data can and cannot tell you before any modelling begins. Most successful models are successful because of good data understanding.

> "Data Understanding → typically referred to as **EDA** (Exploratory Data Analysis)"
> "Data Preparation → typically referred to as **data engineering**"

---

## Seven Stages of Data Understanding

### Stage 0 — Data Generation Process

Ask before looking at a single value:
- How was this data collected?
- By whom, and under what conditions?
- What incentives or constraints shaped the collection?
- Can this data be trusted, and if so, what are the constraints?

### Stage 1 — Schema: What Does This Data Mean?

- What does each variable represent?
- Where was it generated?
- Where might it mislead?

**Common DU catches:** Treating IDs, timestamps, or audit labels as meaningful features.

**Key distinction:**
- **Independent variables (features):** Inputs provided to the model (e.g., age, income, study hours).
- **Target variable (label):** The output the model predicts (e.g., loan approval, exam score).

---

### Stage 2 — Data Types

#### Cardinal Data

Represents **quantities** — arithmetic operations (addition, averaging) are meaningful.

| Sub-type | Description | Example |
|----------|-------------|---------|
| **Continuous** | Any real value in a range | Temperature, yield percentage |
| **Discrete** | Countable integers | Defect count, number of retries |

> The term *cardinal* is used deliberately — some numerical-looking variables are actually categorical.

#### Categorical Data

Represents **labels or groups** — arithmetic operations are NOT meaningful.

| Sub-type | Description | Example |
|----------|-------------|---------|
| **Nominal** | No intrinsic order | Lot number, blood type, colour |
| **Ordinal** | Meaningful order, but equal spacing must NOT be assumed | Low < Medium < High; satisfaction rating |

#### HDB Price Prediction — Example Type Classification

| Variable | Role | Type |
|----------|------|------|
| Listing Number | Identifier | Categorical (Nominal) |
| Location | Independent | Categorical (Nominal — district names) |
| Distance from MRT | Independent | Cardinal (Continuous) |
| Size (sqm) | Independent | Cardinal (Discrete) |
| Years since TOP | Independent | Cardinal (Discrete) |
| Number of rooms | Independent | Cardinal (Discrete) |
| Number of bathrooms | Independent | Cardinal (Discrete) |
| Floor level | Independent | Cardinal (Discrete) |
| Unit price | **Target** | Cardinal (Continuous) |

---

### Stage 3 — Completeness

- Are there missing values?
- Which variables have disproportionate missingness?
- Are missing values: random? systematic? encoded inconsistently (NaN vs empty string vs "N/A")?

**Critical question:** What does "missing" actually mean here? A missing value can itself be informative (e.g., missing income may indicate unemployment).

---

### Stage 4 — Sanity Checks

**Plausibility:**
- Are values within realistic ranges? (Any HDBs over 100 years old?)
- Do minimums/maximums make sense?
- Are there impossible combinations? (1-room flat with 3 showers)
- Are units consistent? (Some rows in psf, others in psm?)

**Consistency:**
- Are categories spelled consistently? (*AngMoKio* vs *AMK* vs *Ang Mo Kio*)
- Do group-level summaries contradict expectations?

**Data Leakage:**
The most dangerous form of sanity failure. A feature that directly or indirectly contains the target causes the model to appear to perform well — but it is simply reading the answer.

> Example: `resale_price_per_sqm` is derived from the resale price itself — including it gives the model the target directly.

---

### Stage 5 — Representativeness

- Are some classes under-represented? (**class imbalance**)
- Are some groups entirely absent? (No 4-room HDB data from Toa Payoh)
- Is the data representative of the population you will predict on?
- Are some categories rare but critically important? (HDBs nearing the 99-year lease limit)

---

### Stage 6 — Granularity and Aggregation

- Is the granularity correct for the task? (Getting HDB price every day is probably excessive)
- Are there repeated entities that should be aggregated?
- Are there composite values that should be split?

**Aggregation example:** A flat listed multiple times across years → keep only transaction rows.

**Split example:** Amenities encoded as `"MRT,School,Market"` → split into separate binary indicator columns.

---

### Stage 7 — DU Conclusion

DU must end with a clear judgement:
- What analyses would be **unsafe** with this data?
- What conclusions would be **unreliable**?
- What **assumptions** are required before proceeding?

These define the **limitations** of the dataset — and they must be documented.

---

## Summary — What Each Stage Catches

| Stage | Failure Mode Detected |
|-------|----------------------|
| 0. Generation Process | Collection bias, incentive bias |
| 1. Schema | Meaningless features (IDs, timestamps used as predictors) |
| 2. Data Types | Treating nominal as ordinal, treating ordinal as cardinal |
| 3. Completeness | Missing data bias, inconsistent encoding |
| 4. Sanity Checks | Impossible values, unit inconsistencies, data leakage |
| 5. Representativeness | Class imbalance, sampling gaps |
| 6. Granularity | Duplicates, inappropriate aggregation/splitting |
| 7. Conclusion | Undocumented assumptions passed silently to modelling |

---

## Related Concepts

- [[ml-foundations]] — CRISP-DM context and the business understanding phase
- [[ml-model-training-evaluation]] — data splits and stratification depend on correct type understanding
- [[descriptive-statistics]] — statistical techniques used during EDA (mean, variance, quartiles, distributions)
