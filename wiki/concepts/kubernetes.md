---
type: concept
status: established
address: c-000073
created: 2026-06-26
updated: 2026-06-26
tags: [kubernetes, k8s, container-orchestration, devops, cloud-native, helm, kubectl, docker]
related:
  - "[[concepts/docker-compose]]"
  - "[[concepts/github-actions-cicd]]"
  - "[[concepts/nginx-reverse-proxy-and-tls]]"
  - "[[synthesis/research-kubernetes]]"
---

# Kubernetes

Kubernetes (K8s) is an open-source container orchestration system for automating the deployment, scaling, and management of containerised applications across clusters of machines. Originally developed at Google (based on internal systems Borg and Omega), it was open-sourced in 2014 and donated to the Cloud Native Computing Foundation (CNCF). It is now the de facto production standard for running containers at scale.

> [!info] Kubernetes vs Docker Compose
> Docker Compose runs containers on a **single host** — it is a developer tool. Kubernetes runs containers across **multiple nodes** with self-healing, auto-scaling, and high availability. They are complementary: Compose for local development, Kubernetes for production.

---

## Architecture

A Kubernetes cluster consists of a **control plane** (the brain — manages desired state) and one or more **worker nodes** (the muscles — run application workloads).

### Control Plane Components

| Component | Role |
|-----------|------|
| **kube-apiserver** | Single entry point for all API requests. Validates, authenticates, and writes state to etcd. |
| **etcd** | Distributed key-value store. The single source of truth for all cluster state (pod specs, service configs, Secrets, node registrations). |
| **kube-scheduler** | Watches for unscheduled pods and assigns each to the best-fit node based on resources, affinity, and constraints. |
| **kube-controller-manager** | Runs all built-in controllers (Deployment, ReplicaSet, StatefulSet, DaemonSet, Job). Uses leader election in HA. |
| **cloud-controller-manager** | Integrates with cloud provider APIs (load balancers, storage, node lifecycle). Omitted for on-premises clusters. |

### Worker Node Components

| Component | Role |
|-----------|------|
| **kubelet** | Agent on each node. Receives PodSpecs from the API server and ensures the described containers are running and healthy. |
| **kube-proxy** | Network proxy. Maintains iptables / IPVS rules to implement Service routing and load balancing. |
| **Container runtime** | Runs the actual containers. Supported: containerd, CRI-O, Docker Engine (via shim). |

---

## Core Objects

### Workloads

| Object | Use case | Pod identity | Persistent storage |
|--------|----------|-------------|-------------------|
| **Pod** | Smallest unit; one or more tightly-coupled containers sharing a network namespace. Rarely created directly. | Ephemeral | No |
| **Deployment** | Stateless applications (web apps, APIs). Manages a ReplicaSet; handles rolling updates and rollbacks. | Replaceable | No |
| **ReplicaSet** | Ensures N identical pod replicas run. Managed by Deployment — rarely used directly. | Replaceable | No |
| **StatefulSet** | Stateful workloads (databases, caches, message queues). Each pod gets a stable ordinal name (`mysql-0`, `mysql-1`) and a dedicated PVC. | Stable | Yes — per pod |
| **DaemonSet** | Runs exactly one pod per node (or per selected nodes). Used for cluster infrastructure: CNI plugins, log collectors, monitoring agents. | One per node | Optional |
| **Job** | One-off batch work. Runs pods to completion; retries on failure. | Temporary | Optional |
| **CronJob** | Scheduled Jobs. Uses cron syntax. Used for backups, periodic processing, cache clearing. | Temporary | Optional |

**Decision tree:**

```
Stateless app?          → Deployment
Stateful (DB, queue)?  → StatefulSet
Must run on every node? → DaemonSet
One-off task?           → Job
Repeating task?         → CronJob
```

### Networking Objects

