---
name: ict2216-lab5-github-actions
description: ICT2216 Lab 5 — Nginx reverse proxy with Docker, Let's Encrypt TLS via Certbot, and GitHub Actions CI/CD pipeline
metadata:
  type: example
domain: devops
course: ICT2216
created: 2026-05-30
tags: [nginx, docker, lets-encrypt, certbot, github-actions, ci-cd, tls, lab]
---

# ICT2216 Lab 5 — Web Proxy and GitHub Actions with Docker

**Lab file:** `Lab5/X05-Github-Actions.pdf`

## Lab Structure

| Step | Topic | Status |
|------|-------|--------|
| 4.1 | Nginx web server via Docker | Done locally |
| 4.2 | Configure Nginx as reverse proxy | Done locally |
| 4.3 | Let's Encrypt TLS with Certbot | Config ready; cert needs real domain + public port 80 |
| 4.4 | Nginx listens on HTTPS (443) | Config ready |
| 4.5 | Modify nginx-tls.conf, redeploy | Config ready |
| 4.6 | Auto-renewal cron job (optional) | See below |
| 5 | GitHub Actions CI/CD workflow | Repo created; push triggers Actions |

## Directory Structure Created

```
Lab5/
├── nginx-proxy/                      # Local Docker setup
│   ├── nginx-compose.yml             # HTTP compose (Step 4.1)
│   ├── nginx-compose-tls.yml         # HTTPS + certbot compose (Step 4.3)
│   ├── nginx.conf                    # HTTP config (server_name localhost)
│   ├── nginx-tls.conf                # HTTPS config with Let's Encrypt paths
│   ├── index.html                    # Hello World page
│   └── certbot/
│       ├── www/                      # ACME challenge files (served by nginx)
│       └── conf/                     # Issued certs (mounted by both services)
└── lab5-cicd/                        # Standalone git repo for GitHub Actions
    ├── index.html
    └── .github/
        └── workflows/
            └── test-nginx.yml
```

## Step 4.1 — Nginx Web Server via Docker

```bash
mkdir -p ./nginx-proxy && cd ./nginx-proxy
# Copy provided files: nginx-compose.yml, index.html, nginx.conf
docker compose -f nginx-compose.yml up -d
curl http://localhost/
```

**nginx-compose.yml:**
```yaml
services:
  nginx:
    image: nginx:latest
    container_name: nginx-proxy
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./index.html:/var/www/html/index.html
    networks:
      lab-webproxy:
        ipv4_address: 10.11.0.6

networks:
  lab-webproxy:
    driver: bridge
    ipam:
      config:
        - subnet: 10.11.0.0/16
          gateway: 10.11.0.1
```

## Step 4.2 — Configure Nginx as Reverse Proxy

**nginx.conf** (update `server_name` to your domain or `localhost`):

```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name localhost;   # replace with yourdomain.com on team VM

        default_type text/html;

        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

Test: `curl http://localhost/` returns the HTML of `index.html`.

## Step 4.3 — Let's Encrypt TLS with Certbot

**Prerequisites:**
- A real domain pointing to the server's public IP
- Port 80 publicly reachable (for ACME HTTP-01 challenge)
- OR DNS access (for DNS-01 challenge)

**nginx-compose-tls.yml** (adds certbot service):

```yaml
services:
  nginx:
    image: nginx:latest
    container_name: nginx-proxy
    restart: unless-stopped
    ports:
      - "80:80"    # For ACME challenge
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certbot/www:/var/www/certbot
      - ./certbot/conf:/etc/letsencrypt
      - ./index.html:/var/www/html/index.html
    networks:
      lab-webproxy:
        ipv4_address: 10.11.0.6

  certbot:
    image: certbot/certbot
    container_name: certbot
    volumes:
      - ./certbot/www:/var/www/certbot
      - ./certbot/conf:/etc/letsencrypt
    networks:
      lab-webproxy:
        ipv4_address: 10.11.0.7
    entrypoint: sh -c "certbot certonly --webroot -w /var/www/certbot
      --email your@email.com --agree-tos --no-eff-email
      --rsa-key-size 4096 --expand --force-renewal
      -d yourdomain.com -d www.yourdomain.com && nginx -s reload"
```

**DNS challenge alternative** (no public port 80 needed):

```bash
sudo certbot certonly --manual --preferred-challenges dns \
  -d yourdomain.com -d www.yourdomain.com \
  --agree-tos -m your@email.com --no-eff-email
# Certbot prints a TXT record value → add to DNS → press Enter
```

## Step 4.4 — Nginx Listens on HTTPS (443)

The `nginx-compose-tls.yml` already exposes port `443:443`. The nginx config (Step 4.5) adds the `listen 443 ssl` server block.

