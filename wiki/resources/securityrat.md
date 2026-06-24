---
type: resource
status: established
title: "SecurityRAT"
category: tool
domain: secure-software-development
tags: [owasp, security-requirements, docker, asvs, automation]
created: 2026-05-11
---

# SecurityRAT

**SecurityRAT** (Security Requirement Automation Tool) is an OWASP project that automates the selection and tracking of security requirements during software development. Given a description of the artifact being built, it generates a tailored list of OWASP ASVS requirements and tracks their compliance status throughout the project.

- Homepage: `https://owasp.org/www-project-securityrat/`
- Demo and docs: `https://securityrat.github.io`
- Docker Compose repo: `https://github.com/SecurityRAT/SecurityRAT-dockercompose`

## Core Workflow

1. Declare the artifact type (web app, API, etc.), level (1–3), authentication model, and reachability
2. SecurityRAT generates the applicable ASVS requirement list
3. Mark each requirement as Fulfilled / Not Fulfilled / N/A with a comment
4. Export to an issue tracker (Jira, GitHub Issues) to create tickets for open items
5. Update compliance status as the project evolves

## ASVS Levels

| Level | Name | Meaning |
|-------|------|---------|
| 1 | Opportunistic | Minimum baseline — low-risk applications |
| 2 | Standard | Most applications — standard security hygiene |
| 3 | Advanced | High-value targets — financial, healthcare, critical infrastructure |

## Docker Setup (Windows)

### Prerequisites

- Docker Desktop installed and running
- Git

### Installation

```sh
# Clone the Docker Compose repo
git clone git@github.com:SecurityRAT/SecurityRAT-dockercompose.git
cd SecurityRAT-dockercompose

# Start all containers
docker-compose up --remove-orphans
```

### Load the Requirements Database (Step 4)

The container ships with a script `/var/dumpRequirements.sh` that imports the OWASP ASVS SQL dump into MariaDB. On Windows, the script has CRLF line endings that break execution inside the Linux container.

**Fix (run once after first `docker-compose up`):**

```powershell
# Strip CRLF inside the running container — must use PowerShell, not Git Bash
# (Git Bash translates /var/ to C:/Git/var/ which breaks the path)
docker exec securityrat-mariadb sed -i 's/\r$//' /var/dumpRequirements.sh

# Then run the script
docker exec securityrat-mariadb sh -c '/var/dumpRequirements.sh'
```

> See [[docker-windows-crlf]] for a full explanation of why this happens and how to diagnose it.

### Access

- URL: `http://localhost:9002`
- Default credentials: `admin` / `admin` or `user` / `user`

### Teardown

```sh
docker-compose down
```

## Container Architecture

| Container | Image | Role |
|-----------|-------|------|
| `securityrat-mariadb` | `securityrat-mariadb:10.7.3` | MariaDB database; holds all requirement data |
| `securityrat` | `securityrat/securityrat:v1.8.5` | Spring Boot application; serves the UI on port 9000 (mapped to 9002) |

The app waits 10 seconds (`JHIPSTER_SLEEP=10`) before connecting to the DB to allow MariaDB to initialise.

## Related

- [[secure-software-requirements]] — the CIA + AAA framework SecurityRAT helps implement
- [[docker-windows-crlf]] — the CRLF fix required on Windows hosts
- [[ICT2216-secure-software-development]] — course that introduced this tool
