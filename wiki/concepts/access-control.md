---
type: concept
title: "Access Control — Identification, Authentication, and Authorisation"
aliases: ["IAA", "authentication", "authorisation", "biometrics", "DAC", "RBAC", "MAC", "POLP", "least privilege", "password security", "role creep"]
tags: [access-control, authentication, authorisation, biometrics, passwords, DAC, RBAC, MAC, POLP, security, inf2005]
created: 2026-09-07
updated: 2026-09-07
status: established
domain: secure-software-development
---

# Access Control — Identification, Authentication, and Authorisation

Access control restricts **who** can do **what** to **which resources**. It operates in three sequential stages:

```
Identification → Authentication → Authorisation
```

| Stage | Question answered | Example |
|-------|-----------------|---------|
| **Identification** | Who are you claiming to be? | "I am Fred" |
| **Authentication** | Prove it | Password check, fingerprint scan |
| **Authorisation** | What are you allowed to do? | Read-only vs admin access |

> **One-line definition:** Access control ensures that only verified identities can perform only the actions they are permitted to perform on only the resources they are permitted to access.

---

## Authentication

Authentication establishes that a subject is who they claim to be. Three factor categories are recognised:

| Category | Basis | Examples |
|----------|-------|---------|
| **Knowledge** | Something you know | Password, passphrase, PIN, challenge-question responses |
| **Token/Device** | Something you have | Smart card, hardware dongle, mobile OTP device, RFID card |
| **Biometrics** | Something you are | Fingerprint, iris scan, retina scan, facial geometry, voice, gait |

**Multi-Factor Authentication (MFA / 2FA)** combines two or more categories, significantly raising the bar for an attacker who must compromise multiple independent factors.

### Authentication via Asymmetric Cryptography

Bob proves his identity to Alice without a shared secret:
1. Alice sends Bob a **random challenge number**.
2. Bob **encrypts it with his private key** and returns the ciphertext.
3. Alice **decrypts with Bob's public key** and compares to the original number.
4. A match proves only Bob's private key could have produced the ciphertext — identity verified.

*Prerequisite:* Alice must already hold an authentic copy of Bob's public key (otherwise a MITM can substitute their own key).

---

## Knowledge-Based Authentication — Passwords

### Best Practices

| Practice | Reason |
|----------|--------|
| Mix uppercase, lowercase, digits, and special characters | Increases password space |
| Minimum length (≥ 12 characters) | Exponentially grows brute-force cost |
| Avoid dictionary words and keyboard walks | Resist dictionary attacks |
| No reuse across sites | Prevents credential-stuffing attacks |
| Change periodically (e.g. every 90 days) | Limits exposure window after a breach |
| Use 2FA | Second factor protects even if password is leaked |
| Use a password manager | Enables unique, strong passwords per site |

### Password Manager Trade-offs

**Pros:** one strong master password enables unique, complex credentials everywhere; removes the human tendency to reuse or simplify passwords.

**Cons:** single point of failure — master password compromise or tool vulnerability exposes all passwords; the master password can leak via keyloggers or memory forensics (hex editor analysis of RAM); Trojans can intercept at entry time.

### Large-Scale Breaches

Password database leaks are now endemic — the RockYou2021 compilation contained over 8 billion credential pairs. Services like *Have I Been Pwned* (haveibeenpwned.com) allow users to check whether their email or password hash has appeared in a known leak.

---

## Password Attacks

### Brute Force

Try every possible combination of characters until a match is found. On average, half the key space must be tried. Defended by: account lockout, rate limiting, CAPTCHA. Limitation: attackers who have exfiltrated the password hash database can bypass lockout by cracking offline.

**Reverse brute force:** try a single common password (e.g. "password123") against a large list of usernames — bypasses per-account lockout policies.

**High-performance cracking:** a 25-GPU cluster achieves ~350 billion guesses/second. Standard Windows passwords have been cracked in under 6 hours; cloud GPU spot instances (e.g. AWS) make this attainable for under $50.

### Dictionary Attack

Build a list of commonly used passwords and their variants; hash each candidate and compare to leaked hashes. Effective because users favour predictable patterns (names, dates, keyboard walks).

### Social Engineering / Google Dorking

Personal information found online (pet names, birthdays, favourite teams) narrows the guessing space. **Google dorking** uses search operators to find exposed credential files:

```
ext:txt inurl:passwd
ext:xlsx inurl:password
```

### Rainbow Table Attack

A **rainbow table** is a precomputed mapping of `hash → password`. An attacker who obtains a hash database searches for each hash in the table to instantly recover the plaintext. Defeated entirely by salting (see below).

Tools: RainbowCrack, Ophcrack, CrackStation.

---

## Secure Password Storage

