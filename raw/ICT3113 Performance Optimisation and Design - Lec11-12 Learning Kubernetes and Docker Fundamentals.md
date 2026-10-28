# Learning Kubernetes & Docker Fundamentals

**Dell Technologies — Industry Session (Weeks 11–12)**

*Dell Technologies*

---

## About Me

- Member of the AI Innovation Hub (AIH) team in Dell Technologies
- 20+ years as an IT Practitioner
- Software Development, Project Management, Operations Management, DevOps, Pre-Sales and Post-Sales
- Passionate about Cloud Native technologies and their emerging trends

Previous experience/affiliations shown as logos: VMware, Pivotal, Puppet, CA Technologies, Quest, Borland.

---

## Key Focus Areas

Four focus areas arranged around the centre label "CLOUD-NATIVE":

- DevOps
- Continuous Delivery
- Microservices
- Containers

---

## A Cloud is an Abstraction

> "THERE IS NO CLOUD — IT'S JUST SOMEONE ELSE'S COMPUTER"

Paired with the well-known xkcd comic strip on cloud computing:

1. "What's this?" / "The cloud."
2. "Huh? I always thought 'the cloud' was a huge, amorphous network of servers somewhere." / "Yeah, but everyone buys server time from everyone else. In the end, they're all getting it here."
3. "How? You're on a cable modem." / "There's a lot of caching."
4. "Should the cord be stretched across the room like this?" / "Of course. It has to reach the server, and the server is over there."
5. "What if someone trips on it? Who would want to do that? It sounds unpleasant." / "Uh. Sometimes people do stuff by accident." / "I don't think I know anybody like that."

---

## Cloud Native Vs Cloud Computing

*Are they the same?*

**Cloud Native** (icon: Cloud Native Computing Foundation logo)
- Architecture
- Applications
- Services

**Cloud Computing** (icons: Google Cloud, AWS, Azure)
- Resource Pooling
- Broad Network Access
- On-Demand Self-Service
- Rapid Elasticity
- Pay As You Go
- Measured Service

**Follow-up framing (second slide, same visuals):**

- Cloud Native → **How?**
- Cloud Computing → **Where?**

Cloud Native Development is an approach to building and running applications that exploits the advantages of the Cloud Computing delivery model.

---

## What is Cloud Native?

> Cloud native technologies empower organizations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach. These techniques enable loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil.

— Cloud Native Computing Foundation (official definition)

This same definition is reused across the next several slides, with different phrases highlighted to build up the "why," "traits," "elements," and "how" of cloud native.

---

## Why go Cloud Native?

Same CNCF definition as above, with **scalable**, **loosely coupled**, **resilient**, **manageable**, and **observable** highlighted in green.

---

## Traits of Cloud Native

The definition text (left) maps to five traits (right), each highlighted in the text in green:

- Scalability
- Loose Coupling
- Resilience
- Manageability
- Observability

---

## How to be Cloud Native?

Same CNCF definition, this time with **Containers**, **service meshes**, **microservices**, **immutable infrastructure**, and **declarative APIs** highlighted in purple.

---

## Elements of Cloud Native

The definition text (left) maps to five elements (right), each highlighted in purple:

- Containers
- Service Meshes
- Microservices
- Immutable Infrastructure
- Declarative APIs

---

## Design Considerations for Distributed Apps

- An app should not be tied to a specific host or network
- The end user should not be affected by a hardware or software failure
- An app should still be accessible as its workload increases
- There should not be any downtime when rolling out new updates to the app

---

## The Art of Microservices

Slide features a "Divide and Conquer" game logo alongside an icon of a single cube splitting into many smaller cubes — illustrating the principle of decomposing one unit into many independent parts.

---

## A Monolithic App

A single blue box labelled **Monolith**, connected to one **Database** cylinder below it.

**Second version of this slide** expands the Monolith box into its internal functional blocks:
- User Login
- Registration
- Product Catalog
- User Reviews
- Shopping Cart
- Payment

All still backed by a single Database, with an illustration of people shopping online alongside.

---

## Limitations of a Monolithic App

- *One unit* of deployment
- All functionalities and processes are *tightly coupled*
- Running as a *single service*
- Adding new features becomes more *complex* over time
- Lock-in to a particular technology stack
- Low fault tolerance
- Scaling limitations

