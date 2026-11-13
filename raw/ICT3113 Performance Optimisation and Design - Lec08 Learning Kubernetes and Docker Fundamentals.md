# Learning Kubernetes & Docker Fundamentals

Dell Technologies. Lecture 08, ICT3113 Performance Optimisation and Design. 63 slides. Diagrams and images are described in *italics* inside square brackets.

---

## Slide 1: Title

**Learning Kubernetes & Docker Fundamentals**

Dell Technologies

---

## Slide 2: About Me

- Member of the AI Innovation Hub (AIH) team in Dell Technologies
- 20+ years as an IT Practitioner
- Software Development, Project Management, Operations Management, DevOps, Pre-Sales and Post-Sales
- Passionate about Cloud Native technologies and their emerging trends

*[Photo of the presenter. Logos of previous employers: VMware, Pivotal, Puppet, CA Technologies, Quest, Borland.]*

---

## Slide 3: Key Focus Areas

*[Venn-style diagram with CLOUD-NATIVE at the centre, surrounded by four circles: DevOps, Continuous Delivery, Microservices, Containers.]*

---

## Slide 4: A Cloud is an abstraction

*[Image reading "THERE IS NO CLOUD. IT'S JUST SOMEONE ELSE'S COMPUTER", next to a comic strip about the cloud being someone else's servers.]*

---

## Slide 5: Cloud Native Vs Cloud Computing

*Are they the same?*

*[Left: CNCF logo with the labels Architecture, Applications, Services. Right: cloud provider logos (Google Cloud, AWS, Azure) with the labels Resource Pooling, Rapid Elasticity, Broad Network Access, Pay As You Go, On-Demand Self-Service, Measured Service.]*

---

## Slide 6: Cloud Native Vs Cloud Computing

*Are they the same?*

*[CNCF logo captioned "How?" and cloud provider logos captioned "Where?".]*

Cloud Native Development is an approach to building and running applications that exploits the advantages of the Cloud Computing delivery model

---

## Slide 7: What is Cloud Native?

Cloud native technologies empower organizations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach. These techniques enable loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil

*[Cloud Native Computing Foundation logo.]*

---

## Slide 8: Why go Cloud Native?

Cloud native technologies empower organizations to build and run **scalable** applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach. These techniques enable **loosely coupled** systems that are **resilient**, **manageable**, and **observable**. Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil

*(Highlighted words: scalable, loosely coupled, resilient, manageable, observable.)*

---

## Slide 9: Traits of Cloud Native

*[The same paragraph, shrunk on the left, with the trait words highlighted.]*

- Scalability
- Loose Coupling
- Resilience
- Manageability
- Observability

---

## Slide 10: How to be Cloud Native?

Cloud native technologies empower organizations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. **Containers**, **service meshes**, **microservices**, **immutable infrastructure**, and **declarative APIs** exemplify this approach. These techniques enable loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil

*(Highlighted words: containers, service meshes, microservices, immutable infrastructure, declarative APIs.)*

---

## Slide 11: Elements of Cloud Native

*[The same paragraph, shrunk on the left, with the element words highlighted.]*

- Containers
- Service Meshes
- Microservices
- Immutable Infrastructure
- Declarative APIs

---

## Slide 12: Design Considerations for Distributed Apps

- An app should not be tied to a specific host or network
- The end user should not be affected by a hardware or software failure
- An app should still be accessible as its workload increases
- There should not be any downtime when rolling out new updates to the app

---

## Slide 13: The Art of Microservices

*[Divide and Conquer game-style crest image, next to a cube icon splitting into smaller cubes.]*

---

## Slide 14: A Monolithic App

*[Diagram: a single block labelled "Monolith" connected to one "Database".]*

---

## Slide 15: A Monolithic App

*[Diagram: the Monolith block now shows the functions inside it: User Login, Registration, Product Catalog, User Reviews, Shopping Cart, Payment. It connects to one Database. An illustration of shoppers sits beside it.]*

---

## Slide 16: Limitations of a Monolithic App

- One unit of deployment
- All functionalities and processes are tightly coupled
- Running as a single service
- Adding new features becomes more complex over time
- Lock-in to a particular technology stack
- Low fault tolerance
- Scaling limitations

*[Small copy of the monolith diagram: all six functions inside one Monolith, one Database.]*

---

## Slide 17: Tightly Coupled Architectures

*[Diagram: a load balancer feeds two Web servers; each Web server connects to both App servers; both App servers connect to a single Database.]*

Architectural components are *strongly connected* to each other

---

## Slide 18: Microservice Architecture

*[Diagram: separate services User Login, Registration, Product Catalog, User Reviews, Shopping Cart, each with its own Database, and Payment with its own Database.]*

---

## Slide 19: Modernising our Monolithic App

*[Diagram: the Monolith with its Database, an arrow, then the microservices (User Login, Registration, Product Catalog, User Reviews, Shopping Cart, Payment), each with its own Database.]*

---

## Slide 20: We have created a new problem here

*[Network graph of many connected coloured nodes, representing many services.]*

---

## Slide 21: Where do we host them?

*[Grey network graph of many connected nodes.]*

---

## Slide 22: Where do we host them?

*[Diagram: a circle labelled "Monolith" sits on a stack of Operating System and Virtual Machine. Beside it is the network graph of many nodes with a question mark.]*

---

## Slide 23: Containers

*[Full-slide photo of stacked shipping containers.]*

---

## Slide 24: What is a Container?

*[Diagram: a cardboard box, with labels pointing into it: App, Language Runtime, App Libraries and Dependencies.]*

---

## Slide 25: What is a Container?

- Standardised unit for *development, deployment* and *distribution*
- Packages up *code* and all its *dependencies* which includes your programming language runtimes, executables, binary code, libraries and configuration files
- Abstracts applications from the environment in which they actually run

---

## Slide 26: What is Docker?

- Open source containerisation platform
- Launched in 2013
- Created the industry standard for containers
- Seamless portability - *Build once run anywhere*
- Cloud-agnostic
- Lightweight

*[Docker logo.]*

---

## Slide 27: Benefits of Containers

- Consistency
- Predictability
- Portability
- Isolation
- Resource efficiency
- Separation of responsibility
- Improved developer productivity

*[Meme image: "It works on my machine".]*

---

## Slide 28: Comparing with a VM

*[Diagram of the VM stack, bottom to top: Infrastructure, Hypervisor, then three VMs, each containing a Guest Operating System and an app (APP A, APP B, APP C).]*

A container is not exactly a **virtual machine** but …

---

## Slide 29: Comparing with a VM

*[Two diagrams side by side.*
*Left (VMs), bottom to top: Infrastructure, Hypervisor, then three VMs each with a Guest Operating System and an app (APP A, B, C).*
*Right (containers), bottom to top: Infrastructure, Operating System, Container Runtime, then APP A, APP B, APP C.]*

---

## Slide 30: Works perfectly with VMs too!

*[Two diagrams side by side.*
*Left (VMs), bottom to top: Infrastructure, Hypervisor, then three VMs each with a Guest Operating System.*
*Right, bottom to top: Infrastructure, Hypervisor, Guest Operating System, Container Runtime, then APP A, APP B, APP C. An arrow links one of the VMs on the left to this stack, showing containers running inside a VM's guest OS.]*

---

## Slide 31: Where do we host them?

*[Network graph of many connected nodes, each marked with a Docker whale logo.]*

---

## Slide 32: Container Sprawl

*[Diagram of several clusters of connected coloured nodes, linked by arrows between clusters.]*

---

## Slide 33: We have a new set of challenges

*[Comic of a stressed developer surrounded by worried speech bubbles. Source: https://cloud.google.com/kubernetes-engine/kubernetes-comic]*

---

## Slide 34: Container Orchestration

*[Diagram of clustered coloured nodes on the left.]*

- Service discovery and load balancing
- Storage orchestration
- Automated rollouts and rollbacks
- Auto-scaling
- Self-healing
- Secret and configuration management
- and lots more ...

---

## Slide 35: What is Kubernetes?

- Container orchestration platform
- Environment for running distributed apps on containers at scale
- *Originally developed by Google*
- Open sourced in 2014
- Flagship project of *Cloud Native Computing Foundation* (CNCF)
- Defines a common set of resources and an API for manipulating them

*[Kubernetes logo.]*

---

## Slide 36: Fun Facts

- κυβερνήτης - Greek word for 'helmsman'
- k8s
  kubernetes *(k, then 8 letters "ubernete", then s)*

*[Illustration of a ship's helmsman at the wheel. Kubernetes logo.]*

---

## Slide 37: Fallacies of Distributed Systems

*[Illustration titled "8 Fallacies of Distributed Systems": 1. The network is reliable. 2. Latency is zero. 3. Bandwidth is infinite. 4. The network is secure. 5. Topology doesn't change. 6. There is one administrator. 7. Transport cost is zero. 8. The network is homogeneous.]*

Source - https://architecturenotes.co/fallacies-of-distributed-systems

---

## Slide 38: Abstracting away the Infrastructure

*[Diagram: a user at the top with App A, App B, App C, App D. These sit on a Kubernetes layer. Below Kubernetes are five Compute nodes, a Network layer, and three Storage nodes.]*

---

## Slide 39: Kubernetes Key Goals

*[Comic panel of a character with a speech bubble: "So, Kubernetes has a few key goals:". Source: https://cloud.google.com/kubernetes-engine/kubernetes-comic]*

---

## Slide 40: Kubernetes Key Goals (comic panels)

*[Three comic panels:]*

1. To distribute containers in a logical and efficient way. **Translation: MAXIMIZE CAPACITY**
2. To scale up (or down) fast with the resources you already have. **Translation: ADAPT TO DEMAND**
3. To keep processes continuously running and healthy. **Translation: DON'T GO DARK**

Source - https://cloud.google.com/kubernetes-engine/kubernetes-comic

---

## Slide 41: Pod

- *Smallest* deployable unit in k8s
- Represents a basic unit of *running code*
- Groups one or more containers together
- Manages the containers
- Has a unique IP address within the cluster

*[Banner image of orcas (a pod of whales).]*

---

## Slide 42: Our Container

*[Diagram: a box labelled with "My Spring Boot App" and "App Libraries and Dependencies".]*

---

## Slide 43: Our Pod

*[Diagram: a pod outline containing the container box, with a Docker whale logo.]*

---

## Slide 44: Our Pod

*[Diagram: the pod outline now shows the Spring Boot logo for the app inside, with a Docker whale logo.]*

---

## Slide 45: Our App

*[Diagram: Kubernetes managing four pods: Payment Pod, Product Pod, Inventory Pod, Shopping Cart Pod.]*

---

## Slide 46: What happens when a Pod is down?

*[Diagram: the same four pods under Kubernetes (Payment Pod, Product Pod, Inventory Pod, Shopping Cart Pod), with a red cross on the Payment Pod.]*

---

## Slide 47: We need a Deployment

*[Diagram: Kubernetes manages "Payment Deployment, Replicas = 1", which manages one Payment Pod.]*

---

## Slide 48: Pod is down

*[Diagram: Kubernetes, with a speech bubble, over "Payment Deployment, Replicas = 1". The one Payment Pod is crossed out in red.]*

---

## Slide 49: Self-healing

*[Diagram: "Payment Deployment, Replicas = 1" now has two Payment Pods: the failed one (crossed out) and a new replacement Payment Pod.]*

---

## Slide 50: Reconcile Loop

- Control loop - non-terminating loop that regulates the state of the system
- Desired state = Actual state
- kube-controller-manager
  - Deployment Controller
  - Job Controller
  - Many other built-in controllers

*[Totoro-style character illustration.]*

---

## Slide 51: Back to our app

*[Diagram: Kubernetes, "Payment Deployment, Replicas = 1", one Payment Pod.]*

---

## Slide 52: High Traffic

*[Diagram: the same single-replica Payment Deployment and one Payment Pod, with an arrow of incoming traffic and a "SALE" tag.]*

---

## Slide 53: High Traffic

*[Diagram: the same single replica, now with a heavy load on the Payment Pod shown by a figure being crushed under it, and a "SALE" tag.]*

---

## Slide 54: Horizontal Scaling

*[Diagram: the Deployment is changed to "Payment Deployment, Replicas = 3" (magic wand effect), while only one Payment Pod exists so far, still under load.]*

---

## Slide 55: Horizontal Scaling

*[Diagram: "Payment Deployment, Replicas = 3" now manages three Payment Pods.]*

---

## Slide 56: Kubernetes Fundamentals Online Course

*[Screenshot of the course page: "Getting Up to Speed with Docker", Course ID: ESDTFD04964, status "Not Registered", rating 5.0 (1).]*

---

## Slide 57: How to access the learning portal?

1. Go to the "Exploring Kubernetes" course page: Kubernetes Course
2. If you don't have an existing Dell account, register an account on the same page and click on "Create Account" else skip to the next slide to proceed with the course enrolment
   - a) Sign up using your university/poly email ID
3. It will prompt you to verify your account with an OTP
4. Check your email inbox for an email titled "Email OTP" from dell.myaccount.automated@dell.com.
   - a) Check your Spam and Junk folders if you don't see this in your inbox
5. Copy the 6-digit OTP from the email and paste it on the "Please verify your email account" page
6. Voila, your account activation is complete!
7. On the "Additional Access Rights Required" page, select "Personal/Individual" and click on submit

---

## Slide 58: How to access the learning portal?

1. Once you have activated your Dell account or if you have an existing Dell account, go to the "Getting Up to Speed with Docker" course page: Docker Course
2. Login with your Dell account and enroll yourself by selecting "English" for language and then click on "Register" to start learning!
3. If you run into any difficulties with access, please contact c.chua@dell.com or Brenda.Koh@dell.com

**\* Take Note \***
The course will launch a new pop-up window, do allow pop up to view the video content

---

## Slide 59: A Typical Learning Path

*[Arrow diagram, left to right: Kickstart, then "Getting Up to Speed with Docker" (course thumbnail), then Retrospective.]*

---

## Slide 60: Exploring Kubernetes

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

*[QR code and link: https://bit.ly/dell-cna-k8s]*

---

## Slide 61: Course Assessment

**Getting Up to Speed with Docker Assessments**

The following assessment measures your knowledge of Getting Up to Speed with Docker.
To receive credit for this course, you must achieve a passing score of **80%**.

The assessment is set up as follows:

- The assessment contains 25 questions.
- Answer a question by selecting a response, clicking Submit and then clicking Next.

*[Screenshot of a Dell Technologies Certificate of Completion for "Getting Up to Speed with Docker", Course Number ESDTFD04573, Course Duration 05:00.]*

---

## Slide 62: Thank you

Dell Digital Proven

62 · © Copyright 2022 Dell Inc.

---

## Slide 63: Dell Technologies

*[Closing slide with the Dell Technologies logo.]*
