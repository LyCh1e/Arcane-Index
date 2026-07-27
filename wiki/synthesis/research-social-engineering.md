---
type: synthesis
title: "Research: Social Engineering"
domain: secure-software-development
maturity: established
tags: [research, social-engineering, human-factors, psychology, phishing, deepfake, defence]
updated: 2026-07-28
created: 2026-07-28
---

# Research: Social Engineering

**Research question:** What is social engineering, how does it exploit psychology, what are the major attack classes, and what defences are most effective?

**Research method:** Autonomous web research (autoresearch) — 3 search passes, 3 deep fetches. Sources: ESET Business Security Blog, Secureframe, Doppel Research 2025, Verizon DBIR 2024/2025, FBI IC3 2024, Unit 42 Global Incident Response Report 2025.

---

## Summary

Social engineering is the dominant initial access vector in modern cyber attacks, accounting for roughly 60% of all breaches by human-element involvement. It succeeds not because technology is weak, but because human cognition is predictable under social pressure. Defences must therefore be designed at the people, process, *and* technology layers simultaneously — no single layer is sufficient.

The threat landscape is bifurcating: commodity attacks (mass phishing, smishing) are becoming cheaper and more automated via AI tooling, while targeted attacks (spear phishing, BEC, deepfake video calls) are becoming more convincing and harder to detect. The democratisation of AI voice and video synthesis has eliminated the advantage defenders previously held in recognising impersonation by voice or appearance alone.

---

## Core Findings

### 1. Psychological Model

Cialdini's six principles (authority, urgency/scarcity, reciprocity, consistency, social proof, liking) remain the foundational analytical framework. Every social engineering attack can be mapped to one or more of these principles. Practitioners who understand the model can run targeted awareness training against specific triggers rather than generic "don't click links" messaging.

### 2. Attack Taxonomy (2025 snapshot)

Three tiers of attack by technical sophistication:

**Commodity (low skill, high volume)**
- Mass phishing, smishing, quishing
- Scareware / fake tech support
- Baiting (USB drops)

**Targeted (moderate skill, specific victim)**
- Spear phishing, whaling, BEC/CEO fraud
- Vishing with pretexting scripts
- Callback phishing (TOAD) — phone-based RAT installation
- MFA fatigue / push bombing

**Advanced (high skill, nation-state or organised crime)**
- Real-time deepfake video/audio impersonation
- Long-con romance/pig-butchering campaigns
- Watering-hole attacks combined with supply chain compromise (e.g. Bybit 2025)

### 3. The Deepfake Inflection Point

The 2024–2025 period marks a qualitative shift. AI-generated deepfake video calls are now convincing enough to deceive experienced finance professionals in live business contexts ($25M CFO fraud, 2024). The 62% organisational exposure rate to deepfake SE incidents (Doppel, mid-2025) confirms this is no longer a theoretical risk. The required countermeasure is **process-level** (out-of-band verification) rather than perceptual — humans can no longer reliably distinguish real from synthetic voice and video.

### 4. Why MFA Alone Is Insufficient

Standard push-notification MFA (TOTP, SMS, authenticator app pushes) does not defeat:

- **MFA fatigue**: repeated push requests until approval
- **Adversary-in-the-middle phishing kits** (Evilginx, Tycoon): relay credentials and session cookies in real time, bypassing TOTP entirely
- **Helpdesk SE**: convince an IT agent to reset MFA on behalf of the attacker

**FIDO2/WebAuthn passkeys** defeat all three: the key is origin-bound (cannot be replicated to a phishing domain) and requires user presence (no remote-push approval). See [[concepts/fido-passkeys-passwordless]].

### 5. Defence Priority Order

Based on the research, the highest-leverage controls in order:

1. **Phishing-resistant MFA (FIDO2)** — eliminates credential replay and MFA fatigue at the technology layer
2. **Out-of-band verification procedures** for high-value requests — defeats even perfect deepfake impersonation
3. **Identity verification at helpdesk** — mandatory for any credential reset, regardless of caller confidence
4. **Psychological-trigger-aware training** — teach *why* an attack is convincing, not just what it looks like
5. **Multi-channel simulated attacks** — email, SMS, voice, QR code; not just click-rate phishing simulations

---

## Cross-Domain Connections

### Social Engineering ↔ Threat Modelling

Social engineering is a first-class threat agent action that most STRIDE exercises under-represent. *Spoofing* (identity impersonation) and *Elevation of Privilege* (gaining access through deception) are the two STRIDE categories most directly associated with SE. Threat models for any system handling sensitive data or high-value transactions must explicitly enumerate SE attack paths alongside technical attack paths. See [[concepts/threat-modeling]].

### Social Engineering ↔ OWASP Top 10

SE is the entry point for multiple OWASP categories:

- **A07 — Identification & Authentication Failures**: credential phishing feeds directly into this category; compromised credentials are the most common result of successful SE
- **A09 — Security Logging & Monitoring Failures**: post-SE-compromise detection depends entirely on having the right logs and monitoring for anomalous access patterns
- **A10 — Server-Side Request Forgery**: BEC attacks frequently culminate in fraudulent wire transfers executed through legitimate-looking internal requests

### Social Engineering ↔ Security Requirements (CIA-AAA)

SE attacks target the **Authenticity** and **Authorisation** components of the CIA-AAA model at the human layer. A system that correctly implements technical authentication (strong MFA, parameterised queries, encrypted storage) can still be fully compromised if an attacker convinces a human operator to grant access, reset credentials, or bypass a control. Security requirements must therefore include:

- Mandatory out-of-band verification for sensitive operations (a *process* requirement, not a software requirement)
- Awareness training and simulated attack frequency (a *people* requirement)
- Phishing-resistant MFA as a minimum standard (a *technology* requirement)

See [[concepts/secure-software-requirements]] and [[synthesis/re-elicitation-cia-aaa-security-requirements]].

### Social Engineering ↔ HCI

The effectiveness of SE attacks is partly an HCI failure: interfaces that create urgency (red banners, countdown timers, modal dialogs), normalise requests for credentials, or provide no ambient signal of security state make users more susceptible. Usability and security are not inherently in opposition — well-designed systems (FIDO2 passkey flows, visible sender-domain indicators in email clients) can reduce SE success rates without increasing friction. See [[concepts/hci-fundamentals]].

---

## Open Questions / Gaps

- How effective is psychological-trigger-aware training compared to generic awareness training in reducing SE success rates? No high-quality RCT evidence found.
- At what point does deepfake quality become indistinguishable from authentic video for all populations, and what is the optimal process-level response threshold?
- Does FIDO2 adoption at scale meaningfully reduce BEC frequency, or do attackers simply route around it via helpdesk SE?

---

## Source Pages

- [ESET: Social Engineering Attacks Explained](https://www.eset.com/blog/en/business-topics/prevention-and-awareness/how-social-engineering-attacks-work-psychology-tactics/)
- [Secureframe: 13 Most Common Social Engineering Attacks (2025)](https://secureframe.com/blog/most-common-social-engineering-attacks)
- [Doppel: Types of Social Engineering Attacks — 2026 Watch List](https://www.doppel.com/blog/10-types-social-engineering-attacks-watch-2025)
- [Verizon DBIR 2025](https://www.verizon.com/business/resources/reports/dbir/)
- [FBI IC3 Annual Report 2024](https://www.ic3.gov/AnnualReport)

**Primary concept page:** [[concepts/social-engineering]]
