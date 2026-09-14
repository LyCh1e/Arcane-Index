---
type: concept
title: "Ethical Hacking and Penetration Testing"
aliases: ["ethical hacking", "penetration testing", "pen testing", "white hat hacking", "offensive security", "reconnaissance", "exploitation", "5 phases of hacking"]
tags: [ethical-hacking, penetration-testing, reconnaissance, offensive-security, computer-misuse-act, inf2005]
created: 2026-09-14
updated: 2026-09-14
status: established
domain: secure-software-development
address: c-000130
---

# Ethical Hacking and Penetration Testing

**Ethical hacking** is the authorised practice of breaking into computer systems with the owner's permission in order to identify vulnerabilities before malicious actors can exploit them. The defining difference between ethical hacking and criminal hacking is a single word: **authorisation**.

> "Having professional or good intentions alone does **not** automatically make hacking legal — authorisation is what matters."

---

## 1. Legal Framework

### The Computer Misuse Act (Singapore, 1993)

Unethical hacking is illegal. The Act criminalises:

- Unauthorised access to computer material
- Unauthorised access with intent to commit or facilitate a crime
- Unauthorised modification of computer material
- Unauthorised use or interception of a computer service
- Unauthorised obstruction of use of a computer
- Unauthorised disclosure of access codes
- Enhanced punishment for offences involving **protected computers**
- Abetment and attempts are punishable as offences in their own right

> **Key word across all offences: "Unauthorised."** This single word is what separates ethical hacking from criminal conduct.

### Jurisdictional Complexity

Digital actions cross borders; a single act may be governed by the laws of multiple countries. Companies operating internationally must comply with *all* relevant jurisdictions.

**Case study — ILOVEYOU virus (2000):** charges were dropped in the Philippines because no applicable law existed at the time. The case accelerated international cybercrime legislation.

Common points of international legal divergence:
- Content control and censorship
- Intellectual property
- Privacy (European laws are markedly stricter than US)
- Hacking and malware laws

### International Collaboration

- **Convention on Cybercrime** — international agreement coordinating law enforcement across borders; covers offences against CIA of data, copyright violations, computer-related fraud, and content offences; sets common standards for resolving international cybercrime cases.
- **Singapore MOUs** — bilateral Memoranda of Understanding with France, India, the Netherlands, UK, US, Australia, and others; facilitate information sharing, capacity building, and threat intelligence exchange.

### Ethics Codes

Law cannot anticipate every situation. Ethics codes fill the gaps:

| Code | Publisher | Core Obligations |
|------|-----------|-----------------|
| **AiSP Code of Ethics** | Association of Information Security Professionals (Singapore) | Protect the public and infrastructure; act honestly and responsibly; serve principals diligently |
| **(ISC)² Code of Ethics** | International Information System Security Certification Consortium | Protect society; act honourably and justly; provide competent service; advance the profession |

Both codes share the same four principles: protect society, act honourably, serve clients diligently, and advance the profession.

---

## 2. Hat Colour Taxonomy

Who is a hacker? Anyone who breaks into (or attempts to break into) computer systems. Hat colour classifies by intent and authorisation:

| Hat | Description |
|-----|-------------|
| **White Hat** | Legally authorised; a computer security professional who uses skills to help secure systems and improve policies/procedures |
| **Black Hat** | Hacks illegally or without authorisation; uses skills to steal, damage, or destroy for personal gain |
| **Gray Hat** | Methods may cross legal or ethical boundaries; may pass vulnerability knowledge to the system owner *or* to a black hat |

> An **ethical hacker wears a White Hat** — always operating with legal authorisation.

### Worked Scenarios

| Scenario | Hat |
|----------|-----|
| Engaged by a company; finds vulnerability; reports confidentially | **White Hat** |
| Engaged by a company; reports confidentially but also sells vulnerability to a competitor | **Gray Hat** — breaches trust despite initial authorisation |
| Secretly exploits a vulnerability to insert malware | **Black Hat** |
| Engaged by a company; confidential report is ignored; publishes the vulnerability publicly | **Gray Hat** — unauthorised disclosure, even if arguably justified |
| Disgruntled employee with insider access deliberately causes damage | **Black Hat** (insider threat) — rated among the *greatest* organisational risks |

The practical boundary between White and Gray is **full integrity within authorisation**: a White Hat's methods are entirely within scope and legal; a Gray Hat's boundary-crossing leaves them exposed to prosecution.

---

## 3. Hackers' Language: Leet Speak

**Leet ("1337")** substitutes letters with visually similar numbers and symbols:

| Attribute | Detail |
|-----------|--------|
| Common mappings | `1`→i/l, `3`→e, `4`→a, `7`→t, `9`→g, `0`→o, `$`→s |
| Sample sentence | `1 d1d n0t h4ck th1s p4g3` → *"I did not hack this page"* |
| Intensity | Ranges from ~10% (light, still readable) to 100% (fully substituted, very hard to decode) |

