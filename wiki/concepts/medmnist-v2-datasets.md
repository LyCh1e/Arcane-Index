---
type: concept
title: "MedMNIST v2 — Medical Imaging Benchmark Datasets"
domain: machine-learning
complexity: medium
maturity: established
tags: [MedMNIST, datasets, medical-imaging, classification, benchmark, CNN, pathology, radiology, OCT, dermatoscopy, ultrasound, CT, MRI, electron-microscopy, OOD]
created: 2026-08-17
updated: 2026-08-17
status: established
related:
  - "[[concepts/ai-in-medicine]]"
  - "[[concepts/ml-model-training-evaluation]]"
  - "[[concepts/neural-networks-linear-models]]"
  - "[[sources/ml-summer-school-lec2]]"
---

# MedMNIST v2 — Medical Imaging Benchmark Datasets

MedMNIST v2 is a standardised collection of 18 medical image classification datasets, all resized to **28 × 28 pixels** (2D) or **28 × 28 × 28 voxels** (3D). The low resolution is deliberate: it makes the datasets fast to train on, provides a level playing field for algorithmic comparison, and mirrors the MNIST philosophy of accessible benchmarking.

**Reference:** Yang et al. (2023), MedMNIST v2 — A Large-Scale Lightweight Benchmark for 2D and 3D Biomedical Image Classification. Scientific Data. CC BY 4.0.
**Access:** https://medmnist.com/v2

---

## Quick Reference — All 2D Datasets

| Dataset | Modality | Task | Classes | Train | Val | Test | Sample |
|---------|----------|------|---------|-------|-----|------|--------|
| PathMNIST | Light microscopy (H&E) | Multi-class | 9 | 89,996 | 10,004 | 7,180 | 28×28×3 colour |
| ChestMNIST | X-ray | Multi-label | 14 | 78,468 | 11,219 | 22,433 | 28×28×1 grey |
| DermaMNIST | Dermatoscopy | Multi-class | 7 | 7,007 | 1,003 | 2,005 | 28×28×3 colour |
| OCTMNIST | Optical coherence tomography | Multi-class | 4 | 97,477 | 10,832 | 1,000 | 28×28×1 grey |
| PneumoniaMNIST | X-ray (paediatric) | Binary | 2 | 4,708 | 524 | 624 | 28×28×1 grey |
| RetinaMNIST | Fundus photography | Ordinal | 5 (ordered) | 1,080 | 120 | 400 | 28×28×3 colour |
| BreastMNIST | Ultrasound | Binary | 2 | 546 | 78 | 156 | 28×28×1 grey |
| BloodMNIST | Light microscopy (stained) | Multi-class | 8 | 11,959 | 1,712 | 3,421 | 28×28×3 colour |
| TissueMNIST | Fluorescence microscopy | Multi-class | 8 | 165,466 | 23,640 | 47,280 | 28×28×1 grey |
| OrganAMNIST | CT (axial) | Multi-class | 11 | 34,561 | 6,491 | 17,778 | 28×28×1 grey |
| OrganCMNIST | CT (coronal) | Multi-class | 11 | 12,975 | 2,392 | 8,216 | 28×28×1 grey |
| OrganSMNIST | CT (sagittal) | Multi-class | 11 | 13,932 | 2,452 | 8,827 | 28×28×1 grey |

## Quick Reference — All 3D Datasets

| Dataset | Modality | Task | Classes | Train | Val | Test | Sample |
|---------|----------|------|---------|-------|-----|------|--------|
| OrganMNIST3D | CT (volume) | Multi-class | 11 | 971 | 161 | 610 | 28³ |
| NoduleMNIST3D | CT (volume) | Binary | 2 | 1,158 | 165 | 310 | 28³ |
| FractureMNIST3D | CT (volume) | Multi-class | 3 | 1,027 | 103 | 240 | 28³ |
| AdrenalMNIST3D | Shape masks from CT | Binary | 2 | 1,188 | 98 | 298 | 28³ |
| VesselMNIST3D | Shape models from MRA | Binary | 2 | 1,335 | 191 | 382 | 28³ |
| SynapseMNIST3D | Electron microscopy (3D) | Binary | 2 | 1,230 | 177 | 352 | 28³ |

---

## Detailed Dataset Profiles

