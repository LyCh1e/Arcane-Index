---
type: index
title: "Study Notes — Index"
updated: 2026-11-19
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

## Daily Read Topic Scopes

> [!info] Read by the tutor agent on every daily-read run
> A module with an entry below is restricted to part of its syllabus: **every** topic on its daily-read page — lecture subtopics, the lab section, and all 20 quiz questions — must come from inside that scope. A module with no entry covers its full syllabus as usual. Only the user sets or changes these; edit or delete an entry here to change or lift a restriction — nothing in `agents/tutor.md` needs to change. This affects the daily reads only, not the study notes or formula sheets.

### INF2005 — restricted to five topic areas (set by the user on 2026-11-16, in force until the user changes it)

| # | In-scope topic area | Where it lives in the INF2005 notes file |
|---|---|---|
| 1 | Social Engineering (self-study, Week 6) — **low weight: fewer than 3 exam questions** | §8 Social Engineering |
| 2 | System Security and Malware (Week 8) | §9 Malware, §10 System Security |
| 3 | Network Security and Defences (Week 9) | §11 Network Security Attacks, §11A Network Security Defence |
| 4 | System and Network Forensics (Week 10) | §11B Digital Forensics |
| 5 | IoT Security or Attacks (self-study, Week 11) | §11C IoT Security |

**Out of scope — do not select, write about, or quiz on:** §1 Foundations,
§2 Symmetric Cryptography, §3 Asymmetric Cryptography, §4 Hashing, Digital
Signatures & Cryptanalysis, §5 Steganography, §6 Access Control and §7
Ethical Hacking, and the two lab files that belong to them
(`inf2005-lab-wk1-cryptography.md`, `inf2005-acw1-stego-verification.md`).
From §12/§13 (summary tables, common exam mistakes) use only the rows that
concern an in-scope area.

How to work inside this scope:

- **Weighting.** Spread the lecture subtopics evenly across areas 2–5.
  Social Engineering (area 1) carries little exam weight, so give it at
  most **one** subtopic on a page, never on two consecutive runs, and
  roughly one run in three at most.
- **More depth for the short sections.** §11A, §11B and §11C are brief in
  the notes file. Also read their full concept pages —
  `wiki/concepts/network-security-defence.md`,
  `wiki/concepts/digital-forensics.md`, `wiki/concepts/iot-security.md` —
  and, for Social Engineering, `wiki/sources/inf2005-csf-social-engineering.md`,
  so each area splits into several distinct subtopics (e.g. forensics:
  evidence integrity & the Pollitt model; Windows artefacts; Linux
  artefacts; web-log attack signatures; packet analysis & scan detection)
  rather than one catch-all subtopic repeated every few days.
- **A smaller pool repeats sooner.** The "not in the last 5 runs" rule will
  often be impossible to satisfy. Apply the tutor's usual fallback (pick the
  in-scope subtopic covered longest ago) and take a genuinely different
  angle, example and set of sub-facts from its last appearance — the
  same way a revisited lab file gets a new angle. The rule that a subtopic
  must not repeat from the immediately previous run still holds.
- **Lab slot.** The only in-scope lab file today is
  `inf2005-acw3-mod-dav-fs-proppatch-dos.md` (a web-server DoS — system and
  network security). Use it for the lab section only when it was **not**
  the lab on the previous run and a new angle on it is available;
  otherwise fill the fourth slot with a **fourth in-scope lecture
  subtopic** instead, so the page still has four sections and 20 questions
  (about 5 each). Any INF2005 lab file added later joins the lab pool only
  if its subject falls inside the five areas.
- **Quiz.** Every question tests in-scope content. An out-of-scope idea
  may appear only where an in-scope topic genuinely relies on it (e.g.
  SHA-256 hashing for evidence integrity in forensics) and must never be
  the thing being tested.
- **Rotation history.** INF2005 entries dated before 2026-11-16 in
  `study-notes/log.md` include out-of-scope topics; leave them as a
  historical record and ignore them when choosing.

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
| **ICT3113 POD** | Performance metrics · Utilisation law · Little's Law · M/M/1 queueing · Multi-server queues (M/M/c) · Operational laws (Forced Flow, Service Demand) · Bottleneck analysis · Kingman formula · Sakasegawa formula · Interactive Response Time Law · Four Sources Framework · Performance testing types (load, stress, soak, regression, benchmark, pipe-clean) · Open-loop vs closed-loop load generation · JMeter test plan sizing (Little's Law bridge, APDEX) · Lost work and Erlang B (formula, recursion, table, sizing) · Reading a stress table by column (knee, ceiling, failure mode) and the serialisation signature (Lab Wk 11) · Connection pool as a c-server queue, hold time, three causes and three instruments (Lab Wk 12) · Database request hold time: N+1 queries, `EXPLAIN ANALYZE`, indexes, histograms, non-sargable queries, saga pattern (Lec09) |
| **INF2005 CSF** | CIA triad · Symmetric crypto (substitution, transposition, DES/3DES/AES, OTP) · Kerckhoffs's Principle · Asymmetric crypto (RSA, Diffie–Hellman) · Hashing & digital signatures · Cryptanalysis (brute force, frequency analysis, known plaintext, birthday attack) · Steganography (LSB, BPCS, steganalysis) · Access control (passwords, biometrics, DAC/RBAC/MAC) · Ethical hacking (CMA, hat types, pen testing stages) · Social engineering (Cialdini principles, phishing/spear/whaling/BEC, vishing, pretexting, deepfakes, MFA fatigue) · Malware (virus/worm/trojan, infection vectors, polymorphic/metamorphic, signs of infection) · System security (hardware/software/OS/hypervisor attacks, privilege escalation, ransomware/WannaCry) · Network security (DoS/DDoS/DRDoS, Evil Twin, ARP poisoning, packet sniffing, port scanning, DPI) · Network defence (defence in depth, stateless/stateful firewall, NIDS/NIPS, application proxy, IPsec/OpenVPN, MAC flooding/port security, RADIUS/TACACS) · Digital forensics (evidence integrity, Pollitt model, Windows registry/event logs, Linux logs, web-log attack signatures, packet analysis, vertical/horizontal scan detection) · IoT security (Mirai, Jeep hack, five device challenges, buffer overflow/code injection/XSS, default passwords, botnet enslaving, data leakage) · Nmap scan types (SYN/Connect/UDP, -O, -sV, NSE) · Wireshark analysis (cleartext Telnet/FTP, FTP brute force, MSN, SIP/RTP) |

---

## See Also

- [[ICT3113 - Performance Testing and Optimisation Cheat Sheet]] — ICT3113 testing types, JMeter sizing, Erlang B, optimisation levers and connection-pool diagnosis with formulas and worked examples
- [[wiki/index|Wiki Index]] — master catalogue of all ingested sources, concepts, and pages
- [[wiki/hot|Recent Context]] — latest session output (~300 words)
- [[wiki/log|Operation Log]] — chronological record of every ingest and update
