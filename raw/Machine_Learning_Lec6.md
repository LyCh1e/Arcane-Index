# International Summer School: Trustworthy AI – Machine Learning Meets Blockchain

**Microcredential 2: Machine Learning**
**Part 6: Transfer Learning and Domain Adaptation**

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

*International Summer School 2026 | Machine Learning*

---

## Slide 2: Where we are going

*Four questions, in order*

1. **Why transfer at all?** — Labels are expensive, medical datasets are small, and a network trained from scratch on 500 images will memorise them.
2. **How do we transfer?** — Feature extraction, partial fine-tuning, full fine-tuning — one recipe with three settings, plus the craft that makes it work.
3. **Three architectures, one recipe** — ResNet, U-Net and Vision Transformer are not three methods. They are three places to put the same cut.
4. **What if the data moves?** — A new clinic, a new camera, a new protocol — and your numbers fall apart. That is domain adaptation.

---

## Slide 3: How to read these figures

*Colour carries meaning throughout — there is no need to memorise it, but it will help*

| Colour | Meaning | Detail |
|---|---|---|
| Blue | pre-trained weights | the source domain |
| Orange | newly initialised | the task-specific part |
| Green | the target domain | where the model has to work |
| Purple | adaptation machinery | alignment, adversarial, PEFT |
| Red | a pitfall | something that quietly breaks |
| Grey | frozen | no gradients flow here |

- **solid** — these weights are being trained
- **hatched** — these weights are frozen

> Whenever you see a block diagram in this session, ask two questions: which colour is it, and is it solid or hatched?

Retinal fundus photograph used throughout: M. Häggström, WikiJournal of Medicine (CC0), as distributed with scikit-image. Histology, microscopy and phantom images likewise from scikit-image's sample data.

---

## Slide 4: Imagenet pre-training

*Large-scale pre-training dataset*

- Large-scale benchmark dataset for visual object recognition
- Over 14 million annotated images across over 20,000 categories
- Organized using the WordNet semantic hierarchy
- Enabled major advances in deep convolutional neural networks
- Established the ImageNet Challenge as a key computer-vision benchmark

---

## Slide 5: Part 1 — Why transfer at all?

*The case for not starting from random numbers.*

- What annotation actually costs in a clinical setting
- What happens when you train from scratch on a small dataset
- What the early layers of a trained network already contain
- The vocabulary: domain, task, source, target

---

## Slide 6: Labels are the bottleneck

*Raw medical images accumulate by themselves. Annotations do not.*

*(Figure: one fundus photograph shown with four annotation styles and their cost — Image-level label ("referable DR: yes"), seconds of expert time; Bounding boxes (one box per structure), about half a minute of expert time; Pixel mask (every vessel pixel traced), tens of minutes of expert time; Landmarks (vessel bifurcations marked), several minutes of expert time.)*

> A hospital PACS holds millions of images and almost no labels.

---

## Slide 7: Starting from random numbers

*Same architecture, same task, same hyperparameters — only the starting point differs*

*(Figure: two training-curve plots. Left — "small target set · 500 labelled images": fine-tuned (validation/training) reaches high accuracy quickly and plateaus; from-scratch (validation/training) shows a large gap between train and validation curves, labelled "overfitting". Right — "large target set · 50,000 labelled images": fine-tuned and from-scratch curves converge closely by epoch 50, labelled "small gap".)*

> Pre-training does not add information about your task. It removes the need to spend your labels learning what an edge is.

---

## Slide 8: What the layers already know

*Generic near the input, task-specific near the output*

*(Figure: a horizontal progression — "first conv layer" (oriented edges, colour blobs, shown as Gabor-like filter patches) → "early/middle blocks" (textures and motifs, shown as abstract activation maps) → "late blocks" (anatomy: disc, macula, crossings, shown on fundus photo crops) → "task head" (the decision, a bar chart of class probabilities: no DR 0.06, mild 0.11, moderate 0.66 [highlighted], severe 0.17). A gradient bar underneath reads "generic · transfers well" → "task-specific · must be relearned".)*

> Transfer works because the left half of this spectrum is nearly universal.

---

## Slide 9: Every network splits in two

*The same split, whatever the architecture*