## Step 4.5 — Modify nginx-tls.conf and Redeploy

**nginx-tls.conf:**

```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    # HTTP server: ACME challenge + redirect to HTTPS
    server {
        listen 80;
        server_name yourdomain.com www.yourdomain.com;

        location /.well-known/acme-challenge/ {
            root /var/www/certbot;
        }

        location / {
            return 301 https://$host$request_uri;
        }
    }

    # HTTPS server: TLS termination
    server {
        listen 443 ssl;
        server_name yourdomain.com www.yourdomain.com;

        default_type text/html;

        ssl_certificate     /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

        # Serve static files
        location / {
            root /var/www/html;
            index index.html;
        }

        # OR reverse-proxy to app container:
        #location / {
        #    proxy_pass http://your-app-container:3000;
        #    proxy_set_header Host $host;
        #    proxy_set_header X-Real-IP $remote_addr;
        #    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        #    proxy_set_header X-Forwarded-Proto $scheme;
        #}
    }
}
```

Deploy TLS config:

```bash
cp nginx-compose-tls.yml nginx-proxy/nginx-compose.yml
cp nginx-tls.conf nginx-proxy/nginx.conf
docker compose -f nginx-compose.yml up -d
curl https://yourdomain.com/
```

## Step 4.6 — Auto-Renewal Cron (Optional)

Let's Encrypt certs expire every 90 days. On the server:

```bash
crontab -e
# Add:
0 3 * * * docker compose -f certbot-compose.yml run --rm certbot renew && docker compose restart nginx
```

Certbot only renews if the cert is within 30 days of expiry, so daily checks are safe.

## Step 5 — GitHub Actions CI/CD

### Repo Structure for GitHub Actions

```
lab5-cicd/
├── index.html                          # Must be at repo root
└── .github/
    └── workflows/
        └── test-nginx.yml              # CI workflow
```

### test-nginx.yml

```yaml
name: Test Nginx Hello World Page

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  test-nginx:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Start Nginx with Docker
        run: |
          docker run -d --name test-nginx -p 8080:80 \
            -v ${{ github.workspace }}/index.html:/usr/share/nginx/html/index.html:ro \
            nginx:latest

      - name: Wait for Nginx to start
        run: sleep 5

      - name: Test Hello World Page
        run: |
          curl -s -o response.html http://localhost:8080/index.html
          grep "Hello World" response.html

      - name: Stop Nginx container
        run: docker stop test-nginx
```

### What the Workflow Does

1. **Trigger** — Fires on every push to `main` and on any pull request
2. **Checkout** — Clones repo into `/home/runner/work/<repo>/` on the runner
3. **Start Nginx** — Runs Nginx in Docker, mounts `index.html` from the workspace
4. **Wait** — Gives Nginx 5 s to start up
5. **Test** — `curl` fetches the page; `grep` asserts "Hello World" is in the response
6. **Stop** — Cleans up the container

If `grep` finds nothing, it exits non-zero → workflow fails → GitHub marks the commit as failed.

### Push to GitHub

```bash
cd lab5-cicd
git init
git add .
git commit -m "Lab 5: Nginx hello-world + GitHub Actions CI workflow"
git branch -M main
# Create repo on GitHub, then:
git remote add origin https://github.com/<username>/ict2216-lab5-github-actions.git
git push -u origin main
```

After push, go to **Actions** tab on the GitHub repo to see the workflow run.

## Key Gotchas

- **index.html must be at repo root** — the workflow mounts `${{ github.workspace }}/index.html`; if it's in a subdirectory the mount fails silently and Nginx serves its own default page, causing `grep` to fail.
- **`sleep 5` is fragile** — on slow runners, Nginx may not be ready. A retry loop is more robust: `until curl -s http://localhost:8080/ > /dev/null; do sleep 1; done`.
- **Let's Encrypt ≠ localhost** — Let's Encrypt cannot issue certs for `localhost` or private IPs. Use a self-signed cert for local testing, and the real cert only on the team VM with a public domain.
- **Certbot `certonly` mode** — Certbot only retrieves the cert; it does NOT edit nginx.conf. You must reference the cert paths manually in nginx-tls.conf.
- **CRLF on Windows** — If editing any nginx config or shell script on Windows, ensure LF line endings (use `.gitattributes` or `dos2unix`) before deploying to a Linux container.

## Related

- [[concepts/nginx-reverse-proxy-and-tls]] — Nginx config reference
- [[concepts/github-actions-cicd]] — Full workflow YAML syntax and pipeline design
- [[concepts/docker-compose]] — Compose networking and volumes
- [[learning/docker-windows-crlf]] — CRLF gotcha for Windows users
