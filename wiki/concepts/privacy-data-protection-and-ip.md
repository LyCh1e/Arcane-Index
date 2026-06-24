---
address: c-000063
type: concept
status: established
title: "Privacy, Data Protection, and Intellectual Property"
domain: it-ethics
source: INF1007
complexity: high
tags: [it-ethics, privacy, pdpa, data-protection, intellectual-property, copyright, hacker-ethics, inf1007]
---

# Privacy, Data Protection, and Intellectual Property

## Privacy

### What Is Privacy?

**Privacy** is a value that relates to the right of people to **control information about themselves**, and to be let alone.

Privacy must be balanced against competing values:
- **Transparency** — accountability for those in positions of power.
- **Public safety** — preventing harm to others.
- **Accountability** — legal and professional obligations.

This balance requires judgement; there is no single correct answer for all situations.

### Why Privacy Matters

- Privacy enables individuals to develop their identities and personalities without external interference.
- Privacy protects individuals from exploitation and manipulation.
- Privacy is necessary for freedom — the ability to act without constant surveillance or social pressure.

### Threats to Privacy

Modern technology has created significant new threats:

| Threat | Description |
|--------|-------------|
| **Data collection and aggregation** | Large amounts of personal data collected by organisations and combined to create detailed profiles |
| **Surveillance** | CCTV, location tracking, monitoring of digital communications |
| **Data breaches** | Unauthorised access to personal information |
| **Social media** | Voluntary sharing of data that can be used in unexpected or harmful ways |

**Examples of misuse:** unsolicited marketing without consent; sharing personal data to third parties without consent; location tracking without consent.

---

## Personal Data and PII

**Personal data** — any information that relates to an identified or identifiable individual.

**Personally Identifiable Information (PII)** — data that can be used to directly identify or link to an individual:
- Full name
- NRIC, FIN, or passport number
- Driver's licence number
- Personal email address or mobile phone number
- Photographs

---

## Singapore's Personal Data Protection Act (PDPA)

The **PDPA** governs the collection, use, disclosure, and care of personal data by organisations in Singapore.

### Key Obligations

| Obligation | Requirement |
|------------|-------------|
| **Consent** | Obtain informed, specific, voluntary consent before collecting, using, or disclosing personal data |
| **Notification** | Inform individuals of the purposes for which their data is collected, used, or disclosed |
| **Purpose Limitation** | Collect, use, or disclose data only for the notified purposes for which consent was obtained; new purpose requires fresh consent |
| **Access and Correction** | Individuals have the right to access and correct their personal data |
| **Accuracy** | Make reasonable efforts to ensure personal data is accurate and complete |
| **Protection** | Implement reasonable security arrangements to protect data from unauthorised access, modification, or disposal |
| **Retention Limitation** | Do not retain personal data longer than necessary for its purpose |
| **Transfer Limitation** | Do not transfer personal data outside Singapore without adequate protections |

---

## Privacy and the Government

### Government-Held Personal Data

Governments collect vast amounts of personal data: national ID cards, tax returns, motor vehicle records, HR records, education and qualifications, travel data, social welfare data, criminal records, health data.

### Culture and Privacy

Privacy expectations vary by cultural orientation:

| Individualistic Culture | Collectivist Culture |
|------------------------|---------------------|
| Personal-emphasised | Social-emphasised |
| Encourages self-expression | Emphasises group harmony |
| Higher value placed on individual privacy | More acceptance of state access to personal data for collective good |

### The Privacy vs. Security Tension

Post-9/11, governments introduced sweeping surveillance powers in the name of counterterrorism. The ethical tension:

**Supporting surveillance (Utilitarian):** Preventing mass casualties may justify limited privacy intrusions. Most law-abiding citizens rarely feel direct intrusion.

**Opposing surveillance:**
- **Kantian:** Using citizens as instruments of the state without consent treats them merely as means, violating their dignity.
- **Social Contract:** Citizens would not agree to comprehensive surveillance if they knew the full terms; it undermines the trust that the social contract depends on.
- Surveillance infrastructure can be captured and used by authoritarian regimes.
- **Chilling effect** — knowledge of being surveilled causes people to self-censor, suppressing free speech and association.

### Ethical Frameworks Applied to Privacy

| Framework | Position |
|-----------|---------|
| **Kantianism** | Privacy must be respected; using people merely as data points without their consent violates the 2nd formulation of the categorical imperative |
| **Utilitarianism** | Privacy protections may be justified on balance; societal benefits from targeted interventions must be weighed against harm of exposing individuals to exploitation |
| **Social Contract** | Rational individuals would agree to privacy protections in the social contract — no one wants their private information misused |
| **Virtue Ethics** | Respecting privacy is a matter of honesty, respect, and integrity — virtues expected of IT professionals handling personal data |

