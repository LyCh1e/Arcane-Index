---
type: concept
title: "Network Security — Vulnerabilities and Exploits"
domain: cyber-security
status: established
created: 2026-10-26
updated: 2026-10-26
sources: [inf2005-csf-network-security-attacks]
tags: [network-security, dos, ddos, drdos, botnet, iot-botnet, arp-spoofing, packet-sniffing, port-scanning, evil-twin, mitm, nmap, wireshark, dpi, cvss, inf2005]
---

# Network Security — Vulnerabilities and Exploits

Network security attacks exploit weaknesses in protocols, architectures, and configuration. The unifying formula is:

```
Vulnerabilities + Threats = Risks
```

A vulnerability in isolation causes no harm; risk materialises only when a threat actor **exploits** it. Severity and likelihood are quantified using the **CVSS** (Common Vulnerability Scoring System) calculator.

---

## 1. Network Fundamentals

A **computer network** is a collection of autonomous computers interconnected by a single technology that lets them exchange information (Tanenbaum & Wetherall). Networks are joined into larger networks; the Internet is the canonical **network of networks**.

### Architecture Comparison

| | Client-Server | Peer-to-Peer (P2P) |
|---|---|---|
| Model | Centralised | Decentralised |
| Strengths | Scalable for large networks | Fault-tolerant; cost-effective for smaller networks (e.g. blockchain) |
| Weaknesses | Bottlenecks; high cost | Less scalable |

### Layers and Packets

Data travels as packets. Each layer of the **TCP/IP (or OSI) stack** adds a specific header before transmission. Attacks often target the semantics of a particular layer (e.g. link-layer ARP, transport-layer TCP).

---

## 2. Common Network Vulnerabilities

| Vulnerability | What it Enables |
|---|---|
| Unsecured SSID / fake AP | Evil Twin, traffic interception |
| Unfiltered service ports | DoS, port scanning reconnaissance |
| Unsecured physical ports | MitM via rogue network device |
| Malicious insiders | Any internal attack |
| Unencrypted packets | Credential theft via sniffing |

---

## 3. Denial of Service (DoS / DDoS)

A DoS attack targets **availability** — it does not need to breach confidentiality or integrity.

### Two Basic Forms

- **Bandwidth flood** — sends more traffic than the target can service (e.g. target handles 100 MB/s, attacker sends 150 MB/s).
- **Service request flood** — sends anomalous requests (HTTP, DNS, TCP SYN) that exhaust server resources without needing to succeed. The **SYN flood** sends TCP SYN packets without completing the three-way handshake, filling the connection table.

### Distributed Reflective DoS (DRDoS)

An amplified variant exploiting stateless protocols:

