# International Summer School: Trustworthy AI – Machine Learning Meets Blockchain

**Microcredential 2: Machine Learning**
**Part 02a: Machine Learning Basics**

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

*International Summer School 2026 | Machine Learning*

---

## Slide 2: Where we are going

*four parts, in this order*

1. **What learning is** — Why a machine can solve problems nobody can write down as rules.
2. **The shape of a problem** — Data, features, tasks, and what "it works" is allowed to mean.
3. **The neuron** — The smallest building block, in full, with numbers.
4. **How it learns** — Loss, gradient descent, backpropagation, and the training loop.

The same four parts, drawn as the pipeline they describe:

```
Data (images, labels) → Features (numbers the model sees) → Model f(x; θ) → Loss (one number) → Optimizer (change θ)
```

---

## Slide 3: How to read the figures

*one colour code, used on every slide in this session*

- **Data and inputs** — what we are given: images, measurements, pixels (blue)
- **The correct answer** — ground truth, labels, targets (green)
- **Parameters** — the numbers the machine is allowed to change (orange)
- **The prediction** — what comes out of the model (purple)
- **Error** — loss, mistakes, and things that go wrong (red)
- **Scaffolding** — boxes and arrows with no meaning of their own (grey)

> ⚠️ Whenever a figure changes colour, something changed role. Orange is the one to watch: it is the only thing training touches.

Medical images in this session: retinal fundus photography, chest radiography, dermoscopy. Sources on the credits slide.

---

## Slide 4: What does it mean to learn?

*Part 1 of 4*

Before any architecture: what problem is machine learning actually solving?

- **The old way:** a human states the rule, the computer executes it
- **The blocker:** for most interesting problems nobody can state the rule
- **The inversion:** supply examples instead, and search for the rule
- **The vocabulary:** model, parameters, loss, optimizer

---

## Slide 5: How we normally write a program

*a human works out the rule, and the computer carries it out*

```
Rules (written by a human) ─┐
                             ├─► Computer (executes the rules, step by step) ─► Output (the answer)
Data (the input) ───────────┘
```

> ⚠️ This is the whole of classical programming: the intelligence sits in the rules, and a person put it there.

---

## Slide 6: Now write the rule for this

*the input your program receives is 784 integers*

One chest radiograph, 28 × 28 pixels → converted to the same window as integers 0–255 (a grid of 8×8 shown as example values: 90, 104, 137, 166, 179, 185, 189, 180 ... up to 128, 150, 173, 190, 199, 201, 201, 194).

**784 numbers.** Write an if-statement over these 784 values that says "pneumonia" or "normal". **Nobody can.**

> ⚠️ A radiologist answers this in a second and cannot tell you the rule. That is the gap machine learning fills.

---

## Slide 7: Turn the picture around

*hand over the answers, and let the machine search for the rule*

**Classical programming:**
```
Rules ─┐
       ├─► Computer (executes) ─► Output
Data ──┘
```
*the rules move from the input side to the output side*

**Machine learning:**
```
Data ───┐
        ├─► Computer (searches) ─► Rules
Answers ┘
```

> ⚠️ Machine learning is not a different kind of computing. It is the same computing with the inputs and outputs swapped.

---

## Slide 8: Train once, use many times

*two phases with very different costs — keep them apart*

**Training — once, offline**
```
data + answers → search for parameters
```
*expensive, done by us*

→ (trained parameters) →

**Use — many times, in the clinic**
```
new x → f(x) → ŷ
```
*cheap, done by everyone*

> ⚠️ Training and inference are separate. Confusing them is a common source of confusion.

---

## Slide 9: Machine Learning — Artificial Intelligence vs. Machine Learning

**Artificial Intelligence**
> "Artificial intelligence is the ability of a machine to imitate human abilities such as logical thinking, learning, planning, and creativity."
> — European Parliament (website)

**Machine Learning** (subset of AI)
Algorithms that learn experiences and patterns from data independently and improve iteratively over time.

---

## Slide 10: What is actually being learned

*a fixed recipe with a few million adjustable numbers inside*

```
input (x1, x2, x3, x4 — measurements or pixels)
   → f (a fixed recipe with adjustable numbers: dials θ1, θ2, θ3, θ4, θ5 — parameters, this is what learning changes)
   → ŷ (prediction)
```

