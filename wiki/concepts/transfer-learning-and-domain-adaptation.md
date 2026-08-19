---
type: concept
status: established
title: "Transfer Learning and Domain Adaptation"
domain: machine-learning
source: [[sources/ml-summer-school-lec6]]
updated: 2026-08-19
tags: [concept, machine-learning, transfer-learning, fine-tuning, domain-adaptation, peft]
---

# Transfer Learning and Domain Adaptation

> "Transfer buys data efficiency, not knowledge. It removes the need to spend your scarce labels learning what an edge is."

This page covers the complete pipeline for reusing pre-trained vision models: vocabulary, the three fine-tuning strategies, architecture-specific details (ResNet, U-Net, ViT), parameter-efficient fine-tuning (PEFT), and domain adaptation when the deployment data looks different from the training data.

---

## 1. Why Transfer at All?

**The annotation problem:** Raw medical images accumulate by themselves. Expert annotations do not. Image-level labels take seconds; pixel masks take tens of minutes per image; a hospital PACS holds millions of unlabelled images.

**The small-dataset problem:** Training from random initialisations on 500 labelled medical images produces a model that memorises them. Training the same architecture from pre-trained ImageNet weights, with most layers frozen, does not.

**Why it works — what layers already know:**

```
first conv   →  early/middle blocks  →  late blocks     →  head
edges/blobs      textures, motifs       anatomy             decision
 ← generic — transfers well →         task-specific — must be relearned
```

The early layers of any trained vision network learn oriented edges, colour blobs, and Gabor-like filters — nearly the same representations regardless of dataset. This is why weights from one task reduce the label burden for another.

Pre-training is a **data efficiency tool**, not a knowledge transfer: "The less data you have, the more it is worth."

---

## 2. Vocabulary — Domain vs Task

Confusion about transfer learning is usually confusion between these two:

| Concept | Definition | Example |
|---------|-----------|---------|
| **Domain** | Distribution the images come from | camera, scanner, light source, protocol, patient population, hospital |
| **Task** | Label space and the mapping to it | diseased/healthy; surgical phases; segmentation mask; keypoints |

| What moves | Name | Example |
|-----------|------|---------|
| Task changes, domain same | task transfer | fundus classification → fundus segmentation |
| Domain changes, task same | domain adaptation | same grading, different endoscope |
| Both change | transfer learning (broad sense) | ImageNet photos → laparoscopic instrument classification |

Most real clinical projects sit in the "both change" cell and use methods from all four quadrants.

---

## 3. The Three Strategies

One recipe, three settings for how much of the encoder you allow to move:

```
1 PRE-TRAIN   source data (millions of cheap labels) → encoder → head₁
2 TRANSFER    copy encoder weights → discard head₁
3 ADAPT       target data (few expensive labels) → same encoder → new head → your model
```

| Strategy | % of weights trained | Labels needed | Overfitting risk | Honest caveat |
|----------|---------------------|--------------|-----------------|---------------|
| **Feature extraction** | ~0.1% (head only) | few hundred | very low | cannot fix a bad representation |
| **Partial fine-tuning** | ~10–40% (last stages + head) | few thousand | moderate | usual compromise; depth choice matters |
| **Full fine-tuning** | 100% | tens of thousands | high | best ceiling; easiest way to destroy what you loaded |

### Practical Order of Operations

1. **Start with feature extraction.** It trains in minutes and gives a baseline you can trust.
2. Unfreeze the last stage with a **much smaller learning rate** and check whether it helps.
3. Only go to full fine-tuning if you have the data to support it — and **always compare against the frozen baseline**.

A from-scratch baseline and a frozen-encoder baseline cost almost nothing and tell you whether transfer is doing any work at all.

### Choosing the Strategy

|  | Few target labels | Many target labels |
|--|---|---|
| **Domain close to source** | Freeze almost everything; linear probe on frozen features; unfreeze last block only if it clearly helps | Fine-tune everything with low LR; layer-wise learning rates |
| **Domain far from source** | Unfreeze the late half; augment heavily; consider self-supervised pre-training on your own unlabelled data | Fine-tune all — but check from-scratch; with enough data it can win |

---

## 4. Learning Rates and Schedules

**One learning rate for the entire network throws away most of what you loaded.**

### Layer-wise (Discriminative) Learning Rates

Apply different learning rates to different parts of the network:
- Early layers: tiny LR — the generic edge detectors barely need to move
- Later stages: moderate LR
- Task head: largest LR — this is randomly initialised and needs to converge fast

### Warm-up + Cosine Decay Schedule

