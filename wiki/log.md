---
type: meta
title: "Operation Log"
updated: 2026-05-11
tags: [meta, log]
---

# Operation Log

Chronological record of all vault operations. Append-only — never edit past entries. New entries go at the TOP.

---

## 2026-05-11 — Ingest: INF2008 Machine Learning

- Action: INGEST
- Source: `raw/INF2008 Machine Learning Notes.md` (Lectures L00–L12, Donny Soh)
- Created: `wiki/sources/INF2008-machine-learning.md`
- Created: 6 concept pages in `wiki/concepts/`
  - `ml-foundations` — AI definitions, four narrow-AI perspectives, expert systems vs ML, supervised/unsupervised/reinforcement learning, CRISP-DM phases mapped to production components, business understanding framework (problem/decision/metric/intervention/value), MoonHub churn and JuneBank loan examples
  - `ml-data-understanding` — 7 DU stages: data generation process, schema, data types (cardinal continuous/discrete vs categorical nominal/ordinal), completeness, sanity checks (plausibility, consistency, leakage), representativeness (class imbalance), granularity and aggregation
  - `ml-model-training-evaluation` — baseline models (majority class, mean, default DT), train-validate-test split, stratification (M&Ms analogy), k-fold cross-validation, confusion matrix, Type I/II errors, accuracy/balanced accuracy/precision/recall/specificity/F1, bias-variance trade-off (4 cases, corrective actions), learning curves
  - `decision-trees-and-ensembles` — Gini impurity formula and worked example, entropy, greedy tree construction, stopping criteria (max_depth, min_samples_split, min_samples_leaf), bagging/bootstrap sampling, Random Forests (OOB estimation: ~36.8% OOB, feature subsampling), AdaBoost, Gradient Boosting (loss gradients, iterative residual fitting, early stopping), stacking; comparison table
  - `neural-networks-linear-models` — label encoding vs OHE (advantages, dangers, when to use), simple and multiple linear regression, RMSE, 4-step gradient descent loop (forward pass, loss, backprop, update), vectorised multiple regression, neuron (z→σ→a), hidden activations (ReLU/Leaky ReLU/tanh), output activations (identity/sigmoid/softmax), backpropagation chain rule, cross-entropy loss, worked backprop example
  - `clustering-and-dimensionality-reduction` — distance measures (L1/L2/L∞), k-NN, K-means objective function (why the mean minimises it), K-means algorithm, elbow method, silhouette score, K-means++, DBSCAN (core/border/noise points, ε/MinPts effects), K-means vs DBSCAN comparison, PCA (5 steps: standardise, covariance matrix, eigendecomposition, project, interpret), t-SNE (Gaussian→t-distribution probabilities, KL divergence gradient descent, perplexity), PCA vs t-SNE comparison
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Ingest: ICT2216 Lectures 1 & 2

