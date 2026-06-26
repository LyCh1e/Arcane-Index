---
type: synthesis
status: developing
address: c-000075
created: 2026-06-26
updated: 2026-06-26
title: "Research: Kubernetes"
tags: [research, kubernetes, k8s, container-orchestration, devops, cloud-native, helm, managed-kubernetes]
related:
  - "[[concepts/kubernetes]]"
  - "[[concepts/docker-compose]]"
  - "[[concepts/github-actions-cicd]]"
  - "[[sources/kubernetes-official-docs]]"
sources:
  - "[[sources/kubernetes-official-docs]]"
---

# Research: Kubernetes

## Overview

Kubernetes (K8s) is the de facto standard for container orchestration in production. It automates deployment, scaling, and management of containerised applications across clusters of machines. Research conducted across 2 rounds: 5 searches + 4 page fetches, drawing on official Kubernetes documentation, Red Hat, Spacelift, and managed-service comparison sources.

---

## Key Findings

- **Kubernetes is a desired-state system**: you declare what you want (3 replicas of `nginx:1.26`); the control plane reconciles actual state to match. Every component (scheduler, controller manager, kubelet) is a reconciliation loop. This is the central design insight. (Source: [[sources/kubernetes-official-docs]])

- **etcd is the single point of failure**: all cluster state lives in etcd. In production, etcd must be deployed in a highly available odd-numbered cluster (3 or 5 nodes) with regular backups. Loss of etcd = loss of cluster state. (Source: [[sources/kubernetes-official-docs]])

- **Workload choice is determined by state requirements**: Deployments for stateless (pods are interchangeable); StatefulSets for stateful (stable pod identity, stable storage via PVCs); DaemonSets for infrastructure agents; Jobs/CronJobs for batch work. Using a Deployment for a database is a common anti-pattern — pods get rescheduled to different nodes and lose their storage. (Source: [[sources/kubernetes-official-docs]])

- **Services solve the ephemeral pod problem**: pods are mortal and their IPs change; a Service provides a stable virtual IP and DNS name. kube-proxy maintains iptables rules to route traffic to healthy pod endpoints. This is Kubernetes' internal service discovery mechanism. (Source: [[sources/kubernetes-official-docs]])

- **Ingress is not a Service type**: it is a separate API object that requires an Ingress controller (NGINX, Traefik, Envoy). Without a deployed controller, an Ingress resource has no effect. This catches many beginners off guard.

- **Secrets are not encrypted by default**: the name "Secret" implies security, but without EncryptionConfiguration, secrets are stored as base64-encoded plaintext in etcd. Any user with etcd read access or Kubernetes API `get` on a Secret reads the value directly. Production clusters must enable AES-GCM encryption at rest. (Source: [[sources/kubernetes-official-docs]])

- **Docker Compose and Kubernetes are not competitors**: they solve different problems. Compose is a single-host developer tool (~50 MB overhead). Kubernetes is a multi-node production orchestrator (~2 GB control plane). Standard pattern: Compose for local development, Kubernetes for production.

- **Helm 4.0 (November 2025) introduced server-side apply**: previously, Helm applied manifests client-side, causing field-ownership conflicts when multiple tools (ArgoCD, kubectl, Helm) touched the same resources. Server-side apply delegates merge logic to the Kubernetes API server, which tracks field ownership correctly.

- **Managed services (GKE/EKS/AKS) abstract the control plane**: self-managing a production control plane is operationally expensive. All major cloud providers offer managed Kubernetes — GKE is fastest to adopt new K8s versions (~2 weeks), EKS most deeply integrated with AWS IAM/VPC, AKS most cost-effective for Azure shops. All three support K8s 1.33 as of October 2025.

---

## Key Entities

- **CNCF (Cloud Native Computing Foundation)** — steward of Kubernetes since 2016; part of the Linux Foundation
- **Google** — original creator; open-sourced 2014; Kubernetes evolved from internal Borg + Omega systems
- **GKE** (Google Kubernetes Engine) — Google's managed Kubernetes; fastest version adoption
- **EKS** (Amazon Elastic Kubernetes Service) — AWS-native; deep IAM and VPC integration
- **AKS** (Azure Kubernetes Service) — Microsoft; strong Active Directory integration
- **Helm** — Kubernetes package manager; v4.0 released November 2025 at KubeCon NA

---

## Key Concepts

- [[concepts/kubernetes]] — full reference: architecture, workloads, networking, security, Helm, managed services, kubectl commands

---

## Contradictions

- **Container runtime**: older sources cite Docker as the standard runtime. Kubernetes deprecated the Docker runtime shim (dockershim) in v1.20 and removed it in v1.24. The current default is `containerd`. Docker Engine still works via a compatibility shim but is not the recommended runtime.

- **kube-proxy optionality**: the official docs note kube-proxy is "optional" (some CNI plugins replace it), but in practice the vast majority of clusters run it. Treating it as optional is accurate but potentially confusing for beginners.

---

## Open Questions

- **eBPF-based networking (Cilium)**: Cilium replaces kube-proxy with eBPF, claiming significant performance improvements. Not well researched — worth a dedicated autoresearch pass.
- **GitOps with ArgoCD / Flux**: the standard pattern for Kubernetes deployments in production is GitOps — the cluster state is the git repo. Not covered in this session.
- **Kubernetes 1.35+ Workload API / gang scheduling**: the official docs mention `PodGroupTemplates` for ML/batch "all-or-nothing" placement — this is very new (K8s 1.35) and not yet widely documented in secondary sources.
- **Service mesh (Istio / Linkerd)**: advanced networking — mTLS between pods, traffic shaping, observability. Outside the scope of this session.

---

## Sources

- [[sources/kubernetes-official-docs]] — Kubernetes / CNCF, 2024. Authoritative reference for components, workloads, networking, security.
