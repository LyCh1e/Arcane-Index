---
type: source
status: ingested
title: "ML Summer School — Lecture 3: Model Evaluation & Experimental Design"
source_file: raw/Machine_Learning_Lec3.md
ingested: 2026-08-18
tags: [source, machine-learning, evaluation, experimental-design]
---

# Source: ML Summer School — Lecture 3

**File:** `raw/Machine_Learning_Lec3.md`
**Lecturer:** Tobias Rueckert, M.Sc. — OTH Regensburg / TU Munich / AKTORmed
**Course:** International Summer School 2026 — Trustworthy AI: ML Meets Blockchain
**Topic:** Model Evaluation & Experimental Design

---

## What This Lecture Covers

Two questions frame the entire lecture:
- **A. Can I trust this number?** — How the experiment is designed determines whether the number is meaningful.
- **B. What does this number mean?** — Every metric answers exactly one specific question.

Five sections: experimental design (splits, leakage, variance) → metric selection → classification metrics → segmentation metrics → detection and instance metrics.

---

## Key Ideas Extracted

### Experimental Design
- Three-set roles: training (every epoch), validation (hundreds of times), test (once only)
- The **winner's curse**: best of 20 noisy numbers is biased upward; leaderboards make this systematic
- **5 forms of data leakage:** same patient in both sets, neighbouring frames, preprocessing before split, duplicates, tuning on test set
- **The split unit rule:** identify what must never appear on both sides (patient, eye, video, hospital) and split by that
- `StratifiedGroupKFold`: stratify by label, group by patient
- **CI formula:** half-width ≈ 1.96·√(p(1−p)/n); at n=50, "0.90 beats 0.86" is indistinguishable from noise
- **Controlled comparison:** one change at a time — augmentation (+0.08), new backbone (+0.02), 3× epochs (+0.01); all three together (+0.15) yields no knowledge

### Metric Selection
- **4 problem categories:** image-level classification, object detection, semantic segmentation, instance segmentation
- **6 metric families:** counting (single threshold), multi-threshold (curves), overlap, boundary, calibration, application-specific
- Concrete confusion matrix example: FN=20, TP=80, TN=810, FP=90 → accuracy 0.89 / sensitivity 0.80 / specificity 0.90 / precision 0.47 / F1 0.59 / balanced acc 0.85 / MCC 0.56
- At 1% prevalence, "always predict no findings" gives 99% accuracy

### Segmentation Metrics
- DSC = 2|R∩P|/(|R|+|P|); IoU = |R∩P|/|R∪P| = DSC/(2−DSC)
- Small-structure trap: 1-pixel shift on 4×4 → DSC=0.75; on 28×28 → DSC=0.96
- Same DSC=0.864, different shape error: HD=7.1px vs HD=26px
- Boundary metrics: HD (penalises worst outlier), ASSD (typical error), NSD (forgives annotation noise within tolerance τ)
- Aggregation: image-level average (0.81) vs patient-level average (0.64) — 17-point difference from identical predictions
- Empty reference (|R|=0, |P|=0): three conventions — 1.0, 0.0, or exclude; must be stated

### Detection & Instance Metrics
- Localisation criterion (IoU ≥ 0.5, mask IoU, centre-inside) and assignment strategy (greedy / Hungarian) must both be stated
- DSC rewards merging 3 lesions into 1 (DSC=0.76 vs F₁=0.50 for correct 3-object detection)
- IoU threshold sensitivity: same predictions, F₁=1.00 at IoU≥0.5 vs F₁=0.50 at IoU≥0.75
- **Panoptic Quality:** PQ = SQ × RQ; SQ = mean IoU of matched instances; RQ = object-level F₁

### Metrics Reloaded Framework
- Nature Methods 21, 195–212 (2024); Maier-Hein, Reinke et al.
- Three steps: problem fingerprint → metric selection → metric application
- Online tool: metrics-reloaded.dkfz.de
- Reference implementations: github.com/Project-MONAI/MetricsReloaded

---

## Concept Pages Generated

- [[concepts/ml-evaluation-metrics|ML Evaluation Metrics]] — comprehensive page for all Lec 3 content
- [[concepts/ml-model-training-evaluation|ML Training & Evaluation]] — extended with experimental design additions

---

## Project Relevance

Five rules for Friday presentations: (1) state split strategy in one sentence, (2) report trivial baseline, (3) three seeds with mean ± std, (4) pick metrics from the fingerprint, (5) one slide titled "what we got wrong".
