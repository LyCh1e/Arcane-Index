# ICT2216 Secure Software Development
## Lecture 7: Secure Software Implementation (Part 2) — References for Secure Coding

---

### Opening Case Studies

**OpenAI Codex — Excessive Logging Destroying SSDs**

A user reported that the OpenAI Codex CLI continuously writes to its SQLite feedback log (`~/.codex/logs_2.sqlite` and associated WAL/SHM files), measuring approximately **37 TB written in roughly 21 days** — extrapolating to about **640 TB/year**. This far exceeds typical consumer SSD endurance ratings of ~600 TBW (terabytes written) for a 1 TB drive, meaning Codex could wear out an SSD in under a year.

Root cause: the SQLite feedback log sink was installed with a global `TRACE`-level default, persisting dependency internals (`tokio-tungstenite`, `hyper_util`, `inotify` events), raw WebSocket and SSE payload bodies, and OpenTelemetry mirror events. TRACE-level entries accounted for roughly **70% of retained bytes**; the two OTel mirror targets pushed the theoretically droppable share to ~96%. A 15-second sample showed ~36,211 rows inserted while the retained row count stayed flat — the signature of a **continuous insert-and-prune cycle** that amplifies writes without growing the database.

> **Secure coding lesson:** Logging level discipline matters. Default `TRACE` or `DEBUG` logging in production is both a security risk (sensitive data in logs) and an operational risk (SSD wear, disk exhaustion). Always set the **minimum necessary logging level** for production, and never log raw payload bodies by default.

---

**Examena — Face Verification Bypass**

The university's proctoring system (Examena) had a vulnerability where the face verification stage could be **skipped by clicking the Verify button a few times** — because no prior photo of the face had been uploaded to verify against.

> **Secure coding lesson:** Authentication and verification checks must fail **closed** (deny by default). A missing baseline (no reference photo) should result in verification failure, not a bypass.

---

**CISA: Most Critical Open-Source Projects Not Using Memory-Safe Code (June 2024)**

A joint report by CISA, FBI, ASD/ACSC (Australia), and CCCS (Canada) examined 172 critical open-source projects:

- **52%** of critical open-source projects contain code written in memory-unsafe languages
- **55%** of total lines of code across these projects are written in memory-unsafe languages
- Of the ten largest projects by LoC, each has a proportion of memory-unsafe LoC **above 26%** (median: 62.5%)
- Even projects written in memory-safe languages often **depend on components** written in memory-unsafe languages

Notable examples of memory-unsafe code ratios:

| Project | Memory-Unsafe Code Ratio |
|---|---|
| Linux | 95% |
| Tor | 93% |
| MySQL Server | 84% |
| glibc | 85% |
| Redis | 85% |
| SystemD | 65% |
| Chromium | 51% |
| Electron | 47% |

**What is memory-safe code?** Memory-safe languages prevent entire classes of vulnerabilities — buffer overflows, use-after-free, null pointer dereferences — at the language level. Examples: Rust, Go, Python, Java. Memory-unsafe languages (C, C++) require the programmer to manually manage memory, making these bugs easy to introduce.

---

**Leap Seconds — An Unexpected Input Validation Problem**

Tech giants including Meta, Google, and Amazon have pushed to **abolish leap seconds** because they cause significant software bugs:

- Leap seconds cause the clock to read `23:59:60` — a time value that does not normally exist
- Earth's rotation has been accelerating recently (July 29, 2022 was 1.59ms shorter than a standard day)
- Most software assumes time always advances monotonically and that seconds always end in `:59`

> **Secure coding question:** Are you using Regular Expressions to validate time input? Does your regex accept `23:59:60`? If not, a leap second would cause your validation to reject a legitimate timestamp. Does your regex accept `99:43:22`? If so, it's too permissive.
>
> This illustrates that input validation must account for **edge cases in real-world data**, not just obvious attack patterns.

---

**LastPass Data Breach — Developer Endpoint Compromise**

The LastPass breach demonstrates how even strong authentication can be circumvented:

> *"Our investigation determined that the threat actor gained access to the Development environment using a developer's compromised endpoint. While the method used for the initial endpoint compromise is inconclusive, the threat actor utilized their persistent access to impersonate the developer once the developer had successfully authenticated using multi-factor authentication."*

