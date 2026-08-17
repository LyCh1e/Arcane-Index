---
type: source
status: established
title: "Trustworthy AI Summer School — Lecture 2: MedMNIST v2 Dataset Briefing"
course: "Trustworthy AI: Machine Learning Meets Blockchain (Microcredential 2)"
institution: OTH Regensburg / TU Munich
lecturer: "Tobias Rueckert, M.Sc."
domain: machine-learning
ingested: 2026-08-17
tags: [source, machine-learning, MedMNIST, medical-imaging, classification, datasets, team-project, evaluation, OOD]
---

# Trustworthy AI Summer School — Lecture 2: MedMNIST v2 Team Project Briefing

**Course:** International Summer School: Trustworthy AI — Machine Learning Meets Blockchain, Microcredential 2: Machine Learning
**Lecturer:** Tobias Rueckert, M.Sc. (OTH Regensburg, TU Munich, AKTORmed Robotic Surgery)
**Raw file:** `raw/Machine_Learning_Lec_2.md`

---

## Overview

This lecture is a dataset briefing for the team project: build a working image-classification pipeline on real clinical data using one MedMNIST v2 dataset.

**MedMNIST v2:** https://medmnist.com/v2 — standardised, low-resolution (28×28) medical imaging benchmarks across 12 2D datasets and 6 3D datasets.

---

## Team Project Requirements

**Artefact:** A Jupyter notebook that runs top-to-bottom on a fresh runtime with fixed seeds.

**Presentation structure:**
1. Dataset — modality, classes, example images, class distribution, majority baseline
2. Setup — model, training procedure, metrics and justification
3. Baseline — results with seed spread
4. Experiments — one factor changed at a time; what happened, what you conclude
5. Error analysis — concrete failure cases and hypotheses
6. Test result, limitations, and what you would do with one more week

**Pass criteria (all six must hold):**
1. ✓ Reproducible: re-run gets the same numbers
2. ✓ Honest split: the three sets (train/val/test) never mix
3. ✓ Documented baseline: appropriate metrics and numbers stated
4. ✓ Controlled comparison: one factor changed at a time
5. ✓ Error analysis: failures and hypotheses identified
6. ✓ Shared understanding: all team members can explain it

---

## Dataset Assignments (This Cohort)

| Group | Dataset |
|-------|---------|
| 1 | PathMNIST |
| 2 | DermaMNIST |
| 3 | OCTMNIST |
| 4 | PneumoniaMNIST |
| 5 | BreastMNIST |
| 6 | BloodMNIST |
| 7 | TissueMNIST |
| 8 | OrganAMNIST |
| 9 | OrganCMNIST |
| 10 | OrganSMNIST |

---

## Key Topics Covered

### MedMNIST v2 Dataset Catalogue

All dataset details extracted to → [[concepts/medmnist-v2-datasets]]

Covers: PathMNIST, ChestMNIST, DermaMNIST, OCTMNIST, PneumoniaMNIST, RetinaMNIST, BreastMNIST, BloodMNIST, TissueMNIST, OrganAMNIST, OrganCMNIST, OrganSMNIST, OrganMNIST3D, NoduleMNIST3D, FractureMNIST3D, AdrenalMNIST3D, VesselMNIST3D, SynapseMNIST3D.

### Task Types Encountered

| Type | Example Datasets | Metric Considerations |
|------|-----------------|----------------------|
| Binary | PneumoniaMNIST, BreastMNIST, VesselMNIST3D | AUC, sensitivity/specificity; never accuracy alone when imbalanced |
| Multi-class | PathMNIST, DermaMNIST, BloodMNIST, OrganA/C/S | Per-class recall; confusion matrix; accuracy only if balanced |
| Multi-label | ChestMNIST | Per-class AUC / average precision; binary cross-entropy (14 sigmoids, not softmax) |
| Ordinal | RetinaMNIST | Quadratic-weighted kappa or MAE — plain accuracy ignores ordering cost |
| 3D Volume | OrganMNIST3D, NoduleMNIST3D, FractureMNIST3D | Overfitting likely with few samples; no ImageNet pre-training available |

---

## Quality Assessment

| Criterion | Rating |
|-----------|--------|
| Specificity | High — dataset-level statistics, pitfalls, and metric rationales |
| Recency | Current — MedMNIST v2 (Yang et al., 2023); sources cited per dataset |
| Domain relevance | High for medical imaging ML classification |
| General ML content | Medium — implies knowledge of CNN training, augmentation, cross-validation |

---

## Extracted To

- [[concepts/medmnist-v2-datasets]] — full dataset catalogue with modality, task type, split sizes, pitfalls, and metric selection guidance