(Diagram repeats the Monolith box with its six internal blocks, connected to one Database.)

---

## Tightly Coupled Architectures

A load-balancer icon routes to two **Web** nodes, which both connect (criss-crossing) to two **App** nodes, which both connect to a single **Database**.

> Architectural components are *strongly connected* to each other.

---

## Microservice Architecture

Five independent service blocks, each with its own dedicated database:

- User Login → Database
- Registration → Database
- Product Catalog → Database
- User Reviews → Database
- Shopping Cart → Database

Plus a separate Payment service with its own Database.

---

## Modernising our Monolithic App

Before/after diagram:

**Before:** the Monolith box (User Login, Registration, Product Catalog, User Reviews, Shopping Cart, Payment) → one shared Database.

**After (arrow to the right):** each of the six functions broken out into its own small service, each with its own small database, plus Payment with its own database — six independent service+database pairs in place of the one monolith.

---

## We Have Created a New Problem Here

A dense graph of many small coloured nodes connected by crossing arrows — illustrating that decomposing a monolith into many microservices creates a new, harder-to-manage web of service-to-service dependencies (the "distributed monolith" / service-mesh complexity problem).

---

## Where do we host them?

This question appears as a recurring motif across three progressively-answered slides:

1. The same dense graph of nodes/services shown with no hosting answer — just the open question "Where do we host them?"
2. The graph shown next to a **Monolith** circle with **Operating System** and **Virtual Machine** boxes beneath it, and a "?" next to the graph of services — contrasting the old (monolith on OS/VM) hosting model with the unanswered question of how to host many small services.
3. (Later slide, after containers are introduced) The same dense graph of nodes, now with a small blue Docker whale icon attached to every single node — the answer is: each service runs in its own container.

---

# Containers

*(Section divider slide — photo of stacked, colour-coded shipping containers at a port.)*

---

## What is a Container?

A container packages together:
- **App**
- **Language Runtime**
- **App Libraries and Dependencies**

(Illustrated as items going into an open cardboard box.)

**Second slide, in bullet form:**

- Standardised unit for *development*, *deployment* and *distribution*
- Packages up *code* and all its *dependencies* which includes your programming language runtimes, executables, binary code, libraries and configuration files
- Abstracts applications from the environment in which they actually run

---

## What is Docker?

- Open source containerisation platform
- Launched in 2013
- Created the industry standard for containers
- Seamless portability — *Build once run anywhere*
- Cloud-agnostic
- Lightweight

---

## Benefits of Containers

- Consistency
- Predictability
- Portability
- Isolation
- Resource efficiency
- Separation of responsibility
- Improved developer productivity

(Accompanied by the classic "¯\\_(ツ)_/¯ IT WORKS on my machine" meme image.)

---

## Comparing with a VM

**First diagram:** three VMs side by side, each with its own **APP** (A, B, C) and its own **Guest Operating System**, all sitting on a shared **Hypervisor**, which sits on **Infrastructure**.

> A container is not exactly a **virtual machine** but …

**Second diagram (side-by-side comparison):**

| VM stack | Container stack |
|---|---|
| APP A / APP B / APP C | APP A / APP B / APP C |
| Guest OS (×3, one per VM) | Container Runtime |
| Hypervisor | Operating System |
| Infrastructure | Infrastructure |

The container stack replaces three separate guest operating systems with a single shared OS plus a container runtime layer.

**Third diagram — "Works perfectly with VMs too!":** shows that containers and VMs are not mutually exclusive — a VM can itself run a Container Runtime and Guest Operating System hosting multiple apps (APP A, APP B, APP C), sitting on the same Hypervisor/Infrastructure as other plain VMs.

---

## Where do we host them? (continued)

The dense service graph reappears, now with every node tagged with a small Docker whale logo — i.e., each service is hosted in its own Docker container.

---

## Container Sprawl

Four clusters of many small Docker-whale-tagged nodes (grey, yellow/orange, pink/salmon, and green), connected by arrows flowing from the grey cluster toward the others — illustrating how the number of containers to manage explodes ("sprawl") as the architecture grows.

---

## We Have a New Set of Challenges

