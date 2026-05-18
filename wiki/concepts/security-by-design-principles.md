---
type: concept
title: "Security by Design Principles"
domain: secure-software-development
complexity: high
tags: [security-design, owasp, secure-defaults, least-privilege, defence-in-depth, fail-secure, attack-surface, separation-of-duties, security-architecture, SSDLC]
updated: 2026-05-19
---

# Security by Design Principles

Security must be built in from the beginning of the design process — not added as an afterthought once functional requirements are satisfied. This concept page covers the foundational motivation (design flaws vs. bugs), the ten OWASP Security by Design Principles, and the role of Security Architecture.

---

## The Right Approach to Secure Software

**Flawed Approach:**
> Design and build software first, then add security after the functional requirements are satisfied.

**Better Approach:**
> Build security in from the start — incorporate security-minded thinking into **all phases** of the development process.

---

## Design Flaws vs. Bugs

Software defects fall into two distinct categories:

| Defect Type | Definition | Phase |
|---|---|---|
| **Flaws** | Problems in the **design** | Design phase |
| **Bugs** | Problems in the **implementation** | Coding phase |

> Gary McGraw (*Software Security: Building Security In*, 2006) found that **50% of security problems are design flaws** — not implementation bugs.

This has a critical implication: even perfect, bug-free code **cannot fix a flawed design**. Security must be addressed before a single line of code is written.

**Real-world example — Banana Token Hack (11 September 2023):**
A design-level vulnerability in a smart contract caused the Banana Token price to crash from **$8.70 to $0.02 in under 3 hours**. The attacker did not exploit a coding error — they exploited the design itself. No amount of careful implementation would have prevented it.

---

## OWASP Security by Design Principles

These ten principles come from the OWASP Development Guide, normalised with Howard and LeBlanc's *Writing Secure Code*.

---

### 1. Minimise Attack Surface Area

> Every feature added to an application adds a certain amount of risk. The goal is to reduce overall risk by reducing what is exposed to potential attackers.

**Strategies:**
- Limit features to authorised users only
- Gate dangerous functionality through centralised validation routines
- Eliminate unnecessary functionality entirely (most effective)

**Web Application Help Feature — impact by approach:**

| Approach | Attack Surface Impact |
|---|---|
| Help available to all users | Maximum exposure; SQL injection risk to anyone |
| Help limited to authorised users | Reduces the pool of potential attackers |
| Search gated through centralised data validation | Dramatically reduces SQL injection risk |
| Search eliminated via better UI design | Near-complete elimination of the attack surface |

**Mapping the Attack Surface (OWASP Cheat Sheet):**

Read source code and identify all entry/exit points:
- User interface forms and fields
- HTTP headers and cookies
- APIs
- Files, databases, local storage
- Email and other message types
- Runtime arguments

Group attack points by function, design, and technology:
- Login/authentication entry points
- Admin interfaces
- Search and enquiry functions
- Data entry (CRUD) forms
- Business workflows
- Transactional interfaces/APIs
- Operational command and monitoring interfaces
- Interfaces with other systems

> The total attack surface of a non-trivial application can easily reach thousands of distinct entry points.

---

### 2. Establish Secure Defaults

> The out-of-the-box experience should be **secure by default**. It should be up to the user to *reduce* their security — not to enable it.

**Examples of secure defaults:**
- **HTTPS** enabled by default
- **Login attempt notifications** sent by default
- **Account information change notifications** sent by default
- Users prompted to **reset their password on first login** by default

The traditional model forces users to opt *into* security — which most will never do. Secure defaults invert this: users must opt *out* if they want reduced security.

---

### 3. Principle of Least Privilege

> Accounts should have the **minimum level of privilege** required to perform their business processes — no more.

Applies to user rights, resource permissions (CPU, memory, network, file system), and service accounts.

**Example — Middleware Server:**

If a middleware service only needs to access the network, read from one specific database table, and write to a log — those are the **only permissions it should have**. Administrative privileges are never warranted.

**Application-level considerations:**

*Administrator accounts:*
- An admin can trigger a "reset password" email — but the reset link goes **directly to the user**, not to the admin
- An admin should **not** be able to set any password directly

*Development environment:*
- A Software Engineer should not have full access to the production database
- A DBA should not have unrestricted access to all user-related data — need-to-know applies

---

### 4. Principle of Defence in Depth

> Where one control would be reasonable, **multiple controls that approach risk from different angles** are better.

Layered controls make a severe vulnerability extremely difficult to exploit. If one layer fails, further layers remain.

**Forms in secure coding:**
- Tier-based validation (validate at the UI layer, business logic layer, and database layer)
- Centralised auditing controls
- Requiring authenticated state to be verified on every page

**Example:**

A flawed administrative interface is unlikely to be exploitable by an anonymous attacker if it **also**:
- Restricts access to production management networks
- Checks for administrative user authorisation
- Logs all access attempts

> Data flow diagrams (DFDs) help identify where additional defensive layers can be inserted — each layer between a client and your data is an opportunity to stop an attack.

---

### 5. Fail Securely

> When a security control encounters an exception, **the exception must not enable behaviour that the control would normally prevent**.

There are three possible outcomes from any security mechanism:
1. Allow the operation
2. Disallow the operation
3. Exception (error)

The exception case must **default to disallow** — never to allow.

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

> Applications regularly fail to process transactions. *How* they fail determines whether the application is secure.

---

### 6. Don't Trust Services

> Many organisations use third-party partners whose security policies and posture likely differ from their own. You typically cannot influence or control external parties.

**Therefore:**
- **Implicit trust of externally run systems is not warranted**
- All external systems must be treated with the same scepticism as untrusted input
- Validate and verify all data received from third-party services

