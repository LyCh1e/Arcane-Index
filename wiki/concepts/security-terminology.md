---
type: concept
address: c-000105
title: "Security Terminology"
domain: secure-software-development
complexity: medium
created: 2026-07-09
updated: 2026-07-09
tags: [concept, security-terminology, encoding, escaping, sanitisation, encryption, hashing, digital-signatures, authentication, authorisation, federated-identity, owasp]
related:
  - concepts/secure-input-validation
  - concepts/secure-design-implementation
  - concepts/owasp-top-10
  - concepts/security-testing-and-verification
---

# Security Terminology

A precision reference for security terms that are frequently confused — even by experienced developers. Misusing these terms leads to misimplemented controls and misread standards (ASVS, OWASP Top 10). Each section contrasts related terms to make the distinctions explicit.

> Source: OWASP Security Terminology Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Security_Terminology_Cheat_Sheet.html

---

## Data Handling: Encoding, Escaping, Sanitisation, and Serialisation

These four terms relate to how data is *transformed* for transport, storage, or display. They are not interchangeable.

### Encoding

**Definition:** Transforming data into a different format using a publicly available, reversible scheme so that it can be safely consumed by a different system.

| Property | Value |
|---|---|
| Purpose | Data usability and compatibility — not security |
| Reversibility | Always reversible |
| Examples | Base64, URL Encoding (`%20`), HTML Entity Encoding (`&amp;`) |
| Security note | Encoding is **not** a security control; using the wrong encoding can *introduce* vulnerabilities |

**Common mistake:** Treating Base64 as a form of protection. Base64 is trivially reversible and provides no confidentiality.

---

### Escaping

**Definition:** A sub-type of encoding where specific characters are prefixed with a "signal" character (such as a backslash) to prevent the parser from interpreting them as control characters rather than data.

| Property | Value |
|---|---|
| Purpose | Ensure the interpreter treats data as *text*, not *code or commands* |
| Reversibility | Reversible |
| Examples | `\'` in SQL, `\n` in strings, `&lt;` in HTML output |
| Security context | **Essential** for preventing injection attacks (XSS, SQLi, command injection) |

**Encoding vs Escaping:** Escaping is *context-specific* — the same string requires different escaping for SQL, HTML, shell, and JavaScript contexts. Encoding is general-purpose format conversion.

---

### Sanitisation

**Definition:** Cleaning or filtering input by *removing, replacing, or modifying* potentially dangerous characters or content to make "dirty" input "clean" according to a security policy.

| Property | Value |
|---|---|
| Purpose | Remove dangerous content from input |
| Reversibility | Not reversible — content is destroyed |
| Examples | Stripping `<script>` tags from HTML input; removing special characters from a filename |
| Security context | Use as a **secondary** defence; prefer parameterised queries or output escaping as the primary control |

**Sanitisation vs Escaping:** Escaping *preserves* the original data by marking it safe for a specific context. Sanitisation *destroys or transforms* the data. For user-facing output, prefer escaping; for database queries, prefer parameterisation.

**Sanitisation vs Validation:** Validation checks whether input *conforms* to expected format and rejects it if not. Sanitisation *modifies* the input. Validation is generally preferred over sanitisation for security inputs — silently modifying data can mask attacks and introduce unexpected behaviour.

---

### Serialisation

**Definition:** Converting an object or data structure into a format (such as a byte stream, JSON, or XML) that can be stored or transmitted and later reconstructed (deserialised).

| Property | Value |
|---|---|
| Purpose | Data persistence and inter-process/inter-system communication |
| Reversibility | Reversible via deserialisation |
| Examples | JSON, XML, Python `pickle`, Java Object Serialisation |
| Security context | **Insecure Deserialisation** occurs when untrusted data is used to reconstruct an object — can lead to Remote Code Execution (RCE), authentication bypass, or privilege escalation |

**Key danger:** Never deserialise data from an untrusted source without strict type checking and integrity verification. This is OWASP Top 10 A08:2021 — Software and Data Integrity Failures.

---

### Quick Comparison

| Term | Changes data? | Security control? | Primary risk if misused |
|---|---|---|---|
| Encoding | Yes (format) | No | Wrong context → injection |
| Escaping | Yes (marks safe) | Yes | Missing → XSS / SQLi |
| Sanitisation | Yes (destroys content) | Secondary | Over-reliance → missed attacks |
| Serialisation | Yes (structure) | No | Untrusted input → RCE |

---

## Cryptography: Encryption, Hashing, and Signatures

These three terms are frequently conflated. They serve fundamentally different security goals.

### Encryption

**Definition:** Transforming data (plaintext) into an unreadable format (ciphertext) using a secret key.

| Property | Value |
|---|---|
| Security goal | **Confidentiality** — only parties with the key can read the data |
| Reversibility | Reversible — decryption with the correct key restores plaintext |
| Types | **Symmetric** (same key for encryption and decryption) · **Asymmetric** (public key encrypts, private key decrypts) |
| Examples | AES-256 (symmetric), RSA (asymmetric), TLS (uses both) |

**Common mistake:** Using encryption for password storage. Encryption is reversible — if the key is compromised, all passwords are exposed. Use hashing instead.

---

### Hashing

**Definition:** Transforming data into a fixed-size string (a *digest*) using a deterministic mathematical function. The same input always produces the same output; different inputs (should) produce different outputs.

