---
type: concept
title: "AI in Medicine"
domain: machine-learning
complexity: medium
maturity: established
tags: [AI, medicine, medical-imaging, OOD, trustworthy-AI, endoscopy, robotic-surgery, surgical-AI, ReMIC, deep-learning, computer-vision]
created: 2026-08-17
updated: 2026-08-17
status: established
related:
  - "[[concepts/ml-foundations]]"
  - "[[concepts/neural-networks-linear-models]]"
  - "[[concepts/medmnist-v2-datasets]]"
  - "[[sources/ml-summer-school-lec1]]"
  - "[[areas/machine-learning]]"
---

# AI in Medicine

AI in medicine is the application of machine learning — primarily deep learning and computer vision — to clinical data such as medical images, pathology slides, electronic health records, and genomics. It is one of the fastest-growing areas of applied ML, with publications increasing from ~15/year in 1995 to ~6,450/year in 2023 (Xie et al., 2025).

---

## 1. Data Modalities

Medical AI is not one problem — it is a collection of distinct domains, each with its own imaging physics, annotation cost, and label distribution.

| Modality | Share of publications | Examples |
|----------|----------------------|---------|
| **Texts** (clinical notes, reports) | 34.6% | NLP for radiology reports, EHR extraction |
| **Radiology** (MRI, CT, X-ray, Nuclear, US) | 30.1% | Chest X-ray diagnosis, tumour segmentation |
| **Pathology** (microscopy slides) | 12.0% | Colon cancer detection, cell classification |
| **Omics** (genomics, proteomics) | 12.4% | Cancer subtype prediction |
| **Clinical images** (dermatoscopy, fundus, OCT) | 4.7% | Skin lesion classification, diabetic retinopathy |
| **Other non-image** (signals, structured data) | 6.2% | ECG arrhythmia, vital-signs prediction |

Source: Schouten et al. (2025) — multimodal AI scoping review, Medical Image Analysis.

---

## 2. Medical Imaging AI — Key Applications

### Endoscopy and Gastrointestinal Imaging

| Task | Technique |
|------|-----------|
| Barrett Esophagus detection | Real-time classification with AI-overlay on endoscope livestream |
| GI Tract 3D reconstruction | Gaussian Splatting from video; fly-through navigation; dynamic tissue modelling |
| Surgical phase recognition | Multi-class classification over laparoscopic video sequences |
| Surgical instrument segmentation | Instance segmentation, keypoint estimation |

### Ophthalmology

| Task | Notes |
|------|-------|
| Diabetic retinopathy grading | Ordinal (0–4); lesions may be sub-pixel at low resolution |
| Macular degeneration (OCT) | Retinal layer structure; 100k+ training images available |

### Pathology

- H&E stained slides are the clinical gold standard for cancer diagnosis
- Colour domain shift between labs/days is a primary augmentation target
- Weak supervision and patch-level labels are common due to annotation cost

### Radiology (CT/X-ray)

- CT values are physically calibrated (air = −1000 HU, water = 0 HU, bone = +400–1000 HU) — brightness has physical meaning
- Multi-label chest X-ray findings: 14 independent yes/no per image (not softmax — sigmoid)
- Patient-level train/test split matters: images from the same patient are not independent

---

## 3. Trustworthiness and Out-of-Distribution (OOD) Detection

**The core trustworthiness challenge in medical AI:** A model trained on one hospital's data may fail silently when deployed at a different hospital — different scanner manufacturer, staining protocol, patient demographics, or clinical workflow. This is **domain shift**.

**Why silent failure is dangerous:** A model that confidently outputs a wrong classification is more dangerous than a model that abstains or flags uncertainty. Clinical deployment requires quantified uncertainty.

### OOD Detection Taxonomy

| Category | Definition | Example |
|----------|-----------|---------|
| **In-Distribution (ID)** | Same domain as training | Same hospital, same scanner |
| **Covariate-shift In-Distribution (cs-ID)** | Distribution shift but same task; still in-distribution by label | Different staining batch, same lab |
| **Near-OOD** | Related domain; similar features but different task or label space | Different cancer type |
| **Far-OOD** | Clearly different domain | Non-medical images sent to a medical classifier |

### OpenMIBOOD Benchmark (CVPR 2025)

