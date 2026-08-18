---
type: concept
title: "ML Model Training & Evaluation"
domain: machine-learning
course: INF2008
complexity: high
address: c-000028
tags: [machine-learning, evaluation, cross-validation, bias-variance, confusion-matrix, precision, recall, F1, baseline]
updated: 2026-05-11
status: established
created: 2026-05-11
---

# ML Model Training & Evaluation

Training a model well requires more than fitting data — it requires systematic evaluation strategies that reveal whether the model will generalise to unseen data.

---

## Baseline Models

A **baseline model** is a simple reference model built with minimal assumptions and default settings. It establishes the minimum acceptable performance level against which all subsequent models are compared.

### What Counts as a Baseline?

| Baseline Type | Description |
|---------------|-------------|
| **Majority class classifier** | Always predict the most frequent class (e.g., if 82% are "No", always predict "No") |
| **Mean predictor** | Always predict the mean target value from the training set (for regression) |
| **Decision Tree with defaults** | Default hyperparameters, no tuning |

---

## Data Splits

### Train–Validate–Test

| Set | Role |
|-----|------|
| **Training** | Fit models; used repeatedly during hyperparameter tuning |
| **Validation** | Guide tuning decisions; compare candidate models |
| **Test** | Final judge — used **once** at the end; provides an unbiased estimate of real-world performance |

> Test data must **never** influence training or model selection. Using test data during selection is a form of data leakage.

### Model Initialisation vs Fitting

- **Initialisation:** The moment a model is defined before seeing data. No patterns learned; hyperparameters fixed; learning capacity set.
- **Fitting:** Training data is introduced; internal parameters are optimised to minimise the loss, subject to the constraints set at initialisation.

---

## Stratification

**Stratification** ensures each data split preserves the same class proportions as the original dataset.

**Why it matters:** Without stratification, minority classes may be under-represented in the test set, making performance metrics unreliable.

**Example:** 300 students, 30% ICT / 70% Non-ICT, 80/20 split → test set should have 18 ICT and 42 Non-ICT — not 8 and 52.

> **M&Ms analogy:** Bowl of 950 Red and 50 Blue. Without stratification, a random grab of 20 likely contains 0 Blue. With stratification, deliberately pick 19 Red + 1 Blue.

### Patient-Level Split — The Medical Imaging Leakage Trap

In medical imaging, a single patient may produce many images (multiple CT slices, multiple frames of video, multiple timepoints). A **random split by image** will frequently put two images of the same patient on opposite sides of the train/test boundary.

This is data leakage: the model has seen the patient's tissue, scanner characteristics, and presentation style during training. The test score then measures memory, not generalisation.

**Rule: always split by patient (or by study or acquisition session), never by image.**

```
WRONG — split by image:
  train: P1-img1  P4-img2  P2-img1  P3-img1 ...
  test:  P1-img2  P2-img3  P3-img2  ...          ← P1, P2, P3 on both sides

CORRECT — split by patient:
  train: P1 (all images)  P2 (all images)  P3 (all images) ...
  test:  P4 (all images)                                     ← P4 only on test side
```

A test score from an image-level random split is indefensible in any clinical publication.

---

### Training and Validation Curves

Plotting loss (or accuracy) over training epochs reveals the training regime:

```
Loss
│  ╲
│   ╲  Training loss (blue) — always falls; proves nothing on its own
│    ╲___________
│         ╲
│          ╲___  Validation loss (orange) — falls then rises: the honest signal
│              ╲____  ← overfitting begins here
└──────────────────── Epochs
      ↑         ↑
  underfitting  sweet spot  overfitting
```

**Reading the curves:**

| Pattern | Diagnosis |
|---------|-----------|
| Both curves high and flat | Underfitting — model too simple, or learning rate too small |
| Training falls, validation falls together | Healthy training |
| Training falls, validation flat | Dataset too small, or bad features |
| Training falls, validation rises | Overfitting — model memorising training data |
| Training and validation both noisy / chaotic | Learning rate too high |

### Early Stopping

Keep the parameters from the epoch where the **validation loss was lowest** — not the last epoch. Training until the last epoch typically overfits.

**Practical implementation:**
```python
best_val_loss = float('inf')
for epoch in range(n_epochs):
    train(...)
    val_loss = evaluate_on_validation(...)
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        save_checkpoint(model)  # save the best parameters

load_checkpoint(model)  # restore best before final test evaluation
```

Most frameworks (PyTorch Lightning, Keras) have built-in early stopping callbacks with a `patience` parameter (how many epochs to wait after the last improvement).

---

## Experimental Integrity

