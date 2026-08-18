# International Summer School: Trustworthy AI – Machine Learning Meets Blockchain

**Microcredential 2: Machine Learning**
**Part 2b: Machine Learning – Classification Models**

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

*International Summer School 2026 | Machine Learning*

---

## Slide 2: Machine Learning – Classification Models

(Title slide with illustrative figures: an image grid of cats and dogs plotted by "Size" vs. "Length of the snout"; a convolutional neural network architecture diagram; and a diagram of a single artificial neuron showing inputs, weights, bias, and activation function producing output ŷ.)

Neuron diagram formula:

```
z = Σ (p=1 to k) w_p · x_i,p + b
ŷ = a(z)
```

Where:
- Inputs: x_i,1 ... x_i,k
- Weights: w_1 ... w_k
- Bias: b
- Activation function: a(z)
- Output: ŷ

---

## Slide 3: k-Nearest Neighbors (kNN)

**Machine Learning – Class. Models & Evaluation**

- Supervised learning algorithm used for classification and regression
- Makes predictions based on the k most similar training samples
- Similarity is usually measured using a distance metric (e.g., Euclidean distance)
- For classification, the predicted class is determined by majority voting among the k neighbors
- For regression, the prediction is typically the average value of the k nearest neighbors

*(Figure: three scatter plots illustrating kNN — a target point among Class 1 (green) and Class 2 (red) points; lines connecting the target to its neighbors; and a circle showing the k nearest neighbors used for the majority vote.)*

Source: https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbours/

---

## Slide 4: k-Nearest Neighbors (kNN) — Advantages & Disadvantages

**Machine Learning – Class. Models & Evaluation**

### Advantages
- **Simple and intuitive** – easy to understand and implement
- **No training phase** – the model simply stores the training data
- **Flexible** – works for both classification and regression and can adapt to complex decision boundaries

### Disadvantages
- **Computationally expensive at prediction time** because distances to many samples must be computed.
- **Sensitive to feature scaling** – features usually need normalization or standardization.
- **Performance degrades in high-dimensional data** due to the curse of dimensionality.

---

## Slide 5: Support Vector Machines (SVMs)

**Machine Learning – Class. Models & Evaluation**

- Supervised learning algorithm used for classification and regression tasks
- Finds the **optimal hyperplane** that **maximizes the margin** between different classes
- Uses **support vectors** (critical training samples) that define the decision boundary
- Can handle **non-linear decision boundaries** using the kernel trick (e.g., RBF, polynomial kernels)
- Effective in **high-dimensional spaces** and when the number of features is large

*(Figure: mapping φ from Input Space to Feature Space illustrating separation of two classes.)*

Source: https://medium.com/data-science/the-kernel-trick-c98cdbcaeb3f

---

## Slide 6: SVMs — Margin and Support Vectors

**Machine Learning – Class. Models & Evaluation**

*(Figure: two scatter plots of linearly separable classes (blue and pink) with X1/X2 axes. Left plot shows multiple candidate separating lines; right plot shows the maximum-margin hyperplane with dashed margin boundaries and highlighted support vectors.)*

- Example dataset showing classes that can be linearly separated
- Maximize the *margin*, i.e., the distance separating the closest pair of data points belonging to opposite classes
- These points are the *support vectors* → support the resulting hyperplane

Source: https://medium.com/data-science/the-kernel-trick-c98cdbcaeb3f

---

## Slide 7: SVMs — Kernel Trick Example (Quadratic Transformation)

**Machine Learning – Class. Models & Evaluation**

*(Figure: 1D data points (blue squares and orange circles) on a number line that are not linearly separable; after a quadratic transformation, the same points become separable in 2D by a horizontal dashed red line.)*

→ The data becomes linearly separable after a quadratic transformation to 2-dimensions.

Source: https://medium.com/data-science/the-kernel-trick-c98cdbcaeb3f

---

## Slide 8: SVMs — Kernel Trick Example (Modulo Transformation)

**Machine Learning – Class. Models & Evaluation**

*(Figure: 1D data points along X1 (0 to 20) that mix even (blue squares) and odd (orange circles) values, not separable on the line; after transformation, plotted with X2 = φ(x) = x mod 2, the even and odd values separate into two rows.)*

→ This transformation φ(x) = x mod 2 allows to linearly separate the even and odd X1 values in 2 dimensions.

Source: https://medium.com/data-science/the-kernel-trick-c98cdbcaeb3f

---

## Slide 9: SVMs — Second-Degree Polynomial Mapping

**Machine Learning – Class. Models & Evaluation**

*(Figure: left — 2D scatter plot of two concentric circular clusters (blue ring, orange center) that are not linearly separable in 2D; right — 3D scatter plot after polynomial transformation showing the classes now linearly separable by a plane.)*

