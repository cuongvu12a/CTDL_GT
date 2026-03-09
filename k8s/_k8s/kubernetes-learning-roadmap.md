# Kubernetes Learning Roadmap

> Mục tiêu: Hiểu tổng quan K8s, deploy local được, maintain dự án công ty. Học sâu sau.

---

## Phương pháp học: Thực hành trước — Lý thuyết sau

### Vấn đề với cách học truyền thống

```
Truyền thống:   Đọc docs 3 ngày → Hiểu mơ hồ → Quên 70% → Bắt đầu làm → Đọc lại
Thực hành trước: Làm thử → Thấy kết quả → Đặt câu hỏi "tại sao?" → Đọc docs → Hiểu sâu
```

Bản chất là **tạo trải nghiệm trước, rồi gắn kiến thức vào trải nghiệm đó**. Não người nhớ tốt hơn khi kiến thức được gắn với một hành động cụ thể đã làm.

### Pattern lặp lại cho mỗi khái niệm mới

```
 DO something (kubectl command)
   ↓
 SEE the result (output, behavior)
   ↓
 ASK "why?" / "what happened?"
   ↓
 READ docs for that specific concept
   ↓
 DO again with understanding
```

---

## Phase 1 — Nền tảng (1-2 tuần)

> Mục tiêu: Hiểu K8s là gì, tại sao cần, và các khái niệm cốt lõi — thông qua thực hành ngay.

### 1.1 Cài minikube ngay lập tức (15 phút)

Không cần hiểu K8s là gì. Cứ cài đã.

```bash
# macOS
brew install minikube kubectl

# Khởi tạo cluster
minikube start

# Xem có gì trong cluster
kubectl get nodes
kubectl get pods --all-namespaces
```

Lúc này chưa hiểu `node`, `pod`, `namespace` là gì — **không sao cả**. Bạn đã có 1 cluster đang chạy để sờ vào.

### 1.2 Deploy thứ gì đó ngay (10 phút)

```bash
# Tạo 1 deployment chạy nginx
kubectl create deployment my-web --image=nginx

# Xem nó
kubectl get pods
```

Output sẽ kiểu:

```
NAME                      READY   STATUS    RESTARTS   AGE
my-web-6b7b4f4b4-x9kzl   1/1     Running   0          30s
```

**Câu hỏi để tự đặt:**

- "my-web-6b7b4f4b4-x9kzl" cái tên dài vậy là gì? → Đó là **Pod**, đơn vị nhỏ nhất trong K8s
- Tại sao tên có đoạn random "x9kzl"? → Vì K8s tự tạo Pod, mỗi Pod có tên unique
- "1/1 Running" nghĩa là gì? → 1 container trong Pod, đang chạy

→ Trải nghiệm Pod trước, rồi mới hiểu Pod là gì.

### 1.3 Phá thử để hiểu Self-Healing (5 phút)

```bash
# Xóa pod đang chạy
kubectl delete pod my-web-6b7b4f4b4-x9kzl

# Xem lại ngay
kubectl get pods
```

Output:

```
NAME                      READY   STATUS    RESTARTS   AGE
my-web-6b7b4f4b4-abc12   1/1     Running   0          5s    ← Pod MỚI tự xuất hiện!
```

**Câu hỏi:**

- "Tại sao mình xóa rồi mà nó lại xuất hiện?" → Vì **Deployment** đảm bảo luôn có đủ số Pod mong muốn
- Đây chính là khái niệm **desired state** — thứ mà docs giải thích dài dòng, nhưng vừa thấy tận mắt trong 5 giây

### 1.4 Scale lên để hiểu ReplicaSet (5 phút)

```bash
# Scale lên 3 pods
kubectl scale deployment my-web --replicas=3

kubectl get pods
```

Output:

```
NAME                      READY   STATUS    RESTARTS   AGE
my-web-6b7b4f4b4-abc12   1/1     Running   0          2m
my-web-6b7b4f4b4-def34   1/1     Running   0          5s
my-web-6b7b4f4b4-ghi56   1/1     Running   0          5s
```

