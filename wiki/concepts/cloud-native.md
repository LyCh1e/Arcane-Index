---
type: concept
status: established
address: c-000082
created: 2026-10-28
updated: 2026-10-28
tags: [cloud-native, cncf, microservices, containers, devops, distributed-systems, architecture]
related:
  - "[[concepts/kubernetes]]"
  - "[[concepts/docker-compose]]"
  - "[[concepts/software-architecture-patterns]]"
  - "[[sources/ict3113-pod-lec11-12-kubernetes-docker]]"
---

# Cloud Native

Cloud Native is an **architectural and engineering approach** to building and running applications that fully exploits the advantages of cloud computing infrastructure. It is the *how* of modern application design — distinct from Cloud Computing, which is the *where*.

> Cloud native technologies empower organisations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach. These techniques enable loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil.
>
> — Cloud Native Computing Foundation (CNCF), official definition

---

## Cloud Native vs Cloud Computing

| Dimension | Cloud Native | Cloud Computing |
|-----------|-------------|-----------------|
| Central question | **How** do you build and run the app? | **Where** does the app run? |
| Concerns | Architecture, application design, service topology | Resource pooling, on-demand self-service, rapid elasticity, pay-as-you-go, measured service |
| Governing body | Cloud Native Computing Foundation (CNCF) | Hyperscalers (AWS, GCP, Azure) |
| Key artefacts | Containers, microservices, service meshes, declarative manifests | Virtual machines, managed databases, object storage, CDNs |

**Summary:** Cloud Native describes *how* you design the software; Cloud Computing describes *where* you deploy it. A Cloud Native application can run on any cloud — or on-premises.

---

## The Five Traits

From the CNCF definition, Cloud Native systems exhibit five traits:

| Trait | Meaning |
|-------|---------|
| **Scalability** | Can expand (or contract) capacity to match demand, ideally automatically |
| **Loose Coupling** | Components interact through well-defined interfaces; changes to one do not cascade into others |
| **Resilience** | The system degrades gracefully and recovers automatically from failure |
| **Manageability** | Operators can update, configure, and observe the system without downtime or manual intervention |
| **Observability** | Internal state is inferred from outputs (logs, metrics, traces) without accessing the system internally |

---

## The Five Elements

The same definition identifies five *technical* elements that realise those traits:

| Element | Role |
|---------|------|
| **Containers** | Portable, immutable packaging unit — app + runtime + dependencies + config. Enables consistent execution across environments. |
| **Service Meshes** | Infrastructure layer for service-to-service communication (mTLS, circuit breaking, retries, observability). Examples: Istio, Linkerd, Consul. |
| **Microservices** | Decomposition of a monolithic application into small, independently deployable services, each with its own data store and release cycle. |
| **Immutable Infrastructure** | Infrastructure is never mutated after deployment; changes are applied by replacing, not patching. Eliminates configuration drift. |
| **Declarative APIs** | Desired state is declared (e.g., in YAML), and automation reconciles actual state to match. Kubernetes is the canonical example. |

---

## Microservices vs Monolith

Understanding Cloud Native requires understanding *why* monoliths are decomposed.

### Monolithic Architecture

All application functions (user login, registration, product catalogue, shopping cart, payment, etc.) packaged and deployed as a single unit, backed by a shared database.

**Limitations:**
- One unit of deployment — a change to any function requires full redeployment
- All functions tightly coupled — bugs in one can crash the whole system
- Technology lock-in — the entire stack must use the same language and framework
- Scaling is all-or-nothing — you cannot scale payment independently of login
- Low fault tolerance
- Increasingly complex to change over time

### Microservices Architecture

Each function decomposed into its own service, each with its own dedicated database and independent release cycle.

**Benefits:**
- Independent deployment — a payment fix does not require redeploying the product catalogue
- Independently scalable — scale only the services under load
- Technology-agnostic — each team can choose its own stack
- Fault isolation — a failing review service does not take down checkout
- Smaller, more maintainable codebases

**The new problem microservices create:**  
A dense, crossed graph of service-to-service dependencies — managing service discovery, load balancing, health checks, and rollouts across dozens of small services becomes operationally overwhelming. This is precisely the problem that **containers + Kubernetes + service meshes** solve.

---

## Design Considerations for Distributed Applications

Before selecting Cloud Native tooling, these four principles must inform the architecture:

1. An application should not be tied to a specific host or network.
2. End users should not be affected by hardware or software failures.
3. The application should remain accessible as its workload increases.
4. Rolling out updates should not cause downtime.

---

## The 8 Fallacies of Distributed Systems

Every Cloud Native engineer must internalise these. All eight are false assumptions that cause real-world failures when built into a distributed system.

| # | Fallacy | Why it matters |
|---|---------|---------------|
| 1 | The network is reliable | Packets drop; connections time out; design for retries and idempotency |
| 2 | Latency is zero | Every network hop adds latency; avoid chatty protocols; use async where possible |
| 3 | Bandwidth is infinite | Large payloads are expensive; pagination, compression, and streaming matter |
| 4 | The network is secure | Assume breach; mTLS between services; Zero Trust |
| 5 | Topology doesn't change | Nodes, IPs, and routes change; service discovery must be dynamic |
| 6 | There is one administrator | Multiple teams, multiple policies, multiple clouds; design for partial failure and conflicting configs |
| 7 | Transport cost is zero | Data transfer incurs financial cost, especially cross-region; co-locate where possible |
| 8 | The network is homogeneous | Mixed vendors, protocols, MTUs, and link speeds; use abstraction layers |

*Source: https://architecturenotes.co/fallacies-of-distributed-systems*

---

## CNCF Landscape

The Cloud Native Computing Foundation (CNCF) governs the open-source projects that form the Cloud Native ecosystem. Key graduated projects include Kubernetes, Prometheus, Envoy, Fluentd, gRPC, and Helm.

---

## Cloud Native and Performance Engineering

Cloud Native architecture is directly relevant to ICT3113 Performance Optimisation and Design:

- **Horizontal scaling** (Kubernetes Deployments with multiple replicas) distributes load across Pods — key to capacity-based performance planning
- **Auto-scaling** (Horizontal Pod Autoscaler) allows the system to adapt to measured demand — closing the loop between performance metrics and infrastructure
- **Observability** (the third trait) is the foundation of performance engineering: you cannot optimise what you cannot measure
- **Container resource requests and limits** feed directly into Kubernetes scheduling and are a micro-level performance design decision

---

## Related Pages

- [[concepts/kubernetes]] — Kubernetes architecture, objects, YAML manifests, security, and Helm
- [[concepts/docker-compose]] — Single-host Docker; the developer-environment complement to Kubernetes
- [[concepts/software-architecture-patterns]] — Broader architectural patterns context
- [[sources/ict3113-pod-lec11-12-kubernetes-docker]] — Dell industry session source notes
