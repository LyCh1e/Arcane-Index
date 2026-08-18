# International Summer School: Trustworthy AI – Machine Learning Meets Blockchain

**Microcredential 2: Machine Learning**
**Part 3: Model Evaluation & Experimental Design**

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

*International Summer School 2026 | Machine Learning*

---

## Slide 2: Table of Contents

*Two questions, five sections*

**A. Can I trust this number?** — How the experiment is set up decides whether the number means anything at all.
**B. What does this number mean?** — Every metric answers one specific question. Most published numbers answer a different one.

1. **Designing the experiment** — splits · leakage · variance
2. **Choosing the metric** — categories · families
3. **Classification** — confusion matrix · ROC/PR · calibration
4. **Segmentation** — DSC · boundary · aggregation
5. **Detection & instances** — matching · AP · PQ

Everything is shown on medical images — because that is where the traps are easiest to see, and hardest to ignore.

---

## Slide 3: "Our model achieves 94.2 % accuracy."

*A sentence that contains almost no information*

> "Our model achieves 94.2 % accuracy on the test set."

- **On which data?** One hospital, one scanner, one operator — or several?
- **Split how?** Random images, or so that no patient appears twice?
- **How many cases?** 94.2 % of 1 000 is a result. Of 35 it is noise.
- **How rare is the finding?** At 6 % prevalence, "always healthy" already scores 94 %.
- **Accuracy of what?** Which errors does it count — and which does it hide?
- **How often measured?** One lucky seed, or the mean over several runs?

Six questions the sentence does not answer. All six are decided before training starts.

---

## Slide 4: Why this comes first

*Validation is not the paperwork at the end of a project*

**A metric is a proxy — never the goal**
Nobody wants a high Dice score. They want a tumour outlined well enough to plan radiotherapy. The metric stands in for that, and sometimes it stands in badly.

**Bad validation survives peer review**
Large multi-centre analyses of biomedical challenges found inappropriate metrics to be one of the core problems — in competitions published in prestigious journals.

**Metric choice steers a whole field**
If the community optimises the wrong number for five years, five years of methods work goes in the wrong direction. This is why Metrics Reloaded exists.

**How to read every figure that follows:** reference / ground truth · model prediction · desirable · pitfall

---

## Slide 5: Designing the experiment

*Can this experiment produce a number that transfers?*

**Section 1** covers:
- splits and the three sets
- data leakage — the most expensive mistake in medical ML
- variance, confidence intervals and controlled comparisons

---

## Slide 6: Three sets, three different jobs

*Confusing them is the quietest way to fool yourself*

*(Figure: a horizontal bar split into Training set 70% (blue), Validation set 15% (orange), Test set 15% (black). All labelled data — split ONCE, never re-shuffled.)*

| Set | Role |
|---|---|
| **Training set** | The model sees the images and the labels. *Touched: every epoch.* |
| **Validation set** | You compare architectures, learning rates, epochs here. *Touched: hundreds of times.* |
| **Test set** | Estimates performance on data nobody optimised for. *Touched: once, at the very end.* |

---

## Slide 7: Cross-validation

*One split → one number. Five splits show how that number moves*

- **Every sample is tested once** — Five rounds, five models, five scores. You report a mean with a spread, not one lucky value.
- **Keep the folds honest** — Stratify so each fold keeps the class ratio. Group by patient or video: frames of one patient never sit in two folds.
- **It is still not a test set** — Choices made after seeing CV results are training decisions. Keep one untouched split for the final number.

---

## Slide 8: The test set is a one-shot resource

*Every look at it spends a little of its value*

**Selecting on the test set is training on it.**
Try 20 configurations, keep the best test score, and you have fitted 20 parameters to the test set — you just did it by hand.

**The winner's curse.**
The best of 20 noisy numbers is biased upwards. The gap you report will shrink on the next dataset.

**Leaderboards make this systematic.**
Hundreds of teams, one public test set, thousands of submissions.

**The protocol that protects you:**
1. Split first — before you look at anything.
2. Develop against the validation set only.
3. Freeze the model, the threshold and the code.
4. Run the test set once. Report what came out.
5. Changed something afterwards? Say so.

