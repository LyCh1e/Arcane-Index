---
address: c-000064
type: concept
status: established
title: "AI Ethics and the Digital Society"
domain: it-ethics
source: INF1007
complexity: high
tags: [it-ethics, ai-ethics, automation, digital-divide, bias, transparency, accountability, tinyml, inf1007]
---

# AI Ethics and the Digital Society

## Work and Wealth in the Information Age

### IT and Automation

**Automation** — the use of technology to perform tasks previously done by humans.

**Historical context:** Automation is not new. The industrial revolution mechanised physical labour. The information revolution is now automating *cognitive* tasks as well.

**Effects of automation on employment:**
- Some jobs are **eliminated** as machines perform them more cheaply.
- New jobs are **created** in designing, building, and maintaining automated systems.
- Remaining jobs **change** — requiring higher-level skills and greater adaptability.

---

### The Digital Divide

The **digital divide** refers to the gap between people who have effective access to digital and information technology, and those who have limited or no access.

**Dimensions:**

| Dimension | Description |
|-----------|-------------|
| **Device access** | Access to computers and smartphones |
| **Connectivity** | Access to internet infrastructure |
| **Digital literacy** | Ability to use technology effectively |

**Who is affected?**
- **Geographic divide** — urban vs. rural populations.
- **Economic divide** — wealthy vs. poor individuals.
- **Age divide** — younger vs. older generations.
- **Global divide** — developed vs. developing nations.

