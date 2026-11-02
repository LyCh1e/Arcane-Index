---
type: source
title: "INF2005 CSF — System and Network Forensics"
domain: cyber-security
course: INF2005
format: lecture-notes
lecturer: "Dr Aris Cahyadi Risdianto"
date: 2026-11-02
tags: [inf2005, digital-forensics, evidence-integrity, os-forensics, windows-registry, linux, network-forensics, packet-analysis, wireshark, port-scan-detection, cyber-security]
related:
  - "[[concepts/digital-forensics]]"
  - "[[concepts/cryptographic-hash-functions]]"
  - "[[concepts/network-security-defence]]"
  - "[[sources/inf2005-csf-network-security-defence]]"
---

# INF2005 CSF — System and Network Forensics

*Lecture slides. Raw file: `INF2005 Cyber Security Fundamentals - Digital Forensics.md`*

Slides adapted from Raj Jain (Washington University in St Louis) for the introduction and from Diogo Barradas (University of Waterloo) for the system forensics section. Full content lives in [[concepts/digital-forensics]].

## Coverage

- Definitions: forensics, digital forensics, digital evidence; four branches (computer, storage, network, mobile)
- Use case: the Maury Travis murder investigation traced through an Expedia map request, an IP address and an ISP dial-up record
- Sources and types of digital evidence
- **Evidence integrity** with hash functions (MD5, SHA-1/2, SHA-256) and the collision question
- **Process model** by Mark M. Pollitt: acquisition, identification, evaluation, admission
- **System forensics**: layered analysis model (Carrier), OS artefacts of interest, Linux and Windows evidence locations, the Windows Registry and Event Viewer
- **Network forensics**: devices as evidence sources, web server logs and attack signatures, network traces, sniffer placement, packet analysis, vertical and horizontal port-scan detection

## Question posed on the slides

How do you deal with hash collisions? The concept page gives an answer and marks it as an addition.

## Housekeeping on the slides

Tutorial and lab on Thursday at 9 AM and 11 AM, consultations on request, and the ACW3 report must be ready for demonstration and evaluation. See [[examples/inf2005-acw3-mod-dav-fs-proppatch-dos]] for the ACW3 work already filed.
