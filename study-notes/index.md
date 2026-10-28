---
type: index
title: "Study Notes — Index"
updated: 2026-10-28
tags: [index, study-notes]
---

> **Part of the Arcane-Index wiki** — [[wiki/index|Wiki Index]] · [[wiki/hot|Recent Context]]

# Study Notes

All exam notes and formula sheets in this folder. Each module has a full notes file and a compact formula/cheat sheet.

---

## Create Study Notes For

> [!tip] Auto-Update
> The `update-study-notes` skill reads this table at the end of every session. Add a row to track a new module; set **Auto-Update** to `yes` to have study notes refreshed automatically whenever new content is ingested for that course.

| Module | Title | Source Pattern | Notes File | Formula Sheet | Auto-Update |
|--------|-------|---------------|------------|---------------|-------------|
| ICT3112 | Software Verification and Validation | `ict3112` | [[ICT3112 - Software Verification and Validation Exam Notes]] | [[ICT3112 - Formula Sheet]] | yes |
| ICT3113 | Performance Optimisation and Design | `ict3113` | [[ICT3113 - Performance Optimisation Exam Notes]] | [[ICT3113 - Formula Sheet]] | yes |
| INF2005 | Cyber Security Fundamentals | `inf2005` | [[INF2005 - Cyber Security Fundamentals Exam Notes]] | [[INF2005 - Formula Sheet]] | yes |

**Source Pattern** is matched against filenames in `wiki/sources/` — any source page whose filename contains the pattern belongs to that module.

---

## Modules

| Module | Title | Notes | Formula Sheet |
|--------|-------|-------|---------------|
| **ICT3112** | Software Verification and Validation | [[ICT3112 - Software Verification and Validation Exam Notes]] | [[ICT3112 - Formula Sheet]] |
| **ICT3113** | Performance Optimisation and Design | [[ICT3113 - Performance Optimisation Exam Notes]] | [[ICT3113 - Formula Sheet]] |
| **INF2005** | Cyber Security Fundamentals | [[INF2005 - Cyber Security Fundamentals Exam Notes]] | [[INF2005 - Formula Sheet]] |

---

## Coverage Summary

| Module | Topics Covered |
|--------|---------------|
| **ICT3112 SVV** | V&V fundamentals · Static vs dynamic · V-Model · ISTQB principles · Reliability (MTTF/MTTR/MTBF, Musa models) · Static analysis · Whitebox testing (CFG, coverage criteria, cyclomatic complexity, basis paths, LCSAJ) · Blackbox testing (use case, EP, BVA, decision tables, state transition) · Browser-based system testing (Selenium WebDriver, explicit waits, Page Object, CI) · Hoare logic (partial/total correctness, 6 inference rules, WP calculus) · Loop invariants (4 obligations, 5-step recipe) · Array rules (ARRAY-READ, ARRAY-ASSIGN) · Frama-C / ACSL (contracts, RTE annotations, pointer validity, loop annotations, vacuity, ACSL array patterns) |
| **ICT3113 POD** | Performance metrics · Utilisation law · Little's Law · M/M/1 queueing · Multi-server queues (M/M/c) · Operational laws (Forced Flow, Service Demand) · Bottleneck analysis · Kingman formula · Sakasegawa formula · Interactive Response Time Law · Four Sources Framework · Performance testing types (load, stress, soak, regression, benchmark, pipe-clean) · Open-loop vs closed-loop load generation · JMeter test plan sizing (Little's Law bridge, APDEX) · Lost work and Erlang B (formula, recursion, table, sizing) |
| **INF2005 CSF** | CIA triad · Symmetric crypto (substitution, transposition, DES/3DES/AES, OTP) · Kerckhoffs's Principle · Asymmetric crypto (RSA, Diffie–Hellman) · Hashing & digital signatures · Cryptanalysis (brute force, frequency analysis, known plaintext, birthday attack) · Steganography (LSB, BPCS, steganalysis) · Access control (passwords, biometrics, DAC/RBAC/MAC) · Ethical hacking (CMA, hat types, pen testing stages) · Social engineering (Cialdini principles, phishing/spear/whaling/BEC, vishing, pretexting, deepfakes, MFA fatigue) · Malware (virus/worm/trojan, infection vectors, polymorphic/metamorphic, signs of infection) · System security (hardware/software/OS/hypervisor attacks, privilege escalation, ransomware/WannaCry) · Network security (DoS/DDoS/DRDoS, Evil Twin, ARP poisoning, packet sniffing, port scanning, DPI) |

---

## See Also

- [[ICT3113 - Performance Testing and Optimisation Cheat Sheet]] — ICT3113 testing types, JMeter sizing, Erlang B and optimisation levers with formulas and worked examples
- [[wiki/index|Wiki Index]] — master catalogue of all ingested sources, concepts, and pages
- [[wiki/hot|Recent Context]] — latest session output (~300 words)
- [[wiki/log|Operation Log]] — chronological record of every ingest and update