- **Encoder** — Convolutions or transformer blocks. Turns pixels into features. Large, general, and already trained by somebody else.
- **Head** — A linear layer, a decoder, a detection head. Small, task-specific, always new — your classes are not their classes.
- **The cut** — Where you place it, and whether the layers before it may move, is the whole design space.

---

## Slide 10: Domain, and task

*Most confusion about transfer learning is confusion between these two*

- **Domain** — where the data comes from. The distribution the images are drawn from. Camera, scanner, light source, acquisition protocol, patient population, hospital.
- **Task** — what you want out. The label space and the mapping to it. Diseased or healthy; seven surgical phases; a segmentation mask; four keypoints per instrument.

| What moves | Example | What it is called |
|---|---|---|
| Domain changes | A model trained in Regensburg is deployed in Munich, on a different endoscope | domain adaptation |
| Task changes | An ImageNet classifier becomes a diabetic retinopathy grader | transfer learning, narrow sense |
| Both change | ImageNet photographs → laparoscopic video, classification → instrument keypoints | the usual situation in practice |

> Ask which of the two has moved before you ask what to do about it. The answer determines the method.

---

## Slide 11: Four situations, four names

*Whether the domain moved, the task moved, or both*

*(Figure: a 2×2 grid — rows: same task / different task; columns: same domain / different domain.*
- **same task, same domain:** "Nothing to transfer" — just train on your data — the ordinary case
- **same task, different domain:** "Domain adaptation" (Part 4) — the same grading task on images from another clinic and camera
- **different task, same domain:** "Task transfer" — the same images, moving from grading to lesion segmentation
- **different task, different domain:** "Transfer learning" (Part 2-3) — ImageNet photographs → retinal screening)

> Most real projects sit in the bottom-right cell — and are attacked with tools from all four.

---

## Slide 12: Part 2 — The paradigms

*One recipe, three settings, and the craft that decides whether it works.*

- Pre-train, transfer, adapt — the shape of every pipeline
- Feature extraction, partial and full fine-tuning
- Choosing between them from data size and domain distance
- Learning rates, schedules, and the things that quietly break

---

## Slide 13: The recipe, in three moves

*Almost every practical pipeline is an instance of this*

*(Figure: three-stage pipeline — "1 pre-train": source data (millions of cheap labels) → encoder blocks → head 1; "2 transfer": copy the encoder → target data (few expensive labels) → same encoder blocks → throw away head 1; "3 adapt": → new head → "a model for your task, trained on a fraction of the data it would otherwise need".)*

> Pre-train → transfer → adapt. The first step is usually somebody else's download.

---

## Slide 14: Three strategies, one dial

*How much of the encoder do you let move?*

*(Figure: a table of blocks (Block 1–5 + head) showing which are pre-trained/updated (solid), pre-trained/frozen (hatched), or newly initialised (orange), across three strategies:*
- **Feature extraction:** all blocks frozen (hatched), only head trained — weights that get gradients ≈ 0.1%, target data you need: smallest
- **Partial fine-tuning:** blocks 1-3 frozen, blocks 4-5 + head trained — ≈ 30%, target data: medium
- **Full fine-tuning:** all blocks + head trained — 100%, target data: largest)*

> One dial, from 0.1% of the parameters to 100%. Small data turns the dial down.

---

## Slide 15: The same three, in properties

*What you trade away when you turn the dial*

| Strategy | Trainable | Labels you want | Overfitting risk | The honest caveat |
|---|---|---|---|---|
| Feature extraction | ~0.1% | a few hundred | very low | cannot fix a bad representation |
| Partial fine-tuning | ~10–40% | a few thousand | moderate | the usual compromise; needs a choice of depth |
| Full fine-tuning | 100% | tens of thousands | high | best ceiling, and the easiest way to destroy what you loaded |

**A practical order of operations**
1. Start with feature extraction. It trains in minutes and gives you a baseline you can trust.
2. Then unfreeze the last stage with a much smaller learning rate and see whether it helps.
3. Only go to full fine-tuning if you have the data to support it — and always compare against the frozen baseline.

> A from-scratch baseline and a frozen-encoder baseline cost almost nothing and tell you whether transfer is doing any work at all.

---