**Uses:**
- Evade keyword-based content filters and detection tools
- Construct stronger passwords (leetified words resist dictionary attacks)
- Communicate within hacker communities

---

## 4. Penetration Testing Approaches

| | **Black Box** | **White Box** |
|---|---|---|
| Style | Stealth — covert attack simulation | Overt — thorough testing within a permitted scope |
| Prior knowledge | Minimal or none | Detailed information provided in advance |
| Coverage | May test human elements (e.g. social engineering via helpdesk or call centre) | Tests all known system and network components |
| Analogy | Simulates a real external attacker | Simulates an insider or auditor with full information |

---

## 5. The Five Phases of Hacking

Scope narrows progressively from broad (reconnaissance) to specific (exploitation and post-exploitation):

```
Reconnaissance → Scanning/Enumeration → Exploitation → Post-Exploitation → Covering Tracks
```

Within a compromised network, an attacker may perform:
- **Privilege escalation** — gaining root or administrator-level access from a lower-privilege foothold
- **Lateral movement** — pivoting to adjacent systems, e.g. Web Server → Database Server → ...

---

### Phase 1 — Reconnaissance

**Goal:** gather information about the target without triggering detection.

#### Passive vs Active Reconnaissance

| | **Passive** | **Active** |
|---|---|---|
| Definition | Gathering information *without* the target's knowledge — no packets sent to target systems | Direct interaction with the target |
| Examples | Google dorking, Whois lookups, OSINT portals, public tools | Port scanning, pinging, connection attempts |
| Detection risk | Low — no contact with target | Higher — target may log your IP and activity |
| Legal risk | Low | May be illegal without explicit authorisation |

#### Techniques and Tools

| Category | Technique/Tool |
|----------|---------------|
| **Google Dorking** | `site:`, `allintitle:`, `inurl:`, `filetype:` directives; Exploit-DB Google Hacking Database for catalogued dork queries |
| **Whois lookups** | `whois target_domain` or web tools; reveals domain registration information; used as groundwork for doxing before social engineering |
| **Social engineering** | Phishing, pretexting, calls to helpdesk |
| **Dumpster diving** | Physical recovery of discarded confidential documents (e.g. unshredded client data, phone bills) |
| **OSINT tools** | Maltego Chlorine (relationship mapping), people-search engines (Pipl, PeekYou, WhitePages), TinEye (reverse image search) |
| **DNS and site profiling** | DNSDataView (DNS record inspection), Netcraft Site Report (technology identification), W3Techs (technology profiling) |
| **Website mirroring** | HTTrack — clones a site locally for offline analysis (can be combined with clickjacking/CSRF attacks) |
| **Username lookup** | KnowEm — cross-platform username duplication detection |

#### Google Dorking Examples

```
site:companyX.com inurl:admin
site:companyX.com inurl:forgotpassword
filetype:pdf confidential
inurl:login.php
```

The **Exploit-DB Google Hacking Database** catalogues known dork queries for finding sensitive exposed data.

---

### Phase 2 — Scanning and Enumeration

**Goal:** use the IP addresses gathered during reconnaissance to scan for open ports, running services, and known vulnerabilities — identifying potential exploit targets.

Deeper enumeration goals:
- Internal IP addresses (neighbouring systems for lateral movement)
- Technologies and operating systems in use (cross-referenced against CVE databases)
- Existing defensive measures

#### Tools and Techniques

| Technique | Purpose | Tool |
|-----------|---------|------|
| **Traceroute** | Maps the network path; can reveal neighbouring systems with potentially weaker security | `tracert <target>` |
| **Ping** | Determines if a host is live (ICMP) | `ping google.com` |
| **Ping Sweep** | Scans an IP range for live hosts | Zenmap, Angry IP Scanner |
| **Port Scanning** | Identifies open ports and running services (TCP Connect, SYN, and other scan types) | Zenmap (Nmap GUI) |
| **NSE (Nmap Scripting Engine)** | Extends Nmap to verify findings, discover new vulnerabilities, automate scanning steps | Built into Zenmap |

#### Vulnerability Databases

| Database | URL | Purpose |
|----------|-----|---------|
| **CVE** | cve.mitre.org | Known vulnerabilities and exploits catalogue |
| **NVD** | nvd.nist.gov | Vulnerability management; CVSS scoring |
| **VulDB** | vuldb.com | Vulnerability database and threat intelligence |

#### Vulnerability Scanning vs Penetration Testing

| | Vulnerability Scanning | Penetration Testing |
|---|---|---|
| What it does | Identifies *potential* security issues | Exploits vulnerabilities to *prove* they are real |
| Example tool | Nessus | Metasploit |
| Output | List of potential vulnerabilities | Proof-of-concept; demonstrated impact |

---

### Phase 3 — Exploitation

**Goal:** deliver a payload using a suitable technique to exploit identified vulnerabilities and gain access.

Vulnerability scanning produces a list of known vulnerabilities on target software; exploitation selects the appropriate exploit for each and delivers it.

#### Frameworks and Tools

