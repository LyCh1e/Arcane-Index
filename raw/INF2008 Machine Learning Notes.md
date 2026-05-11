# INF2008: Machine Learning Notes
> Lecturer: Donny Soh

---

# Lecture 00: Technological Trends

## Learning Outcomes
By the end of this lecture, students should be able to:
- Describe how exponential growth in computation, storage, and connectivity led to modern machine learning.
- Explain key AI perspectives (acting humanly, thinking rationally, cognitive modelling, acting rationally) and why learning-based approaches dominate today.
- Distinguish between supervised, unsupervised, and reinforcement learning, including classification versus regression.

---

## Exponential Growth — The Penny Problem
- A million dollars OR a cent on day one, doubled every day until day 30?
- Result: **$10,737,418.23** — exponential growth wins.

---

## Three Exponential Technological Trends

### 1. Computation Speed
- **Moore's Law**: the number of transistors in a dense integrated circuit (IC) doubles about every two years.

### 2. Hard-Disk Storage
- **Kryder's Law**: magnetic disk areal storage density was then increasing at a rate exceeding Moore's Law.

### 3. Network Connectivity
- **Edholm's Law**: the bandwidth of telecommunication networks (including the Internet) is doubling every 18 months.
- **Nielsen's Law**: High-end user's connection speed grows by 50% per year / doubles roughly every 21 months.
- **Butters' Law**: the amount of data coming out of an optical fiber is doubling every nine months.

> *Imagine the impact on our economy if the pandemic had happened 30 years earlier.*
> - 1991: Gopher | 1994: Yahoo! | 1998: Google | 2005: YouTube

---

## What is Artificial Intelligence?

### Definitions
- **Russell & Norvig (2010)**: Artificial intelligence is the study of intelligent agents that perceive their environment and take actions to achieve goals.
- **Nils J. Nilsson (1998)**: Artificial intelligence is the activity devoted to making machines intelligent, and intelligence is that quality that enables an entity to function appropriately and with foresight in its environment.
- **Ben Shneiderman (2020)**: AI systems are socio-technical systems designed to support or augment human decision-making, often operating with humans in the loop rather than as fully autonomous agents.

### Working Definition (This Course)
AI as computational systems that support adaptive decision-making, perception, or reasoning in complex environments, without assuming perfect rationality or human equivalence.

- **Machine Learning** (Arthur Samuel, 1959): Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed.

---

## Narrow AI — Four Definitions (Russell & Norvig)

| Perspective | Description |
|---|---|
| **Acting Humanly** | Turing Test Approach |
| **Thinking Humanly** | Cognitive Modeling |
| **Thinking Rationally** | First Order Logic |
| **Acting Rationally** | Rational Agents — agents that maximize the expected value of their performance measure given what they currently know |

---

## Types of Machine Learning

### Expert Systems vs Machine Learning
- **Expert Systems**: Domain Expert Rules + Data → Output
- **Machine Learning (Supervised)**: Data + Output → Machine Rules
- **Machine Learning (Unsupervised)**: Data → Machine (discovers structure)
- **Machine Learning (Reinforcement)**: Data + Reward → Machine Rules

### Machine Learning is Different from Expert Systems
> Expert Systems use rules to generate the output but Machine Learning uses output to generate rules.

---

## Types of Machine Learning — Definitions

- **Supervised Learning**: Learning a mapping from inputs to outputs, given a set of example input–output pairs. *(Bishop, 2006)*
- **Unsupervised Learning**: Discovering structure in a dataset without the use of labelled responses. *(Bishop, 2006)*
- **Reinforcement Learning**: Learning what to do, how to map situations to actions so as to maximise a numerical reward signal. *(Sutton & Barto, 2018)*

### Classification vs Regression
- **Classification**: Predicting a class.
- **Regression**: Predicting a number.

---

## Test Your Understanding

| # | Problem | Learning Type | Why |
|---|---|---|---|
| 1 | Given email labeled as spam/not spam, learn a spam filter | Supervised | Explicit labels |
| 2 | Group news articles into sets about the same story | Unsupervised | No labels; grouping by similarity |
| 3 | Automatically discover market segments from customer data | Unsupervised | Discovering structure without labels |
| 4 | Classify patients as having diabetes or not | Supervised | Known labels used for training |
| 5 | Automatically discover topics in documents | Unsupervised | Topic discovery without labels |
| 6 | Group website users into behavior patterns | Unsupervised | Pattern discovery without predefined classes |
| 7 | Predict the price of a new house | Supervised | Numeric target variable (price) |
| 8 | Detect defective products from labeled images | Supervised | Binary labels provided |
| 9 | Predict whether a loan should be approved | Supervised | Labels define the target outcome |
| 10 | Discover groups of genes with similar expression patterns | Unsupervised | Clustering without labels |

---

## Summary
- Exponential growth in computation, storage, and network connectivity fundamentally changed what computers could do at scale.
- As data volumes grew beyond what manual rules could handle, machine learning emerged as a practical alternative to rule-based systems.
- Modern AI systems are largely narrow, task-specific, and data-driven, rather than human-like or perfectly rational.
- Machine learning problems can be broadly categorized into supervised, unsupervised, and reinforcement learning, with supervised learning further divided into classification and regression.

---
---

# Lecture 01: Steps to Train a Model

## Types of Machine Learning (Recap)
- **Expert Systems**: Domain Expert Rules → Output
- **Supervised Learning**: Data + Output → Machine Rules
- **Unsupervised Learning**: Data → Machine Rules
- **Reinforcement Learning**: Data + Reward → Machine Rules

---

## Steps in a Machine Learning Project

### 1. Data Acquisition

**Obtain Data Sources**
- Decide what items/objects will be modeled (e.g., a specific black wallet vs a blue soccer ball).
- Ensure items are accessible during training.

**Collection of Data**
- Introduce variance: shake the item lightly to ensure some variance in the data to make the model more robust.
- Collect sufficient samples (~100 images) to give the training phase enough data per class.

### 2. Modelling
- Feed the acquired data into the model.
- Usually an iterative process.
- Select the algorithm and parameters.

**Testing**
- Testing data is totally different from training data.

### 3. Modelling Iteration
- **Iteration 1**: Add a Background Class — avoids the model predicting only known objects.
- **Iteration 2**: Add more object class data for robustness.

### 4. Model Biases
- Consider how the model will behave with different kinds of the same object.
- Consider how performance changes with different backgrounds.
- Identify additional biases in the dataset.

### 5. Model Deployment
- Deploy the model after adequate testing and iteration.

---
---

# Lecture 02: Value Generation

## Learning Outcomes
By the end of this lecture, students should be able to:
- Frame a business problem clearly before proposing a machine learning solution.
- Identify the decision, metric, and value associated with an ML use case.
- Quantify business impact using simple assumptions and arithmetic.

---

## Production ML Systems
- Most ML courses focus on algorithms (decision trees, linear models, etc.).
- These are still important but form just **one part** of the entire ML system.
- In production ML systems, the majority of system complexity and operational risk lies **outside** the model code.

---

## CRISP-DM Methodology

**CRoss-Industry Standard Process for Data Mining (CRISP-DM)**

Six phases:
1. **Business Understanding**
2. **Data Understanding**
3. **Data Preparation**
4. **Modeling**
5. **Evaluation**
6. **Deployment**

> The sequence of the phases is not strict and moving back and forth between phases is common.

### CRISP-DM Phases → Production ML System Components

| CRISP-DM Phase | Component | Explanation |
|---|---|---|
| Business Understanding | Configuration | Business objectives, constraints, thresholds, and assumptions encoded as configuration |
| Data Understanding | Data Collection | Data ingestion and exploratory analysis |
| Data Preparation | Data Verification / Feature Extraction | Data cleaning, validation, schema checks, and feature pipeline construction |
| Modeling | ML Code | Model development, training logic, and parameterisation |
| Evaluation | Analysis Tools | Offline evaluation, error analysis, and validation prior to deployment |
| Deployment | Serving Infrastructure / Machine Resource Management | Infrastructure required to deploy, scale, and operate the model |
| — | Process Management Tools | Workflow orchestration, scheduling, versioning |
| — | Monitoring | Post-deployment observation of system behaviour |

---

## Business Understanding Phase

**Key Point**: It is about decisions, outcomes, and constraints — NOT thinking of "cool" AI use cases.

### Framework
- **Problem**: What pain exists today?
- **Decision**: What decision is currently made poorly, manually, or too late?
- **Metric**: How do we know the decision improved?
- **Intervention**: What information or capability will ML provide to support the decision?
- **Value**: What business outcome changes if the decision improves?

