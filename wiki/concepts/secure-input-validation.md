---
type: concept
address: c-000097
title: "Secure Input Validation"
domain: secure-software-development
complexity: high
created: 2026-07-02
updated: 2026-07-02
tags: [concept, input-validation, sql-injection, redos, allow-list, regex, owasp, secure-coding]
related:
  - concepts/owasp-top-10
  - concepts/secure-design-implementation
  - concepts/secure-deployment-practices
---

# Secure Input Validation

Input validation ensures that only properly formed data enters a software system. It is a **defence-in-depth** layer — it should be applied as early as possible in the data flow, but it is not the primary defence against XSS or SQL injection. Output encoding and parameterised queries are the primary defences for those; validation reduces the blast radius when those controls are absent or fail.

**OWASP Proactive Control C3: Validate All Input & Handle Exceptions.**

---

## The Core Problem — Injection

Injection attacks occur when an application confuses **data for executable commands**. User input is processed by an interpreter that treats it as instructions.

| Injection Type | Interpreter | Execution Environment |
|----------------|-------------|----------------------|
| SQL Injection | Database engine | Database server |
| Remote Command Injection (RCE) | OS shell / template engine | Web application server |
| XSS / JavaScript Injection | JavaScript engine | Victim's browser |
| Log Injection | Log parser / SIEM | Monitoring system |
| ReDoS | Regex engine (NFA) | Web server / WAF |

The unifying principle: **never pass unvalidated user input to an interpreter**.

---

## Allow-List vs. Block-List

### Block-List (Deny-List) — Do Not Use

Attempting to detect dangerous characters (`'`, `<`, `>`, `1=1`) or known attack strings is **fundamentally flawed**:

- Trivially bypassed by URL encoding (`%27` = `'`), case changes (`<ScRiPt>`), or alternative representations (`CHAR(39)` in SQL)
- Block lists also reject legitimate input — the apostrophe in `O'Brian` is valid
- Attackers always discover new bypass techniques faster than defenders add to the block list

### Allow-List (Whitelist) — Always Prefer

Define exactly what **is** permitted. Anything not on the list is rejected by default.

```python
# Block-list (broken): trying to filter "bad" characters
if "'" in username or "--" in username:
    raise ValueError("Invalid input")
# Bypass: username = "OR 1=1 /*"   ← no single quote needed

# Allow-list (correct): define exactly what's valid
import re
if not re.fullmatch(r'^[a-zA-Z0-9_]{3,30}$', username):
    raise ValueError("Username must be 3-30 alphanumeric characters or underscores")
```

---

## Input Validation Layers

Apply in this order — each layer catches different error classes:

### 1. Framework Validators

Use your web framework's built-in validation first. It is well-tested, community-maintained, and handles the most common cases.

- Django: `Form` / `Serializer` validators, `validators=[]` field argument
- Flask: `WTForms` validators
- Java: JSR-303/JSR-349 Bean Validation (`@NotNull`, `@Size`, `@Pattern`)

### 2. Schema Validation (JSON / XML)

Validate structured inputs against a formal schema before processing.

```python
# JSON Schema validation (Python: jsonschema library)
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string", "minLength": 3, "maxLength": 30},
        "age":      {"type": "integer", "minimum": 0, "maximum": 150}
    },
    "required": ["username"]
}
validate(instance=request_data, schema=schema)
```

### 3. Type Conversion with Strict Exception Handling

Let the language's type system reject malformed input — catch and handle exceptions explicitly.

```python
# Wrong — silent failure
age = int(request.form.get("age", 0))   # "abc" → ValueError, not caught

# Correct — explicit handling
try:
    age = int(request.form["age"])
except (ValueError, KeyError):
    return jsonify({"error": "age must be an integer"}), 400
```

### 4. Range and Length Checks

Enforce explicit bounds for every numeric and string field.

```python
if not (0 <= age <= 150):
    raise ValueError("Age must be between 0 and 150")

if not (3 <= len(username) <= 30):
    raise ValueError("Username must be 3–30 characters")
```

### 5. Enumerated Value Checking

For fields with a fixed set of valid values, reject anything not in the set.

```python
VALID_SORT = {"ASC", "DESC"}
if sort_direction not in VALID_SORT:
    raise ValueError("sort_direction must be ASC or DESC")

VALID_STATUSES = {"pending", "active", "closed"}
if status not in VALID_STATUSES:
    raise ValueError("Invalid status")
```

