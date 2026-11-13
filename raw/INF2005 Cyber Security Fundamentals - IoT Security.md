# INF 2005 - Cyber Security Fundamentals
**Dr Aris Cahyadi Risdianto**

## Internet of Things (IoT) Security: Introduction to Attack and Exploits

---

## What is IoT and Why?

- Things in IoT can be a consumer wearable, a household appliance, or a car with telematics
- These physical objects can be assigned IP addresses or unique identifiers
- Affords less human intervention, greater machine autonomy → better accuracy, efficiency, higher productivity

### Real World IoT Products

Image slide showing example IoT products.

### Types of IoT Applications

There are currently five types of IoT applications:

- **Consumer IoT** – such as light fixtures, home appliances, and voice assistance for the elderly.
- **Commercial IoT** – applications of IoT in the healthcare and transport industries, such as smart pacemakers, monitoring systems, and vehicle-to-vehicle communication (V2V).
- **Industrial Internet of Things (IIoT)** – includes digital control systems, statistical evaluation, smart agriculture, and industrial big data.
- **Infrastructure IoT** – enables the connectivity of smart cities through the use of infrastructure sensors, management systems, and user-friendly user apps.
- **Military Things (IoMT)** – application of IoT technologies in the military field, such as robots for surveillance and human-wearable biometrics for combat.

### IoT Connected Devices Installed Base Worldwide

- The total installed base of IoT connected devices is projected to amount to **75.44 billion worldwide by 2025**, a 2.5 times increase in 5 years
- An automated high-tech lifestyle and livelihood – COOL?

---

## IoT Security Issues

### IoT Security Issues (1)

- **2015 Jeep hack:** Security researchers Charlie Miller and Chris Valasek executed a wireless hack on a Jeep, changing the radio station on the car's media center, turning its windshield wipers and air conditioner on, and stopping the accelerator from working. They infiltrated the car's network through Chrysler's in-vehicle connectivity system, **Uconnect**.
- **Mirai:** one of the largest IoT botnets to date.
  - First attacked journalist Brian Krebs' website and French web host OVH in September 2016; the attacks clocked in at **630 Gbps** and **1.1 Tbps** respectively.
  - The following month, DNS service provider **Dyn**'s network was targeted, making a number of websites, including Amazon, Netflix, Twitter and The New York Times, unavailable for hours.
  - The attacks infiltrated the network through consumer IoT devices, including **IP cameras and routers**.

### IoT Security Issues (2)

- Several Mirai variants have since emerged, including Hajime, Hide 'N Seek, Masuta, PureMasuta, Wicked botnet, and Okiru, among others.
- In the first six months of 2019, Kaspersky's honeypots spotted **105 million attacks** coming from **276,000 unique IP addresses**. The figures can be seen in the context of a smart home boom, with consumers buying in increasing numbers connected devices which often have poor in-built security and/or are not properly secured by their owners.

Source: https://wccftech.com/mirai-botnet-unleashes-ddos-attack/

---

## Network-based Attacks (Recap)

Attacks shown: DoS, DDoS, Man-in-the-Middle (MitM), Packet Sniffing, Port Scanning, ARP Spoofing.

Source: https://www.educba.com/types-of-attack/

- **DoS** and **DDoS** exploit **open services** for TCP and UDP port numbers
- **MitM** exploits **unsecured physical ports** in the network devices
- **Packet sniffing** exploits **unencrypted packets** that contain credentials
- **Port scanning** exploits **unfiltered service** for TCP and UDP port numbers
- **ARP spoofing** exploits **unsecured physical ports** connected to attackers

---

## IoT Device Security Challenges

Source: https://www.fortinet.com/resources/cyberglossary/iot-security

- **Weak authentication and authorization** – default passwords and rogue IoT devices (i.e., undetected)
- **Lack of encryption** makes it vulnerable to data breach or theft, especially those used for medical imaging and patient monitoring, and security cameras
- **Vulnerable firmware and software** due to limited budget for developing and testing secure firmware
- **Insecure communications** due to a lack of network segmentation, and adoption of Bluetooth technology, protocols like HTTP and API, which allow cyber criminals to exploit the IoT devices
- **Difficulty in patching and updating devices** because IoT devices are not designed to receive regular security updates, firmware updates/patches, and perform dynamic testing

---

## IoT Attacks and Exploits

> IoT devices are physical devices operated by an OS. **All system attacks are applied to IoT devices.**

Source for the following attack slides: https://heimdalsecurity.com/blog/iot-security-for-business/

### Vulnerability Exploits

- **Buffer overflows** – IoT devices have small memory, so excess data easily spills over into other parts of the memory space, overwriting it. Malware can end up rewriting the code of the device itself.
- **Code injection** – IoT devices run multiple commands without required interaction with the system admin, so it is easy to execute malicious commands.
- **Cross-Site Scripting (XSS)** – IoT devices provide a web-based interface, and the attacker is able to infect the legitimate page with malware.

### Password Attack

> IoT devices are usually installed once in a lifetime. Most use the default password for simplicity.

- Password attacks (dictionary or brute force) target IoT devices because usually nobody monitors the event for failed password logins.
- Most people use an easy password for the IoT device. According to one study, nearly **60% of users reuse the same password**, so if an attacker gets access to one device, they get access to all devices.

### Man-in-the-Middle Attack: Sniffing

> IoT devices are usually installed in open areas with wireless connection. They are an easy target for man-in-the-middle attacks.

- A malicious hacker intercepts the Internet traffic that goes into and out of an IoT device.
- The preferred target is a **Wi-Fi router**, since it contains all of the traffic data sent from the network, and can then be used to control each device connected to it, including IoT devices.

### Man-in-the-Middle Attack: Spoofing

- An attacker can spoof the IoT device to trick the router into allowing it on the network.
- Once the attacker device (A) can communicate with the router, it can inject malware into it.
- This malware then spreads to all the other devices on the network.

### Botnet Enslaving

> Mirai is the biggest IoT botnet we know about, and it was built on the backs of default passwords and usernames.

- IoT devices are prime candidates for a botnet: easier to hack and harder to diagnose if compromised.
- Once a device is enslaved, it can be used for a wide variety of cybercriminal activities, such as **DDoS attacks, sending spam emails, performing click fraud, and Bitcoin mining**.

### Data Leakage

- IoT devices process a lot of personal information in different industries or use cases.
- Most IoT devices have access to information such as:
  - medical data
  - location data
  - usage patterns
  - search history
  - financial information, etc.
- IoT devices have limited data security mechanisms and encryption.

---

## Quick Reference: IoT Attack Summary

| Attack | Why IoT is vulnerable | Impact |
|---|---|---|
| Buffer overflow | Small memory; excess data overwrites adjacent memory | Malware can rewrite the device's own code |
| Code injection | Runs commands without admin interaction | Easy execution of malicious commands |
| XSS | Web-based management interface | Legitimate page infected with malware |
| Password attack | Default/weak/reused passwords; failed logins not monitored | One compromised device exposes all |
| MitM: sniffing | Open-area wireless; router holds all traffic | Traffic interception; control of connected devices |
| MitM: spoofing | Attacker device impersonates an IoT device to the router | Malware injected and spread across network |
| Botnet enslaving | Easy to hack, hard to diagnose | DDoS, spam, click fraud, Bitcoin mining |
| Data leakage | Handles personal data with limited encryption | Medical, location, usage, financial data exposed |

---

## Q&A
