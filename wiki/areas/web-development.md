---
type: area
status: established
title: "Web Development"
domain: web-development
source: [[sources/INF1005-web-systems-technologies]]
updated: 2026-05-14
tags: [area, web-development]
---

# Web Development

**Source**: INF1005 — *Fundamentals of Web Development* (Connolly & Hoar, 3rd Ed.), SIT.

---

## What I Know

The full web stack from network fundamentals to modern frameworks. The Internet (1969) is the infrastructure; the Web (1989, Berners-Lee) is the application. INF1005 covers 21 chapters spanning HTML/CSS, JavaScript, PHP, Node.js, MySQL, security, and DevOps.

**Core model**: browser (client) ↔ HTTP ↔ server. The client renders HTML/CSS/JS; the server processes requests, queries databases, and returns responses. Security threats originate wherever user input crosses a trust boundary.

---

## Concept Pages

| Page | What It Covers |
|------|---------------|
| [[concepts/web-fundamentals\|Web Fundamentals]] | TCP/IP model, DNS resolution, URLs, HTTP methods/status codes, browser rendering |
| [[concepts/html-and-css\|HTML and CSS]] | Semantic HTML5, tables, forms, CSS selectors/cascade/box model, Flexbox, Grid, responsive design, WCAG |
| [[concepts/javascript-fundamentals\|JavaScript Fundamentals]] | Types, closures, DOM, events, async/await, Fetch API, ES6 modules, browser APIs |
| [[concepts/server-side-web-development\|Server-Side Development]] | PHP, LAMP stack, MySQL/PDO, Node.js, Express, REST API, WebSockets, NoSQL |
| [[concepts/web-security-and-devops\|Web Security & DevOps]] | CIA/STRIDE, XSS/SQLi/CSRF defences, TLS, bcrypt, CI/CD, hosting, DNS records |

---

## Key Ideas

- **Separation of concerns**: HTML = structure, CSS = presentation, JavaScript = behaviour. Mixing them causes maintenance problems
- **Validation layers**: HTML5 (hint) → JavaScript (UX) → server-side (only guaranteed). Never rely solely on client-side validation
- **Security principle**: treat all user input as hostile until sanitised. `htmlspecialchars()` for XSS; prepared statements for SQLi; CSRF tokens for form submissions
- **Node.js event loop**: single-threaded but non-blocking — delegates I/O to OS, then processes callbacks; scales better than thread-per-request (PHP/Apache) model
- **REST is a contract**: both server (Express route) and client (Retrofit/Fetch) agree on URL pattern, HTTP verb, and JSON shape

---

## Cross-Domain Connections

- [[synthesis/web-security-ssdlc-bridge|Attack Patterns ↔ SSDLC Process]] — web developer's XSS/SQLi knowledge maps to OWASP ASVS requirements
- [[synthesis/rest-api-cross-stack|REST API Cross-Stack]] — Express server ↔ Android Retrofit client
- [[concepts/relational-database-fundamentals|Relational DB Fundamentals]] — INF2003 provides the theory behind INF1005's basic PDO/SQL
- [[concepts/owasp-top-10|OWASP Top 10]] — formal security vulnerability catalogue complementing INF1005's code-level defences

---

## Study Notes

[[learning/inf1005-web-systems-study-notes|INF1005 Study Notes]] — exam-prep summaries
