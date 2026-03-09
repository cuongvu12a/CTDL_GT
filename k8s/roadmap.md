# Lộ Trình Học Kubernetes - Từ Người Mới Đến Chuyên Gia

> **Định hướng: Thực hành trước, lý thuyết sau.**
> Mỗi giai đoạn đều có bài tập thực hành kèm lời giải chi tiết.
> Cập nhật theo Kubernetes v1.32 - v1.35 (2024-2026).

---

## Mục Lục

- [Giai đoạn 0: Chuẩn Bị Môi Trường & Công Cụ](#giai-đoạn-0-chuẩn-bị-môi-trường--công-cụ)
- [Giai đoạn 1: Hands-on Đầu Tiên - Pod, Container & kubectl](#giai-đoạn-1-hands-on-đầu-tiên---pod-container--kubectl)
- [Giai đoạn 2: Networking Cơ Bản - Service & Giao Tiếp Giữa Các Pod](#giai-đoạn-2-networking-cơ-bản---service--giao-tiếp-giữa-các-pod)
- [Giai đoạn 3: Quản Lý Ứng Dụng - Deployment, Scaling & Updates](#giai-đoạn-3-quản-lý-ứng-dụng---deployment-scaling--updates)
- [Giai đoạn 4: Cấu Hình & Bảo Mật Ứng Dụng](#giai-đoạn-4-cấu-hình--bảo-mật-ứng-dụng)
- [Giai đoạn 5: Lưu Trữ Dữ Liệu - Persistent Storage](#giai-đoạn-5-lưu-trữ-dữ-liệu---persistent-storage)
- [Giai đoạn 6: Workload Nâng Cao - Job, CronJob, DaemonSet, StatefulSet](#giai-đoạn-6-workload-nâng-cao---job-cronjob-daemonset-statefulset)
- [Giai đoạn 7: Networking Nâng Cao - Ingress, Gateway API & DNS](#giai-đoạn-7-networking-nâng-cao---ingress-gateway-api--dns)
- [Giai đoạn 8: Scheduling & Quản Lý Tài Nguyên](#giai-đoạn-8-scheduling--quản-lý-tài-nguyên)
- [Giai đoạn 9: Observability - Monitoring, Logging & Troubleshooting](#giai-đoạn-9-observability---monitoring-logging--troubleshooting)
- [Giai đoạn 10: Bảo Mật Cụm - RBAC, Network Policy, Pod Security](#giai-đoạn-10-bảo-mật-cụm---rbac-network-policy-pod-security)
- [Giai đoạn 11: Helm, Kustomize & Quản Lý Package](#giai-đoạn-11-helm-kustomize--quản-lý-package)
- [Giai đoạn 12: CI/CD & GitOps](#giai-đoạn-12-cicd--gitops)
- [Giai đoạn 13: Chuyên Gia - CRD, Operator, Service Mesh & Multi-Cluster](#giai-đoạn-13-chuyên-gia---crd-operator-service-mesh--multi-cluster)
- [Giai đoạn 14: Managed Kubernetes & Production Readiness](#giai-đoạn-14-managed-kubernetes--production-readiness)
- [Phụ Lục A: Kiến Trúc Kubernetes (Lý Thuyết Tham Khảo)](#phụ-lục-a-kiến-trúc-kubernetes-lý-thuyết-tham-khảo)
- [Phụ Lục B: Lộ Trình Chứng Chỉ CKA/CKAD/CKS](#phụ-lục-b-lộ-trình-chứng-chỉ-ckackadcks)
- [Phụ Lục C: Công Cụ Hỗ Trợ](#phụ-lục-c-công-cụ-hỗ-trợ)

---

## Giai đoạn 0: Chuẩn Bị Môi Trường & Công Cụ

### Mục tiêu
Cài đặt xong môi trường lab trên máy cá nhân, sẵn sàng thực hành ngay.

### Kiến thức tiên quyết
- **Docker cơ bản**: build image, run container, Dockerfile, docker-compose.
- **Linux cơ bản**: terminal, file system, process, networking (curl, netstat, ss).
- **YAML**: cú pháp, indentation, list, map.

### Cài đặt

| Công cụ | Mục đích | Cài đặt |
|---------|---------|---------|
| **Docker Desktop** | Container runtime | `brew install --cask docker` |
| **Minikube** | Cụm K8s 1 node trên local | `brew install minikube` |
| **kubectl** | CLI tương tác với K8s | `brew install kubectl` |
| **k9s** | TUI quản lý cụm trực quan | `brew install k9s` |
| **Helm** | Package manager cho K8s | `brew install helm` |
| **kubectx + kubens** | Chuyển đổi context/namespace nhanh | `brew install kubectx` |

### Bài tập 0.1: Khởi tạo cụm đầu tiên

**Yêu cầu:** Tạo cụm Minikube, xác nhận hoạt động, khám phá dashboard.

**Lời giải:**

```bash
# Khởi tạo cụm với 2 CPU và 4GB RAM
minikube start --cpus=2 --memory=4096 --driver=docker

# Kiểm tra trạng thái cụm
minikube status

# Xem thông tin cụm
kubectl cluster-info

# Xem các node
kubectl get nodes

# Xem tất cả pod trong mọi namespace (để hiểu K8s chạy gì sẵn)
kubectl get pods -A

# Mở dashboard (chạy trên tab riêng)
minikube dashboard

# Xem các namespace có sẵn
kubectl get namespaces
```

**Kết quả mong đợi:** Cụm chạy thành công, thấy 1 node `Ready`, dashboard mở trên trình duyệt, các namespace mặc định: `default`, `kube-system`, `kube-public`, `kube-node-lease`.

---

## Giai đoạn 1: Hands-on Đầu Tiên - Pod, Container & kubectl

### Mục tiêu
Chạy được ứng dụng đầu tiên trên K8s, hiểu Pod là gì qua thực hành.

### Khái niệm cốt lõi (học qua thực hành)
- **Pod**: Đơn vị nhỏ nhất trong K8s, bao quanh 1 hoặc nhiều container.
- **kubectl**: Công cụ dòng lệnh để tương tác với cụm.
- **YAML manifest**: File mô tả trạng thái mong muốn (desired state) của tài nguyên.

### Bài tập 1.1: Pod đầu tiên - Imperative vs Declarative

**Yêu cầu:** Tạo Pod chạy nginx bằng 2 cách: lệnh trực tiếp và file YAML.

**Lời giải:**

```bash
# Cách 1: Imperative (lệnh trực tiếp) - nhanh, dùng để test
kubectl run my-nginx --image=nginx:1.27 --port=80

# Xem pod đã tạo
kubectl get pods
kubectl get pods -o wide  # thêm thông tin IP, Node

# Xem chi tiết pod
kubectl describe pod my-nginx

# Xem logs
kubectl logs my-nginx

# Truy cập vào shell của container
kubectl exec -it my-nginx -- /bin/bash
# Bên trong container:
curl localhost:80
exit

# Xóa pod
kubectl delete pod my-nginx
```

```bash
# Cách 2: Declarative (file YAML) - chuẩn production
cat <<'EOF' > pod-nginx.yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-nginx
  labels:
    app: nginx
    env: dev
spec:
  containers:
  - name: nginx
    image: nginx:1.27
    ports:
    - containerPort: 80
    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "250m"
        memory: "256Mi"
EOF

kubectl apply -f pod-nginx.yaml
kubectl get pods --show-labels
```

### Bài tập 1.2: Multi-container Pod

**Yêu cầu:** Tạo Pod có 2 container: nginx (web server) và busybox (sidecar ghi log), chia sẻ volume giữa chúng.

**Lời giải:**

```yaml
# multi-container-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-with-logger
  labels:
    app: web-logger
spec:
  containers:
  - name: nginx
    image: nginx:1.27
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/nginx

  - name: log-reader
    image: busybox:1.36
    command: ["sh", "-c", "tail -f /logs/access.log"]
    volumeMounts:
    - name: shared-logs
      mountPath: /logs

  volumes:
  - name: shared-logs
    emptyDir: {}
```

```bash
kubectl apply -f multi-container-pod.yaml

# Xem logs từng container
kubectl logs web-with-logger -c nginx
kubectl logs web-with-logger -c log-reader

# Port-forward để test
kubectl port-forward web-with-logger 8080:80
# Mở tab khác: curl http://localhost:8080

# Xem logs sau khi truy cập
kubectl logs web-with-logger -c log-reader
```

### Bài tập 1.3: Init Container

**Yêu cầu:** Tạo Pod có init container tải file cấu hình trước khi app chính khởi động.

**Lời giải:**

```yaml
# init-container-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-init
spec:
  initContainers:
  - name: init-config
    image: busybox:1.36
    command: ["sh", "-c", "echo 'Welcome to K8s!' > /work-dir/index.html"]
    volumeMounts:
    - name: workdir
      mountPath: /work-dir

  containers:
  - name: nginx
    image: nginx:1.27
    ports:
    - containerPort: 80
    volumeMounts:
    - name: workdir
      mountPath: /usr/share/nginx/html

  volumes:
  - name: workdir
    emptyDir: {}
```

```bash
kubectl apply -f init-container-pod.yaml

# Theo dõi quá trình khởi tạo
kubectl get pod app-with-init -w

# Khi pod Ready, test nội dung
kubectl port-forward app-with-init 8080:80
curl http://localhost:8080
# Output: "Welcome to K8s!"
```

### Bài tập 1.4: Health Checks - Liveness, Readiness & Startup Probes

**Yêu cầu:** Tạo Pod với đầy đủ 3 loại probe. Mô phỏng lỗi liveness để quan sát K8s tự restart.

**Lời giải:**

```yaml
# probes-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-probes
spec:
  containers:
  - name: app
    image: nginx:1.27
    ports:
    - containerPort: 80

    # Startup Probe: kiểm tra app đã khởi động chưa
    # K8s sẽ không chạy liveness/readiness cho đến khi startup thành công
    startupProbe:
      httpGet:
        path: /
        port: 80
      failureThreshold: 30
      periodSeconds: 2

    # Liveness Probe: app còn sống không? Fail => restart container
    livenessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 10
      failureThreshold: 3

    # Readiness Probe: app sẵn sàng nhận traffic không? Fail => loại khỏi Service
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 3
      periodSeconds: 5
```

```bash
kubectl apply -f probes-pod.yaml
kubectl describe pod app-with-probes | grep -A 5 "Liveness\|Readiness\|Startup"

# Mô phỏng lỗi liveness: xóa file mặc định của nginx
kubectl exec app-with-probes -- rm /usr/share/nginx/html/index.html

# Quan sát pod restart
kubectl get pod app-with-probes -w
# Sau vài lần probe fail, RESTARTS sẽ tăng lên
kubectl describe pod app-with-probes | grep -A 3 "Last State"
```

### Bài tập 1.5: Sidecar Container (Kubernetes v1.29+)

**Yêu cầu:** Sử dụng native sidecar container (GA từ v1.33) để chạy log collector bên cạnh app chính.

**Lời giải:**

```yaml
# sidecar-container.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecar
spec:
  initContainers:
  # Native sidecar: init container với restartPolicy: Always
  - name: log-collector
    image: busybox:1.36
    restartPolicy: Always  # <-- Đây là điểm khác biệt: biến thành sidecar
    command: ["sh", "-c", "tail -f /var/log/app/app.log"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app

  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "while true; do echo \"$(date) - App running\" >> /var/log/app/app.log; sleep 5; done"]
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app

  volumes:
  - name: log-volume
    emptyDir: {}
```

```bash
kubectl apply -f sidecar-container.yaml

# Sidecar khởi động trước app và chạy song song
kubectl get pod app-with-sidecar -w
kubectl logs app-with-sidecar -c log-collector -f
```

### Các lệnh kubectl quan trọng cần nhớ

```bash
# Tạo YAML mẫu nhanh (không tạo thật, chỉ in ra YAML)
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml

# Debug pod đang lỗi
kubectl describe pod <tên-pod>
kubectl logs <tên-pod> --previous  # logs của container trước khi restart

# Copy file vào/ra container
kubectl cp local-file.txt <pod>:/path/in/container
kubectl cp <pod>:/path/in/container local-file.txt

# Xem events gần đây
kubectl get events --sort-by='.lastTimestamp'

# Ephemeral debug container (K8s 1.25+)
kubectl debug -it <pod> --image=busybox -- sh
```

---

## Giai đoạn 2: Networking Cơ Bản - Service & Giao Tiếp Giữa Các Pod

### Mục tiêu
Hiểu cách các Pod giao tiếp với nhau và expose ra bên ngoài thông qua Service.

### Khái niệm cốt lõi
- **Service**: Cung cấp IP tĩnh và DNS name cho một nhóm Pod, tự động cân bằng tải.
- **ClusterIP**: Chỉ truy cập nội bộ trong cụm (mặc định).
- **NodePort**: Mở cổng trên mỗi Node (30000-32767).
- **LoadBalancer**: Tích hợp cloud load balancer.
- **Label Selector**: Cách Service "tìm" đúng Pod.

### Bài tập 2.1: ClusterIP Service

**Yêu cầu:** Tạo 2 Pod nginx, tạo ClusterIP Service, chứng minh Service cân bằng tải giữa các Pod.

**Lời giải:**

```yaml
# backend-pods.yaml
apiVersion: v1
kind: Pod
metadata:
  name: backend-1
  labels:
    app: backend
    version: v1
spec:
  containers:
  - name: nginx
    image: nginx:1.27
    ports:
    - containerPort: 80
    command: ["sh", "-c", "echo 'Response from backend-1' > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"]
---
apiVersion: v1
kind: Pod
metadata:
  name: backend-2
  labels:
    app: backend
    version: v1
spec:
  containers:
  - name: nginx
    image: nginx:1.27
    ports:
    - containerPort: 80
    command: ["sh", "-c", "echo 'Response from backend-2' > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"]
```

```yaml
# clusterip-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-svc
spec:
  type: ClusterIP
  selector:
    app: backend   # Chọn tất cả Pod có label app=backend
  ports:
  - port: 80         # Port của Service
    targetPort: 80    # Port của container
    protocol: TCP
```

```bash
kubectl apply -f backend-pods.yaml
kubectl apply -f clusterip-service.yaml

# Xem Service và Endpoints
kubectl get svc backend-svc
kubectl get endpoints backend-svc
# => Thấy 2 IP (của 2 Pod)

# Test cân bằng tải từ bên trong cụm
kubectl run test-client --image=busybox:1.36 --rm -it -- sh
# Bên trong container:
for i in $(seq 1 10); do wget -qO- http://backend-svc; done
# => Kết quả xen kẽ "backend-1" và "backend-2"
exit
```

### Bài tập 2.2: NodePort Service

**Yêu cầu:** Expose ứng dụng ra ngoài cụm bằng NodePort.

**Lời giải:**

```yaml
# nodeport-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-nodeport
spec:
  type: NodePort
  selector:
    app: backend
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080   # Cố định port (hoặc bỏ để K8s tự chọn)
```

```bash
kubectl apply -f nodeport-service.yaml

# Lấy URL truy cập (Minikube)
minikube service backend-nodeport --url
# => http://192.168.49.2:30080

# Hoặc truy cập trực tiếp
curl $(minikube ip):30080
```

### Bài tập 2.3: DNS nội bộ và giao tiếp giữa các namespace

**Yêu cầu:** Tạo 2 namespace, deploy service ở mỗi namespace, chứng minh chúng giao tiếp qua DNS.

**Lời giải:**

```bash
# Tạo 2 namespace
kubectl create namespace frontend
kubectl create namespace backend-ns

# Deploy app ở namespace backend-ns
kubectl run api-server --image=nginx:1.27 -n backend-ns \
  --labels="app=api" -- sh -c "echo 'Hello from API' > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"
kubectl expose pod api-server -n backend-ns --port=80 --name=api-svc

# Từ namespace frontend, gọi service ở backend-ns
kubectl run client --image=busybox:1.36 -n frontend --rm -it -- sh
# Bên trong:
# Cách 1: Dùng FQDN
wget -qO- http://api-svc.backend-ns.svc.cluster.local
# Cách 2: Dùng tên ngắn <service>.<namespace>
wget -qO- http://api-svc.backend-ns
exit

# Dọn dẹp
kubectl delete namespace frontend backend-ns
```

**Lý thuyết rút ra:** Quy tắc DNS trong K8s:
- Cùng namespace: `<service-name>`
- Khác namespace: `<service-name>.<namespace>`
- FQDN: `<service-name>.<namespace>.svc.cluster.local`

---

## Giai đoạn 3: Quản Lý Ứng Dụng - Deployment, Scaling & Updates

### Mục tiêu
Triển khai ứng dụng với khả năng scaling, rolling update, và rollback.

### Khái niệm cốt lõi
- **Deployment**: Controller quản lý ReplicaSet, đảm bảo số Pod mong muốn luôn chạy.
- **ReplicaSet**: Duy trì số lượng Pod replicas.
- **Rolling Update**: Cập nhật ứng dụng không downtime.
- **Rollback**: Quay về phiên bản trước.
- **HPA**: Horizontal Pod Autoscaler - tự động scale dựa trên metrics.

### Bài tập 3.1: Deployment cơ bản và Scaling

**Yêu cầu:** Tạo Deployment với 3 replicas, scale lên 5, scale xuống 2.

**Lời giải:**

```yaml
# nginx-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.26
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: "50m"
            memory: "64Mi"
          limits:
            cpu: "100m"
            memory: "128Mi"
```

```bash
kubectl apply -f nginx-deployment.yaml

# Xem Deployment, ReplicaSet, Pods
kubectl get deploy,rs,pods -l app=nginx

# Scale lên 5
kubectl scale deployment nginx-deploy --replicas=5
kubectl get pods -l app=nginx -w

# Scale xuống 2
kubectl scale deployment nginx-deploy --replicas=2
kubectl get pods -l app=nginx
```

### Bài tập 3.2: Rolling Update & Rollback

**Yêu cầu:** Cập nhật image từ nginx:1.26 lên nginx:1.27, quan sát rolling update, sau đó rollback.

**Lời giải:**

```bash
# Cập nhật image
kubectl set image deployment/nginx-deploy nginx=nginx:1.27

# Quan sát rolling update diễn ra
kubectl rollout status deployment/nginx-deploy
kubectl get pods -l app=nginx -w  # (chạy ở tab khác)

# Xem lịch sử rollout
kubectl rollout history deployment/nginx-deploy

# Xem chi tiết revision cụ thể
kubectl rollout history deployment/nginx-deploy --revision=2

# Giả sử cập nhật bị lỗi (image không tồn tại)
kubectl set image deployment/nginx-deploy nginx=nginx:99.99
kubectl rollout status deployment/nginx-deploy
# => Thấy pod mới bị ImagePullBackOff

# Rollback về revision trước
kubectl rollout undo deployment/nginx-deploy
kubectl rollout status deployment/nginx-deploy
# => Quay về nginx:1.27 thành công
```

### Bài tập 3.3: Deployment Strategy - Tùy chỉnh Rolling Update

**Yêu cầu:** Cấu hình rolling update với maxSurge và maxUnavailable cụ thể.

**Lời giải:**

```yaml
# controlled-rollout.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: controlled-app
spec:
  replicas: 6
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2          # Tối đa thêm 2 Pod mới cùng lúc
      maxUnavailable: 1    # Tối đa 1 Pod không sẵn sàng
  selector:
    matchLabels:
      app: controlled
  template:
    metadata:
      labels:
        app: controlled
    spec:
      containers:
      - name: app
        image: nginx:1.26
        ports:
        - containerPort: 80
```

```bash
kubectl apply -f controlled-rollout.yaml

# Cập nhật và quan sát chiến lược
kubectl set image deployment/controlled-app app=nginx:1.27
kubectl get pods -l app=controlled -w
# => Thấy tối đa 8 pods (6+2 surge) và tối thiểu 5 pods (6-1 unavailable)
```

### Bài tập 3.4: Horizontal Pod Autoscaler (HPA)

**Yêu cầu:** Cấu hình HPA để tự động scale ứng dụng dựa trên CPU usage.

**Lời giải:**

```bash
# Bật metrics-server trên Minikube
minikube addons enable metrics-server
```

```yaml
# hpa-demo.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-apache
spec:
  replicas: 1
  selector:
    matchLabels:
      app: php-apache
  template:
    metadata:
      labels:
        app: php-apache
    spec:
      containers:
      - name: php-apache
        image: registry.k8s.io/hpa-example
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: "200m"
          limits:
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: php-apache
spec:
  selector:
    app: php-apache
  ports:
  - port: 80
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
```

```bash
kubectl apply -f hpa-demo.yaml

# Chờ metrics sẵn sàng (~1 phút)
kubectl get hpa php-apache-hpa -w

# Tạo tải (chạy ở tab khác)
kubectl run load-generator --image=busybox:1.36 --rm -it -- sh
# Bên trong:
while true; do wget -q -O- http://php-apache; done

# Quan sát HPA scale up (tab chính)
kubectl get hpa php-apache-hpa -w
kubectl get pods -l app=php-apache -w
# => Pods tăng dần khi CPU > 50%

# Ctrl+C load-generator => chờ ~5 phút, pods sẽ scale down
```

---

## Giai đoạn 4: Cấu Hình & Bảo Mật Ứng Dụng

### Mục tiêu
Quản lý cấu hình và dữ liệu nhạy cảm tách biệt khỏi container image.

### Khái niệm cốt lõi
- **ConfigMap**: Lưu cấu hình dạng key-value hoặc file.
- **Secret**: Lưu dữ liệu nhạy cảm (mật khẩu, token, chứng chỉ) được mã hóa base64.
- **Environment Variables** vs **Volume Mount**: 2 cách inject cấu hình vào Pod.

### Bài tập 4.1: ConfigMap - Nhiều cách sử dụng

**Yêu cầu:** Tạo ConfigMap từ literal, từ file, và inject vào Pod bằng cả env var và volume mount.

**Lời giải:**

```bash
# Tạo ConfigMap từ literal
kubectl create configmap app-config \
  --from-literal=APP_ENV=production \
  --from-literal=APP_DEBUG=false \
  --from-literal=APP_PORT=8080

# Tạo file cấu hình
cat <<'EOF' > nginx-custom.conf
server {
    listen 80;
    server_name localhost;
    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
    location /health {
        return 200 'OK';
    }
}
EOF

# Tạo ConfigMap từ file
kubectl create configmap nginx-config --from-file=default.conf=nginx-custom.conf
```

```yaml
# configmap-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-config
spec:
  containers:
  - name: app
    image: nginx:1.27
    ports:
    - containerPort: 80

    # Cách 1: Inject từng key thành biến môi trường
    env:
    - name: ENVIRONMENT
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: APP_ENV
    - name: DEBUG_MODE
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: APP_DEBUG

    # Cách 2: Inject tất cả key thành biến môi trường
    envFrom:
    - configMapRef:
        name: app-config

    # Cách 3: Mount file cấu hình
    volumeMounts:
    - name: nginx-config-vol
      mountPath: /etc/nginx/conf.d

  volumes:
  - name: nginx-config-vol
    configMap:
      name: nginx-config
```

```bash
kubectl apply -f configmap-pod.yaml

# Kiểm tra env variables
kubectl exec app-with-config -- env | grep APP_
kubectl exec app-with-config -- env | grep ENVIRONMENT

# Kiểm tra file mount
kubectl exec app-with-config -- cat /etc/nginx/conf.d/default.conf

# Test endpoint /health
kubectl port-forward app-with-config 8080:80
curl http://localhost:8080/health
```

### Bài tập 4.2: Secret

**Yêu cầu:** Tạo Secret chứa thông tin database, inject vào Pod.

**Lời giải:**

```bash
# Tạo Secret (K8s tự encode base64)
kubectl create secret generic db-credentials \
  --from-literal=DB_HOST=mysql.default.svc.cluster.local \
  --from-literal=DB_USER=admin \
  --from-literal=DB_PASSWORD=SuperSecr3t! \
  --from-literal=DB_NAME=myapp
```

```yaml
# secret-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-secrets
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "echo DB=$DB_HOST User=$DB_USER && sleep 3600"]
    env:
    - name: DB_HOST
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_HOST
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_USER
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: DB_PASSWORD

    # Mount Secret dưới dạng file
    volumeMounts:
    - name: db-secret-vol
      mountPath: /etc/secrets
      readOnly: true

  volumes:
  - name: db-secret-vol
    secret:
      secretName: db-credentials
```

```bash
kubectl apply -f secret-pod.yaml

# Kiểm tra
kubectl exec app-with-secrets -- env | grep DB_
kubectl exec app-with-secrets -- ls /etc/secrets/
kubectl exec app-with-secrets -- cat /etc/secrets/DB_PASSWORD

# Xem secret (base64 encoded)
kubectl get secret db-credentials -o yaml
# Decode
kubectl get secret db-credentials -o jsonpath='{.data.DB_PASSWORD}' | base64 -d
```

---

## Giai đoạn 5: Lưu Trữ Dữ Liệu - Persistent Storage

### Mục tiêu
Dữ liệu tồn tại khi Pod bị xóa hoặc restart.

### Khái niệm cốt lõi
- **Volume types**: emptyDir, hostPath, PersistentVolume.
- **PersistentVolume (PV)**: Tài nguyên lưu trữ trong cụm.
- **PersistentVolumeClaim (PVC)**: Yêu cầu lưu trữ từ Pod.
- **StorageClass**: Tự động cấp phát PV (dynamic provisioning).
- **Access Modes**: ReadWriteOnce, ReadOnlyMany, ReadWriteMany.

### Bài tập 5.1: PV, PVC và Pod

**Yêu cầu:** Tạo PV thủ công, tạo PVC để claim, gắn vào Pod. Chứng minh dữ liệu tồn tại sau khi xóa Pod.

**Lời giải:**

```yaml
# persistent-storage.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
  - ReadWriteOnce
  hostPath:
    path: /data/local-pv
  persistentVolumeReclaimPolicy: Retain
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
---
apiVersion: v1
kind: Pod
metadata:
  name: storage-pod
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "echo 'Data persisted!' > /data/test.txt && sleep 3600"]
    volumeMounts:
    - name: data-vol
      mountPath: /data
  volumes:
  - name: data-vol
    persistentVolumeClaim:
      claimName: local-pvc
```

```bash
kubectl apply -f persistent-storage.yaml

# Kiểm tra PV và PVC đã bound
kubectl get pv,pvc

# Ghi dữ liệu
kubectl exec storage-pod -- cat /data/test.txt

# Xóa Pod
kubectl delete pod storage-pod

# Tạo lại Pod mới gắn cùng PVC
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: storage-pod-2
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "cat /data/test.txt && sleep 3600"]
    volumeMounts:
    - name: data-vol
      mountPath: /data
  volumes:
  - name: data-vol
    persistentVolumeClaim:
      claimName: local-pvc
EOF

# Dữ liệu vẫn còn!
kubectl logs storage-pod-2
```

### Bài tập 5.2: Dynamic Provisioning với StorageClass

**Yêu cầu:** Sử dụng StorageClass để tự động tạo PV khi có PVC.

**Lời giải:**

```bash
# Xem StorageClass có sẵn (Minikube có "standard" mặc định)
kubectl get storageclass
```

```yaml
# dynamic-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: dynamic-pvc
spec:
  storageClassName: standard  # StorageClass của Minikube
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 256Mi
---
apiVersion: v1
kind: Pod
metadata:
  name: dynamic-storage-pod
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "date >> /data/log.txt && cat /data/log.txt && sleep 3600"]
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: dynamic-pvc
```

```bash
kubectl apply -f dynamic-pvc.yaml

# PV được tạo tự động!
kubectl get pv,pvc
kubectl logs dynamic-storage-pod
```

---

## Giai đoạn 6: Workload Nâng Cao - Job, CronJob, DaemonSet, StatefulSet

### Mục tiêu
Sử dụng đúng loại workload cho từng use case.

### Khi nào dùng gì?

| Workload | Use Case | Ví dụ |
|----------|----------|-------|
| **Deployment** | Stateless app, có thể scale tự do | Web server, API |
| **StatefulSet** | Stateful app, cần identity ổn định | Database, Kafka |
| **DaemonSet** | Chạy 1 Pod trên mỗi Node | Log collector, monitoring agent |
| **Job** | Chạy 1 lần rồi dừng | Data migration, batch processing |
| **CronJob** | Chạy định kỳ | Backup, report, cleanup |

### Bài tập 6.1: Job và CronJob

**Yêu cầu:** Tạo Job tính Pi, tạo CronJob chạy mỗi phút.

**Lời giải:**

```yaml
# job-pi.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi-calculator
spec:
  completions: 3      # Cần hoàn thành 3 lần
  parallelism: 2      # Chạy song song 2 Pod
  backoffLimit: 4      # Tối đa 4 lần retry nếu lỗi
  activeDeadlineSeconds: 120  # Timeout 2 phút
  template:
    spec:
      containers:
      - name: pi
        image: perl:5.38
        command: ["perl", "-Mbignum=bpi", "-wle", "print bpi(100)"]
      restartPolicy: Never
```

```yaml
# cronjob-cleanup.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: log-cleanup
spec:
  schedule: "*/1 * * * *"   # Mỗi phút
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  concurrencyPolicy: Forbid   # Không chạy job mới nếu job cũ chưa xong
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: cleanup
            image: busybox:1.36
            command: ["sh", "-c", "echo 'Cleanup at $(date)' && sleep 5"]
          restartPolicy: OnFailure
```

```bash
kubectl apply -f job-pi.yaml
kubectl apply -f cronjob-cleanup.yaml

# Theo dõi Job
kubectl get jobs -w
kubectl get pods -l job-name=pi-calculator
kubectl logs job/pi-calculator

# Theo dõi CronJob
kubectl get cronjobs
kubectl get jobs -w  # Chờ xem job mới tạo mỗi phút
```

### Bài tập 6.2: DaemonSet

**Yêu cầu:** Tạo DaemonSet chạy log collector trên mọi node.

**Lời giải:**

```yaml
# daemonset-logger.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-logger
  labels:
    app: node-logger
spec:
  selector:
    matchLabels:
      app: node-logger
  template:
    metadata:
      labels:
        app: node-logger
    spec:
      containers:
      - name: logger
        image: busybox:1.36
        command: ["sh", "-c", "while true; do echo \"Node: $(hostname) - $(date)\"; sleep 30; done"]
        resources:
          requests:
            cpu: "50m"
            memory: "32Mi"
          limits:
            cpu: "100m"
            memory: "64Mi"
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        effect: NoSchedule
```

```bash
kubectl apply -f daemonset-logger.yaml

# Kiểm tra: mỗi node chạy đúng 1 pod
kubectl get daemonset node-logger
kubectl get pods -l app=node-logger -o wide

# Nếu thêm node mới (Minikube)
minikube node add
kubectl get pods -l app=node-logger -o wide
# => Pod mới tự động xuất hiện trên node mới
```

### Bài tập 6.3: StatefulSet

**Yêu cầu:** Deploy ứng dụng stateful mô phỏng database cluster với danh tính ổn định.

**Lời giải:**

```yaml
# statefulset-demo.yaml
apiVersion: v1
kind: Service
metadata:
  name: db-headless
spec:
  clusterIP: None        # Headless Service - bắt buộc cho StatefulSet
  selector:
    app: database
  ports:
  - port: 5432
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: database
spec:
  serviceName: db-headless    # Phải khớp Headless Service
  replicas: 3
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
    spec:
      containers:
      - name: db
        image: busybox:1.36
        command: ["sh", "-c", "echo 'I am $(hostname)' && sleep 3600"]
        volumeMounts:
        - name: data
          mountPath: /data
  volumeClaimTemplates:       # Mỗi Pod có PVC riêng
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: standard
      resources:
        requests:
          storage: 100Mi
```

```bash
kubectl apply -f statefulset-demo.yaml

# Quan sát: Pod tạo tuần tự (0, 1, 2) - KHÔNG song song như Deployment
kubectl get pods -l app=database -w

# Tên Pod ổn định: database-0, database-1, database-2
kubectl get pods -l app=database

# DNS ổn định cho từng Pod
kubectl run dns-test --image=busybox:1.36 --rm -it -- nslookup database-0.db-headless
# => database-0.db-headless.default.svc.cluster.local

# Mỗi Pod có PVC riêng
kubectl get pvc

# Xóa Pod => Pod mới giữ nguyên tên và PVC
kubectl delete pod database-1
kubectl get pods -l app=database -w
# => database-1 tái tạo, gắn lại PVC cũ
```

**So sánh StatefulSet vs Deployment:**

| | Deployment | StatefulSet |
|---|---|---|
| Tên Pod | Random (deploy-abc123) | Có thứ tự (app-0, app-1) |
| Khởi tạo | Song song | Tuần tự |
| Storage | Chia sẻ PVC | Mỗi Pod có PVC riêng |
| DNS | Qua Service | Từng Pod có DNS riêng |
| Use case | Stateless apps | Databases, message queues |

---

## Giai đoạn 7: Networking Nâng Cao - Ingress, Gateway API & DNS

### Mục tiêu
Expose nhiều ứng dụng ra bên ngoài qua domain name, cấu hình TLS.

### Bài tập 7.1: Ingress Controller & Routing

**Yêu cầu:** Cài Ingress Controller, tạo Ingress rules để route traffic dựa trên path và hostname.

**Lời giải:**

```bash
# Bật Ingress addon trên Minikube
minikube addons enable ingress

# Chờ Ingress Controller sẵn sàng
kubectl get pods -n ingress-nginx -w
```

```yaml
# ingress-apps.yaml
# App 1: Frontend
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:1.27
        command: ["sh", "-c", "echo 'Frontend App' > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"]
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-svc
spec:
  selector:
    app: frontend
  ports:
  - port: 80
---
# App 2: API
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: nginx
        image: nginx:1.27
        command: ["sh", "-c", "echo '{\"status\":\"ok\"}' > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"]
---
apiVersion: v1
kind: Service
metadata:
  name: api-svc
spec:
  selector:
    app: api
  ports:
  - port: 80
```

```yaml
# ingress-rules.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  # Route theo path
  - host: myapp.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-svc
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-svc
            port:
              number: 80
  # Route theo hostname
  - host: api.myapp.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-svc
            port:
              number: 80
```

```bash
kubectl apply -f ingress-apps.yaml
kubectl apply -f ingress-rules.yaml

# Thêm hosts entry
echo "$(minikube ip) myapp.local api.myapp.local" | sudo tee -a /etc/hosts

# Test
curl http://myapp.local       # => Frontend App
curl http://myapp.local/api   # => {"status":"ok"}
curl http://api.myapp.local   # => {"status":"ok"}
```

### Bài tập 7.2: Gateway API (Thay thế Ingress - Xu hướng mới)

> **Lưu ý:** Gateway API là tiêu chuẩn mới thay thế Ingress. Ingress-NGINX chính thức ngừng phát triển từ 03/2026. Nên học Gateway API cho các dự án mới.

**Yêu cầu:** Cài đặt Gateway API, tạo Gateway và HTTPRoute.

**Lời giải:**

```bash
# Cài Gateway API CRDs
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/standard-install.yaml

# Cài Gateway Controller (ví dụ: NGINX Gateway Fabric cho Minikube)
kubectl apply -f https://github.com/nginx/nginx-gateway-fabric/releases/latest/download/nginx-gateway-fabric.yaml
```

```yaml
# gateway-demo.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway
spec:
  gatewayClassName: nginx  # Tùy controller đã cài
  listeners:
  - name: http
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: Same
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: app-routes
spec:
  parentRefs:
  - name: my-gateway
  hostnames:
  - "myapp.local"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /api
    backendRefs:
    - name: api-svc
      port: 80
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: frontend-svc
      port: 80
```

**So sánh Ingress vs Gateway API:**

| | Ingress | Gateway API |
|---|---|---|
| Trạng thái | Legacy (sắp ngừng) | GA, tiêu chuẩn mới |
| Routing nâng cao | Qua annotations (không chuẩn) | Native (header, weight) |
| Phân quyền | Không | GatewayClass → Gateway → Route |
| Protocols | HTTP/HTTPS | HTTP, gRPC, TCP, UDP |
| Traffic splitting | Không native | Có (canary, blue/green) |

---

## Giai đoạn 8: Scheduling & Quản Lý Tài Nguyên

### Mục tiêu
Kiểm soát Pod chạy ở đâu và sử dụng bao nhiêu tài nguyên.

### Khái niệm cốt lõi
- **Requests/Limits**: Tài nguyên tối thiểu/tối đa cho container.
- **QoS Classes**: Guaranteed, Burstable, BestEffort.
- **LimitRange**: Giới hạn mặc định cho namespace.
- **ResourceQuota**: Quota tổng tài nguyên cho namespace.
- **Taints/Tolerations**: Ngăn/cho phép Pod chạy trên Node.
- **Node Affinity**: Ưu tiên/bắt buộc Pod chạy trên Node cụ thể.
- **Pod Affinity/Anti-Affinity**: Pod nên/không nên chạy cùng nhau.

### Bài tập 8.1: Resource Requests, Limits & QoS

**Yêu cầu:** Tạo 3 Pod với 3 QoS class khác nhau, kiểm tra.

**Lời giải:**

```yaml
# qos-demo.yaml
# Guaranteed: requests == limits (cho cả CPU và memory)
apiVersion: v1
kind: Pod
metadata:
  name: qos-guaranteed
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "100m"
        memory: "128Mi"
---
# Burstable: requests < limits (hoặc chỉ set 1 trong 2)
apiVersion: v1
kind: Pod
metadata:
  name: qos-burstable
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    resources:
      requests:
        cpu: "50m"
        memory: "64Mi"
      limits:
        cpu: "200m"
        memory: "256Mi"
---
# BestEffort: không set requests/limits
apiVersion: v1
kind: Pod
metadata:
  name: qos-besteffort
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
```

```bash
kubectl apply -f qos-demo.yaml

# Kiểm tra QoS class
kubectl get pod qos-guaranteed -o jsonpath='{.status.qosClass}'
# => Guaranteed
kubectl get pod qos-burstable -o jsonpath='{.status.qosClass}'
# => Burstable
kubectl get pod qos-besteffort -o jsonpath='{.status.qosClass}'
# => BestEffort

# Khi node thiếu tài nguyên, K8s sẽ evict theo thứ tự:
# BestEffort → Burstable → Guaranteed (cuối cùng)
```

### Bài tập 8.2: LimitRange & ResourceQuota

**Yêu cầu:** Tạo namespace với giới hạn tài nguyên cho từng Pod và tổng namespace.

**Lời giải:**

```yaml
# resource-controls.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: team-alpha
---
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: team-alpha
spec:
  limits:
  - type: Container
    default:           # Limits mặc định nếu Pod không set
      cpu: "200m"
      memory: "256Mi"
    defaultRequest:    # Requests mặc định
      cpu: "100m"
      memory: "128Mi"
    max:               # Giới hạn tối đa
      cpu: "1"
      memory: "1Gi"
    min:               # Giới hạn tối thiểu
      cpu: "50m"
      memory: "64Mi"
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-alpha-quota
  namespace: team-alpha
spec:
  hard:
    pods: "10"
    requests.cpu: "2"
    requests.memory: "4Gi"
    limits.cpu: "4"
    limits.memory: "8Gi"
    persistentvolumeclaims: "5"
```

```bash
kubectl apply -f resource-controls.yaml

# Tạo Pod không set resources => tự động nhận default từ LimitRange
kubectl run test-pod --image=busybox:1.36 -n team-alpha -- sleep 3600
kubectl get pod test-pod -n team-alpha -o yaml | grep -A 4 resources

# Xem quota usage
kubectl get resourcequota -n team-alpha
kubectl describe resourcequota team-alpha-quota -n team-alpha

# Thử vượt quota
kubectl create deployment big-deploy --image=busybox:1.36 -n team-alpha --replicas=15 -- sleep 3600
# => Sẽ fail khi vượt quá 10 pods hoặc quota CPU/memory
```

### Bài tập 8.3: Taints, Tolerations & Node Affinity

**Yêu cầu:** Taint một node, tạo Pod có toleration, cấu hình node affinity.

**Lời giải:**

```bash
# Thêm node mới cho Minikube
minikube node add

# Gán label cho node
kubectl label nodes minikube-m02 disk=ssd env=production

# Taint node (ngăn Pod chạy trên node này trừ khi có toleration)
kubectl taint nodes minikube-m02 dedicated=database:NoSchedule
```

```yaml
# scheduling-demo.yaml
# Pod KHÔNG có toleration => không chạy được trên minikube-m02
apiVersion: v1
kind: Pod
metadata:
  name: normal-pod
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
---
# Pod CÓ toleration + node affinity => chạy trên minikube-m02
apiVersion: v1
kind: Pod
metadata:
  name: db-pod
spec:
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "database"
    effect: "NoSchedule"
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disk
            operator: In
            values: ["ssd"]
  containers:
  - name: db
    image: busybox:1.36
    command: ["sleep", "3600"]
```

```bash
kubectl apply -f scheduling-demo.yaml

# Kiểm tra Pod chạy trên node nào
kubectl get pods -o wide
# => normal-pod chạy trên minikube (node 1)
# => db-pod chạy trên minikube-m02 (node 2)
```

### Bài tập 8.4: Pod Anti-Affinity (High Availability)

**Yêu cầu:** Đảm bảo các replicas của cùng app không chạy trên cùng node.

**Lời giải:**

```yaml
# anti-affinity-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ha-web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ha-web
  template:
    metadata:
      labels:
        app: ha-web
    spec:
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values: ["ha-web"]
              topologyKey: kubernetes.io/hostname
      containers:
      - name: web
        image: nginx:1.27
```

```bash
kubectl apply -f anti-affinity-deploy.yaml
kubectl get pods -o wide
# => Pods phân bố trên các node khác nhau (nếu đủ node)
```

---

## Giai đoạn 9: Observability - Monitoring, Logging & Troubleshooting

### Mục tiêu
Giám sát cụm, thu thập logs, và xử lý sự cố.

### Bài tập 9.1: Prometheus & Grafana Stack

**Yêu cầu:** Cài đặt Prometheus + Grafana trên Minikube, xem metrics cụm.

**Lời giải:**

```bash
# Cài bằng Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Cài kube-prometheus-stack (bao gồm Prometheus, Grafana, AlertManager)
kubectl create namespace monitoring
helm install kube-prom prometheus-community/kube-prometheus-stack \
  -n monitoring \
  --set grafana.adminPassword=admin123

# Chờ tất cả pod sẵn sàng
kubectl get pods -n monitoring -w

# Truy cập Grafana
kubectl port-forward svc/kube-prom-grafana 3000:80 -n monitoring
# Mở http://localhost:3000 - Login: admin / admin123
# Vào Dashboards → tìm "Kubernetes / Compute Resources / Cluster"

# Truy cập Prometheus
kubectl port-forward svc/kube-prom-kube-prometheus-prometheus 9090:9090 -n monitoring
# Mở http://localhost:9090
# Thử query: container_cpu_usage_seconds_total
```

### Bài tập 9.2: Troubleshooting - Các kịch bản lỗi thường gặp

**Yêu cầu:** Chẩn đoán và sửa các lỗi phổ biến.

**Kịch bản 1: Pod ở trạng thái CrashLoopBackOff**

```yaml
# broken-pod-1.yaml
apiVersion: v1
kind: Pod
metadata:
  name: crashing-app
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sh", "-c", "echo 'Starting...' && exit 1"]
```

```bash
kubectl apply -f broken-pod-1.yaml
kubectl get pods  # => CrashLoopBackOff

# Bước 1: Xem logs
kubectl logs crashing-app
kubectl logs crashing-app --previous

# Bước 2: Xem events
kubectl describe pod crashing-app | tail -20

# Nguyên nhân: Command exit với code 1
# Sửa: Thay command để app chạy liên tục
```

**Kịch bản 2: Pod ở trạng thái ImagePullBackOff**

```bash
kubectl run bad-image --image=nginx:nonexistent
kubectl describe pod bad-image | grep -A 5 Events
# => Failed to pull image "nginx:nonexistent"
# Sửa: Dùng đúng image tag
```

**Kịch bản 3: Pod ở trạng thái Pending**

```yaml
# pending-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pending-pod
spec:
  containers:
  - name: app
    image: busybox:1.36
    command: ["sleep", "3600"]
    resources:
      requests:
        cpu: "100"     # 100 CPU cores - quá nhiều!
        memory: "256Gi"
```

```bash
kubectl apply -f pending-pod.yaml
kubectl describe pod pending-pod | grep -A 5 Events
# => 0/1 nodes are available: Insufficient cpu, Insufficient memory
# Sửa: Giảm resources.requests
```

**Checklist Troubleshooting:**

```bash
# 1. Trạng thái tổng quan
kubectl get pods -o wide
kubectl get events --sort-by='.lastTimestamp'

# 2. Chi tiết Pod
kubectl describe pod <pod-name>
kubectl logs <pod-name> [-c <container>] [--previous]

# 3. Network debug
kubectl run debug --image=busybox:1.36 --rm -it -- sh
# wget -qO- http://<service-name>
# nslookup <service-name>

# 4. Node debug
kubectl describe node <node-name>
kubectl top nodes
kubectl top pods

# 5. Ephemeral debug container
kubectl debug -it <pod-name> --image=busybox -- sh
```

---

## Giai đoạn 10: Bảo Mật Cụm - RBAC, Network Policy, Pod Security

### Mục tiêu
Bảo mật cụm K8s theo nguyên tắc least privilege.

### Bài tập 10.1: RBAC - Phân quyền người dùng

**Yêu cầu:** Tạo ServiceAccount chỉ có quyền đọc pods trong namespace cụ thể.

**Lời giải:**

```yaml
# rbac-demo.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dev-team
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: dev-viewer
  namespace: dev-team
---
# Role: Định nghĩa quyền trong 1 namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: dev-team
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "watch", "list"]
- apiGroups: [""]
  resources: ["services"]
  verbs: ["get", "list"]
---
# RoleBinding: Gắn Role cho ServiceAccount
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: dev-viewer-binding
  namespace: dev-team
subjects:
- kind: ServiceAccount
  name: dev-viewer
  namespace: dev-team
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

```bash
kubectl apply -f rbac-demo.yaml

# Tạo Pod để test
kubectl run test-app --image=nginx:1.27 -n dev-team

# Test quyền (impersonate ServiceAccount)
kubectl auth can-i get pods -n dev-team --as=system:serviceaccount:dev-team:dev-viewer
# => yes

kubectl auth can-i delete pods -n dev-team --as=system:serviceaccount:dev-team:dev-viewer
# => no

kubectl auth can-i get pods -n default --as=system:serviceaccount:dev-team:dev-viewer
# => no (chỉ có quyền trong namespace dev-team)
```

### Bài tập 10.2: Network Policy

**Yêu cầu:** Tạo Network Policy chỉ cho phép frontend gọi backend, không cho phép traffic khác.

**Lời giải:**

```bash
# Cài CNI hỗ trợ Network Policy (Minikube dùng Calico)
minikube start --cni=calico
# Hoặc nếu đã có cụm:
minikube addons enable network-policy
```

```yaml
# network-policy-demo.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: secure-app
---
# Backend
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  namespace: secure-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
        tier: backend
    spec:
      containers:
      - name: nginx
        image: nginx:1.27
---
apiVersion: v1
kind: Service
metadata:
  name: backend-svc
  namespace: secure-app
spec:
  selector:
    app: backend
  ports:
  - port: 80
---
# Frontend
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: secure-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:1.27
---
# Network Policy: Backend chỉ nhận traffic từ Frontend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-policy
  namespace: secure-app
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: frontend
    ports:
    - port: 80
---
# Default deny all: Chặn mọi traffic không được phép
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
  namespace: secure-app
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

```bash
kubectl apply -f network-policy-demo.yaml

# Test: Frontend CÓ THỂ gọi backend
kubectl exec -n secure-app deploy/frontend -- curl -s --max-time 3 http://backend-svc
# => HTML response (thành công)

# Test: Pod lạ KHÔNG THỂ gọi backend
kubectl run attacker --image=busybox:1.36 -n secure-app --rm -it -- wget -qO- --timeout=3 http://backend-svc
# => timeout (bị chặn)
```

### Bài tập 10.3: Pod Security Standards (Thay thế PodSecurityPolicy)

**Yêu cầu:** Áp dụng Pod Security Standards ở mức restricted cho namespace.

**Lời giải:**

```yaml
# pod-security-ns.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: restricted-ns
  labels:
    # enforce: từ chối Pod không tuân thủ
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
    # warn: cảnh báo nhưng vẫn cho phép
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/warn-version: latest
```

```bash
kubectl apply -f pod-security-ns.yaml

# Thử tạo Pod privileged => BỊ TỪ CHỐI
kubectl run bad-pod --image=nginx:1.27 -n restricted-ns
# => Error: violates PodSecurity "restricted"

# Tạo Pod tuân thủ restricted
kubectl apply -n restricted-ns -f - <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: nginx:1.27
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
      runAsUser: 1000
EOF
# => Tạo thành công
```

---

## Giai đoạn 11: Helm, Kustomize & Quản Lý Package

### Mục tiêu
Quản lý, đóng gói và tùy biến ứng dụng K8s một cách hiệu quả.

### Bài tập 11.1: Helm - Cài đặt và quản lý ứng dụng

**Yêu cầu:** Dùng Helm cài WordPress, tùy chỉnh values, upgrade, rollback.

**Lời giải:**

```bash
# Thêm repo
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Tìm kiếm chart
helm search repo wordpress

# Xem values mặc định
helm show values bitnami/wordpress | head -50

# Cài đặt với tùy chỉnh
helm install my-blog bitnami/wordpress \
  --namespace blog --create-namespace \
  --set wordpressUsername=admin \
  --set wordpressPassword=MyP@ss123 \
  --set service.type=NodePort \
  --set persistence.size=1Gi \
  --set mariadb.primary.persistence.size=1Gi

# Xem trạng thái
helm list -n blog
kubectl get all -n blog

# Upgrade
helm upgrade my-blog bitnami/wordpress -n blog \
  --set replicaCount=2

# Xem lịch sử
helm history my-blog -n blog

# Rollback
helm rollback my-blog 1 -n blog

# Gỡ cài đặt
helm uninstall my-blog -n blog
```

### Bài tập 11.2: Tạo Helm Chart riêng

**Yêu cầu:** Tạo Helm chart cho ứng dụng web đơn giản.

**Lời giải:**

```bash
# Tạo chart mới
helm create my-webapp
```

```bash
# Cấu trúc thư mục được tạo:
# my-webapp/
# ├── Chart.yaml          # Metadata
# ├── values.yaml         # Giá trị mặc định
# ├── templates/
# │   ├── deployment.yaml
# │   ├── service.yaml
# │   ├── ingress.yaml
# │   ├── _helpers.tpl    # Template helpers
# │   └── ...
# └── charts/             # Sub-charts
```

```bash
# Test template render (không deploy)
helm template my-release ./my-webapp

# Lint kiểm tra lỗi
helm lint ./my-webapp

# Cài đặt từ local chart
helm install my-release ./my-webapp

# Cài đặt với custom values
helm install my-release ./my-webapp -f custom-values.yaml

# Package chart
helm package ./my-webapp
# => my-webapp-0.1.0.tgz
```

### Bài tập 11.3: Kustomize - Tùy biến không template

**Yêu cầu:** Dùng Kustomize quản lý cấu hình cho nhiều môi trường (dev, staging, prod).

**Lời giải:**

```
# Cấu trúc thư mục:
# kustomize-demo/
# ├── base/
# │   ├── kustomization.yaml
# │   ├── deployment.yaml
# │   └── service.yaml
# └── overlays/
#     ├── dev/
#     │   └── kustomization.yaml
#     ├── staging/
#     │   └── kustomization.yaml
#     └── prod/
#         ├── kustomization.yaml
#         └── increase-replicas.yaml
```

```yaml
# base/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- deployment.yaml
- service.yaml
```

```yaml
# base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: myapp:latest
        ports:
        - containerPort: 8080
```

```yaml
# base/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
```

```yaml
# overlays/dev/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- ../../base
namePrefix: dev-
namespace: dev
labels:
- pairs:
    env: dev
```

```yaml
# overlays/prod/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- ../../base
namePrefix: prod-
namespace: production
labels:
- pairs:
    env: production
patches:
- path: increase-replicas.yaml
```

```yaml
# overlays/prod/increase-replicas.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 5
```

```bash
# Preview kết quả cho dev
kubectl kustomize overlays/dev

# Preview kết quả cho prod
kubectl kustomize overlays/prod

# Apply cho dev
kubectl apply -k overlays/dev

# Apply cho prod
kubectl apply -k overlays/prod
```

---

## Giai đoạn 12: CI/CD & GitOps

### Mục tiêu
Tự động hóa quy trình deploy lên K8s theo mô hình GitOps.

### Khái niệm cốt lõi
- **GitOps**: Git là single source of truth cho infrastructure và application state.
- **ArgoCD**: GitOps controller phổ biến nhất cho K8s.
- **Push-based CI/CD**: CI pipeline push changes lên K8s (GitHub Actions, GitLab CI).
- **Pull-based GitOps**: ArgoCD/FluxCD pull changes từ Git repo.

### Bài tập 12.1: ArgoCD - Cài đặt và Deploy ứng dụng

**Yêu cầu:** Cài ArgoCD, tạo Application từ Git repo.

**Lời giải:**

```bash
# Cài ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Chờ sẵn sàng
kubectl get pods -n argocd -w

# Lấy mật khẩu admin
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d

# Truy cập UI
kubectl port-forward svc/argocd-server -n argocd 8443:443
# Mở https://localhost:8443 - Login: admin / <password ở trên>
```

```yaml
# argocd-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/<your-repo>/k8s-manifests.git
    targetRevision: main
    path: overlays/dev    # Có thể dùng Kustomize hoặc Helm
  destination:
    server: https://kubernetes.default.svc
    namespace: dev
  syncPolicy:
    automated:
      prune: true         # Xóa resource không còn trong Git
      selfHeal: true      # Tự sửa nếu bị thay đổi ngoài Git
    syncOptions:
    - CreateNamespace=true
```

```bash
kubectl apply -f argocd-app.yaml

# Hoặc dùng ArgoCD CLI
# brew install argocd
# argocd app create my-app --repo <url> --path overlays/dev --dest-server https://kubernetes.default.svc --dest-namespace dev
```

**Workflow GitOps:**
1. Developer push code → CI build image mới → push image lên registry
2. CI cập nhật image tag trong Git repo manifests
3. ArgoCD phát hiện thay đổi trong Git → tự động sync lên cụm
4. Mọi thay đổi infrastructure đều qua Git → có audit trail

---

## Giai đoạn 13: Chuyên Gia - CRD, Operator, Service Mesh & Multi-Cluster

### Mục tiêu
Mở rộng Kubernetes và vận hành hệ thống phức tạp.

### Bài tập 13.1: Custom Resource Definition (CRD)

**Yêu cầu:** Tạo CRD cho một tài nguyên tùy chỉnh.

**Lời giải:**

```yaml
# crd-demo.yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: backups.myapp.example.com
spec:
  group: myapp.example.com
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              schedule:
                type: string
              database:
                type: string
              retention:
                type: integer
            required: ["schedule", "database"]
  scope: Namespaced
  names:
    plural: backups
    singular: backup
    kind: Backup
    shortNames:
    - bk
```

```yaml
# my-backup.yaml
apiVersion: myapp.example.com/v1
kind: Backup
metadata:
  name: daily-db-backup
spec:
  schedule: "0 2 * * *"
  database: "production-db"
  retention: 7
```

```bash
kubectl apply -f crd-demo.yaml
kubectl apply -f my-backup.yaml

# Sử dụng tài nguyên tùy chỉnh
kubectl get backups
kubectl get bk    # short name
kubectl describe backup daily-db-backup
```

### Bài tập 13.2: Service Mesh với Istio (Giới thiệu)

**Yêu cầu:** Hiểu kiến trúc Service Mesh, cài Istio demo profile.

**Lời giải:**

```bash
# Cài Istio CLI
curl -L https://istio.io/downloadIstio | sh -
export PATH=$PWD/istio-*/bin:$PATH

# Cài Istio demo profile (đầy đủ tính năng, chỉ dùng cho lab)
istioctl install --set profile=demo -y

# Bật auto sidecar injection cho namespace
kubectl label namespace default istio-injection=enabled

# Deploy ứng dụng mẫu Bookinfo
kubectl apply -f istio-*/samples/bookinfo/platform/kube/bookinfo.yaml

# Xem pods (mỗi pod có thêm sidecar envoy-proxy)
kubectl get pods
# => Mỗi pod có 2/2 containers (app + istio-proxy)

# Cài Kiali dashboard (observability cho service mesh)
kubectl apply -f istio-*/samples/addons/
kubectl port-forward svc/kiali -n istio-system 20001:20001
```

**Service Mesh cung cấp:**
- **mTLS tự động**: Mã hóa giao tiếp giữa services
- **Traffic management**: Canary deploy, A/B testing, circuit breaker
- **Observability**: Distributed tracing, metrics, service graph
- **Policy**: Rate limiting, access control

### 13.3: Admission Controllers & Validating Admission Policy

**Khái niệm:** Admission controllers là middleware chặn requests tới API server sau authentication/authorization, trước khi lưu vào etcd.

**ValidatingAdmissionPolicy** (GA từ v1.30) cho phép viết validation rules trực tiếp bằng CEL (Common Expression Language) mà không cần webhook.

```yaml
# validating-admission-policy.yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicy
metadata:
  name: require-labels
spec:
  failurePolicy: Fail
  matchConstraints:
    resourceRules:
    - apiGroups: ["apps"]
      apiVersions: ["v1"]
      operations: ["CREATE", "UPDATE"]
      resources: ["deployments"]
  validations:
  - expression: "has(object.metadata.labels) && 'team' in object.metadata.labels"
    message: "Deployment phải có label 'team'"
---
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicyBinding
metadata:
  name: require-labels-binding
spec:
  policyName: require-labels
  validationActions: ["Deny"]
  matchResources:
    namespaceSelector:
      matchLabels:
        enforce-labels: "true"
```

---

## Giai đoạn 14: Managed Kubernetes & Production Readiness

### Mục tiêu
Vận hành K8s trên cloud và chuẩn bị cho production.

### Managed Kubernetes Services

| Provider | Service | Đặc điểm |
|----------|---------|-----------|
| **AWS** | EKS | Tích hợp sâu AWS ecosystem |
| **GCP** | GKE | Autopilot mode, tự động quản lý |
| **Azure** | AKS | Tích hợp Azure AD, miễn phí control plane |
| **Linode** | LKE | Chi phí thấp, đơn giản |
| **DigitalOcean** | DOKS | Dễ dùng cho startup |

### Production Readiness Checklist

```
☐ Security
  ☐ RBAC configured (no cluster-admin for apps)
  ☐ Network Policies enabled
  ☐ Pod Security Standards enforced
  ☐ Secrets encrypted at rest
  ☐ Container images scanned (Trivy, Grype)
  ☐ Non-root containers
  ☐ Service mesh mTLS (nếu cần)

☐ Reliability
  ☐ Resource requests/limits cho mọi container
  ☐ Liveness, readiness, startup probes
  ☐ PodDisruptionBudget cho critical workloads
  ☐ Pod anti-affinity cho HA
  ☐ HPA configured
  ☐ Multiple replicas cho stateless apps

☐ Observability
  ☐ Metrics: Prometheus + Grafana
  ☐ Logging: EFK/Loki stack
  ☐ Tracing: Jaeger/Tempo (nếu microservices)
  ☐ Alerting configured

☐ Operations
  ☐ GitOps (ArgoCD/FluxCD)
  ☐ etcd backup strategy
  ☐ Disaster recovery plan
  ☐ Upgrade strategy documented
  ☐ Cost monitoring
```

### Bài tập 14.1: PodDisruptionBudget

**Yêu cầu:** Đảm bảo ít nhất 2 replicas luôn chạy khi bảo trì node.

**Lời giải:**

```yaml
# pdb-demo.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: critical-app
spec:
  replicas: 4
  selector:
    matchLabels:
      app: critical
  template:
    metadata:
      labels:
        app: critical
    spec:
      containers:
      - name: app
        image: nginx:1.27
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: critical-app-pdb
spec:
  minAvailable: 2    # Hoặc dùng maxUnavailable: 1
  selector:
    matchLabels:
      app: critical
```

```bash
kubectl apply -f pdb-demo.yaml

# Kiểm tra PDB
kubectl get pdb

# Thử drain node (mô phỏng bảo trì)
kubectl drain minikube --ignore-daemonsets --delete-emptydir-data
# => K8s sẽ đảm bảo ít nhất 2 pods vẫn chạy trong quá trình drain
```

### Bài tập 14.2: etcd Backup & Restore

**Yêu cầu:** Backup và restore etcd (critical cho disaster recovery).

**Lời giải:**

```bash
# Trên cụm kubeadm (không phải Minikube):

# Backup etcd
ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Verify backup
ETCDCTL_API=3 etcdctl snapshot status /backup/etcd-snapshot.db --write-table

# Restore etcd
ETCDCTL_API=3 etcdctl snapshot restore /backup/etcd-snapshot.db \
  --data-dir=/var/lib/etcd-restore
```

---

## Phụ Lục A: Kiến Trúc Kubernetes (Lý Thuyết Tham Khảo)

> Đọc sau khi đã thực hành xong Giai đoạn 1-6 để hiểu sâu hơn.

### Control Plane (Master Node)

```
┌──────────────────────────────────────────────┐
│                CONTROL PLANE                  │
│                                              │
│  ┌──────────┐  ┌───────────┐  ┌───────────┐ │
│  │   API     │  │ Scheduler │  │ Controller│ │
│  │  Server   │  │           │  │  Manager  │ │
│  └────┬─────┘  └─────┬─────┘  └─────┬─────┘ │
│       │              │              │        │
│       └──────────────┼──────────────┘        │
│                      │                       │
│              ┌───────┴───────┐               │
│              │     etcd      │               │
│              │ (key-value    │               │
│              │  store)       │               │
│              └───────────────┘               │
└──────────────────────────────────────────────┘
```

| Component | Vai trò |
|-----------|---------|
| **API Server** | Cổng vào duy nhất cho mọi tương tác với cụm |
| **etcd** | Lưu trữ toàn bộ trạng thái cụm (key-value store) |
| **Scheduler** | Quyết định Pod chạy trên Node nào |
| **Controller Manager** | Chạy các vòng lặp điều khiển (Deployment, ReplicaSet, etc.) |
| **Cloud Controller Manager** | Tích hợp với cloud provider (LB, storage, node) |

### Worker Node

```
┌──────────────────────────────────────┐
│            WORKER NODE               │
│                                      │
│  ┌──────────┐  ┌───────────────────┐ │
│  │ Kubelet  │  │ Container Runtime │ │
│  │          │  │ (containerd/CRI-O)│ │
│  └────┬─────┘  └─────────┬────────┘ │
│       │                  │          │
│  ┌────┴──────────────────┴────────┐ │
│  │         Kube-proxy             │ │
│  │   (iptables/IPVS rules)       │ │
│  └────────────────────────────────┘ │
│                                      │
│  ┌─────┐ ┌─────┐ ┌─────┐          │
│  │Pod 1│ │Pod 2│ │Pod 3│   ...    │
│  └─────┘ └─────┘ └─────┘          │
└──────────────────────────────────────┘
```

| Component | Vai trò |
|-----------|---------|
| **Kubelet** | Agent trên mỗi node, quản lý Pod lifecycle |
| **Kube-proxy** | Quản lý network rules cho Service |
| **Container Runtime** | Chạy container (containerd là chuẩn hiện tại, Docker đã deprecated) |

### Networking Model

- **CNI (Container Network Interface)**: Plugin mạng cho K8s.
  - **Calico**: Network policy + routing (phổ biến nhất).
  - **Cilium**: eBPF-based, hiệu năng cao, observability tốt.
  - **Flannel**: Đơn giản, chỉ overlay network.
- **CoreDNS**: DNS server nội bộ, phân giải tên Service → IP.

---

## Phụ Lục B: Lộ Trình Chứng Chỉ CKA/CKAD/CKS

### CKA - Certified Kubernetes Administrator

| Domain | Tỷ trọng | Giai đoạn tương ứng |
|--------|----------|---------------------|
| Cluster Architecture, Installation & Configuration | 25% | GĐ 0, Phụ lục A |
| Workloads & Scheduling | 15% | GĐ 1, 3, 6, 8 |
| Services & Networking | 20% | GĐ 2, 7 |
| Storage | 10% | GĐ 5 |
| Troubleshooting | 30% | GĐ 9 |

### CKAD - Certified Kubernetes Application Developer

| Domain | Tỷ trọng | Giai đoạn tương ứng |
|--------|----------|---------------------|
| Application Design and Build | 20% | GĐ 1, 6 |
| Application Deployment | 20% | GĐ 3, 11 |
| Application Observability and Maintenance | 15% | GĐ 9 |
| Application Environment, Configuration and Security | 25% | GĐ 4, 10 |
| Services & Networking | 20% | GĐ 2, 7 |

### CKS - Certified Kubernetes Security Specialist

| Domain | Tỷ trọng | Giai đoạn tương ứng |
|--------|----------|---------------------|
| Cluster Setup | 10% | GĐ 10, 13 |
| Cluster Hardening | 15% | GĐ 10 |
| System Hardening | 15% | GĐ 10, 13 |
| Minimize Microservice Vulnerabilities | 20% | GĐ 4, 10 |
| Supply Chain Security | 20% | GĐ 12 |
| Monitoring, Logging and Runtime Security | 20% | GĐ 9 |

---

## Phụ Lục C: Công Cụ Hỗ Trợ

| Công cụ | Mục đích | Cài đặt |
|---------|---------|---------|
| **k9s** | TUI quản lý cụm | `brew install k9s` |
| **kubectx/kubens** | Chuyển context/namespace nhanh | `brew install kubectx` |
| **stern** | Multi-pod log tailing | `brew install stern` |
| **kustomize** | Tùy biến YAML | `brew install kustomize` |
| **ArgoCD CLI** | GitOps | `brew install argocd` |
| **Trivy** | Image vulnerability scanner | `brew install trivy` |
| **kubeseal** | Encrypt Secrets (Sealed Secrets) | `brew install kubeseal` |
| **kubectl-neat** | Clean up kubectl output | `kubectl krew install neat` |
| **Lens / OpenLens** | Desktop GUI cho K8s | `brew install --cask lens` |

---

## Tổng Kết Lộ Trình

```
Giai đoạn 0-3:  ████████░░  Beginner     (~2-3 tuần)
  → Pod, Service, Deployment, Scaling

Giai đoạn 4-6:  ████████░░  Intermediate (~2-3 tuần)
  → ConfigMap, Secret, Storage, Workloads

Giai đoạn 7-9:  ████████░░  Advanced     (~3-4 tuần)
  → Ingress/Gateway API, Scheduling, Monitoring

Giai đoạn 10-12: ████████░░  Expert       (~3-4 tuần)
  → Security, Helm, GitOps

Giai đoạn 13-14: ████████░░  Master       (~2-3 tuần)
  → CRD, Operator, Service Mesh, Production
```

**Nguyên tắc học:**
1. **Thực hành trước** - chạy bài tập, quan sát kết quả, rồi mới đọc lý thuyết.
2. **Phá vỡ mọi thứ** - cố tình gây lỗi, xem K8s phản ứng thế nào.
3. **Đọc YAML** - mỗi ngày đọc 1 YAML manifest, hiểu từng field.
4. **Xây dự án thực tế** - deploy ứng dụng microservices hoàn chỉnh.
5. **Thi chứng chỉ** - CKA/CKAD là cách tốt nhất để validate kiến thức.