Equation 5-8. Second-degree polynomial mapping:

```
φ(x) = φ([x1, x2]) = [x1², √2·x1·x2, x2²]
```

→ After applying this transformation:
→ Linearly separable data in 3-d after applying the 2nd-degree polynomial transformation

Source: https://medium.com/data-science/the-kernel-trick-c98cdbcaeb3f

---

## Slide 10: SVMs — SVM Parameter C

**Machine Learning – Class. Models & Evaluation**

*(Figure: two scatter plots (red vs. blue points) with separating margins, comparing C = 1 (wider margin) vs. C = 100 (narrower margin, fewer margin violations).)*

- **Slack variables (ξᵢ)** allow some points to be misclassified or within the margin
- Enable **soft-margin SVMs** for non-linearly separable data
- **C parameter** controls the trade-off between margin size and classification errors
- **Large C** → fewer misclassifications, smaller margin → stricter classifier
- **Small C** → larger margin, more tolerance for errors → more generalization

Source: https://medium.com/data-science/the-kernel-trick-c98cdbcaeb3f

---

## Slide 11: SVMs — High-Dimensional Space Trade-offs

**Machine Learning – Class. Models & Evaluation**

- **Transformation in high-dimensional space:**
  - **High computational cost** due to creating and storing large feature vectors
  - **Memory-intensive**, especially for very high-dimensional spaces
  - **Slower training and prediction**, because all operations are done in the full high-dimensional space
  - **Hard to scale** to large datasets or complex kernels
  - **Numerical instability** can occur when working with very large or sparse feature vectors

Source: https://medium.com/data-science/the-kernel-trick-c98cdbcaeb3f

---

## Slide 12: SVMs — Kernel Trick Explained

**Machine Learning – Class. Models & Evaluation**

- **Kernel trick:**
  - Maps data **implicitly** into a higher-dimensional space without computing new coordinates
  - Uses a **kernel function** to compute the inner product between two points in the high-dimensional space directly
  - Avoids the **computational cost** of explicitly creating and storing high-dimensional feature vectors
  - Enables SVM to **find linear separation** in the high-dimensional space while working with the original low-dimensional data
  - Supports **non-linear decision boundaries** efficiently through mathematical shortcuts provided by the kernel function

---

## Slide 13: SVMs — Advantages & Disadvantages

**Machine Learning – Class. Models & Evaluation**

### Advantages
- Works well in high-dimensional feature spaces
- Robust to overfitting due to margin maximization
- Can model complex non-linear relationships using kernel functions

### Disadvantages
- Training can be slow for very large datasets
- Choice of kernel and hyperparameters can strongly affect performance
- Less interpretable compared to simpler models like decision trees

---

## Slide 14: Decision Trees

**Machine Learning – Class. Models & Evaluation**

- Suitable for regression and classification
- Directed, acyclic graph (DAG)
- Follow a path from the root to a leaf through the tree
- **Terminology:**
  - **Nodes:** Tests on variables / features
  - **Edges:** Outcomes of the test
  - **Leaves:** Regression / classification results

→ Exactly one root node, with no incoming edges

---

## Slide 15: Decision Trees — Example Dataset

**Machine Learning – Class. Models & Evaluation**

**Example Dataset:**

| Weather | Temperature | Humidity | Wind   | Played? |
|---------|--------------|----------|--------|---------|
| Sunny   | Hot          | High     | Weak   | No      |
| Sunny   | Hot          | High     | Strong | No      |
| Cloudy  | Hot          | High     | Weak   | Yes     |
| Rainy   | Mild         | High     | Weak   | Yes     |
| Rainy   | Cool         | Normal   | Weak   | Yes     |
| Rainy   | Cool         | Normal   | Strong | No      |
| Cloudy  | Cool         | Normal   | Strong | Yes     |
| Sunny   | Mild         | High     | Weak   | No      |
| Sunny   | Cool         | Normal   | Weak   | Yes     |
| Rainy   | Mild         | Normal   | Weak   | Yes     |
| Sunny   | Mild         | Normal   | Strong | Yes     |
| Cloudy  | Mild         | High     | Strong | Yes     |
| Cloudy  | Hot          | Normal   | Weak   | Yes     |
| Rainy   | Mild         | High     | Strong | No      |

→ **Question:** What conditions influence the decision to play golf?

Based on: https://www-cbi.cs.uni-saarland.de/wp-content/uploads/SWW-WS2021/SW-V12-Klassifikation.pdf

---

## Slide 16: Decision Trees — Possible Result

**Machine Learning – Class. Models & Evaluation**

- The tree could have the following structure
  → How can the creation be automated?