### PathMNIST
**Modality:** Light microscopy (H&E staining) — colon tissue
**Origin:** NCT-CRC-HE-100K + CRC-VAL-HE-7K (Kather et al.)
**Task:** 9-class (fat · empty slide · debris · lymphocytes · mucus · smooth muscle · healthy colon lining · tumour-associated connective tissue · cancer cells)

**What you are looking at:** A patch of colon tissue about 0.1 mm wide, cut 5 μm thin, stained with haematoxylin (nuclei blue-purple) and eosin (everything else pink). The standard diagnostic stain for cancer — still the clinical gold standard.

**Strengths:** Largest colour set; reasonably balanced; test set from a different clinical centre than training — a built-in generalisation check.

**Pitfalls:**
- Stain colour drifts between labs and days → colour augmentation is essential, not cosmetic
- Smooth muscle and tumour-associated connective tissue are visually near-identical at 28 px → read the confusion matrix, not just accuracy

---

### ChestMNIST
**Modality:** X-ray projection (chest)
**Origin:** NIH ChestX-ray14 (Wang et al.)
**Task:** 14-label multi-label (14 independent sigmoid outputs, not softmax)

**What you are looking at:** A 2D projection of the adult chest; bone absorbs X-rays (white), lung is dark (air). Everything in the beam path is summed into one flat image — ribs, heart, and lung overlap. One pixel ≈ 1 cm of patient.

**Findings:** enlarged heart · fluid around the lung · collapsed lung · air in the chest cavity · nodule · mass · pneumonia · fluid in the lung · consolidation · infiltration · emphysema · fibrosis · thickened lung lining · hernia

**Strengths:** The only multi-label set in the 2D collection.

**Pitfalls:**
- Labels mined automatically from radiology reports → noisy labels
- ~50% of images carry no finding at all; rarest finding < 1% → "answer no to everything" achieves > 90% accuracy
- **Metric:** Per-class AUC or average precision; accuracy is meaningless here

---

### DermaMNIST
**Modality:** Dermatoscopic photography (one skin lesion per image)
**Origin:** HAM10000 (Tschandl et al.) — CC BY-NC 4.0 (non-commercial)
**Task:** 7-class (ordinary mole · melanoma · benign keratosis · basal-cell carcinoma · precancerous keratosis · dermatofibroma · vascular lesion)

**What you are looking at:** A dermatoscope photograph — polarised light + contact lens removes surface glare to reveal pigment patterns under the skin.

**Strengths:** A real screening problem with clinical stakes; colour; small enough to iterate rapidly.

**Pitfalls:**
- ~66% of images are ordinary moles; melanoma is ~1 in 9 → per-class recall essential
- "Never predict melanoma" still gives high accuracy → this is the dangerous failure mode
- Non-commercial licence (CC BY-NC 4.0) — be aware if using for commercial purposes

---

### OCTMNIST
**Modality:** Optical coherence tomography (retinal cross-section)
**Origin:** Kermany et al. retinal OCT collection
**Task:** 4-class (healthy retina · diabetic macular oedema · abnormal neovascularisation · drusen/early AMD)

**What you are looking at:** A cross-section through the retina made by shining light and measuring echo timing (ultrasound with light). The retina is 0.25 mm thick; healthy images show clean horizontal bands; disease shows as bumps, gaps, fluid pockets.

**Strengths:** ~100k training images with strong layered texture → CNNs perform very well; good dataset for "easy baseline" experiments.

**Pitfalls:**
- Test set (1,000 images) is balanced by design; training is not → validation and test answer different questions
- Many images share a patient; naive random split leaks information

---

### PneumoniaMNIST
**Modality:** X-ray (paediatric chest, children under 5)
**Origin:** Kermany et al. paediatric chest radiographs
**Task:** Binary — normal vs. pneumonia

**What you are looking at:** Same physics as ChestMNIST. Pneumonia fills air spaces with fluid → white patches on normally dark lung.

**Strengths:** Small and fast — baseline trains in ~1 minute; ideal for studying augmentation and pre-training effects with many repeated runs.

**Pitfalls:**
- ~74% of training images are pneumonia → "always predict pneumonia" scores 74% accuracy
- **Metric:** Sensitivity and specificity (or AUC); never accuracy alone on this imbalanced set
- One hospital, one age group → no claims generalise beyond this setting

