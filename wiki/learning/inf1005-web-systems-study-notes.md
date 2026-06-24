---
type: learning
status: established
title: "INF1005 Web Systems and Technologies — Exam Study Notes"
domain: web-development
source: "[[sources/INF1005-web-systems-technologies|INF1005 Source]]"
complexity: high
updated: 2026-05-14
tags: [learning, web-development, exam-prep, html, css, javascript, php, security, http, dns]
---

# INF1005 Web Systems and Technologies — Exam Study Notes

Dense Q&A and definition cards for exam preparation. Covers networking, HTML/CSS, JavaScript, PHP, security, and DevOps concepts.

---

## 1. Networking Fundamentals

> [!question]- TCP vs UDP — define both and state when to use each.
> | | TCP | UDP |
> |-|-----|-----|
> | **Stands for** | Transmission Control Protocol | User Datagram Protocol |
> | **Delivery** | Guaranteed — uses sequence numbers, ACKs, and retransmission | Not guaranteed — fire-and-forget |
> | **Ordering** | Packets reassembled in order | No ordering guarantee |
> | **Speed** | Slower (handshake and ACK overhead) | Faster (minimal overhead) |
> | **Use when** | Data integrity is critical: HTTP/S, FTP, SSH, email (SMTP/IMAP) | Speed is critical and loss is acceptable: video streaming, VoIP, online gaming, DNS |

> [!question]- DNS: describe the 10-step resolution process.
> 1. Client makes a domain name request (e.g., `www.example.com`)
> 2. Client checks its **local DNS cache** — if found, return immediately
> 3. Not cached → client queries its configured **primary DNS server** (resolver)
> 4. Primary DNS queries a **Root Name Server**
> 5. Root server returns the address of the appropriate **TLD name server** (e.g., `.com`)
> 6. Primary DNS queries the **TLD name server**
> 7. TLD server returns the address of the **Authoritative DNS Server** for the domain
> 8. Primary DNS queries the **Authoritative DNS Server**
> 9. Authoritative server returns the **IP address** for the domain
> 10. Client makes its actual HTTP/S request to the resolved IP address

> [!question]- State the components of a URL in order.
> `protocol://domain[:port][/path][?query][#fragment]`
> | Component | Example | Notes |
> |-----------|---------|-------|
> | Protocol | `https://` | Connection type |
> | Domain | `www.example.com` | Server address |
> | Port | `:8080` | Optional; default HTTP=80, HTTPS=443 |
> | Path | `/blog/post` | File or directory on server |
> | Query string | `?id=42&lang=en` | Key-value parameters |
> | Fragment | `#section2` | Client-side page anchor |

---

## 2. HTTP Methods and Status Codes

> [!question]- For each HTTP method, state whether it is safe and/or idempotent.
> | Method | Purpose | Safe? | Idempotent? |
> |--------|---------|-------|------------|
> | **GET** | Retrieve a resource; data in URL query string | Yes | Yes |
> | **POST** | Send data (forms, login); data in body | No | No |
> | **PUT** | Update/replace a resource | No | Yes |
> | **DELETE** | Delete a resource | No | Yes |
>
> **Safe** = does not modify server state. **Idempotent** = identical requests produce the same end state (even if repeated multiple times).

> [!question]- State the five HTTP status code families and give key examples from each.
> | Family | Meaning | Key Examples |
> |--------|---------|-------------|
> | **2xx** | Success | 200 OK; 201 Created |
> | **3xx** | Redirection | 301 Moved Permanently; 304 Not Modified (cached) |
> | **4xx** | Client error | 400 Bad Request; 401 Unauthorised; 403 Forbidden; 404 Not Found; 414 URI Too Long |
> | **5xx** | Server error | 500 Internal Server Error; 503 Service Unavailable |

---

## 3. CSS — Cascade, Specificity, and Layout

> [!question]- What is the CSS cascade order? How is specificity calculated?
> When rules conflict, CSS resolves in this priority order (highest wins):
> 1. `!important` declarations
> 2. **Inline styles** (`style="..."`) 
> 3. **ID selectors** (`#id`)
> 4. **Class / attribute / pseudo-class** selectors (`.class`, `[attr]`, `:hover`)
> 5. **Element / pseudo-element** selectors (`p`, `div`, `::first-letter`)
> 6. Universal selector (`*`)
> When specificity is equal, the **later rule** in the stylesheet wins.
> Specificity score (for comparison): ID = 100, Class = 10, Element = 1.
> *Example*: `#nav .link` = 100 + 10 = 110; `div.highlight` = 10 + 1 = 11 → `#nav .link` wins.

