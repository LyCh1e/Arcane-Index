# Access Control

*Cyber Security Fundamentals — Dr Tan Kheng Leong*

## 1. Overview

**Access Control** authenticates and authorizes individuals to access only the information they are allowed to see and use. It consists of three stages:

```
Identification → Authentication → Authorisation
```

- **Identification** — claiming an identity (e.g. "I am Fred!")
- **Authentication** — proving that claimed identity
- **Authorisation** — determining what the now-verified identity is permitted to do

---

## 2. Authentication

**Definition:** proving you are who you claim to be, using a distinguishing characteristic.

### Three Authentication Categories
| Category | Basis | Examples |
|---|---|---|
| **Knowledge** | Something you know | Password, passphrase, challenge-question responses |
| **Token/Device** | Something you have | Identity card, dongle, access card, mobile phone |
| **Biometrics** | Something you are | Fingerprint, iris pattern |

### Worked Example — Authentication via Asymmetric Crypto
*If Bob wants to prove his identity to Alice:*
1. Bob asks Alice for a random number.
2. Bob encrypts the number with **his private key** and sends the ciphertext to Alice.
3. Alice decrypts it using **Bob's public key** and compares the result to the number she sent.
4. A match proves Bob's identity.
- **Assumption:** Alice must already possess Bob's authentic public key beforehand.

---

## 3. Knowledge-Based Authentication: Passwords

### Common Poor Practices
- Re-using a password
- Modifying a password slightly for re-use
- Using an easily guessed password
- Sharing a password
- Writing a password down

### Best Practices for Strong Passwords
- Mix upper/lowercase letters, numbers, and special characters; sufficient minimum length
- Avoid common dictionary words
- Avoid predictable "tricks" (e.g. password walking across a keyboard)
- Change periodically (e.g. every 90 days); no reuse
- Use Two-Factor Authentication (2FA) where available
- Use a secured password manager

### Password Managers
**Pros:** enable unique, strong passwords per site; help prevent password-reuse attacks.
**Cons:**
- Single point of failure — compromising the manager exposes all stored passwords
- Runs in memory, so the master password can potentially be leaked via memory forensics (e.g. hex editor analysis)
- Still vulnerable to keyloggers and Trojans
- A strong master password remains essential

### Contemporary Password Issues
- Large-scale password database leaks are common (e.g. RockYou2021 compilation)
- Services like *Have I Been Pwned* let users check if their credentials were exposed
- **Key point:** formulating a good password is just as important as storing it securely

---

## 4. Attacking Passwords

### Password Space & Cracking
- **Password space** = number of possible character combinations, given password length and character set.
- In practice, cracking is easier than the theoretical password space suggests, because people don't choose randomly — predictable patterns are exploited by cracking tools.

### Brute Force
- Try all possible character combinations.
- Inefficient without significant computing power (on average, takes half the total search space).
- **Reverse brute force** — attacker tries one password against many usernames instead.
- **Account lockout** is a common defense against brute-force login attempts on web apps (though attackers may exfiltrate the password database directly to bypass this).

### High-Performance Password Cracking
- A 25-GPU cluster can crack any standard Windows password in under 6 hours (~350 billion guesses/second).
- Cloud GPU rental (e.g. AWS spot instances) makes this attainable cheaply — cracking an average password can cost under $50.

### Dictionary Attack
- Uses a dictionary of commonly used passwords (and variants).
- Given a list of leaked password **hashes**, the attacker hashes each dictionary word and checks for matches — a match reveals the plaintext.

### Social Engineering
- Personal details shared online (favorite food, pets, birthdays, etc.) can be exploited to guess or narrow down passwords.
- **Google hacking / dorking** — using search operators (e.g. `ext:txt inurl:passwd`, `ext:xlsx inurl:password`) to find exposed credential files.

### Tools
- **Cain and Abel** — a Windows-only password recovery tool using multiple attack techniques; used by both attackers (unauthorized access) and defenders (testing their own defenses / recovering lost access).

---

## 5. Password Security Hardening

