# Machine Learning Lecture 2 — Team Project: MedMNIST v2 Dataset Briefing

## Slide 1

International Summer School:
Trustworthy AI –
Machine Learning Meets Blockchain

Microcredential 2: Machine Learning

Team Project: MedMNIST v2 Dataset Briefing

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

## Slide 2

Your team project
Assignment of groups to datasets

| Group number | Group members | Dataset |
|---|---|---|
| 1 | Ms Charmaine Choo, Ms Srinithi Ramasubramanian, Ms Zi Qin Wong | PathMNIST |
| 2 | Mr Sean Chye, Mr Paul Yao Kudaya, Mr Xian Guang Tan, Mr Zheng Liang Tan | DermaMNIST |
| 3 | Mr Uwais Abdul Rahman, Mr Mohaamad Nabbhil Bin Mohamed Rafi, Mr Izzul Helmi | OCTMNIST |
| 4 | Mr Mohaamed Akram, Mr Kai Wen Chan, Mr Thabith Mohamed | PneumoniaMNIST |
| 5 | Mr Yu Han Awe, Mr Yong'en Jonavan Voo | BreastMNIST |
| 6 | Mr Wei Feng Chua, Mr Derrick Neo, Mr Ruven Ng | BloodMNIST |
| 7 | Mr Teng Ng, Mr Justin Teo, Mr Hong Rui Toh | TissueMNIST |
| 8 | Ms Eng Thong Phoebe Hung, Mr Jerry Kok, Mr Sakilan P | OrganAMNIST |
| 9 | Mr Martin Fabian, Ms Adithi Mandhala, Ms Cheng Yin Tang | OrganCMNIST |
| 10 | Mr Qi Shu, Mr Huruy Zerihun | OrganSMNIST |

Link to the datasets: https://medmnist.com/v2

## Slide 3

Your team project
Assignment of groups to datasets

Suggested slide structure

• Dataset: modality, classes, example images, class distribution, majority baseline
• Setup: model, training procedure, metrics and why you chose them
• Baseline: results with seed spread
• Experiments: what you changed, what happened, what you conclude
• Error analysis: concrete failure cases and hypotheses
• Test result, limitations, and what you would do with one more week

Link to the datasets: https://medmnist.com/v2

## Slide 4

Your team project
One dataset, one honest result

Build a working image-classification pipeline on real clinical data, and be able to say, in plain words, what your numbers do and do not prove.

Tasks
1. Explore your dataset — Load it, look at it, and plot the class distribution before you train anything at all.
2. First baseline method — Select appropriate metrics and justify your choice, and state all results of your experiments.
3. Experiment with your method — Execute controlled comparisons: change a single factor, hold the rest fixed.
4. Error analysis — Identify concrete failure cases with hypothesis.
5. Present and discuss — Ten minutes. Notebook runs top to bottom.

→ Groups of three, one dataset per group

What you hand in
A jupyter notebook that runs. Fresh runtime, top to bottom, seeds fixed.
Presentation of results. Dataset → method → result → your comparisons → error analysis → discussion

You pass if all six are true
✓ Reproducible: we re-run it and get your numbers.
✓ Honest split: the three sets never mix.
✓ Documented baseline: appropriate metrics and numbers.
✓ Controlled comparison: one factor changed at a time.
✓ Error analysis: failures and hypotheses.
✓ Shared understanding: all members can explain it.

## Slide 5

PathMNIST
Colon tissue on a microscope slide

MODALITY: Light microscopy (H&E)
TASK: Multi-class
CLASSES: 9
TRAIN / VAL / TEST: 89,996 / 10,004 / 7,180
ONE SAMPLE: 28 × 28 × 3, colour

Origin: NCT-CRC-HE-100K + CRC-VAL-HE-7K (Kather et al.)
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
A patch of colon tissue about a tenth of a millimetre wide, cut five micrometres thin and dyed with two standard stains: haematoxylin turns cell nuclei blue-purple, eosin turns everything else pink. This is the oldest imaging technique in medicine, and still the one that decides whether a tumour is called cancer.

What the model has to decide
Which of nine tissue types fills this patch. One label per image, exactly one is correct.
fat · empty slide · debris · lymphocytes (immune cells) · mucus · smooth muscle · healthy colon lining · tumour-associated connective tissue · cancer cells

