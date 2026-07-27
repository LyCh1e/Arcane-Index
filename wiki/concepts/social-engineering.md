---
type: concept
title: "Social Engineering"
domain: secure-software-development
complexity: high
tags: [security, social-engineering, phishing, pretexting, vishing, psychology, human-factors, cialdini]
updated: 2026-07-28
status: established
created: 2026-07-28
---

# Social Engineering

Social engineering is a manipulation technique in which threat actors exploit human psychology — rather than technical vulnerabilities — to deceive victims into performing actions that benefit the attacker. Typical goals include credential disclosure, malware installation, unauthorised fund transfers, and physical access to restricted premises.

> Social engineering works because humans are fallible and are neurologically primed to respond to social cues such as authority, urgency, and trust. The attacker does not break the lock; they convince someone to open the door.

According to the Verizon 2025 Data Breach Investigations Report, the human element is involved in approximately **60% of all breaches**, making social engineering the most consistently exploited attack surface in any organisation.

---

## Why It Works — Psychological Foundations

Robert Cialdini's six principles of influence form the canonical framework for understanding why social engineering succeeds. Attackers deliberately select and combine these triggers.

| Principle | Exploitation Pattern |
|-----------|---------------------|
| **Authority** | Impersonating executives, IT support, government officials, auditors |
| **Urgency / Scarcity** | "Your account will be deactivated in 24 hours" — forces hasty decisions |
| **Reciprocity** | Offering a small gift or favour before making a request |
| **Consistency** | Small initial agreement increases compliance with larger follow-up requests |
| **Social Proof** | "Your colleagues have already verified their credentials" |
| **Liking** | Extended rapport-building, matching the target's interests, romance lures |

Additional psychological levers not in Cialdini's original model:

- **Fear** — fake virus alerts, scareware, sextortion threats
- **Curiosity** — "dropped" USB drives, enticing email subjects, baiting offers
- **Sympathy / Guilt** — impersonating a distressed colleague or family member

---

## Attack Taxonomy

### Email-Based Attacks

| Attack | Description |
|--------|-------------|
| **Phishing** | Mass-distributed deceptive emails directing victims to fake login portals or malicious downloads. FBI IC3 2024: 300,000+ complaints, losses exceeding $3 billion. |
| **Spear Phishing** | Personalised phishing using victim-specific reconnaissance (role, name, recent events). |
| **Whaling** | Spear phishing targeting C-suite executives where a single successful compromise yields high-value access. |
| **Clone Phishing** | A legitimate email is duplicated with links or attachments replaced by malicious versions, re-sent from a spoofed address. |
| **Business Email Compromise (BEC)** | Attacker impersonates an executive via email to redirect payments or sensitive data. Caused **$4.4 billion** in losses in 2024 (FBI IC3). No malware involved; relies entirely on pretexting and perceived authority. |

### Telephone and Voice Attacks

| Attack | Description |
|--------|-------------|
| **Vishing** | Voice phishing via phone call. Attackers impersonate IT helpdesks, financial institutions, government agencies, or family members. |
| **Callback Phishing (TOAD)** | Email claims an auto-renewing subscription requires phone cancellation. Victim calls the provided number, where a social engineering operator installs remote access software. Recent variants distribute via Microsoft Teams. |
| **AI-Synthesised Voice Cloning** | Generative AI replicates a known contact's voice in real time, making vishing convincing even to experienced users. |

### Physical Attacks

| Attack | Description |
|--------|-------------|
| **Tailgating / Piggybacking** | Attacker physically follows an authorised employee through a secured door, often while carrying boxes or claiming a forgotten badge. |
| **Shoulder Surfing** | Observing credentials, PINs, or sensitive data in public spaces. |
| **Baiting (USB Drop)** | Infected USB drives left in car parks or common areas. DHS testing found 60% of people plugged in found drives; with official branding, adoption reached 90%. |

### Multi-Vector and Advanced Attacks

| Attack | Description |
|--------|-------------|
| **Pretexting** | Constructing a detailed, believable scenario and adopting a fabricated identity to justify an unusual request. Now accounts for **27% of all social engineering incidents** (Verizon DBIR 2024). |
| **Deepfake Video / Audio Impersonation** | AI-generated audio or video impersonates a real person in real-time video calls. 62% of organisations experienced a deepfake-related SE incident in the 12 months prior to mid-2025. |
| **MFA Fatigue (Push Bombing)** | Repeated MFA push notifications until an exhausted or confused user approves one. Pairs with adversary-in-the-middle kits (Evilginx, Tycoon) and helpdesk SE to bypass MFA at enterprise scale. |
| **QR Code Phishing (Quishing)** | Malicious URLs embedded in QR codes bypass email security gateways. Used by North Korean Kimsuky APT and Russian Void Blizzard in targeted campaigns. |
| **Consent Phishing** | Fake OAuth consent screens grant a malicious application cloud access to the victim's account. |
| **ClickFix and Variants** | Fake error alerts (BSOD, crash notices, CAPTCHA overlays) trick users into running malicious commands via the Windows Run dialog or browser console. Variants include FileFix, ConsentFix, and CrashFix. |
| **Watering Hole** | Attacker compromises a website frequently visited by the target group, injecting malware or fingerprinting scripts. 2021 Florida water treatment facility attack used a compromised contractor site. |
| **Scareware** | Fake security pop-ups claim the victim's device is infected, directing them to purchase fraudulent antivirus software. Office Depot / Support.com settled for $35 million in 2019. |
| **Long-Con / Pig Butchering** | Extended relationship-building (weeks to months) via social media or dating apps, culminating in a request to invest in a fraudulent crypto scheme. |
| **Quid Pro Quo** | Attacker offers a service (IT support, a gift) in exchange for credentials or access. Exploits the reciprocity principle directly. |