> ⚠️ Training never changes the recipe. It only turns the dials. The recipe is our design decision; the dial settings are the machine's.

---

## Slide 11: Every method has the same four parts

*important parts for any paper's methods section*

1. **Data** — Examples of the problem — for supervised learning, an input and the answer we want.
2. **Model family** — The set of functions the machine may choose from — fixed by us, before training.
3. **Loss** — A single number saying how wrong one prediction was. Smaller is better.
4. **Optimizer** — The rule that nudges the parameters so that the loss gets smaller.

Swap any one of the four and you have a different method. The other three keep working.

```
Data (x and y) → Model f(x; θ) → Prediction ŷ → Loss L(ŷ, y) → Optimizer (new θ)
```

> ⚠️ For the rest of the week, whenever something is unclear, ask which of these four parts it belongs to.

---

## Slide 12: The shape of a learning problem

*Part 2 of 4*

What the data has to look like, and what counts as success.

- **Samples:** what one row of a dataset actually is
- **Features:** the numbers the model is allowed to see
- **Supervision:** how much the labels tell us
- **Tasks:** classification, regression, and pixels
- **Generalisation:** train, validate, test — and leakage

---

## Slide 13: One sample, one row

*a dataset is a table: features on the left, the answer on the right*

| age | sex | BMI  | HbA1c | years since diagnosis | smoker | referable retinopathy? |
|-----|-----|------|-------|------------------------|--------|--------------------------|
| 61  | f   | 28.4 | 7.9   | 12                     | no     | yes                      |
| 47  | m   | 31.2 | 9.1   | 6                      | yes    | yes                      |
| 73  | f   | 24.8 | 6.8   | 21                     | no     | no                       |
| 55  | m   | 27.0 | 8.4   | 9                      | no     | yes                      |

*one row = one patient*
features — the numbers the model is allowed to see | the label

> ⚠️ The model only ever sees the left half. Anything a clinician knows that is not in those columns is invisible to it.

---

## Slide 14: An image is already a list of numbers

*no conversion step is needed — a photograph is a grid of integers*

A patch of the fundus photograph → 16 × 16 pixels, drawn as squares → one grid of numbers per colour channel (R, G, B) → **768 numbers** (16 · 16 · 3)

> ⚠️ An image is a very wide row in that same table. A small 28 × 28 colour image is already 2 352 features.

---

## Slide 15: Features: what the model gets to see

*two measurements per skin lesion, and nothing else*

**A two-dimensional feature space**

Suppose that for every lesion we measure exactly two things: its diameter in millimetres, and how irregular its border is on a scale from 0 to 1.

- **Each point** is one lesion
- **Each axis** is one feature
- **The colour** is the label a dermatologist gave

*(Scatter plot: X-axis "lesion diameter [mm]" 2–14, Y-axis "border irregularity" 0.1–0.9. Green circles = benign cluster (lower-left, small/smooth). Red squares = malignant cluster (upper-right, large/ragged), with overlap band in the middle.)*

**Where the two clouds sit**

Small and smooth lesions gather in the lower left, large and ragged ones in the upper right — with a band in the middle where they mix.

---

## Slide 16: Learning means drawing the boundary

*the boundary is the program that came out of the data*

**The learned rule, drawn**

Training, on this picture, means choosing where the line goes. The data does the choosing; we only fixed that it should be a line.

- **Above the line** the model answers malignant
- **Below the line** it answers benign
- **On the line** it is exactly undecided

*(Same scatter plot as Slide 15, now with a purple diagonal decision boundary line separating "predict malignant" (top-left, red-shaded) from "predict benign" (bottom-right, green-shaded) regions.)*

**It is not perfect, and that is expected**

A few points sit on the wrong side. A boundary that got every training point right would be a warning sign, not an achievement — we come back to this in a moment.

---

## Slide 17: And then it can judge a new case

*the only thing we actually wanted from the start*

**Using the boundary**

A new lesion arrives with no label. We measure the same two features, place it on the same map, and read off which side of the line it fell on.

*(Same scatter plot with decision boundary; a new unlabeled point (star marker) appears in the upper-right area, landing on the malignant side, labeled "it lands on the malignant side.")*

**This is inference**

No training, no labels, no optimizer. One forward calculation and an answer.

**And this is where trust starts**