The attacker compromised the **developer's machine** (not the LastPass servers directly), then waited for the developer to complete their own MFA authentication, and used the established session to exfiltrate proprietary information and source code.

> **Secure coding lesson:** MFA protects the authentication event, but not an already-authenticated session on a compromised endpoint. Endpoint security, session timeouts, and anomaly detection are also required. Credentials and secrets stored in the development environment are at risk if developer machines are compromised.

---

**DeepSeek iOS App — Multiple Critical Vulnerabilities**

NowSecure's security assessment of the DeepSeek iOS app found:

- **Unencrypted data transmission** — sensitive data sent over the internet without encryption
- **Weak and hardcoded encryption keys** — uses outdated Triple DES (3DES), reuses initialisation vectors, and hardcodes encryption keys
- **Insecure data storage** — username, password, and encryption keys stored insecurely on the device
- **Extensive data collection and fingerprinting** — user and device data collected and used for tracking
- **Data sent to China** — user data transmitted to servers controlled by ByteDance, subject to PRC laws

> These are textbook violations of basic secure coding practices, including several items from this lecture's OWASP guidance.

---

**Open-Source vs. Closed-Source — Which Is More Secure?**

There is no definitive answer — both models have trade-offs:

| | Open Source | Closed Source |
|---|---|---|
| Code visibility | Anyone can audit | Only vendor can audit |
| Vulnerability disclosure | Publicly disclosed, often faster patching | Privately patched, may be exploited silently |
| Community | Many eyes can find bugs | Dedicated security team |
| Supply chain | Must vet dependencies | Must trust vendor |

The more important question is: **how well is the code maintained, tested, and patched?**

---

### Agenda

This lecture covers key OWASP resources for secure coding, used as reference material throughout development:

1. **OWASP Top 10 Proactive Controls (2024)**
2. **OWASP Cheat Sheet Series** — focusing on Input Validation and SQL Injection Prevention
3. **OWASP Security Knowledge Framework (SKF)**
4. **OWASP Secure Coding Practices Quick Reference Guide**
5. **Securing Database Credentials** — using GitHub Secrets
6. **Docker Development Workflow**

---

## Part 1 — OWASP Top 10 Proactive Controls (2024)

The OWASP Top 10 Proactive Controls describes the **most important security controls** that should be adopted in every secure software development project. Unlike the OWASP Top 10 (which lists the most critical risks/vulnerabilities), the Proactive Controls focus on **defensive techniques and controls**.

Each control entry provides:
- A description of the control
- Best practices to implement it
- Vulnerabilities and risks it addresses
- References for further study
- Tools to integrate into your development

**The 10 Proactive Controls (C1–C10):**

| Control | Description |
|---|---|
| **C1** | Implement Access Control |
| **C2** | Use Cryptography to Protect Data |
| **C3** | Validate All Input & Handle Exceptions |
| **C4** | Address Security from the Start |
| **C5** | Secure By Default Configurations |
| **C6** | Keep Your Components Secure |
| **C7** | Secure Digital Identities |
| **C8** | Leverage Browser Security Features |
| **C9** | Implement Security Logging and Monitoring |
| **C10** | Stop Server-Side Request Forgery |

Reference: https://owasp.org/www-project-proactive-controls/

---

### C2: Use Cryptography to Protect Data

**Applies to:** Passwords, credit card numbers, health records, personal information, business secrets — especially data subject to GDPR, PCI DSS, or other regulations.

**Implementation best practices:**

1. **Never transmit plain-text data.** Encrypt all data in transit between any Point A and Point B. Use TLS for all communications.

2. **Do not create your own cryptographic protocols.** When NIST created AES, they ran an open international competition where the world's best cryptographers proposed algorithms and looked for flaws in each other's work. No individual developer should try to replicate this. Use existing, battle-tested standards.

3. **Do not implement cryptographic routines yourself.** Use an existing cryptographic library (e.g., `cryptography` for Python, `javax.crypto` for Java, `bcrypt`/`argon2` for password hashing). Rolling your own crypto implementation is almost always flawed.

**Vulnerabilities addressed:** OWASP A02:2021 Cryptographic Failures, MASVS-CRYPTO-1

**Tools:**
- **SSLyze** — SSL/TLS configuration scanning library and CLI tool (`github.com/nabla-c0d3/sslyze`)
- **testssl.sh** — TLS/SSL testing tool (`testssl.sh`)
- **SSLLabs** — Free service for scanning and rating TLS configuration
- **OWASP O-Saft** — TLS connection testing tool
- **GitRob** — Command line tool to find sensitive information in publicly available files on GitHub