---

## Example 1: Telco Customer Churn (MoonHub)

**Business Facts:**
- 4 million active users
- Monthly subscription fee: $20 per user
- Average monthly churn rate: 1%
- Users lost per month: 1% × 4,000,000 = **40,000 users**
- Monthly revenue lost: 40,000 × $20 = **$800,000/month**
- Annualised revenue loss: **$9.6 million/year**

**Business Understanding:**
| Element | Detail |
|---|---|
| Problem | Significant recurring revenue loss from churn |
| Decision | Which customers / when to target for retention actions |
| Metric | Monthly churn rate |
| Intervention | ML estimates churn risk; customers ranked for retention decisions |
| Value | Reducing churn 1.0% → 0.9% = 4,000 users retained = $80,000/month = $960,000/year retained |

---

## Example 2: Loan Processing Delays (JuneBank)

**Business Facts:**
- 500,000 loan applications per year
- Average processing time: 7 days
- Each approved loan generates $1,000 net revenue
- 10% of applications are abandoned before completion
- Abandoned applications: 50,000/year → **$50 million/year lost**

**Business Understanding:**
| Element | Detail |
|---|---|
| Problem | Slow and inconsistent processing drives abandonment |
| Decision | Which applications to prioritise for faster review |
| Metric | Application abandonment rate |
| Intervention | ML estimates likelihood of completion; applications ranked for prioritisation |
| Value | Reducing abandonment 10% → 9% = 5,000 additional completions = $5 million retained revenue/year |

---

## Summary
- ML creates value only when it improves a business decision.
- Before any modelling, Business Understanding defines: problem, decision, metric, intervention, value.
- If value cannot be clearly explained and quantified, the ML system is likely unnecessary.
- ML models optimise metrics; ML systems must justify business value.

---
---

# Lecture 03: Data Understanding

## Learning Outcomes
By the end of this lecture, students should be able to:
- Explain what Data Understanding is and why it comes before Data Preparation.
- Correctly identify variable meanings and types (numerical/cardinal, categorical nominal, categorical ordinal).
- Recognise when data is unsafe to use due to quality issues, leakage, imbalance, or wrong granularity.

---

## CRISP-DM Phases (Recap)
- **Business Understanding**: Defines what you want to achieve.
- **Data Understanding**: Defines what data you have.
- **Data Preparation**: Defines what you feed into the model.

> Most successful models are successful because of good data understanding / preparation.
> - Data understanding → typically referred to as **EDA**
> - Data preparation → typically referred to as **data engineering**

---

## Recurring Example: HDB Unit Price Prediction

**Features:**
- Location, Distance from MRT, Size, Years since TOP, Number of rooms, Number of bathrooms, Floor level

**Target:** Unit price

- This is a **supervised** regression problem.

---

## Stage 0: Data Generation Process
Ask:
- How was this data collected?
- By whom?
- Under what conditions?
- What incentives or constraints shaped it?
- Can this data be trusted, and if so, what are the constraints?

---

## Stage 1: Schema — What Does This Data Mean?
- What does each variable represent?
- How/Where was the data generated?
- Where can this data mislead us?
- **Common DU catches**: Treating IDs, timestamps, or labels as meaningful features.

### Independent vs Target Variables
- **Independent variables (features)**: Inputs you provide to a model (e.g., age, income, study hours).
- **Target variable (dependent variable / label)**: The output the model predicts (e.g., loan approval, exam score).

---

## Stage 2: Data Types — Cardinal vs Categorical

### Cardinal Data
Represents quantities where arithmetic operations are meaningful.
- **Key properties**: Values have magnitude; differences are meaningful; can add, subtract, average.
- **Continuous**: Can take any real value in a range (e.g., temperature, yield_percent).
- **Discrete**: Countable integers (e.g., defect_count, number of retries).

> The term *cardinal* was intentionally chosen because numerical variables may also be categorical.

### Categorical Data
Represents labels or groupings, not quantities.
- **Key properties**: Values identify classes; arithmetic operations are NOT meaningful.
- **Nominal**: Categories with no intrinsic order (e.g., lot_number, color).
- **Ordinal**: Categories with a meaningful order (e.g., Low < Medium < High), but equal spacing must NOT be assumed.

### HDB Example Data Types

| Variable | Variable Type | Data Type |
|---|---|---|
| Listing Number | Identifier | Categorical (Nominal) |
| Location | Independent | Categorical (depends!) |
| Distance from MRT | Independent | Cardinal (continuous) |
| Size | Independent | Cardinal (discrete) |
| Years since TOP | Independent | Cardinal (discrete) |
| Number of rooms | Independent | Cardinal (discrete) |
| Number of bathrooms | Independent | Cardinal (discrete) |
| Floor level | Independent | Cardinal (discrete) |
| Unit price | Dependent / Target | Cardinal (continuous) |

---

## Stage 3: Completeness
- Are there missing values?
- Which variables have missing values / disproportionate amount?
- Are missing values: Random? Systematic? Encoded inconsistently (NaN vs empty string)?
- **Critical DU question**: What might "missing" actually mean here?

---

## Stage 4: Sanity Checks

**Plausibility:**
- Are values within realistic ranges? (e.g., any HDBs > 100 years old?)
- Do minimums / maximums make sense?
- Are there impossible combinations? (e.g., 1 room flat with 3 showers)
- Are units consistent? (some rows use psf, some psm)

**Consistency:**
- Are categories spelled consistently? (AngMoKio vs AMK vs Ang Mo Kio)
- Do group-level summaries contradict expectations?

**Leakage:**
- Example feature: `resale_price_per_sqm` — computed from the resale price itself; directly gives the model the answer.

---

## Stage 5: Representativeness
- Are some classes/groups under-represented? (class imbalance)
- Are some groups missing entirely? (e.g., no 4-room HDB in Toa Payoh)
- Is the data representative of the population of interest?
- Are some categories rare but important? (e.g., HDBs nearing 99 years)

---

## Stage 6: Granularity & Aggregation Level
- Is the granularity correct for the task? (e.g., getting HDB price every day)
- Are there repeated entities?
- Should data be aggregated or split?

**Aggregation Example**: A flat may appear multiple times across years → aggregate to only transaction rows.

**Split Example**: Amenities listed as "MRT,School,Market" → split into different variables.

---

## Stage 7: Data Understanding Conclusion
DU must end with judgment:
- What analyses would be unsafe with this data?
- What conclusions would be unreliable?
- What assumptions would be required before proceeding?

> These define the **limitations** of the data.

---

## Summary
- Data Understanding is about **meaning**, not cleaning.
- Data types define what interpretations are valid.
- Leakage, imbalance, and wrong granularity make conclusions unreliable.
- DU ends with a decision: what questions this data **can and cannot** answer.

---
---

# Lecture 04: Introduction to Modelling — Baseline Model

## Learning Outcomes
By the end of this lecture, students should be able to:
- Explain why a baseline model is needed before attempting model optimisation or tuning.
- Correctly frame a supervised learning problem as classification or regression, and justify the choice.
- Apply appropriate train–test (or train–validation–test) splitting strategies, including when and why stratification is required.
- Train a baseline decision tree model using default settings, and explain what happens during model initialisation and fitting.
- Evaluate a baseline model using accuracy, and articulate the limitations of accuracy as a performance metric.
- Reason about model behaviour beyond accuracy, using concepts such as feature importance and rule generality.

---

## What is a Baseline Model?

A **baseline model** is a simple reference model, built with minimal assumptions and default settings, used to establish a minimum expected level of performance against which more complex models are compared.

- Establishes a **minimum acceptable performance**.
- Provides a **reference point for improvement**.

---

## What Counts as a Baseline?

1. **Majority class classifier**: Always predict the class that appears most often in the training set.
   - Example: If 82% of samples are "No", predict "No" for every case.

2. **Mean predictor (for regression)**: Always predict the average (mean) target value from the training set.
   - Example: If average house price is $520k, predict $520k for every house.

3. **Decision Tree with default settings.**

---

## Stratification

**Stratification** ensures that each data split keeps the same class ratio as the original dataset.

**Example**: Predicting ICT participation, 300 students, 30% ICT / 70% Non-ICT
- Without stratification (80/20 split → 60 test): might get 52 Non-ICT (87%) and 8 ICT (13%) — not representative.
- With stratification: test set has 42 Non-ICT and 18 ICT (correct ratios).

**Why it matters**: Without stratification, the test set may under-represent minority classes, making performance metrics unreliable.

### The M&Ms Problem
- Bowl: 950 Red + 50 Blue M&Ms
- **Without stratification**: Blindly grab 20 → likely get 20 Red, 0 Blue.
- **With stratification**: Deliberately pick 19 Red + 1 Blue → perfect representation.

