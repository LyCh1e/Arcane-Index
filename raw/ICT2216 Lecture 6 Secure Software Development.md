# ICT2216: Secure Software Development
## Lecture 6 – Secure Software Implementation (Part 1: Introduction to CI/CD)
*Lecturer: Raymond Chan*

---

## Agenda

1. Introduction to DevOps/DevSecOps
2. CI/CD Pipeline and Security
3. Review on Security of SSL/TLS and Password Storage
4. Introduction to Passwordless System

---

## 1. Introduction to DevOps / DevSecOps

### DevOps Origins
- The term **DevOps** traces back to **Patrick Debois**, who started **DevOpsDays in 2009** to bridge the gap between developers and operations teams and achieve faster software delivery and deployment.
- DevOps may be considered as **extending Agile beyond the software team**.

### What is DevOps?
> DevOps is the process of **continuously improving software applications with small changes and small risks** (in contrast to BIG changes which carry BIG risks).

Reference: https://www.devops.ch/2017/05/10/devops-explained/

### What is DevSecOps?
- **DevSecOps** (also written as DevOpsSec or SecDevOps) is the inclusion of **security and compliance into DevOps**.
- Security is embedded throughout the development pipeline rather than being an afterthought.

---

## 2. CI/CD Pipeline and Security

### Key Concepts
- To achieve DevOps/DevSecOps, one key methodology is to use **automation tools** to implement **Continuous Integration and Continuous Delivery or Deployment (CI/CD)**.

| Term | Description |
|------|-------------|
| **Continuous Integration (CI)** | Automated build and test on every code commit |
| **Continuous Delivery (CD)** | Automated up to deployment-ready stage; **manual** trigger for production deployment |
| **Continuous Deployment (CD)** | Fully **automated** deployment to production without manual approval |

> **Key difference:** Continuous Delivery vs Continuous Deployment = manual process for deployment vs automatic.

### Tools for CI/CD
Common CI/CD tooling includes platforms such as Jenkins, GitHub Actions, GitLab CI, and others.

### GitHub Actions
- Automation of CI/CD can be specified as a **workflow** stored in `.github/workflows/`
- Supports use cases from simple CI to comprehensive CD pipelines
- **Project requirement:** Your project must cover at least the **Build** and **Test** stages.

#### GitHub Actions Workflow Example
In a typical workflow, `setup`, `build`, and `test` jobs run in series, with each step dependent on the successful completion of the preceding one:

```yaml
# Conceptual example structure
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up environment
        run: ...

  build:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: Build application
        run: ...

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: ...
```

Reference: https://www.jenkins.io/doc/book/pipeline/

---

## 3. Review on Security of SSL/TLS and Password Storage

### The Core Problem
Most developers implement **SSL/TLS** and **salted hash password storage** as standard security solutions — but are they truly effective?

### The Fundamental Incompatibility Table

Different security mechanisms are often **incompatible** with each other in ways developers do not appreciate:

| Security Measure | Protects Against | Does NOT Protect Against |
|------------------|-----------------|--------------------------|
| SSL/TLS | Eavesdropping (encrypted channel) | Phishing (attacker controls the server) |
| Salted Hash Password Storage | Password database breach | Phishing (password still transmitted in clear) |
| 2FA/OTP | Replayed stolen passwords | Real-time phishing (attacker proxies the OTP) |

### Why Salted Hash Forces Cleartext Transmission

If implementing **salted hash password storage**, you have no other option but to require users to send their passwords in clear (possibly "protected" over HTTPS). Why?

> **Hash is a one-way function.** The server needs the original user password to go through the same hash function to generate a hash value for comparison with the stored hash.

### Why Phishing Remains Feasible Despite SSL/TLS

- Implementing **password encryption within SSL/TLS is useless** because you would have established the encryption key with the **attacker's server** instead of the legitimate one.
- As a result, **phishing attacks remain feasible and attractive** even when SSL/TLS is prevalent.

### Man-in-the-Middle (MitM) SSL Stripping Attack

- Be aware of potential **MitM SSL stripping attacks** when implementing SSL/TLS.
- An attacker intercepts HTTP traffic before HTTPS is established, downgrading the connection.

### Solution: HTTP Strict Transport Security (HSTS)