Google's Kubernetes comic strip, showing a stressed engineer surrounded by complaints:

- "Why isn't my code up yet??"
- "We can't scale up fast enough!"
- "Sorry to call at 3:00am, but—"
- "For Hera's sake, who knew delivering these services would be so HARD?"
- "Our update cycles are too slow!"
- "Game's gonna get stale, boss…"
- "Oh, crap — power's out again!"

> "Why can't it just WORK ALL THE TIME?!"

*Source: https://cloud.google.com/kubernetes-engine/kubernetes-comic*

---

## Container Orchestration

- Service discovery and load balancing
- Storage orchestration
- Automated rollouts and rollbacks
- Auto-scaling
- Self-healing
- Secret and configuration management
- and lots more …

(Illustrated with the same four coloured container-sprawl clusters, now connected in an orchestrated flow.)

---

## What is Kubernetes?

- Container orchestration platform
- Environment for running distributed apps on containers at scale
- Originally developed by *Google*
- Open sourced in 2014
- Flagship project of *Cloud Native Computing Foundation* (CNCF)
- Defines a common set of resources and an API for manipulating them

---

## Fun Facts

- **κυβερνήτης** — Greek word for 'helmsman'
- **k8s** / **kubernetes** — the "8" in "k8s" stands for the eight letters elided between the "k" and the final "s" in "kubernetes"