---

### RetinaMNIST
**Modality:** Fundus photography (inside of the eye)
**Origin:** DeepDRiD diabetic retinopathy grading challenge
**Task:** Ordinal — 5 ordered grades (0 = no damage to 4 = severe)

**What you are looking at:** A colour photograph of the retina taken through the pupil. Diabetes damages the retinal blood vessels; grading 0–4 tracks how advanced the damage is.

**Strengths:** The only ordinal task in MedMNIST v2.

**Pitfalls:**
- Only 1,080 training images → unstable numbers; use repeated seeds and report confidence intervals
- Confusing grade 0 with grade 4 is far worse than confusing adjacent grades → plain accuracy is wrong
- **Metric:** Quadratic-weighted kappa (penalises large errors more) or mean absolute error

---

### BreastMNIST
**Modality:** Ultrasound
**Origin:** BUSI breast ultrasound dataset (Al-Dhabyani et al.)
**Task:** Binary — malignant vs. normal-or-benign (original three classes collapsed to two)

**What you are looking at:** An echo map. Dense fibrous tissue → bright; fluid/cysts → dark. The grainy speckle is a physical property of ultrasound (not noise) and may carry diagnostic information.

**Strengths:** Smallest dataset here (546 training images) → ideal for experiencing overfitting first-hand.

**Pitfalls:**
- 156 test images → 1 image = 0.64 percentage points; two models "3% apart" differ by only 5 images
- Do not compare models without confidence intervals
- Appearance depends on operator (probe angle, pressure, scan settings)

---

### BloodMNIST
**Modality:** Light microscopy (stained blood smear)
**Origin:** Acevedo et al. peripheral blood cell dataset
**Task:** 8-class (neutrophil · eosinophil · basophil · lymphocyte · monocyte · immature granulocyte · erythroblast · platelet)

**What you are looking at:** One blood cell, centred in frame, on a stained slide (nucleus purple, cytoplasm pale). Automated blood-cell classification replaces routine manual laboratory work.

**Strengths:** Visually distinct classes; ~12k training images; one of the highest-scoring sets; confusion matrices are readable — the model makes the same mistakes a trainee makes.

**Pitfalls:**
- Because it is easy, scores saturate quickly; run-to-run variance dominates any small algorithmic difference
- Without repeated seeds you will report noise as a finding
- One lab, one staining protocol → domain shift is hidden

---

### TissueMNIST
**Modality:** Fluorescence microscopy (kidney cortex cells)
**Origin:** BBBC051 (Broad Institute) — human kidney cortex cells
**Task:** 8-class kidney cell structures (proximal tubule · thick ascending limb · distal convoluted tubule · collecting duct · glomerular endothelium · interstitial endothelium · podocytes · leukocytes)

**What you are looking at:** A single cell cropped from a 3D fluorescence stack and flattened to 2D. Most structure a biologist uses to identify cell type is lost in the flattening and shrinking.

**Strengths:** Largest dataset in MedMNIST v2 (165k train) → data loading and epoch time become engineering constraints; subsampling is a valid and correct first move.

**Pitfalls:**
- Published baselines: ~0.68 accuracy → a low score is not automatically your bug; check the baseline first
- One epoch over 165k images is slow on CPU → fix a subsample size early

---

### OrganAMNIST / OrganCMNIST / OrganSMNIST
**Modality:** CT (computed tomography) — A = axial, C = coronal, S = sagittal view
**Origin:** LiTS — Liver Tumour Segmentation Benchmark
**Task:** 11-class organ identification (liver · spleen · pancreas · heart · bladder · left and right kidney · left and right lung · left and right thigh bone)

**CT physics:** Values are calibrated — air ≈ −1000 HU, water = 0 HU, soft tissue just above, bone far above. Axial = horizontal slices (most clinically common); coronal = front-to-back; sagittal = side view.

**Why all three exist:** A, C, and S use identical labels, identical patients, but different view directions — a ready-made controlled experiment for evaluating view-invariance.

**Strengths:** Training and test use different patients → test score genuinely generalises.

**Pitfalls:**
- Left versus right organ is nearly undecidable from an isolated crop; position in the body is thrown away → expect a confusion block for symmetric pairs
- OrganC (12k) and OrganS (14k) have a third of OrganA's data (34k) on identical classes — a direct lesson in data efficiency

