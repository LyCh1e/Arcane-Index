---
name: ict2216-lab7-automated-testing
description: ICT2216 Lab 7 — GitHub Actions with automated unit testing (Mocha/Chai) and Selenium integration/UI testing on a Node.js app
metadata:
  type: example
domain: secure-software-development
course: ICT2216
created: 2026-06-23
tags: [github-actions, unit-testing, selenium, mocha, chai, node-js, integration-testing, lab]
---

# ICT2216 Lab 7 — GitHub Actions with Automated Testing

**Lab file:** `Lab7/X07 - Github Actions with Automated Testing.pdf`
**Support files:** `Lab7/github-actions-nodejs-test.zip`, `Lab7/selenium-tests.yml`

## Lab Structure

| Step | Topic |
|------|-------|
| 5 | Run Node.js server locally |
| 6 | Run unit tests locally (Mocha + Chai) |
| 7 | Set up Selenium integration test locally |
| 8 | Run Selenium test locally |
| 9 | Integrate both tests into GitHub Actions |

## Pre-requisites

- Git
- Node.js
- Docker Desktop (for Selenium server container)
- `github-actions-nodejs-test.zip` extracted to a local directory

## App Overview (`src/server.js`)

Express.js app on port 3000 with two routes:

- `GET /` — HTML page showing browser user-agent + server timestamp (fetched via JS)
- `GET /timestamp` — JSON `{ timestamp: "2024-12-27T09:38:09.150Z" }`

The exported `getCurrentTimestamp()` function is the unit-under-test.

## Step 6 — Unit Tests (Mocha + Chai)

Tests live in `tests/test.js`. Two test cases: valid ISO format, and within 1 second of now.

```bash
npx mocha tests/test.js
# or
npm test
```

Expected: `2 passing`

## Step 7 — Selenium Setup via Docker

```bash
# Start headless Chrome Selenium server
docker run -d -p 4444:4444 --name selenium-server --network host selenium/standalone-chrome

# Verify
curl http://localhost:4444/wd/hub/status
```

## Step 8 — Run Selenium Test Locally

With Node.js server running (`node src/server.js`):

```bash
node tests/SeleniumTest.mjs local
```

The test opens `http://localhost:3000`, waits for `#timestamp` element, extracts text, and validates ISO 8601 format with `assert.match()`.

## Step 9 — GitHub Actions Workflow

Place `selenium-tests.yml` at `.github/workflows/selenium-tests.yml`. Two-job pipeline:

```
build job → test job
  ↓                ↓
npm install     node:20 container
tar artifact    + selenium service sidecar
upload          download artifact
                npm test (unit)
                node server.js &
                node SeleniumTest.mjs github
```

### Critical workflow design points

- `test` job uses `container: image: node:20` with `options: --network-alias=testserver` so the Selenium container can reach the app as `http://testserver:3000`
- `services: selenium: image: selenium/standalone-chrome` is a sidecar available at `http://selenium:4444/wd/hub`
- `SeleniumTest.mjs` takes a CLI arg (`local` vs `github`) to switch between localhost and container network URLs
- Artifact hand-off: `tar -czvf www-build.tar.gz` → `upload-artifact` → `download-artifact` → `tar -xzvf`

## Testing Pyramid Context

| Layer | Tool | Scope |
|-------|------|-------|
| Unit | Mocha + Chai | `getCurrentTimestamp()` function in isolation |
| Integration/UI | Selenium + ChromeDriver | Full browser → server → DOM validation |
| CI trigger | GitHub Actions | Runs both on every push/PR to `main` |

## Related

- [[concepts/github-actions-cicd]] — workflow anatomy, jobs, services, artifacts
- [[concepts/software-testing-fundamentals]] — testing pyramid, unit vs integration vs E2E
- [[examples/ict2216-lab5-github-actions]] — Lab 5: GitHub Actions foundation
- [[examples/ict2216-lab6-owasp-dependency-check]] — Lab 6: dependency scanning in the same pipeline
