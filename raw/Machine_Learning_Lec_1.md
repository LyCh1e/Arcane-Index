# Machine Learning Lecture 1 — Part 1: Kickoff & Motivation

## Slide 1

International Summer School:
Trustworthy AI –
Machine Learning Meets Blockchain

Microcredential 2: Machine Learning

Part 1: Kickoff & Motivation

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

## Slide 2

*(no extractable text — image-only slide)*

## Slide 3

About Me
Milestones

Tobias Rueckert
PhD Student @ TUM,
Research Assistant @ OTH,
ML Developer @ AKTORmed

tobias.rueckert@oth-regensburg.de

10/2015 – 03/2019 OTH Regensburg, B. Sc.
Computer Science, B. Sc. Bachelor Thesis: Deep learning-based 2D localization of surgical instruments in video images

03/2019 – 08/2021 OTH Regensburg, M. Sc.
Computer Science, M. Sc. Master Thesis: Predicting Postoperative Mortality after Radical Cystectomy for Bladder Cancer using Machine Learning Methods combining Medical Images and Clinical Data

Since 08/2021 – now OTH Regensburg & TU Munich
PhD, Topic: Deep learning-based recognition and tracking of surgical instruments in video sequences by incorporating spatial and temporal information

Since 09/2024 – now AKTORmed Robotic Surgery
Machine Learning Developer in surgical instrument recognition and tracking

## Slide 4

Table of Contents

1 Kickoff & Motivation
2a/b ML – Basics and Class. Models
   Practice: Python Basics, ML Classifiers
3 Model Evaluation
   Practice: PyTorch Tutorial
4a Digital Images
4b Operations on Images
5 Convolutional Neural Networks
6 Transfer Learning and Domain Adaptation
7 Attention and Transformers
8 Final Assessment

## Slide 5

AI in Medicine
ReMIC Lab

## Slide 6

Regensburg Medical Image Computing

Endoscopy · Oncology · Surgery

## Slide 7

Regensburg Medical Image Computing

Endoscopy · Oncology · Surgery
Barrett Esophagus

## Slide 8

ReMIC – Barrett Esophagus
Diagnosis of Esophageal Cancer

Esophagus, Endoscope, Stomach, Monitor
Endoscopic Examination

## Slide 9

ReMIC – Barrett Esophagus
Diagnosis of Esophageal Cancer

Cancer · Barrett · Healthy Mucous Membrane
Endoscopic Examination

## Slide 10

ReMIC – Barrett Esophagus
Diagnosis of Esophageal Cancer

Options for Visualization
Preview
Motion Estimation
Status
Livestream with AI-Overlays

## Slide 11

Regensburg Medical Image Computing

Endoscopy · Oncology · Surgery
3D GI Tract Reconstruction

## Slide 12

Overview
Dynamic 3D reconstruction of the GI Tract

Fly-Through Navigation (Source: [1])
3D Semantics (Source: adapted from [2])
Dynamic Tissue Modeling (Source: [3])

© Danilo Weber Nunes, OTH Regensburg

[1] Bonilla, S., Zhang, S., Psychogyios, D., Stoyanov, D., Vasconcelos, F. and Bano, S., 2024, October. Gaussian pancakes: Geometrically-regularized 3d gaussian splatting for realistic endoscopic reconstruction. In International Conference on Medical Image Computing and Computer-Assisted Intervention (pp. 274-283). Cham: Springer Nature Switzerland.
[2] Ma, R., Wang, R., Pizer, S., Rosenman, J., McGill, S.K. and Frahm, J.M., 2019. Real-time 3D reconstruction of colonoscopic surfaces for determining missing regions. In Medical Image Computing and Computer Assisted Intervention–MICCAI 2019, Part V 22 (pp. 573-582). Springer International Publishing.
[3] Wang, Yuehao, Yonghao Long, Siu Hin Fan, and Qi Dou. "Neural rendering for stereo 3d reconstruction of deformable tissues in robotic surgery." In International conference on medical image computing and computer-assisted intervention, pp. 431-441. Cham: Springer Nature Switzerland, 2022.

## Slide 13

Current Work
Camera Pose Estimation – Point Tracking

Dynamic Points
LEAP-VO on the EndoNeRF Dataset

© Danilo Weber Nunes, OTH Regensburg

## Slide 14

Regensburg Medical Image Computing

Endoscopy · Oncology · Surgery
Trustworthiness

## Slide 15

ReMIC – Trustworthiness
Domain Shift, Out of Distribution Detection (OOD), and Uncertainty

