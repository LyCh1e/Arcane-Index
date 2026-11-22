---
type: source
title: "INF2005 Week 10 Tutorial — Network Scanning and Packet Analysis"
address: c-000141
domain: cyber-security
course: INF2005
format: tutorial
date: 2026-11-22
tags: [inf2005, tutorial, nmap, port-scanning, wireshark, packet-analysis, telnet, ftp, brute-force, msn-messenger, sip, rtp, pcap, cyber-security]
related:
  - "[[concepts/nmap-scan-types]]"
  - "[[concepts/wireshark-packet-analysis]]"
  - "[[examples/inf2005-week10-tutorial-worked-answers]]"
  - "[[concepts/digital-forensics]]"
  - "[[concepts/network-security-attacks]]"
  - "[[sources/inf2005-csf-digital-forensics]]"
---

# INF2005 Week 10 Tutorial — Network Scanning and Packet Analysis

*Tutorial handout (PDF) plus a zip of four capture files. Raw file: `INF2005 Week10 Tutorial - Network Scanning and Packet Analysis.md`. Captures kept in `_attachments/pcaps/`.*

The hands-on companion to the Week 10 forensics lecture ([[sources/inf2005-csf-digital-forensics]]) and the port-scanning and sniffing sections of [[sources/inf2005-csf-network-security-attacks]]. It has three parts and nine tasks.

## Structure

| Part | Tasks | Tool | Needs |
|------|-------|------|-------|
| 1. Network scanning | 1–4 | Nmap / Zenmap | The live lab network (`172.18.23.0/27`, Wi-Fi "ICT-EVENT") |
| 2. Packet analysis | 5–8 | Wireshark | The four supplied captures |
| 3. Packet capture (optional) | 9 | Wireshark | Your own laptop |

## What each task teaches

- **Task 1** — host discovery (`-sn`) versus a default scan of the top 1,000 ports.
- **Task 2** — TCP SYN (`-sS`) versus TCP Connect (`-sT`) versus UDP (`-sU`); the open, closed and filtered states.
- **Task 3** — OS fingerprinting (`-O`) and service and version detection (`-sV`, `-A`).
- **Task 4** — a comprehensive scan (`-sS -sV -O --script=vuln,exploit -p-`) that adds all 65,535 ports and the vulnerability scripts.
- **Task 5** — `telnet.pcap`: credentials sent in cleartext.
- **Task 6** — `ftp.pcap`: a dictionary brute-force against FTP.
- **Task 7** — `chat.dmp`: an MSN Messenger conversation readable on the wire.
- **Task 8** — `sip_chat.pcap`: a SIP call whose RTP audio can be reassembled and played.
- **Task 9** — the protocol sequence behind a single page load.

## Notes

> [!gap] Part 1 has no recorded answers
> Tasks 1–4 depend on scanning a live lab host, and no scan output was supplied. The commands and what each flag does are in [[concepts/nmap-scan-types]]; the answers must be filled in from your own scan. Task 9 is likewise your own capture.

> [!warning] Authorisation
> The handout restricts scanning to the lab hosts on the dedicated Wi-Fi network. Scanning systems you do not own or have written permission to test is unlawful in most jurisdictions; see [[concepts/ethical-hacking]].

- The handout names the audio capture `sit_chat.pcap`; the zip contains `sip_chat.pcap`.
- The handout prints an en dash in `–osscan-guess`; the real option is `--osscan-guess`.
- The handout includes the lab Wi-Fi password; it is not recorded in the wiki.
- Worked answers for Tasks 5–8 are in [[examples/inf2005-week10-tutorial-worked-answers]].
