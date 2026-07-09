# ICT2216 Secure Software Development
## Lecture 8: Secure Software Implementation (Part 3) — Test Automation & Security Testing References

---

### Opening Case Studies

**Singpass Passkey Rollout (1 July 2025)**

Singapore's national digital identity system rolled out **passkey logins** to address ongoing phishing threats:

- Phishing remained Singapore's **second most common scam** the prior year, with losses of almost S$40 million
- Passkeys eliminate interception risk — because no password or OTP is entered or transmitted during login, there is nothing for a scammer to intercept even if the user lands on a fraudulent website
- Passkeys work by verifying a **private key stored on the user's device** against a public key registered in the Singpass system (FIDO2/WebAuthn)
- Passkeys are additive — they join existing methods: QR login, face verification, and SMS OTP
- If a device is lost or stolen, the Singpass app and passkey are **automatically deactivated** when the user sets up Singpass on a new device
- Initial beta: iPhone (iOS) users first; Android support to follow

---

**282 iOS AI Apps Leaking API Keys**

A study found that all 282 iOS AI apps examined fell into one of three insecure categories:

| Category | Count | Description |
|---|---|---|
| **Plaintext keys** | 54 apps | API key sent in the open — readable from a single captured network request |
| **No key needed** | 92 apps | App routes requests through a server that answers anyone, with no check on who is asking — an open relay to a paid AI account |
| **Replayable tokens** | 136 apps | App issues temporary access tokens (supposed to be safer), but the tokens leak in network traffic and were usually still valid when captured — some were not temporary at all |

> **Design question:** By now, do you know how to secure the API key? (Answer from Lecture 7: store in GitHub Secrets / environment variables; never hardcode in source code or transmit in cleartext.)

---

**Critical OAuth Flaws in Grammarly, Vidio, and Bukalapak**

Critical flaws were found in the OAuth implementation of major platforms. The attack flow illustrates an **OAuth token hijacking** vulnerability:

**How a correct OAuth flow works:**
1. User: "I want to log in using Facebook"
2. Service (Bukalapak) → Facebook: "I need a code as proof of identity"
3. Facebook → User: issues a short-lived authorisation `{code}`
4. User → Service: presents the `{code}`
5. Service → Facebook: exchanges the `{code}` for an access token
6. Facebook → Service: `token_of_Dan_for_bukalapak.com`

**The vulnerability:**
In the flawed implementation, the service sent the `{code}` directly via a POST request — but **did not validate that the code was intended for its own client ID**. An attacker who intercepted or obtained a code issued for a different application could replay it against the vulnerable service.

```
POST https://auth.grammarly.com
{
  "facebook_login": {
    "code": "AQBCz2..."
  }
}
```

**Problem:** The code was issued by Facebook for *another* site but was accepted by Grammarly. The code should only be exchangeable by the OAuth client it was issued to. Failing to verify the `redirect_uri` or `client_id` binding allows cross-site token theft.

> These vulnerabilities were responsibly disclosed between February and April 2023 and have since been fixed.

---

**282 iOS AI Apps — Hardcoded Credentials (continued)**

The DeepSeek findings from last lecture, plus the Codex logging issue, and now 282 iOS apps leaking AI API keys all point to the same systemic problem: **credentials are routinely hardcoded, transmitted in plaintext, or stored insecurely** even in production apps from major developers.

---

**Elon Musk / Twitter — Code Review by Printing**

After Elon Musk acquired Twitter, engineers were reportedly asked to **print out their last 30–60 days of code** for manual review, and to be ready for pairing sessions. A satirical site even offered a "Print Your Code for Review by Elon Musk" tool.

> **Discussion:** Manual code review via printouts is clearly not scalable. What is the right approach to code review in a secure development lifecycle? (Answer: structured peer review in source control + automated static analysis tools in CI/CD)

---

### Agenda

1. Test Automation — Unit, Integration, and GUI Tests
2. Security Test References:
   - OWASP Application Security Verification Standard (ASVS)
   - OWASP Web Security Testing Guide (WSTG)
3. Logging Testing Considerations
4. Security Test Reporting
5. Deliverable 3 Details

---

## Part 1 — Test Automation

