---
type: source
title: "INF2005 CSF — Ethical Hacking"
source_file: "raw/INF2005 Cyber Security Fundamentals - Ethical Hacking.md"
module: INF2005 Cyber Security Fundamentals
topic: Ethical Hacking
domain: secure-software-development
tags: [source, inf2005, ethical-hacking, penetration-testing]
created: 2026-09-14
updated: 2026-09-14
status: ingested
---

# Source: INF2005 CSF — Ethical Hacking

**Module:** INF2005 Cyber Security Fundamentals  
**Topic:** Ethical Hacking (lecture slides)  
**Raw file:** [[raw/INF2005 Cyber Security Fundamentals - Ethical Hacking.md]]  
**Concept page:** [[concepts/ethical-hacking]]

---

## Coverage Summary

| Section | Key Content |
|---------|-------------|
| What is Hacking? | Malicious vs professional intent; authorisation as the legal dividing line |
| Legal Framework | Computer Misuse Act (Singapore); "Unauthorised" as the key word across all offences |
| Jurisdictional Complexity | Laws vary by country; ILOVEYOU virus case study; countries differ on hacking, IP, and privacy law |
| International Collaboration | Convention on Cybercrime; Singapore MOUs (France, India, Netherlands, UK, US, Australia) |
| Ethics Codes | AiSP Code of Ethics; (ISC)² Code of Ethics — guide behaviour when law is silent |
| Hat Colours | White (authorised, professional), Black (unauthorised/malicious), Gray (ambiguous); five worked scenarios |
| Leet Speak | 1337; letter-to-symbol substitution; filter evasion and password strengthening |
| Pen-Testing Approaches | Black Box (stealth, minimal prior knowledge) vs White Box (overt, full prior knowledge) |
| Phase 1 — Reconnaissance | Passive vs active; Google dorking; Whois; OSINT tools (Maltego); dumpster diving; doxing |
| Phase 2 — Scanning/Enumeration | Traceroute, Ping, Ping Sweep, Port Scanning (Zenmap/Nmap), NSE; CVE/NVD/VulDB |
| Phase 3 — Exploitation | Metasploit/Armitage; Wireshark; password crackers (Hydra, Cain & Abel); EternalBlue (MS17-010) |
| Phase 4 — Post-Exploitation | Backdoors (Netcat), RATs (ProRAT), rootkits, hidden accounts, `attrib +s +a +h` |
| Phase 5 — Covering Tracks | Ethical: cleanup and system restoration; malicious: log wiping and artefact removal |
| Pentest Report | Scope + findings + vulnerability advice + next steps; delivered confidentially to client officer |

---

## Key Definitions Extracted

- **Ethical hacking** — authorised penetration testing carried out by a security professional (White Hat) to identify and responsibly disclose vulnerabilities.
- **Computer Misuse Act** — Singapore statute criminalising *unauthorised* access to, modification of, and interference with computer systems.
- **Passive reconnaissance** — information gathering with no direct contact with the target (Google dorking, Whois, OSINT portals).
- **Active reconnaissance / scanning** — direct interaction with the target system; risks logging; illegal without authorisation.
- **Vulnerability scanning** — automated review of a system for *potential* security issues (e.g. Nessus); does not prove exploitability.
- **Penetration testing** — actually exploiting vulnerabilities to demonstrate real risk; proves, not merely identifies.

---

## Connections

- [[concepts/ethical-hacking]] — concept page derived from this source
- [[concepts/access-control]] — authentication and authorisation; what "unauthorised" means technically
- [[concepts/vulnerability-tracking-frameworks]] — CVE, NVD, CVSS; cross-referenced throughout the scanning phase
- [[concepts/threat-modeling]] — reconnaissance maps directly to threat-agent enumeration and DFD trust boundaries
- [[concepts/owasp-top-10]] — exploitation targets many OWASP categories (injection, broken authentication, etc.)
- [[areas/secure-software-development]] — parent area
