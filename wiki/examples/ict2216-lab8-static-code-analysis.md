---
name: ict2216-lab8-static-code-analysis
description: ICT2216 Lab 8 — Static Code Analysis with ESLint, security plugins (eslint-plugin-security, security-node, no-unsanitized), SARIF output, and GitHub CodeQL
metadata:
  type: example
domain: secure-software-development
course: ICT2216
created: 2026-06-23
tags: [sast, eslint, codeql, sarif, static-analysis, github-actions, security-plugins, lab]
---

# ICT2216 Lab 8 — Static Code Analysis

**Lab file:** `Lab8/X08 - Static Code Analysis.pdf`
**Support files:** `Lab8/cda-eslint.yml`, `Lab8/codeql.yml`

## Lab Structure

| Step | Topic |
|------|-------|
| 4 | Configure ESLint + SARIF formatter; GitHub Actions workflow |
| 5.1 | `eslint-plugin-security` — eval, ReDoS, Buffer |
| 5.2 | `eslint-plugin-security-node` — Node.js specific issues |
| 5.3 | `eslint-plugin-no-unsanitized` — XSS / DOM manipulation |
| 6 | GitHub CodeQL workflow |

## Key Concept: SARIF

**SARIF** (Static Analysis Results Interchange Format) is the standard format GitHub Code Scanning accepts. ESLint results must be converted to SARIF before uploading. The `@microsoft/eslint-formatter-sarif` package handles this.

After upload, results appear under **Security → Code Scanning** in the GitHub repo.

## ESLint Setup (Modern Flat Config)

```bash
npm install eslint@latest --save-dev
npm install @microsoft/eslint-formatter-sarif --save-dev
npx eslint --init   # generates eslint.config.mjs
```

**Run locally:**

```bash
npx eslint .
npx eslint . --format=@microsoft/eslint-formatter-sarif --output-file=reports/eslint-results.sarif
```

**Config file:** `eslint.config.mjs` (Flat Config — array of objects, direct plugin imports, no `extends` keyword).

## GitHub Actions Workflow (cda-eslint.yml → `.github/workflows/eslint.yml`)

Single job: checkout → cache → npm install → mkdir reports → run ESLint → upload SARIF.

Key line (uses `|| true` to prevent non-zero exit from blocking artifact upload):
```bash
npx eslint . --format @microsoft/eslint-formatter-sarif --output-file reports/eslint-results.sarif || true
```

Then:
```yaml
- uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: reports/eslint-results.sarif
```

## Security Plugins Summary

| Plugin | Detects | Install |
|--------|---------|---------|
| `eslint-plugin-security` | `eval()`, ReDoS, insecure `Buffer()` | `npm i eslint-plugin-security -D` |
| `eslint-plugin-security-node` | Insecure HTTP headers, improper user input (Node.js) | `npm i eslint-plugin-security-node -D` |
| `eslint-plugin-no-unsanitized` | XSS via improper DOM manipulation | `npm i eslint-plugin-no-unsanitized -D` |

### eslint-plugin-security config snippet

```js
import pluginSecurity from "eslint-plugin-security";

plugins: { security: pluginSecurity },
rules: { "security/detect-eval-with-expression": "error" },
```

### eslint-plugin-security-node config snippet

```js
import securityNode from 'eslint-plugin-security-node';

plugins: { 'security-node': securityNode },
rules: { 'security-node/detect-crlf': 'error' },
```

### eslint-plugin-no-unsanitized config snippet

```js
import eslintPluginNoUnsanitized from 'eslint-plugin-no-unsanitized';

plugins: { 'no-unsanitized': eslintPluginNoUnsanitized },
rules: { ...eslintPluginNoUnsanitized.configs.recommended.rules },
```

## GitHub CodeQL (codeql.yml → `.github/workflows/codeql.yml`)

GitHub's own semantic code analysis engine. Scans for vulnerabilities at a deeper level than linting. Uses a matrix strategy to support multiple languages.

```yaml
strategy:
  matrix:
    language: [ 'javascript' ]
steps:
  - uses: github/codeql-action/init@v3
    with:
      languages: ${{ matrix.language }}
  - uses: github/codeql-action/analyze@v3
```

Requires `permissions: security-events: write`.

## Lab Notes

- ESLint ≠ full SAST — it focuses on code quality/style. Security plugins extend it but don't replace dedicated tools.
- Dedicated SAST alternatives: **Semgrep** (lightweight, customisable), **SonarQube** (next lab).
- Other SARIF-compatible tools: Flake8 (Python), Checkstyle (Java), PMD (Java/Apex), SonarCloud (multi-language).

## Related

- [[concepts/github-actions-cicd]] — CI/CD pipeline; where SAST jobs fit
- [[examples/ict2216-lab9-sonarqube]] — Lab 9: SonarQube (deeper SAST)
- [[examples/ict2216-lab7-automated-testing]] — Lab 7: automated testing in the same pipeline
- [[concepts/owasp-top-10]] — A03 Injection / A07 XSS — what these plugins detect