Hospital 1[1,2] · Hospital 2[1,2] · Hospital 3[1,2] · Hospital 4[3]

[1] Rueckert, T., Rauber, D., Maerkl, R., … Wilhelm, D., & Palm, C. (2025). Comparative validation of surgical phase recognition, instrument keypoint estimation, and instrument instance segmentation in endoscopy: Results of the PhaKIR 2024 challenge. arXiv preprint.
[2] Rueckert, T., Maerkl, R., Rauber, D., …, Rueckert, D., Feussner, H., Wilhelm, D., & Palm, C. (2025). Video Dataset for Surgical Phase, Keypoint, and Instrument Recognition in Laparoscopic Surgery (PhaKIR). arXiv preprint.
[3] Twinanda, A. P., Shehata, S., Mutter, D., Marescaux, J., de Mathelin, M., & Padoy, N. (2017). EndoNet: A Deep Architecture for Recognition Tasks on Laparoscopic Videos. IEEE transactions on medical imaging, 36(1), 86–97.

## Slide 16

ReMIC – Trustworthiness
Example: Plant identification app

Hemp, a kind of Hemp (Cannabis)
Other names: true hemp, common hemp
Botanical name: cannabis sativa

© Prof. Dr. Christoph Palm, OTH Regensburg

## Slide 17

ReMIC – Trustworthiness
Example: Plant identification app

Avocado, a species of persea, in the laurel family
Other names: avocado pear tree, avocado pear, alligator pear, butter fruit
Botanical name: Persea americana

© Prof. Dr. Christoph Palm, OTH Regensburg

## Slide 18

ReMIC – Trustworthiness
Example: Plant identification app

Other names: avocado pear tree, avocado pear, alligator pear, butter fruit
Botanical name: Persea americana

Basic information / Care / Culture
Health of the plant: This plant looks sick!
Search for solutions

Causes of illness: Overwatering, Infected with disease

© Prof. Dr. Christoph Palm, OTH Regensburg

## Slide 19

ReMIC – Trustworthiness
Example: Oral cavity carcinoma

© Prof. Dr. Christoph Palm, OTH Regensburg

## Slide 20

ReMIC – Trustworthiness
Example: Oral cavity carcinoma

© Prof. Dr. Christoph Palm, OTH Regensburg

## Slide 21

ReMIC – Trustworthiness
Benchmarks for OOD Detection in Medicine

• 3 benchmarks with 14 different datasets
• 24 different OOD detection methods

Categories shown: ID, cs-ID, near-OOD, far-OOD (datasets: MIDOG, PhaKIR, OASIS-3, and others)

Gutbrod, M., Rauber, D., Nunes, D. W., & Palm, C. (2025). OpenMIBOOD: Open medical imaging benchmarks for out-of-distribution detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2025) (pp. 25874–25886).

## Slide 22

ReMIC – Trustworthiness
Benchmarks for OOD Detection in Medicine

• 3 benchmarks with 14 different datasets
• 24 different OOD detection methods

Gutbrod, M., Rauber, D., Nunes, D. W., & Palm, C. (2025). OpenMIBOOD: Open medical imaging benchmarks for out-of-distribution detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2025) (pp. 25874–25886).

## Slide 23

ReMIC – Trustworthiness
Benchmarks for OOD Detection in Medicine

• 3 benchmarks with 14 different datasets
• 24 different OOD detection methods

Gutbrod, M., Rauber, D., Nunes, D. W., & Palm, C. (2025). OpenMIBOOD: Open medical imaging benchmarks for out-of-distribution detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2025) (pp. 25874–25886).

## Slide 24

AI in Medicine
AKTORmed Robotic Surgery

## Slide 25

AKTORmed Robotic Surgery
Endoscope Guidance

## Slide 26

AKTORmed / ReMIC

Endoscopy · Oncology · Surgery
DeepMIC

## Slide 27

DeepMIC
Surgical Setting

© William F. Hefley

## Slide 28

DeepMIC
Surgical Setting

© AKTORmed Robotic Surgery

## Slide 29

AKTORmed Robotic Surgery
Endoscope Guidance

• Robotic endoscope control during MIS
• Current version: SOLOASSIST II
• Joystick for camera movement
• Adjustment through voice control

+ No need for human assistant
− Additional workload for surgeon
→ SOLOASSIST III

## Slide 30

DeepMIC
Cooperation

• Target: Almost autonomous endoscope adjustment
• Application of machine learning for:
  - Purely visual surgical instrument recognition
  - Instrument tracking over time

