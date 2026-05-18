# ICT2216 Secure Software Development
## Lecture 4: Secure Software Design

---

### Opening Case Study — Banana Token Hack (11 Sept. 2023)

- Banana Token's price crashed from **$8.70 to $0.02 in under 3 hours**
- Root cause: a design-level vulnerability in the smart contract
- Demonstrates that insecure design — not just buggy code — can cause catastrophic real-world damage

> Reference: https://blog.solidityscan.com/banana-token-hack-analysis-3f6f84c08b8f

---

### Agenda
- General Process of Software Design
- Security by Design Principles (OWASP) — 10 Principles
- Security Architecture

---

## General Process of Software Design

Software design consists of three major layers:

| Layer | Activities |
|---|---|
| **Software Architecture** | Architecture views, architecture patterns |
| **Detailed Design** | Interface design, component design, design patterns |
| **Construction Design** | Flow-based design, table-based design |

The **detailed design** activity builds on the software architecture to provide white-box design elements — the structure and behaviour of the software.

**Two major tasks in detailed design:**

1. **Interface Design** — specifying the interfaces between components
2. **Component Design** — modelling the internal structure and behaviour of components
   - In object-oriented systems, modelled using UML: class diagrams, sequence diagrams

---

### Recap: Software Architecture Techniques
- Block-and-line diagrams
- Component diagrams
- Architectural styles and patterns
- Data flow diagrams

### Recap: Detailed Design Activities
1. Interface design
2. Designing the internal structure of components
3. Modelling internal behaviour of components

---

### The Right Approach to Secure Software

**Flawed Approach:**
> Design and build software first, then add security after the functional requirements are satisfied.

**Better Approach:**
> Build security in from the start — incorporate security-minded thinking into **all phases** of the development process.

---

### Design Flaws vs. Bugs

Software defects consist of two categories:

| Defect Type | Definition | When It Occurs |
|---|---|---|
| **Flaws** | Problems in the **design** | Design phase |
| **Bugs** | Problems in the **implementation** | Coding phase |

> Studies [Gary McGraw, *Software Security: Building Security In*, 2006] show that **50% of security problems are flaws** — not bugs.

This means that even perfect code cannot fix a flawed design. Security flaws must be addressed **before** writing a single line of code.

---

## Security by Design Principles — OWASP

These 10 principles come from the OWASP Development Guide, normalised with Howard and LeBlanc's *Writing Secure Code*:

1. Minimise attack surface area
2. Establish secure defaults
3. Principle of Least Privilege
4. Principle of Defence in Depth
5. Fail securely
6. Don't trust services
7. Separation of duties
8. Avoid security by obscurity
9. Keep security simple
10. Fix security issues correctly

---

### 1. Minimise Attack Surface Area

> Every feature added to an application adds a certain amount of risk to the overall application. When you create a new process or machine, the attack surface **will** increase.

The goal is to reduce overall risk by reducing the attack surface — limiting what is exposed to potential attackers.

**Strategies to reduce attack surface:**
- Limit features to authorised users only
- Gate dangerous functionality through centralised validation routines
- Eliminate unnecessary functionality entirely (best option)

**Example — Web Application Help Feature with Search:**

| Approach | Attack Surface Impact |
|---|---|
| Help feature available to all users | Maximum exposure; SQL injection risk to anyone |
| Help feature limited to authorised users | Reduces the pool of potential attackers |
| Search function gated through centralised data validation | Dramatically reduces ability to perform SQL injection |
| Search function eliminated via better UI design | Almost eliminates the attack surface entirely |

**Mapping the Attack Surface (OWASP Cheat Sheet):**

Read through source code and identify all entry/exit points:
- User interface forms and fields
- HTTP headers and cookies
- APIs
- Files
- Databases
- Other local storage
- Email or other kinds of messages
- Runtime arguments

To keep this manageable, group attack points by function, design, and technology:
- Login/authentication entry points
- Admin interfaces
- Enquiry and search functions
- Data entry (CRUD) forms
- Business workflows
- Transactional interfaces/APIs
- Operational command and monitoring interfaces/APIs
- Interfaces with other applications/systems

> The total number of different attack points can easily add up to thousands or more.

---

### 2. Establish Secure Defaults

> The out-of-the-box experience should be **secure by default**. It should be up to the user to *reduce* their security — if they are allowed to.

**Examples of secure defaults:**
- **HTTPS** enabled by default
- **Login attempt notifications** sent by default
- **Account information change notifications** sent by default
- Users prompted to **reset password on first login** by default