- **HSTS** is a possible mitigation — it instructs browsers to only communicate over HTTPS, preventing SSL stripping.

### Cipher Suite Selection

A **cipher suite** specifies the key exchange and authentication protocols, together with encryption and hash/MAC algorithms to be used.

**Example:** `TLS_RSA_WITH_AES_128_GCM_SHA256`

| Component | Example Value |
|-----------|---------------|
| Key exchange/authentication | RSA |
| Encryption | AES_128_GCM |
| Hash/MAC | SHA256 |

### Perfect Forward Secrecy (PFS)

- In 2013, **Snowden** disclosed top-secret worldwide global mass surveillance, revealing that past encrypted communications could be decrypted if private keys were compromised.
- You should **only configure SSL/TLS to support cipher suites that achieve perfect forward secrecy (PFS)**.
- **PFS** ensures that compromise of private SSL keys will **not** compromise past communications.

### Secure Remote Password (SRP) Protocol

A security protocol that addresses phishing, MitM SSL stripping, and achieves perfect forward secrecy:

**SRP Flow:**
1. **Step 1:** User enters username and password *before* contacting any server.
2. **Step 2:** If key establishment is successful, the website is authentic and the webpage can be seen; if not, the password remains safe.

> SRP has been standardised since **2007 (RFC 5054)** for SSL/TLS (e.g. `TLS_SRP_SHA_WITH_AES_128_CBC_SHA`) but was **not widely adopted** — because the website cannot authenticate the user before an account is created.

### Security Theatre Warning

> **Security Theatre:** Is security implemented just for show to make you *feel* secure, or is it actually making you *more* secure?

- Do not blindly follow the crowd in implementing security solutions.
- Think deeper about whether your implementation actually addresses the threat model.

---

## 4. Introduction to Passwordless System Implementation

### Motivation (Recap from Lecture 4)
- Major platforms including Apple (iOS 16), Google (Android 13), and Microsoft have committed to expanded support for the **FIDO standard** for passwordless sign-ins.

### Why Passwordless?

| Benefit | Explanation |
|---------|-------------|
| **Improved UX** | Particularly on mobile — no passwords to remember |
| **Enhanced security** | Passwords are a major vulnerability; users reuse and share them |
| **Lower TCO** | Managing passwords is expensive |

### How Passwordless Works (OTP/Magic Link Approach)

- User enters their **mobile phone number or email address** and receives a **one-time code or link** to log in.
- **Key idea: The database does NOT store ANY password.**

> **Question:** Do you need 2FA if you implement passwordless? *(Consider what factor passwordless already covers.)*

### Using Third-Party Login Services

- Third-party login services (e.g., "Login with Google") are available but are **NOT permitted for the project**.
- Disadvantage: Dependency on the third-party provider; loss of control over authentication.

### Passwordless Best Practices

1. **SMS and Email as Authentication Factors**
   - Phone numbers alone are **not sufficient** for user authentication.
   - Email address possession alone is **not sufficient** for user authentication.

2. **Preventing Phishing Attacks**
   - Implement measures such as binding codes to context (device, IP, etc.).

3. **Preventing Brute Force Attacks**
   - Only the **most recent** one-time-use code (or link) issued will be accepted. When the latest is issued, any previous codes are invalidated. Once used, the latest one is also invalidated.
   - Only **three failed attempts** to input any single one-time-use code are allowed. After this, a new code must be requested.
   - The one-time-use code is valid for **three minutes** (by default) before it expires.

Reference: https://auth0.com/docs/authenticate/passwordless

---

## 5. FIDO and Passkeys

### FIDO Alliance

- The **FIDO ("Fast IDentity Online") Alliance** is an open industry association launched in **February 2013**.
- Mission: develop and promote authentication standards that **"help reduce the world's over-reliance on passwords"**.

**Supported authentication technologies:**
- Biometrics (fingerprint, iris scanners)
- Voice and facial recognition
- Trusted Platform Modules (TPM)
- USB security tokens
- Embedded Secure Elements (eSE), smart cards, and NFC

Reference: https://en.wikipedia.org/wiki/FIDO_Alliance / https://fidoalliance.org/how-fido-works/

### FIDO Passkeys