The point lands close to the boundary far more often than the training picture suggests. A model that reports how sure it is, is worth much more than one that does not.

---

## Slide 18: Why one measurement is not enough

*each feature on its own overlaps; together they separate*

*(Three panels: "only the diameter" — histogram of diameter values for benign (green) vs malignant (red), overlapping; "only the irregularity" — histogram of irregularity values, overlapping; "both together" — 2D scatter plot with a clean separating line.)*

- Only the diameter: **the two classes overlap**
- Only the irregularity: **the two classes overlap**
- Both together: **one line separates them**

> ⚠️ Adding a feature can turn an impossible problem into an easy one. This is the honest reason models look at hundreds of features rather than three.

---

## Slide 19: Who chooses the features?

*the one difference that separates classical statistics / ML from deep learning*

**Features designed by a human:**
```
hand-designed rules (you decide what to measure) → feature vector (a handful of numbers) → a classifier (learns only from those numbers) → label
```
*whatever this step throws away is gone for good*

**Features learned from the data:**
```
one model, trained end to end (the early parts learn what to measure, the later parts learn the decision) → label
```
*nothing between the image and the label is hand-designed*

> ⚠️ Classical pipelines learn the decision. Deep learning learns the measurements as well — which is why it needs far more data.

---

## Slide 20: Four ways to learn

*how much the data already tells us decides the whole approach*

- **Supervised** — every sample carries a label *(scatter plot: labeled green circles and red squares)*
- **Unsupervised** — no labels — find the structure *(scatter plot: unlabeled points grouped into two dashed clusters)*
- **Semi-supervised** — a few labels, a lot of raw data *(scatter plot: mostly unlabeled points, a few labeled green/red points)*
- **Reinforcement** — learns from consequences *(diagram: agent ⇄ environment, with "action" flowing down and "reward" flowing up)*

> ⚠️ Supervised learning is the easiest and the most expensive. Everything else exists because labels cost money.

---

## Slide 21: Regression or classification

*in supervised learning, the output is either a number or a category*

**Regression — the output is a number**
*(Scatter plot: "vessel calibre [arb. units]" vs "blood pressure [arb. units]", with a fitted line through the points.)*

**Classification — the output is a class**
*(Scatter plot: lesion diameter vs border irregularity, with the diagonal decision boundary from earlier, separating benign/green from malignant/red.)*

> ⚠️ The choice changes exactly two things: the shape of the last layer and the loss. Nothing else in the pipeline moves.

---

## Slide 22: The output shape is a choice

*one image, four different questions, four different answers*

Using a retinal fundus photograph as the example image throughout:

- **Classification** — one label for the whole image (e.g., "referable retinopathy: yes")
- **Detection** — a box and a label per object (e.g., bounding box around "optic disc")
- **Semantic segmentation** — one class label per pixel (e.g., green overlay tracing the blood vessels)
- **Keypoint estimation** — a list of named coordinates (e.g., purple dots and connecting lines marking anatomical landmarks)

> ⚠️ Same picture, same four ingredients. Only the shape of the output and the loss change from panel to panel.

---

## Slide 23: Labels are the expensive part

*the annotation format decides the budget of the whole project*

Annotation time per image (order of magnitude):

| Label type | Approx. time |
|---|---|
| Image label | 4 s |
| Bounding box | 20 s |
| Keypoints | 55 s |
| Pixel mask | 8 min |

**Reading the chart**
- **Order of magnitude only.** Real numbers depend on the modality and the annotator.
- **Pixel masks** are one to two orders of magnitude slower than an image-level label.
- **And they need an expert,** which is the part that cannot be outsourced.

**Two people will not agree**
Two clinicians outlining one lesion produce different masks — a ceiling on any score.

**The practical rule**
Pick the cheapest label format that still answers the clinical question.

---

## Slide 24: Training, validation, test

*three jobs — and one of them may only be done once*

```
Training (70%) | Validation (15%) | Test (15%)
```
*the split is made once, before anything is trained, and never revisited*

- **Training set** — The parameters are fitted on this. The model sees it thousands of times.
- **Validation set** — Used to choose between options: learning rate, when to stop, which architecture.
- **Test set** — Locked away. Opened once, at the end, to report a number you can defend.

> ⚠️ Every time you look at the test set and then change something, it quietly becomes a validation set.

