# Ethical Hacking

*Cyber Security Fundamentals*

## 1. What is Hacking?

The process of breaking into computerized systems, motivated by:
- **Malicious intent** — causing damage to reputation and assets, stealing information, exploiting weaknesses
- **Professional intent** — finding vulnerabilities and improving security posture
- Personal, military, or professional goals

> Having professional/good intentions alone does **not** automatically make hacking legal — authorization is what matters.

---

## 2. Legal Framework

### The Computer Misuse Act (Singapore, 1993 — now Computer Misuse and Cybersecurity Act)
Unethical/unauthorized hacking is illegal. Key offences include:
- Unauthorised access to computer material
- Unauthorised access with intent to commit or facilitate a crime
- Unauthorised modification of computer material
- Unauthorized use or interception of computer service
- Unauthorized obstruction of use of a computer
- Unauthorized disclosure of access codes
- Enhanced punishment for offences involving **protected computers**
- Abetment and attempts are punishable as offences too

> **Key word across all offences: "Unauthorised."** This is what separates ethical hacking from a crime.

### Whose Laws Rule the Web?
- Laws vary by country; digital actions can cross borders.
- Companies operating internationally must comply with **all** relevant countries' laws.
- An act legal in one country may be prosecutable in another (e.g. the ILOVEYOU virus case — the Philippines dropped charges due to no applicable law at the time).
- Areas where national laws commonly differ:
  - Content control / censorship
  - Intellectual property
  - Privacy (e.g. Europe's privacy laws are markedly stricter than the US's)
  - Hacking / malware laws

### International Collaboration
- **Convention on Cybercrime** — an international agreement fostering cooperation among law enforcement agencies across countries in fighting:
  - Offences against the Confidentiality, Integrity, and Availability (CIA) of computer data/systems
  - Copyright-related offences
  - Computer-related offences (e.g. online fraud)
  - Content-related offences (e.g. child pornography)
- Sets common standards for resolving international cybercrime cases.
- Singapore has MOUs (Memoranda of Understanding) with France, India, the Netherlands, UK, US, Australia, etc., facilitating information sharing, capacity building, and threat intelligence.

### Ethics in Information Security
Ethics guide behavior when the law is silent or unclear on a situation:
- Protect society, the commonwealth, and infrastructure
- Act honourably, honestly, justly, responsibly, and legally
- Provide diligent and competent service to principals (clients/employers)
- Advance and protect the profession

Reference codes: **AiSP Code of Ethics**, **(ISC)² Code of Ethics**.

> **Ethical hacking is authorized legally** — this is the defining requirement.

---

## 3. Types of Hackers

**Who is a hacker?** Anyone who breaks into (or attempts to break into) computer systems.

| Hat | Description |
|---|---|
| **White Hat** | Legally authorised; a computer security professional who uses their skills to help secure systems and improve policies/procedures |
| **Black Hat** | Hacks illegally / without authorisation; uses skills to steal, damage, or destroy for personal gain |
| **Gray Hat** | Sometimes good, sometimes bad; methods may cross legal/ethical boundaries; may pass vulnerability knowledge either to the system owner **or** to a black hat |

> An **ethical hacker wears a White Hat** — always operating with legal authorization.

### Worked Scenarios (Hat Colour Classification)
- A hacker engaged by a company who finds and **confidentially reports** a vulnerability → **White Hat**
- A hacker engaged by a company who reports a vulnerability confidentially **but also sells it to a competitor** → **Gray Hat** (breaches trust/ethics despite initial authorization)
- A hacker who secretly exploits a vulnerability to **insert malware** → **Black Hat**
- A hacker engaged by a company whose confidential report is **ignored**, so they **publish it publicly** → **Gray Hat** (unauthorized disclosure, though arguably justified)
- **Unhappy employees** (insider threats) are often considered one of the **greatest organizational risks**, alongside malicious external hackers.
- The core practical difference between White Hat and Gray Hat is **integrity/legal standing** — a White Hat operates fully within authorization and may escape legal exposure by design; a Gray Hat's boundary-crossing methods leave them exposed to potential prosecution.

---

## 4. Hackers' Language: Leet Speak

- **Leet ("1337")** — a coded communication style substituting letters with numbers/symbols (e.g. `1`→i/l, `3`→e, `4`→a, `7`→t, `9`→g, `0`→o, `$`→s).
- **Purpose:** hide content from search filters/detection (e.g. hiding websites or newsgroups), and to construct stronger passwords.
- **Example translation:**
  - `1 d1d n0t h4ck th1s p4g3, 1t w4s l1k3 th1s wh3n 1 h4ck3d 1n` → *"I did not hack this page, it was like this when I hacked in"*
- Leetification can be applied at varying intensities (e.g. 10%, 50%, 100% of letters replaced) — the higher the percentage, the harder the text is to read.
- Various online tools exist for leet translation/decoding.