Funded by: Bayerische Forschungsstiftung
Cooperation: AKTORmed, TU Munich, OTH Regensburg (ReMIC, Ostbayerische Technische Hochschule Regensburg), MITI Research Group

## Slide 31

DeepMIC
Prototype

## Slide 32

DeepMIC
Animal Trial – 18th Feb. 2025, Hospital rechts der Isar

• Good handling of overlaps
• Clear separation of the instruments
• However: frequent switching of instrument classes
• Conclusion: BFS satisfied; project was successfully completed.

## Slide 33

PhaKIR-Challenge
Organization, Evaluation, and Publication

PhaKIR - Challenge: Phase, Keypoint and Instrument Recognition, part of MICCAI 2024 Marrakech

Descriptor: Video Dataset for Surgical Phase, Keypoint, and Instrument Recognition in Laparoscopic Surgery (PhaKIR)
Authors: Tobias Rueckert, Raphaela Maerkl, David Rauber, Leonard Klausmann, Suemeyye R. Yildiran, Max Gutbrod, Danilo Weber Nunes, Alvaro Fernandez Moreno, Imanol Luengo, Danail Stoyanov, Nicolas Toussaint, Enki Cho, Hyeon Bae Kim, Oh Sung Choo, Ka Young Kim, Seong Tae Kim, Gonçalo Arantes, Kehan Song, Jianjun Zhu, Junchen Xiong, Tingyi Lin, Shunsuke Kikuchi, Hiroki Matsuzaki, Atsushi Kouno, João Renato Ribeiro Manesco, João Paulo Papa, Tae-Min Choi, Tae Kyeong Jeong, Juyoun Park, Ohwatosin Alabi, Meng Wei, Tom Vercauteren, Runzhi Wu, Mengya Xu, An Wang, Long Bai, Hongliang Ren, Amine Yamlahi, Jakob Hennighausen, Lena Maier-Hein, Kousuke Hirasawa, Shu Yang, Yihui Wang, Hao Chen, Santiago Rodriguez, Nicolás Aparicio, Leonardo Manrique, Juan Camilo Lyons, Olivia Hosie, Nicolás Ayobi, Pablo Arbeláez, Yiping Li, Yasmina Al Khalil, Sahar Nasirihaghighi, Stefanie Speidel, Daniel Rueckert, Hubertus Feussner, Dirk Wilhelm, and Christoph Palm

Abstract: Reliable recognition and localization of surgical instruments in endoscopic video recordings are foundational for a wide range of applications in computer- and robot-assisted minimally invasive surgery (RAMIS)... This paper presents a blueprint for DIY biomedical imaging challenges, designed to provide institutions with greater autonomy over their challenge infrastructure.

## Slide 34

PhaKIR-Challenge

• 3 Tasks:
  - Surgical Procedure Phase Recognition
  - Surgical Instrument Keypoint Estimation
  - Surgical Instrument Instance Segmentation
• Entirely self-hosted
• €3.000 prize money from AKTORmed
• https://phakir.re-mic.de/

Chart: EndoVis-2024 sub-challenges — Registrations vs Submissions
HiSWA-RLLS: 13/6, SegCol: 24/3, FedSurg: 24/4, OSS: 25/4, STIR: 36/5, SegSTRONG-C: 40/10, SurgVU: 60/8, PhaKIR: 66/18

## Slide 35

PhaKIR-Challenge

Table across Hospital 1, Hospital 2, Hospital 3 showing:
- Input frames
- Surgical phase recognition (e.g. Preparation, Gallbladder Dissection, Gallbladder Packaging) with phase labels: P, CTD, ClCu, GD, GP, ClCo, GR
- Instrument instance segmentation
- Instrument keypoint estimation

## Slide 36

PhaKIR-Challenge
Dataset and Annotations

• Training: 8 videos
• Test: 5 videos
• ≈ 33,800 annotated frames
• Segmentation masks and phase annotations from MITI
• Semi-automatic generation and refinement of keypoints from ReMIC

## Slide 37

Datensatz und Annotationen
MICCAI Challenge

*(surgical video still, no additional extractable text)*

## Slide 38

PhaKIR-Challenge
Presentation

• Very positive feedback
• Interesting insights
• Identification of a research gap
  - Robust keypoint / pose tracking of surgical instruments
  - Incorporation of temporal information

## Slide 39

PhaKIR-Challenge
Medical Image Analysis, Full Paper, 2026

Comparative validation of surgical phase recognition, instrument keypoint estimation, and instrument instance segmentation in endoscopy: Results of the PhaKIR 2024 challenge.
Published in Medical Image Analysis (Elsevier). Received July 2025, accepted July 2025.