---

## Information Security — Ethical Dimensions

*(Technical details of the CIA Triad covered in [[concepts/secure-software-requirements|Secure Software Requirements]].)*

### Malware Types

| Type | Description |
|------|-------------|
| **Virus** | Attaches itself to a legitimate file; spreads when the file is executed |
| **Worm** | Self-replicating programme that spreads across networks without needing to attach to a file |
| **Trojan horse** | Appears legitimate but contains malicious code |
| **Ransomware** | Encrypts victim's files and demands payment for the decryption key |
| **Spyware** | Secretly monitors user activity and transmits data to a third party |
| **Adware** | Automatically displays or downloads advertising material |

### Hacker Ethics

**The Hacker Ethic** originated in the hacking community and is built around:
- Information should be free and accessible.
- Code, knowledge, and resources should be shared widely.
- Computing should be a decentralised tool for freedom.

**Conflict with Professional Codes of Ethics:**

| Hacker Ethic Tenet | Professional Code Conflict |
|--------------------|---------------------------|
| Break into systems to expose vulnerabilities | Violates ACM 2.8: access resources only when *authorised* |
| Share copyrighted materials on P2P networks | Violates ACM 1.5: respect the work required to produce creative works |

**Ethical analysis of hacking:**
- **Kantian:** Unauthorised access treats the system owner as a means — using their resources without consent.
- **Rule Utilitarian:** A rule permitting unauthorised access, if universalised, would produce net harm — regardless of whether any individual instance appeared beneficial.

---

## Intellectual Property (IP)

**Intellectual Property** refers to creations of the mind — inventions, literary and artistic works, designs, symbols, names, and images.

IP is an **intangible asset** — non-physical but economically valuable.

### Types of IP Protection

| Type | What It Protects | Registration | Duration |
|------|-----------------|-------------|----------|
| **Copyright** | Original creative works (literature, music, software, films) | Automatic — no registration required | Life of author + 70 years (varies by jurisdiction) |
| **Patent** | Inventions and innovations — exclusive rights to make, use, and sell | Yes | ~20 years |
| **Trademark** | Brand identifiers — names, logos, slogans | Yes | Renewable indefinitely |
| **Trade Secret** | Confidential proprietary information providing competitive advantage | No — protected via NDAs/contracts | No time limit (while secrecy maintained) |
| **Registered Design** | Visual appearance of a product | Yes | Varies |
| **Geographical Indication** | Names/signs indicating a product's geographic origin | Yes | Varies |

### Trade Secrets in Computing

Computing examples: proprietary algorithms, formulas, source code, customer lists, sensitive business data.

- Not registered; secrecy must be actively maintained.
- No time limit — protection lasts as long as the secret is kept.

### Copyright in the Digital Age

Digital technology has made infringement dramatically easier:
- Perfect copies at near-zero cost.
- Global distribution instantaneously via P2P networks and the internet.

**Software piracy** — the unauthorised copying, distribution, or use of software. Software is protected by copyright; the licence agreement specifies permitted use.

**Open Source Software** — software released under a licence permitting users to view, modify, and distribute the source code. Distinct from public domain:
- Open source still has copyright, but is licensed permissively.
- Licences may impose conditions (e.g., copyleft in GPL).

### Fair Use / Fair Dealing

Limited use of copyrighted material without permission is permitted for: education, commentary, criticism, news reporting, and research.

**Factors determining fair use:**
1. The purpose and character of the use (transformative? commercial?).
2. The nature of the copyrighted work.
3. The amount and substantiality of the portion used.
4. The effect of the use on the market for the original work.

### Ethical Analysis of IP

**Why protect IP?**

| Framework | Argument |
|-----------|---------|
| **Kantian** | IP reflects the creative work of real people; using it without permission treats creators merely as a means |
| **Utilitarian** | IP protection incentivises innovation; without financial reward, fewer works would be created, reducing overall societal benefit |
| **Social Contract** | Society has collectively agreed to respect IP rights because the system benefits everyone — creators are rewarded; society gets innovation |

**Against strong IP protection:**
- Overly broad IP restricts free flow of information and can impede further innovation.
- In some cases (e.g., pharmaceutical patents in developing countries), strict enforcement causes significant harm to vulnerable populations.