Default insecurity forces users to opt *into* security — which most will never do. Secure defaults flip this: users must opt *out* if they want less security.

---

### 3. Principle of Least Privilege

> Accounts should have the **least amount of privilege** required to perform their business processes.

This applies to:
- User rights
- Resource permissions (CPU limits, memory, network, file system)

**Example — Middleware Server:**

If a middleware server only needs to:
- Access the network
- Read from a specific database table
- Write to a log

…then those are the **only permissions** it should be granted. Under no circumstances should it be given administrative privileges.

**Application-level considerations:**

*Administrator accounts:*
- Can an admin do *anything* in the application?
- Should an admin be allowed to log in as or access normal user information?
- Define the admin's role narrowly — e.g., an admin can trigger a "reset password" email, but the reset link goes **directly to the user**, not to the admin
- An admin should **not** be able to set any password they like

*Development environment:*
- Should a Software Engineer have full access to the production database? **No.**
- Should a DBA have access to all user-related data? **No** — need-to-know applies.

---

### 4. Principle of Defence in Depth

> Where one control would be reasonable, **multiple controls** that approach risks in different ways are better.

Controls used in depth make severe vulnerabilities extremely difficult to exploit. Even if one layer fails, additional layers remain.

**With secure coding, this may take the form of:**
- Tier-based validation (validate at the UI layer, business logic layer, and database layer)
- Centralised auditing controls
- Requiring users to be authenticated on every page

**Example:**

A flawed administrative interface is unlikely to be vulnerable to anonymous attack if it **also**:
- Gates access to production management networks
- Checks for administrative user authorisation
- Logs all access

> Think of all the layers between a client and your full architecture — each layer is an opportunity to stop an attack.

Data flow diagrams (DFDs) help identify where additional defensive layers can be placed.

---

### 5. Fail Securely

> Handling errors securely is a key aspect of secure coding.

When a security control encounters an exception, **the exception must not enable behaviour that the control would normally prevent**.

There are generally three possible outcomes from a security mechanism:
1. **Allow** the operation
2. **Disallow** the operation
3. **Exception** (error)

The exception case must **default to disallow** — not to allow.

**Classic example of insecure failure:**

```java
isAdmin = true;  // ← dangerous initialisation
try {
    codeWhichMayFail();
    isAdmin = isUserInRole("Administrator");
} catch (Exception ex) {
    log.write(ex.toString());
}
```

**Problem:** If `codeWhichMayFail()` throws an exception, `isAdmin` remains `true` — the user is incorrectly granted admin access.

**Fix — initialise to the secure default:**

```java
isAdmin = false;  // ← secure default
try {
    codeWhichMayFail();
    isAdmin = isUserInRole("Administrator");
} catch (Exception ex) {
    log.write(ex.toString());
}
```

> Applications regularly fail to process transactions. **How** they fail determines whether the application is secure.

---

### 6. Don't Trust Services

> Many organisations use third-party partners whose security policies and posture likely differ from yours.

You typically cannot influence or control external third parties — whether home users, major suppliers, or partners.

**Therefore:**
- **Implicit trust of externally run systems is not warranted**
- All external systems should be treated with the same scepticism as untrusted input
- Validate and verify all data received from third-party services

**Discussion point:**
> Using a 3rd-party service ≠ secure. It can also be a way of *transferring* responsibility without actually reducing risk.

If a third-party service is breached, your users' data may still be compromised — even though your own code is perfectly secure.

---

### 7. Separation of Duties

> A key fraud control is ensuring that **no single person can complete a high-risk action alone**.

**Classic example:**
- The person who *requests* a computer cannot also *sign for* it or *receive* it
- This prevents a single user from requesting many computers and claiming they never arrived

**In application design:**
- Certain roles have different levels of trust from normal users
- **Administrators are different from normal users** — in general, administrators should not also be regular users of the application

**Example of correct separation:**

| Role | Permitted Actions |
|---|---|
| Administrator | Turn system on/off, set password policy, manage users |
| Normal User | Browse storefront, make purchases |

**What an admin should NOT be able to do:**
- Log on to the storefront as a super-privileged user
- "Buy" goods on behalf of other users
- Log in to a normal user's account (potential backdoor)

> Even if an admin has the permission to create users and reset passwords — they should **never** be able to log in *as* the user or set the new password themselves.

---

### 8. Avoid Security by Obscurity

> **Security through obscurity is a weak security control** and nearly always fails when it is the only control.