## Slide 16: Choosing, without guessing

*Two axes decide almost everything: how much labelled data, and how far your domain is from the pre-training domain*

*(Figure: a 2×2 grid — rows: domain close to source / domain far from source; columns: few target labels / many target labels.*
- **close domain, few labels:** "Freeze almost everything" — linear probe on frozen features; unfreeze the last block only if it clearly helps. *500 fundus images, ImageNet-pretrained ResNet.*
- **close domain, many labels:** "Fine-tune everything, low LR" — one pass over all weights with layer-wise learning rates. *50,000 fundus images, the same kind of camera.*
- **far domain, few labels:** "Unfreeze the late half" — keep the early layers, augment heavily, and consider self-supervised pre-training on your own unlabelled data. *300 laparoscopic frames, ImageNet weights.*
- **far domain, many labels:** "Fine-tune all — but check scratch" — with this much target data a from-scratch baseline can win. *100,000 annotated CT slices.*)*

> Little data and a distant domain is the hard corner. Change your source of weights before you change your architecture.

---

## Slide 17: Where the weights come from

*Three sources, with quite different properties*

- **Supervised** — 1.3M photographs, 1,000 classes. Ships with every framework.
- **Self-supervised** — no labels at all — the image is the target. Hide 75% of the image, predict the rest. Masked reconstruction, or contrastive views.
- **Domain-specific** — already pre-trained on medical data. e.g. RadImageNet, retinal foundation models.

> You have unlabelled medical images. Self-supervised pre-training turns them into weights.

---

## Slide 18: Learning rates and schedules

*The single most common reason fine-tuning underperforms*

*(Figure: left — bar chart of "layer-wise (discriminative) learning rates", increasing from stem (lowest) through block 1-5 to head (highest): "early layers barely move — the head moves freely". Right — a "warm-up, then cosine decay" curve: relative learning rate rises sharply during "warm-up" (head only) then decays smoothly as the encoder unfreezes over subsequent epochs.)*

> One learning rate for the whole network throws away most of what you loaded.

---

## Slide 19: The normalisation trap

*No error message, no crash — just worse numbers*

*(Figure: left — histogram "what one channel produces" showing source domain (blue) and target domain (green) distributions with different means/spreads. Right — "after BatchNorm with the stored source statistics": source is re-centred to unit width, but target remains off-centre and too wide — "the shift survives".)*

> Freezing a BatchNorm layer freezes somebody else's statistics. Check what your framework does by default.

---

## Slide 20: Three more silent failures

*All three are silent failures: the code runs, the numbers are just worse*

1. **Input preprocessing** — Pre-trained weights expect the channel means and standard deviations they were trained with, in the channel order they were trained with. A grayscale medical image stacked into three channels is not RGB, and 16-bit CT windowing is a modelling choice, not a detail.
2. **Resolution** — A convolutional encoder tolerates a change of input size, because global pooling absorbs it. A transformer does not: its position embeddings are tied to one token grid, and they have to be interpolated.
3. **Class imbalance** — Pre-training says nothing about your prevalence. A 2% positive rate will happily produce a 98% accurate model that predicts nothing. Choose the metric before you train — see Part 01 on problem fingerprints.

> Before blaming the method, verify preprocessing, input size and class balance. In that order.

---

## Slide 21: Does ImageNet help in medicine?

*The answer is 'it depends', and what it depends on is how many labels you have*

*(Figure: bar chart comparing "from scratch" (grey) vs. "ImageNet pre-trained" (blue) AUC on the target task, at three label-set sizes: full training set (+1.0 points, 0.90 vs 0.90), 20% of the labels (+3.3 points, 0.85 vs 0.88), 5% of the labels (+7.6 points, 0.76 vs 0.83).)*

Schematic of the pattern reported by Raghu et al., NeurIPS 2019 — illustrative values, not reproduced measurements.

> Pre-training is a data-efficiency tool. With enough labels, its advantage shrinks — and you rarely have enough labels.

---

## Slide 22: Part 3 — Three architectures, one recipe

*ResNet, U-Net and Vision Transformer — the same cut in three different places.*