```
Phase 1 — warm-up (head only):
  - Train only the head for a few epochs at a moderate LR
  - Prevents the random head from corrupting the encoder in epoch 1

Phase 2 — progressive unfreezing:
  - Unfreeze stages from the top down, lowering LR as you go
  - Apply cosine decay over the remaining epochs
```

For ResNet, a four-stage schedule (unfreeze layer 4 → layer 3 → layer 2 → stem, each with a lower LR) is the standard.

---

## 5. Silent Failures

All four produce a working pipeline with worse numbers and no error message:

| Failure | Mechanism | Fix |
|---------|-----------|-----|
| **Frozen BatchNorm** | Carries source domain mean/variance; target distribution never re-centred | Unfreeze BN, or use InstanceNorm/LayerNorm |
| **Input preprocessing mismatch** | Pre-trained weights expect specific channel means/std; wrong order; grayscale stacked into 3 channels is not RGB | Apply the exact normalisation the pre-training used |
| **Resolution change (ViT)** | Position embeddings are tied to one token grid; changing resolution invalidates them | Bicubic-interpolate position embeddings to the new grid |
| **Class imbalance ignored** | Pre-training says nothing about your prevalence; 2% positive rate → 98% accuracy = predicts nothing | Check prevalence before training; choose metric accordingly |

---

## 6. Architecture-Specific Details

### ResNet / CNN

```
input (224²×3) → stem → layer 1 (112²×64) → layer 2 (56²×128) → layer 3 (28²×256) → layer 4 (14²×512) → global avg pool → [fc] → K scores
                                                                                                                               ↑
                                                                                                                    always new; one line of code
```

Pre-trained checkpoint gives you everything up to global avg pool. The fc layer is always new. For classification, transfer is one line of code: replace fc, keep the rest. For dense tasks, attach a new decoder.

### U-Net

```
[encoder / contracting path — transferable]  ← pre-trained (e.g. ImageNet ResNet)
     ↓ skip connections ↓
[decoder / expanding path — always new]      ← randomly initialised
     ↓
[1×1 conv → K classes]                       ← always new
```

No checkpoint will ever give you a decoder. Budget learning rate and warm-up for it specifically. Freeze the encoder initially; unfreeze progressively after the decoder has converged.

**The nnU-Net counterpoint (Isensee et al., Nature Methods 2021):** a plain U-Net with no pre-training and no architectural novelty — but with systematic automatic configuration of preprocessing, patch size, spacing, normalisation, augmentation, and post-processing. Won or matched most public 3D medical segmentation challenges. Lessons:
- 3D has no ImageNet; 2D checkpoints transfer poorly to volumetric data
- Configuration effort often beats method novelty
- Without a from-scratch baseline, you cannot claim a gain from pre-training

### Vision Transformer (ViT)

```
image → (16×16 patches) → linear projection + position embeddings → L transformer blocks → CLS token → head → K classes
```

Pre-trained checkpoint gives patch embedding + all L blocks. When changing input resolution:
- Patches stay 16×16 but there are more of them
- Position embeddings trained for a 14×14 token grid must be bicubic-interpolated to the new grid size
- Every good library does this for you — verify that yours did

**PEFT — Parameter-Efficient Fine-Tuning** (right choice with large frozen backbone + small clinical dataset):

| Method | Mechanism | Key parameter |
|--------|-----------|--------------|
| **LoRA** | `ΔW = B · A` — a low-rank update alongside frozen W | rank r ≪ d (usually 4–64) |
| **Adapters** | two small bottleneck layers per block (after attention and after MLP); the block itself never changes | bottleneck dimension |
| **Prompt tuning** | learned prompt tokens prepended to the patch token sequence; the entire model is untouched | number of prompt tokens |

With large enough pre-trained models (foundation models), PEFT is often the right default.

### Summary Table

| Architecture | What the checkpoint gives | What is always new | Input size | In practice |
|-------------|--------------------------|-------------------|------------|-------------|
| ResNet / CNN | stem + all stages + pooling | the fc layer | tolerant (global pooling absorbs it) | progressive unfreezing; watch BatchNorm stats |
| U-Net | contracting path only | whole decoder + 1×1 conv | tolerant within reason | decoder needs its own LR and warm-up |
| Vision Transformer | patch embedding + all L blocks | whatever reads the tokens | needs position embeddings interpolated | LoRA or adapters if data is scarce |

---

## 7. Domain Adaptation

When the deployment site differs from the training site, domain shift degrades performance even if the task is identical.

### Three Types of Shift