Keeping secrets is not inherently bad — but the **security of key systems must not rely on hidden details** remaining unknown.

**What not to do:**
- Rely on the fact that attackers don't know your source code
- Assume that an attacker won't find an obscure API endpoint

**What to do instead:**
- Reasonable password policies
- Defence in depth
- Business transaction limits
- Solid network architecture
- Fraud and audit controls

**Real-world example — Linux:**
- Linux source code is **widely and publicly available**
- Yet when properly configured and secured, Linux is a hardy, robust, and secure operating system
- Security does not come from keeping the code secret — it comes from sound design

> Code audits and white-box testing are valid and encouraged precisely because security should not depend on keeping implementation details hidden.

---

### 9. Keep Security Simple

> Attack surface area and simplicity go hand in hand.

Overly complex architectures are harder to reason about, harder to audit, and more likely to contain subtle security flaws.

**Developers should avoid:**
- Double negatives in access control logic
- Unnecessarily complex architectural patterns when a simpler approach would do

**Example:**

Instead of a complex cluster of singleton entity beans running on separate middleware servers, consider:
- A simpler approach using **global variables with an appropriate mutex mechanism** to protect against race conditions
- Simpler code is more secure, easier to review, and faster to execute

> Complexity is the enemy of security. If you can't explain why a design decision is necessary, it probably isn't.

---

### 10. Fix Security Issues Correctly

> When a security issue is found, **understand the root cause** before applying a fix.

Steps for correctly fixing a security issue:
1. **Develop a test** for the issue (so you can confirm it is fixed and prevent regression)
2. **Understand the root cause** — not just the symptom
3. **Check for widespread impact** — if design patterns were used, the same vulnerability may exist across multiple code bases
4. **Apply the fix broadly** — test the fix on all affected applications

**Example:**

A user discovers they can see another user's account balance by modifying their cookie.

- The fix *seems* straightforward — adjust the cookie validation logic
- But the cookie handling code is **shared across all applications**
- A fix applied to just one application must be tested on **all other affected applications** to prevent regressions and ensure complete remediation

---

## Security Architecture

> "Applications without security architecture are like bridges built without finite element analysis and wind tunnel testing. They look like bridges — but they will fall at the first flutter of a butterfly's wings."

Security architecture is not optional. The need for security architecture in applications is every bit as great as structural engineering is for physical infrastructure.

---

### The Architect's Responsibility

Application architects must design to cope with:
- **Typical usage** — normal load and user behaviour
- **Extreme attack** — brute force, injection, fraud

Just as bridge designers must account for:
- Normal car and foot traffic
- Cyclonic winds, earthquakes, fire, floods, and traffic incidents

---

### What Security Architecture Is (and Is Not)

**Security architecture IS:**
- A carefully considered set of features, controls, safer processes, and a default-secure posture
- Controls that protect the **confidentiality** of information, **integrity** of data, and **availability** of data to the right users

**Security architecture is NOT:**
- "Markitecture" — a collection of security products bundled together and called a "solution" without coherent design

---

### Two Views of Security Architecture

#### Physical Architecture
- Provides a detailed, tangible representation of the system's **physical infrastructure**
- Shows the relationship among the application's physical components distributed across different geographical locations
- Examples: server locations, data centre layout, network topology, CDN placement

#### Logical Architecture
- Emphasises the **abstract, conceptual view** of a system
- Illustrates the relationships and interactions between **software components**
- Examples: service boundaries, API layers, trust zones, authentication flows, data stores

---

### Summary — Security by Design Principles

| Principle | Core Idea |
|---|---|
| Minimise attack surface | Reduce what is exposed; eliminate unnecessary features |
| Secure defaults | The safe option should be the default out-of-the-box |
| Least privilege | Grant only the permissions absolutely necessary |
| Defence in depth | Layer multiple controls; no single point of failure |
| Fail securely | Errors must default to deny, not allow |
| Don't trust services | Treat all external systems as untrusted |
| Separation of duties | No single person can complete a high-risk action alone |
| Avoid obscurity | Security must not depend on secrets being hidden |
| Keep it simple | Complexity is the enemy of security |
| Fix correctly | Find the root cause; test broadly; prevent regression |

---

### References
- OWASP Security by Design Principles: https://owasp.org/www-project-developer-guide/
- OWASP Attack Surface Analysis Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html
- Howard, M. & LeBlanc, D. *Writing Secure Code*. Microsoft Press.
- McGraw, G. (2006). *Software Security: Building Security In*. Addison-Wesley Professional.

---

*End of Lecture 4*