Why this one is worth having
The largest colour set here and reasonably balanced, so a real model trains in minutes. Its test set comes from a different clinical centre than train and validation: a free, built-in generalisation check.

What will bite you
Stain colour drifts between labs and between days, so colour augmentation is not cosmetic. Smooth muscle and tumour-associated connective tissue look almost identical at 28 px: read the confusion matrix, not the accuracy.

## Slide 6

ChestMNIST
Chest X-rays

MODALITY: X-ray projection
TASK: Multi-label
CLASSES: 14, independent
TRAIN / VAL / TEST: 78,468 / 11,219 / 22,433
ONE SAMPLE: 28 × 28 × 1, grey

Origin: NIH ChestX-ray14 (Wang et al.)
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
A shadow picture, not a photograph. X-rays pass through the body; bone absorbs them and comes out white, air-filled lung comes out dark. Everything the beam passed through is summed into one flat image, so ribs, heart and lung overlap. A whole adult chest is squeezed into 28 px, one pixel is roughly a centimetre of patient.

What the model has to decide
Fourteen independent yes/no questions about the same image. An image may carry none, one or several findings — so this is fourteen sigmoids, not one softmax.
enlarged heart · fluid around the lung · collapsed lung · air in the chest cavity · nodule · mass · pneumonia · fluid in the lung · consolidation · infiltration · emphysema · fibrosis · thickened lung lining · hernia

Why this one is worth having
The only multi-label set in the collection. It forces you to drop accuracy and think in per-class AUC or average precision, and to choose a decision threshold → a genuinely clinical question.

What will bite you
The labels were mined automatically from radiology reports, so they are noisy. About half the images carry no finding and the rarest appears in well under one percent: answering "no" everywhere already scores above 90%.

## Slide 7

DermaMNIST
Skin lesions through a dermatoscope

MODALITY: Dermatoscopic photography
TASK: Multi-class
CLASSES: 7
TRAIN / VAL / TEST: 7,007 / 1,003 / 2,005
ONE SAMPLE: 28 × 28 × 3, colour

Origin: HAM10000 (Tschandl et al.) — licence CC BY-NC 4.0
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
A close-up photograph of one spot on the skin, taken with a dermatoscope: a lens with its own light source, pressed onto the skin. Contact and polarised light remove the surface glare, so the pigment pattern underneath becomes visible. The field of view is about a centimetre, and one lesion fills the frame.

What the model has to decide
Which of seven lesion types this is — including the one that matters most, melanoma, against the ordinary mole it can be mistaken for.
ordinary mole (melanocytic nevus) · melanoma · benign keratosis · basal-cell carcinoma · precancerous keratosis · dermatofibroma · vascular lesion

Why this one is worth having
A real screening problem, in colour, small enough to iterate on all week. The class you care about is not the class you have data for, which turns loss, class weighting and threshold into real decisions rather than defaults.

What will bite you
Two thirds of the images are ordinary moles and melanoma is about one in nine, so report per-class recall: a model that never says "melanoma" still looks fine on accuracy. Also the one non-commercial licence here.

## Slide 8

OCTMNIST
A cross-section through the retina

MODALITY: Optical coherence tomography
TASK: Multi-class
CLASSES: 4
TRAIN / VAL / TEST: 97,477 / 10,832 / 1,000
ONE SAMPLE: 28 × 28 × 1, grey

Origin: retinal OCT collection (Kermany et al.)
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
Not a picture of the eye from outside, but a slice through the retina, made by shining light in and timing the echoes — ultrasound logic, with light instead of sound. The retina is a quarter of a millimetre thick and built in layers, so a healthy image looks like clean horizontal bands. Disease shows up as bumps, gaps and pockets of fluid.

What the model has to decide
Which of four retinal conditions the cross-section shows, including the healthy case.
healthy retina · fluid swelling caused by diabetes (macular oedema) · abnormal new vessels growing under the retina · drusen (early age-related deposits)

Why this one is worth having
Nearly 100,000 training images with strong layered texture: convolutional networks do very well here. Use it as the cohort's "what does easy look like" reference, and afford yourself several controlled runs.

What will bite you
The test set holds only 1,000 images and is balanced by design while training is not, so validation and test answer different questions. Many images share a patient, so a naive random split leaks.

## Slide 9

PneumoniaMNIST
Children's chest X-rays