| Object | Scope | Purpose |
|--------|-------|---------|
| **Service** | In-cluster | Stable IP + DNS name for a set of pods. Implements load balancing via kube-proxy. |
| **Ingress** | External HTTP/S | Routes external HTTP/HTTPS traffic to Services. Requires an Ingress controller (NGINX, Traefik, Envoy). Handles TLS termination, path-based routing, virtual hosting. |
| **NetworkPolicy** | In-cluster | Firewall rules — controls which pods can communicate with which. Default: all pods can reach all other pods. |

**Service types:**

| Type | Visibility | Use case |
|------|-----------|----------|
| `ClusterIP` (default) | Internal only | Service-to-service communication (databases, caches) |
| `NodePort` | External via `NodeIP:port` (30000–32767) | Simple external access for dev/testing |
| `LoadBalancer` | External via cloud load balancer | Production external access on GKE/EKS/AKS |
| `ExternalName` | DNS alias | Proxy to external services outside the cluster |

Service DNS format: `<service-name>.<namespace>.svc.cluster.local`

### Configuration and Storage Objects

| Object | Purpose |
|--------|---------|
| **ConfigMap** | Non-confidential config as key-value pairs. Mounted as env vars, CLI args, or volume files. Decouples config from image. |
| **Secret** | Sensitive config (passwords, tokens, TLS certs). Base64-encoded at rest — **not encrypted by default**. Enable EncryptionConfiguration for AES encryption of Secrets in etcd. |
| **PersistentVolume (PV)** | Admin-provisioned storage resource in the cluster. |
| **PersistentVolumeClaim (PVC)** | Pod's request for storage. Kubernetes binds the PVC to a matching PV. StatefulSets create PVCs automatically per pod via `volumeClaimTemplates`. |
| **Namespace** | Virtual cluster partition. Isolates resources between teams, environments, or projects. |

---

## Key Operations

### Rolling Update (Deployment)

```bash
kubectl set image deployment/my-app container=image:v2
# Kubernetes replaces pods gradually — zero downtime
kubectl rollout status deployment/my-app
kubectl rollout undo deployment/my-app          # roll back
kubectl rollout history deployment/my-app       # see revision history
```

### Scaling

```bash
kubectl scale deployment/my-app --replicas=5    # manual scale
# Horizontal Pod Autoscaler (HPA) — automatic:
kubectl autoscale deployment/my-app --min=2 --max=10 --cpu-percent=70
```

### Essential kubectl Commands

```bash
kubectl get pods -n <namespace>                 # list pods
kubectl describe pod <pod-name>                 # detailed pod info
kubectl logs <pod-name> -c <container>          # view logs
kubectl exec -it <pod-name> -- /bin/sh          # shell into pod
kubectl apply -f manifest.yaml                  # apply manifest
kubectl delete -f manifest.yaml                 # delete resources
kubectl port-forward svc/<svc-name> 8080:80     # local port forward
kubectl get events --sort-by=.lastTimestamp     # debug events
```

---