---

## Slide 25: Three ways a fit can turn out

*too simple, about right, and too flexible*

*(Three plots, each showing scattered data points and a dashed grey "truth" curve.)*

- **Underfitting** — too simple — misses the trend (solid red line, roughly straight, ignoring the curve of the data)
- **Good fit** — captures the trend, ignores the noise (solid green curve closely tracking the true dashed curve)
- **Overfitting** — runs through every single point (solid red curve, wildly oscillating to hit every data point)

The dashed grey curve is the truth we are trying to recover — in a real problem we never get to see it.

> ⚠️ Overfitting is not a bug in the code. It is what happens when a flexible model is allowed to take the training data literally.

---

## Slide 26: The same story, seen in the curves

*under- and overfitting in training progress*

*(Plot: loss (y-axis, 0–2.00) vs training progress in epochs (x-axis, 0–60). Blue "training loss" curve falls steadily. Orange "validation loss" curve falls then rises after around epoch 30, marked "stop here" at its minimum. Background shaded into three regions: "underfitting" (left), "sweet spot" (middle), "overfitting" (right).)*

**Reading a training run**
- **Blue falls, always.** Training loss going down proves nothing on its own.
- **Orange is the honest one.** It is measured on data the parameters never saw.
- **The gap between them** is roughly how much the model has memorised.

**Early stopping**
Keep the parameters from the epoch where the orange curve was lowest — not the last one.

**In the lab**
If orange is flat while blue drops, stop and look at the data before touching the model.

---

## Slide 27: The split that quietly ruins results

*split by patient, never by image*

*four patients, three images each*

**Random split by image:**
```
train: P1 P1 P4 P4 P4 P3 P2 P3
test:  P2 P2 P3 P1
```
→ these test images come from patients the model has seen (test images outlined in red)

**Split by patient:**
```
train: P1 P1 P1 P2 P2 P2 P3 P3 P3
test:  P4 P4 P4
```
→ no patient appears on both sides

A red outline marks a test image whose patient also appears in the training set.

> ⚠️ If two images of the same patient land on opposite sides of the split, your test score measures memory, not generalisation.

---

## Slide 28: The artificial neuron

*Part 3 of 4*

One building block, small enough to write on a napkin.

- **The unit:** multiply, add, squash — three operations
- **With numbers:** the same neuron, worked through twice
- **Geometrically:** one neuron is one straight boundary
- **The limit:** and why one is never enough
- **The layer:** many neurons as a single matrix product

---

## Slide 29: Where the name comes from

*inspired by a nerve cell — not a model of one*

**A nerve cell, very roughly:** dendrites (signals in) → soma → axon → signal out

**The artificial neuron:** inputs (x1, x2, x3) with weights (w1, w2, w3) → Σ (add up, then squash) → a (output)

> ⚠️ The analogy is historical and stops here. Nothing that follows depends on biology being right.

---

## Slide 30: One neuron, three steps

*multiply by weights, add a bias, apply one non-linear function*

1. **Weighted sum:** w1x1 + w2x2 + w3x3
2. **Add the bias:** shifts the whole sum (+b → z)
3. **Squash it:** a non-linear function of one number (σ → output a)

```
a = σ( w1x1 + w2x2 + w3x3 + b )    — that is the whole neuron
```

> ⚠️ That is the entire unit. A network with a hundred million parameters is this operation, repeated.

---

## Slide 31: The same neuron with real numbers

*one fixed set of parameters, two different inputs*

**The parameters (these stay the same):**
```
w1 = +1.5
w2 = -2.0
w3 = +3.0
b  = -0.4
```

**Case A:** x = (0.8, 0.5, 0.2)
```
z = 1.5·0.8 − 2.0·0.5 + 3.0·0.2 − 0.4 = +0.4
ReLU(+0.4) = 0.4   → the neuron fires
```

**Case B:** x = (0.2, 0.9, 0.1)
```
z = 1.5·0.2 − 2.0·0.9 + 3.0·0.1 − 0.4 = −1.6
ReLU(−1.6) = 0.0   → the neuron stays silent
```

> ⚠️ Nothing here is beyond arithmetic. The weights decide which inputs matter, and ReLU decides whether the unit speaks at all.

---

## Slide 32: What one neuron can do

*it cuts the space in two, with a straight line*