| Method | Security | Notes |
|--------|----------|-------|
| Store plaintext | None | Never acceptable |
| Store `Encrypt(password)` | Weak | Reversible if encryption key is compromised |
| Store `Hash(password)` | Moderate | One-way, but rainbow tables precompute common hashes |
| Store `Hash(password ‖ salt)` | **Strong** | Salt is a random string appended to the password before hashing — each account's salt is stored in the database alongside the hash |

**How salting defeats rainbow tables:** the attacker would need to precompute a separate rainbow table for every unique salt — computationally infeasible.

**Recommended algorithms:** bcrypt, scrypt, Argon2 (memory-hard key derivation functions designed for password hashing). Standard hash functions (SHA-256) alone are too fast — they can be computed billions of times per second by GPUs. Memory-hard KDFs resist GPU acceleration.

---

## Passphrase Hardening Techniques

**Passphrases** — long sequences of unrelated words — are both memorable and high-entropy:

- "correct horse battery staple" → ≈ 44 bits of entropy (4 random dictionary words)

**Acronym technique:** form a password from the first letters of a memorable sentence:

- "i love to watch physical 100 on netflix every friday, saturday and sunday" → `iltwp100one56a7`

---

## Graphical Authentication

An alternative knowledge factor using images or gestures:

| Type | How it works | Key vulnerability |
|------|-------------|------------------|
| **Recognition-based** | Select personal "passimages" from a challenge set at login | Shoulder surfing; passimage leakage |
| **Cued-recall** | Click on specific points of a displayed image | "Hotspot bias" — users gravitate to faces and distinctive objects, reducing effective password space |
| **Recall-based** | Draw a gesture pattern on a grid (Android-style) | Smudge attacks (fingerprint oil), camera observation |
| **Hybrid** | Combine image selection + gesture | Higher password space; gestures via mouse avoid smudge attacks |

---

## Token-Based Authentication

### eToken / Hardware Token

A physical device (USB key, smart card, or mobile) that stores private keys, digital certificates, and can generate one-time passcodes. Provides on-device computation for 2FA and digital signing. Applications: crypto wallets, bank OTP tokens, building access systems.

### Smart Cards

Credit-card-sized devices with an embedded microprocessor. Chip operating systems (JavaCard, MULTOS) support multiple applications on one card. Capabilities: PIN storage, biometric template storage (on-card matching), encrypted communication via card reader, built-in tamper resistance.

### RFID Tags

Radio-frequency identification — IC with antenna; responds to RF interrogation with identity data. No battery required (passive tags draw power from the RF field).

| Property | Passive RFID | Active RFID |
|----------|-------------|-------------|
| Power | From RF field | Battery |
| Range | Short (~cm to ~m) | Long (tens of metres) |
| Storage | Typically ~2 KB | Larger |

**RFID vulnerabilities:** over-the-air (OTA) spoofing, power-analysis side-channel attacks, MITM/sniffing, proximity theft. Metals and textiles can attenuate the read range of passive tags.

---

## Biometric Authentication

Biometrics use a physiological or behavioural characteristic extracted into a template, which is compared at verification time.

**Two modes:** Enrolment (register template) and Verification (match new sample against stored template).

### Biometric Requirements

| Requirement | Meaning |
|-------------|---------|
| **Universality** | Every person should possess the characteristic |
| **Distinctiveness** | Any two persons should differ sufficiently |
| **Permanence** | Characteristic should be stable over time |
| **Collectability** | Must be measurable and quantifiable |

### Biometric Accuracy Metrics

- **FAR (False Accept Rate)** — probability of incorrectly accepting an impostor (ideally 0)
- **TAR (True Accept Rate)** — probability of correctly accepting a genuine user (ideally 1)
- **ROC (Receiver Operating Characteristic) curve** — plots TAR vs FAR; raising TAR acceptance threshold also raises FAR; system designers must choose an operating point that suits the use case's risk tolerance.

### Biometric Modality Comparison

| Modality | Uniqueness | FAR | Speed | Cost | Notes |
|----------|-----------|-----|-------|------|-------|
| **Retinal scan** | Up to 400 unique features; ~70× more accurate than iris | Very low | Slow (≥10s, 15s focus) | > $100K | Most invasive; capillary patterns can change with disease (glaucoma, detachment) |
| **Iris scan** | 256 unique features; distinct in identical twins | ~1 in 10 million | Fast (< 5s) | $200–$2,000 | Less invasive than retina; unaffected by most diseases |
| **Fingerprint** | ~1 in 64 billion match chance | ~1 in 100,000 (smartphone) | < 1s (contactless) | $30–$1,000 | Most common; affected by dryness, cuts, abrasion |
| **Facial recognition** | Geometric landmarks (eye distance, nose, jawline) | ~1 in 1,000,000 | < 1s | $90–$1,500 | Non-contact; affected by aging, wearables; racial bias (False positive rates up to 100× higher for Asian and Black individuals vs. white individuals in some systems) |

### Biometric Attacks

