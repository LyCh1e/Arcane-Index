---
type: concept
title: "Docker and Docker Compose"
domain: devops
complexity: medium
tags: [docker, docker-compose, containers, nginx, mysql, git, selenium, networking, volumes]
created: 2026-05-11
status: established
---

# Docker and Docker Compose

Docker packages applications into isolated **containers** — lightweight, portable environments that include everything needed to run: code, runtime, libraries, and configuration. Docker Compose extends this to **multi-container applications**, defining all services in a single YAML file and managing their lifecycle together.

---

## Compose File Structure

The compose file is named `compose.yaml` (preferred) or `compose.yml`. The older `docker-compose.yaml` / `docker-compose.yml` naming is still supported.

### Top-Level Elements

| Element | Description |
|---------|-------------|
| `services` | The core — defines each container: image, ports, volumes, environment, build |
| `networks` | How services communicate; Docker creates a default `<project>_default` bridge network automatically |
| `volumes` | Named volumes for persistent data shared between host and container |
| `configs` | Config files granted to specific services |
| `secrets` | Sensitive data (passwords, keys) injected into services |

The `version` top-level element is deprecated in current Compose Specification.

### Minimal Example

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"        # host:container
    volumes:
      - ./html:/usr/share/nginx/html
    environment:
      ENV_VAR: value
```

---

## Key Networking Concepts

### Default Network

Docker Compose automatically creates a bridge network named `<project_name>_default`. Every service in the file joins it and can reach every other service by **service name** as hostname.

```yaml
# 'app' can reach 'db' at hostname 'db' — no explicit network config needed
services:
  app:
    image: myapp
  db:
    image: mysql:8.0
```

### Custom Networks

Define explicit networks for finer control:

```yaml
services:
  app:
    image: myapp
    networks:
      - my_network
networks:
  my_network:
    driver: bridge   # bridge | host | none
```

| Driver | Behaviour |
|--------|-----------|
| `bridge` | Default; isolated network on the host |
| `host` | Removes isolation; container shares host network stack |
| `none` | No networking |

### Aliases

Assign a custom hostname to a service within a specific network:

```yaml
services:
  db:
    networks:
      my_network:
        aliases:
          - database
```

---

## Essential Commands

```sh
docker-compose up               # Start all services (foreground)
docker-compose up -d            # Start detached (background)
docker-compose up --build       # Rebuild images before starting
docker-compose stop             # Stop containers (preserve state)
docker-compose down             # Stop and remove containers
docker-compose down -v          # Also remove named volumes
docker ps -all                  # List all containers (running and stopped)
docker exec -it <id> /bin/sh    # Open an interactive shell in a running container
```

---

## Services Covered in Lab 1

### Nginx Web Server

```yaml
nginxwebsvr:
  image: nginx:alpine
  container_name: nginxwebsvr
  ports:
    - "80:80"
```

Access at `http://localhost/`. No configuration needed for the default welcome page.

### MySQL Database

```yaml
mysqldb:
  image: mysql:8.0
  restart: always
  volumes:
    - ./mysql_data:/var/lib/mysql    # persist DB files on host
  environment:
    MYSQL_ROOT_PASSWORD: pass
    MYSQL_DATABASE: testdb
    MYSQL_USER: user
    MYSQL_PASSWORD: pass
```

Shell into the container to verify: `docker exec -it <id> /bin/sh`, then `cd /usr/bin && ./mysql -u root -p`.

The `restart: always` policy restarts the container automatically on failure or Docker daemon restart.

### Git HTTP Server (No Auth)

Built from a custom Dockerfile (`gitserver.Dockerfile`):

```dockerfile
FROM node:alpine
RUN apk add --no-cache tini git \
    && yarn global add git-http-server \
    && adduser -D -g git git
USER git
WORKDIR /home/git
RUN git init --bare repository.git
ENTRYPOINT ["tini", "--", "git-http-server", "-p", "3000", "/home/git"]
```

```yaml
git-server:
  build:
    dockerfile: gitserver.Dockerfile
    context: .
  restart: always
  ports:
    - "3000:3000"
  volumes:
    - ./repos:/var/www/git
```

Test with: `git clone http://localhost:3000/repository.git`

> No authentication — suitable only for local lab environments. For production, use SSH keys or a full SCM tool (GitLab, Gitea).

### Selenium Grid

```yaml
selenium-hub:
  image: selenium/hub:4.14.1
  ports:
    - "4444:4444"

chrome-node:
  image: selenium/node-chrome:4.14.1
  depends_on:
    - selenium-hub
  environment:
    SE_EVENT_BUS_HOST: selenium-hub
    SE_EVENT_BUS_PUBLISH_PORT: 4442
    SE_EVENT_BUS_SUBSCRIBE_PORT: 4443
  volumes:
    - /dev/shm:/dev/shm    # shared memory for browser stability

firefox-node:
  image: selenium/node-firefox:4.14.1
  # same pattern as chrome-node
```

Hub UI at `http://localhost:4444`. Browser nodes register with the hub via the event bus ports (4442/4443). `/dev/shm` is mounted to prevent Chrome/Firefox from running out of shared memory inside the container.

---

## Volumes — Persistence Pattern

```yaml
volumes:
  - ./mysql_data:/var/lib/mysql   # bind mount: host path : container path
```

A **bind mount** maps a specific host directory into the container. Data written by the container persists on the host. Without this, container data is lost on `docker-compose down`.

---

## Related

- [[securityrat]] — a more complex Docker Compose stack (Spring Boot + MariaDB); introduces the CRLF gotcha
- [[docker-windows-crlf]] — Windows-specific pitfall when shell scripts are copied into Linux containers
- [[ICT2216-secure-software-development]] — source course