*(Plot: a straight purple line dividing the plane. Above the line (z > 0): red squares. Below the line (z < 0): green circles. Arrow labeled "w" perpendicular to the line.)*

**The geometry of z = w·x + b**
- **The line** is the set of inputs where z = 0
- **The weights** point perpendicular to it and set its tilt
- **The bias** slides the line without rotating it

**This is the boundary from part 2**
The dermatology example was one neuron, drawn without saying so. Two weights and a bias were all it needed.

**And this is the ceiling**
One neuron can only ever produce a straight boundary. No choice of weights escapes that.

---

## Slide 33: The problem with straight lines

*some questions have no linear answer at all*

*(Plot: four points at corners of a unit square — (0,1) red square, (1,1) green circle, (0,0) green circle, (1,0) red square — with several dashed lines attempting and failing to separate them, titled "One neuron cannot do this".)*

**Four points, no line**
Four points. Circles belong together, squares belong together. Try to separate them with one straight line.

**Every line fails**
Not because we have not found the right one — because no straight line exists that puts both circles on one side and both squares on the other.

**Why this matters**
"The answer is yes when exactly one of the two findings is present" is a perfectly ordinary clinical rule (XOR). And it has this shape.

More neurons side by side will not help: combining straight lines linearly gives another straight line.

---

## Slide 34: Two units, and it becomes easy

*a hidden layer changes the coordinates before the decision*

**Two units, opposite sides** *(plot of the same 4 XOR points, now with two diagonal lines h1 > 0 and h2 > 0 regions marked)*

```
h1 = ReLU( x1 − x2 )    "is x1 the bigger one?"
h2 = ReLU( x2 − x1 )    "is x2 the bigger one?"
y  = h1 + h2            0, 1, 1, 0 — exactly XOR
```

**In the new coordinates: easy** *(plot in h1/h2 space, showing that (0,0) and (1,1) both map to the same point, now linearly separable by a purple line)*

> ⚠️ Depth is not about doing something exotic. It is about re-describing the input until a straight line is enough.

---

## Slide 35: Why we need the squash

*without a non-linear function, depth buys you nothing*

Three activation functions plotted:

- **Logistic σ(z)** — squashes into (0, 1)
- **Hyperbolic tangent** — squashes into (−1, 1)
- **ReLU max(0, z)** — keeps positives, zeroes the rest

**Without it**
Stack two linear layers and you get one linear layer. Ten of them, still one.

**With it**
Each layer can bend the space, so the next layer sees an easier problem.

**In practice**
ReLU, unless you have a reason. It is fast, and gradients pass through it cleanly.

> ⚠️ The non-linearity is not a detail of the neuron. It is the reason a deep network is more than a big multiplication.

---

## Slide 36: A layer is one matrix product

*many neurons at once, in a single line of code*

```
input (x1, x2, x3; 3 numbers)
  × weight matrix W (2 rows × 3 columns = 6 weights)
  + bias b (one per unit)
  → σ, element by element
  → output (h1, h2; 2 numbers)
```

```python
h = relu(W @ x + b)
# W: (2, 3)  b: (2,)  x: (3,)
```

**Why this matters for the hardware**
A matrix product is exactly what a GPU does thousands of times in parallel — the whole reason deep learning became practical.

> ⚠️ One layer = one matrix, one bias vector, one activation. A network is a handful of those in a row.

---

## Slide 37: How a network learns

*Part 4 of 4*

The search for good parameters, from scratch.

- **Forward:** from an image to a probability
- **Loss:** turning a mistake into one number
- **Descent:** walking downhill on the loss
- **Backpropagation:** where the gradients come from
- **The loop:** batches, steps, epochs — and what breaks

---

## Slide 38: Stack the layers, count the numbers

*a tiny network, and already 74 parameters*

```
input (6 numbers) → hidden layer (5 units) → hidden layer (4 units) → output (3 numbers)
```

- 6·5 + 5 = 35 weights + biases (input → hidden layer 1)
- 5·4 + 4 = 24 weights + biases (hidden layer 1 → hidden layer 2)
- 4·3 + 3 = 15 weights + biases (hidden layer 2 → output)

**Total: 74 parameters**

> ⚠️ Every arrow is one weight. The count grows as the product of adjacent layer sizes, which is why networks get large very quickly.

---