- Action: INGEST
- Sources: `raw/ICT2216 Lecture 1 Secure Software Development.md`, `raw/ICT2216 Lecture 2 Secure Software Development.md`
- Created: `wiki/concepts/owasp-top-10.md` — OWASP Top 10 (2025): all 10 categories with scenarios, code examples, case studies (Instagram, SolarWinds, Bybit, Log4Shell), mitigations, and vulnerability category taxonomy
- Created: `wiki/concepts/vulnerability-tracking-frameworks.md` — CVE, NVD, CAPEC, MITRE ATT&CK, CVSS; BSIMM-16 (goals, SSF domains, 2026 trends), OpenSAMM (maturity levels 0–3), Microsoft SDL; comparison table
- Updated: `wiki/concepts/secure-software-requirements.md` — added IEEE 729 definition, OSA taxonomy (4 requirement types), full SSDLC requirement process (feasibility → gathering → specification → validation), detailed CIA-AAA content (SingHealth case study, DDoS mitigations, SLA terminology, NIST 800-63 password guidelines), PCI SSF and NIST SSDF frameworks
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — added Secure Software Concepts section, linked new concept pages
- Updated: `wiki/index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Ingest: INF1004 Mathematics 2

- Action: INGEST
- Source: `raw/INF1004 Mathematics 2 Notes.md`
- Created: `wiki/sources/INF1004-mathematics-2.md`
- Created: 5 concept pages in `wiki/concepts/`
  - `descriptive-statistics` — types of data, population vs sample, measures of location (mean/median/mode), spread (variance, CV), relative standing (quartiles, boxplot)
  - `probability-theory` — classical/empirical/subjective probability, complement/union/intersection rules, conditional probability, independence vs mutual exclusivity, Bayes' theorem, law of total probability
  - `probability-distributions` — discrete RV (expected value, variance), binomial distribution, continuous distributions (uniform, normal, standard normal), combining independent RVs, sampling distribution, Central Limit Theorem (CLT), sampling methods
  - `linear-algebra-matrices` — matrix types and operations, determinants (2×2 and 3×3), inverse matrix (2×2 formula and Gauss-Jordan), SLE (Ax = b), vectors (magnitude, dot product, orthogonality), parametric line equations, 2D geometric transformations, linear regression (least squares)
  - `eigenvalues-and-svd` — characteristic equation, eigenvalue/eigenvector computation, diagonalisation ($A = PDP^{-1}$, $A^n = PD^nP^{-1}$), SVD ($A = U\Sigma V^T$), SVD computation steps, applications (image compression, PCA, recommender systems, pseudoinverse)
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 2 Example Page

- Action: INGEST
- Source: ICT2216 Lab 2 — SecurityRAT example page (lab PDF content confirmed by user)
- Created: `wiki/examples/ict2216-lab2-securityrat.md` — full compose files, step-by-step, CRLF fix, gotchas table, container architecture
- Updated: `wiki/examples/_index.md`, `wiki/index.md` — Lab 2 example entry added
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — Lab 2 example linked
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 1 Ingest

- Action: INGEST
- Source: ICT2216 Secure Software Development — Lab 1 (Docker + Docker Compose)
- Created: `wiki/concepts/docker-compose.md` — compose file structure, networking, volumes, all four services (Nginx, MySQL, Git, Selenium)
- Created: `wiki/examples/ict2216-lab1-docker-compose.md` — full compose files, build steps, port map, notes
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — added Lab 1, docker-compose concept, example page
- Updated: `wiki/examples/_index.md` — first entry added
- Updated: `wiki/index.md` — Concepts and Examples tables
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 2 Ingest

- Action: INGEST
- Source: ICT2216 Secure Software Development — Lab 2 (SecurityRAT + Secure Requirements)
- Created: `wiki/sources/ICT2216-secure-software-development.md`
- Created: `wiki/concepts/secure-software-requirements.md` — CIA + AAA pillars, risk identification, SANS SWAT / OWASP ASVS mapping
- Created: `wiki/resources/securityrat.md` — Docker setup, CRLF fix, default creds, container architecture
- Created: `wiki/learning/docker-windows-crlf.md` — Windows CRLF breaks Linux container scripts; Git Bash path translation gotcha
- Updated: `wiki/index.md` — Sources, Concepts, Learning, Resources tables
- Status: Complete

---

## 2026-05-11 — Ingest: INF1003 Mathematics 1

- Action: INGEST
- Source: `raw/INF1003 Mathematics 1 Notes.md`
- Created: `wiki/sources/INF1003-mathematics-1.md`
- Created: 5 concept pages in `wiki/concepts/`
  - `discrete-mathematics-foundations` — sequences (AP/GP/recurrence), number theory, modular arithmetic, GCD/LCM, Euclidean algorithm, RSA
  - `combinatorics` — product/sum/division rules, permutations, combinations, pigeonhole principle
  - `propositional-logic` — connectives, truth tables, tautologies, De Morgan's laws, logical equivalences
  - `predicate-logic-and-proofs` — quantifiers (∀/∃), negation rules, rules of inference (modus ponens/tollens etc.), proof methods
  - `sets-functions-relations` — set operations/identities, power sets, function types (injective/surjective/bijective), relation properties, equivalence relations, partial orders
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Structure Update & Writing Style

- Action: CONFIGURE
- Graph view: 13 colour groups applied to `graph.json` — each wiki folder now maps to its vault colour (blue = concepts/synthesis, green = sources, purple = examples/entities, gold = areas, teal = goals/learning, orange = resources, red = gaps, steel-blue = meta, grey = raw/templates)
- vault-colors.css: Added `wiki/examples` → purple nav colour
- CLAUDE.md: Added Writing Style section (British English, grammatically correct prose)
- CLAUDE.md: Updated Vault Structure diagram to include all subfolders
- wiki/examples/: Created folder with `_index.md` — for real-world examples and lab sessions
- wiki/index.md: Added Examples table section
- Status: Complete

---

## 2026-05-11 — First Ingest: 5 Course Notes

- Action: INGEST
- Sources: ICT2113, INF1008, INF1009, INF2007, INF2002
- Created: 5 source index pages in wiki/sources/
- Created: 12 concept pages in wiki/concepts/
  - requirements-engineering, lightweight-rcm (ICT2113)
  - algorithm-complexity, data-structures-fundamentals, sorting-and-searching, graph-algorithms (INF1008)
  - oop-four-pillars, solid-and-design-patterns (INF1009)
  - android-architecture, kotlin-coroutines (INF2007)
  - hci-fundamentals, needfinding-and-task-analysis (INF2002)
- Updated: wiki/index.md (Sources + Concepts tables), wiki/hot.md, raw/.manifest.json
- Status: Complete — vault ready for study/review use

---

## 2026-05-11 — Vault Scaffold

- Action: SCAFFOLD
- Mode: D (Personal / Second Brain) + E (Research)
- Purpose: Personal knowledge base for everything learned and to learn, linking knowledge, filling gaps
- Created: wiki/ structure with 9 domain folders + 4 meta files
- Created: Mode D+E templates (goal, learning, synthesis, gap)
- Applied: vault-colors.css visual customization
- Status: Ready for first ingest