> [!question]- Describe the CSS box model from inside out.
> ```
> [ margin     ]   ← space outside the border (separates from neighbours)
>   [ border   ]   ← visible border around the element
>     [ padding ]  ← space inside the border (between border and content)
>       [ content ] ← actual text / images
> ```
> **Border-box sizing** (strongly recommended):
> ```css
> * { box-sizing: border-box; }
> ```
> Makes `width` and `height` include padding and border, preventing unexpected overflow.
> **Collapsing margins**: vertical margins between adjacent block elements collapse to the **larger** value. Horizontal margins never collapse.

> [!question]- Flexbox vs Grid — when do you use each?
> | | Flexbox | CSS Grid |
> |-|---------|---------|
> | Dimensions | **One-dimensional** — a row or a column | **Two-dimensional** — rows and columns simultaneously |
> | Use for | Aligning items within a row or column; navigation bars; centering | Full page layout; complex grid structures |
> | Key properties | `justify-content` (main axis), `align-items` (cross axis), `flex: 1` | `grid-template-columns`, `grid-template-rows`, `gap`, `grid-column` span |
>
> **Best practice**: use Grid for the overall page structure; use Flexbox for aligning content within individual cells or components.

---

## 4. JavaScript Core Concepts

> [!question]- `===` vs `==` — why is strict equality always preferred?
> `==` performs **type coercion** before comparison:
> - `"5" == 5` → `true` (string coerced to number)
> - `null == undefined` → `true`
> - `0 == false` → `true`
> - `"" == false` → `true`
>
> `===` compares value **and type** with no coercion:
> - `"5" === 5` → `false`
> - `null === undefined` → `false`
>
> Use `===` at all times to avoid subtle bugs from unexpected coercion. The only exception is `== null` to check for both `null` and `undefined` simultaneously (an accepted convention).

> [!question]- Describe the three phases of event propagation in order.
> 1. **Capture phase** — the event travels from the document root **down** to the target element; listeners added with `{ capture: true }` fire here
> 2. **Target phase** — the event fires on the exact target element
> 3. **Bubble phase** — the event travels back **up** from the target to the root; most `addEventListener` listeners fire here by default
>
> `e.stopPropagation()` — stops the event from travelling further in either direction.
> `e.preventDefault()` — cancels the browser's default behaviour (e.g., form submission, link navigation) without stopping propagation.

> [!question]- Explain the async evolution: callback → Promise → async/await.
> **Problem**: network calls are asynchronous; naïve code blocks the browser.
> **Promises** represent a value that may not be available yet:
> ```javascript
> fetch("/api/data")
>   .then(response => response.json())
>   .then(data => { /* use data */ })
>   .catch(error => console.error(error));
> ```
> **async/await** (ES7) is syntactic sugar over Promises — makes asynchronous code read like synchronous code:
> ```javascript
> async function loadData() {
>   try {
>     const response = await fetch("/api/data");
>     const data = await response.json();
>     return data;
>   } catch (err) { console.error(err); }
> }
> ```
> `await` suspends the function until the Promise resolves — without blocking the event loop.

---

## 5. PHP and Server-Side Web Development

> [!question]- Name the key PHP superglobals and state what each holds.
> | Superglobal | Contains |
> |-------------|---------|
> | `$_GET` | URL query string parameters (`?key=value`) |
> | `$_POST` | Form data sent via HTTP POST |
> | `$_REQUEST` | Combined GET, POST, and COOKIE |
> | `$_SERVER` | Server and execution environment info (e.g., `$_SERVER['REMOTE_ADDR']`) |
> | `$_SESSION` | Session variables (persisted across requests for the same user) |
> | `$_COOKIE` | HTTP cookie values |
> | `$_FILES` | Uploaded file information |
> | `$_ENV` | Environment variables |

> [!question]- State the three-step PDO prepared statement pattern.
> ```php
> // Step 1: Prepare — SQL with placeholders
> $stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
>
> // Step 2: Bind — associate a value with the placeholder
> $stmt->bindValue(':id', $_GET['id'], PDO::PARAM_INT);
>
> // Step 3: Execute — run the query
> $stmt->execute();
> $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
> ```
> The database driver treats the bound values as pure **data**, never as SQL syntax — this is what prevents SQL injection.

---

## 6. Web Security

> [!question]- SQL injection: describe the attack pattern and the defence.
> **Attack**: malicious SQL code embedded in user input:
> ```sql
> -- Input: ' OR '1'='1
> SELECT * FROM users WHERE username='' OR '1'='1'; -- always true → all rows returned
> ```
> This can log in as any user, extract all data, or (with stacked queries) drop tables.
> **Defence**: use **prepared statements / parameterised queries** exclusively. Never concatenate user input into a SQL string. Validate and sanitise all inputs server-side.

