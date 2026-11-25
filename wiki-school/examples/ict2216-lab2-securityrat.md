---
type: lab
status: established
title: "ICT2216 Lab 2 — SecurityRAT: Defining Secure Software Requirements"
course: ICT2216
tags: [lab, ict2216, docker, securityrat, owasp, asvs, security-requirements, mariadb]
created: 2026-05-11
---

# ICT2216 Lab 2 — SecurityRAT: Defining Secure Software Requirements

Two-part lab: (1) Team discussion to define security requirements using the CIA+AAA framework; (2) Deploying OWASP SecurityRAT to auto-generate an ASVS-based checklist for a declared software artifact.

Parent concepts: [[secure-software-requirements]], [[securityrat]], [[docker-compose]]

---

## Part 1 — Team Security Requirements Discussion

Work through each security pillar as a team. For each, answer the three sub-questions.

### Functional Requirements (2–3 only)
The core features your application must perform.

### Non-Functional Requirements (2–3 only)
Quality attributes: performance, scalability, maintainability, etc.

### Security Requirements (CIA + AAA)

Reference: SANS SWAT Checklist — https://www.sans.org/cloud-security/swat/

#### Confidentiality
1. What data must be protected? (passwords, PII, payment data)
2. What are the confidentiality risks? (data leakage, unencrypted storage)
3. What requirements protect it? (encrypt at rest and in transit, mask PII in logs)

#### Integrity
1. What data must maintain integrity? (transaction records, user roles)
2. What are the integrity risks? (SQL injection, parameter tampering)
3. What requirements ensure integrity? (input validation, parameterised queries)

#### Availability
1. How will you ensure availability? (redundancy, load balancing)
2. What are the availability risks? (DDoS, server crashes)
3. What are your availability requirements? (uptime SLA, failover)

#### Authentication
1. Who are the users? (admin, regular user, guest)
2. What are the authentication risks? (brute force, credential stuffing)
3. What will you implement? (MFA, account lockout after N attempts)

#### Authorization
1. Are there different user types with different permissions?
2. What are the authorization risks? (privilege escalation, IDOR)
3. What permission model will you use? (RBAC, least privilege)

#### Accountability
1. What actions need to be logged? (login events, data changes, admin actions)
2. What are the accountability risks? (log tampering, no audit trail)
3. What logging requirements will you define? (immutable logs, all admin actions)

---

## Part 2 — OWASP SecurityRAT

## Repository

```sh
git clone git@github.com:SecurityRAT/SecurityRAT-dockercompose.git
cd SecurityRAT-dockercompose
```

---

## docker-compose.yml

```yaml
version: '3'
services:
  mariadb-service:
    container_name: securityrat-mariadb
    build:
      context: ./mariadb
    image: securityrat-mariadb:10.7.3
    environment:
      MYSQL_DATABASE: 'securityrat'
      MYSQL_ROOT_PASSWORD: 'changeit'
      MYSQL_USER: 'securityrat'
      MYSQL_PASSWORD: 'password'
    command: mysqld --skip-ssl

  securityrat:
    container_name: securityrat
    image: securityrat/securityrat:v1.8.5
    platform: linux/amd64
    privileged: true
    shm_size: '256m'
    tmpfs:
      - /tmp:exec
    environment:
      - SPRING_DATASOURCE_URL=jdbc:mysql://mariadb-service:3306/securityrat?useUnicode=true&characterEncoding=utf8&useSSL=false&useLegacyDatetimeCode=false&serverTimezone=UTC&createDatabaseIfNotExist=true
      - SPRING_DATASOURCE_USERNAME=securityrat
      - SPRING_DATASOURCE_PASSWORD=password
      - JHIPSTER_SLEEP=10
    ports:
      - 9002:9000
```

## mariadb/Dockerfile

```dockerfile
FROM mariadb:10.7.3

ADD https://raw.githubusercontent.com/SecurityRAT/Security-Requirements/master/owasp_asvs_3_0_1.sql /var/requirements.sql

COPY dumpRequirements.sh /var/
```

## mariadb/dumpRequirements.sh

```sh
#!/bin/sh
mysql -u root -p"$MYSQL_ROOT_PASSWORD" securityrat < /var/requirements.sql
```

---

## Step-by-Step

### Step 1 — Install Docker Desktop

See [[docker-compose]] for installation instructions (Windows: WSL2 + Docker Desktop).

### Step 2 — Clone the repo

```sh
git clone git@github.com:SecurityRAT/SecurityRAT-dockercompose.git
```

### Step 3 — Start the containers

```sh
docker-compose up --remove-orphans
```

Wait for MariaDB and the Spring Boot app to fully start (the app sleeps 10 s waiting for the DB).

### Step 4 — Load the requirements database (CRLF fix required on Windows)

The script `dumpRequirements.sh` is copied into the Linux container with Windows CRLF line endings, breaking the shebang. Fix and run using **PowerShell** (not Git Bash — Git Bash translates `/var/` to `C:/Git/var/`):

```powershell
# Strip CRLF inside the container
docker exec securityrat-mariadb sed -i 's/\r$//' /var/dumpRequirements.sh

# Run the script to import the ASVS SQL dump
docker exec securityrat-mariadb sh -c '/var/dumpRequirements.sh'
```

Verify the data loaded:

```powershell
docker exec securityrat-mariadb mysql -u root -pchangeit securityrat -e "SHOW TABLES;"
# Should list ~39 tables including REQUIREMENTSKELETON, PROJECTTYPE, STATUSCOLUMN, etc.
```

### Step 5 — Access the UI

Open `http://localhost:9002` in a browser.

### Step 6 — Log in

| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin` | Administrator |
| `user` | `user` | Standard user |

### Step 7 — Create an Artifact and Generate Requirements

1. Click **New Artifact** (or the browse icon)
2. Fill in **Artifact Settings**:
   - Name: your project name
   - Level: 1 (Opportunistic) / 2 (Standard) / 3 (Advanced)
   - Artifact Type: Web Application, API, etc.
   - Authentication: select the model your app uses
   - Session management and Reachability as appropriate
   - Implementation Type: Default
3. Click **Generate**
4. Review the generated ASVS requirement list — each row shows:
   - Properties tags (e.g. Single Sign-On, Firewall, Web Service)
   - ASVS ID (e.g. `ASVS_3.0.1_1.1`)
   - Short name and description
   - Fulfilled status (Unknown / Yes / No / N/A)
   - Comment field

### Step 8 — Clean Up

```sh
docker-compose down
```

---

## Container Architecture

| Container | Image | Role | Port |
|-----------|-------|------|------|
| `securityrat-mariadb` | `securityrat-mariadb:10.7.3` (custom build) | MariaDB database holding all ASVS requirement data | internal only |
| `securityrat` | `securityrat/securityrat:v1.8.5` | Spring Boot app; serves the SecurityRAT UI | 9002 → 9000 |

---

## Key Gotchas

| Issue | Cause | Fix |
|-------|-------|-----|
| `dumpRequirements.sh: not found` | CRLF shebang in Linux container | `docker exec ... sed -i 's/\r$//'` via PowerShell |
| `sed: can't read C:/Git/var/...` | Git Bash path translation | Use PowerShell instead of Git Bash |
| App can't connect to DB | MariaDB not ready yet | Wait longer; `JHIPSTER_SLEEP=10` may not be enough on slow machines — re-run `docker-compose up` |

See [[docker-windows-crlf]] for a full explanation of the CRLF issue.
