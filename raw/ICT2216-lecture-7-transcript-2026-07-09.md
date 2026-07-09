---
source_type: lecture-transcript
fetched: 2026-07-09
course: ICT2216
lecture: 7
title: "Secure Software Implementation (Part 2) — Lecture Transcript"
companion_notes: "raw/ICT2216 Lecture 7 Secure Software Development.md"
---

# ICT2216 Lecture 7 — Transcript Key Insights

Curated extraction of classroom discussion, Q&A, and supplementary explanations not present in the structured slide notes.

---

## Stored Procedures vs Prepared Statements — Schema Leakage Argument

Lecturer preference: stored procedures over prepared statements, for a security reason beyond SQL injection prevention.

If an attacker retrieves your application's source code, prepared statement queries reveal your database schema:
- The table names (`users`, `orders`, `payments`) are visible in the source
- The column names (`username`, `password_hash`, `credit_card`) are visible
- The attacker can use this to craft more targeted attacks

Stored procedures only expose the function name (`GetUser`, `InsertOrder`) — the internal SQL, table structure, and column names remain hidden inside the database. Even with the source code, the attacker cannot easily reconstruct the schema.

Additional advantage: stored procedures allow removal of base table permissions from the application account entirely — the app only needs EXECUTE on the procedures, not SELECT/INSERT/UPDATE on the underlying tables.

Caveat: stored procedures that use internal string concatenation are still injectable. Must use parameterised stored procedures.

---

## Version Pinning — The Debate

Two competing valid positions:

**Case for version pinning:**
- Know exactly what version of every dependency is running
- Prevent unexpected breaking changes from automatic updates
- If you don't have sufficient test coverage, pinning is safer

**Case against version pinning (update freely):**
- If automated tests cover all functionality, any regression from a library update will be caught
- Delaying updates leaves you on a vulnerable version longer
- Most minor updates (0.0.x, 0.1.x) are bug fixes and security patches — safe to apply automatically

**Lecturer's personal policy:**
- Minor version updates (e.g., 26.5.1 → 26.5.2): allow CI/CD to auto-update
- Major version updates (e.g., 26 → 27): manual review required, not auto-updated
- Rationale: major updates often have breaking changes; minor updates are almost always security patches or bug fixes

**Key point:** From a security perspective, not updating = potentially vulnerable. From a stability perspective, updating without testing = potentially broken. Sufficient automated testing is the bridge.

---

## Leap Seconds and POSIX/Unix Time

Leap seconds occur because Earth's rotation speed is not constant. When Earth rotation slows, the year has slightly more than 365 days' worth of time — so a leap second is inserted (e.g., 23:59:60).

Problem: most software assumes time is monotonic and that seconds end at :59. Regex-based time validators typically do not account for the value 60 in the seconds field.

**Why POSIX/Unix epoch time solves this:**
- POSIX time counts the number of seconds elapsed since 1970-01-01 00:00:00 UTC
- When a leap second is inserted, the counter simply increments by 1 — no special handling needed
- The 23:59:60 edge case never arises in the storage layer
- Unix designers anticipated non-constant time advancement and designed accordingly

**Input validation implication:**
- If validating time values with regex, the pattern must either accept :60 as a valid seconds value or explicitly reject it as a known edge case
- A regex that rejects 23:59:60 would fail on a legitimate timestamp during a leap second event
- A regex that accepts 99:99:99 is too permissive and would allow invalid times
- Lesson: input validation edge cases come from real-world data, not just attack patterns

---

## Log Injection — Reverse Shell Connection

Why log encoding is a hard security requirement, not just best practice:

IS students learn in Ethical Hacking courses to use log injection to obtain a reverse shell. The technique:
1. Attacker identifies that user input is written to a log file without sanitisation
2. Attacker injects a newline followed by a shell command (e.g., a reverse shell payload)
3. If the log processing system (log aggregator, SIEM, or shell script reading the log) executes the injected line, the attacker gains a shell
4. Attacker then uses the shell to remove the log entry, eliminating the audit trail

This is why:
- Encode/sanitise before writing to logs (remove newlines, escape special characters)
- Protect log integrity (append-only storage, file permissions, cryptographic signing)
- Forward logs to a centralised service immediately — a compromised node cannot erase already-forwarded logs

---

## ZIP Bomb (CPOM Attack) — File Upload

When allowing ZIP file uploads, ZIP bombs are an additional threat beyond malware:

A ZIP bomb (also called a decompression bomb or CPOM attack) is a small compressed file that expands to a massive size when decompressed. Example: a 42 KB ZIP file that decompresses to 4.5 petabytes.

If an application automatically decompresses uploaded ZIP files without size checking:
- The decompression process exhausts disk space and/or RAM
- Results in a denial-of-service condition on the server

File upload security must therefore include:
- File type validation by header (not just extension)
- File size limits on both the compressed and expected decompressed size
- Malware scanning (ClamAV or equivalent)
- ZIP bomb detection (nested compression ratio checking)

---

## Open Source vs Closed Source Security

Neither is inherently more secure. The more important question is maintenance quality.

| | Open Source | Closed Source |
|--|-------------|--------------|
| Code visibility | Anyone can audit | Only vendor audits |
| Vulnerability disclosure | Publicly disclosed; faster community patches | Privately patched; may be silently exploited |
| Community | Many eyes find bugs | Dedicated security team |
| Supply chain | Must vet dependency sources | Must trust vendor |

The lecturer's framing for D3 (the QA team reviewing the dev team's code): this is analogous to a closed-source internal audit — the code is visible to the internal QA team but not to external parties. This model is consistent with enterprise software security review.

---

## Emoji in Usernames and Passwords

Application teams should explicitly decide whether emoji are supported and test accordingly:
- Emoji occupy supplementary Unicode planes (U+1F000+)
- Database schema must use a character set that supports 4-byte Unicode (e.g., MySQL `utf8mb4`, not `utf8`)
- Input validation must either explicitly allow emoji character categories or reject them with a clear error
- Password fields that allow emoji expand the effective alphabet, increasing entropy — but may cause compatibility issues with some authentication systems

Test: try inserting emoji into username and password fields in your application. Check whether the database stores them correctly and whether login still works after storage.

---

## Passive Observation — Codex Storage

Lecturer noted independently observing Codex consuming unexpectedly large storage on a 4TB SSD Mac, finding it suspicious before the public GitHub issue was raised. The continuous insert-and-prune cycle (36,000+ rows in 15 seconds with flat total row count) is the signature of a write-amplified log rotation — writes far exceed the logical data size because old rows are constantly deleted and rewritten.

Root cause classification: debatable whether feature or bug. The TRACE-level default could be intentional (feed more context to the model) or unintentional (developers did not anticipate heavy usage patterns). The correct classification is a **misconfiguration** — the logging level was not calibrated for production deployment.
