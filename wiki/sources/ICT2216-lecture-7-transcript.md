---
type: source
address: c-000099
title: "ICT2216 Lecture 7 — Spoken Lecture Transcript"
domain: secure-software-development
course: ICT2216
source_type: lecture-transcript
raw: raw/ICT2216-lecture-7-transcript-2026-07-09.md
companion: "[[sources/ICT2216-lecture-7-secure-coding]]"
created: 2026-07-09
updated: 2026-07-09
tags: [source, ICT2216, transcript, secure-coding, stored-procedures, version-pinning, leap-seconds, log-injection, zip-bomb]
---

# ICT2216 Lecture 7 — Spoken Lecture Transcript

Companion source to [[sources/ICT2216-lecture-7-secure-coding]] (the structured slide notes). The transcript contains classroom discussion, Q&A, and supplementary explanations not present in the structured notes. No new concept pages created — insights appended to [[concepts/secure-input-validation]] and [[concepts/secure-deployment-practices]].

## New Insights Not in the Structured Notes

### Stored Procedures — Schema Leakage Argument

Prepared statements embed SQL query strings in source code, exposing table and column names if the source is leaked. Stored procedures only expose function names; the internal SQL and schema remain hidden inside the database. Appended to [[concepts/secure-input-validation#Defence 2 — Stored Procedures]] under an expanded schema-leakage rationale.

### Version Pinning Debate

Minor updates (patch/minor semver): safe to auto-apply; almost always bug fixes and security patches. Major updates: manual review required. The alternative to pinning is comprehensive automated testing that catches regressions. Appended to [[concepts/secure-deployment-practices#Monitor and Update Continuously]].

### Leap Seconds and POSIX Time

POSIX/Unix epoch time (seconds since 1970-01-01 00:00:00 UTC) sidesteps the leap-second problem because it counts seconds monotonically — no 23:59:60 edge case in the storage layer. Timestamp-format storage does not have this property. Regex time validators must either accept :60 or risk rejecting valid timestamps during a leap second event. Appended to [[concepts/secure-input-validation]] under a new "Real-World Edge Cases in Input Validation" section.

### Log Injection → Reverse Shell

Log injection is not only a forensic contamination risk — IS students learn it in Ethical Hacking as a reverse-shell technique. Unsanitised input written to logs can inject shell commands executed by log-processing systems, followed by attacker deletion of the log entry to eliminate the audit trail. Appended to [[concepts/secure-deployment-practices#The Four Implementation Rules]].

### ZIP Bomb (File Upload)

ZIP bomb (CPOM attack): a small compressed file that decompresses to an enormous size, causing disk/RAM exhaustion (DoS). File upload security must include decompressed-size limits and ZIP bomb detection, not just extension/header checking and malware scanning. Appended to [[concepts/secure-deployment-practices#File Upload Security Checklist]].

### Open vs Closed Source

Neither is inherently more secure — maintenance, testing, and patch response quality determine actual security. Internal audits (analogous to the D3 assessment) are a valid security model for closed-source projects.

## Related Pages

- [[sources/ICT2216-lecture-7-secure-coding]] — companion structured notes (c-000096)
- [[concepts/secure-input-validation]] — updated with leap seconds, stored procedure schema rationale
- [[concepts/secure-deployment-practices]] — updated with version pinning debate, log injection reverse shell, ZIP bomb