### The Testing Pyramid

The **testing pyramid** is a model for the ideal distribution of testing resources:

```
        /\
       /  \        ← UI / End-to-End Tests (few)
      /    \          Minimise: brittle, slow, expensive to maintain
     /------\
    /        \     ← Integration / API Tests (some)
   /          \       Focus: automated, API-centric
  /            \
 /--------------\
/                \  ← Unit Tests (many)
\________________/   Establish solid foundation: fast, cheap, reliable
```

Rising with the pyramid:
- **Complexity** — harder to write and maintain
- **Fragility** — more things can break an end-to-end test
- **Cost of maintenance** — more expensive to update
- **Execution time** — slower feedback cycle
- **Time to locate bug on failure** — harder to pinpoint the root cause

**Key principle:** Automated unit tests should form the **bulk** of your tests. The focus for integration and UI tests should be on **highly automated, API-centric** testing.

**The main objective of security testing:** Verify that the implemented security controls operate as expected and meet the security requirements. Security testing is integrated throughout the SDLC — not bolted on at the end.

---

### Unit Tests

**Unit testing** validates individual units or components of an application — a single method or a single class — in isolation.

**Example (Rails/Ruby):**

```ruby
class UserTest < ActiveSupport::TestCase

  def setup
    @user = User.new(name: 'Example User', email: 'user@example.com',
                     password: 'foobar', password_confirmation: 'foobar')
  end

  test 'should be valid' do
    assert @user.valid?
  end

  test 'name should be present' do
    @user.name = ''
    assert_not @user.valid?
  end

end
```

**What to test in unit tests for secure software:**
- Required fields are enforced
- Field length constraints
- Valid email address format
- Unique email address constraint
- Password complexity / minimum length
- Password confirmation matching

**Unit testing frameworks:** PHPUnit, PyUnit, JUnit

---

### Integration, System, and UI Tests

**Integration and system tests** validate the behaviour of multiple units working together, or the application as a whole.

**Example (Capybara/RSpec — browser automation):**

```ruby
describe 'should be able to login' do
  let(:user) { FactoryGirl.create(:user) }

  before do
    visit login_path
    fill_in 'Email', with: user.email
    fill_in 'Password', with: user.password
    click_button 'Sign in'
  end

  it { should have_selector('h1', text: 'Welcome') }
end
```

This simulates a real browser interaction: visiting the login page, filling in credentials, clicking Sign In, and asserting the welcome page appears.

**Automated integration and UI tests in CI:**

A typical setup uses:
- **Maven** — build and dependency management for Java-based projects
- **TestNG** — test automation framework invoked by `maven-surefire-plugin` to run `@Test` annotated methods
- **Selenium WebDriver** — library for automating browser interactions

The workflow: Dev team pushes code → Jenkins triggers → Maven builds → TestNG/Selenium runs tests → results reported back.

---

### Security Testing in the SDLC

Security testing is integrated at every phase, not just at the end:

| SDLC Phase | Security Testing Activity |
|---|---|
| Definition | Policy review |
| Design & Architecture | Architecture review, UML model review |
| Development | Code review, code walkthroughs |
| Testing | Unit and system tests, penetration testing, configuration audits |
| Deployment | Configuration audits, operational health checks |
| Maintenance | Regression tests, acceptance tests |

The OWASP Testing Framework advocates: **test early and test often** — waiting until code is completely built is costly because defects are much cheaper to fix when found early.

---

## Part 2 — OWASP Application Security Verification Standard (ASVS)

Reference: https://owasp.org/www-project-application-security-verification-standard/

**What is ASVS?**

ASVS is a **catalog of verification requirements** for security controls. It bridges the gap between security requirements and test cases:

```
Requirements → OWASP ASVS → Test Cases → OWASP Web Security Testing Guide (WSTG)
                                        ↓
                                   WSTG Checklist (for reporting)
```

> **Important:** Security testing is never an exact science where all possible test cases can be fully defined. Not all security tests can be automated — a balanced approach of both automated and manual testing is required.

---

### ASVS Verification Levels

ASVS defines **three levels** of security verification:

