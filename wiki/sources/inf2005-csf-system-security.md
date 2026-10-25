---
type: source
title: "INF2005 CSF — (Operating) System Security"
domain: secure-software-development
course: INF2005
format: lecture-notes
lecturer: "Dr Aris Cahyadi Risdianto"
week: 8
date: 2026-10-25
tags: [inf2005, system-security, hardware-attacks, spectre, vm-escape, hypervisor, privilege-escalation, ransomware, wannacry, cyber-security]
---

# INF2005 CSF — (Operating) System Security

*Week 8 lecture notes. Raw file: `INF2005 Cyber Security Fundamentals - System Security.md`*

Full ingested content lives in [[concepts/system-security]].

## Coverage

- Von Neumann architecture; attacks cross layer boundaries
- Hardware attacks: counterfeit, fault injection, micro-architectural (Spectre detail)
- Software attacks: control flow (stack smashing, ROP), code injection, command injection
- Hypervisor types; hyperjacking, VM escape (VENOM CVE-2015-3456, CVE-2017-4907, CVE-2020-3960), VM rootkits
- OS attacks: loadable kernel module attack, kernel rootkit, privilege escalation (horizontal vs. vertical), 4-step attack chain
- System software attacks: dynamic linking (LD_PRELOAD), package management, ransomware (WannaCry case study)

## Related Pages

- [[concepts/system-security]] — full concept page
- [[sources/inf2005-csf-malware-introduction]] — companion lecture (malware types)
- [[concepts/access-control]] — privilege levels and protection rings
