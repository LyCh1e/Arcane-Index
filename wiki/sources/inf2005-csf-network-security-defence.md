---
type: source
title: "INF2005 CSF — Network Security: Introduction to Network Defence"
domain: cyber-security
course: INF2005
format: lecture-notes
lecturer: "Dr Aris Cahyadi Risdianto"
date: 2026-11-02
tags: [inf2005, network-security, defence-in-depth, firewall, ids, ips, proxy, vpn, port-security, aaa, radius, tacacs, cyber-security]
related:
  - "[[concepts/network-security-defence]]"
  - "[[concepts/network-security-attacks]]"
  - "[[sources/inf2005-csf-network-security-attacks]]"
  - "[[sources/inf2005-csf-digital-forensics]]"
---

# INF2005 CSF — Network Security: Introduction to Network Defence

*Lecture slides. Raw file: `INF2005 Cyber Security Fundamentals - Network Security Defence.md`*

The companion to [[sources/inf2005-csf-network-security-attacks]]: the previous lecture showed the attacks, this one maps each attack to a defence layer. Full content lives in [[concepts/network-security-defence]].

## Coverage

- Recap of ARP and of the attacks (DoS/DDoS, MitM, sniffing, scanning, ARP spoofing) and the weakness each one exploits
- **Defence in depth**: seven layers from policies to data, with the attacks mapped onto layers
- **Firewalls**: DMZ architecture, zero-trust segmentation, what a firewall does and does not mitigate, rule ordering, packet filtering, stateless against stateful
- **IDS and IPS**: NIDS, HIDS, port mirroring, signature against anomaly detection, inline prevention
- **Proxies**: application gateways and caching
- **VPNs**: authentication, tunnelling, encryption; L2TP/IPsec compared with OpenVPN
- **Physical port security**: switch MAC learning, MAC flooding, shutdown violation mode
- **Network AAA**: RADIUS and TACACS

## Questions posed on the slides

1. Why can servers not tell legitimate from spoofed requests over UDP? (reflection attacks)
2. What happens when a switch runs out of MAC table memory?

Answers are in the concept page and are marked as additions where they go beyond the slides.

## Slide errors worth knowing

- The spoofing bullet reads "authentication/authorization/authorization (AAA)"; the intended terms are authentication, authorisation and accounting.
- The AAA slide phrases accounting as "When do you do?"; the sense is "what did you do, and when?" (the example is a timestamped access log).