### Passphrases & Coping Techniques
- **Passphrases** — memorable, long sequences of unrelated words.
- **Acronym technique** — take the nth letter/number of each word in a sentence to form a password.
  - Example: *"i love to watch physical 100 on netflix every friday, saturday and sunday"* → `iltwp100one56a7`

### Secure Password Storage (progressively better)
| Method | Security Level |
|---|---|
| `Encrypt(password)` | Better than storing plaintext, but reversible if key is compromised |
| `Hash(password)` | Good — one-way, but vulnerable to precomputed lookup/rainbow tables |
| `Hash(password + Salt)` | **Best** — salt randomizes the hash, defeating precomputed tables |

- **Salt** — a random string added to a password before hashing.
- Because the salt isn't known in advance, attackers cannot precompute lookup tables for it.

### Hash/Rainbow Table Attacks
- Attackers store `<hash, password>` pairs and search for a target hash to reveal the corresponding password — known as a **lookup table attack** or **rainbow table attack**.
- Tools: RainbowCrack, Ophcrack, CrackStation.

### System Administrator Recommendations
- Enforce password change/formulation policies (defends against guessing attacks)
- Implement additional authentication factors (e.g. 2FA)
- Store passwords securely — **salt and hash**, hash sensitive data multiple times
- Educate users on security awareness (defends against social engineering)
- Maintain correct access rights on web accounts (defends against Google dorking / directory traversal)
- Monitor authentication logs; raise alerts on repeated failed logins across different times

---

## 6. Graphical-Based Authentication

An alternative form of "something you know," using images/gestures instead of text.

### Three Categories

**1. Recognition-Based**
- User enrolls a set of "passimages."
- At login, the user picks their passimages from a **challenge set** that mixes passimages with distractor images.
- Password space example: if choosing 1 image from a set of 9, across 5 rounds → `9⁵ = 6561` combinations.
- **Vulnerable to shoulder surfing** and other observational attacks.

**2. Cued-Recall**
- User is shown an image and selects specific points on it to register as their password.
- At login, they must click those points again (within a margin of error).
- **Vulnerable to "hotspots"** — common points people gravitate toward (e.g. faces, distinctive objects) — makes it susceptible to social hacking and shoulder surfing.

**3. Recall-Based**
- User draws a pattern connecting points/grids (e.g. Android-style pattern unlock).
- Theoretical password space: 389,112 combinations across all pattern lengths and directions — but the actual effective space is smaller since people favor a limited set of common patterns.
- **Vulnerable to smudge attacks** (finger oil marks are hard to fully wipe away) and easy to capture via camera.

### Hybrid Approach (Recognition + Recall)
- Combines picture selection with a gesture, increasing the overall password space.
- Gestures can be drawn via mouse to avoid smudge-attack issues.
- Example: Windows 8 introduced a "picture password" combining image selection with gestures.

---

## 7. Token-Based Authentication (Something You Have)

- Physical device used to aid authentication — inserted, or used to generate a one-time code.
- Commonly deployed as part of **2FA** in financial transactions.
- Common types: **eToken**, **Smart Cards**, **RFID Tags**.

### eToken
- Can be implemented as a USB key, smart card, or mobile device.
- Physically protects stored data — passwords, digital signatures, certificates, private keys.
- Workflow: password authentication on the client side triggers the token to retrieve a stored key / generate a passcode, sent to the server for verification.
- Provides on-board 2FA and digital signing.
- **Applications:** crypto devices (e.g. Aladdin eToken), physical premise access (electronic keys), banking tokens (e.g. Maybank, HLF), blockchain transaction signing.

### Smart Cards
- Credit-card-sized, usually with an embedded microprocessor (computation + storage).
- Chip operating systems support multiple secured applications on one card:
  - **JavaCard** — open, multi-app system supporting loadable applets
  - **MULTOS** — supports dynamic loading, updating, and deletion of applications
