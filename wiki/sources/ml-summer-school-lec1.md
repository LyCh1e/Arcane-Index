---
type: source
status: established
title: "Trustworthy AI Summer School — Lecture 1: Kickoff & Motivation"
course: "Trustworthy AI: Machine Learning Meets Blockchain (Microcredential 2)"
institution: OTH Regensburg / TU Munich
lecturer: "Tobias Rueckert, M.Sc."
domain: machine-learning
ingested: 2026-08-17
tags: [source, machine-learning, AI-in-medicine, medical-imaging, OOD, trustworthy-AI, surgical-AI, ReMIC, DeepMIC, PhaKIR]
---

# Trustworthy AI Summer School — Lecture 1: Kickoff & Motivation

**Course:** International Summer School: Trustworthy AI — Machine Learning Meets Blockchain, Microcredential 2: Machine Learning
**Lecturer:** Tobias Rueckert, M.Sc. (OTH Regensburg, TU Munich, AKTORmed Robotic Surgery)
**Raw file:** `raw/Machine_Learning_Lec_1.md`

---

## Course Structure (Full Programme)

| Lecture | Topic |
|---------|-------|
| 1 | Kickoff & Motivation |
| 2a/b | ML — Basics and Classification Models; Practice: Python Basics, ML Classifiers |
| 3 | Model Evaluation; Practice: PyTorch Tutorial |
| 4a | Digital Images |
| 4b | Operations on Images |
| 5 | Convolutional Neural Networks |
| 6 | Transfer Learning and Domain Adaptation |
| 7 | Attention and Transformers |
| 8 | Final Assessment |

---

## Lecturer Background

Tobias Rueckert's research is split across three institutions:

| Role | Institution | Focus |
|------|-------------|-------|
| PhD Student | TU Munich | Deep learning-based recognition and tracking of surgical instruments in video sequences — spatial and temporal information |
| Research Assistant | OTH Regensburg (ReMIC Lab) | Medical image computing: endoscopy, oncology, surgery |
| ML Developer | AKTORmed Robotic Surgery | Surgical instrument recognition and tracking for robotic endoscopy |

**Bachelor thesis:** Deep learning-based 2D localisation of surgical instruments in video images.
**Master thesis:** Predicting postoperative mortality after radical cystectomy for bladder cancer using ML combining medical images and clinical data.

---

## Key Topics Covered

### 1. AI in Medicine — Overview

- AI publication volume in healthcare grew from ~15 per year (1995) to ~6,450 (2023) — over 400× growth in 28 years
- Data modalities breakdown: Texts 34.6%, Radiology 30.1%, Pathology 12.0%, Omics 12.4%, Clinical images 4.7%, Other non-image 6.2%
- Source: Xie et al. (2025) — 30-year bibliometric study; Schouten et al. (2025) — multimodal AI scoping review

### 2. ReMIC Lab — Medical Image Computing Applications

| Application | Description |
|-------------|-------------|
| Barrett Esophagus detection | Endoscopic cancer diagnosis with AI-overlay livestream |
| GI Tract 3D reconstruction | Dynamic 3D reconstruction using Gaussian Splatting; fly-through navigation |
| Camera pose estimation | Point tracking via LEAP-VO on the EndoNeRF dataset |
| Trustworthiness / OOD | OpenMIBOOD — 3 benchmarks, 14 datasets, 24 OOD detection methods (CVPR 2025) |

### 3. OOD Detection — Trustworthiness in AI

**Out-of-Distribution (OOD) detection** is a core trustworthiness problem: a model that performs well on its training distribution can fail silently when given inputs from a different distribution (different hospital, staining protocol, patient population). This is a fundamental challenge for deploying AI in medicine.

**OpenMIBOOD benchmark** (Gutbrod et al., CVPR 2025):
- 3 benchmarks spanning 14 different medical imaging datasets
- 24 OOD detection methods evaluated
- Datasets: MIDOG, PhaKIR, OASIS-3, and others
- Categories: In-Distribution (ID), covariate-shift in-distribution (cs-ID), near-OOD, far-OOD

**Clinical analogy:** A plant identification app that correctly identifies an avocado as an avocado but labels a hemp plant as healthy (misidentifying cannabis as innocuous) — the confident wrong answer is more dangerous than no answer.

### 4. AKTORmed / DeepMIC — Robotic Endoscopy

**SOLOASSIST II** — current commercial robotic endoscope; moved by joystick or voice control, adds workload to the surgeon.

**DeepMIC project** (funded by Bayerische Forschungsstiftung):
- Goal: almost-autonomous endoscope adjustment using ML
- Approach: purely visual surgical instrument recognition + tracking over time
- Partners: AKTORmed, TU Munich, OTH Regensburg (ReMIC), MITI Research Group
- Animal trial (Feb 2025): good overlap handling, clear instrument separation; concluded BFS satisfied

### 5. PhaKIR Challenge — MICCAI 2024

Phase, Keypoint, and Instrument Recognition challenge at MICCAI 2024 Marrakech:
- 3 tasks: surgical procedure phase recognition; instrument keypoint estimation; instrument instance segmentation
- Entirely self-hosted; €3,000 prize money from AKTORmed
- 66 registrations, 18 submissions (largest of the MICCAI 2024 EndoVis sub-challenges by registrations)
- Dataset: 8 training videos, 5 test videos, ≈33,800 annotated frames; 3 hospitals
- Published: Medical Image Analysis (Elsevier), received and accepted July 2025

### 6. Data Availability Challenge

- ImageNet (general): 14 million annotated images
- Laparoscopic cholecystectomy: ~1 million procedures/year in the US (~630 hours of footage) — but common datasets (e.g. cholec80) only cover ~50 hours
- Root cause: annotation requires expensive medical expertise (a radiologist or surgeon must label every frame)

---

## Quality Assessment

| Criterion | Rating |
|-----------|--------|
| Specificity | High — concrete research examples, benchmark results, publication references |
| Recency | Current — papers from 2024–2025 |
| Domain relevance | High for AI-in-medicine and trustworthy ML |
| General ML content | Low — Lec 1 is motivation only; fundamentals are in Lec 2a/b and later |

---

## Extracted To

- [[concepts/ai-in-medicine]] — publication growth, data modalities, OOD detection, medical imaging AI overview, data availability challenge
- [[concepts/medmnist-v2-datasets]] — indirect (course context; datasets are the team project material from Lec 2)
