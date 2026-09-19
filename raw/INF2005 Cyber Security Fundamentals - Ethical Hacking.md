# Ethical Hacking

*Cyber Security Fundamentals*

## 1. What is Hacking?

The process of breaking into computerized systems, motivated by:
- **Malicious intent** — causing severe damage to reputation and assets, stealing information, exploiting weaknesses
- **Professional intent** — finding weaknesses (vulnerabilities) and improving security posture
- Personal, military, or professional goals

> Having professional/good intentions alone does **not** automatically make hacking legal — authorization is what matters. ("My intentions and goals are professional, can I start hacking?")

Real-world context referenced: ransomware affecting a mosque payroll system in Singapore; fake "I'm not a robot" CAPTCHA scams that install malware; the OpenAI–Hugging Face incident discussed at Black Hat USA 2026 — illustrating that hacking threats and their coverage are constantly evolving.

---

## 2. Legal Framework

### The Computer Misuse Act (Singapore, 1993 — now Computer Misuse and Cybersecurity Act)
Unethical/unauthorized hacking is illegal. Key offences (Chapter 50A Part II) include:
- Unauthorized access to computer material
- Access with intent to commit or facilitate commission of an offence
- Unauthorized modification of computer material
- Unauthorized use or interception of computer service
- Unauthorized obstruction of use of a computer
- Unauthorized disclosure of an access code
- Enhanced punishment for offences involving **protected computers**
- Abetments and attempts are punishable as offences too

> **Key word across all offences: "Unauthorised."** This is what separates ethical hacking from a crime.

### Whose Laws Rule the Web?
- Laws vary by country; digital actions can cross borders.
- Companies operating internationally must comply with **all** relevant countries' laws.
- An act legal in one country may be prosecutable in another (e.g. the ILOVEYOU virus case — the Philippines dropped charges due to no applicable law at the time).
- Areas where national laws commonly differ:
  - Content control / censorship
  - Intellectual property
  - Privacy (e.g. Europe's privacy laws, including **GDPR**, are markedly stricter than the US's)
  - Hacking / malware laws

### International Collaboration
- **Convention on Cybercrime** — an international agreement fostering cooperation among law enforcement agencies across countries in fighting:
  - Offences against the Confidentiality, Integrity, and Availability (CIA) of computer data/systems
  - Copyright-related offences
  - Computer-related offences (e.g. online fraud)
  - Content-related offences (e.g. child pornography)
- Sets common standards for resolving international cybercrime cases.
- Singapore has MOUs (Memoranda of Understanding) with France, India, the Netherlands, UK, US, Australia, etc., facilitating information sharing, capacity building, and cyber threat intelligence to strengthen the cybersecurity landscape of Singapore and its partners.

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
| **White Hat** | Legally authorised to conduct hacking; a computer security professional who uses their skills to help — hacking as a job to secure systems and provide insight into policies and procedures |
| **Black Hat** | Hacks illegally / without authorisation; a computer security expert who uses skills to steal, damage and destroy — hacking for personal gain or motive |
| **Gray Hat** | Sometimes good guy, sometimes bad; a skilled hacker whose methods may cross legal and ethical boundaries; may transfer vulnerability knowledge to either the systems owner **or** to a black hat |

> An **ethical hacker wears a White Hat** — always operating with legal authorization.

### Worked Scenarios (Hat Colour Classification)
- A hacker engaged by company X, who finds and reports a vulnerability **confidentially to X** → **White Hat**
- A hacker engaged by company Y, who reports a vulnerability confidentially **but also sells it to Y's competitor X** → **Gray Hat** (breaches trust/ethics despite initial authorization)
- A hacker who exploits company X's vulnerability to **secretly insert a malware payload** → **Black Hat**
- A hacker engaged by company Y, whose confidential report is **disregarded**, so they **publish it in a public blog** → **Gray Hat** (unauthorized disclosure, though arguably justified)
- **Unhappy employees** (insider threats) are often considered one of the **greatest organizational risks** — a distinct category from external Black/White/Gray Hats.
- The core difference between a White Hat and a Gray Hat is **integrity** — a White Hat's authorized standing means they may escape legal prosecution, whereas a Gray Hat's boundary-crossing methods leave them exposed.

---

## 4. Hackers' Language: Leet Speak

- **Leet ("1337")** — a coded communication style substituting letters with numbers/symbols:
  - `1`→i/L, `3`→e/E, `4`→a/A, `7`→t, `9`→g, `0`→o, `$`→s, `I`→1/!
  - `|\|`→n, `|\/|`→m, `5`→S, `Z`→2, `f`→/=, `K`→|<, `X`→><, `D`→|)
- **Purpose:** invented for coded communications — hiding websites, newsgroups, etc. to avoid detection by search filters; also used to create stronger passwords.

