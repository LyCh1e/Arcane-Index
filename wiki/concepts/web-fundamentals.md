---
type: concept
title: "Web Fundamentals (Internet, HTTP, DNS)"
domain: web-development
source: [[sources/INF1005-web-systems-technologies]]
complexity: medium
updated: 2026-05-14
tags: [concept, web-development, internet, http, dns, tcp-ip, networking]
---

# Web Fundamentals (Internet, HTTP, DNS)

Covers the history and architecture of the Internet and World Wide Web, the TCP/IP networking model, DNS resolution, URL structure, HTTP request/response, and web browser rendering.

---

## 1. The Internet vs the Web

| | Internet | World Wide Web |
|-|---------|---------------|
| **Created** | 1969 (ARPANET, US DoD) | 1989 (Tim Berners-Lee, CERN) |
| **What it is** | Global packet-switched network infrastructure | Application running *over* the Internet |
| **Core technologies** | TCP/IP | URL, HTTP, HTML |

**Packet switching** (vs circuit switching): data is broken into independent packets that travel different routes and are reassembled at the destination. Efficient because packets share links; no dedicated circuit needed.

**TCP/IP adopted** across all ARPANET in January 1983.

---

## 2. TCP/IP Network Model

| Layer | Role | Protocols |
|-------|------|-----------|
| **Application** | Familiar protocols used by software | HTTP, FTP, SSH, DNS, SMTP, POP, IMAP |
| **Transport** | End-to-end delivery | TCP (reliable, ordered, ACKs) / UDP (fast, no guarantee) |
| **Internet (IP)** | Routing packets between networks; best-effort | IPv4, IPv6 |
| **Link** | Physical transmission; error detection | MAC addresses, Ethernet, Wi-Fi |

**TCP** guarantees arrival and ordering via sequence numbers and acknowledgements. Lost packets are retransmitted.

**UDP** trades reliability for speed — used in streaming, VoIP, gaming, DNS.

**IPv4**: four 8-bit integers (`192.168.1.1`) — address space exhausted in 2011.
**IPv6**: eight 16-bit integers — vastly larger space.
**PAT (Port Address Translation)**: allows multiple devices to share one IPv4 address.

---

## 3. DNS — Domain Name System

Translates human-readable hostnames to IP addresses. Evolved from a simple `hosts` file to a distributed, hierarchical system.

### Domain Name Structure

- **gTLD** (Generic): `.com`, `.net`, `.org`, `.gov`, `.edu`; new TLDs since 2012 (`.art`, `.cash`, …)
- **ccTLD** (Country Code): `.sg`, `.uk`, `.ca`
- **IDN** (Internationalised): non-ASCII characters (deployed 2009)
- **ICANN** oversees TLD management and accredits registrars.

### DNS Resolution — 10-Step Process

1. Client makes domain request
2. Check local DNS cache
3. If not cached → query primary DNS server
4. Primary DNS queries Root Name Server
5. Root returns TLD server address
6. DNS server queries TLD server
7. TLD returns Authoritative DNS Server addresses
8. DNS server queries Authoritative DNS Server
9. IP address returned to DNS server
10. Client makes request to the resolved IP

---

## 4. URLs

Structure: `protocol://domain[:port][/path][?query][#fragment]`

| Component | Description | Example |
|-----------|-------------|---------|
| Protocol | Connection type | `https://` |
| Domain | Server address | `www.example.com` |
| Port | Optional (default HTTP=80, HTTPS=443) | `:8080` |
| Path | File or directory on server | `/blog/post` |
| Query string | Key-value parameters | `?id=42&lang=en` |
| Fragment | Page section anchor | `#section2` |

**Relative URL types**:

| Type | Syntax |
|------|--------|
| Same directory | `file.html` |
| Child directory | `subdir/file.html` |
| Parent directory | `../file.html` |
| Root reference | `/path/file.html` |

---

## 5. HTTP — Hypertext Transfer Protocol

### Request Methods

| Method | Use |
|--------|-----|
| **GET** | Retrieve a resource; data in URL query string |
| **POST** | Send data (forms); data in request body |
| **HEAD** | Like GET but headers only |
| **PUT** | Update/replace a resource |
| **DELETE** | Delete a resource |

| Property | GET | POST |
|----------|-----|------|
| Data location | URL | Body |
| Bookmarkable | Yes | No |
| Cached | Yes | No |
| Binary data | No | Yes |
| Use case | Search/filtering | Login/submission |

**Safety and idempotency**: GET is both safe and idempotent; PUT and DELETE are idempotent (same result if repeated) but not safe; POST is neither.

### Response Status Codes

| Code | Meaning |
|------|---------|
| 200 OK | Successful |
| 301 Moved Permanently | Permanent redirect |
| 304 Not Modified | Cached version is current |
| 401 Unauthorized | Authentication required |
| 404 Not Found | Resource not found |
| 414 URI Too Long | Too much data in URL |
| 500 Internal Server Error | Server-side error |

### HTTP Headers

- **Request**: `Host`, `User-Agent`, cache directives
- **Response**: `Server`, `Last-Modified`, `Content-Type`, encoding

---

## 6. Browser Rendering

When a browser receives an HTML document it:
1. Parses HTML → finds all referenced resources (CSS, JS, images)
2. Downloads resources (can be parallelised)
3. Applies CSS → layout
4. Renders to screen

### Key Performance Metrics

| Metric | Meaning |
|--------|---------|
| **TTFB** | Time to First Byte |
| **FP** | First Paint |
| **FCP** | First Contentful Paint |
| **LCP** | Largest Contentful Paint |
| **TTI** | Time to Interactive |
| **CLS** | Cumulative Layout Shift |

---

## 7. Web Application Stacks

| Stack | Components |
|-------|-----------|
| **LAMP** | Linux, Apache, MySQL, PHP |
| **MERN** | MongoDB, Express, React, Node.js |
| **WISA** | Windows, IIS, SQL Server, ASP.NET |
| **JAM** | JavaScript, APIs, Markup (static sites) |

---

## 8. Client-Server Architecture

- **Clients**: devices varying in OS, speed, screen size, memory (browsers, phones, tablets)
- **Servers**: respond to HTTP requests — types include Web, Application, Database, Mail, Media, Authentication
- **Server farms**: multiple servers + load balancers + failover for reliability and scale
- **Cloud services**: elastic provisioning — scale on demand

**Web 2.0** shifted the web from read-only (static HTML) to interactive — users contribute content; logic migrated from server to browser (JavaScript).

---

## See Also

- [[concepts/html-and-css|HTML and CSS]] — markup and styling layer built on top of HTTP
- [[concepts/javascript-fundamentals|JavaScript Fundamentals]] — client-side programming
- [[concepts/server-side-web-development|Server-Side Web Development]] — PHP, Node.js, databases
- [[concepts/web-security-and-devops|Web Security and DevOps]] — HTTPS, authentication, hosting
- [[sources/INF1005-web-systems-technologies|INF1005 Source Page]]