---

### C3: Validate All Input & Handle Exceptions

**The core problem:** Injection attacks occur when an application confuses **data input as executable commands**. Different injection types target different execution environments:

| Injection Type | What Gets Executed | Where |
|---|---|---|
| **SQL Injection** | SQL commands (or parts thereof) | Database server |
| **Remote Command Injection (RCE)** | OS commands or server-side templates | Web application server/host |
| **JavaScript Injection / XSS** | JavaScript code | Another user's browser |

Input validation is a programming technique that ensures only **properly formatted data** may enter a software system component. When an injection attack targets a client, web servers can perform quoting/encoding on attacker-provided data before forwarding it.

**Implementation approaches:**
- Allowlisting vs. Denylisting
- Client-side and server-side validation
- Regular expressions (with caution — see ReDoS section below)

**Tools:**
- OWASP Java HTML Sanitizer Project
- Java JSR-303/JSR-349 Bean Validation
- Java Hibernate Validator, Apache Commons Validator
- PHP's filter functions
- `sqlmap.py` (for testing SQL injection)
- ZAP-based scans
- CSP Evaluator

---

### C6: Keep Your Components Secure

**The problem:** Most applications rely heavily on third-party libraries and frameworks. Vulnerable dependencies introduce risk regardless of how clean your own code is.

**Two categories of best practices:**

1. **Identify trusted libraries and frameworks** — before bringing a dependency into your project, assess its reputation, maintenance activity, and security track record

2. **Monitor and update packages continuously** — third-party components receive new CVEs regularly; your dependency versions must be tracked and updated

**Key principle:** When possible, use the security features already embedded in frameworks you are already using, rather than adding yet more third-party libraries.

**Tools:**

| Tool | Purpose |
|---|---|
| **OWASP Dependency-Check** | Identifies project dependencies and checks against publicly disclosed vulnerabilities (CVEs via NVD) |
| **OWASP Dependency-Track** | Periodically monitors SBOM (Software Bill of Materials) files for new vulnerabilities |
| **Retire.JS** | Scans JavaScript libraries for known vulnerabilities |
| **Renovate** | Automated dependency update pull requests |
| **Harbor** | Open-source registry securing container artifacts with policies and RBAC |

**OWASP Dependency-Check** works by:
1. Inspecting project dependencies and collecting evidence about each (name, version, CPE)
2. Matching against the NVD (National Vulnerability Database) to find associated CVEs
3. Generating a report linking each vulnerable dependency to its CVE entries
4. Auto-updating via NVD Data Feeds (initial download may take 10+ minutes; subsequent updates are small JSON files)

---

### C9: Implement Security Logging and Monitoring

**Definitions:**
- **Logging** — recording events for debugging and diagnostic purposes
- **Security logging** — recording security-relevant events during the runtime operation of an application
- **Monitoring** — live review of application and security logs using automation

**Uses of security logging:**
- Feeding intrusion detection systems (IDS)
- Forensic analysis and investigations after a breach
- Satisfying regulatory compliance requirements (PDPA, GDPR, PCI DSS)

**Secure logging design and implementation rules:**

1. **Encode and validate dangerous characters before logging** — to prevent **log injection attacks** (where attackers inject fake log entries to confuse forensic analysis)

2. **Never log sensitive information** — do not log:
   - Passwords
   - Session IDs
   - Credit card numbers
   - Social security / NRIC numbers
   - Other PII (PDPA compliance)

3. **Protect log integrity** — attackers may attempt to tamper with logs to cover their tracks:
   - Set appropriate file permissions on log files
   - Audit log changes
   - Use append-only or write-once log storage where possible

4. **Forward logs to a central, secure logging service** — distributed systems must centralise logs so that:
   - Log data cannot be lost if one node is compromised
   - Centralised monitoring and alerting is possible

> **Log4Shell reminder:** Log4J (the popular Java logging library) had a critical RCE vulnerability (CVE-2021-44228) — a reminder that logging libraries themselves can introduce vulnerabilities. Evaluate your logging library choice.