Principles from Lecture 3 of the ML Summer School that determine whether a result can be trusted before the metric is even chosen.

### The Test Set Is a One-Shot Resource

> "If the test set influenced any decision you made, it is no longer a test set — it is a second validation set."

Every look at the test set spends a little of its integrity. Selecting a model, a threshold, or an architecture by test score is training on the test set — done by hand.

**The winner's curse:** the best of 20 noisy configurations is biased upward. The gap reported will shrink on the next dataset. Leaderboards make this systematic.

**Five-step test set protocol:**
1. Split first — before looking at anything, including computing normalisation statistics.
2. Develop against the validation set only.
3. Freeze the model, threshold, and code.
4. Run the test set once. Report what comes out.
5. Changed something afterwards? State that explicitly.

### Five Forms of Data Leakage

Beyond the patient-level split trap (see above), leakage appears in four additional forms:

| Form | Example |
|------|---------|
| **Same patient in both sets** | Two eyes of one patient, or left and right knee — same anatomy on both sides |
| **Neighbouring frames** | Video at 25 fps: frame 100 and frame 101 are effectively the same image |
| **Preprocessing before split** | Normalisation statistics, resampling, or feature selection computed on all data before splitting |
| **Duplicates and re-uploads** | Public datasets frequently overlap — the same case appears under two IDs |
| **Tuning on the test set** | Choosing epoch count, threshold, or architecture by test score |

**The one question to answer:** "What is the unit that must never appear on both sides?" (patient, eye, video, whole-slide image, hospital, annotator). Split by that unit — never by row.

Use `StratifiedGroupKFold` to stratify by label *and* group by patient simultaneously.

### Confidence Intervals — How Precise Is the Number?

```
half-width ≈ 1.96 · √( p(1−p) / n )
```

Precision grows with √n, not with n. Concrete examples for a measured accuracy of 0.90:

| Test-set size | 95% CI |
|--------------|--------|
| n = 20 | [0.70, 0.97] (±13.7 pt) |
| n = 50 | [0.79, 0.96] (±8.5 pt) |
| n = 100 | [0.83, 0.94] (±6.0 pt) |
| n = 250 | [0.86, 0.93] (±3.7 pt) |
| n = 1 000 | [0.88, 0.92] (±1.9 pt) |

Below roughly a hundred test samples, almost nothing is distinguishable. At n=50, "0.90 beats 0.86" is within sampling noise — not a meaningful claim.

**Two separate uncertainties:** the CI above covers only the finite test set. Re-training with different random seeds adds a second spread — report both: mean ± std over ≥ 3 seeds.

### Controlled Comparison — One Change at a Time

Stacking multiple changes in a single experiment produces a number, not knowledge:

| Variant | Score | Δ |
|---------|-------|---|
| Baseline | 0.71 | — |
| Baseline + augmentation | 0.79 | +0.08 |
| Baseline + new backbone | 0.73 | +0.02 |
| Baseline + 3× epochs | 0.72 | +0.01 |

Changing all three at once gives +0.15 — but the experiment cannot say which of the three earned it. Keep everything frozen except the one thing being tested.

### External Validation and the Generalisation Gap

An internal test set cannot measure generalisation to different sites, scanners, or patient populations.

Example: one model trained on Site A only, tested at three sites:
- Site A (training data): 0.91
- Site B (different camera): 0.78
- Site C (different protocol): 0.61

The model did not get worse — the data got different. Internal validation cannot detect this 30-point gap. External validation is required whenever generalisability claims are made.

### 8-Point Honest Experiment Checklist

1. **Split by the right unit** — patient, video, session — never by row
2. **Split once, before anything else** — including before computing normalisation statistics
3. **Stratify** — and print the class balance of every split
4. **Report the trivial baseline** — majority class, and one simple classical model
5. **Several seeds** — mean ± standard deviation, at least three runs
6. **Confidence intervals** — Wilson for proportions, bootstrap for everything else
7. **One change per comparison** — everything else frozen, same seeds
8. **State what you could not test** — other sites, scanners, populations

---

## Cross-Validation

Cross-validation replaces or supplements a validation set for more robust model selection.

### k-Fold Cross-Validation

1. Split data into k equal folds.
2. Train on k−1 folds; test on the remaining fold.
3. Repeat k times (each fold tested exactly once).
4. Average the performance metrics across folds.

**Process:**
- For each candidate hyperparameter setting: run k-fold CV → compute mean validation score.
- Select the setting with the best average score.
- Retrain one final model on the full training set.
- Evaluate once on the test set.