---

## Real-World Case Studies

### Bybit Cryptocurrency Heist (2025) — $1.4 Billion
North Korean Lazarus Group actors targeted a Safe{Wallet} developer via social engineering, tricking them into installing malicious Docker code that granted workstation access. The resulting compromise led to the largest cryptocurrency theft on record.

### MGM Resorts (2023) — Tens of Millions in Losses
Attackers gathered employee information from LinkedIn, then called MGM's IT helpdesk impersonating staff members. After obtaining password resets, they deployed ransomware across MGM's systems, disrupting hotel operations for weeks.

### $25 Million Deepfake CFO Fraud (2024)
A finance employee at a multinational joined what appeared to be a legitimate video call with their CFO and several colleagues. All participants were AI-generated deepfakes. The employee authorised a $25 million transfer.

### M&S and Co-op Group (2025) — ~£440 Million Estimated Losses
The Scattered Spider group called outsourced IT helpdesks, impersonating employees to obtain password resets. The resulting access enabled ransomware deployment. M&S was unable to process online orders for several weeks.

### Twitter (2020) — Vishing for Credentials
Attackers used vishing to trick Twitter employees into sharing internal credentials. Within hours, attackers had posted from accounts of Barack Obama, Elon Musk, and Joe Biden, netting over $100,000 in bitcoin.

---

## Red Flags — Recognition Signals

Individual recognition remains the primary last line of defence when technical controls fail.

- **Unsolicited urgency**: pressure to act immediately, within the hour, or before your manager knows
- **Unusual request channel**: executive sending a sensitive request via personal email or WhatsApp
- **Demands for secrecy**: "don't tell your bank / boss / IT team"
- **Identity mismatch**: caller ID, email domain, or display name differs subtly from the legitimate entity
- **Grammatical anomalies**: unnatural phrasing, inconsistent register, or machine-translated tone
- **Unexpected credential requests**: no legitimate IT team or bank ever needs your password
- **Mismatched URLs**: hover before clicking; display text and actual URL differ
- **Pressure to bypass procedure**: "the normal approval process will take too long this time"

---

## Defence Framework

Effective defence requires controls at three independent layers; any single layer can be bypassed.

### People Layer
- Continuous security awareness training focused on psychological triggers rather than just phishing simulation click rates
- Multi-channel simulated attack exercises covering email, SMS, voice, and QR codes
- Organisational culture that actively rewards rapid incident reporting without penalising the victim

### Process Layer
- **Out-of-band verification**: any high-value payment or sensitive data request must be confirmed through a separately known channel (not a number or address provided by the requester)
- Segregation of duties for financial operations — no single person can authorise and execute a large transfer
- Strict identity verification protocols for helpdesk password resets (not merely caller ID)
- Tested incident response plans covering social engineering scenarios specifically

### Technology Layer
- **Phishing-resistant MFA** (FIDO2 / passkeys) — eliminates credential replay and neutralises MFA fatigue by design; see [[concepts/fido-passkeys-passwordless]]
- Email security gateways with anti-impersonation and anomalous-sender detection
- URL filtering and sandboxing for link-click post-processing
- Anomaly detection on access patterns (unusual login hours, unexpected data volumes)
- Advanced email filtering blocking lookalike domains and display-name spoofing

---

## Relationship to Other Security Concepts

| Concept | Relationship |
|---------|-------------|
| [[concepts/threat-modeling]] | Social engineering is a primary threat agent action; STRIDE's *Spoofing* and *Elevation of Privilege* categories directly map to SE techniques |
| [[concepts/owasp-top-10]] | A07 (Identification & Authentication Failures), A09 (Security Logging & Monitoring Failures) are frequently exploited post-SE-breach |
| [[concepts/secure-software-requirements]] | Security requirements must include awareness training, verification procedures, and anti-impersonation controls as explicit, testable items |
| [[concepts/fido-passkeys-passwordless]] | FIDO2/WebAuthn passkeys are origin-bound — a phished site cannot trigger the registered key, directly neutralising credential-phishing and MFA fatigue |
| [[concepts/security-testing-and-verification]] | Red team / penetration testing must include social engineering simulation (vishing, phishing campaigns) not just technical attack paths |
| [[concepts/security-terminology]] | Social engineering exploits failures of *authentication* and *authorisation* at the human layer rather than the software layer |

---

## Key Statistics (2024–2025)

| Statistic | Source |
|-----------|--------|
| Human element involved in ~60% of breaches | Verizon DBIR 2025 |
| Phishing accounts for ~36% of initial access vectors | Unit 42 Global Incident Response Report 2025 |
| BEC losses exceeded $4.4 billion in 2024 | FBI IC3 Annual Report 2024 |
| Pretexting accounts for 27% of all SE incidents | Verizon DBIR 2024 |
| 62% of organisations experienced a deepfake SE incident in the prior 12 months | Doppel Research, mid-2025 |
| 60% of found USB drives were plugged in; 90% if branded with official logos | DHS field test |