```
                    Weather
          Sunny  /    |    \  Rainy
                /   Cloudy   \
        Temperature   Yes    Wind
       Cool Mild Hot        Weak  Strong
        No  Yes  No          Yes    No
```

---

## Slide 17: Decision Trees — ID3-Algorithm

**Machine Learning – Class. Models & Evaluation**

- Greedy algorithm
- Make the best decision locally
- **Target:** Reduce entropy after splits
- Iteratively select the "best" feature for each node
- Start: Select the best feature for the root node

→ How is the best feature determined?

---

## Slide 18: Decision Trees — ID3-Algorithm (Information Gain)

**Machine Learning – Class. Models & Evaluation**

- Criterion for determining which feature is best suited for the next split:
- *Maximize* information gain I(Sʲ, θ)
- *Minimize* Entropy H(Sʲ) in the remaining subsets Sᵢ

```
I(Sʲ, θ) = H(Sʲ) − Σ (i=1 to k) [ |Sᵢʲ| / |Sʲ| · H(Sᵢʲ) ]
```

Where:
- Sʲ: Dataset at split nr. j
- θ: Currently viewed feature
- H(Sʲ): Entropy in dataset / split
- Sᵢʲ: Subset of Sʲ, for that θ has value i
- |Sⱼ|: Cardinality of Sⱼ
- |Sᵢʲ|: Cardinality of Sᵢʲ

(Information value before split → H(Sʲ); Information value after split → the summation term)

---

## Slide 19: Decision Trees — ID3-Algorithm (Entropy)

**Machine Learning – Class. Models & Evaluation**

- Entropy: Measure of information content
- *Maximum*, if the relative frequency p(c) is the same in all categories
- *Minimal*, if the relative frequency p(c) of a category is equal to 1

```
H(Sʲ) = − Σ (c∈C) p(c) log(p(c))

I(Sʲ, θ) = H(Sʲ) − Σ (i=1 to k) [ |Sᵢʲ| / |Sʲ| · H(Sᵢʲ) ]
```

Where:
- Sʲ: Dataset at split nr. j
- C: Number of categories
- p(c): Relative frequency of instances belonging to category c

---

## Slide 20: Decision Trees — Weather Example: Determining the Root Node (1)

**Machine Learning – Class. Models & Evaluation**

- Identify feature with maximum information gain I(Sʲ, θ):

```
I(Sʲ, θ) = H(Sʲ) − Σ (i=1 to k) [ |Sᵢʲ| / |Sʲ| · H(Sᵢʲ) ] ,     H(Sʲ) = − Σ (c∈C) p(c) log(p(c))
```

Total entropy H(S¹) is determined by 14 instances: 9 x "Yes", 5 x "No":

```
H(S¹) = − (9/14) log(9/14) − (5/14) log(5/14) = 0.940286
```

There are 8 instances of the event "Wind = Weak", 6 were played, 2 were not:

```
H(S¹_Weak) = − (6/8) log(6/8) − (2/8) log(2/8) = 0.8112781
```

There are 6 instances of the event "Wind = Strong", 3 were played, 3 were not:

```
H(S¹_Strong) = − (3/6) log(3/6) − (3/6) log(3/6) = 1.0
```

---

## Slide 21: Decision Trees — Weather Example: Determining the Root Node (2)

**Machine Learning – Class. Models & Evaluation**

The total entropy and the entropy for the two events "wind = weak/strong" result in:

```
I(S¹, Wind) = H(S¹) − (|S¹_Weak|/|S¹|) · H(S¹_Weak) − (|S¹_Strong|/|S¹|) · H(S¹_Strong)

           = 0.940286 − (8/14) · 0.8112781 − (6/14) · 1

           = 0.04812709
```

---

## Slide 22: Decision Trees — Weather Example: Determining the Root Node (3)

**Machine Learning – Class. Models & Evaluation**

Similarly, for the other characteristics, the following applies:

```
I(S¹, Weather)     = 0.247
I(S¹, Temperature) = 0.029
I(S¹, Humidity)    = 0.152
```

→ The "weather" feature therefore provides the greatest gain in information
→ "Weather" is selected as the tree root

---

## Slide 23: Decision Trees — Weather Example: Determining the Root Node (4)

**Machine Learning – Class. Models & Evaluation**

- The tree with root node "Weather" looks like this:

```
                       Weather
        Sunny    /       |        \    Rainy
                /      Cloudy       \
    [Yes,Yes,No,No,No]  [Yes,Yes,Yes,Yes]  [Yes,Yes,Yes,No,No]
```

→ Apply the procedure recursively to each of the 3 attributes, with the corresponding subset of events

---

## Slide 24: Decision Trees — Recursion for Attributes

**Machine Learning – Class. Models & Evaluation**