MODALITY: X-ray projection
TASK: Binary
CLASSES: 2
TRAIN / VAL / TEST: 4,708 / 524 / 624
ONE SAMPLE: 28 × 28 × 1, grey

Origin: paediatric chest radiographs (Kermany et al.)
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
The same shadow physics as ChestMNIST, but the patients are children under five and there is only one question on the table. Pneumonia is an infection that fills the air spaces of the lung with fluid and cells; air is dark on an X-ray and fluid is bright, so the normally black lung develops white patches.

What the model has to decide
Pneumonia: yes or no. One output, one sigmoid, and one threshold that you have to choose deliberately.
normal · pneumonia

Why this one is worth having
Small and fast — a baseline trains in about a minute, so you can run many careful experiments instead of one slow one. The clean place to see what augmentation and pre-trained weights are actually worth.

What will bite you
Roughly three quarters of the training images are pneumonia, so "always pneumonia" scores about 74%. Quote sensitivity and specificity, or AUC. One hospital, one age group — no claims beyond that.

## Slide 10

RetinaMNIST
A photograph of the inside of the eye

MODALITY: Fundus photography
TASK: Ordinal
CLASSES: 5, ordered
TRAIN / VAL / TEST: 1,080 / 120 / 400
ONE SAMPLE: 28 × 28 × 3, colour

Origin: DeepDRiD challenge
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
A colour photograph of the back wall of the eye, taken straight through the pupil. The retina is the only place in the body where blood vessels can be photographed directly, without cutting. The bright disc is where the optic nerve leaves the eye; the darker area beside it is the part you read with. Diabetes damages exactly these vessels.

What the model has to decide
How advanced the damage is, from 0 (nothing visible) to 4 (severe). The grades are ordered: confusing 0 with 4 is far worse than confusing 0 with 1.
grade 0 → grade 4, from no visible damage to severe disease

Why this one is worth having
The only ordinal task in MedMNIST v2, and therefore the only one where plain accuracy is obviously the wrong instrument. Quadratic-weighted kappa or mean absolute error respect the ordering — choosing is half the work.

What will bite you
Only 1,080 training images across five grades, so expect unstable numbers and use repeated seeds. Grading is a human judgement and experts disagree; the lesions defining grade 1 are smaller than one pixel.

## Slide 11

BreastMNIST
Breast ultrasound

MODALITY: Ultrasound
TASK: Binary
CLASSES: 2
TRAIN / VAL / TEST: 546 / 78 / 156
ONE SAMPLE: 28 × 28 × 1, grey

Origin: BUSI breast ultrasound set (Al-Dhabyani et al.)
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
An echo map. A probe sends short sound pulses into the tissue and records what comes back: bright means a strong echo from dense, fibrous tissue, dark means almost none, as in fluid or a cyst. The grainy speckle is a physical property of ultrasound, not sensor noise — do not filter it away without asking what it carries.

What the model has to decide
Malignant, or not. Note that the original three classes were collapsed into two, so "normal" and "benign" share one bucket.
malignant · normal or benign (the two were merged)

Why this one is worth having
The smallest dataset here — ideal for feeling rather than reading about overfitting, and for showing what augmentation and pre-trained weights are worth. Fast enough for ten repeated runs and a reported spread.

What will bite you
With 156 test images one image is worth 0.64 percentage points, so two models "3% apart" differ by five images. Without an interval that comparison is not evidence. Appearance also depends on the operator.

## Slide 12

BloodMNIST
Single blood cells under the microscope

MODALITY: Light microscopy (stained)
TASK: Multi-class
CLASSES: 8
TRAIN / VAL / TEST: 11,959 / 1,712 / 3,421
ONE SAMPLE: 28 × 28 × 3, colour

Origin: peripheral blood cell set (Acevedo et al.)
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
One blood cell, centred in the frame, on a glass slide stained so that the nucleus goes purple and the surrounding cytoplasm stays pale. A cell is around ten micrometres across — a hundred of them fit across a millimetre. Sorting and counting them by hand is routine laboratory work, which is exactly why automating it is worth money.

What the model has to decide
Which of eight cell types is in the frame. Exactly one is correct, and the classes are visually distinct.
neutrophil · eosinophil · basophil · lymphocyte · monocyte · immature granulocyte · erythroblast (young red-cell precursor) · platelet (clotting fragment)

