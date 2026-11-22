---
type: concept
title: "Nmap Scan Types and Options"
domain: cyber-security
status: established
created: 2026-11-22
updated: 2026-11-22
address: c-000143
sources: [inf2005-week10-tutorial-scanning-packet-analysis]
tags: [nmap, port-scanning, syn-scan, tcp-connect, udp-scan, os-detection, service-detection, nse, reconnaissance, inf2005]
related:
  - "[[concepts/network-security-attacks]]"
  - "[[concepts/digital-forensics]]"
  - "[[concepts/ethical-hacking]]"
  - "[[concepts/transport-layer-tcp-udp]]"
  - "[[sources/inf2005-week10-tutorial-scanning-packet-analysis]]"
---

# Nmap Scan Types and Options

**Nmap** is the standard network scanner for host discovery, port scanning, service and OS detection. It is a reconnaissance tool: the general idea of port scanning is in [[concepts/network-security-attacks]] §8; this page covers the options used in the Week 10 tutorial ([[sources/inf2005-week10-tutorial-scanning-packet-analysis]]).

## The commands, in the order the tutorial uses them

| Task | Command | What it does |
|------|---------|--------------|
| 1 | `nmap -sn 172.18.23.0/27` | **Ping scan**: host discovery only, no port scan. `/27` is 32 addresses (30 usable hosts). |
| 1 | `nmap 172.18.23.21` | **Default scan** of the 1,000 most common TCP ports. |
| 2 | `nmap -sS <ip>` | **TCP SYN ("half-open") scan**: send SYN, read the reply, send RST instead of completing the handshake. Fast and less likely to be logged by the application; needs raw-packet privileges. |
| 2 | `nmap -sT <ip>` | **TCP Connect scan**: uses the operating system's `connect()`, so the full three-way handshake completes and the target usually logs it. Used when you lack raw-socket privileges. |
| 2 | `nmap -sU -p 69 <ip>` | **UDP scan** of port 69 (TFTP). Slow, because an open UDP port often sends no reply. |
| 3 | `nmap -O <ip>` | **OS detection** by TCP/IP stack fingerprinting. |
| 3 | `nmap -O --osscan-guess <ip>` | Reports the closest guess when no exact match exists. |
| 3 | `nmap -sV <ip>` | **Service and version detection** by probing open ports and matching banners. |
| 3 | `nmap -sV -A <ip>` | `-A` adds OS detection, version detection, default scripts and traceroute. |
| 4 | `nmap -sS -sV -O --script=vuln,exploit -p- <ip>` | **Comprehensive scan** (below). |

## Port states

| State | Meaning |
|-------|---------|
| **open** | A service is accepting connections (TCP: replies SYN/ACK; UDP: replies with data). |
| **closed** | Reachable, but no service is listening (TCP: replies RST). |
| **filtered** | A firewall or filter is dropping the probes, so Nmap cannot tell whether it is open. |
| **open\|filtered** | Typical for UDP: no reply, so open and filtered cannot be told apart. |

## Why the comprehensive scan differs (Task 4, Q1)

Compared with the earlier scans, `-sS -sV -O --script=vuln,exploit -p-`:

- scans **all 65,535 ports** (`-p-`), not just the top 1,000 or one named port;
- adds **service and version detection** (`-sV`) and **OS detection** (`-O`) in one run;
- runs **Nmap Scripting Engine (NSE)** scripts in the `vuln` and `exploit` categories, which check discovered services against known vulnerabilities and attempt exploitation checks;
- is therefore **much slower and much noisier**: more packets, more likely to trip a NIDS ([[concepts/network-security-defence]]), and the exploit scripts can disturb or crash fragile services.

Which services are vulnerable (Q2) comes from the scan output on the lab host, which is not recorded here. Cross-check findings with the CVE databases named in [[concepts/network-security-attacks]].

## Seen from the defender's side

A SYN scan appears in a trace as bulk SYN-only packets: **vertical** (one host, many ports) or **horizontal** (many hosts, one port). See port-scan detection in [[concepts/digital-forensics]] and [[concepts/wireshark-packet-analysis]].

> [!warning] Scan only what you are authorised to scan
> Run these against the lab hosts only. See [[concepts/ethical-hacking]] for the legal framework.