Includes KDE plot of bootstrap results for instrument instance segmentation task (95% HD values) across participating teams: jmees.inc., uniandes24, augi, kist_harilab, floor9, sk, goncalo, hanglok, recogna.
Challenge data table showing sample inputs, ground truth, and participant predictions across teams for Samples 5–8.

## Slide 40

AI in Medicine
Autonomous Robotic Surgery

"grabbing gallbladder" — 7X speed
"Here, we show our system autonomously performing"

John Hopkins University
Robot performs first realistic surgery without human help
https://hub.jhu.edu/2025/07/09/robot-performs-first-realistic-surgery-without-human-help/

## Slide 41

AI in Medicine
Autonomous Robotic Surgery
Our setup

Da Vinci Research Kit (dVRK) Si
Porcine Gallbladder on Liver (Gallbladder Neck, Cystic Duct, Cystic Artery)
Surgical Configuration (Stereo Endoscope, Wrist Cameras, Clip Applier, Scissors, Cadiere Forceps)

to perform ex vivo cholecystectomy

John Hopkins University
Robot performs first realistic surgery without human help
https://hub.jhu.edu/2025/07/09/robot-performs-first-realistic-surgery-without-human-help/

## Slide 42

AI in Medicine
Surgical Instrument Recognition

• Robotic surgery & automation
• Surgical safety & error prevention
• Augmented Reality Guidance
• Skill Assessment
• Research on Surgical Technique & Outcomes
• Documentation & Automatic Report Generation

[1] https://hub.jhu.edu/2025/07/09/robot-performs-first-realistic-surgery-without-human-help/
[2] AKTORmed Robotic Surgery

## Slide 43

AI in Medicine
Development

Graph of annual publication volume of artificial intelligence in healthcare (1995–2023):
1995: 15, 1997: 18, 1999: 19, 2001: 24, 2003: 36, 2005: 45, 2007: 61, 2009: 87, 2011: 156, 2013: 213, 2015: 322, 2017: 739, 2019: 1480, 2020: 2677, 2021: 4029, 2022: 5320, 2023: 6450

Xie, Y., Zhai, Y., & Lu, G. (2025). Evolution of artificial intelligence in healthcare: a 30-year bibliometric study. Frontiers in medicine, 11, 1505692.

## Slide 44

AI in Medicine
Data Modalities

Distribution of data modalities: Texts 34.6%, Radiology 30.1%, Pathology 12.0%, Omics 12.4%, Other non-image 6.2%, Clinical images 4.7% (with sub-breakdowns: Structured/Unstructured, MRI, CT, X-Ray, Nuclear, US, Fundus, OCT, Dermatoscopy, Signal, Others)

Count of individual data modality use by year (2018–2024), broken down by Radiology, Pathology, Clinical images, Texts, Omics, Other non-images — showing steady growth each year.

Schouten, D., Nicoletti, G., Dille, B., Chia, C., Vendittelli, P., Schuurmans, M., Litjens, G., & Khalili, N. (2025). Navigating the landscape of multimodal AI in medicine: A scoping review on technical challenges and clinical applications. Medical image analysis, 105, 103621.

## Slide 45

AI in Medicine
Medical Data Availability

• General datasets: ImageNet (14 million annotated images)
• Medical datasets table comparing: Endovis2015, Endovis2017, Endovis2018, CholecSeg8k, AutoLaparo (Multitask), ROBUSTMIS2019, SAR-RARP50 (Multitask), CholecInstanceSeg (Ours) — by patient type, environment, procedures, annotations, semantic classes, and instance-level labeling

• 1 million laparoscopic cholecystectomies per year in the US, approx. 630 hours of footage
• Common datasets (e.g. cholec80) ~50 hours

Reason? Expensive Expertise

[1] Alabi, O., Toe, K. K. Z., Zhou, Z., Budd, C., Raison, N., Shi, M., & Vercauteren, T. (2025). CholecInstanceSeg: A tool instance segmentation dataset for laparoscopic surgery. Scientific Data, 12, 825.

## Slide 46

Contact
www.re-mic.de

OTH REGENSBURG CONTACT
Tobias Rueckert, M. Sc.
Regensburg Medical Image Computing (ReMIC)
Ostbayerische Technische Hochschule Regensburg (OTH Regensburg)
Technical University of Munich (TU Munich)
AKTORmed Robotic Surgery

+49 941 943 1314
Galgenbergstraße 32, 93053 Regensburg
tobias.rueckert@oth-regensburg.de