---

## Train–Validate–Test Split

| Set | Purpose |
|---|---|
| **Training** | Build/fit candidate models; used repeatedly during hyperparameter tuning |
| **Validation** | Guide hyperparameter tuning decisions; model comparison |
| **Test** | Final judge of models; used **once** at the end; provides unbiased estimate of real-world performance |

> Test data must **never** influence training or model selection decisions.

---

## Model Initialisation

Model initialisation is the moment a model is defined, **before** it has seen any data.
- No patterns are learned.
- No parameters are estimated.
- No optimisation has occurred.
- Learning capacity/capability is **fixed** here.
- For a decision tree: tree structure is empty; hyperparameters are fixed.

---

## Model Fitting

- Training data is introduced.
- Internal parameters are determined to best match the objective, given fixed hyperparameters.
- The model improves performance while obeying limits defined at initialisation.
- Once fitted, model behaviour is shaped by both the **data** and the **chosen constraints**.

---

## Evaluation Metrics Overview

| Category | Metrics |
|---|---|
| Foundational | Confusion Matrix, Type I / Type II Errors |
| Classification | Accuracy, Balanced Accuracy, Precision, Recall, Specificity, F1 Score |
| Probability & Ranking | Log Loss, ROC-AUC, PR-AUC |
| Regression | MAE, MSE / RMSE, R² |

---

## Accuracy is Not Always Accurate

The basic accuracy measure ignores class imbalance, treating all errors as equal.

**Example: Fraud Detection**
- 100,000 transactions: 99,500 Legitimate (99.5%) + 500 Fraud (0.5%)
- Model predicts "Legitimate" for every transaction
- Accuracy = 99.5% — **but detects zero fraud cases!**

---

## Summary
- A baseline model establishes the minimum acceptable performance reference.
- Train-validate-test splitting ensures proper evaluation without data leakage.
- Stratification is critical for imbalanced datasets.
- Accuracy alone is misleading when classes are imbalanced.

---
---

# Lecture 05: Decision Trees

## Learning Outcomes
By the end of this lecture, students should be able to:
- Explain the structure of a decision tree, including roots, depth, internal nodes, leaves, and decision stumps.
- Explain what makes a good split using intuitive examples, and relate this idea to impurity reduction.
- Explain and compute Gini impurity for a node, and describe how it is used to select splits.
- Construct a simple decision tree step-by-step from a small labelled dataset using greedy splitting.
- Explain why decision trees are greedy and prone to overfitting.
- Explain how stopping criteria control overfitting and improve generalisation.

---

## What is a Tree? (Graph Theory)

In graph theory, a tree is an undirected, connected graph containing no cycles.
- Contains a single **root** node.
- Each node (except the root) must have a **single parent**.
- Starting from the root, we must be able to visit all nodes (tree is connected).

---

## What Makes a Good Split?

**Analogy — Sorting Clothes:**
- **Split by Type** (Shirts / Pants / Socks) → Each pile is uniform → **Good split**
- **Split by Color** (Blue/Red/Yellow/etc.) → Mixed types in each pile → **Bad split**

A good split makes resulting nodes more **uniform (pure)**.

---

## Entropy

**English definition**: Entropy is the lack of order. The more random an event, the higher its entropy.

$$H = -\sum_i p_i \log_2 p_i$$

- A fair coin (p=0.5): entropy = 1.0 (maximum)
- At p=0.3: entropy > 0.88
- At p=0.2: entropy > 0.72

---

## Gini Impurity

**Definition**: The probability that you would misclassify a randomly chosen data point if you guessed its label according to the class proportions in that node.

$$Gini = 1 - \sum_i p_i^2$$

- **Lower Gini = purer node**
- Gini = 0 when all samples belong to one class
- Faster to compute than entropy (no logarithms)

**Worked Example:**
- Node contains 10 samples: 7 Bus, 3 MRT
- p(Bus) = 0.7, p(MRT) = 0.3
- Gini = 1 − (0.7² + 0.3²) = 1 − (0.49 + 0.09) = 1 − 0.58 = **0.42**

---

## Decision Stump

A **binary decision stump** has:
- Depth of one
- Two binary outcomes
- Two leaves
- Three nodes

---

## Gini & Entropy on a Split (Before and After)

**Parent Node** (5 Bus, 3 MRT):
- p(B)=0.625, p(M)=0.375
- Gini(parent) = 1 − (0.625² + 0.375²) = 1 − 0.5312 = **0.469**
- H(parent) = **0.954**

**After Split:**
- Left child (2 Bus, 3 MRT): Gini(left) = 1 − (0.4² + 0.6²) = **0.48**
- Right child (3 Bus, 0 MRT): Gini(right) = **0**
- Weighted Gini = (5/8) × 0.48 + (3/8) × 0 = **0.30**
- Weighted Entropy = (5/8) × 0.971 + (3/8) × 0 = **0.607**

---

## Building a Decision Tree — Step by Step

**Running Example**: "How should I go to school today?"

**Features**: Breakdown (Slow/Yes/No), Rain (Y/N), Oversleep (Y/N), ML Lecture (Slight/Major/Average)

**Training Data (8 days):**

| Breakdown | Rain | Oversleep | ML Lecture | Bus/MRT |
|---|---|---|---|---|
| Slow | Y | Slight | Y | B |
| Yes | Y | Major | Y | B |
| Slow | N | Major | Y | M |
| No | N | Average | N | M |
| Slow | N | Average | N | B |
| Yes | N | Major | Y | B |
| Yes | N | Average | Y | B |
| Slow | Y | Slight | N | B |

**Process:**
1. Compute entropy/Gini for all possible decision stumps.
2. Select the split with the lowest entropy / highest information gain as the root node.
3. Recursively apply to each branch using only observations in that branch.
4. Continue until stopping criteria are met.

---

## When to Stop?

Entropy only tells us **where** to split, not **when** to stop. Splitting until entropy = 0 leads to:
- **Memorisation**
- **Perfect training accuracy**
- → **Overfitting**

### Stopping Criteria

| Parameter | Description |
|---|---|
| `max_depth` | Limits how many decisions a tree can make in sequence; prevents overly specific rules. (sklearn: root at depth 0) |
| `min_samples_split` | Requires a node to contain enough data before it is allowed to split |
| `min_samples_leaf` | Ensures each final rule is supported by a minimum number of samples; prevents memorising rare cases |

---

## Summary
- A good split makes resulting nodes more uniform (lower impurity).
- Gini impurity measures the probability of misclassification; lower is better.
- Decision trees are **greedy**: they choose splits based only on local improvement.
- Without stopping criteria, trees overfit by memorising training data.
- `max_depth`, `min_samples_split`, and `min_samples_leaf` are key regularisation tools.

---
---

# Lecture 06: Model Evaluation

## Learning Outcomes
By the end of this lecture, students should be able to:
- Explain why training accuracy alone is insufficient and articulate the concept of generalisation.
- Correctly apply train–validation–test splitting and justify the role of each dataset.
- Use k-fold cross-validation to compare models and tune hyperparameters.
- Construct and interpret confusion matrices and distinguish between Type I and Type II errors.
- Select and justify appropriate classification metrics based on problem context.
- Explain the bias–variance trade-off and diagnose underfitting vs. overfitting.
- Recommend corrective actions based on observed bias–variance cases.

---

## Will the Model Generalise?

- Decision trees can achieve **perfect training accuracy**.
- Key ML questions: Will this model generalise? How do we choose the correct model?

---

## Train–Validate–Test Split

| Set | Role |
|---|---|
| **Training** | Build/fit models; used repeatedly during hyperparameter tuning |
| **Validation** | Guide hyperparameter tuning; model comparison and ablation studies |
| **Test** | Final judge of models; used **once** at the end; unbiased estimate of real-world performance |

> Test data must **never** influence training or model selection decisions.

---

## Cross-Validation

Cross-validation is a **replacement for a validation set**.

### k-Fold Cross-Validation
1. Split data into k equal parts (folds)
2. Train on k−1 folds
3. Test on the remaining fold
4. Repeat k times (each fold tested once)
5. Average the performance metrics

**Coffee Shop Analogy**: 5 coffee shops, drink 4 cups/day, avoid one shop each day, rate after 5 days, choose the best average.

### Cross-Validation Process
- For each candidate model/hyperparameter: run k-fold CV → compute mean validation performance.
- Choose the setting with the best average CV score.
- Retrain one final model on the full training dataset.
- Cross-validation is **NOT** a guarantee of real-world performance.