> If the test set influenced any decision you made, it is no longer a test set — it is a second validation set.

---

## Slide 9: Data leakage — the expensive one

*Neighbouring video frames are not independent samples*

*(Figure: one endoscopic video, eight consecutive frames (frame 100–107), visually near-identical — "≈ the same image".)*

**Split A — randomly by frame** ✗: alternating train/test frames scattered across Video A, B, C — test frames sit between training frames.

**Split B — by video (grouped)** ✓: entire videos assigned wholly to train or test — the test video was never seen at all.

---

## Slide 10: What the leak actually costs you

*The optimistic number is the one that reaches the clinic*

*(Figure: bar chart "Same data, same model, two protocols" — Split A (random by frame) scores 0.96; Split B (grouped by video) scores 0.74.)*

**Which number would the clinic see?**
- **0.74** — the honest estimate for a new patient
- **0.96** — an estimate of how well the model memorises this video

> The 0.22 gap is not progress. It is leakage.

---

## Slide 11: Five ways data leaks

*All of them look like a well-performing model*

- **Same patient in both sets** — Two images of one eye, two slices of one scan, left and right knee.
- **Neighbouring frames** — Video at 25 fps: frame 100 and frame 101 are the same picture.
- **Preprocessing before the split** — Normalisation statistics, resampling or feature selection computed on all data.
- **Duplicates and re-uploads** — Public datasets overlap. The same case appears under two IDs.
- **Tuning on the test set** — Choosing the epoch, the threshold or the architecture by test score.

**The only question you have to answer:** "What is the unit that must never appear on both sides?"
- patient
- eye, knee, breast
- video or session
- whole-slide image
- hospital or scanner
- annotator

Then split by that unit — never by row.

---

## Slide 12: Cross-validation has the same problem

*k-fold must respect the group, or it inherits the leak*

