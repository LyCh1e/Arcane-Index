---
type: source
title: "INF2005 CSF — IoT Security: Introduction to Attack and Exploits"
address: c-000134
domain: cyber-security
course: INF2005
format: lecture-notes
lecturer: "Dr Aris Cahyadi Risdianto"
date: 2026-11-13
tags: [inf2005, iot, iot-security, mirai, botnet, buffer-overflow, code-injection, xss, default-passwords, mitm, data-leakage, cyber-security]
related:
  - "[[concepts/iot-security]]"
  - "[[concepts/network-security-attacks]]"
  - "[[concepts/network-security-defence]]"
  - "[[concepts/wireless-and-iot]]"
  - "[[sources/inf2005-csf-network-security-defence]]"
---

# INF2005 CSF — IoT Security: Introduction to Attack and Exploits

*Lecture slides. Raw file: `INF2005 Cyber Security Fundamentals - IoT Security.md`*

The closing lecture of the network security block. It applies the attacks from [[sources/inf2005-csf-network-security-attacks]] to Internet of Things devices and explains why those devices are easier to compromise than ordinary hosts. Full content lives in [[concepts/iot-security]].

## Coverage

- What IoT is and the **five application types**: consumer, commercial, industrial (IIoT), infrastructure and military (IoMT)
- Scale: 75.44 billion connected devices projected worldwide by 2025
- Case studies: the **2015 Jeep hack** (Uconnect) and the **Mirai** botnet (Krebs, OVH, Dyn) with its variants
- Recap of network attacks and the weakness each exploits
- **Five IoT device security challenges**: weak authentication, no encryption, vulnerable firmware, insecure communications, difficult patching
- **Eight IoT attacks**: buffer overflow, code injection, XSS, password attack, MitM sniffing, MitM spoofing, botnet enslaving, data leakage
- Quick-reference table linking each attack to why IoT is vulnerable and its impact

## Key figures from the slides

| Item | Figure |
|------|--------|
| Mirai attack on Krebs's site | 630 Gbps |
| Mirai attack on OVH | 1.1 Tbps |
| Kaspersky honeypots, first half of 2019 | 105 million attacks from 276,000 unique IP addresses |
| Users who reuse the same password | nearly 60% (one study) |

## Notes

- The Q&A slide is empty in the source.
- The slides state that **all system attacks apply to IoT devices**, because an IoT device is a physical device running an operating system; compare [[sources/inf2005-csf-system-security]].