**Ethical implications:** The digital divide raises concerns about **fairness and equality of opportunity** — those without digital access are increasingly disadvantaged in education, employment, and civic participation. Social Contract Theory suggests rational people would agree to policies that address this gap (Rawls' difference principle: inequalities must benefit the least advantaged).

---

### Globalisation and Outsourcing

IT has enabled the integration of economies globally and made it far easier to **outsource** work to lower-cost locations.

**Arguments for outsourcing:**
- Reduces costs, making goods and services cheaper for consumers.
- Allows companies to focus on core competencies.
- Provides employment opportunities in developing countries.

**Arguments against outsourcing:**
- Displaces workers in higher-cost countries.
- Can lead to exploitation of workers in countries with weaker labour protections.
- May undermine local communities and social cohesion.

---

## AI Categorisation

| Category | Description | Current Status |
|----------|-------------|---------------|
| **Weak AI (Narrow AI)** | Designed and trained for a specific task; no general reasoning abilities beyond that domain | Exists today |
| **Strong AI (AGI)** | Can perform any intellectual task a human can; has general reasoning abilities | Hypothetical |
| **Superintelligence** | Surpasses human intelligence in virtually all domains | Hypothetical |

*Examples of Weak AI:* Speech recognition (Siri, Alexa), image classification, recommendation systems, medical diagnosis tools.

---

## Ethical Concerns of AI Use

### Bias and Fairness

AI systems can exhibit and **amplify** biases present in training data.

**Examples:**
- Facial recognition systems with higher error rates for certain demographic groups.
- Hiring algorithms that discriminate against applicants from particular backgrounds.
- Criminal recidivism prediction tools that are biased against minority defendants.

**Why this matters:** Biased AI systems produce unjust real-world consequences — denied loans, wrongful imprisonment, missed medical diagnoses.

**Ethical analysis:**
- **Kantian:** A biased AI treats affected individuals as less worthy of accurate assessment — a failure to respect persons equally, using them merely as means.
- **Utilitarian:** Biased AI increases overall unhappiness by producing systematically unjust outcomes, particularly for already-disadvantaged groups.
- **Social Contract:** People would not agree to systems that systematically disadvantage them.

---

### Misuse of AI

AI can be deliberately misused:

| Misuse | Description |
|--------|-------------|
| **Deepfakes** | AI-generated synthetic media (images, video, audio) used to impersonate real people — e.g., scammers impersonating relatives to extort money |
| **Disinformation** | AI-generated content used to spread false information at scale |
| **Surveillance** | AI-powered surveillance used by authoritarian governments to monitor and control populations |
| **Autonomous weapons** | AI systems that can select and engage targets without human intervention |

---

### Accountability and Transparency

**When an AI system causes harm, who is responsible?**
- The developer of the AI model?
- The organisation that deployed it?
- The individual user who applied it?

The **opacity** ("black box" nature) of many AI systems — especially deep learning — makes it difficult to understand why a particular decision was made, complicating accountability.

**Explainability:** The ability to explain in human-understandable terms why an AI system made a particular decision. Increasingly treated as an ethical requirement in high-stakes domains (healthcare, criminal justice, lending).

---

### Privacy

AI systems often require large amounts of personal data:
- Data may be collected and used without individuals' knowledge or meaningful consent.
- **Inference attacks** — using AI to infer sensitive attributes (health conditions, political views) from seemingly innocuous data.
- Computer vision and audio AI capabilities enable novel forms of surveillance.

---

### Job Displacement

AI-powered automation threatens to displace significant numbers of workers across many industries.

**Counter-argument:** Technology has historically created new types of jobs while eliminating old ones; the long-term net effect may be positive.

**Concern:** The transition may be severely disruptive. Displaced workers may lack the skills required for newly created jobs, producing structural unemployment and increased inequality — particularly for less-educated workers.

---

## Principles for Ethical AI

Several organisations and governments have proposed AI ethics principles. Common themes:

| Principle | Description |
|-----------|-------------|
| **Fairness** | AI should treat people fairly and without discrimination |
| **Transparency** | People should understand how AI systems make decisions that affect them |
| **Accountability** | Clear lines of responsibility must exist for AI systems and their outcomes |
| **Privacy** | AI systems must respect individuals' privacy rights |
| **Safety and Security** | AI systems must be safe, reliable, and resistant to attack |
| **Human oversight** | Humans must remain in meaningful control of AI systems, especially in high-stakes applications |

---

## Ethical Frameworks Applied to AI

| Framework | Analysis |
|-----------|---------|
| **Kantianism** | AI systems that make decisions without transparency or appeal treat individuals merely as data objects rather than rational agents with rights; AI must respect human autonomy and dignity |
| **Act Utilitarianism** | AI can produce enormous benefits (improved healthcare, resource allocation, personalised education) but if harms are concentrated on vulnerable groups, the calculus may not justify deployment; all affected parties must be counted |
| **Social Contract** | People would agree to AI use subject to proper oversight, accountability, and fairness; they would not agree to AI systems that systematically disadvantage them or operate without transparency |
| **Virtue Ethics** | AI developers and deployers should cultivate virtues of honesty, responsibility, and care; asks "What would a responsible, virtuous engineer or organisation do?" |

---

## The Information Age — Technology and Society

Technology has a dynamic, bidirectional relationship with society:
- People create and adopt technology.
- Once adopted, technology changes society and changes people (neurologically, psychologically, socially).

**Technologies solve problems but create new ones:**

| Technology | Benefit | New Problem |
|-----------|---------|-------------|
| Automobiles | Greater mobility | Traffic congestion, pollution |
| The Web | Valuable information retrieval | Children exposed to harmful content |
| Low-cost international communication | Global news and entertainment access | Outsourcing, job displacement |
| Mechanical calculators | Faster computation | De-skilling of bookkeepers |

**IT professionals** have a special responsibility: they create the future. The core question is *how to ensure IT is used to bring benefits and do no harm to users and society.*

---

## Connections

- [[concepts/ethical-frameworks|Ethical Frameworks]] — provides the normative grounding for AI ethics analysis
- [[concepts/embedded-sensor-fusion-and-edge|Sensor Fusion and Edge Computing]] — TinyML is the embedded implementation of AI at the edge
- [[concepts/ml-foundations|Machine Learning Foundations]] — technical underpinning of AI systems
- [[concepts/clustering-and-dimensionality-reduction|Clustering & Dimensionality Reduction]] — unsupervised learning that can produce opaque, unaccountable outputs
- [[concepts/privacy-data-protection-and-ip|Privacy, Data Protection, and IP]] — AI privacy concerns share the same PDPA obligations
- [[concepts/wireless-and-iot|Wireless Networking & IoT]] — IoT data feeds AI surveillance systems
