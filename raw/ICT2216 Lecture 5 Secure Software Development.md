# ICT2216 Secure Software Development
## Lecture 5: Secure Software Design (Part 2) & Secure Agile Development

---

### Agenda
- Secure Software Design (CIA-AAA applied to design)
  - Confidentiality Design
  - Integrity Design
  - Availability Design
  - Authentication Design
  - Authorisation Design
  - Accountability Design
- Secure Agile Development
- Design Process & Threat Modelling Process
- Secure Design Architecture

---

## Part 1 — Secure Software Design

### Overview

Every security requirement identified in earlier phases must be translated into a concrete design decision. Secure software design applies CIA-AAA principles directly to how the system is architected.

---

## Confidentiality Design

Disclosure protection can be achieved using two main categories of technique:

**Masking** — useful when data is displayed on screen or printed forms (e.g., masking a credit card number as `**** **** **** 1234`)

**Cryptographic techniques** — used to assure confidentiality when data is:
- Transmitted over a network
- Stored in transactional data stores
- Kept in offline archives

---

### Symmetric Algorithms

Symmetric algorithms use a **single shared key** for both encryption and decryption — the same key is used by both the sender and the receiver.

**Examples:** DES, 3DES, Blowfish, AES

| Property | Detail |
|---|---|
| Key management | Requires a secure out-of-band mechanism to exchange the key |
| Number of keys (N persons) | N(N-1)/2 — grows rapidly |
| Speed | Much faster than asymmetric |
| Non-repudiation | Not addressed |

---

### Asymmetric Algorithms

Asymmetric algorithms use **two mathematically related keys**:
- **Private key** — kept secret by the owner
- **Public key** — disclosed to anyone who needs to communicate securely

It must be computationally infeasible to derive the private key from the public key.

**Examples:** RSA, ECC, DSA

| Property | Detail |
|---|---|
| Key management | Based on Public Key Infrastructure (PKI) |
| Number of keys (N persons) | N key pairs |
| Speed | Much slower than symmetric |
| Non-repudiation | Addressed (private key signing proves identity) |

---

### Choosing Between Symmetric and Asymmetric

In practice, most secure systems use **both**:
- Asymmetric cryptography to securely exchange a session key
- Symmetric cryptography (with that session key) for the actual data transfer

This is the approach used by TLS/HTTPS.

---

### Design Question — Signup Feature

> A developer is designing a Signup feature for a mobile app. Should the username/password be sent to the backend server in plaintext during signup? What if SSL certificate pinning is not correctly implemented?

**Better design approach:**
- Hash the password **on the client side** before transmission, so the server never sees the plaintext password — even during an intercept
- Or use a challenge-response mechanism (server sends a nonce, client hashes password+nonce)
- Enforce SSL certificate pinning correctly to prevent MITM attacks

---

### Digital Certificates

Digital certificate standard: **ITU X.509 version 3 (X.509 v3)**

A certificate contains:
- Certificate version
- Serial number (unique per CA)
- Signature algorithm
- Issuer distinguished name (the Certificate Authority)
- Validity period (not before / not after)
- Subject name (the entity the cert is issued to)
- Subject public key and algorithm
- Extensions (key usage, subject alternative names, etc.)
- Digital signature of the CA

Certificates enable **trust**: by verifying a certificate's signature against a trusted CA, you can confirm that the public key inside genuinely belongs to the stated entity.

---

## Integrity Design

Integrity of software and data can be accomplished using one or more of the following techniques:

1. **Hashing (hash functions)**
2. **Referential integrity design**
3. **Resource locking**

---

### Hashing (Hash Functions)

Hash functions condense variable-length inputs into an **irreversible, collision-free, fixed-size output** called a message digest or hash value.

**Common hash algorithms:** MD5 (deprecated), SHA-1 (deprecated), SHA-256, SHA-3

**Uses:**
- **File integrity verification** — sender provides file + checksum; receiver hashes the received file and compares
- **Password storage** — store the hash of the password, never the plaintext

**Dictionary / Rainbow Table Attacks:**

A dictionary attack tries a large list of known words or leaked passwords against a hash. If all users have the same password hashed the same way, one rainbow table can crack many accounts at once.

**Salted Hashing:**