Why this one is worth having
Colour, eight fairly clean classes, twelve thousand training images: one of the highest-scoring sets here. Its confusion matrices are genuinely readable — the model makes the mistakes a trainee makes.

What will bite you
Because it is easy, scores saturate and the gap between two models can disappear into run-to-run noise; without repeated seeds you will report noise as a finding. One lab, one staining protocol.

## Slide 13

TissueMNIST
Kidney cells, flattened out of 3-D

MODALITY: Fluorescence microscopy
TASK: Multi-class
CLASSES: 8
TRAIN / VAL / TEST: 165,466 / 23,640 / 47,280
ONE SAMPLE: 28 × 28 × 1, grey

Origin: BBBC051 human kidney cortex cells (Broad Institute)
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
A single cell cut out of a microscopy image of kidney cortex. The original recording was a small 3-D stack; here it has been flattened into one grey image and shrunk to 28 px. The result is honest but bleak — mostly a bright blob on a dark background. Very little of the structure a biologist would use survives.

What the model has to decide
Which of eight structures of the kidney cortex the cell belongs to — mostly parts of the tubule system that filters blood and concentrates urine.
proximal tubule · thick ascending limb · distal convoluted tubule · collecting duct · glomerular endothelium · interstitial endothelium · podocytes · leukocytes

Why this one is worth having
By far the largest set here: the only one where data loading and epoch time become real engineering constraints, and where subsampling deliberately is the correct move rather than a shortcut.

What will bite you
Published baselines land near 0.68 accuracy, so a low number is not automatically your bug — check the baseline before you rebuild the pipeline. One epoch over 165,000 images is slow on a CPU: fix a subsample on Monday.

## Slide 14

OrganAMNIST
Abdominal CT, axial view

MODALITY: Computed tomography (CT)
TASK: Multi-class
CLASSES: 11
TRAIN / VAL / TEST: 34,561 / 6,491 / 17,778
ONE SAMPLE: 28 × 28 × 1, grey

Origin: LiTS — Liver Tumour Segmentation Benchmark
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
CT takes X-ray projections from all around the body and computes cross-sections from them. Its grey values are calibrated — air near −1000, water 0, soft tissue just above, bone far above — so here brightness means something physical. Axial means slices perpendicular to the body's long axis — like cutting a loaf of bread.

What the model has to decide
Which of eleven organs sits in this crop. One label per image, and the crop is centred on the organ.
liver · spleen · pancreas · heart · bladder · left and right kidney · left and right lung · left and right thigh bone

Why this one is worth having
A, C and S differ in nothing but the viewing direction — a ready-made controlled experiment: train on one view, test on another. Axial is the view radiologists read most, and the easiest of the three.

What will bite you
Left against right organ is nearly undecidable from an isolated crop: what separates them is position in the body, which the crop throws away. Expect a confusion block. Training and test use different patients, so the test score really generalises.

## Slide 15

OrganCMNIST
Abdominal CT, coronal view

MODALITY: Computed tomography (CT)
TASK: Multi-class
CLASSES: 11
TRAIN / VAL / TEST: 12,975 / 2,392 / 8,216
ONE SAMPLE: 28 × 28 × 1, grey

Origin: LiTS — Liver Tumour Segmentation Benchmark
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
CT takes X-ray projections from all around the body and computes cross-sections from them. Its grey values are calibrated — air near −1000, water 0, soft tissue just above, bone far above — so here brightness means something physical. Coronal means slices from front to back — the orientation of a classic standing chest X-ray.

What the model has to decide
Which of eleven organs sits in this crop. One label per image, and the crop is centred on the organ.
liver · spleen · pancreas · heart · bladder · left and right kidney · left and right lung · left and right thigh bone

Why this one is worth having
A, C and S differ in nothing but the viewing direction — a ready-made controlled experiment: train on one view, test on another. A third of the data of the axial set on identical classes: an immediate lesson in data efficiency.

What will bite you
Left against right organ is nearly undecidable from an isolated crop: what separates them is position in the body, which the crop throws away. Expect a confusion block. With fewer images per class, pre-trained weights matter more here than in the axial set.

## Slide 16

OrganSMNIST
Abdominal CT, sagittal view

MODALITY: Computed tomography (CT)
TASK: Multi-class
CLASSES: 11
TRAIN / VAL / TEST: 13,932 / 2,452 / 8,827
ONE SAMPLE: 28 × 28 × 1, grey