**Câu hỏi:** "Ai quản lý việc tạo 3 Pods này?" → **ReplicaSet**. Giờ mới đọc docs về ReplicaSet — đã có hình ảnh cụ thể trong đầu.

### 1.5 Expose ra ngoài để hiểu Service (5 phút)

```bash
# Expose deployment
kubectl expose deployment my-web --type=NodePort --port=80

# Lấy URL truy cập
minikube service my-web --url
```

Output: `http://192.168.49.2:31234`

Mở browser → thấy trang Nginx.

**Câu hỏi:**

- "3 Pods đang chạy, mình truy cập vào cái nào?" → **Service** tự load balance
- "Port 31234 ở đâu ra?" → **NodePort** tự assign random port
- "Nếu 1 Pod chết, mình có bị mất kết nối không?" → Không, Service tự route sang Pod khác

→ Vừa hiểu Service, Load Balancing, Self-healing qua 1 trải nghiệm thực tế.

### 1.6 Xem kiến trúc bằng mắt (5 phút)

```bash
# Xem tất cả resource liên quan
kubectl get all

# Xem chi tiết 1 pod
kubectl describe pod <tên-pod>

# Xem kiến trúc cluster
kubectl get nodes -o wide
kubectl cluster-info
```

**Đến đây mới mở docs đọc kiến trúc K8s** — lúc này đọc "Control Plane quản lý desired state" sẽ nhớ ngay: "À, đúng rồi, lúc mình xóa Pod mà nó tự tạo lại — đó là Control Plane làm."

### 1.7 Tài liệu đọc sau khi đã thực hành

