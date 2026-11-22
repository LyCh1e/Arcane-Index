# INF2005 – Tutorial 2: Network Scanning and Packet Analysis

*Transcribed from `INF2005-Week10-Tutorial-Scanning-and-Packet.pdf` (SIT Restricted). The lab Wi-Fi password printed in the handout is deliberately omitted.*

## Part 1: Network Scanning

**NMAP installation.** Install an NMAP scanner: NMAP/ZenMAP (https://nmap.org/download).

**Connection setup.** Connect to the special Wi-Fi network "ICT-EVENT" (password given in the handout). Do not use "SIT-WIFI" because it may not work, or you will be disconnected. Check the connection to the target IP addresses (e.g. 172.18.23.21) with `ping 172.18.23.21`. If there is a reply, continue.

### Task 1: Execute and analyse the ping and basic scan results

- Ping scan: `nmap -sn 172.18.23.0/27`
- Basic scan: `nmap 172.18.23.21`

Questions:
1. How many IP addresses or hosts are replying to the ping or are in "up" status?
2. How many ports are open on the 172.18.23.21 IP address?

### Task 2: Execute and analyse the TCP and UDP scan results

- TCP SYN scan: `nmap -sS 172.18.23.21`
- TCP Connect scan: `nmap -sT 172.18.23.21`
- UDP scan: `nmap -sU -p 69 172.18.23.21`

Questions:
1. Which TCP port numbers are in the open and filtered state?
2. Which UDP port numbers are open?

### Task 3: Execute and analyse the service and version detection scanning

- Identify the target operating system: `nmap -O 172.18.23.21`
- More aggressive: `nmap -O --osscan-guess 172.18.23.21` (the handout prints an en dash before `osscan-guess`)
- Identify service and version: `nmap -sV 172.18.23.21`
- More aggressive: `nmap -sV -A 172.18.23.21`

Questions:
1. What is the operating system of 172.18.23.21?
2. What are the services and versions running on 172.18.23.21?

### Task 4: Execute and analyse the comprehensive scanning

Launch a comprehensive scan that includes service detection, OS detection, and vulnerability/exploit script scanning:

`nmap -sS -sV -O --script=vuln,exploit -p- 172.18.23.21`

Questions:
1. What are the differences between comprehensive scanning and the previous scanning methods?
2. Which services have vulnerabilities as well as exploits?

## Part 2: Packet Analysis

**Wireshark installation.** Windows or macOS: follow the Packt installation steps. Ubuntu Linux: `sudo apt install -y software-properties-common`, `sudo add-apt-repository ppa:wireshark-dev/stable`, `sudo apt update`, `sudo apt install -y wireshark`.

**Example packet data.** Download the PCAP exercise files from xSite and extract the zip file.

### Task 5: Analysing the unencrypted remote session
Open `telnet.pcap` with Wireshark. Question: Who is logged into 192.168.0.1? Mention the username and password.

### Task 6: Analysing the suspicious activity on a file transfer session
Open `ftp.pcap` with Wireshark. Questions: 1. What were the usernames? 2. How many passwords were used? 3. What type of attack is this?

### Task 7: Determine the protocol used and view the text-based chat conversation
Open `chat.dmp` with Wireshark. Questions: 1. What were the email addresses? 2. What was said about the new IT guy?

### Task 8: Determine the protocol used and replay the audio-based conversation
Open `sit_chat.pcap` with Wireshark (the file in the zip is named `sip_chat.pcap`). Question: What is the language?

## Part 3: Packet Capture (Optional)

### Task 9
Understand the protocols involved in a single web-browsing activity:
- Close all browser sessions and related online applications (WhatsApp, Telegram, Outlook, …).
- Open the browser without restoring previous sessions.
- Open Wireshark and start the capture on the wireless interface.
- Enter a single URL (e.g. Google.com) and wait until it has opened completely.
- Stop the capture.

Questions: 1. How many packets are involved? 2. What protocols are involved? 3. What is the order of the protocols?