**Used for**: Comparing models, choosing models, selecting hyperparameters.

---

## Foundational Metrics

### Confusion Matrix

|  | Predict True | Predict False |
|---|---|---|
| **Actual True** | True Positives (TP) | False Negatives (FN) |
| **Actual False** | False Positives (FP) | True Negatives (TN) |

- **Type I Error** = False Positive (FP)
- **Type II Error** = False Negative (FN)

---

## Classification Metrics

**Running Example** (Rain prediction): 500 observations, 280 actual rain, 220 actual no rain.

| | Predict True | Predict False |
|---|---|---|
| **Actual True** | 280 (TP) | 0 (FN) |
| **Actual False** | 70 (FP) | 150 (TN) |

### Accuracy
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FN + FP} = \frac{280 + 150}{500} = 86\%$$

### Balanced Accuracy
$$\text{Balanced Accuracy} = \frac{\frac{TP}{TP+FN} + \frac{TN}{TN+FP}}{2} = \frac{1.0 + 0.6818}{2} = 84.1\%$$

### Precision, Recall, Specificity
$$\text{Recall} = \frac{TP}{TP + FN}$$ — Out of all actual positives, what % did the model correctly predict?

$$\text{Precision} = \frac{TP}{TP + FP}$$ — What % of positive predictions were correct?

$$\text{Specificity} = \frac{TN}{TN + FP}$$ — How well did the model catch negative cases?

### Precision-Recall Trade-off
- **High precision, low recall**: You say YES rarely, but right when you do; many real YES cases are missed.
- **High recall, low precision**: You say YES a lot; catch everything, but many YESes are wrong.

### F1 Score
Uses the **harmonic mean** between precision and recall:

$$F1 = \frac{2 \times Precision \times Recall}{Precision + Recall}$$

- If either value is small, F1 becomes very small.
- Good for **imbalanced data**.
- Example: If 1 in 10,000 credit card transactions is fraudulent, predicting everything as non-fraudulent gives 99.99% accuracy but F1 = 0.

---

## Bias–Variance Trade-off

The error for any supervised ML algorithm = **Bias error + Variance error + Noise**.

### Bias (Underfitting)
- Model is too simple to capture patterns.
- Makes strong assumptions.
- High training error, high test error.
- Example: Shallow decision tree (depth = 1–2).

### Variance (Overfitting)
- Model is too flexible; learns noise in training data.
- Low training error, high test error.
- Example: Deep decision tree (many splits).

> Decision trees are **low-bias, high-variance** models.
> - Low bias → can fit complex patterns
> - High variance → small data changes result in very different trees

---

## Bias–Variance Cases

| | Low Variance | High Variance |
|---|---|---|
| **Low Bias** | ✅ Ideal (well-fit model) | Overfitting — model's predictions vary widely across datasets |
| **High Bias** | Underfitting — predictions consistent but far from truth | Poor design/data — model is both wrong and unstable |

### Analogies
- **Low Bias, Low Variance**: Professional marksman hitting bullseye 10 times in a row.
- **High Bias, Low Variance**: Digital scale always 1kg lighter — reliable but systematically inaccurate.
- **Low Bias, High Variance**: Students who memorise practice papers without understanding concepts.
- **High Bias, High Variance**: Voice recognition system trained on few noisy, varied recordings.

### Actions to Take

| Case | What to Do |
|---|---|
| **High Bias (Underfitting)** | Increase model complexity, add features, reduce regularisation |
| **Low Bias, High Variance (Overfitting)** | Regularise, add data, use ensembling (bagging, random forests) |
| **High Bias, High Variance** | Revisit problem formulation, fix data quality, feature selection, increase dataset size significantly |
| **Low Bias, Low Variance** | Monitor for drift, validate on truly unseen data |

---

## Learning Curves

### High Bias, Low Variance
- Both training and test accuracies are low and converge to approximately the same value as training samples increase.
- Test curve plateaus early and well below the desired performance — even with more data, performance doesn't improve meaningfully.

### Low Bias, High Variance
- Training accuracy starts high but decreases slightly as more data is added.
- Test accuracy starts low and increases steadily.
- Large gap between training and test accuracy → adding data helps reduce variance.

### Low Bias, Low Variance (Ideal)
- Training and test accuracy converge near the target.
- Adding data improves test accuracy.
- Small gap that narrows quickly.

---

## Summary
- Cross-validation enables robust model selection without compromising the test set.
- Different metrics reveal different failure modes — choose based on application context.
- Bias–variance trade-off guides corrective actions based on observed training/validation behaviour.

---
---

# Lecture 07: Ensemble Methods

## Learning Outcomes
By the end of this lecture, students should be able to:
- Explain why ensemble methods can improve generalisation by reducing bias and/or variance.
- Differentiate between bagging, boosting, and stacking.
- Explain how Random Forests combine bootstrap sampling and feature subsampling to reduce variance.
- Describe out-of-bag (OOB) estimation.
- Explain boosting as a sequential error-correcting process.

---

## Why Ensemble Learning?

**Nasi Lemak Analogy:**
- One review = one very opinionated uncle.
- Thousands of reviews average out personal bias.
- We trust the crowd more than choosing blind.

**Ensemble Learning:**
- Combines multiple base learners.
- Predictions are aggregated by voting or averaging.
- Base learners must be both **accurate** and **diverse**.

---

## When Ensembles Work / Fail

| Case | Description | Result |
|---|---|---|
| **Uncorrelated errors, real signal** | Five blind men touching different parts of a real elephant — each observation is partially correct, errors are uncorrelated | ✅ Ensembles work |
| **Correlated errors** | All five blind men touching the same leg — everyone says "it's a tree"; no diversity | ❌ Ensembles fail |
| **Bad data / no signal** | Five blind men touching a tree, wall, or ground instead of elephant — wrong input | ❌ Ensembles still fail |

---

## Types of Ensemble Learning

### Bagging
- Train many models on slightly different datasets (bootstrap samples).
- Average their predictions.
- Targets **variance reduction**.
- Does **not** fix systematic bias.

### Boosting
- Forces each new model to focus on previous mistakes.
- Builds a more complex decision boundary over time.
- Targets **bias reduction**.

**Food Recommendation Analogy for Boosting:**
- Round 1: "Where should I eat?" → "McDonald's."
- Round 2: "Where except fast food?" → "PS Cafe."
- Round 3: "Where except fast food and expensive cafes?" → "Small Japanese ramen."

### Stacking
- Train different types of models on the same dataset.
- Train a final meta-model that learns how to combine their predictions.

---

## Random Forests (Bagging)

Random Forests = Bagging + additional randomness:
1. **Bootstrap sampling of data** (bagging)
2. **Random sub-sampling of features at each split** (feature bagging)

Predictions from individual trees are aggregated → **Bootstrap Aggregation**.

### Bootstrap Algorithm
- To create dataset D1 of size N:
  - Draw one sample from original dataset D0
  - Place a copy in D1
  - Replace it back in D0
  - Repeat N times
- This process can be **parallelised** for each tree.

### Why Sub-datasets are Also N Samples?
**Statistical foundation**: Sampling N points from N preserves:
- Expected empirical distribution
- Variance properties of estimators
- Bias unchanged; variance decreases significantly.

---

## Out-of-Bag (OOB) Property

For each tree trained via bootstrap sampling:
- Each tree draws N samples with replacement
- Probability a given sample is NOT selected for that tree:

$$\left(1 - \frac{1}{N}\right)^N \approx e^{-1} \approx 0.368$$

- **~36.8%** of training samples are OOB for each individual tree.
- **~63.2%** appear at least once.
- Each data point is OOB for ~36.8% of trees.

### OOB Testing Process
1. For each training sample xi, identify all trees that did NOT see xi (~36.8% of trees).
2. Predict xi using only those trees.
3. Compare to true label.
4. Repeat for all samples.