**Logging libraries:**
- **Log4J** (Java) — widely used but had critical CVE-2021-44228 (Log4Shell); ensure you are on a patched version
- **winston** (Node.js) — popular, flexible logger
- **Pino** (Node.js) — extremely fast, low-overhead structured logger

---

## Part 2 — OWASP Cheat Sheet Series

The OWASP Cheat Sheet Series was created by application security professionals to provide concise, actionable security guidance on specific topics. It currently contains **78+ cheat sheets** (and growing).

Reference: https://cheatsheetseries.owasp.org/

This lecture focuses on two cheat sheets:
1. **Input Validation Cheat Sheet**
2. **SQL Injection Prevention Cheat Sheet**

---

### Input Validation Cheat Sheet

**Purpose:** Input validation ensures only properly formed data enters the workflow of an information system. It prevents malformed data from persisting in the database and triggering malfunction of downstream components.

**Key principles:**
- Input validation should happen **as early as possible** in the data flow — ideally as soon as data is received from an external party
- Input validation is **not** the primary defence against XSS, SQL Injection, and other attacks — it is a defence-in-depth layer. Output encoding and parameterised queries are the primary defences for those attacks

---

#### Implementing Input Validation

Multiple layers of validation should be applied:

1. **Framework validators** — use built-in validators provided by your web framework (e.g., Django Validators, Apache Commons Validators)

2. **Schema validation** — validate JSON and XML inputs against a schema (JSON Schema, XML Schema/XSD)

3. **Type conversion with strict exception handling** — e.g., `Integer.parseInt()` in Java, `int()` in Python — let the language's type system reject non-integer input; catch and handle exceptions explicitly

4. **Range and length checks** — enforce:
   - Minimum and maximum values for numerical parameters and dates
   - Minimum and maximum lengths for strings

5. **Enumerated value checking** — for fields with a fixed set of values (e.g., day of week, country code), validate that the input matches exactly one of the allowed values

6. **Regular expressions** — for structured data not covered above, use a regex that covers the **entire input string** (anchored with `^` and `$`) and does **not** use "any character" wildcards like `.` or `\S`

---

#### Allow List vs. Block List

**Block list (deny list) validation** is a common but massively flawed approach:
- Trying to detect dangerous characters like `'`, strings like `1=1`, or tags like `<script>` is trivially bypassed by attackers using encoding, case changes, or alternative representations
- Block lists also frequently prevent legitimate input — e.g., the apostrophe in `O'Brian` is a valid character

**Allow list (whitelist) validation** is the correct approach:
- Define exactly what **is** authorised; everything else is rejected by definition
- For well-structured data (dates, SSNs, zip codes, email addresses): define a strong validation pattern, typically using regular expressions
- For enumerated options (drop-down lists, radio buttons): validate that the input matches exactly one of the values offered to the user

---

#### Validating Free-Form Unicode Text

Free-form text (e.g., name fields, comment boxes) is harder to validate because many characters need to be permitted. Key techniques:

1. **Normalisation** — ensure canonical encoding is used across all text and no invalid characters are present (e.g., Unicode normalisation form NFC or NFKC). Prevents attacks using visually identical but technically different characters.

2. **Character category allow-listing** — Unicode defines categories such as "decimal digits" and "letters" that cover not just Latin but also Arabic, Cyrillic, CJK ideographs, etc. Allow the categories relevant to your application.

3. **Individual character allow-listing** — if you need letters and also the apostrophe `'` (for Irish names) but not the full punctuation category, list the specific characters explicitly.

> **Design question:** Does your application support emoji? If so, how does your validation handle them? They occupy different Unicode planes and may require special handling.

> **Key reminder:** Free-form text input demonstrates why input validation is **not** the primary safeguard against XSS — context-aware output encoding is required when rendering user-supplied text.

---

#### Regular Expressions — Best Practices and ReDoS

Regular expressions are a powerful tool for input validation, but they must be used carefully.

**General rules:**
- Cover the **entire input string** — anchor with `^` and `$`
- Define the **allowed set of characters** to accept
- Define **minimum and maximum lengths** (e.g., `{1,25}`)
- Avoid "any character" wildcards (`.` or `\S`) — these make validation too permissive
- Be aware of ReDoS (see below)

**Allow List Regex Examples:**

```
# U.S. Zip Code (5 digits, optional -4)
^\d{5}(-\d{4})?$

# U.S. State from a drop-down
^(AA|AE|AP|AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|
HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|
NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|
TX|UT|VT|VI|VA|WA|WV|WI|WY)$
```