1. The attacker sends requests to many **reflector** hosts with a **spoofed source address** (the victim's IP).
2. Reflectors send replies to the victim — a large volume of unsolicited traffic.
3. Reflectors are **bots** coordinated by a **command-and-control (C&C)** server.

### Botnets

| Term | Meaning |
|---|---|
| **Bot** | Malware granting the attacker complete remote control |
| **Zombie** | An Internet-connected computer infected by a bot |
| **Botnet** | A collection of zombies operated together |
| **IoT botnet** | IoT devices used as zombies; their stripped-down Linux makes malware easy to cross-compile |

---

## 4. Man-in-the-Middle: Access Point Attacks

Wireless networks create an accessible attack surface for anyone in physical range.

- **Wardriving** — mapping WiFi access points by driving around, to locate exploitable targets.
- **Evil Twin** — a fake WiFi AP whose SSID mimics a legitimate network. Victims connect, believing the network is genuine, while all their traffic flows through the attacker's device.
- **Access point hijacking** — the attacker's AP sits in the traffic path, enabling full interception and modification.

The attack exploits two weaknesses: open WiFi authentication (no mutual verification) and SSID being trivially cloned.

---

## 5. Packet Sniffing

Sniffing captures frames or packets that were not addressed to the capturing host.

### Passive vs. Active

| | Passive sniffing | Active sniffing |
|---|---|---|
| Technique | NIC in **promiscuous mode** listens to all frames | **Injects packets** to redirect traffic |
| Works well on | **Hubs** (broadcast to all ports) | **Switched networks** (normally unicast) |
| Detection | Difficult | More detectable |
| Tools | Wireshark, Cain and Abel | ArpSpoof |

On a **switch**, unicast frames are forwarded only to the correct port. The attacker must first **poison the ARP cache** to redirect traffic (see Section 6 below).

### Practical Risk

Any credentials sent over **unencrypted HTTP** are visible in plain text to a sniffer. Applying a `http.request.method == POST` filter in Wireshark and following the TCP stream exposes submitted passwords immediately. **Countermeasure: enforce HTTPS/TLS throughout.**

---

## 6. ARP Spoofing (ARP Poisoning)

### ARP Overview

The **Address Resolution Protocol** maps a 32-bit IP address (network layer) to a 48-bit MAC address (link layer). The NIC driver requires the MAC address to place a frame on the wire.

Each host maintains an **ARP cache** of IP → MAC mappings. ARP is **stateless** — there is no authentication; requests and replies can be forged, and unsolicited replies are accepted.

### Normal ARP Flow

1. Host checks its ARP cache. If the destination IP is absent, it sends an **ARP request** ("Who has 129.119.103.2?") broadcast to `FF:FF:FF:FF:FF:FF`.
2. Every host on the segment receives the broadcast; the owner of that IP replies with its MAC address.
3. The requester updates its ARP cache.

### Poisoning Attack

1. Attacker sends a **forged ARP reply** to a victim, mapping the target IP (e.g. the gateway) to the attacker's MAC.
2. The victim accepts the unsolicited reply and updates its ARP cache.
3. Frames destined for the gateway now go to the attacker → **MitM position on a switched network**.
4. ARP entries expire, so the attacker **continuously re-sends forged replies** to maintain the poisoned state.

---

## 7. Port Spoofing and Deep Packet Inspection

### Port Spoofing

Port-based security assumes that **well-known ports carry their standard protocols** (SSH on 22, HTTP on 80, HTTPS on 443). An attacker can tunnel SSH or other protocols over an unexpected port to evade port-based firewall rules, potentially carrying malware or exfiltrating data.

### Deep Packet Inspection (DPI)

Standard packet filtering inspects headers only. **DPI** inspects the payload to identify the actual application protocol regardless of port number. It can:

- Identify, classify, reroute, or block packets based on payload content.
- Forward misclassified traffic (e.g. faux-HTTPS carrying SSH) to the appropriate analysis tool.

DPI is computationally more expensive but provides substantially stronger protection against port-spoofing and evasion techniques.

---

## 8. Port Scanning

Port scanning probes a host's TCP/UDP ports to determine which are **open, closed, or filtered**. It is primarily a **reconnaissance** technique — attackers use it before exploiting a service; defenders use it to audit their own attack surface.

### Common Nmap Scans

| Scan type | Command | Notes |
|---|---|---|
| TCP Connect | `nmap -sT <ip>` | Full three-way handshake; **logged by the target** |
| Focused | `nmap -p <port> <ip>` | Single or range of ports |
| Zenmap Quick | `nmap -T4 -F <ip>` | Top 100 ports; timing level 4 (faster) |

Findings are cross-referenced with **cve.mitre.org** and **nvd.nist.gov** to check for known exploits against open services.

---

## Attack–Vulnerability Mapping (Summary)

| Attack | Primary vulnerability exploited |
|---|---|
| DoS / DDoS | Open services on TCP/UDP port numbers |
| Man-in-the-Middle (MitM) | Unsecured physical / wireless access |
| Packet sniffing | Unencrypted packets containing credentials |
| ARP spoofing | Stateless, unauthenticated ARP protocol |
| Port scanning | Unfiltered services on TCP/UDP ports |
| Port spoofing | Port-number-only security controls |

---

## Key Countermeasures

| Threat | Countermeasure |
|---|---|
| Sniffing / credential theft | Enforce HTTPS/TLS; encrypt all sensitive traffic |
| Evil Twin / rogue AP | Mutual authentication (WPA3-Enterprise, 802.1X) |
| ARP poisoning | Dynamic ARP inspection (DAI) on managed switches; static ARP entries for critical hosts |
| DoS / DDoS | Rate limiting, SYN cookies, upstream scrubbing services |
| Port spoofing | Deep Packet Inspection; application-layer firewalls |
| Port scan reconnaissance | Host-based firewalls; intrusion detection logging |