## Slide 39: The forward pass, end to end

*from a retinal image to five numbers*

```
one image → flattened
  → hidden layer 1 (512 units, ×W + b, then σ)
  → hidden layer 2 (128 units, ×W + b, then σ)
  → output layer (5 numbers, ×W + b)
  → logits
```

*every arrow is one matrix product and one non-linearity*

> ⚠️ No magic anywhere in the chain: multiply, add, squash, repeat. The last layer's outputs are called logits.

---

## Slide 40: From scores to probabilities

*softmax makes the five numbers comparable*

**What the last layer produces (logits):**
```
no DR: +0.3   mild: +1.1   moderate: −0.7   severe: +3.8   proliferative: +0.5
```

**softmax →**

**Positive, and adding up to 100%:**
```
no DR: 2.6%   mild: 5.9%   moderate: 1.0%   severe: 87.3%   proliferative: 3.2%
```

> ⚠️ Softmax gives numbers that behave like probabilities. Whether they are honest probabilities is a completely separate question.

---

## Slide 41: How wrong is wrong?

*the loss turns a prediction into a single number*

```
Loss = − Σ (i=1 to output size) yᵢ · log(ŷᵢ)
```

*(Plot: loss (−log p) vs. probability the model gave to the correct class, showing a steeply decreasing curve.)*

- **confident and wrong** → loss 3.65 (low probability given to correct class)
- **unsure** → loss 2.30
- **confident and right** → loss 0.14 (high probability given to correct class)

**Cross-entropy, in words**
- **Right and confident:** almost no loss
- **Unsure:** a moderate penalty
- **Wrong and confident:** the loss grows without bound

**Why the logarithm**
It punishes confident mistakes far harder than hesitant ones. A model that says 99% and is wrong should hurt more than one that says 51%.

**One number, on purpose**
The optimizer can only follow one quantity, so every trade-off you care about has to be squeezed into it.

---

## Slide 42: Different tasks, different losses

*same recipe, one interchangeable part*

- **Regression — squared error.** The output is a number. Penalise the square of the difference between prediction and truth.
- **Classification — cross-entropy.** The output is a probability per class. Penalise the log of the probability given to the right one.
- **Segmentation — per-pixel, plus overlap.** Cross-entropy at every pixel, usually combined with a term that rewards overlap of the whole region.

The other three ingredients do not notice the difference:
```
Data (unchanged) → Model (only the last layer changes) → Loss (swapped) → Optimizer (unchanged)
```

> ⚠️ Choosing a loss is choosing what you are willing to be wrong about. It deserves as much thought as the architecture.

---

## Slide 43: Training is walking downhill

*the loss as a landscape over the parameters*

*(Contour plot with two axes θ1 and θ2, showing a path of orange dots spiraling from "start: random weights" down to a green star marked "low loss".)*

**A surface over the parameters**
Fix the data. Then the loss is a function of the parameters alone — a surface with one height for every possible setting of the dials.

- **Two axes here,** millions in a real network
- **Height** is the loss on the training data
- **Training** is finding a low place on that surface

**We do not see the surface**
At any point we can measure the height and the local slope, and nothing else. Descending in fog, one step at a time.

---

## Slide 44: One step of gradient descent

*the slope says which way, the learning rate says how far*

*(Plot: a U-shaped loss curve over parameter θ, with a series of orange dots stepping down from a high point toward the minimum, marked by a green star.)*

**Downhill, one step at a time**

**The update rule:**
```
new θ = old θ − learning rate · slope of the loss at θ
```

- **The slope** is the gradient — one number per parameter
- **The minus sign** is what makes it descent rather than ascent
- **The learning rate** is ours to choose, and it is the one that hurts

**All parameters at once**
The same update is applied to every parameter in the same step, each with its own slope.

---

## Slide 45: The learning rate decides everything

*the same problem, three step sizes*

*(Three U-shaped loss curve plots, each showing gradient descent with a different step size.)*

- **Too small** — creeps — training takes for ever
- **About right** — steady progress to the bottom
- **Too large** — overshoots, and gets worse (steps bounce increasingly wildly between the two sides of the curve)

> ⚠️ If a training run misbehaves, the learning rate is the first thing to change — by a factor of ten, not ten per cent.

---

## Slide 46: Backpropagation

*one backward sweep gives the gradient of every parameter*