- Kubernetes official docs: [Concepts section](https://kubernetes.io/docs/concepts/)
- Video: "Kubernetes in 100 Seconds" → "Kubernetes Explained" (Fireship, TechWorld with Nana)
- So sánh với Docker Compose để hiểu rõ bài toán orchestration

---

## Phase 2 — Thực hành Local nâng cao (2-3 tuần)

> Mục tiêu: Tự tay deploy ứng dụng hoàn chỉnh lên K8s local, quen với kubectl và YAML.

### 2.1 kubectl cơ bản

Các command dùng hàng ngày:

```bash
kubectl get <resource>          # Liệt kê resources
kubectl describe <resource>     # Xem chi tiết
kubectl logs <pod>              # Xem logs
kubectl exec -it <pod> -- bash  # Vào bên trong Pod
kubectl apply -f <file.yaml>    # Apply manifest
kubectl delete -f <file.yaml>   # Xóa resource
```

### 2.2 Viết YAML manifests

Hiểu cấu trúc cơ bản:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-web
  namespace: default
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-web
  template:
    metadata:
      labels:
        app: my-web
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80
```

### 2.3 ConfigMap & Secret

```bash
# DO: Tạo ConfigMap
kubectl create configmap my-config --from-literal=APP_ENV=production

# SEE: Xem nội dung
kubectl get configmap my-config -o yaml

# ASK: "Làm sao inject cái này vào Pod?"

# READ: Docs về envFrom, volumeMounts cho ConfigMap

# DO: Viết YAML gắn ConfigMap vào Pod, apply, exec vào Pod kiểm tra
kubectl exec -it <pod> -- env | grep APP_ENV
```

### 2.4 Namespace

```bash
# Tạo namespace cho dev environment
kubectl create namespace dev

# Deploy vào namespace cụ thể
kubectl apply -f deployment.yaml -n dev

# Xem pods trong namespace
kubectl get pods -n dev
```

### 2.5 Bài tập thực hành

1. Deploy 1 web app (React/Node) + 1 database (PostgreSQL) trên minikube
2. Expose web app ra ngoài bằng Service NodePort
3. Sử dụng ConfigMap cho biến môi trường, Secret cho DB password
4. Scale `kubectl scale deployment --replicas=3` và kiểm tra load balancing
5. Thử xóa Pod, xem K8s tự healing

---

## Phase 3 — Maintain dự án công ty (2-3 tuần)

> Mục tiêu: Đọc hiểu và vận hành K8s setup hiện có của công ty.

### 3.1 Đọc hiểu manifests/Helm charts hiện có

- Clone setup K8s của công ty
- Đọc từng file manifest, đối chiếu với kiến thức từ Phase 1-2
- Hiểu flow: request từ client → Ingress → Service → Pod

### 3.2 Helm cơ bản

```bash
helm install <release> <chart>      # Cài đặt
helm upgrade <release> <chart>      # Cập nhật
helm list                            # Liệt kê releases
helm values <chart>                  # Xem config mặc định
```

### 3.3 CI/CD integration

Hiểu pipeline hiện tại:

```
Push code → CI build Docker image → Push lên Registry → CD deploy lên K8s
```

### 3.4 Resource requests & limits

```yaml
resources:
  requests:
    cpu: "100m"      # Minimum CPU cần
    memory: "128Mi"  # Minimum memory cần
  limits:
    cpu: "500m"      # Maximum CPU được dùng
    memory: "512Mi"  # Maximum memory — vượt sẽ bị OOMKilled
```

### 3.5 Health checks

```yaml
livenessProbe:       # Pod có đang sống không? Fail → restart Pod
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:      # Pod có sẵn sàng nhận traffic không? Fail → loại khỏi Service
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### 3.6 Monitoring & Logging cơ bản

```bash
# Xem logs
kubectl logs <pod>
kubectl logs <pod> --previous       # Logs của container trước (nếu bị restart)
kubectl logs -f <pod>               # Follow logs realtime

# Xem resource usage
kubectl top pods
kubectl top nodes
```

### 3.7 Troubleshooting phổ biến

| Trạng thái | Nguyên nhân thường gặp | Cách debug |
|---|---|---|
| `CrashLoopBackOff` | App crash liên tục | `kubectl logs <pod> --previous` |
| `Pending` | Không đủ resource trên node | `kubectl describe pod <pod>` xem Events |
| `ImagePullBackOff` | Sai image name hoặc thiếu credentials | Kiểm tra image name, imagePullSecrets |
| `OOMKilled` | Vượt memory limit | Tăng limit hoặc optimize app |
| Service không kết nối | Sai selector hoặc port | `kubectl describe service`, kiểm tra labels match |

### 3.8 Bài tập thực hành

1. Clone setup K8s của công ty về local, đọc hiểu từng file manifest
2. Tự deploy 1 service của công ty lên local cluster
3. Giả lập lỗi (kill pod, sai config) → debug và fix

---

## Phase 4 — Nâng cao dần (học khi cần)

> Mục tiêu: Mở rộng kiến thức theo nhu cầu thực tế gặp phải. Không cần học trước.

| Khi gặp bài toán... | Học thêm... |
|---|---|
| Traffic tăng đột biến | HPA (Horizontal Pod Autoscaler) |
| Cần chạy DB/stateful app trên K8s | StatefulSet, PersistentVolume, StorageClass |
| Cần kiểm soát ai được làm gì | RBAC, ServiceAccount |
| Cần kiểm soát traffic giữa services | Network Policy, Ingress nâng cao |
| Muốn GitOps workflow | ArgoCD hoặc FluxCD |
| Deploy strategy phức tạp | Canary, Blue-Green Deployment |
| Scheduling tối ưu | Taints, Tolerations, Node Affinity |
| Mở rộng K8s | CRDs, Custom Controllers, Operators |
| Quản lý nhiều cluster | Multi-Cluster Management |

---

## So sánh với Roadmap gốc (roadmap.sh/kubernetes)

```
Roadmap gốc:  14 sections, ~50+ topics    → Comprehensive nhưng overwhelming
Lộ trình này:  4 phases,  ~20 topics core  → Focused, thực tế, đủ để maintain
```

## Tài liệu tham khảo

- [Kubernetes Official Docs](https://kubernetes.io/docs/)
- [Kubernetes Roadmap](https://roadmap.sh/kubernetes)
- [Minikube Getting Started](https://minikube.sigs.k8s.io/docs/start/)
- [Helm Docs](https://helm.sh/docs/)
- Video: TechWorld with Nana - Kubernetes Tutorial for Beginners
- Video: Fireship - Kubernetes in 100 Seconds