A **salt** is a unique, random value added to each password before hashing:
- Must be **unique per user** and **randomly generated**
- Stored alongside the hash in the database
- Makes rainbow table attacks computationally infeasible

**Strategy for Strong Hashing (e.g., bcrypt / PBKDF2):**
1. Generate a random salt
2. Calculate hash of (password + salt)
3. Calculate hash again
4. Repeat tens of thousands of times (e.g., 60,000 iterations)

This key stretching makes brute-force attacks extremely slow.

**Design Question:**
> Are you creating one salt for all passwords or a unique salt per user? When and where is the salt generated?

---

### Referential Integrity Design

**Referential integrity** is a property of data stating that all references within it are valid.

In a relational database, referential integrity requires that every value of a foreign key in one table exists as a primary key value in the referenced table.

**Without referential integrity:**
- Orphaned records can exist (e.g., an ORDER with no corresponding CUSTOMER)
- Data inconsistencies go undetected
- "Phantom" records accumulate over time

**With referential integrity:**
- Database enforces that you cannot delete a CUSTOMER who still has ORDERs (unless cascading delete is configured)
- Ensures that ORDER_DETAIL always points to a valid ORDER and PRODUCT

**Design question:** Does your application allow deleting a customer who still has orders? What happens to those order records?

---

### Resource Locking

Two concurrent operations must not be allowed on the same object simultaneously.

**Example — Online banking with web and mobile clients:**
- Can a user log in on both devices at the same time?
- What if the user presses the "Transfer" button on both simultaneously?

Resource locking (e.g., database-level locks, optimistic/pessimistic locking, mutexes) prevents race conditions that could lead to double-spends, double-debits, or data corruption.

---

## Availability Design

**Replication, Failover, and Scalability** techniques ensure the system remains available even under load or failure conditions.

### Replication
- A **single point of failure** (no redundancy) causes all users to be affected when that component fails
- By replicating data, databases, and software across multiple systems, redundancy is achieved
- Typically follows a **master-slave** or **primary-secondary** backup scheme

### Failover
- **Failover** = automatic switching from an active system/server/component to a standby (redundant) one when the primary fails
- Minimises downtime and is transparent to end users when designed correctly
- Failover clusters allow one node to take over another's workload

### Scalability Techniques

| Type | Description |
|---|---|
| **Vertical scaling** | Add resources to the existing node (more RAM, faster CPU, larger storage) |
| **Horizontal scaling** | Add more nodes to the existing cluster (more servers) |

Horizontal scaling is generally preferred for availability — it avoids any single node being a bottleneck or point of failure.

---

## Authentication Design

**Basic authentication factors:**
- Something you **know** (password, PIN)
- Something you **are** (biometric — fingerprint, face)
- Something you **have** (access token, smartphone, hardware key)

**Design considerations:**
- Consider **multi-factor authentication (MFA)** — requiring two or more factors dramatically reduces account takeover risk
- Consider **Single Sign-On (SSO)** — allows users to authenticate once and access multiple services (e.g., "Sign in with Google")

**Design questions:**
- What happens if an admin forgets their password? How is account recovery handled?
- How is the initial admin account created? Who has access to that process?

---

## Authorisation Design

**Role-Based Access Control (RBAC)** is the predominant method for authorisation in most applications — permissions are assigned to roles, and users are assigned to roles.

**User-Based Access Control (UBAC)** is appropriate for applications with very few users and highly granular permission requirements.

**Key design principles for authorisation:**
- **Separation of duties** — no single user should be able to complete a high-risk action alone
- **Least privilege** — grant only the minimum permissions necessary
- Consider the **performance impact** — overly complex permission checks can slow the system

---

## Accountability Design

Design for **auditing** must be factored in from the very beginning, not added as an afterthought.

**Log data should capture:**
- **Who** performed the action (authenticated identity)
- **What** was done (action type and parameters)
- **Where** it happened (source IP, component)
- **When** it occurred (accurate timestamp)

**Key design rule:** Sensitive data must **never** be logged in plaintext form (no passwords, no credit card numbers in logs).

**Good logging design:**
- Easy for developers to use for debugging
- Does **not** contain any user PII or credentials
- Stores only the minimum necessary information
- Implements log rotation and disposal policies
- Logs are protected from tampering (access-controlled, ideally write-once)