$$\text{OOB Accuracy} = \frac{\text{\# samples whose OOB prediction is correct}}{\text{\# samples that have at least one OOB prediction}}$$

---

## Feature Subsampling in Random Forests

**Problem without feature subsampling:**
- Strong features dominate early splits.
- Trees become similar → correlated errors.
- Averaging adds no new information.

**With feature subsampling:**
- Each split considers only a random subset of features.
- Different trees focus on different features.
- Lower correlation between trees → stronger ensemble and lower variance.

**Asian Parents Analogy:**
- Without subsampling: Ask 10 relatives "study or play?" → all focus on academics.
- With subsampling: Each relative considers only one factor (health, happiness, discipline, etc.) → diverse advice.

---

## Random Forest Hyperparameters

| Feature | Meaning | Default |
|---|---|---|
| `n_estimators` | Number of decision trees | 100 |
| `criterion` | Split quality measure (gini/entropy) | gini |
| `max_depth` | Maximum depth of each tree | None |
| `min_samples_split` | Min samples to split at an internal node | 2 |
| `min_samples_leaf` | Min samples at a leaf node | 1 |
| `max_features` | Features to consider at each split | sqrt(num_features) |
| `bootstrap` | Enable bootstrap sampling | True |
| `random_state` | Random seed for reproducibility | None |

---

## AdaBoost Intuition

1. Train first model; identify incorrectly predicted points.
2. Increase weightage of incorrectly predicted points (size increase).
3. Train a new model on these weighted points.
4. Repeat until stopping criteria.
5. Combine all models into an ensemble classifier.

---

## Gradient Boosting (GBM) Intuition

- Tree boosting builds models **sequentially**.
- A weak regression tree is first trained on the input data.
- The **loss gradients** (errors) of this model are computed.
- Subsequent weak trees are trained to predict these gradients.
- Each new tree focuses on aspects the current ensemble predicts poorly.
- At prediction time, outputs of all trees are **summed**, scaled by a learning rate η.

---

## What is a Loss Gradient?

**Example**: y_actual = 10, y_pred = 7

- Residual = 10 − 7 = 3
- Loss (Squared Error): L = (10 − 7)² = 9
- Loss gradient: dL/dy_pred = −2(10 − 7) = −6

**Interpreting the sign (−)**: Prediction is too low; needs to increase.
**Interpreting the magnitude (6)**: How urgently to move (−6 is much worse than −0.006).

**What boosting does with −6:**
- Creates new tree trying to predict −6 for this data point.
- Tree output scaled by learning rate η (e.g., η=0.1):
  - y_new = 7 − 0.1 × (−6) = 7.6

### Iterative Loss Gradient
- Iteration 0: ŷ₀ = 7 → gradient = −6 → ŷ₁ = 7.6
- Iteration 1: ŷ₁ = 7.6 → gradient = −4.8 → ŷ₂ = 8.08
- Iteration 2: ŷ₂ = 8.08 → gradient = −3.84 → ŷ₃ = 8.464
- Sequence: 7 → 7.6 → 8.08 → 8.464 → … → 10

---

## When Does Boosting Stop?

1. Gradient = zero (theoretical; causes overfitting).
2. **Early stopping** — adding another tree no longer improves validation performance.
3. **Fixed number of trees** (number of iterations).
4. **Minimum improvement threshold** (loss < certain value).
5. Library implementations:
   - `GradientBoosting` (sklearn): Fixed estimators + optional early stopping
   - `XGBoost` / `LightGBM`: Early stopping with fixed number of trees

---

## Summary

| Method | Error Reduced | Training | Aggregation |
|---|---|---|---|
| Bagging | Variance | Parallel | Voting/Averaging |
| Boosting | Bias | Sequential | Weighted sum |
| Stacking | Both | Parallel | Meta-learner |

---
---

# Lecture 08: Embeddings (Categorical Encoding)

## Learning Outcomes
By the end of this lecture, students should be able to:
- Differentiate between numerical and categorical variables.
- Explain why categorical features require encoding before model training.
- Compare Label Encoding and One-Hot Encoding.

---

## The Problem — Computers Cannot Read!

- Computers/Models only understand numbers.
- What about values like: Color_door = Red, Color_roof = Blue, Color_window = Green?
- The colors have no numeric scale / representation.
- If you sort alphabetically: Grande, Tall, Venti (Starbucks sizes) — this imposes a meaningless order.

---

## Label Encoding

**Definition**: Assigns a unique integer to each category.

**Example** — "Color" column:
- Red: 0
- Green: 1
- Blue: 2

### Advantages
- Memory efficient (single column).
- Useful for **ordinal** data (preserves ranking).

### Disadvantages
- **Imposes artificial ordinality**: Model might incorrectly assume Red (0) < Green (1) < Blue (2).
- Can mislead models like linear regression that interpret numbers as meaningful distances.

### When Label Encoding Makes Sense
When the **order is meaningful** (ordinal variables):
- Low = 0
- Medium = 1
- High = 2

---

## One-Hot Encoding (OHE)

**Definition**: Creates a new binary column for each unique category.

**Example** — "Color" column:
- Red: [1, 0, 0]
- Green: [0, 1, 0]
- Blue: [0, 0, 1]

### Advantages
- Avoids ordinal misinterpretation.
- Works well for **non-ordered** categorical features.

### Disadvantages
- Increases memory usage.
- **Curse of Dimensionality**: High-dimensional data can slow training.
- 500 different zip codes → 500 new variables.

---
---

# Lecture 09: Linear Models I

## Learning Outcomes
By the end of this lecture, students should be able to:
- Explain what linear regression is and identify dependent and independent variables.
- Describe what residual (error) means and how model error is measured using RMSE.
- Explain how learning in linear regression involves minimizing prediction error.
- Extend linear regression to multiple linear regression.
- Explain how a single-layer perceptron relates to linear regression and why non-linearity matters.

---

## Linear Regression

**Classic Example**: Pendulum experiment
- We adjust the **length** of the pendulum (Independent Variable, x).
- We measure the **period** of the pendulum (Dependent Variable, y).
- This is **regression** — predicting a continuous output.

$$y = m \times x + c$$

**Sample Data:**
| x (cm) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| y (s) | 2.6 | 3.6 | 3.5 | 4.9 | 5.1 | 5.8 | 6.3 | 6.6 | 7.3 | 8.2 |

---

## What is Residual Error?

$$e_i = y_i - \hat{y}_i$$

The residual error is the difference from the actual (y_actual) from the predictions (y_predicted).

---

## What is Squared Error?

If we just summed the errors, positive and negative errors cancel out.
$$\sum (y_i - \hat{y}_i) \rightarrow +3 \text{ and } -3 \text{ sum to } 0$$

So we **square** the errors:
$$\sum (y_i - \hat{y}_i)^2$$

Benefits:
- All errors become positive.
- Large errors affect the total more (penalty for large errors).

---

## Root Mean Squared Error (RMSE)

$$MSE = \frac{1}{n} \sum (y_i - \hat{y}_i)^2$$

$$RMSE = \sqrt{\frac{1}{n} \sum (y_i - \hat{y}_i)^2}$$

- Divide by n to get the **mean** of the squared errors.
- Square root to get back the **same units** as y.
- **Learning** = choosing the line of best fit that minimizes RMSE.

$$\min_{m,c} RMSE(m, c)$$

---

## Multiple Linear Regression

**Extended Example**: Adjust both the **length** and **weight** of the pendulum.

$$y = \sum_{k=1}^{d} (m_k \times x_k) + c$$

**Sample Data:**
| x1 (cm) | 1 | 1 | 1 | 4 | 4 | 4 | 7 | 7 | 7 | 10 | 10 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| x2 (g) | 10 | 20 | 30 | 10 | 20 | 30 | 10 | 20 | 30 | 10 | 20 | 30 |
| y (s) | 2.6 | 2.4 | 2.5 | 4.9 | 4.7 | 4.5 | 6.3 | 6.6 | 6.5 | 8.2 | 8.1 | 8.3 |

Weight has little impact on period — mostly x1 (length) drives the prediction.

---

## Neural Network: Single Layer Perceptron

Extends multiple linear regression by applying a **nonlinear activation function**:

$$z = \sum_{k=1}^{d} (m_k \times x_k) + c$$

$$y = f(z)$$

If f(z) = z, then: y = f(z) = z → exactly multiple linear regression.

---

## What is a Non-linear Function?

- **Linear**: $1, 2, 3, 4, 5 → \$5, \$10, \$15, \$20, \$25$ (constant rate)
- **Non-linear**: $1, 2, 3, 4 → \$5, \$9, \$15, \$20$ (varying rate)

---

## Linear Models — Increasing Complexity
1. Linear Regression: y = mx + c
2. Multiple Linear Regression: y = Σ(mk × xk) + c
3. Neural Network (Single Layer Perceptron): y = f(Σ(mk × xk) + c)

---
---

# Lecture 10: Linear Models II

## Learning Outcomes
By the end of this lecture, students should be able to:
- Explain the formulation of simple and multiple linear regression.
- Describe how gradients are used to train regression models.
- Express regression learning using vectorised gradient notation.
- Explain how a neuron generalises linear regression.
- Describe the role of activation functions and loss functions in neural networks.
- Explain how neural networks learn using forward pass, backpropagation, and gradient descent.

---

## How Learning Works — The Guessing Game

Guessing a number between 0–99:
- Each wrong guess gives feedback (higher/lower).
- Each new guess narrows the search.
- Loss decreases with each better guess.
- → This is analogous to **gradient descent**.

---

## Simple Linear Regression — Full Theory

### Four Steps:

#### 1. Forward Pass
$$\hat{y}_i = w^T x_i + b$$
- yi = true value (target)
- ŷi = predicted value
- xi = input feature
- w = weight (parameter)
- b = bias (intercept)

Initialise w, b, then calculate ŷi.

#### 2. Loss Calculation (Half MSE)
$$L(w, b) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

Goal: find w and b that minimize this loss.

#### 3. Backpropagation
$$\frac{\partial L}{\partial w} = -\frac{1}{n} \sum e_i x_i$$

$$\frac{\partial L}{\partial b} = -\frac{1}{n} \sum e_i$$

Where: ei = yi − ŷi (residual)

#### 4. Gradient Descent
$$w = w - \alpha \frac{\partial L}{\partial w}$$

$$b = b - \alpha \frac{\partial L}{\partial b}$$

Where α is the learning rate.

---

## Simple Linear Regression — Worked Example

Data: (x=2, y=3), (x=3, y=4), (x=4, y=5)
Initialize: w=1, b=0, α=0.1

| i | x | y | ŷ=wx+b | e=y−ŷ |
|---|---|---|---|---|
| 0 | 2 | 3 | 2 | 1 |
| 1 | 3 | 4 | 3 | 1 |
| 2 | 4 | 5 | 4 | 1 |

L = (1/6)(1² + 1² + 1²) = 0.5

∂L/∂b = −(1/3)(1+1+1) = −1

∂L/∂w = −(1/3)(1×2 + 1×3 + 1×4) = −3

**Updated:** w = 1 − 0.1×(−3) = **1.3**, b = 0 − 0.1×(−1) = **0.1**

---

## Multiple Linear Regression — Vectorised

$$\hat{y}_i = w^T x_i + b \quad \text{where } w, x_i \in \mathbb{R}^d$$

**Gradient formulas (vectorised):**
$$\nabla_w L = -\frac{1}{n} X^T e$$

$$\frac{\partial L}{\partial b} = -\frac{1}{n} \sum_{i=1}^{n} e_i$$

**Update rules:**
$$w = w - \alpha \nabla_w L$$

$$b = b - \alpha \frac{\partial L}{\partial b}$$

---

## What is a Neuron?

**Step 1**: Compute the same linear model:
$$z = W^T x + b$$

**Step 2**: Apply a nonlinear transformation:
$$a = \sigma(z)$$

| Symbol | Meaning |
|---|---|
| x | Input features |
| w | Weights |
| z | Linear combination |
| a | Activated output |

**Without activation**: Stacking layers W₂(W₁x) is still linear.
**With activation**: The network becomes nonlinear and can represent complex functions.

---

## Why Use Activation Functions?

1. **Non-linearity**: Without activation, stacking layers collapses to a single linear transform.
2. **Feature Interactions**: Activation functions enable composition of nonlinear transformations.
3. **Non-linear decision boundaries**: Linear models can only separate linearly separable data.

---

## Inner (Hidden Layer) Activation Functions

| Activation | Formula | Range | Pros |
|---|---|---|---|
| **tanh** | tanh(x) = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ) | (−1, 1) | Zero-centered |
| **ReLU** | ReLU(z) = max(0, z) | [0, ∞) | Computationally simple; no saturation for positive; faster training |
| **Leaky ReLU** | max(αz, z) | (−∞, ∞) | Fixes dead neuron issue |

**Typical usage today:**
- ReLU → default hidden layers
- Leaky ReLU → deep CNNs / GANs
- tanh → mostly RNNs / LSTMs

---

## Output Activation Functions

| Task | Output Activation |
|---|---|
| Regression | Linear (identity): f(z) = z |
| Binary classification | Sigmoid: σ(z) = 1/(1+e⁻ᶻ), Range: (0, 1) |
| Multi-label classification | Sigmoid (per class) |
| Multi-class classification | Softmax: softmax(zᵢ) = eᶻⁱ / Σⱼeᶻʲ |

**Softmax Example** (3 classes):
- Input logits: z = [2.0, 1.0, 0.1]
- Softmax output: [0.659, 0.242, 0.099]
- Outputs sum to 1.

---

## How Does Learning Take Place in a Neuron?

### Chain Rule for Backpropagation
$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}$$

