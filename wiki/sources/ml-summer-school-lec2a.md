---
type: source
status: established
title: "Trustworthy AI Summer School — Lecture 2a: Machine Learning Basics"
course: "Trustworthy AI: Machine Learning Meets Blockchain (Microcredential 2)"
institution: OTH Regensburg / TU Munich
lecturer: "Tobias Rueckert, M.Sc."
domain: machine-learning
ingested: 2026-08-17
tags: [source, machine-learning, fundamentals, gradient-descent, backpropagation, neural-networks, loss, overfitting, training-loop, PyTorch]
---

# Trustworthy AI Summer School — Lecture 2a: Machine Learning Basics

**Course:** International Summer School: Trustworthy AI — Machine Learning Meets Blockchain, Microcredential 2: Machine Learning
**Lecturer:** Tobias Rueckert, M.Sc. (OTH Regensburg, TU Munich, AKTORmed Robotic Surgery)
**Raw file:** `raw/Machine_Learning_Lec_2a.md`

---

## Overview

Part 2a of 4 in the ML Basics module. A ground-up introduction to machine learning using a consistent medical imaging thread (retinal fundus photography, chest radiography, dermatoscopy). Every concept is grounded by a visual worked example.

### Four-Part Structure

1. **What learning is** — Why a machine can solve problems nobody can write rules for; the classical programming → ML inversion; training vs inference.
2. **The shape of a problem** — Samples, features, task types, supervision types, annotation cost, train/val/test split, patient-level split, underfitting/overfitting.
3. **The artificial neuron** — Multiply–add–squash; worked ReLU examples; geometric interpretation; XOR problem; why depth works; layers as matrix products.
4. **How it learns** — Loss (cross-entropy); gradient descent; backpropagation; batches/steps/epochs; PyTorch training loop; debugging checklist.

---

## Key Topics and Concepts

### The ML Inversion

Classical programming: Rules + Data → Computer → Output.
Machine learning: Data + Answers → Computer → Rules.
"ML is not a different kind of computing. It is the same computing with the inputs and outputs swapped."

### The Four Ingredients (Universal Framework)

Every ML method is a choice of exactly four things:
1. **Data** — examples with labels (for supervised learning)
2. **Model family** — the set of functions the machine may choose from (fixed by the designer)
3. **Loss** — one number saying how wrong one prediction was
4. **Optimizer** — the rule that nudges parameters so loss decreases

Swapping any one ingredient produces a different method.

### Annotation Cost Table (order of magnitude)

| Label type | Approximate time |
|---|---|
| Image label | 4 s |
| Bounding box | 20 s |
| Keypoints | 55 s |
| Pixel mask | 8 min |

Pixel masks are one–two orders of magnitude slower than image labels, and they require expert annotators.

### Task Types and Output Shapes

Same image, different output shapes, different losses:
- **Classification** — one label per image
- **Detection** — a bounding box + label per object
- **Semantic segmentation** — one class label per pixel
- **Keypoint estimation** — named coordinates (anatomical landmarks)

Only the output shape and the loss change between tasks; the rest of the four-ingredient pipeline is identical.

### Feature Design vs End-to-End Learning

| Approach | Pipeline |
|---|---|
| Classical ML | Hand-designed features → classifier (learns decision only) |
| Deep learning | Raw pixels → model trained end-to-end (learns measurements AND decision) |

Deep learning needs far more data because it must learn what to measure, not just how to decide.

### Patient-Level Data Split (Medical AI)

If two images from the same patient appear on opposite sides of the train/test split, the test score measures memory, not generalisation. Always split by patient, never by image.

### XOR Problem — Why Depth Is Needed

One neuron can only produce a straight decision boundary. XOR (output is true when exactly one input is true) cannot be separated by any straight line in 2D — no matter how many neurons are placed side by side (combining linear functions gives another linear function). A hidden layer changes the coordinate system so that the next layer sees a linearly separable problem.

### Training Loop (PyTorch — the canonical 5-line loop)

```python
for epoch in range(n_epochs):
    for x, y in train_loader:        # 1. batch
        y_hat = model(x)             # 2. forward pass
        loss  = criterion(y_hat, y)  # 3. compute loss
        loss.backward()              # 4. backward pass (gradients)
        optimizer.step()             # 5. update parameters
        optimizer.zero_grad()        # CRITICAL — must clear gradients each step
```

Without `zero_grad()`, gradients from every previous step accumulate and the run silently makes no sense.

### When Loss Will Not Go Down — Debugging Checklist

Work through in this order before changing the model:

1. **Overfit one batch** — train 8 samples until loss → 0. If it won't, the bug is in the code.
2. **Look at one batch** — plot images with the labels the loader actually produced.
3. **Change the learning rate** — 10× smaller, then 10× larger. Two runs, five minutes.
4. **Check the label wiring** — class indices in the right order? Any label polarity inverted?
5. **Check the split** — same patient/slide/video on both sides?
6. **Compare the two curves** — which curve misbehaves tells you which problem you have.

Changing the architecture is somewhere below number ten.

---

## Quality Assessment

| Criterion | Rating |
|-----------|--------|
| Pedagogical clarity | Very high — consistent colour-code, illustrative figures described, everything grounded with numbers |
| Coverage | Complete for the named scope (basics through training loop) |
| New vs existing wiki content | Partially overlaps with `neural-networks-linear-models.md` and `ml-model-training-evaluation.md`; key new additions are XOR/depth, training loop code, debugging checklist, patient-level split, annotation costs |

---

## Extracted To

- [[concepts/neural-networks-linear-models]] — XOR problem and why depth is needed; training loop; batches/steps/epochs; debugging checklist
- [[concepts/ml-model-training-evaluation]] — patient-level split; training and validation curves; early stopping