---

## 5. Penetration Testing Approaches

| | Black Box | White Box |
|---|---|---|
| **Style** | Stealth / "covert" attack | Thorough testing within a permitted scope |
| **Prior Knowledge** | Minimal or no pre-knowledge of the target system | Detailed information about the target is known in advance |
| **Coverage** | May test human elements too (e.g. helpdesk, call centre via social engineering) | Tests all known aspects of the system/network; does not try to cover tracks — "overt" |

---

## 6. The 5 Phases of Hacking (Pen Testing)

```
1. Reconnaissance
2. Scanning (and Enumeration)
3. Exploitation / Gaining Access
4. Post-Exploitation / Maintaining Access
5. Covering Tracks (Cleanup)
```

Scope narrows from **broad** (reconnaissance) to **specific** (exploitation and beyond). Within a network, attackers may perform:
- **Privilege escalation** — gaining root/sysadmin-level access
- **Lateral movement** — pivoting across systems, e.g. Web Server → DB Server → ...

---

## 7. Step 1: Reconnaissance

**Goal:** gather information about the target.

### Techniques
- Google dorking, social engineering, dumpster diving (real cases: unshredded confidential client data leaks; scammers dumpster-diving for phone bills)
- **Whois lookups** — a built-in Linux tool (`whois target_domain`) or web-based tools to find domain registration info; commonly used to conduct **doxing** ahead of social engineering.

### Reconnaissance Tool Categories
| Category | Example tools/sites |
|---|---|
| Personal info lookup | Multi-lookup sites, people-search engines (Pipl, PeekYou, WhitePages), photo/reverse-image search (TinEye, Google Images), contact finders |
| Username lookup | Cross-platform username duplication checkers (e.g. KnowEm) |
| IP address info | IP-to-address lookup, geolocation tools, DNS record viewers |
| OSINT (Open Source Intelligence) | Maltego Chlorine, Board Reader (forum post search by name) |

### Google Dorking (Search Directives)
- `site:domain.com search terms`
- `allintitle:` / `intitle:` — search page titles
- `inurl:` — search URL structure (e.g. `inurl:admin/login.php`)
- `filetype:pdf` — restrict to a file type
- Example: `site:companyX.com inurl:admin`, `site:companyX.com inurl:forgotpassword`
- The **Exploit-DB Google Hacking Database** catalogs known dork queries for finding sensitive exposed data.

### Other Tool-Based Recon
- **DNSDataView** — inspects DNS record types
- **Netcraft Site Report** — identifies what technologies a site runs
- **W3Techs** — technology profiling of websites
- **HTTrack** — website mirroring/cloning tool (can be combined with clickjacking and CSRF attacks)

### Passive vs. Active Reconnaissance
| | Passive | Active |
|---|---|---|
| Definition | Gathering info **without** the target's knowledge — no packets sent to target systems | Interacting **directly** with the target |
| Examples | Google dorking, online portals, public domain tools | Port scanning, pinging, direct connection attempts |
| Risk | Low detection risk | Target may log your IP/activity; may be illegal if unauthorized |

---

## 8. Step 2: Scanning (and Enumeration)

