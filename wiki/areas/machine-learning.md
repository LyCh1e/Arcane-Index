---
type: area
status: established
title: "Machine Learning"
domain: machine-learning
source: [[sources/INF2008-machine-learning]]
updated: 2026-08-18
tags: [area, machine-learning]
---

# Machine Learning

**Source**: INF2008 — Machine Learning, SIT.

---

## What I Know

ML is the practice of building systems that learn patterns from data rather than being explicitly programmed. INF2008 covers the full CRISP-DM lifecycle, supervised/unsupervised learning, model evaluation, and the mathematical foundations of key algorithms.

---

## Concept Pages

| Page | What It Covers |
|------|---------------|
| [[concepts/ml-foundations\|ML Foundations]] | CRISP-DM lifecycle, learning types (supervised/unsupervised/reinforcement), business value framing |
| [[concepts/ml-data-understanding\|ML Data Understanding]] | EDA, feature types, missing values, outliers, feature engineering, data splitting |
| [[concepts/ml-model-training-evaluation\|ML Training & Evaluation]] | Train/validation/test split, cross-validation, bias-variance tradeoff, precision/recall/F1, ROC-AUC |
| [[concepts/decision-trees-and-ensembles\|Decision Trees & Ensembles]] | ID3/CART, information gain, Gini impurity, Random Forests, Bagging, Boosting (AdaBoost, XGBoost) |
| [[concepts/neural-networks-linear-models\|Neural Networks & Linear Models]] | Linear/logistic regression, perceptron, MLP, backpropagation, activation functions, CNNs |
| [[concepts/clustering-and-dimensionality-reduction\|Clustering & Dimensionality Reduction]] | K-Means, DBSCAN, Hierarchical clustering, PCA, t-SNE |
| [[concepts/ai-in-medicine\|AI in Medicine]] | Publication growth (1995–2023), data modalities, OOD detection, surgical AI, data annotation bottleneck |
| [[concepts/medmnist-v2-datasets\|MedMNIST v2 Datasets]] | 18 medical imaging benchmarks: modality, task type, split sizes, pitfalls, metric selection guide |
| [[concepts/ml-classification-models\|ML Classification Models]] | kNN (lazy learning, O(n) prediction, curse of dimensionality) and SVM (max-margin hyperplane, kernel trick, C parameter) |
| [[concepts/ml-evaluation-metrics\|ML Evaluation Metrics]] | 6 metric families, classification/segmentation/detection metrics, pitfall gallery (14 entries), Metrics Reloaded framework (Nature Methods 2024) |
| [[concepts/digital-image-processing\|Digital Image Processing]] | Grayscale/RGB/HSV image models, point operations (histogram/stretching/equalisation/LUTs), convolution, smoothing, edge detection (Sobel), CNN connection |

---

## Key Ideas

- **CRISP-DM** is iterative, not linear: Business Understanding → Data Understanding → Data Preparation → Modelling → Evaluation → Deployment; revisit earlier phases when evaluation fails
- **Bias-variance tradeoff**: high bias = underfitting (too simple); high variance = overfitting (too complex). Cross-validation finds the sweet spot
- **Ensembles beat single models**: Random Forest (bagging = parallel, reduces variance); Boosting (sequential, reduces bias). XGBoost adds regularisation
- **Backpropagation** = chain rule of calculus applied layer-by-layer to compute ∂Loss/∂weight; requires differentiable activation functions
- **PCA** reduces dimensionality by projecting onto eigenvectors of the covariance matrix (= top singular vectors of the data matrix via SVD)

---

## Cross-Domain Connections

- [[synthesis/maths-to-ml-bridge|Mathematics → ML]] — linear algebra, probability, and statistics that underpin every algorithm here
- [[concepts/linear-algebra-matrices|Linear Algebra]] — weight matrices in neural networks, dot products, matrix multiplication
- [[concepts/eigenvalues-and-svd|Eigenvalues & SVD]] — PCA's mathematical engine
- [[concepts/probability-distributions|Probability Distributions]] — Gaussian Naive Bayes, model evaluation statistics
- [[concepts/algorithm-complexity|Algorithm Complexity]] — training complexity varies: linear regression O(n·d²), k-means O(n·k·d·i)

---

## Study Notes

*(none yet — INF2008 study-notes page not yet created)*