Gutbrod et al. (2025) — "OpenMIBOOD: Open medical imaging benchmarks for out-of-distribution detection":
- **3 benchmarks** spanning **14 datasets** (MIDOG, PhaKIR, OASIS-3, and others)
- **24 OOD detection methods** evaluated
- Provides standardised evaluation infrastructure for medical OOD detection

**Key insight:** OOD detection methods perform very differently across modalities. A method that works for pathology may not transfer to radiology — making benchmark diversity essential.

### Illustrative Failure Case

A commercial plant identification app correctly identifies an avocado; given the same image under different lighting it outputs "unhealthy — overwatering, diseased." In medicine, this level of confabulation — confident wrong answer — is the failure mode that kills. The OOD problem is not theoretical; it is the primary barrier to clinical deployment.

---

## 4. Surgical AI and Robotic Surgery

### SOLOASSIST — Robotic Endoscope Control

- **SOLOASSIST II** (current): robotic arm controls an endoscope during minimally invasive surgery (MIS). Surgeon moves it via joystick or voice commands — removes the need for a human assistant but adds cognitive workload.
- **SOLOASSIST III** (target): near-autonomous adjustment driven by ML — the endoscope follows the surgical instrument without manual input.

### DeepMIC Project (OTH Regensburg / AKTORmed / TU Munich)

- **Goal:** Almost-autonomous endoscope adjustment using ML
- **Approach:** Purely visual — no additional hardware sensors
  - Surgical instrument recognition (what instrument is in view)
  - Instrument tracking over time (where it is moving)
- **Animal trial result (Feb 2025):** Good overlap handling; clear instrument class separation; passed all BFS (Bayerische Forschungsstiftung) requirements

### Autonomous Robotic Surgery (JHU, 2025)

Johns Hopkins University demonstrated a robot performing an ex vivo laparoscopic cholecystectomy (gallbladder removal) without human assistance, using:
- Da Vinci Research Kit (dVRK) Si
- Stereo endoscope + wrist cameras
- Porcine gallbladder on liver as the specimen

This marks the first demonstration of a complete realistic surgical procedure executed autonomously.

---

## 5. Data Availability — The Annotation Bottleneck

| Type | Scale |
|------|-------|
| ImageNet (general computer vision) | 14 million annotated images |
| Laparoscopic cholecystectomy footage (yearly, US) | ~1 million procedures ≈ 630 hours |
| Common surgical datasets (e.g. Cholec80) | ~50 hours |
| Large cancer pathology datasets (e.g. NCT-CRC-HE-100K) | ~100,000 patches |

**Root cause:** Labelling medical images requires expert time (radiologist, pathologist, or surgeon) at rates of hours per case. This creates an inherent ceiling on dataset size that does not exist in natural image AI.

**Consequences:**
- Models trained on small datasets overfit to institutional specifics (one lab, one scanner, one surgeon)
- Transfer learning and pre-training on large datasets become essential — but domain gap from natural images to medical images is significant
- Semi-automatic annotation pipelines (as used in PhaKIR) are a partial solution

### PhaKIR Dataset (PhaKIR Challenge, MICCAI 2024)

- 13 training videos + 5 test videos from 3 hospitals
- ≈33,800 annotated frames
- Segmentation masks and phase annotations from MITI Research Group
- Keypoints generated semi-automatically by ReMIC and refined manually
- Published: Medical Image Analysis (Elsevier), 2025

---

## 6. Key Observations for ML Practitioners

| Observation | Implication |
|-------------|-------------|
| Medical datasets are small relative to natural image datasets | Pre-training and transfer learning are almost always worth trying |
| Label quality is domain-limited | Expert disagreement is a feature, not a bug — uncertainty quantification matters |
| Class imbalance is the norm | Never report accuracy alone on an imbalanced dataset |
| Domain shift is ubiquitous | Evaluate on data from a different source than training; single-site results are incomplete |
| 3D data has no ImageNet analogue | 3D models almost always overfit on small medical volumes; regularise aggressively |

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/ml-foundations]] | Supervised learning, CRISP-DM, bias-variance tradeoff — foundational ML concepts applied here |
| [[concepts/ml-model-training-evaluation]] | Metric selection (AUC, sensitivity/specificity, kappa) is central to medical ML |
| [[concepts/neural-networks-linear-models]] | CNNs are the primary architecture for medical image classification |
| [[concepts/medmnist-v2-datasets]] | Benchmark datasets covering 6 medical imaging modalities and 4 task types |
| [[sources/ml-summer-school-lec1]] | Primary source for this concept page |