---

## Design Exercise — Revisiting the API Credentials Question

> How do you securely design storage of API credentials in a mobile application or Dockerfile?

Applying the CIA-AAA design framework:

**Confidentiality Design:**
- Storing credentials in source code → **zero marks, completely insecure**
- Use a separate configuration file? Better, but still needs protection
- Download the configuration file on first launch from a secure server?
- Encrypt the configuration file

**Integrity Design:**
- If all users share the same database credentials — any credential leak compromises all users
- If shared credentials have CHANGE PASSWORD permission, an attacker can lock everyone out
- If shared credentials have GRANT/UPDATE/DELETE permissions, catastrophic data loss is possible
- Design principle: each user (or service) should have **separate credentials with least privilege**

**Availability Design:**
- Can attackers DDoS the database directly? Network-level controls needed

**Authentication Design:**
- How do you ensure only the right user/process can access the database?

**Authorisation Design:**
- What permissions does each credential actually need? (SELECT only? No DDL?)

**Accountability Design:**
- Log access on both the application and database sides

**A possible (non-exhaustive) design approach:**
1. Require login authentication
2. Use the password hash to encrypt the config file
3. Derive the decryption key from the password hash at runtime
4. Use a device ID to additionally encrypt and store the config file locally

---

## Password Storage Exercise

Comparing different storage strategies for the same set of passwords:

| Approach | Example | Security |
|---|---|---|
| Plaintext | `123456` | ❌ Catastrophic |
| Unsalted MD5 | `e10adc3949ba59abbe56e057f20f883e` | ❌ Rainbow table trivially cracks |
| Unsalted SHA-256 | `8d969eef6ecad3c29a3a629280e686cf...` | ❌ Still vulnerable to precomputed attacks |
| Salted SHA-256 | Long hash + unique salt per user | ✅ Much better |
| Salted + iterations (bcrypt/PBKDF2) | + account metadata (create date, last login, fail count, history) | ✅ Best practice |

The final column shows **additional security metadata** that should be stored:
- Account creation date
- Last login datetime
- Failed login count (for lockout/velocity checking)
- Password history (to prevent reuse)

---

## Passwordless Authentication

A growing trend — removing passwords entirely:

**How it works:**
1. User registers an **authenticator app or device** (something you have)
2. Initial setup validates identity via SMS or email OTP
3. Subsequent logins require approval from the authenticator app/device
4. No password is ever transmitted or stored

**Real-world examples:**
- WhatsApp — uses OTP at setup, no ongoing password
- Microsoft Accounts — fully passwordless option
- SingPass — multi-factor without traditional passwords
- Apple ID sign-in prompts on trusted devices
- Google — approval prompts on registered devices

---

## Part 2 — Secure Agile Development

### Integrating Security into Agile Sprints

Security activities must be embedded across the entire agile lifecycle, not bolted on at the end:

| Phase | Security Activities |
|---|---|
| **Modelling** | Derived requirements, security requirements |
| **Sprint Planning** | Definition of Ready (security criteria), secure design, architectural analysis |
| **Agile Sprint** | Origin analysis, code review, static analysis, unit tests, refactoring, formal methods, continuous integration |
| **Dynamic Testing** | Dynamic analysis, penetration testing, regression and performance testing |
| **Release** | Test automation, red teaming, automated deployment, sprint demo, user testing |
| **Operations** | Vulnerability tracking, operational monitoring, release management |

**Key tools used across the lifecycle:**
- IDE (development environment)
- Configuration management
- Test automation frameworks

---

## Design Process — Threat Modelling as Part of Secure Design

The threat modelling process integrates directly with secure architecture design:

### Step 1: Architecture
Document the system's structure:
- Topologies (physical and logical)
- Services, ports, and protocols
- Identities and authentication mechanisms
- Authorisation rules
- Data elements
- Actors (human and non-human)
- Auditing controls

### Step 2: Identify Threats
- Trust boundaries
- Data flows
- Entry and exit points
- Mis-actors (attackers)
- Attack trees
- Categorised threat lists: **STRIDE, OWASP Top 10, CWE Top 25**

### Step 3: Prioritise and Implement Controls
- Input validation
- Error handling
- Encryption and hashing
- Replication
- Access Control Lists (ACLs)
- Multi-factor authentication
- Logging

