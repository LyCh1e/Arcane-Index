---
type: concept
title: "Web Security and DevOps"
domain: web-development
source: [[sources/INF1005-web-systems-technologies]]
complexity: high
updated: 2026-05-14
tags: [concept, web-development, security, devops, authentication, cryptography, tls, sql-injection, xss, csrf, hosting, ci-cd]
---

# Web Security and DevOps

Covers the CIA triad, STRIDE threat model, authentication strategies, cryptography, TLS/HTTPS, common attack vectors (SQL injection, XSS, CSRF, brute force, DoS), hosting options, cloud service models, CI/CD, and DNS administration.

---

## 1. Information Security Core Concepts

### CIA Triad

| Property | Meaning |
|----------|---------|
| **Confidentiality** | Protect data from unauthorised access |
| **Integrity** | Ensure data is accurate and unaltered |
| **Availability** | Ensure systems are accessible when needed |

### STRIDE Threat Model (Microsoft)

| Letter | Threat | Description |
|--------|--------|-------------|
| **S** | Spoofing | Attacker uses someone else's credentials |
| **T** | Tampering | Unauthorised modification of data |
| **R** | Repudiation | Removing traces of an attack; denying actions |
| **I** | Information Disclosure | Unauthorised access to sensitive data |
| **D** | Denial of Service | Preventing legitimate access to a system |
| **E** | Elevation of Privilege | Gaining unauthorised system privileges |

---

## 2. Authentication and Authorisation

**Authentication** = verifying *who you are*.
**Authorisation** = determining *what you are allowed to do*.

### Authentication Factors

| Factor | Type |
|--------|------|
| **Knowledge** | Something you know — password, PIN |
| **Ownership** | Something you have — token, phone, hardware key |
| **Inherence** | Something you are — fingerprint, face scan |

**MFA (Multi-Factor Authentication)**: requires two distinct factors.

### Web Authentication Strategies

| Strategy | Description | Notes |
|----------|-------------|-------|
| **HTTP Basic Auth** | Browser popup; credentials in request header | Simple, but credentials sent with every request |
| **Form-Based Auth** | Custom HTML form; POST to server; session cookies | Most common; requires HTTPS |
| **Token Auth (Bearer/JWT)** | Stateless tokens in `Authorization` header | Used for REST APIs; no server-side session |
| **Third-Party Auth (OAuth)** | "Sign in with Google/GitHub" | Delegates auth to trusted provider |

---

## 3. Cryptography

### Symmetric Encryption

Same key encrypts and decrypts. Fast but requires secure key distribution.
- **AES** (Advanced Encryption Standard) — current standard.

### Asymmetric (Public Key) Cryptography

Two mathematically linked keys:
- **Public key** — shared openly; used to encrypt or verify
- **Private key** — kept secret; used to decrypt or sign

Solves the key distribution problem. Used in TLS and digital signatures.

### Digital Signatures

Validate **authenticity**, **integrity**, and **non-repudiation** of a message. Signed with private key; verified with public key.

### TLS / HTTPS

**TLS** (Transport Layer Security) — successor to SSL. **HTTPS** = HTTP over TLS — encrypts all data in transit.

Requires an **SSL/TLS certificate** issued by a **Certificate Authority (CA)**.

| Certificate Type | Verification | Trust Level |
|-----------------|-------------|-------------|
| **DV** (Domain-Validated) | Domain ownership only | Basic |
| **OV** (Organisation-Validated) | Organisation identity | Higher |
| **EV** (Extended Validation) | Strictest verification | Highest; used by banks |

---

## 4. Credential Storage

```php
// BAD: Plain-text passwords
$password = "mypassword";

// BAD: MD5 — fast, vulnerable to rainbow tables
$hash = md5($password);

// GOOD: bcrypt via PHP's built-in function
$hash = password_hash($password, PASSWORD_BCRYPT);
$valid = password_verify($inputPassword, $storedHash);
```

**Salting**: adding unique random noise to each password before hashing. Prevents rainbow table attacks — even identical passwords produce different hashes.

---

## 5. Common Attack Vectors

### SQL Injection

Malicious SQL code embedded in user input:

```sql
-- Attacker input: ' OR '1'='1
SELECT * FROM users WHERE username='' OR '1'='1'; -- Always true
```

**Defence**: use **prepared statements / parameterised queries** (never string-concatenate user input into SQL).

```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->bindValue(':id', $_GET['id']);
$stmt->execute();
```

---

### Cross-Site Scripting (XSS)

Malicious script injected into a trusted page, executed in victims' browsers.

| Type | How |
|------|-----|
| **Reflected XSS** | Script returned immediately in server response (e.g., search result page) |
| **Stored XSS** | Script stored in database; affects all visitors to that page |

**Defence**:
- Escape all output with `htmlspecialchars()` in PHP (or equivalent)
- Sanitise all user input before storing
- Set **Content Security Policy (CSP)** headers
- Avoid using `innerHTML` with user-controlled data in JavaScript