- **Capabilities:** store PIN codes; securely store biometric templates (e.g. MegaMatcher On Card); encrypt information; communicate securely via a card reader; built-in tamper resistance (hard to duplicate/forge).
- **Applications:** identification/authentication for access control, transaction rights, pandemic tracking.

### RFID Tags
- **Radio Frequency Identification** — an integrated circuit with an antenna that responds to an RF signal with identity information.
- Power supply is optional — the IC can draw power from the RF signal itself.
- **Vulnerable to:** OTA (over-the-air) spoof attacks, theft, side-channel (power analysis) attacks, MITM/sniffing.
- **Active tags** — battery-powered, continuously broadcast.
- **Passive tags** — powered by the RFID reader's RF energy; read range affected by nearby metals/textiles; typically ~2KB storage.
- **Applications:** supply-chain logistics, patient tracking in healthcare (e.g. dementia patients), inmate tracking in prisons.

---

## 8. Biometric Authentication (Something You Are)

- Uses **physiological** or **behavioural** characteristics — a feature set is extracted and compared against a stored template.
- Can support both **identification** and **authentication**.
- Two operational modes: **Enrollment** (registering a template) and **Verification** (matching against it).

### Essential Requirements of a Good Biometric Characteristic
| Requirement | Meaning |
|---|---|
| **Universality** | Every person should have the characteristic |
| **Distinctiveness** | Any two people should differ sufficiently in this characteristic |
| **Permanence** | Should remain sufficiently stable over time |
| **Collectability** | Must be measurable quantitatively |

### Practical Considerations
- **Acceptability** — must be convenient enough that users are willing to use it (e.g. issues with contact lenses for iris scans, dry/injured fingers for fingerprint scans); enrollment time and privacy concerns/cultural stigma also matter.
- **Accuracy** — measured via:
  - **False Accept Rate (FAR)** — likelihood of wrongly granting access (ideally 0)
  - **True Accept Rate (TAR)** — likelihood of correctly granting access (ideally 1)
  - **ROC (Receiver Operating Characteristic)** curve — shows the TAR/FAR tradeoff; a higher TAR generally comes with a higher FAR too.

### Comparison of Common Biometric Modalities
| Modality | Uniqueness | Accuracy Notes | Enrollment/Verification Speed | Cost | Other Notes |
|---|---|---|---|---|---|
| **Iris Scanning** | 256 unique characteristics; distinct even in identical twins | More accurate than fingerprint, less than retina; FAR ~1 in 10 million | Enrollment: a few seconds; verification: ≤5s | $200–$2000 (reducing for phones) | Less invasive than retinal scan; unaffected by diseases like glaucoma |
| **Retinal Scanning** | Up to 400 unique characteristics | ~70× more accurate than iris; ~20,000× more accurate than fingerprint | Requires 15s of focus; verification ≥10s | $100K+ | Most invasive; capillary patterns can change with disease (e.g. glaucoma, detachment) |
| **Fingerprint Scanning** | ~1 in 64 billion match chance | ~1 in 100,000 false positives on smartphones | Enrollment ≤1 min; contactless verification <1s, contact verification 5–10s | $30–<$1000 | Doesn't change over time but affected by dryness/injuries |
| **Facial Recognition** | Geometric landmarks (eye distance, nose width, jawline) | >90% accuracy with ML support; FAR ~1 in 1,000,000 | Enrollment/verification <1s | $90–$1500 (reducing for phones) | Less intrusive; can be affected by wearables and aging; unsuitable for pandemic mask-wearing scenarios |

### Hacking Biometrics
- Facial recognition and fingerprinting are vulnerable to **spoofing attacks**.
- Studies show facial recognition false-positive rates for Asian and Black individuals up to **100× higher** than for white individuals — a significant bias/fairness concern.
- Fingerprint spoofing is a real risk for mobile payment authentication.

### Behavioural Biometrics
- Based on *how* you do something (e.g. gait — how you walk/hold yourself), typically captured via computer vision or wearable/floor sensors.
- Sufficient for verification in low-security contexts; with AI support, accuracy can reach ~99.3%.
- Can change over time (e.g. weight gain, joint injuries).
- **Keystroke Dynamics** — measures key hold time and inter-key pauses.
- Implementation cost: gait analysis is significantly more expensive than keystroke dynamics.