| Tool | Purpose |
|------|---------|
| **Metasploit / Armitage** | Exploitation frameworks bundled in Kali Linux; develop and launch exploits against remote targets with configurable payloads |
| **Exploit-DB** | Repository of ready-to-use exploits for penetration testers and researchers |
| **Wireshark** | Packet sniffing — captures and analyses network traffic; intercepts unencrypted credentials |
| **Hydra** | Online password-cracking tool (brute force and dictionary attacks) |
| **Cain & Abel / Ophcrack** | Password cracking and hash cracking |
| **EternalBlue (MS17-010)** | NSA-developed exploit targeting a Windows SMB vulnerability; demonstrated via Metasploit |

#### Common Techniques

- Search for unencrypted login pages: `inurl:login.php`
- Attempt default usernames and passwords on discovered services (many devices ship with `admin`/`access`)
- Packet sniffing on unencrypted connections using Wireshark

---

### Phase 4 — Post-Exploitation (Maintaining Access)

**Goal:** convert temporary access into persistent access for continued operations or lateral movement toward the final target.

#### Persistence Techniques

| Technique | Description |
|-----------|-------------|
| **Hidden user accounts** | Create new accounts with elevated privileges under an inconspicuous name |
| **Startup scripts** | Insert malicious scripts into the startup process (Windows Registry run keys, Linux cron jobs) to re-launch on reboot |
| **Backdoors** | **Netcat (nc)** — opens a persistent listening shell the attacker can reconnect to at any time; commonly flagged as malicious by antivirus tools |
| **RATs (Remote Access Trojans)** | **ProRAT** — full remote control capability; keylogging, file access, webcam access |
| **Rootkits** | Kernel-level malware providing deep system control; conceals processes, files, and network connections from the operating system |

#### Hiding Artefacts

- **Windows Explorer:** Folder Options → View → disable "Show hidden files, folders, and drives"
- **CMD attribute flag:** `attrib +s +a +h <folder/filename>` — marks a file or folder as system (`+s`), archive (`+a`), and hidden (`+h`); invisible to standard directory listings

---

### Phase 5 — Covering Tracks

**Goal:** remove evidence of the intrusion.

| Context | Purpose |
|---------|---------|
| **Malicious hacker** | Erase log files, remove trojans, wipe artefacts to avoid detection and prosecution |
| **Ethical hacker** | Restore the system to its original state — uninstall tools, delete temporary accounts, clean up log entries created during the test |

Ethical covering-tracks is a professional obligation: the client's system must be left exactly as found, with no residual backdoors, tools, or accounts.

---

## 6. The Penetration Test Report

The professional deliverable that separates ethical hacking from unauthorised access:

| Component | Description |
|-----------|-------------|
| **Scope and objectives** | What was tested, what was excluded, and the testing goals agreed with the client |
| **Findings** | Record of all vulnerabilities discovered during the test |
| **Vulnerability advice** | Specific remediation recommendations for each finding |
| **Next steps** | Broader recommendations and a prioritised action plan for the client |
| **Delivery** | Submitted directly and confidentially to an officer of the client organisation |

Without the report, a pen test is just unauthorised hacking. The report is the deliverable.

---

## 7. Key Takeaways

- **Authorisation is the defining line** — the Computer Misuse Act criminalises *unauthorised* access; intent alone does not legalise hacking.
- **White = authorised; Black = unauthorised/malicious; Gray = ambiguous/boundary-crossing.** Insider threats (disgruntled employees) represent one of the greatest organisational risks.
- **Ethics codes (AiSP, ISC²) fill gaps where law is silent** — but ethical hacking must always be *legally authorised* first.
- **Passive reconnaissance risks nothing** (no contact with target); **active reconnaissance/scanning risks detection and may be illegal** without explicit authorisation.
- **Vulnerability scanning finds potential issues; penetration testing proves them** via actual exploitation.
- The five-phase lifecycle moves from broad (recon) to specific (exploitation) — each phase builds on intelligence gathered in the previous one.
- A pen test is only complete with a clear, actionable **report** — the deliverable that makes the work professional and legally defensible.

---

## Connections

- [[concepts/access-control]] — authentication and authorisation; the technical meaning of "unauthorised" in the Computer Misuse Act
- [[concepts/vulnerability-tracking-frameworks]] — CVE, NVD, CVSS; cross-referenced throughout the scanning and exploitation phases
- [[concepts/threat-modeling]] — reconnaissance maps to threat-agent enumeration; DFD trust boundaries identify targets for lateral movement
- [[concepts/owasp-top-10]] — exploitation targets many OWASP categories (injection, broken authentication, IDOR, etc.)
- [[concepts/secure-software-requirements]] — ethical hacking validates that security requirements have been properly implemented in the final system
- [[concepts/steganography]] — information hiding as one possible covert technique used in post-exploitation data exfiltration
- [[sources/inf2005-csf-ethical-hacking]] — source material for this page
- [[areas/secure-software-development]] — parent area
