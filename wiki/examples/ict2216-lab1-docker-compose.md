---
type: lab
title: "ICT2216 Lab 1 — Multi-Container Stack with Docker Compose"
course: ICT2216
tags: [lab, ict2216, docker, docker-compose, nginx, mysql, git, selenium]
created: 2026-05-11
---

# ICT2216 Lab 1 — Multi-Container Stack with Docker Compose

Hands-on lab building a four-service Docker Compose application: Nginx web server, MySQL database, a bare Git HTTP server, and a Selenium Grid for browser testing. The final `compose.yaml` wires all services together; a separate `compose-selenium.yaml` handles the Selenium stack.

Parent concept: [[docker-compose]]

---

## Final compose.yaml

```yaml
services:
  nginxwebsvr:
    image: nginx:alpine
    container_name: nginxwebsvr
    ports:
      - "80:80"

  mysqldb:
    image: mysql:8.0
    restart: always
    volumes:
      - ./mysql_data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: pass
      MYSQL_DATABASE: testdb
      MYSQL_USER: user
      MYSQL_PASSWORD: pass

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

## compose-selenium.yaml

```yaml
services:
  selenium-hub:
    image: selenium/hub:4.14.1
    container_name: selenium-hub
    ports:
      - "4444:4444"
    environment:
      GRID_TIMEOUT: 30000
      GRID_BROWSER_TIMEOUT: 30000

  chrome-node:
    image: selenium/node-chrome:4.14.1
    container_name: chrome-node
    depends_on:
      - selenium-hub
    environment:
      SE_EVENT_BUS_HOST: selenium-hub
      SE_EVENT_BUS_PUBLISH_PORT: 4442
      SE_EVENT_BUS_SUBSCRIBE_PORT: 4443
    volumes:
      - /dev/shm:/dev/shm

  firefox-node:
    image: selenium/node-firefox:4.14.1
    container_name: firefox-node
    depends_on:
      - selenium-hub
    environment:
      SE_EVENT_BUS_HOST: selenium-hub
      SE_EVENT_BUS_PUBLISH_PORT: 4442
      SE_EVENT_BUS_SUBSCRIBE_PORT: 4443
    volumes:
      - /dev/shm:/dev/shm
```

## gitserver.Dockerfile

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

---

## Step-by-Step Build Order

### Section 1 — Nginx

```sh
# compose.yaml with only nginxwebsvr defined
docker-compose up
# verify at http://localhost/
docker ps -all
```

### Section 2 — Add MySQL

```sh
mkdir ./mysql_data
# add mysqldb service to compose.yaml
docker-compose up
docker ps -all
docker exec -it <mysqldb-cntr-id> /bin/sh
# inside container:
cd /usr/bin && ./mysql -u root -p
# password: pass
```

### Section 3 — Add Git Server

```sh
mkdir ./repos
# create gitserver.Dockerfile
# add git-server service to compose.yaml
docker-compose build
docker-compose up -d
git clone http://localhost:3000/repository.git
```

### Section 4 — Selenium Grid (separate file)

```sh
docker-compose -f compose-selenium.yaml up -d
# hub UI: http://localhost:4444
```

---

## Service Port Map

| Service | Host Port | Container Port | URL |
|---------|-----------|---------------|-----|
| Nginx | 80 | 80 | `http://localhost/` |
| MySQL | (none exposed) | 3306 | internal only |
| Git HTTP | 3000 | 3000 | `http://localhost:3000/repository.git` |
| Selenium Hub | 4444 | 4444 | `http://localhost:4444` |

---

## Notes

- MySQL port is not exposed to the host in this config — only accessible to other services within the Compose network (by hostname `mysqldb`)
- The git server runs with **no authentication** — acceptable for a local lab, not for any networked environment
- `/dev/shm` is mounted for Selenium browser nodes to prevent shared-memory exhaustion inside the container
- `restart: always` on MySQL and git-server means they survive Docker daemon restarts automatically