- Where the encoder ends and the head begins, in each case
- A concrete unfreezing schedule for a ResNet
- Why U-Net transfer only ever means the encoder
- Position embeddings, and parameter-efficient fine-tuning

---

## Slide 23: Where to cut, in general

*The head follows from the task, not from the architecture*

| Task | What the encoder must hand over | What the head looks like | Practical note |
|---|---|---|---|
| Classification | pooled feature vector | one linear layer, K outputs | the simplest case; often just a new fc |
| Segmentation | feature maps at several scales | a decoder plus a 1×1 convolution | the decoder is usually new and usually large |
| Detection | feature maps at several scales | a detection head with anchors or queries | the head has its own pre-training story |
| Keypoints / pose | high-resolution feature maps | a heatmap head, one channel per keypoint | resolution matters more than depth |

**The consequence**
Classification transfer is nearly free. Dense tasks — segmentation, detection, pose — always come with a substantial new, randomly initialised component, and that component needs its own learning rate and its own warm-up.

> The deeper the task, the more of your network is new — and the more careful the schedule has to be.

---

## Slide 24: ResNet: where the encoder ends

*Four stages, a pooling operation, and one linear layer that is always yours*

*(Figure: ResNet architecture flow — input (224²×3) → stem → layer 1 (112²×64) → layer 2 (56²×128) → layer 3 (28²×256) → layer 4 (14²×512) → global avg pool (7²×512) → fc (K classes) → K scores. "encoder — load the pre-trained weights" spans stem through global avg pool; "the only new layer" marks the fc layer.)*

> For classification, ResNet transfer is one line of code: replace fc, keep the rest.

---

## Slide 25: ResNet: a usable schedule

*Progressive unfreezing, from the head downwards*

*(Figure: four stages of progressive unfreezing shown as stacked bars (stem, layer 1-4, fc) across "stage 1 (epochs 1-3)" through "stage 4 (epochs 16-30)", with more layers becoming trainable (solid) as stages progress, while earlier layers remain frozen (hatched) or become trainable later. A companion plot shows learning rate decaying (log scale) across the four stages.)*

> Release from the top down, lower the rate as you go, and watch the normalisation layers.

---

## Slide 26: U-Net: anatomy

*An encoder, a decoder, and the skip connections that make it work*

*(Figure: the U-Net "U" shape — "contracting path · encoder" (left side, downsampling from input 256² through 128², 64² to a bottleneck) and "expanding path · decoder" (right side, upsampling back up to mask output), with dashed skip connections carrying fine detail across corresponding resolutions.)*

> Half of this network looks exactly like a classification encoder. That half is transferable.

---

## Slide 27: U-Net: the encoder transfers

*A pre-trained backbone on the left, a brand-new decoder on the right*

*(Figure: same U-Net shape as before, but now colour-coded — the left/encoder side labelled "a ResNet with ImageNet weights" (blue, pre-trained), the right/decoder side labelled "decoder: randomly initialised" (orange, new), ending in a 1×1 conv → K classes. Caption: "the skips now feed pre-trained features into a brand-new decoder".)*

> No checkpoint will ever give you a decoder. Budget learning rate and warm-up for it.

---

## Slide 28: The counterpoint: nnU-Net

*In 3D medical segmentation, a well-configured network trained from scratch is a very strong baseline*

**nnU-Net — Isensee et al., Nature Methods, 2021**
A plain U-Net with no pre-training, no attention, no architectural novelty — but with systematic, automatic configuration of preprocessing, patch size, spacing, normalisation, augmentation and post-processing. It won or matched the field across a large number of public segmentation challenges, and it remains a baseline that new methods are expected to beat.

**What this does not mean:**
- That transfer learning does not work
- That pre-trained encoders are useless in 2D
- That you should skip Part 2

**What it does mean:**
- 3D has no ImageNet, and 2D checkpoints transfer poorly to it
- Configuration effort often beats method novelty
- Without a from-scratch baseline you cannot claim a gain

> Run the from-scratch baseline. It is the only way to know what your pre-training is worth.

---

## Slide 29: ViT: anatomy

*Patches become tokens, tokens go through L identical blocks, and a single token carries the answer*

*(Figure: a fundus image split into a grid of patches (16×16 pixels each) → linear projection + learned position embedding → one token per patch, plus a CLS token → fed through ×L transformer blocks → MLP head reads the CLS token → K classes, or a dense head.)*