$$\frac{\partial L}{\partial b} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial b}$$

### Loss Functions
- **Regression**: Half MSE = (1/2n) Σ(yᵢ − ŷᵢ)²
- **Classification**: Cross Entropy Loss = −Σ tᵢ × log(pᵢ)

### Gradient Descent Update
$$W = W - \lambda \frac{\partial L}{\partial W}$$

$$b = b - \lambda \frac{\partial L}{\partial b}$$

---

## Backpropagation — Step by Step Example

**Setup**: x=2, w=0.5, b=1, a=z (identity activation), y=4, λ=0.1

**Forward Pass:**
- z = 0.5×2 + 1 = 2
- a = z = 2
- ŷ = 2

**Loss Calculation:**
- L = (1/2)(4−2)² = 2

**Backpropagation:**
1. ∂L/∂a = a − y = 2 − 4 = −2
2. ∂a/∂z = 1 (identity activation)
3a. ∂z/∂w = x = 2
3b. ∂z/∂b = 1

**Chain Rule:**
- ∂L/∂w = (−2)(1)(2) = −4
- ∂L/∂b = (−2)(1)(1) = −2

**Gradient Descent:**
- w = 0.5 − 0.1×(−4) = **0.9**
- b = 1 − 0.1×(−2) = **1.2**

---
---

# Lecture 11: Unsupervised Learning (Clustering)

## Learning Outcomes
By the end of this lecture, students should be able to:
- Explain how unsupervised learning differs fundamentally from supervised learning.
- Compute and interpret L1, L2, and L∞ distances.
- Derive and explain the K-means objective function.
- Identify when K-means will fail.
- Explain how DBSCAN defines density and detects noise.
- Compare K-means and DBSCAN mathematically and practically.

---

## Supervised vs Unsupervised Learning

**Supervised Learning**: Data has two parts — labeled data (y-variable / dependent variable) and input features (x-variables / independent variables).

**Unsupervised Learning**: Given only X = {x₁, x₂, ..., xₙ} — **there is no Y**.
- Goal: discover hidden structure and group similar points.
- No ground truth / explicit target.

---

## Distance Measures

### Euclidean Distance (L2 Norm)
$$d(x, y) = \sqrt{\sum_{i=1}^{p} (x_i - y_i)^2}$$

**Example**: City A at (3,4), City B at (7,1):
d(A,B) = √((7−3)² + (1−4)²) = √(16+9) = √25 = **5**

### Manhattan Distance (L1 Norm)
$$d(x, y) = \sum_{i=1}^{p} |x_i - y_i|$$

**Example**: Walking in NYC grid from (2,3) to (5,6):
d(A,B) = |5−2| + |6−3| = 3+3 = **6**

### Chebyshev Distance (L∞ / Maximum Norm)
$$d(x, y) = \max_{1 \leq i \leq p} |x_i - y_i|$$

**Example**: Chess king from (1,1) to (4,6):
d(A,B) = max(|4−1|, |6−1|) = max(3, 5) = **5**

---

## Distance Example — Worked

**Points**: A=(3,5,7), B=(9,5,9)

| Distance | Calculation | Result |
|---|---|---|
| Manhattan | |3−9| + |5−5| + |7−9| = 6+0+2 | **8** |
| Euclidean | √((-6)² + 0² + (-2)²) = √(36+0+4) | **√40** |
| Chebyshev | max(6, 0, 2) | **6** |

---

## k-Nearest Neighbour Algorithm

- For each new test data point, find the k closest data points.
- Take a vote count among those k neighbors and assign the majority class.

**Issues:**
- Very prone to overfitting. Common heuristic: k = √(number of training samples).
- Doesn't work well when the number of training samples or features is large.
- Must **scale/normalize** features — otherwise features with larger numeric range dominate distances.

---

## K-Means Clustering

### Objective Function
$$J = \sum_{j=1}^{k} \sum_{x_i \in C_j} ||x_i - \mu_j||^2$$

Where:
- J = sum of squared distances (loss function)
- k = number of clusters
- μⱼ = centroid (mean vector) of cluster j
- Cⱼ = set of points assigned to cluster j

