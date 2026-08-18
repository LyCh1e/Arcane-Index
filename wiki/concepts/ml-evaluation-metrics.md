---
type: concept
status: established
title: "ML Evaluation Metrics"
domain: machine-learning
source: [[sources/ml-summer-school-lec3]]
updated: 2026-08-18
tags: [concept, machine-learning, evaluation, metrics, segmentation, detection]
---

# ML Evaluation Metrics

> "A number without a protocol is not a result."

This page covers the complete evaluation framework from Lecture 3 of the ML Summer School. For experimental design (splits, leakage, variance), see [[concepts/ml-model-training-evaluation|ML Training & Evaluation]]. For basic confusion-matrix metrics, that page also applies.

---

## 1. Three Ways to Get the Metric Wrong

Before choosing any number, there are three distinct failure modes:

1. **Wrong problem category** — The metric is computed correctly and answers a question nobody asked. *Example: scoring "find every lesion" with Dice.*
2. **Wrong metric inside the category** — Correct family, but the specific metric breaks for this problem. *Example: Dice on 4-pixel structures; accuracy at 1% prevalence.*
3. **Wrong application of a good metric** — Correct metric, correct problem, then averaged incorrectly. *Example: pooling images across patients; undefined empty-reference cases.*

All three produce plausible numbers and clean tables. Only the third is usually caught in review.

---

## 2. Four Problem Categories

The category follows the clinical question, not the model architecture.

```
Do you need a label for the whole image?
  YES → Image-level Classification (ImLC)
  NO  → Do you need the exact outline of each region?
    NO  → Object Detection (ObD)
    YES → Must two touching objects be told apart?
      NO  → Semantic Segmentation (SemS)
      YES → Instance Segmentation (InS)
```

Pick the wrong category and every metric that follows is wrong — however carefully computed.

---

## 3. Six Metric Families

Pick **one metric from each relevant family** — not five correlated metrics from the same family.

| Family | Members | Applies to |
|--------|---------|------------|
| **Counting** | sensitivity · precision · F₁ · MCC · balanced accuracy | ImLC, ObD, InS |
| **Multi-threshold** | AUROC · average precision (AP) · FROC score | ImLC, ObD, InS |
| **Overlap** | DSC · IoU · clDice | SemS, InS |
| **Boundary** | HD · ASSD · MASD · NSD | SemS, InS |
| **Calibration** | ECE · Brier score · negative log-likelihood | ImLC |
| **Application-specific** | volume error · connectivity · latency | any |

---

## 4. Classification Metrics

### Confusion Matrix — Worked Example

*1 000 screening images, 100 referable:*

| | Predicted positive | Predicted negative |
|---|---|---|
| **Reference positive** | TP = 80 | FN = 20 |
| **Reference negative** | FP = 90 | TN = 810 |

| Metric | Formula | Value |
|--------|---------|-------|
| Accuracy | (TP+TN) / all | 0.89 |
| Sensitivity (recall) | TP / all positives | 0.80 |
| Specificity | TN / all negatives | 0.90 |
| Precision (PPV) | TP / all flagged | 0.47 |
| F₁ score | harmonic mean(sens, prec) | 0.59 |
| Balanced accuracy | mean(sensitivity, specificity) | 0.85 |
| Matthews correlation coeff. | uses all four cells | 0.56 |

Same four numbers; seven very different verdicts. Accuracy says 0.89 — but of every 100 images flagged, 53 are healthy.

### The 1% Prevalence Trap

A model that **always predicts "no findings"** at 1% prevalence scores:
- Accuracy: **0.99** ← measures the prevalence, not the model
- Sensitivity: 0.00
- F₁: 0.00
- Balanced accuracy: 0.50
- MCC: 0.00

> When prevalence is low, accuracy is a function of the prevalence — not the model. Report sensitivity, precision, and MCC.

### Screening vs Confirmation Trade-off

**Screening** (find everything, accept extra work)
- A missed finding is the catastrophic failure
- Optimise sensitivity at an acceptable false-positive rate
- Report: sensitivity @ fixed FP rate, FROC, recall-weighted F₂

**Confirmation / autonomy** (act only when certain)
- A false positive triggers an intervention
- A miss keeps the human in the loop — acceptable
- Optimise precision at an acceptable sensitivity
- Report: precision @ fixed sensitivity, PPV, F₀.₅

### ROC vs Precision–Recall

Same classifier, two prevalences:

| Curve | Prevalence 50% | Prevalence 2% |
|-------|---------------|--------------|
| AUROC | 0.82 | 0.79 — *hardly moves* |
| Average precision | 0.82 | 0.23 — **collapses** |

AUROC is prevalence-independent and threshold-free — but hides false positives when positive class is rare. Use AP or the full PR curve when the positive class is rare.

### What to Report for Classification