Origin: LiTS — Liver Tumour Segmentation Benchmark
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
CT takes X-ray projections from all around the body and computes cross-sections from them. Its grey values are calibrated — air near −1000, water 0, soft tissue just above, bone far above — so here brightness means something physical. Sagittal means slices from left to right — the side view, as if looking at the patient in profile.

What the model has to decide
Which of eleven organs sits in this crop. One label per image, and the crop is centred on the organ.
liver · spleen · pancreas · heart · bladder · left and right kidney · left and right lung · left and right thigh bone

Why this one is worth having
A, C and S differ in nothing but the viewing direction — a ready-made controlled experiment: train on one view, test on another. The hardest of the three views, and therefore the most rewarding to compare against the other two.

What will bite you
Left against right organ is nearly undecidable from an isolated crop: what separates them is position in the body, which the crop throws away. Expect a confusion block. In a side view left and right organs project onto each other.

## Slide 17

OrganMNIST3D
The same organs, as little cubes

MODALITY: Computed tomography, 3-D
TASK: Multi-class
CLASSES: 11
TRAIN / VAL / TEST: 971 / 161 / 610
ONE SAMPLE: 28 × 28 × 28, volume

Origin: LiTS — Liver Tumour Segmentation Benchmark
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
Not an image but a small block of 28 × 28 × 28 grey values — think of a stack of 28 slices, or a cube holding 22,000 tiny cells of brightness. The model can now see the organ's actual three-dimensional shape: a liver is a wedge, a kidney a bean, a thigh bone a rod. The 2-D crops do not contain that.

What the model has to decide
Which of eleven organs the volume contains — the same eleven classes as OrganA/C/S, so a direct 2-D against 3-D comparison is available.
liver · spleen · pancreas · heart · bladder · left and right kidney · left and right lung · left and right thigh bone

Why this one is worth having
The cleanest "does 3-D pay for itself?" question in the collection, against a 2-D baseline that already exists on the very same patients and classes. Small enough to still train on a CPU.

What will bite you
971 training volumes for eleven classes is about 88 examples each, while a 3-D convolution has far more parameters than its 2-D counterpart: overfitting is the default outcome. And there is no ImageNet for volumes.

## Slide 18

NoduleMNIST3D
Lung nodules in chest CT

MODALITY: Computed tomography, 3-D
TASK: Binary
CLASSES: 2
TRAIN / VAL / TEST: 1,158 / 165 / 310
ONE SAMPLE: 28 × 28 × 28, volume

Origin: LIDC-IDRI thoracic CT database
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
A cube cut out of a chest CT around a nodule — a small, roughly round lump in lung tissue. Nodules are common and mostly harmless; a few are early lung cancer. Radiologists judge them by size, edge sharpness and how spiky the border is, all of which are properties of the 3-D shape rather than of one slice.

What the model has to decide
Benign or malignant. The label is not a biopsy result: it is derived from radiologists' malignancy ratings, with the undecided middle rating dropped.
benign · malignant

Why this one is worth having
A genuine clinical decision with a cost attached — a missed cancer against an unnecessary operation — and the best dataset here for the trustworthy-AI discussion, because the ground truth is visibly an expert opinion.

What will bite you
Only 1,158 training cubes, and the classes are not equally represented: check the balance in your first five minutes and pick the metric accordingly. The class boundary is a threshold through a subjective scale.

## Slide 19

FractureMNIST3D
Broken ribs in chest CT

MODALITY: Computed tomography, 3-D
TASK: Multi-class
CLASSES: 3
TRAIN / VAL / TEST: 1,027 / 103 / 240
ONE SAMPLE: 28 × 28 × 28, volume

Origin: RibFrac rib-fracture CT dataset
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
A cube cut from a chest CT around a broken rib. Bone absorbs X-rays strongly, so the rib is the bright curved bar and everything darker around it is soft tissue and air. The three classes differ only in how the bone failed: bent but intact, cracked with the ends still aligned, or cracked with the ends pushed apart.

What the model has to decide
Which of three fracture types this is — a fine-grained distinction that changes how the patient is treated.
buckle (bent, still one piece) · non-displaced (crack, ends aligned) · displaced (ends moved apart)

Why this one is worth having
The most fine-grained 3-D task here: the classes differ by millimetres of geometry, not by texture. That makes visualising a few volumes before training genuinely necessary rather than merely good practice.