> Cross-validation is **not** a guarantee of real-world performance — it reduces selection bias, but cannot overcome bad data or distributional shift.

---

## Evaluation Metrics

### Confusion Matrix

|  | Predicted Positive | Predicted Negative |
|--|-------------------|--------------------|
| **Actual Positive** | True Positive (TP) | False Negative (FN) — **Type II Error** |
| **Actual Negative** | False Positive (FP) — **Type I Error** | True Negative (TN) |

---

### Classification Metrics

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| **Accuracy** | $\frac{TP+TN}{TP+TN+FP+FN}$ | % of all predictions that are correct |
| **Balanced Accuracy** | $\frac{1}{2}\left(\frac{TP}{TP+FN} + \frac{TN}{TN+FP}\right)$ | Average of sensitivity and specificity; better for imbalanced data |
| **Precision** | $\frac{TP}{TP+FP}$ | Of all positive predictions, what % were correct? |
| **Recall (Sensitivity)** | $\frac{TP}{TP+FN}$ | Of all actual positives, what % were caught? |
| **Specificity** | $\frac{TN}{TN+FP}$ | Of all actual negatives, what % were correctly rejected? |
| **F1 Score** | $\frac{2 \times Precision \times Recall}{Precision + Recall}$ | Harmonic mean; useful for imbalanced data |

**Why accuracy alone is misleading:**
- 100,000 transactions; 99,500 legitimate (99.5%), 500 fraud (0.5%)
- Model that always predicts "legitimate" → accuracy = 99.5% — but detects **zero fraud**
- F1 score for this model = 0

### Precision–Recall Trade-off

| Setting | Effect |
|---------|--------|
| High precision, low recall | Rarely says "yes" but is right when it does; misses many true positives |
| High recall, low precision | Says "yes" often; catches most positives but many are wrong |

Choose based on the **cost of each error type** in the application domain.

---

### Regression Metrics

| Metric | Formula | Notes |
|--------|---------|-------|
| **MAE** | $\frac{1}{n}\sum |y_i - \hat{y}_i|$ | Robust to outliers |
| **MSE** | $\frac{1}{n}\sum (y_i - \hat{y}_i)^2$ | Penalises large errors more |
| **RMSE** | $\sqrt{MSE}$ | Same units as target variable |
| **R²** | Explained variance ratio | 1.0 = perfect; 0 = predicts mean only |

---

## Bias–Variance Trade-off

Total prediction error = **Bias² + Variance + Irreducible Noise**

| Term | Definition | Symptom |
|------|-----------|---------|
| **Bias** | Error from incorrect assumptions; model too simple | High training error AND high test error |
| **Variance** | Sensitivity to training data fluctuations; model too flexible | Low training error, high test error |

> Decision trees are **low-bias, high-variance** models: they can fit complex patterns but are highly sensitive to the specific training data.

### Four Cases

| | Low Variance | High Variance |
|--|-------------|--------------|
| **Low Bias** | ✅ Ideal — well-fitted model | Overfitting — predictions vary across different datasets |
| **High Bias** | Underfitting — consistent but systematically wrong | Poor design — wrong and unstable |

### Corrective Actions

| Case | Action |
|------|--------|
| High Bias (Underfitting) | Increase model complexity; add features; reduce regularisation |
| Low Bias, High Variance (Overfitting) | Regularise; add data; use ensembling (bagging, random forests) |
| High Bias, High Variance | Revisit problem formulation; fix data quality; select better features; get more data |
| Low Bias, Low Variance | Monitor for distributional drift; validate on truly unseen data |

---

## Learning Curves

A plot of training and validation performance vs. number of training samples reveals the bias-variance state:

| Pattern | Diagnosis |
|---------|-----------|
| Both curves low and flat; converge early | High bias (underfitting) — more data won't help |
| Large gap; training high, validation rising as data grows | High variance (overfitting) — more data helps |
| Both curves high; small gap that narrows | Ideal — low bias, low variance |

---

## Related Concepts

- [[concepts/ml-evaluation-metrics|ML Evaluation Metrics]] — full metric coverage: segmentation DSC/IoU/boundary, detection AP/PQ, calibration, pitfall gallery
- [[concepts/decision-trees-and-ensembles|Decision Trees & Ensembles]] — key algorithms; overfitting is the central challenge
- [[concepts/ml-foundations|ML Foundations]] — CRISP-DM evaluation phase context
- [[concepts/ml-data-understanding|ML Data Understanding]] — stratification depends on data type understanding
- [[concepts/descriptive-statistics|Descriptive Statistics]] — statistical literacy needed to interpret metrics