Reference: OWASP Validation Regex Repository

---

#### Regular Expression Denial of Service (ReDoS)

**What it is:** A Denial of Service attack that exploits inefficient regular expression implementations. When a crafted input is provided to a vulnerable regex pattern, the regex engine enters **catastrophic backtracking** — exploring exponentially many paths — and the program hangs for a very long time.

**How it works — NFA backtracking:**

The regex engine uses non-deterministic finite automata (NFA). When the input fails to match at one position, the engine **backtracks** and tries alternative paths. A poorly designed pattern can cause the number of paths to grow exponentially with input length.

**Example — the pattern `^(a+)+$`:**
- For input `aaaaX` (4 a's + non-matching character): **16 possible paths**
- For input `aaaaaaaaaaaaaaaaX` (16 a's + non-matching character): **65,536 possible paths**
- Each additional `a` **doubles** the number of paths

The `X` at the end ensures no match is found, forcing the engine to explore all paths before concluding failure.

**Evil Regex patterns** — patterns that can get stuck on crafted input. An Evil Regex contains **grouping with repetition** where inside the repeated group there is either more repetition or alternation with overlapping:

```
(a+)+          ← grouping with repetition, inner repetition
([a-zA-Z]+)*   ← grouping with repetition, inner repetition
(a|aa)+        ← grouping with repetition, overlapping alternation
(a|a?)+        ← grouping with repetition, overlapping alternation
(.*a){x}       ← for x > 10
```

All of the above are susceptible to inputs like `aaaaaaaaaaaaaaaaaaaaaaaa!`

**Attack surfaces for ReDoS:**
- An attacker identifies that an application uses a vulnerable regex
- Sends a crafted input designed to maximise backtracking
- Can hang: web browsers, Web Application Firewalls (WAFs), database servers, and web servers

**If the regex is itself user-supplied** (e.g., a search filter), an attacker can inject an Evil Regex directly.

**Mitigation:**
- Use linear-time regex engines where available (e.g., RE2)
- Test regex patterns with tools that detect catastrophic backtracking
- Set timeouts on regex execution
- Avoid the Evil Regex patterns listed above — prefer possessive quantifiers or atomic groups

---

### SQL Injection Prevention Cheat Sheet

Reference: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

**Primary Defences** (in order of preference):

**Option 1: Prepared Statements (Parameterised Queries)** ✅ Best practice

The query structure is defined first; user input is passed as parameters that are never interpreted as SQL syntax. This is the gold standard.

```python
# Vulnerable (string concatenation)
query = "SELECT * FROM users WHERE username = '" + username + "'"

# Safe (parameterised query)
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

```java
// Vulnerable
String query = "SELECT * FROM users WHERE username = '" + username + "'";

// Safe
PreparedStatement stmt = conn.prepareStatement(
    "SELECT * FROM users WHERE username = ?"
);
stmt.setString(1, username);
```

**Option 2: Stored Procedures (properly constructed)**

When stored procedures are used with parameterised inputs, they provide similar protection to prepared statements. However, stored procedures that use string concatenation internally are still vulnerable.

**Option 3: Allow-List Input Validation**

For parts of the query that cannot be parameterised (e.g., table names, column names, sort direction), validate the input against a strict allow list of known-safe values.

```python
# Sort direction must be exactly "ASC" or "DESC"
if sort_direction not in ["ASC", "DESC"]:
    raise ValueError("Invalid sort direction")
```

**Option 4: Escaping All User-Supplied Input**

Escaping is the least preferred option — it is error-prone, database-specific, and easy to forget. Only use as a last resort when refactoring to parameterised queries is not immediately possible.

**Additional Defences:**
- **Enforce Least Privilege** — the application's database account should have only the minimum permissions needed (e.g., SELECT only on read operations, no DROP or CREATE)
- **Perform Allow-List Input Validation as a Secondary Defence** — even when parameterised queries are used, validating input format adds defence-in-depth

**Bobby Tables:** A well-known guide with code examples for preventing SQL injection across many languages and frameworks: https://bobby-tables.com/python

---

## Part 3 — OWASP Security Knowledge Framework (SKF)

Reference: https://demo.securityknowledgeframework.org/

The OWASP SKF contains:
- **Code Examples** — best practice code snippets showing how to implement security controls and prevent common vulnerabilities in multiple languages and frameworks
- **Checklists** — security control checklists correlated with the knowledge base
- **Knowledge Base** — searchable repository of security knowledge items
- **SKF Labs** — practice labs for developers and security specialists to train security testing skills, with write-ups for correct testing methodology

Available code example categories include:
- Flask — SQL query (parameterised)
- Flask — Input validation
- Flask — Directory listing prevention
- Flask — XSL injection prevention
- Flask — Session cookies (domain binding)
- Flask — Random password token generation
- Django — Encoder
- Django — Directory path traversal prevention

---

## Part 4 — OWASP Secure Coding Practices Quick Reference Guide

Reference: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/

A checklist-format guide covering all areas of secure coding. This lecture highlights two particularly relevant sections for your project:

### Database Security Checklist

- Use **strongly typed parameterised queries** (prepared statements)
- Use input validation and output encoding; if these fail, do **not** run the database command
- Ensure variables are **strongly typed**
- The application should use the **lowest possible privilege level** when accessing the database
- Use **secure credentials** for database access
- Connection strings must **not be hardcoded** in the application — store them in a separate configuration file on a trusted system and encrypt them
- Use **stored procedures** to abstract data access and allow removal of permissions on base tables
- **Close the connection** as soon as possible
- Remove or change all **default database administrative passwords**; use strong passwords or MFA
- **Turn off unnecessary database functionality** (unnecessary stored procedures, utility packages, default features)
- Remove unnecessary default vendor content (sample schemas)
- **Disable default accounts** that are not required for business purposes
- The application should connect with **different credentials for each trust level** (user, read-only user, guest, administrator)

### File Management Checklist

- Do not pass user-supplied data directly to **dynamic include functions**
- **Require authentication** before allowing file uploads
- **Limit the type of files** that can be uploaded to only those needed for business purposes
- **Validate uploaded file type by checking file headers** — checking the file extension alone is not sufficient (attackers rename malicious files)
- Do **not** save uploaded files in the **same web context as the application** — use a content server or database
- **Prevent or restrict** uploading of files that may be interpreted/executed by the web server
- **Turn off execution privileges** on file upload directories
- When referencing existing files, use a **whitelist of allowed file names and types**; reject anything not on the list
- Do not pass user-supplied data into **dynamic redirects** — if necessary, validate as relative paths only
- Use **index values mapped to pre-defined paths** rather than passing file paths directly
- **Never send the absolute file path** to the client
- Ensure application files and resources are **read-only**
- **Scan user-uploaded files** for viruses and malware

---

## Part 5 — Securing Database Credentials: The GitHub Secrets Solution

**The question (from previous lectures):** How do you securely store database credentials and other secrets in your application and Docker/CI pipeline?

**The answer for GitHub Actions: GitHub Secrets**

GitHub Actions provides **encrypted environment variables** called Secrets:
- Stored encrypted at rest in GitHub's infrastructure
- Injected into workflow runners as environment variables at runtime
- **Never visible in workflow logs** (masked automatically)
- **Not passed to workflows triggered by pull requests from forks** (security feature)
- Accessible to all collaborators with repository access

**Types of secrets:**
- **Repository secrets** — available to all workflows in the repository
- **Environment secrets** — scoped to a specific deployment environment (e.g., `production`, `staging`)

**How to use in a GitHub Actions workflow:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Connect to database
        env:
          DB_HOST: ${{ secrets.DB_HOST }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
        run: ./deploy.sh
```

**What to store as secrets:**
- Database connection strings and passwords
- API keys and tokens (AWS credentials, third-party service keys)
- TLS certificates and private keys (for deployment)
- Any credential referenced in `docker-compose.yml` or Dockerfile

> **Never** hardcode secrets directly in your `Dockerfile`, `docker-compose.yml`, workflow YAML files, or any file that is committed to the repository. Even private repositories have been breached (see Deloitte case study above).

---

## Part 6 — Docker Development Workflow

### Overview

Developing a Docker application follows the same general flow as non-Docker development. The key difference: during development, you deploy and test your application **running within Docker containers** in your local environment.

**6-step Docker development workflow:**

1. **Write code** — develop your application as normal
2. **Create Dockerfiles** — define the image build instructions for each service
3. **Build images** — `docker build` creates the images from your Dockerfiles
4. **Define services (Docker Compose)** — write `docker-compose.yml` to configure multi-service applications
5. **Run containers and test** — `docker run` or `docker-compose up` starts all services; test your application
6. **Push to registry** — `git push` triggers CI/CD; images are pushed to Docker Hub, Amazon ECR, or another registry

---

### Dockerfile

A **Dockerfile** is a text document containing all the commands to assemble a Docker image. Each instruction creates a layer in the image.

```dockerfile
FROM node:18-alpine

# Install build dependencies
RUN apk add --no-cache python3 g++ make

WORKDIR /app

COPY package*.json ./
RUN npm ci --production

COPY . .

EXPOSE 3000
CMD ["node", "server.js"]
```

**Security best practices for Dockerfiles:**
- Use a **specific, pinned base image tag** (not `latest`) — `node:18.17.1-alpine` not `node:latest`
- Run as a **non-root user** — add `USER node` or create a dedicated user
- Use **multi-stage builds** to separate build and runtime stages, keeping secrets out of the final image
- Do not `COPY .` blindly — use `.dockerignore` to exclude `.env`, `.git`, credentials files
- Do not hardcode secrets as `ENV` variables or `ARG` values in the Dockerfile — these are visible in image metadata

---

### Docker Compose

`docker-compose` is a tool for defining and running **multi-container Docker applications**.

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=db
      - DB_PASSWORD=${DB_PASSWORD}    # injected from .env or host env
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

With a single `docker-compose up` command, all services are created and started according to their configuration.

**Security best practices for Docker Compose:**
- Use **environment variable substitution** (`${VAR}`) rather than hardcoding values
- Store actual values in a `.env` file that is **excluded from version control** (in `.gitignore`)
- In CI/CD, inject values via **GitHub Secrets** (not `.env` files)
- Use **named volumes** for persistent data rather than bind mounts in production
- Apply **network segmentation** — only expose ports that must be reachable; internal services communicate on internal Docker networks

---

### Summary Table — Key OWASP Resources

| Resource | URL | Purpose |
|---|---|---|
| OWASP Top 10 Proactive Controls | https://owasp.org/www-project-proactive-controls/ | 10 most important defensive controls for secure development |
| OWASP Cheat Sheet Series | https://cheatsheetseries.owasp.org/ | 78+ topic-specific security guidance sheets |
| OWASP SKF | https://demo.securityknowledgeframework.org/ | Code examples, checklists, labs for multiple languages |
| OWASP Secure Coding Guide | https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/ | Checklist across 12 coding practice areas |
| OWASP Dependency-Check | https://owasp.org/www-project-dependency-check/ | SCA tool — scans dependencies for CVEs |
| Bobby Tables | https://bobby-tables.com/ | SQL injection prevention code examples by language |

---

### Key Secure Coding Takeaways

| Topic | Rule |
|---|---|
| Cryptography | Never roll your own; never transmit plaintext; use established libraries |
| Input validation | Allow list, not block list; validate type, length, range, and format; validate on the server |
| ReDoS | Avoid evil regex patterns with nested quantifiers; use linear-time engines; set timeouts |
| SQL Injection | Use prepared statements (parameterised queries); enforce least privilege on DB accounts |
| Logging | Never log sensitive data; encode before logging; centralise logs; protect log integrity |
| Dependencies | Track all third-party components; scan for CVEs; update regularly |
| Secrets management | Never hardcode credentials; use GitHub Secrets or a vault; never commit `.env` files |
| Docker security | Pin image versions; run as non-root; use `.dockerignore`; inject secrets via env vars |
| File uploads | Validate by header not extension; don't serve from web root; disable execution; scan for malware |
| Memory safety | Prefer memory-safe languages or frameworks where possible; keep C/C++ components updated |

---

### References
- LastPass breach: https://healthitsecurity.com/news/proprietary-info-source-code-stolen-in-lastpass-password-manager-data-breach
- OWASP C9 Security Logging: https://owasp.org/www-project-proactive-controls/v3/en/c9-security-logging
- OWASP ReDoS: https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS
- Microsoft Teams cleartext token storage: https://www.bleepingcomputer.com/news/security/microsoft-teams-stores-auth-tokens-as-cleartext-in-windows-linux-macs/
- Docker microservices development workflow: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/docker-application-development-process/docker-app-development-workflow

---

*End of Lecture 7*
