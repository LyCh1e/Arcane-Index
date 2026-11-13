---
type: concept
title: "IoT Security — Attacks and Exploits"
address: c-000135
domain: cyber-security
status: established
created: 2026-11-13
updated: 2026-11-13
sources: [inf2005-csf-iot-security]
tags: [iot, iot-security, mirai, botnet, default-passwords, buffer-overflow, code-injection, xss, mitm, data-leakage, firmware, inf2005]
related:
  - "[[concepts/network-security-attacks]]"
  - "[[concepts/network-security-defence]]"
  - "[[concepts/wireless-and-iot]]"
  - "[[concepts/malware]]"
  - "[[sources/inf2005-csf-iot-security]]"
---

# IoT Security — Attacks and Exploits

An IoT device is a physical object (a wearable, an appliance, a car with telematics) that has an IP address or unique identifier and an operating system. Because it runs an OS, **every system attack applies to it**. IoT devices are attractive targets because they are numerous, often unattended, rarely patched and usually protected by default credentials. For the protocols and radio technologies themselves, see [[concepts/wireless-and-iot]].

## 1. What IoT is

Connected objects give less human intervention and greater machine autonomy, which improves accuracy, efficiency and productivity. The installed base was projected to reach **75.44 billion devices worldwide by 2025**, about 2.5 times the figure five years earlier.

| Application type | Examples |
|------------------|----------|
| **Consumer IoT** | Light fixtures, home appliances, voice assistants for the elderly |
| **Commercial IoT** | Healthcare and transport: smart pacemakers, monitoring systems, vehicle-to-vehicle (V2V) communication |
| **Industrial IoT (IIoT)** | Digital control systems, statistical evaluation, smart agriculture, industrial big data |
| **Infrastructure IoT** | Smart cities: infrastructure sensors, management systems, user apps |
| **Military Things (IoMT)** | Surveillance robots, wearable biometrics for combat |

## 2. Case studies

- **2015 Jeep hack.** Charlie Miller and Chris Valasek attacked a Jeep wirelessly through Chrysler's in-vehicle connectivity system, **Uconnect**. They changed the radio station, switched on the wipers and air conditioning, and stopped the accelerator from working.
- **Mirai (2016).** One of the largest IoT botnets. It attacked Brian Krebs's website (**630 Gbps**) and the French host OVH (**1.1 Tbps**) in September 2016, then the DNS provider **Dyn** the following month, which made Amazon, Netflix, Twitter and The New York Times unreachable for hours. It spread through consumer devices, chiefly **IP cameras and routers**, using default usernames and passwords.
- **Variants:** Hajime, Hide 'N Seek, Masuta, PureMasuta, Wicked and Okiru.
- **Scale of scanning:** in the first half of 2019, Kaspersky's honeypots recorded **105 million attacks from 276,000 unique IP addresses**.

## 3. Why network attacks work (recap)

| Attack | Exploits |
|--------|----------|
| DoS / DDoS | Open TCP and UDP services |
| Man-in-the-middle | Unsecured physical ports on network devices |
| Packet sniffing | Unencrypted packets that carry credentials |
| Port scanning | Unfiltered TCP and UDP services |
| ARP spoofing | Unsecured physical ports connected to attackers |

Detail and countermeasures are in [[concepts/network-security-attacks]] and [[concepts/network-security-defence]].

## 4. IoT device security challenges

1. **Weak authentication and authorisation:** default passwords and rogue (undetected) devices.
2. **Lack of encryption:** data breach or theft, especially for medical imaging, patient monitoring and security cameras.
3. **Vulnerable firmware and software:** limited budget for developing and testing secure firmware.
4. **Insecure communications:** no network segmentation; use of Bluetooth and protocols such as HTTP and web APIs.
5. **Difficulty patching and updating:** devices are not designed for regular security or firmware updates, or for dynamic testing.

## 5. IoT attacks and exploits

| Attack | Why IoT is vulnerable | Impact |
|--------|----------------------|--------|
| **Buffer overflow** | Small memory, so excess data spills into adjacent memory | Malware can rewrite the device's own code |
| **Code injection** | Runs multiple commands without admin interaction | Malicious commands execute easily |
| **Cross-site scripting (XSS)** | Web-based management interface | A legitimate page is infected with malware |
| **Password attack** | Default, weak or reused passwords; failed logins rarely monitored | One compromised device exposes all |
| **MitM: sniffing** | Open-area wireless; the Wi-Fi router carries all traffic | Interception, then control of every connected device |
| **MitM: spoofing** | Attacker device impersonates an IoT device to the router | Malware injected and spread across the network |
| **Botnet enslaving** | Easy to hack, hard to diagnose | DDoS, spam, click fraud, Bitcoin mining |
| **Data leakage** | Handles personal data with limited encryption | Medical, location, usage, search and financial data exposed |

### Points to remember

- IoT devices are usually installed **once and left**, so the default password stays. Nearly **60%** of users reuse one password, so one breach can open every device.
- The **Wi-Fi router** is the preferred MitM target because it holds all of the network's traffic.
- Spoofing works in two steps: the attacker's device is admitted by the router, then injects malware that spreads to the other devices.
- A device that becomes a bot is a **zombie**; see the botnet table in [[concepts/network-security-attacks]] and [[concepts/malware]] for infection vectors.

## 6. Defence (derived, not on the slides)

The slides list problems rather than fixes. The controls below follow from the challenges above and from [[concepts/network-security-defence]]; they are marked as additions.

- Change default credentials and use unique passwords per device.
- Segment IoT devices on their own network or VLAN behind a firewall.
- Encrypt traffic and stored data; avoid plain HTTP.
- Keep firmware patched; prefer vendors that issue updates.
- Monitor failed logins and unusual outbound traffic (IDS/IPS, logs; see [[concepts/digital-forensics]]).

## See also

- [[concepts/network-security-attacks]], [[concepts/network-security-defence]], [[concepts/wireless-and-iot]], [[concepts/malware]]