### 6. Regular Expression Validation

For structured data not covered by the above layers. Apply carefully — see ReDoS section below.

**Rules for safe validation regex:**
- Anchor the entire string with `^` and `$`
- Define the **allowed** character set (not what to reject)
- Specify **minimum and maximum** length
- Avoid `.` and `\S` wildcards — they are too permissive
- Avoid nested quantifiers (see ReDoS)

```python
import re

# UK postcode
POSTCODE_RE = re.compile(r'^[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}$')

# US ZIP code (5 digits, optional -4)
ZIP_RE = re.compile(r'^\d{5}(-\d{4})?$')

# Date YYYY-MM-DD
DATE_RE = re.compile(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$')

if not POSTCODE_RE.fullmatch(user_postcode):
    raise ValueError("Invalid postcode format")
```

---

## Validating Free-Form Unicode Text

Name fields, comment boxes, and other free-text inputs cannot be restricted to ASCII. Apply these techniques:

**1. Unicode Normalisation** — before any validation, normalise to a canonical form (NFC or NFKC). This prevents attacks using visually identical but technically different character sequences (homoglyph attacks, zero-width joiners, etc.).

```python
import unicodedata
normalised = unicodedata.normalize("NFC", raw_input)
```

**2. Category Allow-Listing** — Unicode defines character categories (letters across all scripts, decimal digits, punctuation). Allow only the categories relevant to your field.

```python
import unicodedata
def is_allowed_char(ch):
    cat = unicodedata.category(ch)
    return cat.startswith('L') or cat.startswith('N')   # letters or numbers across all scripts
```

**3. Individual Character Exceptions** — add specific punctuation characters that your application genuinely requires (e.g., apostrophe for Irish names, hyphen for compound names).

> **Edge case to document:** Does your application accept emoji? Unicode emoji occupy supplementary planes (U+1F000+) and may require `re.UNICODE` flags and surrogate pair handling in Python 2 (not in Python 3). Decide explicitly and encode the decision in validation logic.

---

## Regular Expression Denial of Service (ReDoS)

### What It Is

A Denial of Service attack that exploits the **catastrophic backtracking** behaviour of NFA-based regex engines. A crafted input causes the engine to explore exponentially many paths before concluding no match, hanging the thread for seconds or minutes.

### How It Works

NFA regex engines try every possible interpretation when a match fails. For certain patterns, the number of paths explored grows **exponentially** with input length.

**Example — pattern `^(a+)+$`:**

| Input | a count | Paths explored |
|-------|---------|---------------|
| `aaaaX` | 4 | 16 |
| `aaaaaaaaX` | 8 | 256 |
| `aaaaaaaaaaaaaaaaaX` | 16 | 65,536 |
| `aaaaaaaaaaaaaaaaaaaaaaaaX` | 24 | 16,777,216 |

Each additional `a` doubles the path count. The `X` at the end forces exhaustive exploration (the engine must prove no match exists).

### Evil Regex Patterns

Patterns vulnerable to ReDoS share a common structure: **grouping with repetition where the repeated group itself contains repetition or overlapping alternation**.

```
(a+)+           ← inner + inside outer +
([a-zA-Z]+)*    ← inner + inside outer *
(a|aa)+         ← overlapping alternation with repetition
(a|a?)+         ← overlapping alternation with repetition
(.*a){x}        ← for x > 10, potentially catastrophic
```

All are hung by inputs like: `aaaaaaaaaaaaaaaaaaaaaaaX`

### Attack Surfaces

- Web application servers (any request containing user-supplied data validated by an evil regex)
- Web Application Firewalls (WAFs) that apply their own regex-based rules
- Database servers (SQL `REGEXP` operator with user-supplied patterns)
- If the **regex itself is user-supplied** (e.g., a search filter field), an attacker can inject an evil regex directly

### Mitigation

| Approach | Detail |
|----------|--------|
| Use a linear-time engine | **RE2** (Google) guarantees O(n) matching — no backtracking. Python: `pip install google-re2`; Go: `regexp` package uses RE2 by default |
| Avoid evil patterns | Never write `(a+)+`, `([a-zA-Z]+)*`, or alternation-with-repetition. Prefer possessive quantifiers (`a++`) or atomic groups `(?>a+)` where the engine supports them |
| Set execution timeouts | Interrupt regex evaluation after a bounded time limit |
| Test patterns | Use tools like vuln-regex-detector or RXXR2 to test patterns for catastrophic backtracking before deployment |

