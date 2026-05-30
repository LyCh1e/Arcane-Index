---
name: nginx-reverse-proxy-and-tls
description: Nginx as a reverse proxy — configuration, Docker deployment, Let's Encrypt TLS/SSL termination with Certbot, and auto-renewal
metadata:
  type: concept
domain: devops
complexity: medium
created: 2026-05-30
tags: [nginx, reverse-proxy, tls, ssl, lets-encrypt, certbot, docker]
---

# Nginx as a Reverse Proxy with TLS

## What is a Reverse Proxy?

A reverse proxy sits in front of your application servers and forwards client requests to the appropriate backend. It handles:

- **TLS/SSL termination** — decrypts HTTPS at the proxy; backend talks plain HTTP internally
- **Static file serving** — serves HTML/CSS/JS directly without hitting the app
- **Load balancing** — distributes requests across multiple backend instances
- **Security filtering** — rate limiting, header rewriting, access control

## Nginx Docker Setup (HTTP)

Minimal `docker-compose.yml` to serve a static page:

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

Corresponding `nginx.conf`:

```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name yourdomain.com www.yourdomain.com;

        default_type text/html;

        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

Start and test:

```bash
docker compose -f nginx-compose.yml up -d
curl http://localhost/
```

## Let's Encrypt TLS with Certbot

Let's Encrypt is a free CA. Certbot is the ACME client that automates cert issuance.

### Two Domain Verification Methods

| Method | How it works | When to use |
|--------|-------------|-------------|
| **ACME (HTTP-01)** | Let's Encrypt GETs a token from `/.well-known/acme-challenge/<TOKEN>` on port 80 | You control the web server |
| **DNS-01** | You add a TXT record to your domain's DNS | No public port 80 access |

### Docker Compose with Certbot (ACME)

```yaml
services:
  nginx:
    image: nginx:latest
    ports:
      - "80:80"   # Required for certbot HTTP challenge
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certbot/www:/var/www/certbot      # Challenge files
      - ./certbot/conf:/etc/letsencrypt     # Issued certs
      - ./index.html:/var/www/html/index.html

  certbot:
    image: certbot/certbot
    volumes:
      - ./certbot/www:/var/www/certbot
      - ./certbot/conf:/etc/letsencrypt
    entrypoint: sh -c "certbot certonly --webroot -w /var/www/certbot
      --email your@email.com --agree-tos --no-eff-email
      --rsa-key-size 4096 --expand --force-renewal
      -d yourdomain.com -d www.yourdomain.com && nginx -s reload"
```

### DNS Challenge (when no public port 80)

```bash
sudo certbot certonly --manual --preferred-challenges dns \
  -d yourdomain.com -d www.yourdomain.com \
  --agree-tos -m your@email.com --no-eff-email
```

Certbot will print a TXT record value to add to your DNS. After adding it, press Enter to proceed.

### nginx.conf for HTTPS (nginx-tls.conf)

```nginx
http {
    # HTTP server — redirect + ACME challenge
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

    # HTTPS server — TLS termination
    server {
        listen 443 ssl;
        server_name yourdomain.com www.yourdomain.com;

        ssl_certificate     /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

        default_type text/html;

        # Serve static files
        location / {
            root /var/www/html;
            index index.html;
        }

        # OR reverse-proxy to app:
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

Switch to TLS config and redeploy:

```bash
cp nginx-compose-tls.yml nginx-proxy/nginx-compose.yml
cp nginx-tls.conf nginx-proxy/nginx.conf
docker compose -f nginx-compose.yml up -d
curl https://yourdomain.com/
```

## Auto-Renewal (Cron)

Let's Encrypt certs expire every **90 days**. Add a cron job on the server:

```bash
crontab -e
# Add:
0 3 * * * docker compose -f certbot-compose.yml run --rm certbot renew && docker compose restart nginx
```

This runs the renewal check daily at 03:00; certbot only actually renews if the cert is within 30 days of expiry.

## Key Points

- Certbot must use `certonly` mode — it obtains the cert but does not install it; Nginx config must reference the cert paths manually.
- `ssl_certificate` points to `fullchain.pem` (your cert + intermediate CA chain); `ssl_certificate_key` points to `privkey.pem`.
- The `certbot/www` volume must be served by Nginx at `/.well-known/acme-challenge/` for ACME validation to work.
- Let's Encrypt **cannot** issue certs for `localhost` — a real publicly reachable domain is required.

## Related

- [[concepts/docker-compose]] — compose file fundamentals, networking, volumes
- [[concepts/web-security-and-devops]] — TLS/HTTPS, CA chain, HSTS
- [[examples/ict2216-lab5-github-actions]] — full Lab 5 walkthrough