### Why the Mean?
The centroid that minimizes the within-cluster sum of squared distances **is the mean**:
$$\mu_j = \frac{1}{|C_j|} \sum_{x_i \in C_j} x_i$$

*Mathematical proof*: Setting the derivative of Jⱼ to zero with respect to μⱼ gives μ = (1/n)Σxᵢ. Second derivative = 2n > 0, confirming a global minimum.

---

## K-Means Algorithm

```
1. Initialize k centroids (e.g., random data points)
2. REPEAT:
   a. Assign each point to the nearest centroid
   b. Recalculate centroids as means of assigned points
3. UNTIL convergence (centroid locations don't change,
   loss below threshold, or max iterations reached)
```

---

## K-Means: Choosing K

- K-means requires us to choose k **in advance**.
- Choosing k is fundamentally **heuristic**.
- As k increases, loss **always decreases**.

### Elbow Method
- Plot J vs k; look for "elbow" (point of diminishing returns).
- **Limitations**: Subjective, may not exist clearly, not a statistical test, is just a visual heuristic.
- In high dimensions: elbow curves become smoother; harder to choose k.

### Silhouette Score

For each data point xᵢ:
- a(i) = average distance from xᵢ to points in its **own** cluster
- b(i) = average distance from xᵢ to points in the **nearest other** cluster

$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

**Average silhouette score:**
$$\bar{s} = \frac{1}{n} \sum_{i=1}^{n} s(i)$$

| Score | Interpretation |
|---|---|
| Close to 1 | Well separated clusters |
| Close to 0 | Weakly separated clusters |
| Negative | Likely wrong assignment |

---

## K-Means Limitations

- Assumes clusters are **spherical / convex**.
- Fails on irregular shapes (e.g., spiral clusters).
- Sensitive to initialisation.

---

## K-Means++ Initialisation

Instead of random selection:
1. Choose first centroid randomly.
2. Choose next centroid with probability proportional to **squared distance** from nearest existing centroid.

$$P(x_i) \propto D(x_i)^2$$

Points farther away are more likely to be selected as the next centroid.

---

## DBSCAN

**Density-Based Spatial Clustering of Applications with Noise**

### Parameters
- **ε (epsilon)**: Radius within which points are considered neighbors.
- **MinPts**: Minimum number of points required to form a dense region.

### Point Types
| Type | Definition |
|---|---|
| **Core Point** | Has ≥ MinPts points within ε (including itself) |
| **Border Point** | Has < MinPts within ε, but lies within ε of at least one core point |
| **Noise / Outlier** | Has < MinPts within ε AND is not within ε of any core point |

### DBSCAN Algorithm
1. Pick a random unvisited point.
2. If it has ≥ MinPts neighbors within ε → core point → new cluster.
3. Expand cluster recursively to all points within ε.
4. If not a core point and not a neighbor → outlier.

### Key Features
- **No need to predefine k** — automatically finds optimal cluster count.
- Can detect **clusters of irregular shapes**.
- Identifies **outliers** (noise points).

### Limitations
- Choosing right ε and MinPts can be tricky.
- Struggles when cluster densities differ significantly.

---

## Effects of Parameters

### Epsilon Effects
- **Large ε**: Over-merging → many points in one cluster.
- **Reducing ε**: Helps separate distinct shapes.
- **Too small ε**: Too much fragmentation.

### MinPts Effects
- **Small MinPts**: Low bias, high variance; sensitive to noise; many small clusters.
- **Large MinPts**: High bias, low variance; misses small clusters; more noise points.
- **Very large MinPts**: Even real clusters break apart; fragmentation increases.

---

## K-Means vs DBSCAN

| Feature | K-Means | DBSCAN |
|---|---|---|
| Requires k? | Yes | No |
| Shape Assumption | Spherical / Convex | Arbitrary |
| Handles Noise | No | Yes |
| Sensitive to Scaling | Yes | Yes |
| Sensitive to Initialization | Yes | No |
| Struggles With | Irregular shapes | Varying densities |
| Optimization based | Yes (minimizes J) | No |
| Produces convex clusters | Yes | No |
| Works Well When | Compact clusters | Density-separated clusters |

---

## Appendix: Unsupervised Learning Methods

### Cluster Analysis
**Partitional Clustering:**
- **K-Means**: Centroid-based; assigns points to nearest cluster center iteratively.
- **DBSCAN**: Density-based; groups dense areas; detects outliers as noise.

**Hierarchical Clustering:**
- **HDBSCAN**: Hierarchical DBSCAN; automatically determines optimal cluster count.
- **DIANA**: Divisive; starts with all points in one cluster and recursively splits.

### Dimensionality Reduction
**Linear Methods:**
- **PCA** (Principal Component Analysis): Transforms correlated features into uncorrelated components.

**Non-Linear Methods:**
- **t-SNE**: Maps high-dimensional data to 2D/3D for visualization.
- **UMAP**: Similar to t-SNE but faster and better at preserving structure.

**Feature Selection:**
- **Recursive Feature Elimination (RFE)**: Iteratively removes less important features.
- **Mutual Information**: Measures information a feature contributes.

### Association Rule Mining
- **Apriori Algorithm**: Finds associations by analyzing frequently occurring itemsets.
- **FP-Growth**: More memory-efficient; no multiple dataset scans needed.
- **GSP**: Detects sequences of events in datasets.
- **PrefixSpan**: Efficient sequential pattern discovery.

---
---

# Lecture 12: Unsupervised Learning II — PCA & t-SNE

## Learning Objectives
By the end of this lecture, students should be able to:
- Understand the need for PCA and explain why dimensionality reduction is useful.
- Perform PCA step by step.
- Interpret PCA results and scatter plots.
- Compare custom PCA with sklearn implementation.
- Understand the motivation and intuition behind t-SNE.

---

# Part I: Principal Component Analysis (PCA)

## Motivating Example: Food Nutritional Labels

Food labels contain many numbers: Calories, Carbohydrates, Sugar, Fat, Protein, Sodium.

**Observations:**
- Foods high in carbs are often high in sugar.
- Foods high in fat are often high in calories.
- High sodium foods usually don't have much sugar.

**Simplified to 3 key factors:**
1. **Energy intake** → combines Calories, Carbs, Sugar
2. **Heart health** → combines Fat, Sodium
3. **Protein intake** → remains separate

→ This is exactly what PCA does: finds patterns and reduces complexity while keeping the most important information.

---

## PCA Concepts

- **Features**: Original variables in the dataset.
- **Principal Components (PCs)**: New orthogonal directions formed as **linear combinations** of features.
  - Rotated coordinate axes
  - Capture the most variance in the data

---

## PCA — Step by Step

### Step 1: Standardize the Data

$$X_{scaled} = \frac{X - \bar{X}}{\sigma}$$

**Example (Calories for Chicken, Apple, Cake):**
| Food | Original | Mean | Std Dev | Scaled |
|---|---|---|---|---|
| Chicken | 165.0 | 203.33 | 107.57 | -0.356 |
| Apple | 95.0 | 203.33 | 107.57 | -1.007 |
| Cake | 350.0 | 203.33 | 107.57 | 1.363 |

**Why standardize?**
- PCA maximizes variance.
- If one feature has a larger scale, it dominates the covariance matrix.
- PCA would align with it regardless of correlation.

---

### Step 2: Compute the Covariance Matrix

$$C = \frac{1}{m} X_{scaled}^T X_{scaled}$$

Where:
- C is an n×n covariance matrix
- m = number of samples
- n = number of features

**Interpretation of Covariance Matrix:**
- **Positive values**: Strong positive relationship (when one increases, the other increases).
- **Negative values**: Inverse relationship.
- **Values close to zero**: Little or no relationship.

**Food Example Observations:**
- Calories & Fat: very strong positive correlation (0.999) → high calorie foods tend to be high in fat.
- Carbohydrates & Sugar: strong correlation (0.999) → high-carb foods often contain sugar.
- Protein has **negative** correlations with most features → high-protein foods less related to high-carb/fat foods.

> **Note on covariance matrix size**: The covariance matrix size is determined by the number of **features**, not the number of samples. A dataset with 5 attributes → 5×5 covariance matrix.

---

### Step 3: Compute Eigenvalues and Eigenvectors (Eigen Decomposition)

$$CW = \lambda W$$

Where:
- C = covariance matrix
- W = eigenvector matrix (each column is a principal component direction)
- λ = eigenvalues (how much variance each PC explains)

**Food Example:**
| PC Dir | Eigenvalue | Variance (%) |
|---|---|---|
| PC1 (Energy) | 4.530 | 75.49% |
| PC2 (Heart) | 1.470 | 24.50% |
| PC3 (Protein) | 0 | 0% |

