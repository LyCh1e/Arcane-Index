---
type: concept
status: established
created: 2026-06-25
updated: 2026-06-25
address: c-000068
title: "FIDO, Passkeys, and Passwordless Authentication"
domain: secure-software-development
complexity: high
tags: [fido, passkeys, passwordless, authentication, otp, mfa, phishing, webauthn, biometrics, security]
---

# FIDO, Passkeys, and Passwordless Authentication

Passwords are the leading attack surface for credential theft, phishing, and account takeover. Passwordless authentication eliminates the shared-secret problem entirely — replacing passwords with cryptographic mechanisms tied to devices the user possesses.

---

## Why Passwordless?

| Benefit | Explanation |
|---------|-------------|
| **Improved UX** | No passwords to remember or type — particularly valuable on mobile |
| **Enhanced security** | Passwords are reused, shared, phishable, and breachable; passkeys are not |
| **Lower TCO** | Password reset support is expensive; passwordless removes that overhead |

> **The database does NOT store ANY password.** This is the core architectural difference — there is nothing to breach.

---

## OTP / Magic Link Approach (Simple Passwordless)

The lightest-weight passwordless pattern:

1. User enters their mobile phone number or email address
2. System issues a **one-time code or magic link** sent to that address
3. User clicks or enters the code; system authenticates

**Security constraints (ICT2216 standard):**
- Only the **most recent** code issued is valid; any previous codes are immediately invalidated upon issuing a new one
- Once used, the code is also invalidated (single-use)
- Maximum **three failed attempts** per code — after three failures, the user must request a new code
- Codes expire after **three minutes** by default

**Preventing phishing:** Bind the code to context (device fingerprint, IP address, browser session) so a code intercepted and replayed from a different context is rejected.

> **Does passwordless OTP replace 2FA?** The OTP code itself acts as a "something you have" factor (possession of the phone/inbox). Whether a second factor is required depends on your threat model, but pure OTP passwordless already achieves one strong factor without a separate password factor.

**Limitation:** SMS and email possession alone are **not sufficient proof of identity** — they are factors, not identities. Phone numbers can be SIM-swapped; email can be compromised.

**Third-party login services** (e.g., "Login with Google") are a related but distinct pattern — they delegate authentication to an identity provider. The disadvantage is dependency on the provider's availability and loss of control over your user authentication flow.

---

## FIDO Alliance

The **FIDO ("Fast IDentity Online") Alliance** is an open industry association launched in **February 2013**.

**Mission:** Develop and promote authentication standards that reduce the world's over-reliance on passwords.

**Supported authenticator types:**
- Biometrics — fingerprint scanners, iris scanners, facial recognition
- Voice recognition
- Trusted Platform Modules (TPM)
- USB security keys (hardware tokens)
- Embedded Secure Elements (eSE), smart cards, and NFC
- Device PIN (fallback)

**FIDO specifications:**
- **FIDO UAF** — Universal Authentication Framework (passwordless on mobile)
- **FIDO U2F** — Universal 2nd Factor (hardware security key as second factor)
- **FIDO2 / WebAuthn** — the current standard; passkeys are FIDO2 credentials

---

## Passkeys

**Passkeys** are "discoverable" FIDO2 credentials — a password replacement providing faster, easier, and more secure sign-ins across a user's devices. Cryptographic private keys reside **only on end-user devices** (computers, phones, or security keys) and **never leave them**.

### Registration Flow

| Step | What Happens |
|------|-------------|
| 1 | User selects an available FIDO authenticator matching the service's acceptance policy |
| 2 | User **unlocks** the authenticator (fingerprint, face scan, PIN, button press) |
| 3 | Authenticator generates a **new public/private key pair** unique to: this device + this service + this user account |
| 4 | **Public key** is sent to and stored by the online service. The **private key and local auth method details never leave the device** |

### Login Flow

| Step | What Happens |
|------|-------------|
| 1 | Service sends a cryptographic **challenge** to the user's registered device |
| 2 | User **unlocks** the authenticator (same method as registration) |
| 3 | Authenticator uses the account's private key to **sign the challenge** |
| 4 | Client sends the signed challenge back; service **verifies using the stored public key** and grants access |

**Why passkeys defeat phishing:** The key pair is bound to the exact origin (domain) during registration. A phishing site with a different domain cannot trigger authentication for the legitimate service's key pair — the authenticator refuses.

### Platform Implementations

| Vendor | Approach |
|--------|----------|
| **Google** | Smart Lock app + Bluetooth proximity; four sign-in variants; backup code recommended |
| **Apple** | Requires initial username/password login; secondary device approval; QR code scanning; credentials synced via iCloud Keychain |
| **Microsoft** | Approval prompts to Authenticator app; one-time code still available; **number matching** required in approval prompts to prevent MFA fatigue attacks (users pressing "Approve" without reading) |

---

## Passkey Limitations

Despite the elegance of FIDO2/WebAuthn, **real-world usability is a serious concern** (Ars Technica, 2024):

### Cross-Platform Inconsistency

- The experience of logging in with a passkey on Windows differs from iOS, which differs from Android
- Some browsers (e.g., Firefox) are not supported on certain platforms (e.g., PayPal does not support Firefox passkeys on any OS)

### Management Confusion

- A passkey created in one browser may display misleading metadata (e.g., "Firefox on Mac OS X 10" even when working across all browsers/OSes)
- FIDO2/WebAuthn specifications only expose the **browser and OS used at creation time** — cross-platform interoperability metadata does not exist in the spec
- Password managers (e.g., 1Password) cannot coordinate with services to present consistent information

### Platform Lock-In

- When enrolling a USB security key, macOS may preempt the process and steer the user toward creating an iCloud-synced passkey instead
- Competing platforms (Google, Apple) may "hijack" the authentication process to promote their own ecosystem

> **Conclusion:** Passkeys are elegantly designed but currently **cannot be considered usable security** — defined as a security measure that is as easy, or only incrementally harder to use, than less-secure alternatives. The cryptographic foundation is sound; the UX layer is fragmented and confusing.

---

## Choosing an Authentication Pattern

| Scenario | Recommended Approach |
|----------|---------------------|
| Consumer web app, broad device support needed | OTP / magic link (simpler, universal) |
| High-security, tech-savvy users | FIDO2 passkeys |
| Enterprise with managed devices | FIDO2 + platform SSO (e.g., Windows Hello for Business) |
| Must support legacy browsers | MFA with TOTP (e.g., Google Authenticator) |
| Regulatory environment (finance, healthcare) | MFA mandatory; evaluate passkeys as second factor |

---

## Related

- [[concepts/secure-design-implementation]] — Authentication design (factor types, MFA, SSO, RBAC); SSL/TLS analysis and why phishing survives common defences
- [[concepts/mcp-security]] — Phishing-adjacent: prompt injection and tool poisoning as parallel threat patterns in agentic contexts
- [[concepts/secure-software-requirements]] — CIA-AAA requirements: Authentication pillar
- [[sources/ICT2216-lecture6-secure-implementation]] — Source lecture