| Level | Target | Approach |
|---|---|---|
| **Level 1** | Low assurance applications | Completely penetration testable; minimal verification |
| **Level 2** | Applications containing sensitive data | Recommended for most apps; requires security reviews and DevSecOps integration |
| **Level 3** | Most critical applications | High-value transactions, sensitive medical data, highest trust requirements; requires formal reviews, unit and hybrid testing |

---

### ASVS 14 Verification Categories

| Category | Description |
|---|---|
| **V1** | Architecture, Design and Threat Modelling Requirements |
| **V2** | Authentication Verification Requirements |
| **V3** | Session Management Verification Requirements |
| **V4** | Access Control Verification Requirements |
| **V5** | Validation, Sanitisation and Encoding Verification Requirements |
| **V6** | Stored Cryptography Verification Requirements |
| **V7** | Error Handling and Logging Verification Requirements |
| **V8** | Data Protection Verification Requirements |
| **V9** | Communications Verification Requirements |
| **V10** | Malicious Code Verification Requirements |
| **V11** | Business Logic Verification Requirements |
| **V12** | File and Resources Verification Requirements |
| **V13** | API and Web Service Verification Requirements |
| **V14** | Configuration Verification Requirements |

---

### V2: Authentication Verification Requirements

V2 is broken down into sub-categories:

- V2.1: Password Security Requirements
- V2.2: General Authenticator Requirements
- V2.3: Authenticator Lifecycle Requirements
- V2.4: Credential Storage Requirements
- V2.5: Credential Recovery Requirements
- V2.6: Look-up Secret Verifier Requirements
- V2.7: Out of Band Verifier Requirements
- V2.8: Single or Multi-Factor One Time Verifier Requirements
- V2.9: Cryptographic Software and Devices Verifier Requirements
- V2.10: Service Authentication Requirements

---

#### V2.1: Password Security Requirements

Each requirement is mapped to a CWE number and NIST SP 800-63 section:

| ID | Requirement | CWE | NIST § |
|---|---|---|---|
| 2.1.1 | Verify user-set passwords are **at least 12 characters** in length (after collapsing multiple spaces) | 521 | 5.1.1.2 |
| 2.1.2 | Verify passwords **of at least 64 characters** are permitted; passwords **over 128 characters are denied** | 521 | 5.1.1.2 |
| 2.1.3 | Verify password **truncation is not performed** (consecutive multiple spaces may be replaced by a single space) | 521 | 5.1.1.2 |
| 2.1.4 | Verify **any printable Unicode character** is permitted in passwords, including spaces and emoji | 521 | 5.1.1.2 |
| 2.1.5 | Verify users **can change their password** | 620 | — |
| 2.1.6 | Verify password change requires the user's **current and new password** | 620 | — |
| 2.1.7 | Verify passwords are checked against a set of **breached passwords** (e.g., top 1,000–10,000 most common, or via external API using zero-knowledge proof). If breached, user must set a new password | 521 | 5.1.1.2 |
| 2.1.8 | Verify a **password strength meter** is provided | 521 | 5.1.1.2 |
| 2.1.9 | Verify **no password composition rules** that limit character types (no requirement for uppercase, lowercase, numbers, or special characters) | 521 | 5.1.1.2 |
| 2.1.10 | Verify **no periodic credential rotation** or password history requirements | 263 | 5.1.1.2 |
| 2.1.11 | Verify **paste functionality, browser password helpers, and external password managers are permitted** | 521 | 5.1.1.2 |
| 2.1.12 | Verify users can **temporarily view their masked password**, or at least the last typed character, on platforms without this as built-in functionality | 521 | 5.1.1.2 |

> **Note:** These requirements directly align with **NIST SP 800-63** guidelines covered in earlier lectures — no complexity rules, no forced rotation, minimum 12 characters (8 if MFA is used), allow all Unicode including emoji.

---

#### V2.4: Credential Storage Requirements