What will bite you
1,027 training cubes over three subtle classes, and a hairline crack may be one voxel wide at 28³. Interpolating augmentation blurs exactly the sharp edge that separates two of your classes — justify every one you switch on.

## Slide 20

AdrenalMNIST3D
Shape only — no texture at all

MODALITY: Shape masks from CT
TASK: Binary
CLASSES: 2
TRAIN / VAL / TEST: 1,188 / 98 / 298
ONE SAMPLE: 28 × 28 × 28, volume

Origin: AdrenalMNIST3D, from CT segmentations (Yang et al.)
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
The adrenal glands are two small hormone factories, one on top of each kidney, normally about the size and shape of a flattened almond. What you get here is not the CT image but its outline: a binary mask, voxel by voxel, of where the gland is and where it is not. All brightness information has already been removed.

What the model has to decide
Normal gland, or enlarged gland (hyperplasia — an overgrowth of gland tissue). The only clue available is the shape.
normal · hyperplasia (enlarged)

Why this one is worth having
The purest shape problem in the collection, and it answers a real question about medical imaging AI: how much of the performance comes from texture and how much from geometry alone? Very fast to train.

What will bite you
The input is itself the output of a segmentation step, so you inherit its errors. Brightness augmentation is meaningless on a mask — and random scaling may augment away the very feature that defines "enlarged".

## Slide 21

VesselMNIST3D
Brain arteries and their bulges

MODALITY: Shape models from MRA
TASK: Binary
CLASSES: 2
TRAIN / VAL / TEST: 1,335 / 191 / 382
ONE SAMPLE: 28 × 28 × 28, volume

Origin: IntrA intracranial aneurysm dataset
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
A short piece of an artery in the brain, reconstructed as a 3-D surface from angiography and then turned into a cube of voxels — geometry only, no image intensities. An aneurysm is a balloon-like bulge in the artery wall; if it bursts it causes a stroke. A healthy segment looks like a tube or a Y, an aneurysm has a sac.

What the model has to decide
Healthy vessel segment, or aneurysm. Roughly one sample in nine is an aneurysm.
healthy vessel segment · aneurysm

Why this one is worth having
The clearest imbalance lesson of the eighteen: answering "healthy" for everything already scores about 89%. Small, fast, and visually intuitive — you can look at a bulge and agree with the label.

What will bite you
Choose the metric before you train — balanced accuracy, AUC, or precision and recall at a stated threshold — and keep it fixed. The segments were cut out by hand, so where one ends may itself hint at the label.

## Slide 22

SynapseMNIST3D
Electron microscopy, the nanometre scale

MODALITY: Electron microscopy, 3-D
TASK: Binary
CLASSES: 2
TRAIN / VAL / TEST: 1,230 / 177 / 352
ONE SAMPLE: 28 × 28 × 28, volume

Origin: rat brain volume, multi-beam electron microscopy
Example images: MedMNIST v2 (Yang et al., 2023), CC BY 4.0

What you are actually looking at
Not X-rays and not light, but electrons: an electron microscope resolves single nanometres, and each cube here covers only a few micrometres of brain tissue. Inside sits one synapse — the contact where one nerve cell passes a signal to the next. A chest X-ray and this cube are ten orders of magnitude apart.

What the model has to decide
Excitatory or inhibitory — whether this synapse makes the receiving cell more, or less, likely to fire. Neuroscientists tell them apart by subtle differences in appearance.
excitatory synapse · inhibitory synapse

Why this one is worth having
A completely different corner of biomedical imaging from everything else here, and the one dataset where you, as a non-expert, cannot check a single label by eye. Sit with that for a moment.

What will bite you
1,230 training cubes, and the class difference lives in fine texture that barely survives 28³. All cubes come from one animal and one session, so there is no second domain to test against.

## Slide 23

Contact
www.re-mic.de

OTH REGENSBURG CONTACT
Tobias Rueckert, M. Sc.
Regensburg Medical Image Computing (ReMIC)
Regensburg Center for Artificial Intelligence (RCAI)
Regensburg Center of Health Sciences and Technology (RCHST)
Regensburg Center of Biomedical Engineering (RCBE)

+49 941 943 1314
Galgenbergstraße 32, 93053 Regensburg
tobias.rueckert@oth-regensburg.de