| Report | When | Why |
|--------|------|-----|
| Confusion matrix itself | always | four numbers, no interpretation needed |
| Sensitivity and specificity | always | properties of the model, not the cohort |
| Precision (PPV) | always | state the prevalence it belongs to |
| Balanced accuracy or MCC | if imbalanced | one honest single-number summary |
| AUROC | useful | prevalence-independent, threshold-free |
| Average precision / PR curve | if rare class | what AUROC hides at low prevalence |
| Operating point | always | and the set it was chosen on |
| Calibration (ECE or Brier) | if scores are used | needed the moment a human reads the probability |
| Plain accuracy alone | **never** | it is a function of the prevalence |

---

## 5. Segmentation Metrics

### DSC and IoU

```
DSC = 2|R∩P| / (|R| + |P|)       — the F₁ score applied to pixels
IoU = |R∩P| / |R∪P| = DSC / (2 − DSC)
```

- DSC = 0.77, IoU = 0.62 are equivalent rankings — they always agree on method order
- **Neither knows anything about shape**

### The Small-Structure Trap

The same one-pixel shift produces very different DSC values depending on structure size:

| Structure size | DSC |
|---------------|-----|
| 4 × 4 px | 0.75 |
| 10 × 10 px | 0.90 |
| 28 × 28 px | 0.96 |

Small structures are where human annotators disagree most — a low DSC may be measuring the reference, not the model. Treat very small structures as detection, not segmentation.

### Shape Blindness — Same DSC, Different Mistake

Two segmentation errors, both DSC = 0.864:
- **A:** uniform erosion (outline slightly too small everywhere)
- **B:** half the structure missing (one side cut off)

| Metric | Case A | Case B |
|--------|--------|--------|
| DSC | 0.864 | 0.864 |
| Hausdorff distance | 7.1 px | 26.0 px |
| NSD (τ = 3 px) | 0.00 | 0.69 |

Boundary metrics detect what overlap metrics miss entirely.

### Boundary Metrics Compared

| Metric | What it measures | Use it when |
|--------|-----------------|-------------|
| **HD** (Hausdorff Distance) | worst-case outlier | one spurious blob matters clinically |
| **ASSD** (Average Symmetric Surface Distance) | typical error | robust summary across the boundary |
| **NSD** (Normalised Surface Distance) | fraction of boundary within tolerance τ | annotation noise is known; τ reflects inter-rater distance |

Example: a small spurious blob far from the main structure vs a contour 2px too small everywhere:

| | Spurious blob | Uniform −2px |
|---|---|---|
| DSC | 0.99 | 0.94 |
| HD | 40 px | 3 px |
| ASSD | 2.1 px | 2.3 px |
| NSD (τ = 3 px) | 0.94 | 1.00 |

ASSD is nearly identical despite very different errors. HD catches the outlier; NSD forgives errors inside the tolerance.

### clDice — Tubular Structures

Standard overlap metrics miss topological disconnection. Example: 6% of vessel pixels missing → DSC=0.97, clDice=0.95 — but 8 connected components become 79. The tree is no longer a tree.

Use **clDice** for vessels, airways, nerves, or any structure where connectivity is the clinical information.

### Aggregation Level

*One hospital, five patients, 150 images (Patient 1 contributes 100 images):*

- **Image-level average → 0.81** — Patient 1 dominates; two-thirds of every image in the mean
- **Patient-level average → 0.64** — every patient counts once; the clinically relevant unit

> Identical predictions. A **17-point difference** produced purely by the order of averaging. Always aggregate per patient first, then across patients.

### Empty Reference (|R|=0)

When both reference and prediction contain no structure, DSC = 0/0. Three published conventions:

| Convention | DSC | Rationale |
|-----------|-----|-----------|
| Count as 1.0 | 0.86 | perfect prediction = perfect score |
| Count as 0.0 | 0.56 | nothing to overlap with |
| Exclude | 0.80 | report only where the question exists |

Same model, same predictions, three published numbers. **State the convention explicitly.**

### What to Report for Segmentation

- **One overlap metric** — DSC or IoU, not both (equivalent rankings)
- **One boundary metric** — NSD if tolerance is defensible; otherwise ASSD or HD95
- **Per-case values** — box plot shows failures a mean hides
- **Aggregation at patient level** — per case first, then across patients; state this
- **Empty-reference convention** — which of the three, in writing
- **clDice** if structures are tubular
- **Reference quality** — one annotator or several? inter-rater agreement?

---

## 6. Detection and Instance Metrics

### Two Decisions Before Any Metric

**1. Localisation criterion** — When does a prediction "hit" a reference?
- box IoU ≥ 0.5
- mask IoU ≥ 0.5
- centre of prediction inside reference region

**2. Assignment strategy** — Two predictions hit the same object — who wins?
- greedy by confidence score
- greedy by overlap
- optimal (Hungarian) matching
- the loser in any strategy becomes a false positive