| ID | Requirement | CWE |
|---|---|---|
| 2.4.1 | Passwords SHALL be **salted and hashed** using an approved one-way key derivation or password hashing function (resistant to offline attacks) | 916 |
| 2.4.2 | Salt SHALL be **at least 32 bits**, chosen arbitrarily; each credential must have a **unique salt value** and the resulting hash stored | 916 |
| 2.4.3 | If PBKDF2 is used, the **iteration count SHOULD be at least 100,000** (or as large as server performance allows) | 916 |
| 2.4.4 | If bcrypt is used, the **work factor SHOULD be at least 10** (or as large as server performance allows) | 916 |
| 2.4.5 | An additional iteration of key derivation SHOULD be performed using a **secret salt known only to the verifier**, stored separately (e.g., in a Hardware Security Module) | 916 |

---

#### V2.5: Credential Recovery Requirements

| ID | Requirement | CWE |
|---|---|---|
| 2.5.1 | System-generated activation/recovery secrets must **not be sent in cleartext** | 640 |
| 2.5.2 | **Password hints or knowledge-based "secret questions" must not be present** | 640 |
| 2.5.3 | Password credential recovery must **not reveal the current password** in any way | 640 |
| 2.5.4 | **Shared or default accounts** (e.g., "root", "admin", "sa") must not be present | 16 |
| 2.5.5 | Users must be **notified when an authentication factor is changed or replaced** | 304 |
| 2.5.6 | Forgotten password recovery must use a **secure mechanism** (e.g., time-based OTP/TOTP, soft token, mobile push, or offline recovery) | 640 |
| 2.5.7 | If OTP or MFA factors are lost, identity must be re-verified at the **same level as during enrollment** | 308 |

---

#### V10: Malicious Code Verification Requirements

| ID | Requirement | CWE |
|---|---|---|
| 10.1.1 | Verify a **code analysis tool** is in use that can detect potentially malicious code (time functions, unsafe file operations, network connections) | 749 |
| 10.2.1 | Verify that source code and third-party libraries **do not contain unauthorised phone-home or data collection** capabilities; where such functionality exists, **user permission must be obtained** before data collection | 359 |
| 10.2.2 | Verify that the application **does not request unnecessary or excessive permissions** to privacy-related features or sensors (contacts, cameras, microphones, location) | 272 |
| 10.2.3 | Verify that source code and third-party libraries **do not contain backdoors** (hardcoded/undocumented accounts or keys, code obfuscation, binary blobs, rootkits, anti-debugging, insecure debug features, or hidden functionality) | 507 |
| 10.2.4 | Verify that source code and third-party libraries **do not contain time bombs** (search for date and time related functions used in suspicious conditions) | 511 |

---

## Part 3 — OWASP Web Security Testing Guide (WSTG)

Reference: https://owasp.org/www-project-web-security-testing-guide/

The WSTG provides detailed test cases for security testing, organised into **11 test categories**:

| Category | Code |
|---|---|
| Information Gathering | OTG-INFO-### |
| Configuration and Deployment Management Testing | OTG-CONFIG-### |
| Identity Management Testing | OTG-IDENT-### |
| Authentication Testing | OTG-AUTHN-### |
| Authorisation Testing | OTG-AUTHZ-### |
| Session Management Testing | OTG-SESS-### |
| Input Validation Testing | OTG-INPVAL-### |
| Testing for Error Handling | OTG-ERR-### |
| Testing for Weak Cryptography | OTG-CRYPST-### |
| Business Logic Testing | OTG-BUSLOGIC-### |
| Client Side Testing | OTG-CLIENT-### |

---

### How to Use ASVS + WSTG Together

**Example workflow** — three security requirements derived from use/misuse case modelling:

1. Password requirements must be aligned with current standards for sufficient complexity
2. Accounts must be locked out after five unsuccessful login attempts
3. Login error messages must be generic

**Step 1:** From security requirement → zoom into appropriate ASVS category → get verification requirements

For requirement 1 → **V2.1 Password Security Requirements:**
- Verify passwords are at least 12 characters (ASVS 2.1.1)
- Verify passwords 64+ characters are permitted (ASVS 2.1.2)
- Verify spaces are allowed and truncation is not performed (ASVS 2.1.3)
- Verify Unicode characters are permitted (ASVS 2.1.4)
- Verify users can change their password (ASVS 2.1.5)
- Verify password change requires current + new password (ASVS 2.1.6)

