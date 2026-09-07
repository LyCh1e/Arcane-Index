---
type: source
title: "INF2005 Cyber Security Fundamentals — Access Control"
source: "raw/INF2005 Cyber Security Fundamentals - Access Control.md"
domain: secure-software-development
tags: [inf2005, access-control, authentication, authorisation, biometrics, passwords, DAC, RBAC, MAC, POLP, separation-of-duties]
created: 2026-09-07
lecturer: "Dr Tan Kheng Leong"
---

# Source Index — INF2005 CSF: Access Control

**Module:** INF2005 Cyber Security Fundamentals  
**Lecturer:** Dr Tan Kheng Leong  
**Topic:** Access Control  
**Raw file:** `raw/INF2005 Cyber Security Fundamentals - Access Control.md`

---

## Coverage

### IAA Framework

`Identification → Authentication → Authorisation`

Three authentication factor categories: **Knowledge**, **Token/Device**, **Biometrics**

### Authentication via Asymmetric Crypto

Bob encrypts Alice's random challenge with his private key; Alice decrypts with Bob's public key — match confirms identity. Requires Alice to already hold an authentic copy of Bob's public key.

### Password Best Practices

Mixed-case + digits + special characters; sufficient length; no reuse; periodic change; 2FA; password manager. Manager weakness: single point of failure; memory forensics risk; keylogger vulnerability.

### Password Attacks

| Attack | Description |
|--------|-------------|
| Brute force | Try all combinations; avg ½ key space; 25-GPU cluster = 350B guesses/s |
| Reverse brute force | One password vs many usernames (bypasses per-account lockout) |
| Dictionary attack | Hash dictionary words, compare to leaked hash DB |
| Social engineering | Personal info from online profiles narrows guesses |
| Google dorking | Search operators find exposed credential files (`ext:txt inurl:passwd`) |
| Rainbow table | Precomputed hash→password lookup; defeated by salting |

### Secure Password Storage (best to worst)

1. `Hash(password + Salt)` — best; salting defeats precomputed tables
2. `Hash(password)` — vulnerable to rainbow tables
3. `Encrypt(password)` — reversible if key leaks
4. Plaintext — never acceptable

### Passphrase Techniques

- Acronym: sentence → first letters → password (e.g. → `iltwp100one56a7`)
- Random word passphrases: high entropy, memorable

### Graphical Authentication

- **Recognition-based:** pick passimages from challenge set; password space `9⁵ = 6561` (for 5 rounds of 9 images); shoulder surfing vulnerable
- **Cued-recall:** click points on an image; hotspot bias reduces effective space
- **Recall-based (pattern):** 389,112 theoretical combos; smudge attack / camera vulnerable
- **Hybrid:** combines selection + gesture for higher space (Windows 8 picture password)

### Token-Based Authentication

- **eToken:** USB/card stores private keys and certificates; on-board 2FA; banking tokens, premise access
- **Smart Cards:** embedded microprocessor; JavaCard (multi-app) / MULTOS; tamper-resistant; stores biometric templates
- **RFID:** IC + antenna; passive (powered by reader RF field) vs active (battery); vulnerable to OTA spoofing, power analysis, MITM

### Biometric Accuracy

- **FAR** (False Accept Rate): likelihood of wrongly granting access — should be 0
- **TAR** (True Accept Rate): likelihood of correctly granting access — should be 1
- **ROC curve:** shows TAR/FAR tradeoff; operating point chosen by risk tolerance

### Biometric Modalities (from most to least accurate)

1. Retinal scan — 400 features; 70× more accurate than iris; invasive; > $100K
2. Iris scan — 256 features; FAR ~1 in 10M; non-invasive; $200–$2,000
3. Fingerprint — FAR ~1 in 100K; most common; $30–$1,000
4. Facial recognition — >90% accuracy with ML; FAR ~1 in 1M; racial bias noted

Behavioural biometrics: gait (~99.3% with AI), keystroke dynamics, voice recognition (~95%).

### Authorisation Models

| Model | Control | Notes |
|-------|---------|-------|
| DAC | Resource owner (via ACLs) | Flexible; weak system-wide enforcement |
| RBAC | Admin assigns roles | Supports POLP; risk of Role Creep |
| MAC | OS enforces security labels (classification + category) | Most secure; highest overhead |

### Principle of Least Privilege (POLP)

Minimum permissions for the function; limits compromise blast radius. Mobile example: flashlight Trojan with device-admin access stole banking credentials.

### Separation of Duties (SoD)

Split critical tasks across multiple people — the person who prepares a payslip is not the person who approves it.

---

## Linked Concepts

- [[concepts/access-control]] — full concept page: IAA framework, password attacks, salted hashing, graphical auth, biometrics (FAR/TAR/ROC), token types, DAC/RBAC/MAC, POLP, SoD
- [[concepts/public-key-cryptography-and-key-exchange]] — asymmetric challenge-response authentication protocol
- [[concepts/fido-passkeys-passwordless]] — modern standard for asymmetric authentication without passwords
- [[concepts/secure-software-requirements]] — CIA triad, AAA requirements framework