| Property | Value |
|---|---|
| Security goal | **Integrity** — a small change in input produces a completely different hash |
| Reversibility | **One-way — non-reversible** |
| Examples | SHA-256 (general integrity), Argon2 / bcrypt / PBKDF2 (password hashing) |
| Password hashing | Must use a salt (random per-user value prepended before hashing) to prevent rainbow table attacks |

**Encryption vs Hashing:**

| | Encryption | Hashing |
|---|---|---|
| Reversible? | Yes (with key) | No |
| Key required? | Yes | No |
| Purpose | Confidentiality | Integrity / password storage |
| Use for passwords? | **Never** | **Always** (with salt) |

---

### Digital Signatures

**Definition:** Using asymmetric cryptography to provide proof of the **origin** and **integrity** of a message.

| Property | Value |
|---|---|
| Security goals | **Authenticity** (who sent it) + **Non-repudiation** (sender cannot deny it) |
| Mechanism | Sender signs a *hash* of the message with their **private key**; receiver verifies using the sender's **public key** |
| Examples | JWT signatures (HS256 = HMAC, RS256 = RSA), GPG/PGP email signatures, TLS certificate signing |

**Encryption vs Signature:**

| | Encryption | Digital Signature |
|---|---|---|
| Who uses the public key? | Sender (to encrypt) | Receiver (to verify) |
| Who uses the private key? | Receiver (to decrypt) | Sender (to sign) |
| Security goal | Confidentiality | Authenticity + Non-repudiation |

**HMAC vs Digital Signature:** HMAC (Hash-based Message Authentication Code) uses a *shared secret* for integrity and authenticity — both parties know the same key. Digital signatures use *asymmetric* keys — only the private key can sign, anyone with the public key can verify. HMAC requires the verifier to be trusted; digital signatures do not.

---

### Quick Comparison

| Term | Goal | Reversible? | Key type |
|---|---|---|---|
| Encryption | Confidentiality | Yes (with key) | Symmetric or asymmetric |
| Hashing | Integrity / password storage | No | None |
| Digital Signature | Authenticity + non-repudiation | No (hash is signed) | Asymmetric (private signs, public verifies) |

---

## Identity: Authentication and Authorisation

### Authentication (AuthN)

**Definition:** The process of *verifying who a user is*.

| Property | Value |
|---|---|
| Core question | "Who are you?" |
| Factors | **Something you know** (password) · **Something you have** (hardware token, OTP device) · **Something you are** (biometrics) |
| MFA | Two or more factors from different categories |

---

### Authorisation (AuthZ)

**Definition:** The process of *verifying what a user has permission to do*.

| Property | Value |
|---|---|
| Core question | "Are you allowed to do this?" |
| Sequence | Always occurs **after** successful authentication |
| Models | **RBAC** (Role-Based Access Control) — permissions assigned to roles, roles assigned to users · **ABAC** (Attribute-Based Access Control) — permissions based on attributes of the user, resource, and environment |

**Authentication vs Authorisation:**

| | Authentication | Authorisation |
|---|---|---|
| Verifies | *Who* the user is | *What* the user may do |
| Happens | First | After authentication |
| Failure result | 401 Unauthorized | 403 Forbidden |
| Example | Checking username + password | Checking if the logged-in user can delete a record |

> **Common error:** Returning 403 for failed authentication (before identity is established). A 401 indicates the request was not authenticated; a 403 indicates it was authenticated but not authorised.

---

## Federated Identity Terms

When working with OAuth 2.0, SAML, or OpenID Connect (OIDC), these terms appear in specifications and are often confused:

| Term | Definition | Example |
|---|---|---|
| **Identity Provider (IdP)** | The system that creates, maintains, and manages identity information, and provides authentication services to other systems | Google, Microsoft Entra ID (Azure AD), Okta, Auth0 |
| **Relying Party (RP)** | An application or service that *relies on* an IdP to authenticate users on its behalf (OAuth 2.0 / OIDC terminology) | Your web app using "Login with Google" |
| **Service Provider (SP)** | In **SAML**, the equivalent of a Relying Party — the system that provides a service and consumes SAML assertions from an IdP | Your enterprise app using SAML SSO |
| **Principal** | The entity (user, service account, or device) that is being authenticated | The user logging in; a machine account calling an API |

**RP vs SP:** Functionally equivalent — both are the consumer of federated identity. The difference is vocabulary: **RP** is used in OAuth 2.0 and OIDC; **SP** is used in SAML. When a system supports both protocols, it is simultaneously an RP (for OIDC flows) and an SP (for SAML flows).

---

## See Also

- [[concepts/secure-input-validation]] — escaping and sanitisation in context: allow-list validation, SQL injection prevention, ReDoS
- [[concepts/secure-design-implementation]] — authentication design (SRP, FIDO2), authorisation models (RBAC), cryptography at design level
- [[concepts/secure-deployment-practices]] — password hashing in credential storage (bcrypt, PBKDF2), secrets management
- [[concepts/security-testing-and-verification]] — ASVS V2.1 (password requirements), V2.4 (credential storage — hashing requirements), V2.5 (credential recovery)
- [[concepts/owasp-top-10]] — A03 Injection (escaping/sanitisation), A02 Cryptographic Failures (encryption vs hashing), A08 Insecure Deserialisation
- [[resources/owasp-cheat-sheet-series]] — full catalogue; see SQL Injection Prevention, Input Validation, Password Storage, Cryptographic Storage, Session Management
- [[sources/owasp-security-terminology-cheat-sheet]] — source page