**Eigenvectors (Feature Loadings):**
| Feature | PC1 | PC2 | PC3 |
|---|---|---|---|
| Calories | 0.4227 | 0.3601 | -0.466 |
| Carbohydrates | 0.44288 | -0.2755 | 0.53903 |
| Sugar | 0.43458 | -0.3135 | -0.5096 |
| Fat | 0.43303 | 0.32008 | 0.47912 |
| Sodium | 0.42967 | 0.33374 | -0.0483 |
| Protein | -0.2534 | 0.69448 | 0.02775 |

**Interpretation:**
- **PC1**: Strongly influenced by Calories, Carbs, Sugar, Fat, Sodium (all ≈ +0.43). Weak influence from Protein (−0.25). → Represents **energy density**.
- **PC2**: Strongly influenced by Protein (+0.69), negatively by Carbs and Sugar. → Represents **protein vs carb/sugar** contrast.
- **PC3**: Eigenvalue = 0 (no variance captured).

**Why only 2 non-zero eigenvalues?**
- Rank ≤ min(samples − 1, features) = min(3 − 1, 6) = min(2, 6) = 2
- Only 2 non-zero eigenvalues → remaining components have zero variance.
- Subtracting the mean removes one degree of freedom.

---

### Why Subtracting the Mean Removes One Degree of Freedom

If you have m numbers and center them:
$$\tilde{x}_i = x_i - \bar{x}$$

Then: $$\sum_{i=1}^{m} \tilde{x}_i = 0$$

The centered values must satisfy a constraint — if you know the first m−1 values, the last is determined automatically.

**Example**: x = [2, 4, 6] → mean = 4 → centered = [−2, 0, 2]
→ −2 + 0 + 2 = 0 ✓ (if you know −2 and 0, you know 2)

---

### Step 4: Compute Principal Components

$$\text{Principal Components} = X_{scaled} \times W_{eigenvectors}$$

Each row of 6 original features → converted to PC coordinates (PC1, PC2, PC3).

**Chicken PC1 Calculation:**
| Feature | Scaled | PC1 Weight | Product |
|---|---|---|---|
| Calories | -0.356 | 0.4227 | -0.151 |
| Carbs | -1.225 | 0.443 | -0.542 |
| Sugar | -1.258 | 0.435 | -0.547 |
| Fat | -0.429 | 0.433 | -0.186 |
| Sodium | -0.404 | 0.430 | -0.174 |
| Protein | 1.401 | -0.253 | -0.355 |
| **Sum PC1** | | | **-1.954** |

**Final PCA Results:**
| Food | PC1 | PC2 | PC3 |
|---|---|---|---|
| Chicken | -1.954 | 1.304 | ≈0 |
| Apple | -1.005 | -1.616 | ≈0 |
| Cake | 2.960 | 0.312 | ≈0 |

---

### Step 5: Analysis of Principal Components

- Each data point now has coordinates (PC1, PC2, PC3) instead of original features.
- **PC score** measures the alignment with a principal direction.
- **Large magnitude** = strong alignment.

**Interpretation:**
- Cake: High PC1 → energy-dense food.
- Chicken: High PC2 → protein-rich, low energy density.
- Apple: Negative scores on both PC1 and PC2.

---

# Part II: t-SNE (t-Distributed Stochastic Neighbor Embedding)

## Motivation
t-SNE is used for **dimensionality reduction and visualization** of high-dimensional data.

---

## t-SNE Intuition — Marble Bag

**Step 1**: Measure probabilities in the high-dimensional space (Marble Bag)
- Similar marbles (size, texture) → high probability of being neighbors.
- Far apart marbles → much lower probability.
- Uses a **Gaussian distribution** (bell curve) to convert distances to probabilities.

**Step 2**: Random 2D initialization — drop all marbles randomly on a flat table.

**Step 3**: Map high-dimensional space to 2D.

**Step 4**: Shift marbles by minimizing **KL divergence**:
- Close in bag but far on table → **pull together**.
- Far in bag but close on table → **push apart**.

**Step 5**: Marbles settle down — final visualization after gradient descent over multiple iterations.

---

## t-SNE Steps — Worked Example

**5 images, each 3×3 = 9-dimensional vector**

| | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 |
|---|---|---|---|---|---|---|---|---|---|
| Img1 | 102 | 179 | 92 | 14 | 106 | 71 | 188 | 20 | 102 |
| Img2 | 121 | 210 | 214 | 74 | 202 | 87 | 116 | 99 | 103 |
| Img3 | 151 | 130 | 149 | 52 | 1 | 87 | 235 | 157 | 37 |
| Img4 | 129 | 191 | 187 | 20 | 160 | 203 | 57 | 21 | 252 |
| Img5 | 235 | 88 | 48 | 218 | 58 | 254 | 169 | 255 | 219 |

---

### Step 1: Compute Pairwise Distances

t-SNE does not work with raw high-dimensional data — converts to **pairwise distances**.

**Img1 vs Img2 Distance:**
| | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 |
|---|---|---|---|---|---|---|---|---|---|
| Img1-Img2 | -19 | -31 | -122 | -60 | -96 | -16 | 72 | -79 | -1 |
| (Img1-Img2)² | 361 | 961 | 14884 | 3600 | 9216 | 256 | 5184 | 6241 | 1 |

Sum of Squares = 40,564 → Root = **201.41**

**Pairwise Distance Matrix:**
| | Img1 | Img2 | Img3 | Img4 | Img5 |
|---|---|---|---|---|---|
| Img1 | 0 | 201.75 | 214.43 | 264.45 | 417.84 |
| Img2 | 201.75 | 0 | 272.56 | 225.96 | 406.69 |
| Img3 | 214.43 | 272.56 | 0 | 376.58 | 353.27 |
| Img4 | 264.45 | 225.96 | 376.58 | 0 | 402.20 |
| Img5 | 417.84 | 406.69 | 353.27 | 402.20 | 0 |

---

### Step 2: Convert Distances to Probabilities

**Formula:**
$$P_{j|i} = \frac{\exp(-d_{ij}^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-d_{ik}^2 / 2\sigma_i^2)}$$

**What is Perplexity?**
| Perplexity | Effect | Dataset Size Recommendation |
|---|---|---|
| Low (~5-10) | Very local focus; may fragment global structure | Small (~100 points) |
| Medium (~30-50) | Balanced; preserves local and some global structure | Medium (~1000 points) |
| High (~100+) | Global focus; may lose fine details; large clusters blend | Large (~10,000+ points) |

**Worked Example (P₂|₁, assuming σ₁=100):**
- exp(−d₁₂² / 2σ₁²) = exp(−40703.99 / 20000) = exp(−2.035) ≈ 0.13065
- Sum of numerators (row 1) = 0.261474
- P₂|₁ = 0.13065 / 0.261474 = **0.4997** (~50% chance Img1 and Img2 are neighbors)

---

### Step 3: Generate Random 2D Coordinates

$$Y_i \sim N(0, 0.01)$$

Small random spread around zero; allows gradual movement during optimization.

---

### Step 4: Compute Q_ij (Low-Dimensional Similarities)

$$Q_{ij} = \frac{(1 + ||Y_i - Y_j||^2)^{-1}}{\sum_{k \neq l} (1 + ||Y_k - Y_l||^2)^{-1}}$$

Uses **Student's t-distribution** (heavier tails than Gaussian) for the low-dimensional space.

**Why t-distribution?** Prevents the "crowding problem" — moderate distances in high-D can map to very different distances in 2D.

---

### Step 5: Update 2D Positions via Gradient Descent

$$\frac{dX_i}{dt} = 4 \sum_{j \neq i} (P_{ij} - Q_{ij}) Q_{ij} (x_i - x_j)$$

**Interpretation:**
- The factor 4 comes from the derivative of KL divergence with Student's t-kernel.
- If **Pᵢⱼ > Qᵢⱼ**: Points should be closer → **pull together**.
- If **Pᵢⱼ < Qᵢⱼ**: Points should be further apart → **push apart**.
- **Multiplying by Qᵢⱼ**: If points already close, move them less (prevent overcorrections).
- **Multiplying by (xᵢ−xⱼ)**: Determines direction of movement; proportional to distance.

---

## PCA vs t-SNE

| Feature | PCA | t-SNE |
|---|---|---|
| Approach | Linear | Non-linear |
| Goal | Maximizes global variance | Preserves local similarity |
| Type | Deterministic | Stochastic |
| Axes | Interpretable (loadings) | No meaningful axes |
| Use Case | Compression, preprocessing | Visualization |

---

*End of INF2008 Machine Learning Notes*