---

## 3D Datasets

### OrganMNIST3D
Same 11 organ classes as OrganA/C/S but as 28³ voxel volumes. The model can now see the organ's 3D shape (liver = wedge, kidney = bean, thigh bone = rod). Small dataset (971 volumes) — a direct 2D vs. 3D comparison against the axial dataset is the primary experiment.

**Pitfalls:** 971 training volumes for 11 classes ≈ 88 per class; 3D convolutions have far more parameters → overfitting is the default. No ImageNet equivalent for 3D pre-training.

### NoduleMNIST3D
Lung nodule classification (benign vs. malignant) from chest CT cubes. Labels derived from radiologist malignancy ratings — the label is an expert judgement, not a biopsy, making this the best dataset for the "trustworthy AI" discussion.

**Pitfalls:** Check class balance in the first 5 minutes and fix the metric before training.

### FractureMNIST3D
Rib fracture type (buckle / non-displaced / displaced) from chest CT. The classes differ by millimetres of bone geometry, not by texture or colour.

**Pitfalls:** Interpolation-based augmentation blurs the sharp bone edges that separate the classes — justify every augmentation switched on. Hairline cracks may be one voxel wide at 28³.

### AdrenalMNIST3D
Shape-only (binary mask, no image intensities) of adrenal glands — normal vs. hyperplasia (enlarged). The only clue is geometry.

**Pitfalls:** Input is the output of a segmentation step → inherits segmentation errors. Brightness augmentation is meaningless on a binary mask. Random scaling may remove the size feature that defines "enlarged".

### VesselMNIST3D
Brain artery segment (healthy vs. aneurysm) from MRA-derived surface models. An aneurysm is a balloon-like bulge; a healthy segment looks like a tube or Y.

**Pitfalls:** ~1 in 9 samples is an aneurysm → "always healthy" scores ~89%. Fix metric before training.

### SynapseMNIST3D
Neuron synapse classification (excitatory vs. inhibitory) from rat brain electron microscopy. An electron microscope resolves nanometres; each 28³ cube covers only a few micrometres of brain tissue.

**Pitfalls:** You cannot check a single label by eye — a feature, not a bug, for understanding the limits of model interpretability. All cubes come from one animal and one session; no external domain exists for testing.

---

## Metric Selection Guide

| Task type | Recommended metric | Why not accuracy alone |
|-----------|--------------------|----------------------|
| Multi-class, balanced | Accuracy + per-class recall | Catch systematic class failures |
| Multi-class, imbalanced | Per-class recall + macro F1 | Majority class swamps accuracy |
| Binary, imbalanced | AUC + sensitivity/specificity at stated threshold | "Always negative" achieves high accuracy |
| Multi-label | Per-label AUC or average precision | Single label accuracy meaningless for independent tasks |
| Ordinal | Quadratic-weighted kappa or MAE | Penalises large ordinal errors more than adjacent ones |
| 3D, small dataset | Report with multiple seeds and confidence interval | High variance — single run is noise |

---

## Experimental Design Principles (from Team Project Briefing)

1. **Explore before training** — plot class distribution; identify imbalance before choosing a metric.
2. **Majority baseline** — state what "always predict the most common class" achieves; nothing below this is useful.
3. **Controlled comparisons** — change exactly one factor (learning rate, augmentation, architecture) per experiment; hold everything else fixed.
4. **Honest data split** — train, validation, and test sets never touch each other; if data splits are provided, use them.
5. **Error analysis** — look at concrete failure cases; form a hypothesis for why the model fails on each.
6. **Reproducibility** — fix random seeds; a fresh runtime top-to-bottom must reproduce your numbers.

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/ai-in-medicine]] | The clinical and domain context for why these datasets matter |
| [[concepts/ml-model-training-evaluation]] | Train/val/test split, cross-validation, bias-variance tradeoff, metric selection |
| [[concepts/neural-networks-linear-models]] | CNNs are the primary architecture applied to all these datasets |
| [[concepts/ml-data-understanding]] | EDA, class distribution analysis, augmentation strategies |
| [[sources/ml-summer-school-lec2]] | Primary source — team project briefing with full dataset profiles |