**Also refer to OWASP Top 10 Proactive Controls C6 (Implement Digital Identity) for implementation guidance:**
- Minimum 8 characters if MFA is also used; 10 characters if not
- All printable ASCII including spaces should be accepted
- Encourage long passwords and passphrases
- Remove complexity requirements — use MFA or longer lengths instead
- Block the top 1,000–10,000 most common passwords (reference: https://github.com/danielmiessler/SecLists/tree/master/Passwords)

**Step 2:** From verification requirements → zoom into relevant WSTG category → get test cases

For requirement 1 → **WSTG Authentication Testing → Testing for Weak Password Policy (OTG-AUTHN-007):**

Test objectives:
- Determine the resistance of the application against brute force password guessing using available password dictionaries by evaluating length, complexity, reuse, and ageing requirements

How to test:
1. What characters are permitted and forbidden? Is the user required to use different character sets?
2. How often can a user change their password? Can they rotate through 5 passwords to reset to their original? (history bypass)
3. When must a user change their password? (Note: NIST and NCSC recommend **against** forced regular expiry, though PCI DSS may require it)
4. How often can a user reuse a password? Does the application maintain a history of the previous 8 passwords?
5. How different must the next password be from the last?
6. Is the user prevented from using their username or other account information in the password?
7. What are the minimum and maximum password lengths, and are they appropriate for the sensitivity of the account?
8. Is it possible to set common passwords such as `Password1` or `123456`?

---

### Testing for Weak Username Policy (OTG-IDENT-05)

**Summary:** User account names are often highly structured (e.g., `jbloggs` for Joe Bloggs, `fnurks` for Fred Nurks), making them guessable.

**Test objectives:**
- Determine whether a consistent account name structure makes the application vulnerable to account enumeration
- Determine whether the application's error messages permit account enumeration

**How to test:**
- Determine the structure of account names
- Evaluate the application's response to valid vs. invalid account names
- Use different responses to valid/invalid account names to enumerate valid ones
- Use account name dictionaries to enumerate valid accounts

**Remediation:** Ensure the application returns **consistent, generic error messages** for all invalid credential combinations — do not differentiate between "username not found" and "incorrect password."

---

### Testing for Weak Lock Out Mechanism (OTG-AUTHN-003)

**For requirement 2: accounts must be locked out after five unsuccessful login attempts.**

Account lockout mechanisms must balance:
- Protecting accounts from unauthorised access (too lenient = brute force succeeds)
- Protecting users from denial of authorised access (too strict = easy to lock out legitimate users)

Accounts are typically locked after 3–5 unsuccessful attempts and unlocked after a predetermined timeout, via self-service, or by an administrator.

**Example test sequence:**

| Step | Action | Expected Result |
|---|---|---|
| 1 | 3 incorrect passwords → correct password | Login succeeds (lockout not triggered at 3) |
| 2 | 4 incorrect passwords → correct password | Login succeeds (lockout not triggered at 4) |
| 3 | 5 incorrect passwords → correct password | "Your account is locked out." |
| 4 | Correct password 5 minutes later | Still locked: "Your account is locked out." |
| 5 | Correct password 10 minutes later | Still locked: "Your account is locked out." |
| 6 | Correct password 15 minutes later | Login succeeds (automatic unlock after 10–15 mins) |

---

### CAPTCHA — A Supplement, Not a Replacement

A CAPTCHA may **hinder** brute force attacks but should **not replace** a proper lockout mechanism. CAPTCHA mechanisms can be bypassed if implemented incorrectly.

**Common CAPTCHA flaws:**
- Easily defeated challenge (simple arithmetic, limited question set)
- Checking HTTP response code rather than response success value
- Server-side logic defaults to "solved" on error
- CAPTCHA result is **never validated server-side** (client-side only)
- CAPTCHA input field is improperly validated or escaped

**How to evaluate CAPTCHA effectiveness:**

1. Assess challenges and attempt to automate solutions
2. Attempt to submit a request without solving CAPTCHA via normal UI
3. Attempt to submit with intentional CAPTCHA failure
4. Submit directly to the server via a proxy (bypassing client-side CAPTCHA check)
5. Fuzz CAPTCHA data entry points with injection payloads and special characters
6. Check if the solution is the alt-text, filename, or a hidden field value
7. Attempt to re-submit previously known good responses (replay)
8. Check if clearing cookies bypasses CAPTCHA (shown only after N failures)
9. In multi-step flows, attempt to skip directly to the step after CAPTCHA
10. Check for alternative API endpoints (e.g., mobile API) that don't enforce CAPTCHA

---

### Unlock Mechanism Testing

Initiate the unlock mechanism and look for weaknesses. Unlock links should be **unique and one-time-use** to prevent an attacker from guessing or replaying them.

> **Important distinction:** An account unlock mechanism is not the same as a password recovery mechanism — though both should follow the same security principles.

**Remediation — unlock mechanisms in order from lowest to highest assurance:**

1. Time-based automatic lockout and unlock
2. Self-service unlock (sends unique unlock link to registered email)
3. Manual administrator unlock
4. Manual administrator unlock with positive user identification

---

### Testing for Account Enumeration (Generic Error Messages)

**For requirement 3: login error messages must be generic.**

**How to test — valid username with wrong password:**

✅ **Correct (generic) error messages:**
```
Authentication failed.
Return to Login page.
```
```
No configuration found. Contact your system administrator.
Return to Login page.
```

❌ **Incorrect (revealing) error messages:**
```
Login for User foo: invalid password.
```

The second format reveals that the username `foo` exists, enabling username enumeration. An attacker can use this to build a list of valid accounts before launching a targeted credential attack.

---

## Part 4 — Logging Testing Considerations

### What Logs Should NOT Contain

Event logs often contain data useful to attackers (information leakage) that can also be used directly in exploits. Review logs for the presence of:

- Debug information and stack traces
- Usernames
- System component names
- Internal IP addresses
- Less-sensitive personal data (email addresses, postal addresses, telephone numbers associated with named individuals)
- Business data

> Any of the above in logs creates an **information disclosure** risk — if an attacker gains log access, they gain reconnaissance data about the system.

---

### Log Location — Why Centralised Logging Matters

Servers generate local logs — but if the server is compromised:
- An attacker can **wipe local logs** to cover their tracks
- Most attacker toolkits include a **"log zapper"** capable of cleaning logs containing specific information (like the attacker's IP address) — routinely included in system-level rootkits

**Consequence:** Local-only logs cannot be trusted after a compromise.

**Solution:** Forward logs to a **separate, centralised, secure logging service** that the compromised server cannot access or modify. This ensures log data survives even if individual nodes are compromised.

---

### Log Rotation Testing

Most servers rotate logs to prevent filling the filesystem. Log rotation should be tested to ensure:

1. Logs are kept for the **time defined in the security policy** — not more, not less
2. Logs are **compressed once rotated** (more logs stored in the same disk space)
3. File system permissions on rotated log files are the **same or stricter** than the active log (e.g., the web server process should not be able to write to rotated logs)
4. An attacker cannot **force logs to rotate** to hide their tracks (e.g., by generating excessive log volume to trigger size-based rotation)

---

### Log Access Control

- **End users must never see event logs** — even a glimpse of log data provides reconnaissance
- **Web administrators should not be able to view raw application logs** — this would break separation of duties
- Access control schemas protecting log access must be **independent** of the access control schema for other application user roles
- **Unauthenticated users must never see any log data**

---

### Log Review — Detecting Attacks in Progress

Log review can reveal active attacks:

| HTTP Status Pattern | Likely Meaning |
|---|---|
| **Large volume of 40x (Not Found) errors** from the same source | CGI scanner or directory enumeration tool being used against the server |
| **50x (Server Error) messages** | Attacker abusing parts of the application that fail unexpectedly — early phases of SQL injection produce 500 errors when the malformed query fails on the backend |

---

## Part 5 — Security Test Reporting

Reference: https://owasp.org/www-project-web-security-testing-guide/stable/5-Reporting/README

After performing security tests, a report must be produced that:
- Is **easy to understand**
- Highlights all risks found in a clear, actionable way

**Standard structure for a security test report:**

1. **Introduction** — scope, objectives, methodology, tools used
2. **Executive Summary** — high-level findings for non-technical stakeholders; overall risk rating
3. **Findings** — detailed description of each vulnerability found:
   - Vulnerability name and category
   - Affected component / URL / parameter
   - Severity rating (Critical / High / Medium / Low / Informational)
   - Description and proof of concept
   - Remediation recommendation
   - References (CVE, CWE)
4. **Appendices** — e.g., the WSTG Checklist showing all test cases conducted and their results

> **Note for D2:** A security test report is not required for Deliverable 2 (which covers implementation). You may include a checklist for automated tests performed. The full security verification report is required for **Deliverable 3**.

---

## Part 6 — Deliverable 3 Details

**Deadline:** Week 13, Monday 27 July, 9:00 AM
**Page limit:** 35 pages (excluding appendices — markers do not need to read appendices)

### D3 Components

**1. Implementation Walkthrough**

- Based on the D2 implementation report of the **assigned** development team (cross-team review)
- Provide feedback on whether sufficient explanation of the logic and flow of code is present to commence secure software verification by a QA/security team
- If insufficient, elaborate on what should be included
- *No communication or argument between development team and QA/security team during this phase*

**2. Source Code Review**

- Manually analyse the **assigned development team's code**
- Describe the findings
- Suggest anything missing and any vulnerabilities found, with remediation recommendations

**3. Static Code Analysis (SAST)**

- Use a suitable automated tool to analyse **separately**:
  - (1) Your own code
  - (2) The assigned development team's code
- Describe the findings
- For vulnerabilities found: include the way to fix them
- **Important:** Do NOT fix vulnerabilities in your own code during D3 (the findings stand as evidence)

**4. Dynamic Application Security Testing (DAST)**

- Dynamically analyse the **assigned development team's code** (running application)
- Describe the findings
- If vulnerabilities are found, include remediation recommendations

**5. Overall Section**

- Provide solutions with references for all vulnerabilities found (referencing CVE and CWE earns bonus marks)
- **Conclusion section** summarising:
  - Overall findings and comments about the application
  - **Security rating** (1 = minimum, 5 = maximum) with justification
  - **Usability rating** (1 = minimum, 5 = maximum) with justification

### Rebuttal Phase (Optional)

- Dev team receives the QA team's D3 report on **27 July**
- Dev team may prepare a **rebuttal report (maximum 1 page)**
- Rebuttal submission deadline: **Week 13, Thursday 30 July, 9:00 AM**

---

### Summary

| Topic | Key Takeaway |
|---|---|
| Testing pyramid | Unit tests (bulk) → Integration/API tests → UI tests (few); automated unit tests are fastest and cheapest to fix |
| Security testing objective | Verify that security controls operate as expected; test early and often, not just at the end |
| ASVS | 14 categories of verification requirements; 3 assurance levels (L1 penetration testable, L2 recommended for most apps, L3 for critical systems) |
| ASVS V2.1 password rules | Min 12 chars, max 128, no complexity rules, no expiry, allow all Unicode, check against breached password lists, allow paste |
| ASVS V2.4 storage | Salted + hashed (bcrypt work factor ≥10, PBKDF2 iterations ≥100,000); salt ≥32 bits, unique per user |
| ASVS V2.5 recovery | No secret questions; no revealing current password; notify on factor change; use TOTP/push for recovery |
| WSTG | 11 test categories; test cases for each ASVS verification requirement |
| Lockout testing | Confirm lockout triggers at correct attempt count; confirm timeout before automatic unlock; test both too-lenient and too-strict thresholds |
| CAPTCHA | Supplement to lockout, not a replacement; validate server-side; test for 10 common bypass techniques |
| Generic error messages | Never reveal whether the username or password was incorrect; always return identical messages |
| Log security | Never log sensitive data; store logs centrally (not locally); protect from tampering; restrict access strictly; review for 40x/50x anomalies |
| D3 | SAST + DAST + manual code review + implementation walkthrough; 35 page limit; security + usability rating with justification |

---

### References
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP WSTG Reporting: https://owasp.org/www-project-web-security-testing-guide/stable/5-Reporting/README
- NIST SP 800-63: https://pages.nist.gov/800-63-3/
- SecLists (common passwords): https://github.com/danielmiessler/SecLists/tree/master/Passwords

---

*End of Lecture 8*