Three sub-trees explored for the "Sunny" branch:

```
Weather --Sunny--> Wind    --Weak-->   [Yes, No, No]
                            --Strong--> [Yes, No]

Weather --Sunny--> Humidity --High-->   [No, No, No]
                             --Normal--> [Yes, Yes]

Weather --Sunny--> Temperature --Hot-->  [No, No]
                                --Mild--> [Yes, No]
                                --Cool--> [Yes]
```

```
I(S², Wind)        = 0.020
I(S², Humidity)    = 0.971   ← selected (highest gain, boxed in original)
I(S², Temperature) = 0.571
```

---

## Slide 25: Decision Trees — Final Tree

**Machine Learning – Class. Models & Evaluation**

```
                              Weather
             Sunny    /         |          \    Rainy
                     /        Cloudy         \
              Humidity     [Yes,Yes,Yes,Yes]   Windy
          High /    \ Normal              Weak /    \ Strong
     [No,No,No]    [Yes,Yes]            [Yes,Yes,Yes]  [No,No]
```

→ Observation: All instances are classified equally in each leaf (entropy = 0)
→ The "temperature" attribute was not used
→ Due to its greedy property, the ID3 algorithm does not guarantee the best tree

---

## Slide 26: Gini Index

**Machine Learning – Class. Models & Evaluation**

```
G = Σ (i=1 to C) p(i) · (1 − p(i))
```

- C: Number of classes in the subset of the dataset
- i: selected class out of C

- Gini Impurity is the probability of *incorrectly* classifying a randomly chosen element in the dataset if it were randomly labeled *according to the class distribution* in the dataset
- Gini is faster than Entropy → no logarithmic operations
- Gini isolates the most frequent classes earlier
- Gini produces purer child nodes faster
- → Often used as default in popular ML-libraries, e.g., scikit-learn

---

## Slide 27–31: Decision Trees — ID3 vs. CART Comparison Table

**Machine Learning – Class. Models & Evaluation**

| ID3 | CART |
|---|---|
| **Categorical only** – Cannot handle numerical features without manual preprocessing | **Categorical & numerical** – Handles both data types natively out of the box |
| **Multi-way splits** – Creates one branch per distinct attribute value | **Binary splits only** – Every node is always split into exactly two children |
| **No feature reuse** – Each feature can only appear once per root-to-leaf path | **Feature reuse** – The same feature can appear multiple times on one path |
| **Entropy only** – Information gain is the sole split criterion | **Entropy or Gini** – The split criterion can be freely chosen per use case |
| **No pruning** – Grows until pure, which often leads to overfitting | **Built-in pruning** – Cost-complexity pruning actively reduces overfitting |

*(This table was built up progressively across slides 27–31, each slide adding one more row.)*

---

## Slide 32: Decision Trees — Limitations

**Machine Learning – Class. Models & Evaluation**

- Tends to overfit training data, especially with deep trees
- **High variance** – small changes in data can produce a very different tree
- **Unstable predictions** when the dataset changes slightly
- Uses **all training data and features**, which can lead to biased splits
- Performance depends on **one single model**

---

## Slide 33: Random Forests — Bagging

**Machine Learning – Class. Models & Evaluation**

*(Figure: Original Data → split into multiple Bootstrapping samples → each fed into a Classifier (Aggregating) → combined into an Ensemble classifier (Bagging).)*

- **Bootstrap Aggregating (Bagging):**
  - Extends one model to multiple models
  - Sample B bootstrap-samples from dataset
  - Apply ML algorithm for each bootstrap-sample
  - Aggregate results

---

## Slide 34: Random Forests — Ensemble of Decision Trees

**Machine Learning – Class. Models & Evaluation**

*(Figure: Dataset → Decision Tree (1), Decision Tree (2), Decision Tree (3), ... → Result (1), Result (2), Result (3) → Majority Voting/Averaging → Final Result = Random Forest.)*

- **Random Forests:**
  - Ensemble of Decision Trees
  - Combine predictions from different models
  - Additionally to bagging: Choose a subset m of all p features at each node
  - *Target:* Increase robustness, avoid overfitting

---

## Slide 35: Random Forests — Properties

**Machine Learning – Class. Models & Evaluation**

- **Reduces overfitting** by averaging many trees
- **Lower variance** due to aggregation of many models
- **More stable predictions** because errors average out
- Uses **bootstrap samples and random feature subsets**, increasing diversity
- Combines **many trees (ensemble)** → usually higher accuracy

---

## Slide 36: Jupyter Notebooks

- 01_Decision_Tree_ID3.ipynb
- 02_Decision_Tree_CART.ipynb
- 03_ML_Classifiers_Tutorial.ipynb

---

## Slide 37: Contact

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