**Forward pass — work out the prediction, then the loss:**
```
x (the image) → layer 1 (×W1 + b1, σ) → layer 2 (×W2 + b2, σ) → ŷ (the prediction) → L (the loss)
```

**Backward pass — the chain rule, walked in reverse:**
```
∂L/∂ŷ (the prediction) ← ∂L/∂W2 (layer 2 weights) ← ∂L/∂W1 (layer 1 weights)
```
*one sweep gives every gradient*

> ⚠️ Backpropagation is not a learning algorithm. It is an efficient way to compute the derivatives that gradient descent needs.

---

## Slide 47: Batches, steps and epochs

*three words that get mixed up in many lab reports*

The training set: 12 samples → **batch size 3** → 4 batches per pass

Split into mini-batches:
```
step 1: [3 samples]
step 2: [3 samples]
step 3: [3 samples]
step 4: [3 samples]
```
**4 steps = 1 epoch** (one look at every sample)

> ⚠️ One step is one parameter update from one batch. One epoch is one pass over the whole training set.

---

## Slide 48: The training loop

*five steps, repeated thousands of times — and that is all training is*

Cycle: 1) take a batch → 2) forward pass → 3) compute the loss → 4) backward pass → 5) update θ → repeat (thousands of times)

```python
for epoch in range(n_epochs):
    for x, y in train_loader:        # 1
        y_hat = model(x)             # 2
        loss  = criterion(y_hat, y)  # 3
        loss.backward()              # 4
        optimizer.step()             # 5
        optimizer.zero_grad()
```

**The one line everyone forgets**
Without zero_grad() the gradients from every previous step keep adding up, and the run silently makes no sense.

> ⚠️ Everything else in this microcredential changes one line of this loop. The loop itself stays exactly as it is.

---

## Slide 49: When the loss will not go down

*a checklist, in this order, before you change the model*

1. **Overfit one batch** — Take eight samples and train until the loss is near zero. If it will not, the bug is in the code, not the data.
2. **Look at one batch** — Plot the images together with the labels the loader actually produced. This finds more bugs than anything else.
3. **Change the learning rate** — Ten times smaller, then ten times larger. Two runs, five minutes, and usually the answer.
4. **Check the label wiring** — Are the class indices in the order you assume? Is any label polarity inverted?
5. **Check the split** — Same patient, slide or video on both sides? A score that looks too good usually is.
6. **Compare the two curves** — Which curve misbehaves tells you which problem you have: capacity, data, or leakage.

Work down the list. Changing the architecture is somewhere below number ten.

---

## Slide 50: What to take away

*six sentences that carry the whole session*

- **Learning is fitting** — Choosing the parameters of a fixed function so that it reproduces examples. Nothing more mysterious than that.
- **Four ingredients** — Data, a model family, a loss, an optimizer. Every method is a choice of those four.
- **Features are the input** — Classical pipelines receive them from a human. Deep learning learns them too.
- **A neuron is arithmetic** — A weighted sum, a bias, one non-linear function. Depth re-describes the input until a line suffices.
- **Training is descent** — Follow the slope of the loss downhill; backpropagation supplies the slopes.
- **Validation is the truth** — Training loss says what the model memorised. Only held-out data says what it learned.

> ⚠️ Next: the same four ingredients, applied to images — and why a dense layer is the wrong first choice for a photograph.

---

## Slide 51: Images, data and credits

*everything used in this session, and what is illustrative*

**Medical images**
- Retinal fundus photograph: M. Häggström, WikiJournal of Medicine, CC0, via scikit-image (data.retina).
- Chest radiograph and retinal thumbnail: MedMNIST v2, Yang et al., Scientific Data 10:41 (2023), CC BY 4.0.
- Histology and cell images: scikit-image sample data.

**Figures**
All diagrams and plots were drawn for this course with Matplotlib.
The vessel overlay on the segmentation panel is a morphological filter, not a trained model, and the annotations on that slide illustrate output formats rather than predictions.

**What is illustrative rather than measured**
The lesion feature values, the training and validation curves, the loss surface and the annotation times are schematic: they were chosen to be readable and to show the right qualitative behaviour. No number on those slides should be quoted as a result.

*Questions during the session are welcome at any point — do not wait for the end.*

---

## Slide 52: Contact

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