**Goal:** using the IP addresses gathered during recon (which you're **authorised** to test), scan ports on each to identify open ports and running services — potential exploit targets.

Deeper enumeration goals:
- Internal IPs (neighbouring systems)
- Technologies and Operating Systems in use (cross-referenced against CVE databases)
- Existing defences

### Key Techniques & Tools
| Technique | Purpose | Tool/Command |
|---|---|---|
| **Traceroute** | Maps the network path to a target; can reveal neighbouring systems with potentially weaker security, enabling lateral movement | `tracert <target>` |
| **Ping** | Determines if a system is "alive," using ICMP packets | `ping google.com` |
| **Ping Sweep** | Scans an entire IP range for live hosts (faster than individual pings) | Zenmap, Angry IP Scanner |
| **Port Scanning** | Identifies specific open ports/services on a host | Zenmap; scan types include TCP Connect scan, SYN scan, and others |
| **NSE (Nmap Scripting Engine)** | Verifies initial scan findings, discovers new vulnerabilities, automates pen-testing steps | Built into Zenmap (Profile → New Profile) |

### Public Domain Vulnerability Databases
- **CVE** (cve.mitre.org) — identifies known vulnerabilities and exploits
- **NVD** (nvd.nist.gov) — vulnerability management (National Vulnerability Database)
- **VulDB** (vuldb.com) — vulnerability database and threat intelligence

### Remote Access Attempts
- Attempt login to discovered remote access services: `telnet target_ip`, `ssh root@target_ip`
- Try **default usernames/passwords** — weak security on devices (e.g. exposed printers with default creds `admin`/`access`) can lead to immediate access.

### Vulnerability Scanning vs. Penetration Testing
| Vulnerability Scanning | Penetration Testing |
|---|---|
| Reviews systems for **potential** security issues | Performs actual **exploitation and proof-of-concept attacks** to demonstrate real vulnerabilities |

- Example tool: **Nessus** — a dedicated vulnerability scanner.

---

## 9. Step 3: Exploitation

**Process:** vulnerability scanning identifies a collection of known vulnerabilities on target software → exploitation delivers a **payload** using a suitable technique/tool.

- **Goal:** ultimately gain admin-level (or other) access.
- Databases referenced again: CVE, NVD, VulDB.
- **Exploit-DB** — a repository of exploits for penetration testers, researchers, and ethical hackers.
- Emerging concern: **Edge Computing / Side-Channel Attacks**.

### Exploit Techniques
- "A way to exploit a security flaw to circumvent security controls" — different targets require different exploits.
- `inurl:login.php` — search for unencrypted login pages
- **Wireshark** — packet sniffing to intercept unencrypted credentials
- Password cracking tools: **Cain & Abel, Hydra, Ophcrack**

### Exploitation Frameworks
- **Metasploit, Armitage**, and similar tools (bundled in Kali Linux) — popular frameworks to develop and launch exploits against remote targets, with configurable payloads.
- Example: the **EternalBlue (MS17-010)** exploit demonstrated via Metasploit.

---

## 10. Step 4: Post-Exploitation (Maintaining Access)

**Goal:** convert temporary access into **persistent access**, enabling continued work or lateral movement toward the final target.

### Techniques
- **Creating User Accounts** — add a new, hidden, or inconspicuous user account with elevated privileges.
- **Modifying Startup Services** — insert malicious scripts/programs into the system's startup process (e.g. cron jobs on Linux, Windows Registry) to auto-launch.
- **Installing Backdoors and RATs (Remote Access Trojans)** — e.g. **Netcat (nc)** sets up a backdoor listener the attacker can reconnect to later; note Netcat is commonly flagged as malicious by antivirus/security tools. Example RAT: **ProRAT**.
- **Installing Rootkits** — kernel-level malware giving deep system control and making detection difficult.

### Hiding Artifacts
- **Via Windows Explorer:** Folder Options → View tab → disable "Show hidden files" — applies to files, folders, and drives.
- **Via CMD:** `attrib +s +a +h <folder/filename>` — sets a file/folder's attributes to system, archive, and hidden.

---

## 11. Step 5: Covering Tracks (Cleanup)

After completing an attack (or, for an ethical hacker, completing authorized testing), the target machine must be restored / presence removed:
- Hiding files, folders, and accounts
- Cleaning up log files, removing Trojans, etc.
- Restoring the target machine — uninstalling apps, deleting temporary accounts, etc.

> For **ethical hacking**, this step is about **cleanup and restoring the system to its original state**, not evading detection maliciously.

---

## 12. The Penetration Test Report

A professional pentest concludes with a report containing:
- Pentest scope and objectives
- Record of findings during the test
- Specific advice on how to close identified vulnerabilities
- Recommended steps for the client to follow going forward
- Delivered directly and confidentially to an officer of the client organization

---

## Summary: The 5 Phases Recap

1. **Reconnaissance** — information gathering on the target (and its neighbours), passive or active; may involve non-technical techniques (social engineering, dumpster diving).
2. **Scanning** — use recon data to examine the target's/neighbour's security posture more closely. **Enumeration** identifies running apps/services and cross-references vulnerability databases for known exploits.
3. **Gaining Access (Exploitation)** — exploit identified vulnerabilities using information from scanning/enumeration (and sometimes recon) or vulnerability scanning results.
4. **Maintaining Access (Post-Exploitation)** — sustain access for continued exploitation or lateral movement.
5. **Covering Tracks** — avoid detection; for ethical hacking, this means proper cleanup and system restoration.

## Key Takeaways
- The defining line between ethical and criminal hacking is **authorization** — the Computer Misuse Act criminalizes *unauthorised* access, modification, and use.
- **White Hat = authorized**, **Black Hat = unauthorized/malicious**, **Gray Hat = ambiguous/boundary-crossing**; insider threats (disgruntled employees) are a major real-world risk category too.
- Ethics (AiSP/(ISC)² codes) fill gaps where law is silent, but ethical hacking must always be **legally authorized** first.
- Pen testing follows a structured 5-phase lifecycle — **Recon → Scan/Enumerate → Exploit → Maintain Access → Cover Tracks** — moving from broad information-gathering to specific, targeted actions.
- **Passive** recon avoids detection (no direct contact with target); **Active** recon/scanning risks logging and may be illegal without authorization.
- Vulnerability **scanning** finds potential issues; **penetration testing** proves them via actual exploitation.
- A pentest is only complete with a clear, actionable **report** delivered to the client — the deliverable that separates professional ethical hacking from mere unauthorized access.