> [!question]- XSS: distinguish reflected vs stored XSS, and state the defences.
> | Type | How it works |
> |------|-------------|
> | **Reflected XSS** | Malicious script is embedded in a URL; when the victim clicks the link, the server reflects it back in the response (e.g., search result page echoes the query) |
> | **Stored XSS** | Malicious script is stored in the database (e.g., a comment field); every visitor who loads that page executes it |
>
> **Defences**:
> - Escape all user-controlled output: `htmlspecialchars($_POST['comment'])` in PHP (converts `<script>` to `&lt;script&gt;`)
> - Sanitise input before storing it
> - Set a **Content Security Policy (CSP)** HTTP header to restrict which scripts may execute
> - Never set `innerHTML` from user-controlled data in JavaScript — use `textContent` instead

> [!question]- CSRF: describe the attack and the token defence.
> **Attack**: a malicious website or email contains a request (form or image tag) that targets a site where the victim is already authenticated. The victim's browser automatically includes session cookies, so the server processes the request as legitimate.
> *Example*: `<img src="https://bank.com/transfer?to=attacker&amount=1000">`
>
> **Defence**: include a **CSRF token** — a unique, unpredictable, per-session value — in every state-changing form as a hidden field:
> ```html
> <input type="hidden" name="csrf_token" value="randomUniqueToken123">
> ```
> The server validates the token on every POST request. A cross-origin attacker cannot read the token (same-origin policy) and therefore cannot forge a valid request.

> [!question]- bcrypt vs MD5 for password storage — why is MD5 inadequate?
> **MD5**: a fast cryptographic hash function.
> - Fast = bad for passwords: attackers can compute billions of hashes per second
> - Vulnerable to **rainbow table attacks** (precomputed hash → plaintext lookups)
> - No built-in salt
>
> **bcrypt**: a deliberately slow, adaptive hashing function designed specifically for passwords.
> - Built-in **salting**: generates a unique random salt for each password → identical passwords produce different hashes → rainbow tables are useless
> - **Work factor (cost)**: can be increased over time as hardware speeds up
> - PHP: `password_hash($pw, PASSWORD_BCRYPT)` and `password_verify($input, $stored_hash)`

> [!question]- State the CIA triad definitions.
> | Property | Definition |
> |----------|-----------|
> | **Confidentiality** | Data is protected from unauthorised access — only authorised parties can read it |
> | **Integrity** | Data is accurate and unaltered — unauthorised modification is detected and prevented |
> | **Availability** | Systems and data are accessible to authorised users when needed |

> [!question]- Expand the STRIDE acronym and state what each threat is.
> | Letter | Threat | Description |
> |--------|--------|-------------|
> | **S** | **Spoofing** | Attacker uses someone else's identity or credentials |
> | **T** | **Tampering** | Unauthorised modification of data in transit or at rest |
> | **R** | **Repudiation** | Attacker removes traces of malicious actions; denies performing them |
> | **I** | **Information Disclosure** | Sensitive data exposed to unauthorised parties |
> | **D** | **Denial of Service** | Legitimate users are prevented from accessing the system |
> | **E** | **Elevation of Privilege** | Attacker gains permissions beyond those granted |

---

## Quick Reference

| Concept | Key Rule |
|---------|---------|
| TCP vs UDP | TCP = reliable, ordered; UDP = fast, no guarantee |
| DNS resolution | Client → cache → resolver → root → TLD → authoritative → IP |
| HTTP safe methods | GET, HEAD only |
| HTTP idempotent | GET, PUT, DELETE (not POST) |
| CSS specificity | ID(100) > Class(10) > Element(1); later rule wins on tie |
| Box model (inside out) | content → padding → border → margin |
| Flexbox | 1D; justify-content (main axis); align-items (cross axis) |
| Grid | 2D; grid-template-columns/rows; fr units |
| `===` vs `==` | Always use `===`; `==` coerces types |
| Event propagation | Capture → Target → Bubble |
| SQL injection defence | Prepared statements with bound parameters |
| XSS defence | `htmlspecialchars()` on output; CSP header |
| CSRF defence | Server-validated CSRF token in every state-changing form |
| bcrypt advantage | Built-in salt + slow work factor |

## See Also

- [[concepts/web-fundamentals|Web Fundamentals]]
- [[concepts/html-and-css|HTML and CSS]]
- [[concepts/javascript-fundamentals|JavaScript Fundamentals]]
- [[concepts/web-security-and-devops|Web Security and DevOps]]