```python
# Vulnerable pattern
import re
evil_re = re.compile(r'^(a+)+$')
# evil_re.fullmatch('a' * 25 + 'X')   ← hangs

# Safe alternative using RE2 (linear-time)
import re2
safe_re = re2.compile(r'^a+$')         ← no backtracking possible
```

---

## SQL Injection Prevention

**OWASP Proactive Control C3; OWASP Cheat Sheet — SQL Injection Prevention.**

### Defence 1 — Prepared Statements (Parameterised Queries) ✅ Gold Standard

The query structure is defined first as a template with placeholders. User input is bound as parameters that are **never interpreted as SQL syntax** by the database.

```python
# Vulnerable — string concatenation
username = request.form['username']
cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
# Attack: username = "' OR '1'='1" → dumps entire table

# Safe — parameterised query
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
# The DB driver handles quoting/escaping internally; no SQL interpretation possible
```

```java
// Java — PreparedStatement
String query = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement stmt = conn.prepareStatement(query);
stmt.setString(1, username);
stmt.setString(2, password);   // Each value is bound, not concatenated
ResultSet rs = stmt.executeQuery();
```

**Why it works:** The database receives the query structure and the parameter values as separate entities. The query is compiled before parameters are bound — there is no mechanism by which parameter content can be interpreted as SQL syntax.

### Defence 2 — Stored Procedures (Properly Constructed)

Equivalent to prepared statements when parameterised internally. However, stored procedures that use string concatenation internally are still vulnerable:

```sql
-- Safe stored procedure (parameterised)
CREATE PROCEDURE GetUser(@Username NVARCHAR(50))
AS
    SELECT * FROM Users WHERE Username = @Username   ← bound parameter

-- Vulnerable stored procedure (dynamic SQL)
CREATE PROCEDURE GetUser(@Username NVARCHAR(50))
AS
    EXEC('SELECT * FROM Users WHERE Username = ''' + @Username + '''')   ← still injectable
```

### Defence 3 — Allow-List for Non-Parameterisable Query Parts

Table names, column names, and sort direction **cannot be parameterised** in most database drivers. Validate against a strict allow-list.

```python
ALLOWED_COLUMNS  = {"id", "username", "email", "created_at"}
ALLOWED_SORT_DIR = {"ASC", "DESC"}

if column not in ALLOWED_COLUMNS:
    raise ValueError(f"Invalid column: {column}")
if sort_dir not in ALLOWED_SORT_DIR:
    raise ValueError(f"Invalid sort direction: {sort_dir}")

query = f"SELECT * FROM users ORDER BY {column} {sort_dir}"   # safe — both validated
```

### Defence 4 — Escaping (Last Resort Only)

Database-specific character escaping. Error-prone, easy to forget, not portable across databases. Use **only** when refactoring to parameterised queries is temporarily blocked.

### Additional Defences

- **Enforce least privilege on the database account.** The application's DB user should have only the permissions needed for its operations. A read-heavy app should have SELECT only, never DROP or CREATE.
- **Input validation as secondary defence.** Even with parameterised queries, validating format and length adds a layer of defence-in-depth.

Reference: https://bobby-tables.com/python — practical code examples by language.

---

## Complexity Summary

| Validation Layer | What It Catches | Performance |
|-----------------|-----------------|-------------|
| Framework validators | Common field errors, type errors | O(1) per field |
| Schema validation | Structural errors, missing fields | O(size) |
| Type conversion | Non-numeric in numeric field | O(1) |
| Range/length check | Out-of-bounds values | O(1) |
| Enumerated value | Unknown enum members | O(1) hash lookup |
| Regex (RE2) | Format violations | O(n) guaranteed |
| SQL parameterisation | SQL injection | O(1) overhead over raw query |

---

## See Also

- [[concepts/owasp-top-10]] — A05 Injection and A10 Mishandling of Exceptional Conditions
- [[concepts/secure-design-implementation]] — output encoding, authentication design, accountability logging
- [[concepts/secure-deployment-practices]] — security logging rules; component security; secrets management
- [[sources/ICT2216-lecture-7-secure-coding]] — source lecture