(Illustrated with a cartoon ship's helmsman saying "WE ARE ON THE RIGHT WAY!")

---

## 8 Fallacies of Distributed Systems

1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

*Source: https://architecturenotes.co/fallacies-of-distributed-systems*

---

## Abstracting Away the Infrastructure

A developer deploys **App A**, **App B**, **App C**, **App D** onto a **Kubernetes** layer, which in turn abstracts away the underlying **Compute** nodes, **Storage**, and **Network** — the developer works against Kubernetes and never touches the infrastructure directly.

---

## Kubernetes: Key Goals

Google's Kubernetes comic (a Greek-goddess-styled figure) introduces the "key goals" of Kubernetes, each with a literal description and its "translation":

1. "To distribute containers in a logical and efficient way." → **Translation: MAXIMIZE CAPACITY**
2. "To scale up (or down) fast with the ops you already have." → **Translation: ADAPT TO DEMAND**
3. "To keep processes continuously running and healthy." → **Translation: DON'T GO DARK**

*Source: https://cloud.google.com/kubernetes-engine/kubernetes-comic*

---

## Pod

- *Smallest* deployable unit in k8s
- Represents a basic unit of *running code*
- Groups one or more containers together
- Manages the containers
- Has a unique IP address within the cluster

---

## Our Container

Building a worked example: a container holding **My Spring Boot App** plus its **App Libraries and Dependencies**.

---

## Our Pod

Builds up the worked example step by step:

1. An empty Pod boundary (rounded arch shape) with a Docker whale icon in the corner, and an (empty) cardboard-box container icon inside it.
2. The same Pod boundary, now with the box icon replaced by the Spring Boot (green power-button) icon — representing "My Spring Boot App" container running inside the Pod.

---

## Our App

Four Pods, each managed by Kubernetes, each running one Spring-Boot-style container:

- Payment Pod
- Product Pod
- Inventory Pod
- Shopping Cart Pod

Kubernetes sits above all four Pods with dashed arrows pointing down to each.

---

## What happens when a Pod is down?

Same four-Pod diagram as above, but the **Payment Pod** now shows a red "✗" over its app icon — illustrating a Pod failure. Kubernetes still oversees all four Pods via dashed arrows.

---

## We Need a Deployment

Introduces the **Deployment** resource: Kubernetes manages a **Payment Deployment** (with **Replicas = 1**), which in turn manages the **Payment Pod**.

```
kubernetes
    │
    ▼
Payment Deployment (Replicas = 1)
    │
    ▼
Payment Pod
```

---

## Pod is down

The Payment Pod (under the Payment Deployment, Replicas = 1) now shows the red "✗" failure mark. Kubernetes is shown reacting (empty speech bubble above it), about to respond to the failure.

---

## Self-healing

Kubernetes detects the failed Payment Pod and automatically creates a **new, healthy** Payment Pod alongside it — both pods now shown side by side under the same Payment Deployment: one healthy (left), one still marked failed (right, being cleaned up/replaced).

---

## Reconcile Loop

- **Control loop** — non-terminating loop that regulates the state of the system
- **Desired state = Actual state**
- **kube-controller-manager**
  - Deployment Controller
  - Job Controller
  - Many other built-in controllers

(Illustrated with a Totoro-style character inside a ring — a playful nod to the continuous "loop.")

---

## Back to our App

Returns to the single Payment Deployment (Replicas = 1) → Payment Pod diagram, now healthy again, as the baseline before introducing scaling.

---

## High Traffic

Two sequential slides show a "SALE" tag appearing and a customer/shopper icon appearing at the single Payment Pod, under the Payment Deployment (Replicas = 1) — illustrating a surge of incoming traffic hitting the single-replica deployment.

---

## Horizontal Scaling

Two sequential slides:

1. Kubernetes (with a magic-wand icon) updates the Payment Deployment to **Replicas = 3**, with the shopper icon still at the original single Pod.
2. The Payment Deployment (Replicas = 3) now fans out (dashed arrows) to **three** Payment Pods side by side, each an independent healthy replica — spreading the incoming traffic across multiple Pods.

---

## Kubernetes Fundamentals Online Course

Dell course registration card shown as an example:

- Course: **"Getting Up to Speed with Docker"**
- Course ID: **ESDTFD04964**
- Status: Not Registered
- Rating: 5.0 (1)

---

## How to access the learning portal?

**Part 1 — account setup:**

1. Go to the "Exploring Kubernetes" course page: *Kubernetes Course* [link]
2. If you don't have an existing Dell account, register an account on the same page and click on "Create Account", else **skip to the next slide** to proceed with the course enrolment
   a. Sign up using your university/poly email ID
3. It will prompt you to verify your account with an OTP
4. Check your email inbox for an email titled "Email OTP" from dell.myaccount.automated@dell.com
   a. Check your Spam and Junk folders if you don't see this in your inbox
5. Copy the 6-digit OTP from the email and paste it on the "Please verify your email account" page
6. Voila, your account activation is complete!
7. On the "Additional Access Rights Required" page, select "Personal/Individual" and click on submit

**Part 2 — course enrolment:**

1. Once you have activated your Dell account or if you have an existing Dell account, go to the "Getting Up to Speed with Docker" course page: *Docker Course* [link]
2. Login with your Dell account and enrol yourself by selecting "English" for language and then click on "Register" to start learning!
3. If you run into any difficulties with access, please contact **c.chua@dell.com** or **Brenda.Koh@dell.com**

**\* Take Note \***
The course will launch a new pop-up window, do **allow pop up** to view the video content.

---

## A Typical Learning Path

A timeline arrow moving left to right:

**Kickstart** → **Getting Up to Speed with Docker** (video course) → **Retrospective**

---

## Exploring Kubernetes

Course outline — 10 modules:

1. Introduction to Kubernetes
2. Understanding the Kubernetes Architecture
3. Deploying Applications in Kubernetes
4. Imperative and Declarative Workflows
5. Services and Networking
6. Applying Deployment Strategies
7. Externalizing Configuration with ConfigMaps and Secrets
8. Persisting Data with Volumes
9. Managing Namespaces and Resource Quotas
10. Best Practices and Troubleshooting

Access link (with QR code): **https://bit.ly/dell-cna-k8s**

---

## Course Assessment

### Getting Up to Speed with Docker Assessments

The following assessment measures your knowledge of Getting Up to Speed with Docker.

To receive credit for this course, you must achieve a passing score of **80%**.

The assessment is set up as follows:

- The assessment contains 25 questions.
- Answer a question by selecting a response, clicking Submit and then clicking Next.

**Example certificate shown:**

> **DELL Technologies — CERTIFICATE OF COMPLETION**
> This is to acknowledge that
> **WEI JIE TAN**
> has completed the following
> **GETTING UP TO SPEED WITH DOCKER**
> Jan 31, 2024
> Course Number: ESDTFD04573
> Course Duration: 05:00

---

## Thank You

*Dell Technologies — closing slide.*

---
*Dell Digital Proven — © Copyright 2022 Dell Inc.*