> Same recipe, same cut. The complications are the position embeddings and the appetite for data.

---

## Slide 30: ViT: the resolution problem

*Change the input size and the position embeddings no longer fit*

*(Figure: "pre-trained: 14×14" position-embedding grid (shown as a heatmap) → bicubic interpolation → "fine-tuning: 24×24" — a larger interpolated grid. Caption: "one grid of learned position vectors, resampled to the new grid" / "224 px input, patch 16" → "384 px input, patch 16".)*

> Interpolate the position embeddings. Every good library does it for you — check that yours did.

---

## Slide 31: ViT: fine-tune almost nothing

*Parameter-efficient fine-tuning — the encoder stays frozen, a small number of new parameters do the adapting*

*(Figure: three PEFT methods illustrated side by side —*
- **LoRA:** ΔW = B·A — a low-rank update, applied alongside frozen weights W, with rank r ≪ d
- **Adapters:** two tiny bottleneck layers per block (attention adapter, MLP adapter) — "the block itself never changes"
- **Prompt tuning:** learned prompt tokens prepended to the patch tokens — "prepend a handful of trainable vectors — the model is untouched")*

> With a large frozen backbone and a small clinical dataset, PEFT is often the right default, not the exotic option.

---

## Slide 32: The three, side by side

*The same four questions, four times*

| Architecture | What the checkpoint gives you | What is always new | Input size | What to do in practice |
|---|---|---|---|---|
| ResNet / CNN | stem + stages + pooling | the fc layer | tolerant — pooling absorbs it | progressive unfreezing; watch BatchNorm |
| U-Net | the contracting path only | the whole decoder + 1×1 conv | tolerant, within reason | the new decoder needs its own learning rate |
| Vision Transformer | patch embedding + all L blocks | whatever reads the tokens | needs position embeddings interpolated | LoRA or adapters if data is scarce |

> Three architectures, one procedure: find the encoder, replace the head, decide what moves, respect the schedule.

---

## Slide 33: Part 4 — When the data moves

*Domain adaptation: your task is unchanged, your images are not.*

- What domain shift looks like, and what it costs
- Four places in the pipeline where you can intervene
- Methods that need target labels, few labels, or none at all
- The evaluation split that hides the whole problem

---

## Slide 34: Domain shift, made visible

*The same eye, the same task, four acquisition settings*

*(Figure: a "source domain" fundus photo (Site A, reference camera) alongside three "target domain" photos of the same task — Site B (older desktop camera), Site C (handheld device), Site D (mobile screening, low resolution) — each with colour histograms of the retinal pixels (red/green/blue channels) shown beneath, visibly shifted between sites.)*

> Nothing clinical changed. Everything statistical did.

---

## Slide 35: Three kinds of shift

*They need different responses, so it is worth telling them apart*

- **Covariate shift** — the images look different, the rule stays the same. *(Illustration: overlapping source/target distribution curves labelled "same rule".)* Example: a different camera.
- **Label shift** — the same images, but the classes appear at different rates. *(Illustration: bar chart — screening 4% positive vs. referral clinic 35% positive.)* Example: screening vs. referral clinic.
- **Concept shift** — the same images, but they are labelled differently. *(Illustration: same fundus image with two different annotation outlines — "rater A — tight" vs. "rater B — generous".)* Example: a different annotation protocol.

> Feature alignment fixes covariate shift. It cannot fix a changed label definition.

---

## Slide 36: What it costs

*One model, trained on one site, evaluated on four*

*(Figure: bar chart — Dice on vessel segmentation. Trained on Site A only, evaluated: Site A held-out 0.884; Site B 0.792 (−9.2 points); Site C 0.741 (−14.3 points); Site D 0.663 (−22.1 points).)*

Illustrative values — the pattern, not measurements from a specific study.

> Your held-out test set from the same site is not evidence of generalisation. It is evidence of interpolation.

---

## Slide 37: How much target data?

*The setting is decided by the answer, before any method is chosen*