| Type | What changes | Can feature alignment fix it? |
|------|-------------|------------------------------|
| **Covariate shift** | Images look different; the rule (label mapping) stays the same | Yes |
| **Label shift** | Same images; class prevalences differ (screening 4% vs referral clinic 35%) | No |
| **Concept shift** | Same images; label definition differs (tight vs generous annotation boundary) | No — the label itself is different |

### The Cost of Ignoring Domain Shift

Illustrative DSC on vessel segmentation (one model, trained on Site A only):

| Site | DSC | Drop |
|------|-----|------|
| Site A (training) | 0.884 | — |
| Site B (different camera) | 0.792 | −9.2 pt |
| Site C (different protocol) | 0.741 | −14.3 pt |
| Site D (mobile screening) | 0.663 | −22.1 pt |

> "Your held-out test set from the same site is not evidence of generalisation — it is evidence of interpolation."

### Four Intervention Levels

```
target image → [1 Input] → block 1 → block 2 → block 3 → block 4 → [2 Features] → head → [3 Output]
                                  ↑ [4 Normalisation] ↑
```

**1. Input — colour and stain normalisation**
Map the target image appearance to the source statistics. Cheap, interpretable, no labels, no retraining.
> Try this before anything else.

**2. Features — distribution alignment**

*Moment matching (CORAL, MMD):* align the mean and covariance of source and target feature distributions. Aligning statistics is not aligning classes — it usually helps and can quietly hurt.

*Adversarial adaptation (DANN / GRL):*
```
feature extractor → task loss  (labelled source images)
                 → domain classifier → domain loss  (source vs target)
                         ↑ gradient reversal (−λ)
```
The domain classifier learns to separate source from target; the reversed gradient forces the feature extractor to erase the domain difference. Genuinely finicky — budget time for the λ schedule.

**3. Output — pseudo-labelling / self-training**
```
1 Train on labelled source
2 Predict on raw target images
3 Keep only confident predictions (threshold)
4 Add them as training data and retrain
5 Repeat
```
Works surprisingly well and fails silently. Watch the class balance of pseudo-labels — they will reflect whatever bias the model already has.

**4. Normalisation — AdaBN and TENT**

*AdaBN:* recompute the running mean and variance of BatchNorm layers on target images (forward pass only, no gradient). No labels needed.

*TENT (test-time entropy minimisation):* minimise the entropy of the model's predictions on the target image at test time. Sharpens the prediction from a diffuse distribution to a confident one.

> If you do exactly one thing about domain shift, recompute the normalisation statistics on target data.

### Domain Generalisation

Train from the start so that the unseen clinic is not a special case — no adaptation step needed at deployment.

**Method:** strong, physically meaningful augmentation that simulates the diversity of deployment conditions (colour, illumination, blur, resolution, geometry).

> "Strong, physically meaningful augmentation is the most reliable domain-generalisation method we have."

### The Split Trap

| Split strategy | Dice |
|---------------|------|
| Random by image (all sites mixed) | 0.88 |
| Leave-one-site-out | 0.71 |

Same data, same model, same predictions. The 0.17-point difference is invisible performance debt that will be paid when the model is deployed at a new site.

> Split by site and by patient — or you will not see any of this.

---

## 8. Common Pitfalls

**Transfer learning:**
- One learning rate for pre-trained encoder and new head
- No warm-up; random head damages encoder in epoch 1
- Frozen BatchNorm layers still carrying source statistics
- Input normalisation that does not match the checkpoint
- ViT position embeddings never interpolated to the new resolution
- No from-scratch baseline, so the gain is unmeasured

**Domain adaptation and evaluation:**
- Random split — domain shift is invisible in your numbers
- Several frames of one video in both splits
- Pseudo-labels accepted without checking their class balance
- Feature alignment applied to a concept shift it cannot fix
- Adversarial adaptation reported from a single best run
- A single-centre test set described as external validation

---

## Related Concepts

- [[concepts/convolutional-neural-networks|Convolutional Neural Networks]] — encoder anatomy, what layers learn, U-Net decoder
- [[concepts/neural-networks-linear-models|Neural Networks & Linear Models]] — backpropagation; the weight-update mechanism that applies here
- [[concepts/ml-evaluation-metrics|ML Evaluation Metrics]] — split-by-site rule; external validation; domain shift in evaluation
- [[concepts/ml-model-training-evaluation|ML Training & Evaluation]] — experimental design; five forms of data leakage; the split unit rule
- [[concepts/medmnist-v2-datasets|MedMNIST v2 Datasets]] — practical benchmarks including cross-centre scenarios
