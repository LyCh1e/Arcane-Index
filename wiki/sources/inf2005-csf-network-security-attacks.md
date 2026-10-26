---
type: source
title: "INF2005 CSF — Network Security: Vulnerabilities and Exploits"
domain: cyber-security
course: INF2005
format: lecture-notes
lecturer: "Dr Aris Cahyadi Risdianto"
week: 9
date: 2026-10-26
tags: [inf2005, network-security, dos, ddos, arp-spoofing, packet-sniffing, port-scanning, mitm, evil-twin, cyber-security]
---

# INF2005 CSF — Network Security: Vulnerabilities and Exploits

*Week 9 lecture notes. Raw file: `INF2005 Cyber Security Fundamentals - Network Security Attacks.md`*

Full ingested content lives in [[concepts/network-security-attacks]].

## Coverage

- Computer network definition; client-server vs. peer-to-peer architectures; TCP/IP layer model
- Vulnerability + threat = risk; CVSS scoring; common network vulnerabilities (unsecured SSID, unfiltered ports, unencrypted packets)
- DoS / DDoS: bandwidth floods, service request floods (SYN flood), Distributed Reflective DoS, botnets and IoT zombies
- MitM via access points: wardriving, Evil Twin attacks, access point hijacking
- Packet sniffing: passive (promiscuous mode on hubs) vs. active (ARP poisoning on switches); Wireshark demo
- Port spoofing and Deep Packet Inspection as a countermeasure
- ARP: purpose, stateless protocol, ARP cache poisoning mechanic
- Port scanning with nmap; TCP Connect scan, focused scan, Zenmap Quick Scan; cross-referencing CVE/NVD databases

## Related Pages

- [[concepts/network-security-attacks]] — full concept page
- [[concepts/tcp-ip-network-model]] — OSI / TCP/IP layer background
- [[concepts/network-layer-protocols]] — protocol-level context
- [[sources/inf2005-csf-ethical-hacking]] — reconnaissance and hacking methodology
- [[sources/inf2005-csf-system-security]] — system-layer attacks
- [[sources/inf2005-csf-malware-introduction]] — malware types (botnets)