### Translation Examples
- `1 d1d n0t h4ck th1s p4g3, 1t w4s l1k3 th1s wh3n 1 h4ck3d 1n` → *"I did not hack this page, it was like this when I hacked in"*
- `Hacking is Good` → `H4ck||\|g 1$ 900d`
- The technique works by **replacing a certain percentage of letters in a word with non-alphabetic symbols**.

### Leetification Intensity
Text can be leetified at varying percentages — the higher the percentage, the harder it is to read:
- **10% Leetification** — mostly readable, e.g. `Fourscor3 and s3v3n y3ars ago...`
- **50% Leetification** — noticeably harder, e.g. `ƒ0µr$(0r3 4nđ $3v3n ¥34r$ 490...`
- **100% Leetification** — heavily obfuscated, e.g. `ƒ0µ®$(0®3 4|\|đ $3\/3|\| ¥34®$ 490...`

Various online tools exist for leet translation/decoding (e.g. albinoblacksheep.com, md5decrypt.net, 1337.me).

---

## 5. What is Ethical Hacking? — Pen Testing Approaches

| | Black Box | White Box |
|---|---|---|
| **Style** | Hackers attack in "stealth" mode ("covert") | Tester aims to be thorough within the permitted scope |
| **Prior Knowledge** | Minimal or no pre-knowledge of the target system | Detailed information about the target is known |
| **Coverage** | Employees may be tested too (e.g. helpdesk, call centre — social engineering) | Tests all known aspects of the system/network; doesn't try to cover tracks — "overt" |

---

## 6. The (Ethical) Hacking Process — Stages

```
1. Reconnaissance
2. Scanning
3. Enumeration
4. Gaining Access
5. Keeping/Maintaining Access
6. Covering Tracks
```

Scope narrows from **broad** (reconnaissance) to **specific** (exploitation and beyond), involving:
- **Privilege escalation** — gaining root/sysadmin-level access
- **Lateral movement** — pivoting across systems toward the final target(s)

### Stage Descriptions
1. **Reconnaissance** — information gathering on the target
2. **Scanning** — use information gathered in Stage 1 to examine the target's security posture more closely
3. **Enumeration** — identify user/admin accounts for use, running services etc. when attempting to gain access (associated technique: **Sniffing**)
4. **Gaining Access** — exploit system/network/web vulnerabilities using information from Stages 2 and 3 (associated techniques: **Lateral Movement / Privilege Escalation**)
5. **Keeping or Maintaining Access** — for future exploitation (associated technique: **Backdoor Trojans**)
6. **Covering Tracks** — avoid detection (for Ethical Hacking, this means cleanup of footprints)

---

## 7. Stage 1: Reconnaissance

**Goal:** gather information about the target, e.g. to understand how to hack into "Company Z" to steal information or damage its reputation.