## A Minimal Deployment Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:1.0
        ports:
        - containerPort: 8080
        env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "500m"
            memory: "512Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: my-app-svc
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP
```

---

## Security

### RBAC (Role-Based Access Control)

RBAC controls who can do what to which resources. Four objects:

| Object | Scope | Purpose |
|--------|-------|---------|
| **Role** | Namespace | Grants permissions within a namespace |
| **ClusterRole** | Cluster-wide | Grants permissions across all namespaces |
| **RoleBinding** | Namespace | Binds a Role to a user/ServiceAccount |
| **ClusterRoleBinding** | Cluster-wide | Binds a ClusterRole cluster-wide |

**Principle of least privilege** — assign the minimum permissions needed, prefer `Role + RoleBinding` over `ClusterRole + ClusterRoleBinding`.

### Secrets Hardening

- Secrets are base64-encoded, **not encrypted**, in etcd by default
- Enable `EncryptionConfiguration` with AES-GCM to encrypt at rest
- Use RBAC to restrict `get`/`list`/`watch` on Secrets — even `list` leaks values
- Set `automountServiceAccountToken: false` on pods that don't call the API
- Prefer external secret stores: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault (via External Secrets Operator)

### Pod Security Standards

Three built-in policy levels applied per namespace:

| Level | Restriction |
|-------|-------------|
| **Privileged** | No restrictions (system namespaces only) |
| **Baseline** | Prevents known privilege escalations |
| **Restricted** | Follows pod hardening best practices |

---

## Helm — Kubernetes Package Manager

Helm is to Kubernetes what `apt` / `yum` is to Linux. It packages Kubernetes manifests into versioned, templated **charts** for repeatable, environment-aware deployments.

### Chart Structure

```
my-chart/
├── Chart.yaml          # metadata: name, version, dependencies
├── values.yaml         # default config values
├── templates/          # Go-templated Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
└── charts/             # sub-chart dependencies
```

### How It Works

1. `values.yaml` holds defaults (`image.tag`, `replicaCount`, `ingress.host`)
2. Templates reference values via Go template syntax: `{{ .Values.image.tag }}`
3. `helm install my-release ./my-chart` renders templates + values → applies YAML to cluster
4. Each install creates a **release** with a version history
5. `helm upgrade my-release ./my-chart --set image.tag=v2` — zero-downtime update
6. `helm rollback my-release 1` — roll back to revision 1

Helm 4.0 (released November 2025, KubeCon NA) introduced **server-side apply** — delegates manifest merge logic to the Kubernetes API server, resolving field-ownership conflicts correctly.

---

## Managed Kubernetes Services

Self-managing a control plane in production is operationally expensive. Managed services handle control plane provisioning, upgrades, and HA automatically.

| Provider | Service | Best suited for | Version cadence |
|----------|---------|-----------------|----------------|
| Google Cloud | **GKE** | Performance, automation, advanced scaling, built-in observability | Fastest (~2 weeks to new K8s version) |
| AWS | **EKS** | AWS-native workloads; deep IAM and VPC integration | 4–8 weeks |
| Azure | **AKS** | Microsoft/Azure shops; cost-effective; strong AD integration | 3–6 weeks |

All three supported Kubernetes 1.33 as of October 2025. All three handle: control plane HA, node auto-provisioning, managed upgrades, and cloud load balancer integration.

---

## Kubernetes vs Docker Compose

| Dimension | Docker Compose | Kubernetes |
|-----------|---------------|------------|
| Host scope | Single machine | Multiple nodes |
| Auto-scaling | ❌ Manual only | ✅ HPA + Cluster Autoscaler |
| Self-healing | Restart on failure only | Full cluster-level recovery |
| Rolling updates | ❌ | ✅ Built-in |
| Service discovery | Container names (DNS) | Service DNS + kube-proxy |
| Config overhead | ~50 MB, single YAML | ~2 GB control plane, multi-manifest |
| Learning curve | Low | High |
| **Best for** | Local dev, CI, single-host | Production, microservices, HA |

**Rule of thumb:** use Compose for development and single-host deployments; graduate to Kubernetes when you need multi-node HA, auto-scaling, or production-grade self-healing.

---

## Common Pitfalls

- **No resource requests/limits** — pods can starve other workloads; always set `resources.requests` and `resources.limits`
- **Secrets are not encrypted by default** — enable EncryptionConfiguration
- **Running as root** — set `securityContext.runAsNonRoot: true`
- **Skipping readiness/liveness probes** — traffic routed to pods that aren't ready; health checks are mandatory in production
- **Direct pod creation** — pods are ephemeral; always use a workload controller

---

## Related Pages

- [[concepts/docker-compose]] — single-host alternative; complementary for local dev
- [[concepts/github-actions-cicd]] — CI/CD pipelines that deploy to Kubernetes
- [[concepts/nginx-reverse-proxy-and-tls]] — Ingress controllers commonly use NGINX
- [[synthesis/research-kubernetes]]
