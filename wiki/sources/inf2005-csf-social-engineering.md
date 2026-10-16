---
type: source
title: "INF2005 CSF — Social Engineering"
source_file: "raw/INF2005 Cyber Security Fundamentals - Social Engineering.md"
module: INF2005 Cyber Security Fundamentals
topic: Phishing, Pharming & Social Engineering
domain: secure-software-development
tags: [source, inf2005, social-engineering, phishing, pharming, spear-phishing, dns-poisoning]
created: 2026-10-16
updated: 2026-10-16
status: ingested
---

# Source: INF2005 CSF — Social Engineering

**Module:** INF2005 Cyber Security Fundamentals  
**Topic:** Human Aspects of Security — Phishing, Pharming & Social Engineering (Dr Peter Loh)  
**Raw file:** [[raw/INF2005 Cyber Security Fundamentals - Social Engineering.md]]  
**Concept page:** [[concepts/social-engineering]]

---

## Coverage Summary

| Section | Key Content |
|---------|-------------|
| People as the Weak Link | Technical protections bypassed through users; recommended reading: Kevin Mitnick, *The Art of Deception* |
| Phishing | Definition; 8 annotated worked examples distinguishing phishing from legitimate email |
| Spear Phishing | Personalised attacks using online profile data; URL shorteners; inconsistent message headers |
| Phishing Red Flags | 7-point checklist: impersonal greeting, mismatched sender domain, typos, urgency, suspicious links, credential requests, account-validation demands |
| Detection Tools | virustotal.com, checkshorturl.com, urlvoid.com, scanurl.net; PhishTank and its API |
| Pharming | Redirects traffic via hosts-file tampering or DNS cache poisoning; less common than phishing |
| Social Engineering (No-Tech) | Five techniques: Authority (Legal/Organisational/Social), Charm, Pretext, Baiting, Reciprocation |
| Mitigation | Verify identity via a separate, independently known channel; inspect full message headers; never log in via an emailed link |

---

## Key Facts and Details

### Phishing Detection Checklist

| Signal | Explanation |
|--------|-------------|
| Impersonal greeting | Legitimate organisations use your name; mass phishing relies on generic salutations |
| "From" ≠ "Received from" | Display name and actual sending domain differ; visible in the full message source/header |
| Typos and awkward phrasing | Professional enterprises do not send poorly-written communications |
| Urgency or threats | "Click NOW or else…" creates panic to bypass critical thinking |
| Links in the email body | Legitimate organisations ask you to navigate directly to their site from your browser |
| Shortened or deceptive URLs | Hover to preview; use urlvoid.com, checkshorturl.com, scanurl.net to check |
| Requests for credentials or financial info | No legitimate service asks for this via email |
| Account-validation prompts | Entering credentials on the linked page delivers them to the attacker |

### Pharming vs Phishing

| Dimension | Phishing | Pharming |
|-----------|---------|---------|
| Attack vector | Email tricks the **user** into visiting a fake site | Hosts file or DNS redirects **traffic** silently |
| URL typed by victim | Wrong URL (clicked or mis-typed) | Correct URL — but still lands on the fake site |
| Technical mechanism | Social deception | Hosts-file tampering or DNS cache poisoning |
| Detection | Check sender headers; hover over links | Check the browser address bar — URL must still match the real domain |
| Relative frequency | Very common | Less common |

### Five Social Engineering Techniques (INF2005 Framing)

| Technique | Mechanism | Key Detail |
|-----------|-----------|-----------|
| **Authority** | Exploit respect for position, rank, or uniform | Three sub-types: Legal (law/safety enforcement), Organisational (supervisory hierarchy), Social (peer group pressure) |
| **Charm** | Induce liking or sympathy | People naturally want to help those they like or feel sorry for |
| **Pretext** | Fabricated scenario with prepared cover answers | Impersonates authority figures or creates a situation that makes help seem reasonable; charm is sometimes categorised as pretext since the dividing line is blurred |
| **Baiting** | False promise targeting greed or curiosity | Physical: infected USB drives left in conspicuous locations; Online: enticing ads leading to malicious sites or malware-laden downloads |
| **Reciprocation** | Exploit the urge to repay a favour | Quid pro quo; Philip Kunz experiment (1974) — 600 Christmas cards sent to strangers; 200+ replied within five days |

---

## Connections

- [[concepts/social-engineering]] — full attack taxonomy, psychological foundations, modern case studies, and defence framework; Pharming section added from this source
- [[wiki/sources/inf2005-csf-ethical-hacking.md]] — INF2005 companion lecture on ethical hacking methodology and legal framework