*(Figure: four columns showing decreasing target labels available, left to right:*
- **Supervised fine-tuning** — some labelled target images — "the easy case — just fine-tune"
- **Semi-supervised adaptation** — a few labels + much raw data — "labels anchor, raw data aligns"
- **Unsupervised adaptation** — raw target images only — "align distributions, or self-train"
- **Test-time / source-free** — target data only at inference — "adapt statistics on the fly")*

> Establish which column you are in first. It rules out most of the literature immediately.

---

## Slide 38: Four places to intervene

*Everything that follows is one of these four*

*(Figure: a pipeline — target image → block 1 → block 2 → block 3 → block 4 → features → head → prediction, with four numbered intervention points: 1 Input (harmonise the images, at the target image); 2 Features (align the distributions, at the features node); 3 Output (trust confident predictions, at the head); 4 Normalisation (recompute the statistics, spanning the blocks).)*

> Input, features, output, normalisation. Four levers, and you may pull more than one.

---

## Slide 39: Level 1 — input

*Colour and stain normalisation, computed here for real on both modalities*

*(Figure: two rows — "histology": scanner A tile, scanner B tile (different stain colour), and "B mapped onto A" (colour-normalised); "fundus": Site A image, Site C image (different colour cast), and "C mapped onto A" (colour-normalised).)*

> Cheap, interpretable, no labels, no retraining. Try this before anything clever.

---

## Slide 40: Level 2 — moment matching

*CORAL and MMD — align the distributions rather than the images*

*(Figure: two scatter plots of source (blue) and target (green) feature points in a 2-D feature space — "before" (two visibly separated clusters) and "after aligning mean and covariance" (clusters overlapping).)*

> Aligning statistics is not aligning classes. It usually helps, and it can quietly hurt.

---

## Slide 41: Level 2 — adversarial

*Adversarial adaptation, and the gradient reversal layer*

*(Figure: architecture diagram — source+target images → feature extractor → splits into two heads: label predictor → task loss (labelled source images only), and GRL (gradient reversal layer) → domain classifier → domain loss (source or target?). A dashed red arrow shows "the gradient comes back with a flipped sign (−λ)".)*

The domain classifier learns to separate source from target — the reversed gradient pushes the extractor to erase the difference.

> Elegant, widely used, and genuinely finicky. Budget time for the λ schedule.

---

## Slide 42: Level 3 — pseudo-labels

*Pseudo-labelling and self-training*

*(Figure: cycle diagram — 1 train on labelled source → 2 predict on raw target images → 3 keep only confident predictions → 4 add them and train again → repeat. Companion histogram: "confidence of the model on a target image", with a threshold line splitting "discard" (low confidence) from "keep as pseudo-label" (high confidence).)*

> Self-training works surprisingly well and fails silently. Watch the class balance of your pseudo-labels.

---

## Slide 43: Level 4 — normalisation

*AdaBN and test-time entropy minimisation*

*(Figure: left — "AdaBN — recompute μ and σ on the target images": three overlaid histograms (source/source statistics, target/source statistics, target/target statistics) showing the target distribution re-aligning once its own statistics are used. Right — "TENT — minimise the entropy of the prediction": bar chart of predicted probability per class (no DR, mild, moderate, severe) "before adapting" (spread out) vs. "after TENT" (sharply peaked on moderate), with entropy dropping from H=1.37 to H=0.91.)*

> If you do exactly one thing about domain shift, recompute the normalisation statistics on target data.

---

## Slide 44: The levers, per architecture

*The four levers, translated*

| Architecture | Input harmonisation | Where feature alignment attaches | Normalisation adaptation |
|---|---|---|---|
| ResNet / CNN | yes — and check the channel statistics | on the pooled or stage features | AdaBN, directly — the classic case |
| U-Net | yes — the most effective single lever | on the bottleneck, or per scale | BatchNorm or InstanceNorm per encoder stage |
| Vision Transformer | yes — plus patch-level augmentation | on the CLS token or on patch tokens | adapt LayerNorm parameters instead |

**A note on segmentation specifically**
Dense predictions are more fragile under shift than classification: a small change in contrast moves boundaries everywhere at once. Output-level methods therefore need structure-aware constraints — consistency under augmentation, or shape priors — rather than per-pixel confidence alone.

> The levers are the same. Only where you attach them changes.

