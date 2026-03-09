# Kubernetes Learning Roadmap — Overview

> Mục tiêu: Hiểu tổng quan K8s, deploy local được, maintain dự án công ty.

```
Phương pháp: DO → SEE → ASK → READ → DO (thực hành trước, lý thuyết sau)
```

---

## Phase 1 — Nền tảng (1-2 tuần)

- [ ] Cài minikube + kubectl
- [ ] Khởi tạo cluster (`minikube start`)
- [ ] Tạo Deployment đầu tiên (`kubectl create deployment`)
- [ ] Hiểu Pod — xóa thử, xem self-healing
- [ ] Hiểu ReplicaSet — scale lên 3 replicas
- [ ] Hiểu Service — expose app ra ngoài, truy cập browser
- [ ] Xem kiến trúc cluster (`kubectl get all`, `cluster-info`)
- [ ] Đọc docs Concepts sau khi đã trải nghiệm

---

## Phase 2 — Thực hành Local nâng cao (2-3 tuần)

- [ ] Thành thạo kubectl: `get`, `describe`, `logs`, `exec`, `apply`, `delete`
- [ ] Viết YAML manifests (Deployment, Service)
- [ ] ConfigMap — inject biến môi trường vào Pod
- [ ] Secret — quản lý dữ liệu nhạy cảm (DB password)
- [ ] Namespace — tách biệt môi trường dev/staging
- [ ] **Bài tập**: Deploy web app + PostgreSQL trên minikube
- [ ] **Bài tập**: Expose bằng NodePort, test load balancing với 3 replicas

---

## Phase 3 — Maintain dự án công ty (2-3 tuần)

- [ ] Đọc hiểu manifests / Helm charts của công ty
- [ ] Helm cơ bản: `install`, `upgrade`, `list`, `values`
- [ ] Hiểu CI/CD pipeline: build image → push registry → deploy K8s
- [ ] Resource requests & limits (CPU, memory)
- [ ] Health checks: liveness probe, readiness probe
- [ ] Monitoring & Logging: `kubectl logs`, `kubectl top`
- [ ] Troubleshooting: CrashLoopBackOff, Pending, ImagePullBackOff, OOMKilled
- [ ] **Bài tập**: Deploy 1 service công ty lên local, giả lập lỗi và debug

---

## Phase 4 — Nâng cao (học khi gặp bài toán thực tế)

| Bài toán | Học thêm |
|---|---|
| Traffic tăng đột biến | HPA (Horizontal Pod Autoscaler) |
| Chạy DB/stateful app trên K8s | StatefulSet, PersistentVolume, StorageClass |
| Kiểm soát quyền truy cập | RBAC, ServiceAccount |
| Kiểm soát traffic giữa services | Network Policy, Ingress nâng cao |
| GitOps workflow | ArgoCD / FluxCD |
| Deploy strategy phức tạp | Canary, Blue-Green |
| Scheduling tối ưu | Taints, Tolerations, Node Affinity |
| Mở rộng K8s | CRDs, Custom Controllers, Operators |
| Quản lý nhiều cluster | Multi-Cluster Management |

---

## Tài liệu tham khảo

- [Kubernetes Official Docs](https://kubernetes.io/docs/)
- [Minikube Getting Started](https://minikube.sigs.k8s.io/docs/start/)
- [Helm Docs](https://helm.sh/docs/)
- [Kubernetes Roadmap](https://roadmap.sh/kubernetes)
- Video: TechWorld with Nana — Kubernetes Tutorial for Beginners
- Video: Fireship — Kubernetes in 100 Seconds
