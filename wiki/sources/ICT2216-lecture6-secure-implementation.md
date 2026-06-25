---
type: source
status: established
created: 2026-06-25
updated: 2026-06-25
title: "ICT2216 Lecture 6 — Secure Software Implementation (Part 1: Introduction to CI/CD)"
source_type: course notes
author: Raymond Chan, Singapore Institute of Technology
date_published: 2026-01-01
confidence: high
tags: [ict2216, secure-software-development, devsecops, ci-cd, ssl-tls, passwordless, fido, passkeys, github-actions, hsts, pfs, srp]
related:
  - "[[concepts/secure-design-implementation]]"
  - "[[concepts/fido-passkeys-passwordless]]"
  - "[[concepts/github-actions-cicd]]"
---

# ICT2216 Lecture 6 — Secure Software Implementation (Part 1)

## Summary

Lecture 6 of ICT2216 — Secure Software Development (SIT). Covers four topics: DevOps/DevSecOps definitions and CI/CD pipeline security; a critical analysis of SSL/TLS and password storage limitations; passwordless authentication via OTP/magic link; and FIDO passkeys (registration/login flows, platform implementations, usability limitations).

## Key Claims

- DevSecOps embeds security throughout CI/CD rather than treating it as an end-gate; it extends Agile beyond the software team
- The fundamental incompatibility table: SSL/TLS does not protect against phishing; salted hashing forces cleartext transmission; 2FA/OTP does not protect against real-time phishing proxies
- Salted hash password storage is correct for at-rest storage but forces the client to transmit plaintext, which a phishing server receives unimpeded by TLS
- HSTS mitigates MitM SSL stripping; PFS prevents retrospective decryption of captured sessions; SRP (RFC 5054, 2007) addresses phishing + MitM + PFS but was not widely adopted
- Passkeys (FIDO2/WebAuthn) are cryptographically sound but cross-platform UX is fragmented; cannot currently be considered "usable security" per the Ars Technica 2024 analysis
- OTP passwordless: codes expire in 3 minutes; max 3 failed attempts per code; only the most recently issued code is valid

## Sections

1. DevOps / DevSecOps (origins, definitions, extending Agile)
2. CI/CD Pipeline and Security (CI vs Continuous Delivery vs Continuous Deployment, GitHub Actions project requirement)
3. SSL/TLS and Password Storage review (incompatibility table, phishing resilience, MitM stripping, HSTS, cipher suite selection, PFS, SRP, Security Theatre)
4. Passwordless OTP/magic link (design constraints, brute-force mitigations)
5. FIDO Alliance and Passkeys (registration/login flow, Google/Apple/Microsoft implementations, limitations)

## Concepts Generated

| Concept | Type | Action |
|---------|------|--------|
| [[concepts/fido-passkeys-passwordless]] | new | Created |
| [[concepts/secure-design-implementation]] | existing | Updated — SSL/TLS analysis section added |
| [[concepts/github-actions-cicd]] | existing | Updated — DevSecOps intro + CI/CD distinction table added |