- **Passkeys** are a password replacement providing faster, easier, and more secure sign-ins across a user's devices.
- Passkeys are **"discoverable" FIDO credentials** for passwordless authentication.
- Cryptographic keys reside on end-user devices (computers, phones, or security keys).

### Passkey – Registration Flow

| Step | Description |
|------|-------------|
| 1 | User chooses an available FIDO authenticator that matches the online service's acceptance policy |
| 2 | User unlocks the FIDO authenticator (fingerprint, PIN, button, etc.) |
| 3 | Device creates a **new public/private key pair** unique to: local device + online service + user's account |
| 4 | **Public key** is sent to and stored by the online service. The **private key** and local authentication method details **never leave the local device** |

### Passkey – Login Flow

| Step | Description |
|------|-------------|
| 1 | Online service challenges the user to login with a previously registered device |
| 2 | User unlocks the FIDO authenticator using the same method as registration |
| 3 | Device uses the user's account identifier to select the correct key and **signs the service's challenge** |
| 4 | Client sends the signed challenge back; service **verifies with the stored public key** and logs in the user |

### Passkey Implementations

| Vendor | Implementation Notes |
|--------|---------------------|
| **Google** | Smart Lock App + Bluetooth proximity; 4 ways to sign in; backup code recommended |
| **Apple** | Requires initial username/password login; secondary device authentication; QR code scanning stores credentials in local storage |
| **Microsoft** | Similar to Google; one-time code still available; **number matching** in approval prompts to prevent MFA fatigue attacks (user pressing "Approve" without awareness) |

References:
- https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys
- https://developers.google.com/identity

### Passkey Limitations

Despite the elegance of the FIDO2/WebAuthn specification, **real-world usability is a significant concern**:

#### Cross-Platform Inconsistency
- The experience of logging into a site with a passkey on Windows differs from iOS, which differs from Android.
- Some browsers (e.g., Firefox) may not be supported on certain platforms (e.g., PayPal does not support Firefox passkeys on any OS).

#### Management Confusion
- A passkey created in one browser may display with misleading metadata (e.g., showing "Firefox on Mac OS X 10" even when working across all browsers/OSes).
- FIDO2/WebAuthn specs only expose the browser and OS used *at creation time* — cross-platform interoperability metadata does not exist.
- Password managers (e.g., 1Password) have no way to coordinate with services to present consistent information.

#### Steering Users Toward Platform Lock-in
- When a user tries to enroll a physical security key (USB dongle), macOS may preempt the process and steer them toward creating an iCloud-synced passkey instead.
- Competing platforms (Google, Apple) may "hijack" the authentication process to promote their own ecosystem.

> **Conclusion:** Passkeys are elegantly designed but currently **cannot be considered usable security** — defined as a security measure that is as easy, or only incrementally harder, to use than less-secure alternatives.

Reference: https://arstechnica.com/security/2024/12/passkey-technology-is-elegant-but-its-most-definitely-not-usable-security/

---

## Key Takeaways

| Theme | Key Point |
|-------|-----------|
| DevSecOps | Security must be embedded throughout CI/CD, not bolted on at the end |
| CI/CD | GitHub Actions workflows must cover at minimum Build and Test stages |
| SSL/TLS | Salted hashes force cleartext password transmission; phishing remains viable; use PFS cipher suites only |
| HSTS | Mitigates MitM SSL stripping attacks |
| SRP | Addresses phishing + MitM + PFS but not widely adopted |
| Passwordless | Eliminates stored passwords; OTP codes expire in 3 min; max 3 failed attempts |
| FIDO/Passkeys | Cryptographically sound but cross-platform UX is fragmented and confusing |
| Security Theatre | Always ask whether a security measure actually reduces risk, or merely looks like it does |

---

## References

- https://www.jenkins.io/doc/book/pipeline/
- https://auth0.com/docs/authenticate/passwordless
- https://en.wikipedia.org/wiki/FIDO_Alliance
- https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys
- https://developers.google.com/identity
- https://fidoalliance.org/how-fido-works/
- https://arstechnica.com/security/2024/12/passkey-technology-is-elegant-but-its-most-definitely-not-usable-security/
- https://www.devops.ch/2017/05/10/devops-explained/