```php
$safe = htmlspecialchars($_POST["comment"]);
```

---

### Cross-Site Request Forgery (CSRF)

Forces authenticated users to execute unwanted actions on a site where they are logged in.

**Defence**: include a unique, unpredictable **CSRF token** in every state-changing form:

```html
<input type="hidden" name="csrf-token" value="randomUniqueToken123">
```

Server validates the token before processing the request.

---

### Brute-Force Attacks

Automated password guessing.

**Defences**: rate limiting, account lockout after N failed attempts, CAPTCHA, intrusion detection systems.

---

### Denial of Service (DoS / DDoS)

Overloading a server with illegitimate requests, preventing real users from accessing it.

**Defences**: rate limiting, CDN (Content Delivery Network), load balancers, DDoS protection services (e.g., Cloudflare).

---

### Security Misconfiguration

- Out-of-date server software
- Default credentials not changed
- Unnecessary services exposed
- Verbose error messages revealing internals

---

## 6. DevOps

Combining Development and Operations for faster, more reliable delivery.

### CI/CD Pipeline

| Stage | Meaning |
|-------|---------|
| **CI** (Continuous Integration) | Developers integrate code frequently; automated tests run on every commit |
| **CD** (Continuous Delivery) | Automated release process — ready to deploy at any time |
| **CD** (Continuous Deployment) | Automatically deployed to production when all tests pass |

### Testing Types

| Type | What it tests |
|------|--------------|
| **Unit testing** | Individual functions/components in isolation |
| **Integration testing** | Units working together |
| **Functional testing** | System against requirements |
| **Non-functional testing** | Security, performance, usability |
| **Penetration testing** | Security by simulating real attacks |

**Selenium** — browser automation tool for functional/regression testing.

### Infrastructure as Code (IaC)

Describe infrastructure in text files (Ansible, Vagrant, Terraform) — version-controlled, reproducible, auditable.

---

## 7. Hosting Options

| Type | Description |
|------|-------------|
| **Shared Hosting** | Multiple sites on one physical server; cheapest; least control |
| **Virtualised Shared** | Virtual server with root access; more control |
| **Dedicated Hosting** | Entire physical server rented; maximum control |
| **Collocated Hosting** | You own and manage hardware in a data centre |
| **Cloud Hosting** | Distributed, elastic, pay-per-use |

### Cloud Service Models

| Model | What you rent | Examples |
|-------|--------------|---------|
| **IaaS** | Servers, storage, networking | AWS EC2, Google Compute Engine |
| **PaaS** | Platform for deploying apps | Heroku, App Engine |
| **SaaS** | Finished software | Gmail, Salesforce |

### Server Virtualisation

- **Hypervisor** — software that creates and manages virtual machines
- **Docker** — container-based deployment; packages OS + app as an image
- **Kubernetes** — orchestrates and scales containers across multiple hosts

---

## 8. DNS Administration

| Record | Purpose |
|--------|---------|
| **A** | Hostname → IPv4 address |
| **AAAA** | Hostname → IPv6 address |
| **CNAME** | Alias → another A record |
| **MX** | Specifies mail server(s) |
| **NS** | Specifies authoritative name servers |
| **TXT / SPF** | Anti-spam validation; domain verification |
| **PTR** | Reverse DNS lookup (IP → hostname) |

---

## 9. Apache Web Server

- Main config: `httpd.conf`
- Directory-level config: `.htaccess` files
- Key directives: `Timeout`, `KeepAlive`, `DirectoryIndex`

**VirtualHost** — serve multiple domains from one server:

```apache
<VirtualHost *:80>
  ServerName www.example.com
  DocumentRoot /var/www/example
</VirtualHost>
```

**URL Rewriting** (HTTPS redirect):

```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

---

## 10. Architecture: Monolithic vs Microservices

| | Monolithic | Microservices |
|-|-----------|--------------|
| Structure | Single codebase | Disaggregated into small, well-defined services |
| Scaling | Scale the entire app | Scale individual services independently |
| Maintenance | Harder as app grows | Easier per service; more complex overall |
| Deployment | One deployment | Many deployments; requires orchestration |

---

## See Also

- [[concepts/web-fundamentals|Web Fundamentals]] — HTTPS sits on top of HTTP (TLS wraps the protocol)
- [[concepts/server-side-web-development|Server-Side Web Development]] — PHP/Node.js where SQL injection and XSS vulnerabilities arise
- [[concepts/javascript-fundamentals|JavaScript Fundamentals]] — XSS via `innerHTML`; CORS
- [[concepts/owasp-top-10|OWASP Top 10]] — comprehensive security vulnerability catalogue
- [[concepts/secure-software-requirements|Secure Software Requirements (CIA + AAA)]] — CIA triad in the secure SDLC context
- [[sources/INF1005-web-systems-technologies|INF1005 Source Page]]
