---
type: source
status: established
title: "Trustworthy AI Summer School — Lecture 2b: ML Classification Models"
course: "Trustworthy AI: Machine Learning Meets Blockchain (Microcredential 2)"
institution: OTH Regensburg / TU Munich
lecturer: "Tobias Rueckert, M.Sc."
domain: machine-learning
ingested: 2026-08-17
tags: [source, machine-learning, classification, kNN, SVM, decision-trees, ID3, CART, random-forests, kernel-trick]
---

# Trustworthy AI Summer School — Lecture 2b: ML Classification Models

**Course:** International Summer School: Trustworthy AI — Machine Learning Meets Blockchain, Microcredential 2: Machine Learning
**Lecturer:** Tobias Rueckert, M.Sc. (OTH Regensburg, TU Munich, AKTORmed Robotic Surgery)
**Raw file:** `raw/Machine_Learning_Lec_2b.md`

---

## Overview

A survey of classical supervised classification algorithms, presented with a consistent visual language from Lec 2a. Algorithms covered: kNN, SVM (with kernel trick), Decision Trees (ID3 and CART), and Random Forests.

Notebooks referenced:
- `01_Decision_Tree_ID3.ipynb`
- `02_Decision_Tree_CART.ipynb`
- `03_ML_Classifiers_Tutorial.ipynb`

---

## Algorithms Covered

### k-Nearest Neighbours (kNN)

- **Type:** Supervised; lazy learning (no training phase — stores training data)
- **Classification:** majority voting among the k nearest neighbours (by Euclidean distance, or other metric)
- **Regression:** average of k nearest neighbours
- **Advantages:** Simple; no training; flexible decision boundaries
- **Disadvantages:** O(n) prediction cost; sensitive to feature scaling; curse of dimensionality in high dimensions

### Support Vector Machines (SVM)

- **Type:** Supervised; finds the hyperplane that maximises the margin between classes
- **Support vectors:** The training points closest to the hyperplane; they define it
- **Kernel trick:** Maps data implicitly into a higher-dimensional space using a kernel function (RBF, polynomial) to find linear separation without explicitly computing new feature vectors
- **C parameter:** Controls the bias-variance tradeoff: large C → small margin, fewer errors; small C → large margin, more tolerance for misclassification
- **Advantages:** Effective in high dimensions; margin maximisation provides regularisation; non-linear boundaries via kernels
- **Disadvantages:** Slow on large datasets; kernel/hyperparameter choice requires expertise; less interpretable

Kernel examples shown:
- Quadratic transformation: makes 1D inseparable data separable in 2D
- Modulo transformation: φ(x) = x mod 2 separates even/odd values
- 2nd-degree polynomial mapping: φ([x₁,x₂]) = [x₁², √2·x₁x₂, x₂²] separates concentric circles in 3D

### Decision Trees — ID3 Algorithm

- **Full name:** Iterative Dichotomiser 3
- **Type:** Greedy algorithm; selects the feature with maximum information gain at each split
- **Split criterion:** Information gain I(S,θ) = H(S) − Σ |Sᵢ|/|S| · H(Sᵢ)
- **Entropy:** H(S) = −Σ p(c) log p(c)
- **Worked example:** Weather/golf dataset (14 instances, 4 features)
  - H(S¹) = 0.940286 (9 yes, 5 no)
  - I(Weather) = 0.247 → selected as root
  - I(Temperature) = 0.029, I(Humidity) = 0.152, I(Wind) = 0.048
  - Result: Weather → {Cloudy: Yes all; Sunny: Humidity split; Rainy: Wind split}
- **Limitation:** Greedy does not guarantee globally optimal tree; does not handle numerical features; no built-in pruning

### ID3 vs CART Comparison

| Property | ID3 | CART |
|----------|-----|------|
| Feature types | Categorical only | Categorical and numerical |
| Split structure | Multi-way (one branch per value) | Binary only (always two children) |
| Feature reuse | Each feature used at most once per path | Same feature can appear multiple times |
| Split criterion | Information gain (entropy) only | Entropy or Gini — freely chosen |
| Pruning | None — grows until pure (overfits) | Built-in cost-complexity pruning |

### Gini Index

G = Σ p(i) · (1 − p(i))

- Probability of misclassifying a randomly chosen element
- Faster than entropy (no logarithms)
- Isolates the most frequent class earlier
- Default criterion in scikit-learn

### Random Forests

- Bootstrap aggregating (bagging) of decision trees + random feature subset per node
- Additional feature subsampling beyond standard bagging to reduce tree correlation
- Reduces overfitting; lower variance; more stable predictions than a single tree

---

## Quality Assessment

| Criterion | Rating |
|-----------|--------|
| Specificity | High — algorithms presented with mathematical definitions, visual examples, trade-off tables |
| New vs existing wiki content | kNN and SVM are entirely new; ID3 algorithm name and worked example are new; ID3 vs CART table is new; Random Forest content already in `decision-trees-and-ensembles.md` |

---

## Extracted To

- [[concepts/ml-classification-models]] — kNN and SVM (new algorithms, not in any prior wiki page)
- [[concepts/decision-trees-and-ensembles]] — ID3 named algorithm with worked golf example; ID3 vs CART comparison table