**Discussion point:**
> Using a third-party service ≠ being secure. It can also be a way of *transferring* responsibility without actually reducing risk. If a third-party service is breached, your users' data may still be compromised — even if your own code is perfectly correct.

---

### 7. Separation of Duties

> A key fraud control is ensuring that **no single person can complete a high-risk action alone**.

**Classic example:**
- The person who *requests* a computer cannot also *sign for* it or *receive* it
- This prevents a single user from requesting many machines and claiming they never arrived

**In application design:**

| Role | Permitted Actions |
|---|---|
| Administrator | Turn system on/off, set password policy, manage users |
| Normal User | Browse storefront, make purchases |

**What an admin should NOT be able to do:**
- Log on to the storefront as a super-privileged user
- "Buy" goods on behalf of other users
- Log in directly to a normal user's account (potential backdoor)

> Even if an admin has permission to create users and reset passwords — they should **never** be able to log in *as* the user or set the new password themselves. The reset link must go directly to the user.

---

### 8. Avoid Security by Obscurity

> **Security through obscurity is a weak control** and nearly always fails when it is the only control.

Keeping secrets is not inherently wrong — but the **security of key systems must not rely on hidden implementation details remaining unknown**.

**What not to do:**
- Rely on the fact that attackers don't know your source code
- Assume that an attacker won't discover an obscure API endpoint

**What to do instead:**
- Reasonable password policies
- Defence in depth
- Business transaction limits
- Solid network architecture
- Fraud and audit controls

**Real-world example — Linux:**
Linux source code is widely and publicly available. Yet when properly configured, Linux is a robust and secure operating system. Security comes from sound design — not from keeping the code secret.

> Code audits and white-box testing are valid precisely because security should not depend on hiding implementation details.

---

### 9. Keep Security Simple

> Attack surface area and simplicity go hand in hand. Overly complex architectures are harder to reason about, harder to audit, and more likely to contain subtle security flaws.

**Developers should avoid:**
- Double negatives in access control logic
- Unnecessarily complex architectural patterns when a simpler approach would suffice

**Example:**
Instead of a complex cluster of singleton entity beans running on separate middleware servers, consider a simpler approach using global variables with an appropriate mutex mechanism to protect against race conditions. Simpler code is more secure, easier to review, and faster to execute.

> Complexity is the enemy of security. If you cannot explain why a design decision is necessary, it probably isn't.

---

### 10. Fix Security Issues Correctly

> When a security issue is identified, **understand the root cause** before applying a fix.

**Steps for correct remediation:**
1. **Develop a test** for the issue — confirm it is reproducible and can be used to prevent regression
2. **Understand the root cause** — not just the visible symptom
3. **Check for widespread impact** — if shared design patterns or shared code were used, the same vulnerability may exist across multiple code bases
4. **Apply the fix broadly** — test the fix on all affected applications

**Example:**

A user discovers they can view another user's account balance by modifying their cookie.

- The fix seems straightforward — adjust cookie validation logic
- But the cookie handling code is **shared across all applications**
- A fix applied to one application must be tested on **all other affected applications** to prevent regressions and ensure complete remediation

---

## Security Architecture

> "Applications without security architecture are like bridges built without finite element analysis and wind tunnel testing. They look like bridges — but they will fall at the first flutter of a butterfly's wings."

Security architecture is not optional. Its need in software is every bit as fundamental as structural engineering is for physical infrastructure.

### The Architect's Responsibility

Application architects must design to cope with:
- **Typical usage** — normal load and expected user behaviour
- **Extreme attack** — brute force, injection, fraud attempts, DoS

Just as bridge designers must account for normal traffic *and* cyclonic winds, earthquakes, fire, floods, and traffic incidents.

### What Security Architecture Is (and Is Not)

**Security architecture IS:**
- A carefully considered set of features, controls, safer processes, and a default-secure posture
- Controls that protect the **confidentiality** of information, the **integrity** of data, and the **availability** of data to authorised users

**Security architecture is NOT:**
- "Markitecture" — a collection of security products bundled together and marketed as a "solution" without coherent underlying design

### Physical Architecture vs. Logical Architecture

| View | Focus | Examples |
|---|---|---|
| **Physical Architecture** | Tangible infrastructure and its geographical distribution | Server locations, data centre layout, network topology, CDN placement |
| **Logical Architecture** | Abstract, conceptual relationships between software components | Service boundaries, API layers, trust zones, authentication flows, data stores |

Both views are required for complete security architecture: the physical view reveals network-level attack paths, whilst the logical view reveals trust boundary violations and component-level risks.

---

## Summary Table

| Principle | Core Idea |
|---|---|
| Minimise attack surface | Reduce what is exposed; eliminate unnecessary features |
| Secure defaults | The safe option should be the default out-of-the-box |
| Least privilege | Grant only the permissions absolutely necessary |
| Defence in depth | Layer multiple controls; no single point of failure |
| Fail securely | Errors must default to deny, not allow |
| Don't trust services | Treat all external systems as untrusted |
| Separation of duties | No single person can complete a high-risk action alone |
| Avoid obscurity | Security must not depend on secrets remaining hidden |
| Keep it simple | Complexity is the enemy of security |
| Fix correctly | Find the root cause; test broadly; prevent regression |

---

## Related

- [[secure-software-requirements]] — requirements phase; CIA-AAA defines *what* to protect; these principles define *how* to design the protection
- [[threat-modeling]] — identifies *which* threats these design principles must defend against
- [[owasp-top-10]] — the OWASP Top 10 vulnerabilities are often the direct result of violating these principles
- [[software-design-process]] — the general design pipeline (Architecture → Detailed Design → Construction) into which security design must be integrated
- [[ICT2216-secure-software-development]] — source course