The same predictions can score 0.6 or 0.9 depending on these two choices. Neither is a detail — both must appear in the methods section.

### Why DSC Breaks for Detection

*Three lesions, two predictions:*
- **Prediction A:** one merged blob covering all three references → DSC = 0.76, object-level F₁ = 0.50
- **Prediction B:** three separate objects matching three references → DSC = 0.66, object-level F₁ = 1.00

DSC rewards merging because it sees pixels, not objects. If the clinical question is "find every lesion", the problem is detection — use object-level metrics.

### IoU Threshold Sensitivity

The winner of a comparison can swap when the threshold changes:

| | Method A (finds all 4, boxes a bit off) | Method B (finds 3, boxes precise) |
|---|---|---|
| F₁ at IoU ≥ 0.5 | 1.00 | 0.86 |
| F₁ at IoU ≥ 0.75 | 0.50 | 0.86 |

Choose the IoU threshold from the clinical task, keep it fixed, and report it. Or report a curve.

### Panoptic Quality

Combines detection and segmentation quality into one number:

```
PQ = SQ × RQ

SQ (segmentation quality)  = mean IoU of matched instances
RQ (recognition quality)   = object-level F₁
```

*Example: 3 matched instances (IoU = 0.85, 0.72, 0.91); 1 FN; 1 FP*
→ SQ = 0.83, RQ = 0.75, PQ = 0.62

PQ cannot hide a missed instance behind good pixels — SQ and RQ separate where the failure is.

---

## 7. The Pitfall Gallery

Complete reference from the lecture:

| Pitfall | Fix |
|---------|-----|
| Random split on grouped data (frames, slices, both eyes) | Split by patient |
| Tuning on the test set (threshold, epoch, architecture) | Validation set only |
| One seed, one number (no spread) | Mean ± std over ≥ 3 runs |
| No baseline (0.94 may be majority class) | Report the trivial model |
| Accuracy on imbalanced data (measures prevalence) | Balanced accuracy, MCC, PR curve |
| AUROC with rare positive class (hides false positives) | Average precision |
| Score treated as probability (AUROC cannot see this) | ECE, Brier, reliability diagram |
| Dice on tiny structures (one pixel costs 25 points) | Treat as detection |
| Overlap metric alone (shape-blind) | Add a boundary metric (NSD, HD95, ASSD) |
| Pooling images across patients (longest scan wins) | Aggregate per patient |
| Silent empty-reference handling (0/0) | State the convention |
| Detection scored with Dice (rewards merged objects) | Object-level F₁, AP, FROC |
| Unstated IoU threshold (changes the ranking) | State it, or report a curve |
| Accuracy or specificity in detection (no true negatives exist) | FP per image |

---

## 8. Metrics Reloaded Framework

**Paper:** Maier-Hein, Reinke et al. — *Nature Methods* 21, 195–212 (2024)
**Sister paper:** Reinke, Tizabi et al. — *Nature Methods* 21, 182–194 (2024) — the pitfall catalogue

**Three steps:**
1. **Problem fingerprint** — Which category? Are classes balanced? How big are the structures? Is the reference noisy? Are cases independent?
2. **Metric selection** — Follow the decision tree; pick one relevant metric from each relevant family
3. **Metric application** — Aggregate at the right level; handle empty references; report confidence intervals and full confusion matrix

**Online interactive tool:** [metrics-reloaded.dkfz.de](https://metrics-reloaded.dkfz.de)
**Reference implementations:** [github.com/Project-MONAI/MetricsReloaded](https://github.com/Project-MONAI/MetricsReloaded)

### Starting-Point Recommendations per Category

| Problem category | Counting metric | Curve metric | Complement with |
|-----------------|----------------|--------------|-----------------|
| Image-level classification | balanced accuracy or MCC | AUROC, or AP if rare | ECE / Brier if scores used |
| Semantic segmentation | DSC (clDice for tubular) | NSD, or ASSD / HD95 | volume error if volume matters |
| Object detection | F₁ or sensitivity @ fixed FP | AP or FROC | localisation criterion + assignment |
| Instance segmentation | F₁ or panoptic quality | average precision | DSC + NSD per matched instance |

In every category additionally: confusion matrix or per-case values; confidence intervals; aggregation level; empty-reference convention.

---

## Related Concepts

- [[concepts/ml-model-training-evaluation|ML Training & Evaluation]] — splits, leakage, variance, CI formula
- [[concepts/medmnist-v2-datasets|MedMNIST v2 Datasets]] — metric selection guide per dataset
- [[concepts/ai-in-medicine|AI in Medicine]] — OOD detection, annotation bottleneck
- [[concepts/neural-networks-linear-models|Neural Networks & Linear Models]] — softmax calibration