*(Figure comparing two 3-fold splits of patients A–D (with letters = patient ID, orange = held out in this fold):*

**Random 3-fold** ✗ — same patient (A) appears across training and test of the same fold (e.g. fold 1 has patient A split between train and held-out).

**Grouped 3-fold (by patient)** ✓ — every patient lives in exactly one fold.

---

## Slide 13: Stratify, then beat the trivial model

*Two habits that cost nothing and save arguments*

**1 · Stratify — keep the class balance in every split**

| class | cases | in training | in test |
|---|---|---|---|
| healthy | 903 | 94.0% | 62.0% |
| disease | 57 | 6.0% | 38.0% |

An unstratified random split of a rare class produces test sets like this. The scores are then not comparable to anything.

Use `StratifiedGroupKFold`: stratify by label, group by patient.

**2 · Baselines you must beat**

| baseline | accuracy |
|---|---|
| Always predict "healthy" | 0.94 |
| Predict the training majority | 0.94 |
| Random guess, class prior | 0.89 |
| Logistic regression on 5 features | 0.95 |
| Your deep network | 0.96 |

A deep network that beats "always healthy" by two points has not yet earned the GPU hours.

> Report the trivial baseline next to your model. It is the only way a reader can see the size of the achievement.

---

## Slide 14: One number is not a result

*Retraining the same model gives a different answer*

*(Figure: scatter/error-bar plot "Five random seeds each — nothing else changed", comparing "Baseline" (0.841 ± 0.013) vs "Our method" (0.852 ± 0.012), each with 5 individual seed points scattered around the mean.)*

**The honest reading:**
- **+1.1 pt** — the difference between the two means
- **±1.3 pt** — the spread of one method across seeds
- A single run of each would have let you claim either method wins.
- **Report mean ± std over ≥ 3 seeds.**

---

## Slide 15: The 95 % confidence interval

*How far your number could move if you had drawn a different test set*

```
half-width ≈ 1.96 · √( p(1−p) / n )
```

**Four times the data, half the width**
Precision grows with √n, not with n. Below roughly a hundred test samples, almost nothing is distinguishable.

**Two separate uncertainties**
This interval covers the finite test set only. Re-training with new seeds adds a second spread — report both.

**Comparing two models**
Heavily overlapping intervals mean the difference you see is within sampling noise. Say that, instead of declaring a winner.

---

## Slide 16: How precise is that number?

*A test set is a sample — and small samples are vague*

*(Figure: "The same measured accuracy of 0.90 — 95% confidence interval by test-set size" — plot showing accuracy 0.90 with shrinking CI bands as n grows: n=20 → [0.70, 0.97] (±13.7pt); n=50 → [0.79, 0.96] (±8.5pt); n=100 → [0.83, 0.94] (±6.0pt); n=250 → [0.86, 0.93] (±3.7pt); n=1000 → [0.88, 0.92] (±1.9pt).)*

> On 50 test cases, "0.90 beats 0.86" is indistinguishable from noise.

---

## Slide 17: Change one thing at a time

*Otherwise you have a better model and no knowledge*

*(Figure: "What usually happens" — a chain of changes: Baseline (0.71) → + augmentation → + new backbone → + 3× epochs → 0.86, with "+0.15 — but which of the three changes earned it? The experiment cannot say." marked with a red "?".)*

**Controlled comparison** (bar chart, one change at a time from Baseline):
| variant | score | Δ |
|---|---|---|
| Baseline | 0.71 | — |
| Baseline + augmentation | 0.79 | +0.08 |
| Baseline + new backbone | 0.73 | +0.02 |
| Baseline + 3× epochs | 0.72 | +0.01 |

> One change at a time, everything else frozen — now "augmentation helped" is a claim you can defend.

---

## Slide 18: The test set that agrees with you

*An internal test set cannot measure generalisation*

*(Figure: "One model, trained on Site A only" — three retinal fundus photographs labelled Site A (training data), Site B (different camera), Site C (different protocol), with a bar chart of "test score per site": A = 0.91, B = 0.78, C = 0.61.)*

> The model did not get worse — the data got different. An internal test set cannot see this.

---

## Slide 19: Checklist — the honest experiment

*Eight lines that make a result defensible*

- **Split by the right unit.** Patient, video, session — never by row.
- **Split once, before anything else.** Including before computing normalisation statistics.
- **Stratify.** And print the class balance of every split.
- **Report the trivial baseline.** Majority class, and one simple classical model.
- **Several seeds.** Mean ± standard deviation, at least three runs.
- **Confidence intervals.** Wilson for proportions, bootstrap for everything else.
- **One change per comparison.** Everything else frozen, same seeds.
- **Say what you could not test.** Other sites, other scanners, other populations.

> None of this is about being pedantic. It is about being able to answer the question "how do you know?"

---

## Slide 20: Choosing the metric

*Trustworthy — but is it the number you wanted?*

**Section 2** covers:
- what a metric can and cannot represent
- the four problem categories — and picking the wrong one
- the families of metrics, and why you need more than one

---

## Slide 21: A metric is only ever a proxy

*Four translations between the clinic and the number*

*(Figure: flow diagram — "What the clinic actually cares about" ("Will this patient need treatment?") → "Problem category" (classification, detection, segmentation ...) → "Validation metric" (accuracy, DSC, AP, NSD ...) → "One number" (0.87).)*

> A metric is only a proxy. Every arrow is a modelling decision — and a place where the number stops meaning what you think.

---

## Slide 22: Three ways to get the metric wrong

*The taxonomy behind the Metrics Reloaded framework*

1. **Wrong problem category** — The metric is computed correctly and answers a question nobody asked. *Example: Scoring "find every lesion" with Dice — see section 5.*
2. **Wrong metric inside the category** — The right family, but a member of it that this problem breaks. *Example: Dice on 4-pixel structures; accuracy at 1% prevalence.*
3. **Wrong application of a good metric** — Correct metric, correct problem, and then averaged the wrong way. *Example: Pooling images across patients; undefined empty cases.*

> All three produce a plausible number, a clean table and a paper. Only the third one is usually caught in review.

---

## Slide 23: One image, four different questions

*The category follows the clinical need, not the model*

*(Figure: one retinal fundus photograph shown four times with different annotation styles:*
- **Image-level classification** — a single label overlay: "referable: 0.87, no findings: 0.13" — *one label for the whole image*
- **Object detection** — bounding boxes around lesions — *position of every object*
- **Semantic segmentation** — blood vessels traced in blue, lesions highlighted — *one label for every pixel*
- **Instance segmentation** — individual lesions circled with distinct colours (orange, purple, green, blue) — *pixels + object identity*)

> Pick the wrong category and every metric that follows is wrong, however carefully you compute it.

---

## Slide 24: Which category is your problem?

*Three questions, and the metric families follow*

*(Decision-tree figure:*
- Do you need a label for the whole image? → **yes** → Image-level classification
- → **no**, I need specific regions → Do you need the exact outline of each region? → **no**, a box or a point is enough → Object detection
- → **yes** → Must two touching objects be told apart? → **no** → Semantic segmentation; → **yes** → Instance segmentation)

> Three questions decide the category — and the category decides the metrics.

---

## Slide 25: Six families of metrics

*Pick one from each relevant family — not five from one*

| Family | Members | Applies to |
|---|---|---|
| **Counting** | sensitivity · precision · F₁ · MCC · balanced acc. — one fixed threshold | ImLC ObD InS |
| **Multi-threshold** | AUROC · average precision · FROC score — the whole trade-off | ImLC ObD InS |
| **Overlap** | DSC · IoU · clDice — how much agrees | SemS InS |
| **Boundary** | HD · ASSD · MASD · NSD — where it disagrees | SemS InS |
| **Calibration** | ECE · Brier score · negative log-likelihood — is the confidence honest | ImLC |
| **Application-specific** | volume error · connectivity · latency — your actual question | any |

*(ImLC = Image-Level Classification, ObD = Object Detection, InS = Instance Segmentation, SemS = Semantic Segmentation)*

> Metrics Reloaded recommends metrics from different families — plus, when nothing fits, one you define yourself.

---

## Slide 26: Classification

*One label per image — the family everything is built on*

**Section 3** covers:
- the confusion matrix and everything derived from it
- class imbalance: why accuracy stops working
- ROC versus precision–recall, thresholds, calibration

---

## Slide 27: Everything starts with four numbers

*TP, FP, TN, FN — and roughly twenty metrics built on them*

*(Figure: confusion matrix for "1000 screening images, 100 of them referable" — prediction negative/positive vs reference positive/negative: FN=20, TP=80, TN=810, FP=90.)*

| metric | value | formula |
|---|---|---|
| Accuracy | 0.89 | (TP+TN) / all |
| Sensitivity (recall) | 0.80 | TP / all positives |
| Specificity | 0.90 | TN / all negatives |
| Precision (PPV) | 0.47 | TP / all flagged |
| F₁ score | 0.59 | harmonic mean of the two above |
| Balanced accuracy | 0.85 | mean of sens. and spec. |
| Matthews corr. coeff. | 0.56 | uses all four cells |

> Same four numbers, seven very different verdicts. Accuracy says 0.89; of every 100 images you flag, 53 are healthy.

---

## Slide 28: 99 % accuracy, zero patients found

*At low prevalence, accuracy measures the prevalence*

*(Figure: "The 'model' that always answers 'no findings'" — confusion matrix with FN=10, TP=0, TN=990, FP=0, giving 99.0% accuracy in a large red box.)*

| metric | value |
|---|---|
| Sensitivity | 0.00 |
| Specificity | 1.00 |
| F₁ score | 0.00 |
| Balanced accuracy | 0.50 |
| Matthews corr. coeff. | 0.00 |

> With 1% prevalence, accuracy is a measure of the prevalence — not of the model. Ask for sensitivity, precision and MCC.

---

## Slide 29: Which error hurts more?

*The question that picks the metric — and the threshold*

**Screening** — find everything, accept extra work
- A missed cancer is the failure that matters.
- A false alarm costs one follow-up examination.
- Optimise sensitivity at an acceptable false-positive rate.
- Report: sensitivity @ fixed FP rate, FROC, recall-weighted F₂.

**Confirmation / autonomy** — act only when certain, accept misses
- A false positive triggers an intervention or moves a robot.
- A miss means a human stays in the loop — the status quo.
- Optimise precision at an acceptable sensitivity.
- Report: precision @ fixed sensitivity, PPV, F₀.₅.

> Both are correct engineering. What is never correct is reporting one number and leaving the trade-off unstated.

---

## Slide 30: The ROC curve

*Every point on the curve is one threshold*

- **The two axes** — TPR: of all true positives, how many we found. FPR: of all negatives, how many we falsely flagged.
- **Threshold-free by construction** — All thresholds at once, so two models can be compared before anyone commits to one.
- **A curve cannot be deployed** — The operating point is a separate decision, driven by what a miss costs against a false alarm.

---

## Slide 31: ROC or precision–recall?

*The same classifier, two class balances*

*(Figure: two pairs of curves for the same classifier at different prevalences.*
**ROC curve** — prevalence 50%: AUROC 0.82; prevalence 2%: AUROC 0.79. Caption: "hardly moves: 0.82 → 0.79".
**Precision–recall curve** — prevalence 50%: AP 0.82; prevalence 2%: AP 0.23. Caption: "collapses: 0.82 → 0.23".)

> Same classifier, same scores — only the class balance changed. On rare findings, report AP or the PR curve, not AUROC alone.

---

## Slide 32: One curve, but you deploy one point

*AUROC is an average over decisions you will never make*

- sensitivity equals the true positive rate
- 1 − specificity equals the false positive rate

---

## Slide 33: Classification — what to report

*A defensible minimum for the Friday presentations*

| report | when | why |
|---|---|---|
| The confusion matrix itself | always | four numbers, no interpretation needed |
| Sensitivity and specificity | always | properties of the model, not the cohort |
| Precision (PPV) | always | state the prevalence it belongs to |
| Balanced accuracy or MCC | if imbalanced | one honest single-number summary |
| AUROC | useful | prevalence-independent, threshold-free |
| Average precision / PR curve | if rare class | what AUROC hides at low prevalence |
| The operating point | always | and the set it was chosen on |
| Calibration (ECE or Brier) | if scores are used | needed the moment a human reads the probability |
| Plain accuracy alone | never | it is a function of the prevalence |

> Nine rows. Eight of them are one line of scikit-learn.

---

## Slide 34: Segmentation

*One label per pixel — where overlap metrics quietly fail*

**Section 4** covers:
- Dice and IoU: what they measure and what they ignore
- small structures, shape blindness, boundary metrics
- aggregation and the empty-reference case

---

## Slide 35: Dice and IoU

*The de-facto standard — and it is a counting metric*

*(Figure: two overlapping blob shapes — reference (green outline) and prediction (blue outline) — with intersection region shown, and legend: "reference ∩ prediction" 3085 px (green), "reference only (missed)" 1200 px (blue), "prediction only (spurious)" 674 px (orange).)*

```
DSC = 2|R∩P| / (|R|+|P|) = 0.77
IoU = |R∩P| / |R∪P| = 0.62
```

- DSC is exactly the F₁ score applied to pixels — TP, FP, FN.
- IoU = DSC / (2 − DSC): they always rank methods identically.

> Neither of them knows anything about shape.

---

## Slide 36: The small-structure trap

*The same one-pixel error, three very different scores*

*(Figure: three squares of increasing size (4×4, 10×10, 28×28 px) each with a one-pixel shift between reference (green) and prediction (blue) outline.)*

| structure size | DSC |
|---|---|
| 4 × 4 px | 0.75 |
| 10 × 10 px | 0.90 |
| 28 × 28 px | 0.96 |

*one-pixel shift, every time*

**Why it matters:** Small structures are exactly where human annotators disagree most — so a low DSC may be measuring the reference, not the model.

> The error is identical — one pixel. Overlap metrics punish small structures far harder.

---

## Slide 37: The same DSC, a different mistake

*Overlap metrics do not know what a shape is*

*(Figure: two blob shapes, A — outline slightly too small (uniformly eroded), B — half the structure missed (one side cut off), both with DSC = 0.864.)*

| | A | B |
|---|---|---|
| DSC | 0.864 | 0.864 |
| Hausdorff distance | 7.1 px | 26.0 px |
| NSD (τ = 3px) | 0.00 | 0.69 |

> The same DSC — to three decimals. Boundary metrics see the difference at once — and even disagree on which error is worse.

---

## Slide 38: Boundary metrics

*Three different definitions of "how far off is the edge"*

*(Figure: A — one spurious blob, far away (small orange circle outside the main shape); B — contour 2px too small everywhere (uniformly eroded outline).)*

| | A | B |
|---|---|---|
| DSC | 0.99 | 0.94 |
| Hausdorff distance | 40 px | 3 px |
| Avg. surface distance | 2.1 px | 2.3 px |
| NSD (τ = 3px) | 0.94 | 1.00 |

ASSD is nearly identical but hides two very different failures. HD sees the outlier; NSD forgives error inside the tolerance.

> Choose by the question: penalise the worst outlier (HD), the typical error (ASSD), or accept annotation noise (NSD).

---

## Slide 39: When no metric asks your question

*Vessels, airways, nerves: topology is the information*

*(Figure: reference vessel tree vs. prediction with 120 tiny gaps, on a retinal fundus image.)*

| DSC | clDice | connected pieces |
|---|---|---|
| 0.97 | 0.95 | 8 → 79 |

Only 6% of the vessel pixels are gone, so every overlap-based metric still reports a good result. The tree, however, is no longer a tree — and that was the clinical information.

> When no standard metric asks your question, add one that does — Metrics Reloaded has an explicit step for exactly this.

---

## Slide 40: How you average changes the answer

*Hierarchical data: images inside patients inside sites*

*(Figure: "One hospital, five patients, 150 images" — bar chart of number of images per patient (Patient 1: 100 images, Patient 2: 12, Patient 3: 8, Patient 4: 10, Patient 5: 20) alongside their mean DSC (Patient 1: 0.90, Patient 2: 0.55, Patient 3: 0.50, Patient 4: 0.45, Patient 5: 0.80).)*

- **Average over all 150 images → 0.81** — Patient 1 contributes two thirds of every image in the average.
- **Average over the five patients → 0.64** — Every patient counts once — the clinically relevant unit.

> Identical predictions. A 17-point difference produced purely by the order of averaging.

---

## Slide 41: Nothing there: the empty reference

*0 / 0 — and three published answers*

30 of 100 test images contain no lesion at all — and the model correctly predicts nothing. For those images |R| = 0 and |P| = 0, so DSC = 0/0. Three conventions are in use:

| convention | value | rationale |
|---|---|---|
| count them as 1.0 | 0.86 | "a perfect prediction is a perfect score" |
| count them as 0.0 | 0.56 | "there was nothing to overlap with" |
| exclude them | 0.80 | "report on the images where the question exists" |

> Same model, same predictions, three published numbers. State your convention — or the comparison is meaningless.

---

## Slide 42: Segmentation — what to report

*One overlap metric, one boundary metric, stated conventions*

**Report:**
- **One overlap metric** — DSC or IoU — not both, they are equivalent.
- **One boundary metric** — NSD if a tolerance is defensible, otherwise ASSD or HD95.
- **Per-case values, not just the mean** — A box plot shows the failures that a mean hides.
- **Aggregation at the patient level** — Per case first, then across patients — and say so.

**State explicitly:**
- **The empty-reference convention** — Counted as 1, as 0, or excluded — pick one and write it down.
- **Any application-specific metric** — Volume error, connectivity, number of components.
- **Whether structures were size-stratified** — Small and large lesions are different problems.
- **Reference quality** — One annotator, or several? What was inter-rater agreement?

> If a reader cannot reproduce your aggregation from the text, your number cannot be compared to anyone else's.

---

## Slide 43: Detection & instances

*Counting objects — and one metric family that breaks*

**Section 5** covers:
- localisation criterion and assignment strategy
- the IoU threshold, average precision, FROC
- instance segmentation and panoptic quality

---

## Slide 44: Two decisions before any metric exists

*Which prediction counts as a hit, and who gets the hit*

**1 · Localisation criterion** — When does a prediction "hit" a reference? (box IoU ≥ 0.5 · mask IoU ≥ 0.5 · centre inside)

**2 · Assignment strategy** — Two predictions hit the same object — who wins? greedy by confidence score · greedy by overlap · optimal (Hungarian) matching · *the loser becomes a false positive*

> Neither decision is a detail: the same predictions can score 0.6 or 0.9 depending on how you make them.

Both must appear in your methods section. In practice almost no paper states them.
*(blue = reference · orange = prediction · the number is the confidence score)*

---

## Slide 45: Detection scored as segmentation

*Dice rewards the model that merged three lesions into one*

*(Figure: Prediction A — one merged blob covering all 3 reference lesions; Prediction B — three separate objects matching the 3 references.)*

| | A | B |
|---|---|---|
| DSC (pixel level) | 0.76 | 0.66 |
| F₁ (object level) | 0.50 | 1.00 |

A found 1 of 3 objects; B found 3 of 3 objects.

> DSC prefers the prediction that found one object out of three. It is the correct metric — for the wrong question. Overlap metrics are blind to how many objects there are. If the domain question is "find every lesion", the problem is object detection, not semantic segmentation.

---

## Slide 46: The IoU threshold decides the winner

*Same predictions, two thresholds, two different rankings*

*(Figure: Method A — finds all four lesions, boxes a bit off (IoU values shown per box, e.g. 0.67, 0.78, etc.); Method B — finds three, boxes accurate (higher IoU per box, e.g. 0.88, misses one).)*

| | A | B |
|---|---|---|
| F₁ at IoU ≥ 0.5 | 1.00 | 0.86 |
| F₁ at IoU ≥ 0.75 | 0.50 | 0.86 |

> The same two methods, the same predictions — and the winner swaps when the threshold moves. The threshold encodes how precisely you need to localise. Choose it from the clinical task, then keep it fixed. Reporting a single IoU threshold hides this. Report a curve, or state the threshold and why.

---

## Slide 47: Panoptic quality

*Detection and segmentation quality in one number*

*(Figure: 3 instances matched with IoU 0.85, 0.72, 0.91; 1 missed instance (FN); 1 spurious instance (FP).)*

```
PQ = 0.62
SQ (segmentation quality) = 0.83   — mean IoU of the matched instances
RQ (recognition quality)  = 0.75   — the object-level F₁ score
```

> PQ = SQ × RQ — one number that cannot hide a missed instance behind good pixels.

---

## Slide 48: Putting it together

*A framework, a checklist, and five rules for Friday*

**Section 6** covers:
- the Metrics Reloaded framework and its online tool
- the pitfall gallery — everything on one page
- what we expect on Friday

---

## Slide 49: Metrics Reloaded

*A consensus framework, an online tool and reference code*

**Metrics Reloaded — the three steps:**
1. **Problem fingerprint** — Which category? Are classes balanced? How big are the structures? Is the reference noisy? Are cases independent?
2. **Metric selection** — Follow the decision tree for your category and pick one relevant metric from each relevant family — not five similar ones.
3. **Metric application** — Aggregate at the right level, handle empty references, report confidence intervals and the full confusion matrix.

An interactive version of the whole decision tree: **metrics-reloaded.dkfz.de**
Reference implementations of every metric: github.com/Project-MONAI/MetricsReloaded

---

## Slide 50: The pitfall gallery

*Everything from this session, on one page*

| Pitfall | Fix |
|---|---|
| Random split on grouped data (frames, slices, both eyes) | → split by patient |
| Tuning on the test set (threshold, epoch, architecture) | → validation set only |
| One seed, one number (no spread) | → mean ± std over ≥ 3 runs |
| No baseline (0.94 may be the majority class) | → report the trivial model |
| Accuracy on imbalanced data (measures prevalence) | → balanced accuracy, MCC, PR curve |
| AUROC with a rare positive class (hides the false positives) | → average precision |
| A score treated as a probability (AUROC cannot see this) | → ECE, Brier, reliability diagram |
| Dice on tiny structures (one pixel costs 25 points) | → treat it as detection |
| Overlap metric alone (shape-blind) | → add a boundary metric (NSD, HD95, ASSD) |
| Pooling images across patients (the longest scan wins) | → aggregate per patient |
| Silent empty-reference handling (0/0) | → state the convention |
| Detection scored with Dice (rewards merged objects) | → object-level F₁, AP, FROC |
| Unstated IoU threshold (changes the ranking) | → state it, or report a curve |
| Accuracy or specificity in detection (no true negatives exist) | → FP per image |

---

## Slide 51: Your project — five rules for Friday

*These five are what the assessment actually looks for*

1. **State your split strategy in one sentence.** "Grouped by patient, stratified by label, 70/15/15, fixed seed." If you cannot write that sentence, fix the split first.
2. **Report a trivial baseline next to every result.** Majority class, and one classical model. It costs three lines and it is the only way we can see how much your model added.
3. **Three seeds, mean ± standard deviation.** If your improvement is smaller than your spread, the correct claim is "we could not detect a difference". That is a valid result.
4. **Pick metrics from the fingerprint, not from habit.** Say which problem category you are in, and one metric per relevant family. Justify each in half a sentence.
5. **Bring one slide titled "what we got wrong".** Mandatory, and assessed. An error you found and can explain is worth more than two extra accuracy points.

Metrics Reloaded online tool: metrics-reloaded.dkfz.de

---

## Slide 52: Take-home

*Five sentences worth more than the other fifty slides*

- **A number without a protocol is not a result.** How you split, how often you looked, how many seeds — before the metric matters at all.
- **Data leakage is the default, not the exception.** Medical data is grouped. If you did not choose the group, the split chose it for you.
- **Every metric answers exactly one question.** Start from the clinical question, derive the category, then the metric. Never the other way round.
- **One metric is never enough, five correlated ones are no better.** Pick one per family: counting, curve, overlap, boundary, calibration.
- **If no metric fits, define one and say why.** The framework has a step for that. Using it is not a weakness — it is the point.

Lab 0 now: build the same model twice — once with the wrong split, once with the right one.

---

## Slide 53: Appendix — a starting point per category

*Metrics Reloaded recommendations, condensed*

| problem category | counting metric | curve metric | complement with |
|---|---|---|---|
| Image-level classification | balanced accuracy or MCC | AUROC, or AP if the class is rare | ECE / Brier if scores are used |
| Semantic segmentation | DSC (clDice for tubular) | NSD, or ASSD / HD95 | volume error if volume matters |
| Object detection | F₁ or sensitivity @ fixed FP | average precision or FROC | localisation criterion + assignment |
| Instance segmentation | F₁ or panoptic quality | average precision | DSC + NSD per matched instance |

**In every category, additionally:**
- the confusion matrix or per-case values, not only the mean
- confidence intervals, and the number of cases they are based on
- the aggregation level and the empty-reference convention

---

## Slide 54: Appendix — sources and tools

*Everything in this session is traceable to these*

**Metrics Reloaded: recommendations for image analysis validation**
Maier-Hein, Reinke et al. · Nature Methods 21, 195–212 (2024)
The framework, the problem fingerprint and the decision trees.

**Understanding metric-related pitfalls in image analysis validation**
Reinke, Tizabi et al. · Nature Methods 21, 182–194 (2024)
The sister paper — the catalogue of pitfalls behind section 2.

**Why rankings of biomedical image analysis competitions should be interpreted with care**
Maier-Hein et al. · Nature Communications 9, 5217 (2018)
How much a ranking depends on choices nobody reports.

**Metrics Reloaded online tool**
metrics-reloaded.dkfz.de
Answer the fingerprint questions, get a metric set.

**Reference implementations (MONAI)**
github.com/Project-MONAI/MetricsReloaded
Every metric in the framework, in Python.

Fundus photograph: M. Häggström, WikiJournal of Medicine (CC0), via scikit-image. Lesions and all diagrams: own work.

---

## Slide 55: Contact

**www.re-mic.de**

**OTH REGENSBURG**
- Phone: +49 941 943 1314
- Address: Galgenbergstraße 32, 93053 Regensburg
- Email: tobias.rueckert@oth-regensburg.de

**Tobias Rueckert, M. Sc.**
- Regensburg Medical Image Computing (ReMIC)
- Regensburg Center for Artificial Intelligence (RCAI)
- Regensburg Center of Health Sciences and Technology (RCHST)
- Regensburg Center of Biomedical Engineering (RCBE)