### Voice Recognition
- Combines **physical** traits (mouth, nose, tongue shape) and **behavioural** traits (emotional state, illness).
- Not universal (excludes speech-impaired individuals) and not highly distinctive.
- Microsoft's AI speech recognition achieves ~95% accuracy (5.1% error — comparable to humans).
- Can be **text-dependent** (fixed passphrase) or **text-independent** (free speech, requires more enrollment).
- Enrollment tends to be slow (e.g. Google Home); cost is similar to fingerprint scanners.

### Authentication Wrap-Up: Key Selection Factors
1. **Ease of use** — acceptability, ease of enrollment, intrusiveness
2. **Accuracy level needed** — higher accuracy generally means more false alarms
3. **Cost** — budget constraints
4. **Ease of administration/maintenance**

---

## 9. Authorisation

**Definition:** Once a subject is authenticated, authorisation determines whether they are permitted to carry out a specific action.

```
Subject → Access Request → Reference Monitor → Object
```

### Three Main Access Control Models

**1. Discretionary Access Control (DAC)**
- Access rights are assigned based on rules specified by the resource **owner** (the user who created the object).
- Uses **Access Control Lists (ACLs)** and capability tables; the OS checks these to determine allowed access.
- Categories: **Owner** (user), **Group** (defined set of users), **Other/World** (everyone else).
- Example: Microsoft's ACL model (Group and Individual permissions).

**2. Role-Based Access Control (RBAC)**
- Also called *non-discretionary* access control.
- System administrators assign access rights based on **organizational roles**, not individual accounts.
- Supports the **Principle of Least Privilege** — users get only the access needed for their job.
- **Risk — Role Creep:** occurs when a user transfers to a new role but retains access rights from their previous role, since roles aren't reviewed/updated. Requires ongoing role review to prevent.
- Example tools: Centrify, SolarWinds.

**3. Mandatory Access Control (MAC)**
- Access is controlled by the **OS**, based on system-administrator-configured settings, using **security labels**.
- Security labels combine:
  - **Classification** (e.g. Top Secret, Secret, Sensitive, Unclassified)
  - **Category** (specific department/project — enforces "need to know")
- A user is granted access only if both their classification and category match the object's labels.
- **Most secure** access control model, but requires significant planning/management overhead due to constant label updates.

### Principle of Least Privilege (POLP)
- Security best practice: limit privileges to the **minimum necessary** to perform a given job/task.
- Reduces the blast radius if a low-level account, device, or application is compromised.
- **Mobile example:** a flashlight app only needs to control the LED — it should NOT need location, contacts, or SMS access. A real-world banking Trojan disguised as a flashlight app requested device-admin permissions and stole banking credentials, illustrating the risk of over-permissioned apps.

### Separation of Duties (SoD)
- Divides tasks/responsibilities for a process across **multiple people**, so no single individual has complete control.
- Reduces risk of fraud, errors, and security breaches.
- Example: the person who **authorizes** a paycheck should not be the same person who **prepares** it.

---

## Key Takeaways
- Access Control = **Identification → Authentication → Authorisation**.
- Authentication rests on three factor types: **Knowledge** (passwords/passphrases/graphical passwords), **Token** (eToken/smart card/RFID), and **Biometrics** (physiological/behavioural).
- Passwords should always be stored **salted and hashed**, never encrypted-only or plain-hashed — salting defeats precomputed rainbow-table attacks.
- Biometric systems are evaluated on **FAR/TAR** trade-offs (via ROC curves), plus acceptability, accuracy, cost, and maintainability.
- Authorisation models — **DAC** (owner-controlled), **RBAC** (role-controlled, watch for role creep), **MAC** (OS-enforced security labels, most secure but heaviest to administer).
- **Principle of Least Privilege** and **Separation of Duties** are cross-cutting controls that limit the damage any single compromised account or individual can cause.