- **Spoofing:** presenting a fake artifact (silicone fingerprint, photo, 3D-printed face) to fool the scanner.
- **Adversarial examples:** carefully crafted inputs that fool ML-based facial recognition.
- **Algorithmic bias:** trained on non-representative datasets, many systems exhibit significantly higher error rates for certain demographic groups — a fairness and security concern.

### Behavioural Biometrics

Based on *how* a user behaves rather than what they physically are:

| Modality | Captured via | Accuracy | Notes |
|----------|-------------|---------|-------|
| **Gait analysis** | CV cameras, floor sensors, wearables | ~99.3% with AI | Can change with injury or weight change |
| **Keystroke dynamics** | Software (key hold time, inter-key pause intervals) | Moderate | Low-cost deployment |
| **Voice recognition** | Microphone | ~95% (Microsoft Speech Recognition) | Combines physical + behavioural traits; text-dependent vs text-independent modes |

---

## Authorisation

Once a subject is authenticated, **authorisation** determines which actions they may perform on which objects:

```
Subject → Access Request → Reference Monitor → Object
```

The **reference monitor** enforces the access control policy and cannot be bypassed.

### Access Control Models

**1. Discretionary Access Control (DAC)**

- Access rights granted by the **resource owner** (the user who created the object).
- Implemented via **Access Control Lists (ACLs)** — lists of subjects and their permitted operations on each object.
- Ownership categories: Owner, Group, Other/World.
- Example: Unix file permissions (`rwxr-xr--`), Windows ACLs.
- **Weakness:** owners may grant excessive permissions; no system-wide policy enforcement.

**2. Role-Based Access Control (RBAC)**

- Administrators assign rights to **roles** (job functions), not to individual users; users are then assigned to roles.
- Supports the **Principle of Least Privilege** by design — roles grant only the permissions the job function requires.
- **Risk — Role Creep:** a user who transfers to a new role retains their old role's permissions unless explicitly revoked. Requires periodic role review and immediate revocation on role change.
- Tools: Centrify, SolarWinds Identity.

**3. Mandatory Access Control (MAC)**

- Enforced by the **operating system** using **security labels** assigned to all subjects and objects.
- Labels combine:
  - **Classification level:** Top Secret → Secret → Sensitive → Unclassified (hierarchical)
  - **Category / compartment:** specific project or department (enforces "need to know")
- Access is granted only when both classification and category match.
- **Most secure model** — users cannot override it; requires significant administrative overhead for label maintenance.
- Used in: military systems, classified government networks (e.g. SELinux).

### Comparison

| Model | Who controls access | Flexibility | Security | Overhead |
|-------|-------------------|-------------|---------|---------|
| DAC | Resource owner | High | Low–medium | Low |
| RBAC | System administrator (via roles) | Medium | Medium–high | Medium |
| MAC | Operating system (via labels) | Low | Highest | High |

---

## Supporting Principles

### Principle of Least Privilege (POLP)

Grant every subject (user, process, application) only the **minimum permissions necessary** to perform its function — nothing more.

- **Rationale:** limits blast radius if an account or process is compromised.
- **Mobile example:** a flashlight app needs LED control only — not GPS, contacts, or SMS. A real-world Trojan disguised as a flashlight app on Android requested device-admin rights and exfiltrated banking credentials via the over-permissioned access.
- **Implementation:** start with no permissions and add only what is needed; review permissions regularly.

### Separation of Duties (SoD)

Divide critical tasks across **multiple people** so no single individual has end-to-end control over a sensitive process.

- **Rationale:** prevents fraud, reduces error risk, limits insider-threat impact.
- **Example (payroll):** the person who prepares a payslip must not be the same person who authorises the payment.
- Closely related to **dual control** (two people must act together) and **four-eyes principle** (requires a second approver).

---

## System Administrator Recommendations

1. **Enforce password policies** — minimum length, complexity, rotation, no reuse.
2. **Implement MFA** — additional factor greatly increases attack cost.
3. **Store passwords with salted hashing** — use bcrypt, scrypt, or Argon2.
4. **Apply POLP across all accounts and services.**
5. **Review and revoke roles promptly on transfer or departure.**
6. **Monitor authentication logs** — alert on repeated failures across different time windows.
7. **Educate users** — social-engineering resistance training.
8. **Control web-facing directory permissions** — prevent Google dorking from finding exposed credential files.

---

## Key Connections

- [[concepts/secure-software-requirements]] — CIA triad, AAA (Authentication, Authorisation, Audit)
- [[concepts/public-key-cryptography-and-key-exchange]] — asymmetric key authentication challenge-response protocol
- [[concepts/fido-passkeys-passwordless]] — modern passwordless authentication standard built on asymmetric crypto
- [[concepts/threat-modeling]] — access control failures modelled via STRIDE (Spoofing, Tampering, Elevation of Privilege)
- [[concepts/cryptographic-hash-functions]] — salted password hashing implementation
- [[areas/secure-software-development]] — parent area