### Human-Based Techniques
- **Shoulder Surfing** — observing someone directly to capture credentials or sensitive info
- **Dumpster Diving** — searching through discarded materials for sensitive data (real cases referenced: unshredded confidential client data found in a bank's discarded documents; scammers dumpster-diving for phone bills)
- **Social Engineering** — manipulating people into divulging information (covered in more depth in a separate lecture)

### Whois
- A **web-based information harvesting technique**, evolved from Unix OS; also available on other OSs and in hacking toolkits (e.g. downloadable from Microsoft Sysinternals).
- **Output typically contains:**
  - Domain name registrant (domain owner)
  - Name servers for the domain
  - Names and contact info of admin/technical staff, etc.
- Usable via web tools (whois.com, who.is, domaintools.com, crazydomains.sg, vodien.com) or built into Linux: `whois target_domain` (e.g. `whois companyX.com`)

### Google Hacking (Dorking)
- **Not** hacking Google itself — using Google's search capabilities to aid reconnaissance.
- **Main benefits:**
  - Low profile and passive — little or no exposure for the attacker
  - Leverages Google's ranked results
- **Best practice:** keep searches reasonably precise — specific keywords, ideally ≤10 — using basic and advanced search operators.

**Search directives:**
- `site:domain.com search terms`
- `allintitle:` / `intitle:` — search within page titles
- `inurl:` — search URL structure (e.g. `inurl:admin/login.php`)
- `filetype:pdf` — restrict to a specific file type

**Example dork queries for exposed credential files:**
- `ext:csv inurl:passwd`
- `ext:xlsx inurl:password`
- `ext:txt inurl:passwd`
- `ext:txt inurl:password`

Reference resources: Exploit-DB's Google Hacking Database, Google's advanced operators reference, freeCodeCamp's Google dorking tutorial.

### Reconnaissance Tool Categories
| Category | Example tools/sites |
|---|---|
| Personal info lookup | Multi-lookup (illmob.org), people-search (Pipl, PeekYou, Lullar, WhitePages.sg, Webmii), photo/reverse-image search (TinEye, Google Images), contact finders (RevealName, WhitePages US) |
| Username lookup | Cross-platform username duplication checker (KnowEm) |
| IP address info | IP-to-address lookup (WhatIsMyIP), geolocation (IPLocation), DNS record viewer (Nirsoft DNSDataView) |
| OSINT (Open Source Intelligence) | Maltego Chlorine, Board Reader (forum post search by name) |

### Netcraft
- **Site Report tool** (toolbar.netcraft.com/site_report) — reveals what technologies a target website is running.

---

## 8. Stage 2: Scanning (and Enumeration)

```
Recon → IP addresses → Port Scan and Enumerate → open ports, running services → Vulnerability Scanning → Penetration Testing
```

- After recon, you should have a list of IP addresses which you are **authorised** to test.
- Scan ports on each IP address to identify **open ports** and the **services running** on targets — these can then be used for exploits.
- Reference vulnerability databases at this stage: **cve.mitre.org**, **nvd.nist.gov**.

### Passive vs. Active Scanning
| | Passive | Active |
|---|---|---|
| Definition | Gathering info **without** the target's knowledge — no packets sent to target systems | Interacting **directly** with the target |
| Examples | Google dorking, online portals, public domain tools | Port scanning, pinging, direct connection attempts |
| Risk | Low detection risk | Target may log your IP/activity; may be illegal if unauthorized |

### Scanning Techniques

**Ping**
- Used to determine if a system is "alive" — a special type of **Internet Control Message Protocol (ICMP)** packet.
- Example: `ping google.com`

**Ping Sweeps**
- Manually pinging many hosts individually is time-consuming; ping sweeps automate host discovery across a range.
- Tools: **Zenmap, Angry IP Scanner**

**Nmap**
- A leading network scanning tool, run via the **Zenmap** GUI.
- **Ping Sweep** — discovers live hosts across a range.
- **TCP Sweep** — TCP is the core communication standard enabling devices/applications to reliably exchange messages over a network; relies on the **TCP three-way handshake**.
- **TCP vs. UDP Sweep** — different sweep types target the two core transport protocols, each with different discovery characteristics.

**Trace Route**
- `tracert <target domain name – URL or IP address>`
- Enables discovery of **neighbouring systems** with potentially lower security.
- Facilitates **lateral movement** and indirect target exploitation.

**Enumeration**
- Follows scanning; digs deeper into discovered services to extract usable detail (e.g. user/account lists, share names, service versions).
- **Banner Grabbing** — a specific enumeration technique: connecting to an open port/service and reading the "banner" it returns (which often reveals software name/version), providing clues for suitable exploits.

**Port Scanning**
- Identifies specific ports and services running on a particular host.
- Example scan types: **TCP connect scan, SYN scan** (many more types exist).
- Tool: **Zenmap**

**Public Domain Vulnerability Databases**
- **CVE** (cve.mitre.org) — identifies vulnerabilities and exploits
- **NVD** (nvd.nist.gov) — vulnerability management (National Vulnerability Database)
- **VulDB** (vuldb.com) — claimed top vulnerability database and threat intel

**Scanning for Vulnerabilities**
- Locating and identifying known weaknesses in services and software, using a **vulnerability scanner**.
- Example tool: **Nessus**

**NSE — Nmap Scripting Engine**
- Verifies findings from an initial port scan, discovers new processes/vulnerabilities, and automates pen-testing techniques.
- Used via Zenmap's built-in scripts (Profile → New Profile, or Command).

### Vulnerability Scanning vs. Penetration Testing
| Vulnerability Scanning | Penetration Testing |
|---|---|
| Reviews systems for **potential** security issues | Performs actual **exploitation and proof-of-concept attacks** to demonstrate real vulnerabilities |

---

## 9. Stage 3: Exploitation / Gaining Access

```
Vulnerability Scanning (collection of known vulnerabilities of software etc. on targets) → Exploitation (payload delivered to target)
```

- Know what exploits can be run against known vulnerabilities; exploit with a suitable technique and tool.
- **Ultimate goal:** get admin access (or some level of access).
- Emerging concern: **Edge Computing / Side-Channel Attacks**.
- Key references: **CVE** (cve.mitre.org), **NVD** (nvd.nist.gov), **VulDB** (vuldb.com), and the **Exploit Database** — a repository of exploits for penetration testers, researchers, and ethical hackers.

### Exploit Tools
- "A way to exploit a security flaw to circumvent security controls" — different targets require different exploits.
- `inurl:login.php` — search for unencrypted login pages
- **Wireshark** — packet sniffing to intercept unencrypted credentials
- Password cracking tools: **Cain & Abel, Hydra, Ophcrack**

### Exploitation Frameworks: Metasploit, Armitage, and Others
- Popular exploitation frameworks bundled in **Kali Linux**.
- **Exploit** — code developed and launched against a remote target; **Payload** — chosen and configured to run once the exploit succeeds.
- **Typical workflow:**
  1. Use **nmap** to scan the victim IP
  2. Identify vulnerabilities
  3. Use **msf (Metasploit Framework)** to exploit the vulnerable service
- Example demonstrated: the **EternalBlue (MS17-010)** exploit via Metasploit.

---

## 10. Stage 4: Post-Exploitation (Maintaining Access)

```
Payload delivered to target → Temporary access → Post Exploitation → Persistent access
```

**Goal:** convert temporary access into persistent access, to continue work or move laterally toward the final target(s).

### Techniques
- **Creating User Accounts** — a simple method is to create a new, hidden, or less-obvious user account with elevated privileges.
- **Modifying Startup Services** — malicious scripts/programs added to the system's startup process (e.g. cron jobs on Linux, the Registry on Windows) to launch automatically.
- **Installing Backdoors and RATs (Remote Access Trojans)** — e.g. **Netcat (nc)** sets up a backdoor listener on the target machine that the attacker can reconnect to later to execute commands. Example RAT: **ProRAT**. Note: Netcat is commonly flagged as malicious by antivirus and endpoint security tools.
- **Installing Rootkits** — kernel-level malware giving deep system control and making detection difficult.

### Hiding Artifacts
- **Via Windows Explorer:** Computer → Organize → Folder and search options → View tab → disable "Show hidden files" — applies to files, folders, and drives.
- **Via CMD:** `attrib +s +a +h <folder/filename>` — sets a file/folder's attributes to system, archive, and hidden; applicable to files and folders.

---

## 11. Stage 5: Covering Tracks (Cleanup)

After an attacker compromises a machine and completes the attack (or creates a backdoor), their presence must be removed or kept hidden. Similarly, when an **ethical hacker** completes work, the target machine must be **restored**:
- Hiding files, folders, and accounts
- Cleaning up log files, Trojans, etc.
- Restoring the target machine — uninstalling apps, deleting temporary accounts, etc.
- Related defensive control: preventing cut/paste/copy/delete/rename of files & folders in Windows (to protect against tampering)

> For **ethical hacking**, this step is about **cleanup and restoring the system to its original state**, not evading detection maliciously.

---

## 12. The Penetration Test Report

A professional pentest concludes with a report containing:
- Pentest scope and objectives
- Record of findings during the test
- Specific advice on how to close identified vulnerabilities
- Steps to be followed by the client going forward
- Delivered directly to an **authorized officer** of the client organization

> "Can you tell if hacking done is ethical?" — the report and prior authorization are what make the process demonstrably ethical, not the techniques themselves (which are identical to a black hat's).

---

## Summary: The Hacking Stages Recap

1. **Reconnaissance** — information gathering on the target, including neighbours (passive or active); may involve non-technical techniques (dumpster diving, shoulder surfing, social engineering).
2. **Scanning** — use recon data to examine the target's/neighbour's security posture more closely. **Enumeration** identifies running apps/services and determines their vulnerabilities (and exploits) from vulnerability databases.
3. **Gaining Access** — exploit vulnerabilities using information from scanning & enumeration (sometimes from reconnaissance) or vulnerability scanning.
4. **Keeping or Maintaining Access** — for continuation of exploitation / lateral movement.
5. **Covering Tracks** — avoid detection (cleanup, for ethical hacking).

*(Next lecture in the module sequence: Web Security)*

## Key Takeaways
- The defining line between ethical and criminal hacking is **authorization** — the Computer Misuse Act criminalizes *unauthorised* access, modification, and use; the key word is "unauthorised."
- **White Hat = authorized**, **Black Hat = unauthorized/malicious**, **Gray Hat = ambiguous/boundary-crossing**; insider threats (disgruntled employees) are a distinct, often greater, risk category.
- Ethics (AiSP/(ISC)² codes) fill gaps where law is silent, but ethical hacking must always be **legally authorized** first.
- Pen testing follows a structured lifecycle — **Reconnaissance → Scanning → Enumeration → Gaining Access → Maintaining Access → Covering Tracks** — moving from broad information-gathering to specific, targeted actions, with privilege escalation and lateral movement occurring along the way.
- **Passive** recon/scanning avoids detection (no direct contact with target); **Active** scanning risks logging and may be illegal without authorization.
- Vulnerability **scanning** finds potential issues; **penetration testing** proves them via actual exploitation.
- A pentest is only complete with a clear, actionable **report** delivered to an authorized client officer — the deliverable that separates professional ethical hacking from mere unauthorized access.