### Step 4: Document and Validate
- Documented Threat Profile
- Residual Risk assessment
- Verification and Validation (V&V) report

---

## Secure Design Architecture

### Identify Physical Topology

Determine **where and how** applications will be deployed:

| Zone | Description |
|---|---|
| **Intranet (Internal)** | Internal corporate network — lower external threat exposure |
| **Internet (External)** | Public-facing — highest threat exposure |
| **Demilitarised Zone (DMZ)** | Sits between internal and external — web/app servers typically live here |
| **Development environment** | Must also be secured — source code and credentials at risk |

**Typical layered architecture:**
- Internet → Firewall → DMZ (Application Server) → Firewall → Internal Network (Database Server)

---

### Identify Logical Topology

Determine the **components, services, protocols, and ports** that need to be defined, developed, and configured:

- How will authentication be designed? (forms-based, certificate-based, token-based, biometrics, SSO, MFA)
- What ports and protocols will be used? (e.g., HTTP/HTTPS on 80/443, database on 1433)
- How are services structured? (presentation layer, business logic, data layer)

**Example:**
- User browser → Port 80/443 (HTTPS) → Application Server
- Application Server → Port 1433 (TCP/IP) → Database Server (certificate-based authentication)

---

### Identify Human and Non-Human Actors

All actors that interact with the system must be identified:

**Human actors:**
- Customers, sales agents, system administrators, database administrators, developers, testers

**Non-human actors:**
- Scheduled backup processes
- Backend batch jobs
- Automated monitoring agents

Each actor must be modelled with appropriate authentication and authorisation — automated processes should use service accounts with least privilege, not shared human accounts.

---

### Identify Data Elements

Classify all data the system handles:

- Product information
- Customer information (PII — subject to PDPA)
- Testing data (must not be real production data — see PCI SSF discussion from Lecture 3)
- Product data / configuration
- Passwords and credentials
- Sensitive vs. non-sensitive classifications

**Data Access Control Matrix** — define who can do what to which data:

| Data | Administrator | Sales Agent | Customer |
|---|---|---|---|
| Customer Data | CRUD | CRUD | Read (own only) |
| Product Data | CRUD | Read | Read |
| Order Data | CRUD | CRUD (own) | Read (own only) |

---

### Identify External Dependencies and Techniques

**External dependencies** — software and hardware components the system relies on but does not own:
- Credit card processors
- Third-party backup services
- Cloud infrastructure providers
- Open-source libraries and frameworks

**Security techniques to consider for each dependency:**

| Area | Techniques |
|---|---|
| Authentication | Basic auth, MFA, SSO, OTP, biometrics |
| Password management | Complexity policy, expiration, recovery/reset, NIST 800-63 standards |
| Certificate management | PKI, CA hierarchy, certificate revocation (CRL/OCSP) |
| Flow control | Firewalls, reverse proxies, WAFs |
| Auditing | Application event logs, syslog, SIEM |
| Intrusion detection | IDS/IPS |
| Database security | Encryption at rest, encryption in transit, least-privilege DB accounts |
| Sandboxing | Isolate risky code execution |

---

### Summary

Good secure software design translates each CIA-AAA security requirement into a concrete architectural decision. The key takeaways from this lecture are:

1. **Confidentiality** — choose the right cryptographic approach (symmetric vs. asymmetric); never store credentials in source code
2. **Integrity** — use salted, iterated hashing for passwords; enforce referential integrity in databases; use resource locking to prevent race conditions
3. **Availability** — design for replication, failover, and horizontal scalability from the start
4. **Authentication** — prefer MFA; design admin account creation and recovery carefully; consider passwordless designs
5. **Authorisation** — use RBAC with least privilege and separation of duties; consider performance impact
6. **Accountability** — log who/what/where/when; never log sensitive data in plaintext; implement log rotation
7. **Secure Agile** — embed security activities into every sprint phase, from modelling to operations
8. **Threat Modelling in Design** — use the 4-step process (architecture → identify threats → implement controls → document and validate) and tools like STRIDE and OWASP Top 10

---

### References
- CVSS Specification Document: https://www.first.org/cvss/specification-document
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- NIST 800-63: https://pages.nist.gov/800-63-3/

---

*End of Lecture 5*
