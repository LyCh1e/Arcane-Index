---
type: source
status: ingested
title: "ICT3113 POD — Lec 11–12: Learning Kubernetes and Docker Fundamentals (Dell Industry Session)"
source_type: lecture-slides
domain: performance-engineering
date_ingested: 2026-10-28
tags: [ict3113, docker, kubernetes, cloud-native, microservices, containers, devops, performance-engineering]
related:
  - "[[concepts/cloud-native]]"
  - "[[concepts/kubernetes]]"
  - "[[concepts/docker-compose]]"
---

# ICT3113 POD — Lec 11–12: Learning Kubernetes and Docker Fundamentals

**Source type:** Lecture slides (industry session — Dell Technologies)  
**Module:** ICT3113 Performance Optimisation and Design, Weeks 11–12  
**Presenter:** Dell Technologies AI Innovation Hub team member (20+ years IT practitioner; background in DevOps, Cloud Native, Pre/Post-Sales)

---

## Summary

An industry-practitioner introduction to Cloud Native computing, Docker containers, and Kubernetes. The session moves logically through four escalating problems:

1. **Monoliths are rigid** → decompose into microservices
2. **Microservices create dependency sprawl** → package each service in a container
3. **Container sprawl is unmanageable** → orchestrate with Kubernetes
4. **Distributed systems are hard** → Kubernetes abstracts infrastructure and automates recovery

The session provides the conceptual vocabulary (Cloud Native traits, CNCF definition, container anatomy, Pod/Deployment/Reconcile Loop) rather than hands-on YAML authoring — that is covered in the Dell self-paced courses linked from the slides.

---

## Key Concepts Covered

### Cloud Native vs Cloud Computing

| Dimension | Cloud Native | Cloud Computing |
|-----------|-------------|-----------------|
| Question answered | **How?** (architecture) | **Where?** (infrastructure) |
| Focus | Containers, microservices, service meshes, immutable infrastructure, declarative APIs | Resource pooling, on-demand self-service, rapid elasticity, pay-as-you-go |
| Examples | CNCF ecosystem | GCP, AWS, Azure |

> Cloud Native Development is an approach to building and running applications that **exploits** the advantages of the Cloud Computing delivery model.

### Cloud Native Traits (CNCF)

From the official CNCF definition — five traits, five elements.

**Traits (the "why"):** Scalability · Loose Coupling · Resilience · Manageability · Observability  
**Elements (the "how"):** Containers · Service Meshes · Microservices · Immutable Infrastructure · Declarative APIs

→ Full treatment: [[concepts/cloud-native]]

### Monolith → Microservices Transition

| Monolith | Microservices |
|---------|--------------|
| Single deployable unit | Each function independently deployable |
| Tightly coupled | Loosely coupled, independent |
| Shared database | Per-service database |
| Hard to scale partial features | Scale individual services |
| Technology lock-in | Polyglot stack possible |
| Low fault tolerance | Failure of one service does not cascade |

**The new problem microservices introduce:** complex service-to-service dependency graphs ("distributed monolith" risk) → solved with containers + service mesh + orchestration.

### Containers

- Package **app + language runtime + libraries + config** as one portable unit
- Standardised unit for development, deployment, and distribution
- Abstracts applications from the host environment
- Docker (launched 2013) created the industry standard — "Build once, run anywhere"

**Container vs VM comparison:**

| VM stack | Container stack |
|---------|----------------|
| App per Guest OS | All apps share one host OS |
| Separate Guest OS per app | Container runtime replaces Guest OS |
| Full OS overhead | Lightweight — shares kernel |
| Better isolation | Better density |

Containers and VMs are **complementary**: containers can run inside VMs. This is the common production configuration.

### Kubernetes Fundamentals

- Container orchestration platform; environment for running distributed apps on containers **at scale**
- Originally developed by Google; open-sourced 2014; CNCF flagship project
- Etymology: κυβερνήτης — Greek for "helmsman"; the 8 in **k8s** represents the eight elided letters
- Defines a common set of resources and a declarative API for manipulating them

**Key goals:**  
1. Distribute containers logically and efficiently → **Maximise capacity**  
2. Scale up/down fast → **Adapt to demand**  
3. Keep processes continuously running → **Don't go dark**

**Core resource types introduced:**

| Resource | Description |
|----------|-------------|
| **Pod** | Smallest deployable unit; groups ≥1 containers; unique cluster IP |
| **Deployment** | Manages Pods via ReplicaSet; handles replicas, rolling updates, self-healing |
| **Reconcile Loop** | Non-terminating control loop — kube-controller-manager continuously reconciles desired state = actual state |

**Self-healing sequence:** Pod fails → kube-controller-manager detects mismatch (actual ≠ desired) → new Pod created → failed Pod cleaned up.

**Horizontal scaling:** update `replicas` on the Deployment (e.g., `Replicas = 3`) → Kubernetes fans out to three independent Pods.

→ Deep technical reference: [[concepts/kubernetes]]

### 8 Fallacies of Distributed Systems

Classic list; every distributed system designer must internalise these:

1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

*Source cited in slides: https://architecturenotes.co/fallacies-of-distributed-systems*

---

## Container Orchestration Capabilities (Kubernetes)

- Service discovery and load balancing
- Storage orchestration
- Automated rollouts and rollbacks
- Auto-scaling
- Self-healing
- Secret and configuration management

---

## Design Considerations for Distributed Apps (summary)

- An app should not be tied to a specific host or network
- The end user should not be affected by a hardware or software failure
- An app should remain accessible as workload increases
- No downtime when rolling out new updates

---

## Linked Concept Pages

- [[concepts/cloud-native]] — Cloud Native definition, traits, elements, and patterns
- [[concepts/kubernetes]] — Deep technical reference: architecture, objects, operations, security
- [[concepts/docker-compose]] — Single-host Docker; dev/CI complement to Kubernetes
