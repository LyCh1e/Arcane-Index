---
type: source
status: ingested
title: "ML Summer School — Lecture 6: Transfer Learning and Domain Adaptation"
source_file: raw/Machine_Learning_Lec6.md
ingested: 2026-08-19
tags: [source, machine-learning, transfer-learning, domain-adaptation, fine-tuning]
---

# Source: ML Summer School — Lecture 6

**File:** `raw/Machine_Learning_Lec6.md`
**Lecturer:** Tobias Rueckert, M.Sc. — OTH Regensburg / TU Munich / AKTORmed
**Course:** International Summer School 2026 — Trustworthy AI: ML Meets Blockchain
**Topic:** Transfer Learning and Domain Adaptation (51 slides)

---

## What This Lecture Covers

Four parts: Why transfer? → The three fine-tuning strategies → ResNet/U-Net/ViT specifics → Domain adaptation (4 intervention levels).

---

## Key Ideas Extracted

### Why Transfer?

- Labels are the bottleneck — a hospital PACS holds millions of unlabelled images
- From-scratch on 500 labelled images overfits; pre-trained features + frozen encoder does not
- First conv layers = edges/colour blobs (generic, transfers well); late blocks = task-specific anatomy; head = the decision (must always be relearned)
- Pre-training is a data-efficiency tool, not a knowledge transfer: "It removes the need to spend your scarce labels learning what an edge is"

### Vocabulary: Domain vs Task

| Concept | Definition | Example |
|---------|-----------|---------|
| **Domain** | distribution the images come from | camera, scanner, acquisition protocol, hospital |
| **Task** | label space + desired mapping | class/segmentation mask/keypoints |
| **Domain adaptation** | same task, different domain | same grading, different endoscope |
| **Transfer learning** | different task (and domain) | ImageNet → DR grading |

Four-situation 2×2: same task+same domain (just train) / same task+different domain (domain adaptation) / different task+same domain (task transfer) / different task+different domain (the usual real-world case).

### Three Fine-tuning Strategies

| Strategy | Trainable | Labels needed | Overfitting risk | Caveat |
|----------|-----------|--------------|-----------------|--------|
| Feature extraction | ~0.1% | few hundred | very low | cannot fix a bad representation |
| Partial fine-tuning | ~10–40% | few thousand | moderate | usual compromise; depth choice matters |
| Full fine-tuning | 100% | tens of thousands | high | best ceiling; easiest way to destroy what you loaded |

**Practical order:** (1) Start with feature extraction — trains in minutes, gives a trustworthy baseline. (2) Unfreeze the last stage with a much smaller learning rate and see whether it helps. (3) Only go to full fine-tuning if data supports it — always compare against frozen baseline.

### Learning Rates and Schedules

- **Layer-wise (discriminative) learning rates:** early layers barely move; the head moves freely; one LR for the whole network throws away most of what you loaded
- **Schedule:** warm-up (head only first) then cosine decay as encoder unfreezes progressively

### Silent Failures

| Failure | What happens |
|---------|-------------|
| Frozen BatchNorm | carries source domain statistics — the shift survives |
| Wrong input preprocessing | model expects channel means/std from training domain |
| Resolution change in ViT | position embeddings are tied to one token grid; must be interpolated |
| Class imbalance | pre-training says nothing about your prevalence; 98% accuracy = predicts nothing |

### Three Architectures

| Architecture | What the checkpoint gives | What is always new | Input size flexibility | Practical note |
|-------------|--------------------------|-------------------|----------------------|----------------|
| ResNet / CNN | stem + all stages + pooling | the fc layer | tolerant (global pooling absorbs it) | progressive unfreezing, watch BatchNorm |
| U-Net | contracting path (encoder) only | the whole decoder + 1×1 conv | tolerant within reason | decoder needs its own learning rate |
| Vision Transformer (ViT) | patch embedding + all L blocks | whatever reads the tokens | needs position embeddings interpolated | LoRA or adapters if data is scarce |

**nnU-Net counterpoint:** a plain U-Net with automatic configuration (preprocessing, patch size, spacing, normalisation, augmentation), no pre-training, no attention — won or matched most public 3D segmentation challenges. Isensee et al., Nature Methods 2021. Lesson: configuration effort often beats method novelty; always run a from-scratch baseline.

### PEFT — Parameter-Efficient Fine-Tuning

| Method | Mechanism | Key property |
|--------|-----------|-------------|
| **LoRA** | ΔW = B·A (low-rank update alongside frozen W, rank r ≪ d) | fraction of parameters, same quality |
| **Adapters** | two bottleneck layers per transformer block (attention + MLP) | the block itself never changes |
| **Prompt tuning** | learned prompt tokens prepended to patch tokens | the model is completely untouched |

"With a large frozen backbone and a small clinical dataset, PEFT is often the right default, not the exotic option."

### Domain Adaptation

**Three types of shift:**
- **Covariate shift:** images look different, rule unchanged → feature alignment fixes it
- **Label shift:** same images, different class prevalence → cannot be fixed by feature alignment
- **Concept shift:** same images, different label definition → feature alignment cannot fix it

**Cost of shift:** illustrative vessel segmentation DSC — Site A (training): 0.884 → Site B: 0.792 (−9.2pt) → Site C: 0.741 (−14.3pt) → Site D: 0.663 (−22.1pt). "Your held-out test set from the same site is not evidence of generalisation — it is evidence of interpolation."

**Four intervention levels:**
1. **Input** — colour/stain normalisation; cheap, interpretable, no labels, no retraining; try this first
2. **Features** — CORAL/MMD (moment matching, align distributions), adversarial (GRL, domain classifier with reversed gradient, gradient reversal λ schedule is finicky)
3. **Output** — pseudo-labelling/self-training: train on source → predict on target → keep confident predictions → retrain; works but watch class balance of pseudo-labels
4. **Normalisation** — AdaBN (recompute μ and σ on target images); TENT (minimise entropy of predictions at test time); "if you do exactly one thing about domain shift, recompute the normalisation statistics on target data"

**Domain generalisation:** train so that the unseen clinic is not a special case — strong, physically meaningful augmentation (colour, illumination, blur, resolution, geometry) is the most reliable method we have.

**Split trap:** random split (Dice 0.88) vs leave-one-site-out (Dice 0.71) on the same data and model. "Split by site and by patient, or you will not see any of this."

**PhaKIR:** 8 cholecystectomy videos, 3 clinics, 18 instrument classes — leave-one-clinic-out evaluation is a domain-adaptation benchmark built into the dataset.

---

## Concept Pages Generated

- [[concepts/transfer-learning-and-domain-adaptation|Transfer Learning and Domain Adaptation]] — full concept page