---

## Slide 45: Domain generalisation

*Train so that the unseen clinic is not a special case*

*(Figure: "one image, many appearances" — several augmented variants of a fundus image (colour, illumination, blur, resolution, geometry changes) → one model (a stack of blocks that "never sees the deployment site") → "an unseen clinic": no target images at training time, no adaptation step at deployment, the model must simply be robust enough.)*

Augmentation as domain randomisation: colour, illumination, blur, resolution, geometry.

> Strong, physically meaningful augmentation is the most reliable domain-generalisation method we have.

---

## Slide 46: The trap that hides all this

*How you split your data decides whether you can see domain shift at all*

*(Figure: two split strategies compared on data from Site A, B, C —*
- **Random split by image:** images from all sites shuffled between train and test ("T"); test images come from the same cameras that produced the training images → **Dice 0.88**
- **Split by site (leave-one-site-out):** Site A and B entirely train, Site C entirely test ("T"); Site C is held out entirely — no image, no patient, no camera leaks into training → **Dice 0.71**)*

> Split by site and by patient. A lower number you can trust beats a higher number you cannot.

---

## Slide 47: Putting it together

*A decision path you can follow on a real project*

*(Figure: a flowchart — "a new medical imaging task" → "Do pre-trained weights exist for something close to your data?" → yes: "use them — closer beats bigger" (generic ImageNet works too, it is just further away) → "How many labelled target images do you have?" → few: freeze / many: fine-tune all (always run a from-scratch baseline for comparison) → "Will the deployment site differ from your training data?" → yes: "plan for adaptation now" (harmonise inputs, align features, self-train, or adapt at test time) → final note: "and evaluate by site, not by image — otherwise you will not see any of this".)*

> Weights first, strategy second, adaptation third — and the split decided before any of them.

---

## Slide 48: Our own case: PhaKIR

*Eight cholecystectomy videos from three clinics — a domain-shift problem by construction*

*(Figure: Clinic 1 (own endoscope, own light source), Clinic 2 (different camera, different team), Clinic 3 (different surgical technique) → all feed into "PhaKIR" (8 cholecystectomy videos, 18 instrument classes, phases/keypoints/masks) → "leave-one-clinic-out" evaluation: train on two clinics, test on the third; the drop you measure is the domain gap; an honest number to report.)*

> If your dataset spans several centres, you already own a domain-adaptation benchmark. Use it.

---

## Slide 49: Pitfalls, collected

*Every one of these produces a working pipeline and a worse model*

**Transfer learning**
- ✗ One learning rate for the pre-trained encoder and the new head
- ✗ No warm-up, so the random head damages the encoder in epoch one
- ✗ Frozen BatchNorm layers still carrying source statistics
- ✗ Input normalisation that does not match the checkpoint
- ✗ ViT position embeddings never interpolated to the new resolution
- ✗ No from-scratch baseline, so the gain is unmeasured

**Domain adaptation and evaluation**
- ✗ A random split, so domain shift is invisible in your numbers
- ✗ Several frames of one video, or one patient, in both splits
- ✗ Pseudo-labels accepted without checking their class balance
- ✗ Feature alignment used against a concept shift it cannot fix
- ✗ Adversarial adaptation reported from its single best run
- ✗ A single-centre test set described as external validation

> None of these throws an exception. All of them cost you performance you already paid for.

---

## Slide 50: Five things to take away

*If the rest fades, these are the ones worth keeping*

1. **Transfer buys data efficiency, not knowledge.** It removes the need to spend your scarce labels learning what an edge is. The less data you have, the more it is worth.
2. **Find the encoder, replace the head, decide what moves.** ResNet, U-Net, ViT — one procedure, three sets of housekeeping details. The details are where the performance is.
3. **Where the weights come from matters most.** Closer beats bigger. Self-supervised pre-training on your own unlabelled archive is often the largest single improvement available.
4. **A model that works in your hospital is not validated.** Domain shift is the default, not the exception. Four levers: input, features, output, normalisation — start with normalisation.
5. **Split by site and by patient, or you will not see any of this.** A lower number you can trust is worth more than a higher number you cannot. This is the cheapest decision on the list.

---

## Slide 51: Contact

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
