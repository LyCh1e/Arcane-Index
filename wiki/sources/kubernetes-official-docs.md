---
type: source
status: established
address: c-000074
created: 2026-06-26
updated: 2026-06-26
title: "Kubernetes Official Documentation — Components and Workloads"
source_type: official documentation
author: Kubernetes / CNCF
date_published: 2024-01-01
url: https://kubernetes.io/docs/concepts/
confidence: high
tags: [kubernetes, k8s, container-orchestration, control-plane, workloads, networking, rbac]
related:
  - "[[concepts/kubernetes]]"
  - "[[synthesis/research-kubernetes]]"
---

# Kubernetes Official Documentation

## Summary

Official CNCF documentation for Kubernetes. Primary reference for component architecture (`/docs/concepts/overview/components/`), workload types (`/docs/concepts/workloads/`), networking (`/docs/concepts/services-networking/`), and security (`/docs/concepts/security/`). High-confidence authoritative source; versioned alongside each Kubernetes release.

## Key Claims

- The control plane comprises: kube-apiserver, etcd, kube-scheduler, kube-controller-manager, and (optionally) cloud-controller-manager
- Worker nodes run: kubelet, kube-proxy, and a CRI-compatible container runtime
- etcd is the single source of truth for all cluster state; HA deployments require a highly available etcd cluster
- Workload hierarchy: Pod < ReplicaSet < Deployment (for stateless); Pod < StatefulSet (for stateful, stable identity, per-pod PVCs)
- DaemonSets guarantee one pod per matching node; used for cluster infrastructure daemons
- Service types: ClusterIP (internal), NodePort (external via static port), LoadBalancer (cloud-provisioned external LB), ExternalName (DNS alias)
- Kubernetes v1.35+ introduces the Workload API for PodGroupTemplates supporting gang scheduling for batch/ML workloads
- Secrets are base64-encoded, **not encrypted**, in etcd by default; EncryptionConfiguration must be explicitly enabled

## Sections Used

- `kubernetes.io/docs/concepts/overview/components/` — cluster components
- `kubernetes.io/docs/concepts/workloads/` — workload types and lifecycle
- `kubernetes.io/docs/concepts/services-networking/service/` — Service types
- `kubernetes.io/docs/concepts/security/rbac-good-practices/` — RBAC
- `kubernetes.io/docs/concepts/configuration/secret/` — Secrets

## Concepts Generated

| Concept | Action |
|---------|--------|
| [[concepts/kubernetes]] | Created |
