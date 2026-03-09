# Lộ Trình Học Docker Toàn Diện — Từ Zero Đến Production

> **Phương châm:** Thực hành trước, lý thuyết sau. Mỗi giai đoạn bắt đầu bằng **LÀM** rồi mới **HIỂU**.
>
> **Đối tượng:** Developer muốn nắm vững Docker từ cơ bản đến chuyên sâu, hướng tới triển khai production thực tế.

---

## Tổng Quan Lộ Trình

| Giai đoạn | Chủ đề | Thời gian đề xuất |
|-----------|--------|-------------------|
| 1 | Chạy container đầu tiên | Ngày 1–3 |
| 2 | Tự build Docker Image (Dockerfile) | Ngày 4–7 |
| 3 | Ứng dụng đa container với Docker Compose | Ngày 8–14 |
| 4 | Dockerfile nâng cao & tối ưu hóa | Ngày 15–21 |
| 5 | Networking chuyên sâu | Ngày 22–28 |
| 6 | Storage & Quản lý dữ liệu | Ngày 29–32 |
| 7 | Bảo mật Docker | Ngày 33–39 |
| 8 | Vận hành Production | Ngày 40–46 |
| 9 | CI/CD với Docker | Ngày 47–53 |
| 10 | BuildKit & Compose nâng cao | Ngày 54–60 |
| 11 | Container Internals (hiểu bản chất) | Ngày 61–67 |
| 12 | Hệ sinh thái & Công cụ thay thế | Ngày 68–74 |
| 13 | Debug & Xử lý sự cố | Liên tục |

---

## Giai đoạn 1: Chạy Container Đầu Tiên (Ngày 1–3)

### LÀM trước

```bash
# Pull và chạy Nginx, truy cập qua trình duyệt
docker pull nginx
docker run -d -p 8080:80 --name web nginx
# Mở http://localhost:8080 để xem kết quả

# Chạy MySQL với biến môi trường
docker run -d \
  --name mydb \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=testdb \
  -p 3306:3306 \
  mysql:8.0

# Chạy Redis
docker run -d --name cache -p 6379:6379 redis:7-alpine

# Quản lý container
docker ps                    # Liệt kê container đang chạy
docker ps -a                 # Liệt kê tất cả (kể cả đã dừng)
docker stop web              # Dừng container
docker start web             # Khởi động lại
docker restart web           # Restart
docker logs web              # Xem log
docker logs -f web           # Xem log real-time
docker rm web                # Xóa container (phải dừng trước)
docker rm -f web             # Buộc xóa container đang chạy

# Quản lý image
docker images                # Liệt kê image
docker rmi nginx             # Xóa image
docker system prune          # Dọn dẹp tài nguyên không dùng
```

### HIỂU sau

- **Container vs VM:** Container chia sẻ kernel của host OS, nhẹ hơn và khởi động nhanh hơn VM rất nhiều. VM ảo hóa toàn bộ phần cứng, container chỉ ảo hóa ở mức process.
- **Vấn đề Docker giải quyết:** "Nó hoạt động trên máy của tôi" — Docker đóng gói ứng dụng cùng toàn bộ môi trường, thư viện và cấu hình vào một container, đảm bảo chạy giống nhau trên mọi môi trường.
- **Vòng đời container:** `created` → `running` → `paused` → `running` → `stopped` → `removed`.
- **DockerHub:** Registry công cộng chứa hàng triệu image sẵn có (MySQL, Nginx, Redis, PostgreSQL...).

### Bài tập 1.1 — Khám phá Container

**Đề bài:** Triển khai 3 container (Nginx, MySQL, Redis) trên cùng một máy, đảm bảo truy cập được từ bên ngoài qua các port khác nhau. Sau đó thực hiện các thao tác quản lý vòng đời container.

**Yêu cầu cụ thể:**
1. Chạy Nginx trên port 8080, MySQL trên port 3307 (tránh xung đột nếu máy đã có MySQL), Redis trên port 6380.
2. Kiểm tra tất cả 3 container đang chạy.
3. Dừng MySQL, xác nhận nó đã dừng nhưng vẫn tồn tại.
4. Khởi động lại MySQL.
5. Xem log của Nginx.
6. Dọn dẹp: xóa tất cả container.

**Lời giải chi tiết:**

```bash
# Bước 1: Chạy 3 container
docker run -d --name nginx-web -p 8080:80 nginx:1.25
docker run -d --name mysql-db -p 3307:3306 \
  -e MYSQL_ROOT_PASSWORD=mypassword \
  -e MYSQL_DATABASE=testdb \
  mysql:8.0
docker run -d --name redis-cache -p 6380:6379 redis:7-alpine

# Bước 2: Kiểm tra
docker ps
# Kết quả: 3 container ở trạng thái "Up"

# Bước 3: Dừng MySQL
docker stop mysql-db
docker ps          # MySQL không còn trong danh sách
docker ps -a       # MySQL vẫn tồn tại với status "Exited"

# Bước 4: Khởi động lại MySQL
docker start mysql-db
docker ps          # MySQL đã trở lại trạng thái "Up"

# Bước 5: Xem log Nginx
docker logs nginx-web
docker logs -f --tail 10 nginx-web   # 10 dòng cuối, real-time

# Bước 6: Dọn dẹp
docker stop nginx-web mysql-db redis-cache
docker rm nginx-web mysql-db redis-cache
# Hoặc gộp:
docker rm -f nginx-web mysql-db redis-cache
```

**Kiểm tra kết quả:**
- Truy cập `http://localhost:8080` → Trang chào Nginx.
- Kết nối MySQL: `mysql -h 127.0.0.1 -P 3307 -u root -pmypassword`.
- Kết nối Redis: `redis-cli -p 6380 ping` → nhận `PONG`.

---

## Giai đoạn 2: Tự Build Docker Image — Dockerfile (Ngày 4–7)

### LÀM trước

**Tạo ứng dụng web đơn giản và đóng gói vào Docker image:**

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Xin chào từ Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```
# requirements.txt
flask==3.0.0
```

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

```
# .dockerignore
.git
__pycache__
*.pyc
.env
.venv
node_modules
```

```bash
# Build và chạy
docker build -t myapp:v1 .
docker run -d -p 5000:5000 --name myapp myapp:v1

# Xem lịch sử layer của image
docker history myapp:v1

# Push lên DockerHub
docker login
docker tag myapp:v1 <username>/myapp:v1
docker push <username>/myapp:v1
```

### HIỂU sau

- **Image layer:** Mỗi chỉ dẫn trong Dockerfile tạo ra một layer. Docker cache các layer — nếu layer không thay đổi, Docker dùng lại cache, giúp build nhanh hơn.
- **Các chỉ dẫn Dockerfile quan trọng:**
  - `FROM` — Chọn image nền (base image).
  - `WORKDIR` — Đặt thư mục làm việc bên trong container.
  - `COPY` / `ADD` — Sao chép file từ host vào image (`ADD` hỗ trợ thêm URL và giải nén tar).
  - `RUN` — Chạy lệnh trong quá trình build (cài đặt packages, compile...).
  - `EXPOSE` — Khai báo port (chỉ là metadata, không thực sự mở port).
  - `CMD` — Lệnh mặc định khi container khởi chạy.
  - `ENV` — Đặt biến môi trường.
- **`.dockerignore`:** Ngăn file không cần thiết (`.git`, `node_modules`, `.env`) bị copy vào build context, giúp build nhanh hơn và bảo mật hơn.
- **Tag image:** Luôn dùng tag cụ thể (`python:3.12-slim`) thay vì `latest` để đảm bảo tính nhất quán.

### Bài tập 2.1 — Đóng gói ứng dụng Node.js

**Đề bài:** Viết một REST API đơn giản bằng Node.js (Express), đóng gói vào Docker image, và push lên DockerHub.

**Yêu cầu:**
1. Tạo API có 2 endpoint: `GET /` trả về `{"message": "Hello Docker"}` và `GET /health` trả về `{"status": "ok"}`.
2. Viết Dockerfile tối ưu (dùng `node:20-slim`, copy `package.json` trước để tận dụng cache).
3. Viết file `.dockerignore` phù hợp.
4. Build image, chạy container, kiểm tra cả 2 endpoint.
5. Dùng `docker history` phân tích các layer.

**Lời giải chi tiết:**

```javascript
// app.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.json({ message: 'Hello Docker' });
});

app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.listen(3000, '0.0.0.0', () => {
  console.log('Server running on port 3000');
});
```

```json
// package.json
{
  "name": "docker-node-app",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.18.0"
  }
}
```

```dockerfile
# Dockerfile
FROM node:20-slim

WORKDIR /app

# Copy package.json trước để tận dụng layer cache
COPY package.json package-lock.json* ./
RUN npm ci --only=production

# Copy source code sau
COPY . .

EXPOSE 3000

CMD ["node", "app.js"]
```

```
# .dockerignore
node_modules
.git
.gitignore
*.md
.env
.dockerignore
Dockerfile
```

```bash
# Build và chạy
docker build -t node-api:v1 .
docker run -d -p 3000:3000 --name node-api node-api:v1

# Kiểm tra
curl http://localhost:3000/
curl http://localhost:3000/health

# Phân tích layer
docker history node-api:v1

# Push lên DockerHub
docker tag node-api:v1 <username>/node-api:v1
docker push <username>/node-api:v1
```

### Bài tập 2.2 — Tối ưu thứ tự layer cache

**Đề bài:** Cho Dockerfile sau (đã cố ý viết sai thứ tự), hãy phân tích vấn đề và sửa lại để tối ưu cache.

```dockerfile
# Dockerfile CẦN TỐI ƯU
FROM python:3.12
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y curl
EXPOSE 8000
CMD ["python", "app.py"]
```

**Lời giải:**

Vấn đề: Mỗi khi thay đổi bất kỳ file nào trong source code, `COPY . /app` ở dòng 2 sẽ phá cache, buộc tất cả các bước phía sau (bao gồm `pip install` và `apt-get install`) phải chạy lại.

```dockerfile
# Dockerfile ĐÃ TỐI ƯU
FROM python:3.12-slim

# Cài đặt system dependencies trước (ít thay đổi nhất)
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy file dependency trước (chỉ thay đổi khi thêm/xóa package)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code cuối cùng (thay đổi thường xuyên nhất)
COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
```

**Nguyên tắc:** Sắp xếp từ ít thay đổi nhất → thay đổi nhiều nhất. System packages → app dependencies → source code.

---

## Giai đoạn 3: Ứng Dụng Đa Container với Docker Compose (Ngày 8–14)

### LÀM trước

**Triển khai ứng dụng 3 tầng: Frontend + Backend + Database**

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d myapp"]
      interval: 5s
      timeout: 3s
      retries: 5

  api:
    build: ./api
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgres://admin:secret@db:5432/myapp
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped

  frontend:
    build: ./frontend
    ports:
      - "8080:80"
    depends_on:
      - api

volumes:
  pgdata:
```

```bash
# Khởi chạy toàn bộ stack
docker compose up -d

# Xem log tất cả services
docker compose logs -f

# Xem log của một service cụ thể
docker compose logs -f api

# Xem trạng thái
docker compose ps

# Dừng toàn bộ
docker compose down

# Dừng và xóa cả volumes (cẩn thận: mất dữ liệu!)
docker compose down -v
```

### HIỂU sau

- **Docker Compose:** Công cụ định nghĩa và chạy ứng dụng đa container bằng file YAML. Thay vì chạy từng `docker run` riêng lẻ, chỉ cần một lệnh `docker compose up`.
- **Docker Networking trong Compose:**
  - Compose tự động tạo một network cho tất cả services.
  - Container giao tiếp với nhau bằng **tên service** (ví dụ: `db`, `api`) — Docker tự resolve DNS.
  - Không cần biết IP, chỉ cần dùng tên service làm hostname.
- **`depends_on` với healthcheck:** Đảm bảo service A chỉ khởi động khi service B đã **thực sự sẵn sàng** (không chỉ "đã chạy").
- **`volumes`:** Dữ liệu trong container là tạm thời — khi xóa container, dữ liệu mất. Volume giúp dữ liệu tồn tại bền vững (persistent).
- **`restart: unless-stopped`:** Tự động khởi động lại container khi nó crash hoặc khi Docker daemon khởi động lại.

### Bài tập 3.1 — Triển khai stack WordPress hoàn chỉnh

**Đề bài:** Sử dụng Docker Compose triển khai WordPress với MySQL, phpMyAdmin và Nginx reverse proxy.

**Yêu cầu:**
1. MySQL làm database, dữ liệu lưu trữ bền vững qua volume.
2. WordPress kết nối MySQL.
3. phpMyAdmin để quản lý database qua giao diện web.
4. Nginx làm reverse proxy, route traffic đến WordPress.
5. Tất cả service dùng `healthcheck`.
6. Dùng file `.env` cho các biến nhạy cảm.

**Lời giải chi tiết:**

```
# .env
MYSQL_ROOT_PASSWORD=rootsecret
MYSQL_DATABASE=wordpress
MYSQL_USER=wpuser
MYSQL_PASSWORD=wpsecret
```

```yaml
# docker-compose.yml
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - backend
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p${MYSQL_ROOT_PASSWORD}"]
      interval: 10s
      timeout: 5s
      retries: 5

  wordpress:
    image: wordpress:6-php8.2-fpm
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: ${MYSQL_USER}
      WORDPRESS_DB_PASSWORD: ${MYSQL_PASSWORD}
      WORDPRESS_DB_NAME: ${MYSQL_DATABASE}
    volumes:
      - wp_data:/var/www/html
    networks:
      - backend
      - frontend
    depends_on:
      db:
        condition: service_healthy

  nginx:
    image: nginx:1.25-alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - wp_data:/var/www/html:ro
    networks:
      - frontend
    depends_on:
      - wordpress

  phpmyadmin:
    image: phpmyadmin:5
    ports:
      - "8081:80"
    environment:
      PMA_HOST: db
      PMA_USER: root
      PMA_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    networks:
      - backend
    depends_on:
      db:
        condition: service_healthy

volumes:
  mysql_data:
  wp_data:

networks:
  frontend:
  backend:
```

```nginx
# nginx.conf
server {
    listen 80;
    server_name localhost;
    root /var/www/html;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        fastcgi_pass wordpress:9000;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```

```bash
# Khởi chạy
docker compose up -d

# Kiểm tra
docker compose ps
curl http://localhost        # WordPress
curl http://localhost:8081   # phpMyAdmin
```

### Bài tập 3.2 — Voting App (ứng dụng microservices)

**Đề bài:** Xây dựng ứng dụng bình chọn gồm 5 services:
- **vote** (Python/Flask): Giao diện bình chọn giữa 2 lựa chọn.
- **result** (Node.js): Hiển thị kết quả bình chọn real-time.
- **worker** (.NET/Java): Xử lý phiếu bầu từ Redis, lưu vào PostgreSQL.
- **redis**: Hàng đợi message tạm thời.
- **db** (PostgreSQL): Lưu trữ kết quả cuối cùng.

**Yêu cầu:**
1. Viết `docker-compose.yml` định nghĩa 5 services.
2. Tạo 2 network riêng biệt: `front-tier` (vote, result) và `back-tier` (vote, result, worker, redis, db).
3. Đảm bảo dữ liệu PostgreSQL persistent.
4. Service `worker` chỉ khởi chạy khi cả Redis và PostgreSQL đã healthy.

**Lời giải chi tiết:**

```yaml
# docker-compose.yml
services:
  vote:
    image: dockersamples/examplevotingapp_vote
    ports:
      - "5001:80"
    networks:
      - front-tier
      - back-tier
    depends_on:
      redis:
        condition: service_healthy

  result:
    image: dockersamples/examplevotingapp_result
    ports:
      - "5002:80"
    networks:
      - front-tier
      - back-tier
    depends_on:
      db:
        condition: service_healthy

  worker:
    image: dockersamples/examplevotingapp_worker
    networks:
      - back-tier
    depends_on:
      redis:
        condition: service_healthy
      db:
        condition: service_healthy

  redis:
    image: redis:7-alpine
    networks:
      - back-tier
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - back-tier
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 3s
      retries: 5

volumes:
  db-data:

networks:
  front-tier:
  back-tier:
```

```bash
docker compose up -d
# Truy cập http://localhost:5001 để bình chọn
# Truy cập http://localhost:5002 để xem kết quả
```

---

## Giai đoạn 4: Dockerfile Nâng Cao & Tối Ưu Hóa (Ngày 15–21)

### LÀM trước

**Multi-stage build — Giảm image từ 1GB xuống dưới 50MB:**

```dockerfile
# --- Stage 1: Build ---
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# --- Stage 2: Production ---
FROM node:20-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./

# Chạy bằng user không phải root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

CMD ["node", "dist/main.js"]
```

**ENTRYPOINT vs CMD:**

```dockerfile
# CMD: Lệnh mặc định, có thể bị ghi đè hoàn toàn
CMD ["python", "app.py"]
# docker run myapp python other_script.py  → chạy other_script.py

# ENTRYPOINT: Lệnh cố định, CMD trở thành tham số mặc định
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run myapp            → python app.py
# docker run myapp other.py   → python other.py
```

**ARG vs ENV:**

```dockerfile
# ARG: Chỉ tồn tại lúc build, không có trong container chạy
ARG APP_VERSION=1.0.0
RUN echo "Building version $APP_VERSION"

# ENV: Tồn tại cả lúc build và lúc container chạy
ENV NODE_ENV=production
```

### HIỂU sau

- **Multi-stage build:** Cho phép dùng nhiều `FROM` trong một Dockerfile. Stage đầu để build/compile, stage cuối chỉ copy kết quả build — giảm kích thước image và loại bỏ build tools không cần thiết.
- **Chọn base image:**
  - `alpine` — Siêu nhẹ (~5MB), dùng `musl` libc, có thể gây lỗi tương thích.
  - `slim` (Debian-slim) — Nhẹ (~80MB), tương thích tốt hơn Alpine.
  - `distroless` (Google) — Không có shell, không có package manager, chỉ có runtime. Bảo mật cao nhất.
  - `scratch` — Image rỗng, chỉ dùng cho binary static (Go, Rust).
- **HEALTHCHECK:** Docker kiểm tra định kỳ xem container có hoạt động đúng không. Orchestrator (Compose, Kubernetes) dùng kết quả này để tự restart container không khỏe mạnh.
- **Exec form vs Shell form:**
  - Exec form `["python", "app.py"]` — Chạy trực tiếp, nhận signal (SIGTERM) đúng cách, nên dùng.
  - Shell form `python app.py` — Chạy qua `/bin/sh -c`, không nhận signal trực tiếp, tránh dùng cho CMD/ENTRYPOINT.
- **`LABEL`:** Thêm metadata cho image (author, version, description) — hữu ích cho quản lý và automation.
- **`STOPSIGNAL`:** Thay đổi signal mặc định khi dừng container (mặc định là `SIGTERM`).

### Bài tập 4.1 — Thử thách tối ưu kích thước image

**Đề bài:** Cho ứng dụng Go sau, hãy viết Dockerfile tối ưu nhất có thể. Mục tiêu: image cuối cùng **dưới 10MB**.

```go
// main.go
package main

import (
    "fmt"
    "net/http"
    "os"
)

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        hostname, _ := os.Hostname()
        fmt.Fprintf(w, "Hello from container: %s\n", hostname)
    })

    http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        fmt.Fprint(w, "OK")
    })

    fmt.Printf("Server starting on port %s\n", port)
    http.ListenAndServe(":"+port, nil)
}
```

**Lời giải chi tiết:**

```dockerfile
# Stage 1: Build
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod ./
COPY main.go ./
# Build static binary (không phụ thuộc thư viện C)
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o server .

# Stage 2: Scratch image (image rỗng)
FROM scratch
COPY --from=builder /app/server /server
EXPOSE 8080
ENTRYPOINT ["/server"]
```

```bash
docker build -t go-app:optimized .
docker images go-app:optimized
# SIZE: ~6-7MB

# So sánh với build naive
docker build -t go-app:naive -f Dockerfile.naive .
# SIZE: ~300MB+ (nếu dùng FROM golang:1.22)
```

**Giải thích kỹ thuật:**
- `CGO_ENABLED=0` — Tắt CGO, build static binary không cần thư viện C.
- `-ldflags="-s -w"` — Loại bỏ symbol table và debug info, giảm kích thước binary.
- `FROM scratch` — Image rỗng hoàn toàn, chỉ chứa file binary.

### Bài tập 4.2 — Dockerfile cho ứng dụng Java Spring Boot

**Đề bài:** Viết Dockerfile multi-stage cho ứng dụng Spring Boot với các yêu cầu:
1. Stage build dùng Maven.
2. Stage test chạy unit test (build fail nếu test fail).
3. Stage production dùng Eclipse Temurin JRE, non-root user, healthcheck.

**Lời giải chi tiết:**

```dockerfile
# Stage 1: Build dependencies (cached)
FROM maven:3.9-eclipse-temurin-21 AS deps
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Stage 2: Build & Test
FROM deps AS builder
COPY src ./src
# Chạy test, nếu fail thì build dừng lại
RUN mvn package -B

# Stage 3: Production
FROM eclipse-temurin:21-jre-alpine AS production
WORKDIR /app

RUN addgroup -S spring && adduser -S spring -G spring

COPY --from=builder /app/target/*.jar app.jar
RUN chown spring:spring app.jar

USER spring

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=30s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/actuator/health || exit 1

ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

## Giai đoạn 5: Networking Chuyên Sâu (Ngày 22–28)

### LÀM trước

```bash
# 1. Bridge Network (mặc định) — tạo network riêng
docker network create mynet
docker run -d --name app1 --network mynet nginx
docker run -d --name app2 --network mynet nginx

# Container có thể giao tiếp bằng tên
docker exec app1 ping app2          # Thành công!
docker exec app1 curl http://app2   # Thành công!

# 2. Host Network — không có network isolation
docker run -d --network host --name host-nginx nginx
# Nginx lắng nghe trực tiếp trên port 80 của host, không cần -p

# 3. None Network — hoàn toàn cô lập
docker run -d --network none --name isolated alpine sleep 3600
docker exec isolated ping google.com  # Thất bại — không có mạng

# 4. Kiểm tra chi tiết network
docker network ls
docker network inspect mynet

# 5. Kết nối container vào nhiều network
docker network create frontend-net
docker network create backend-net
docker run -d --name api --network backend-net nginx
docker network connect frontend-net api
# Container "api" bây giờ thuộc cả 2 network

# Dọn dẹp
docker network prune
```

### HIỂU sau

- **Các loại network driver:**
  - `bridge` — Mặc định. Tạo network ảo, container giao tiếp qua DNS (tên container). Dùng cho single-host.
  - `host` — Container chia sẻ network stack với host. Hiệu năng cao nhất, nhưng không có network isolation.
  - `overlay` — Kết nối container trên nhiều host khác nhau (dùng VXLAN). Cần cho Docker Swarm/Kubernetes.
  - `macvlan` — Container nhận địa chỉ MAC riêng, xuất hiện như thiết bị vật lý trên LAN. Dùng cho legacy app cần truy cập trực tiếp từ mạng vật lý.
  - `ipvlan` — Tương tự macvlan nhưng chia sẻ MAC address (L2/L3 mode).
  - `none` — Không có network, hoàn toàn cô lập.
- **DNS Resolution:** Trong user-defined bridge network, Docker tự động cung cấp DNS — container có thể gọi nhau bằng tên. Default bridge network **không** có tính năng này.
- **Port mapping:** `-p hostPort:containerPort`. Dùng `-p 8080:80` để map port 80 của container ra port 8080 của host.

### Bài tập 5.1 — Thiết kế mạng cho hệ thống Microservices

**Đề bài:** Thiết kế và triển khai network architecture cho hệ thống:
- **Gateway** (Nginx) — Nhận traffic từ bên ngoài.
- **Auth Service** — Xác thực người dùng.
- **Product Service** — Quản lý sản phẩm.
- **Order Service** — Quản lý đơn hàng.
- **PostgreSQL** — Database chung.
- **Redis** — Cache chung.

**Yêu cầu bảo mật:**
- Chỉ Gateway được truy cập từ bên ngoài.
- Database và Redis chỉ được truy cập từ các service nội bộ.
- Auth Service được truy cập bởi tất cả service khác.

**Lời giải chi tiết:**

```yaml
# docker-compose.yml
services:
  gateway:
    image: nginx:1.25-alpine
    ports:
      - "80:80"
    networks:
      - public
      - services
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro

  auth:
    build: ./auth-service
    networks:
      - services
      - data

  product:
    build: ./product-service
    networks:
      - services
      - data

  order:
    build: ./order-service
    networks:
      - services
      - data

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - data

  redis:
    image: redis:7-alpine
    networks:
      - data

volumes:
  pgdata:

networks:
  public:      # Chỉ gateway kết nối ra ngoài
  services:    # Giao tiếp giữa các service
  data:        # Truy cập database/cache
```

**Kết quả:**
- `gateway` ∈ {public, services} → nhận traffic ngoài, forward đến services.
- `auth`, `product`, `order` ∈ {services, data} → gọi nhau và truy cập DB/cache.
- `postgres`, `redis` ∈ {data} → chỉ service nội bộ truy cập được.
- Từ bên ngoài, **không thể** truy cập trực tiếp `postgres` hoặc `redis`.

---

## Giai đoạn 6: Storage & Quản Lý Dữ Liệu (Ngày 29–32)

### LÀM trước

```bash
# 1. Named Volume — Docker quản lý, persistent
docker volume create mydata
docker run -d --name db -v mydata:/var/lib/postgresql/data postgres:16
docker rm -f db
# Dữ liệu vẫn còn trong volume "mydata"
docker run -d --name db2 -v mydata:/var/lib/postgresql/data postgres:16
# db2 sẽ có dữ liệu của db cũ!

# 2. Bind Mount — Mount thư mục từ host
docker run -d --name web \
  -v $(pwd)/html:/usr/share/nginx/html:ro \
  -p 8080:80 nginx
# Thay đổi file trong ./html sẽ phản ánh ngay trong container

# 3. tmpfs Mount — Chỉ lưu trong RAM
docker run -d --name secure \
  --tmpfs /tmp:rw,noexec,nosuid,size=100m \
  nginx

# 4. Quản lý volume
docker volume ls
docker volume inspect mydata
docker volume rm mydata
docker volume prune          # Xóa volume không được dùng

# 5. Backup volume
docker run --rm \
  -v mydata:/source:ro \
  -v $(pwd):/backup \
  alpine tar czf /backup/mydata-backup.tar.gz -C /source .

# 6. Restore volume
docker volume create mydata-restored
docker run --rm \
  -v mydata-restored:/target \
  -v $(pwd):/backup:ro \
  alpine tar xzf /backup/mydata-backup.tar.gz -C /target
```

### HIỂU sau

- **3 loại mount trong Docker:**
  - **Named Volume:** Docker quản lý hoàn toàn, lưu trong `/var/lib/docker/volumes/`. Phù hợp cho database, dữ liệu ứng dụng.
  - **Bind Mount:** Mount trực tiếp thư mục/file từ host. Phù hợp cho development (hot reload), config file.
  - **tmpfs Mount:** Lưu trong RAM, nhanh nhất nhưng mất khi container dừng. Phù hợp cho dữ liệu nhạy cảm tạm thời, cache.
- **Read-only mount (`:ro`):** Ngăn container ghi vào volume — quan trọng cho bảo mật (config files, static assets).
- **Volume drivers:** Ngoài `local`, có thể dùng NFS, cloud storage (AWS EBS, Azure Disk) qua volume driver plugins.
- **Anonymous volume:** Tạo khi dùng `VOLUME` trong Dockerfile hoặc `-v /path` không có tên. Khó quản lý, tránh dùng trong production.

### Bài tập 6.1 — Backup & Restore Database

**Đề bài:** Thiết lập PostgreSQL với volume, thêm dữ liệu, thực hiện backup, xóa hoàn toàn container và volume, rồi restore lại từ backup.

**Lời giải chi tiết:**

```bash
# Bước 1: Khởi chạy PostgreSQL với named volume
docker run -d --name pg \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=testdb \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16-alpine

# Bước 2: Thêm dữ liệu
docker exec -i pg psql -U postgres -d testdb <<EOF
CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT, email TEXT);
INSERT INTO users (name, email) VALUES
  ('Nguyen Van A', 'a@example.com'),
  ('Tran Thi B', 'b@example.com'),
  ('Le Van C', 'c@example.com');
EOF

# Xác nhận dữ liệu
docker exec pg psql -U postgres -d testdb -c "SELECT * FROM users;"

# Bước 3: Backup
docker run --rm \
  -v pgdata:/source:ro \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/pgdata-$(date +%Y%m%d).tar.gz -C /source .

# Bước 4: Xóa hoàn toàn
docker rm -f pg
docker volume rm pgdata

# Bước 5: Restore
docker volume create pgdata
docker run --rm \
  -v pgdata:/target \
  -v $(pwd)/backups:/backup:ro \
  alpine sh -c "tar xzf /backup/pgdata-*.tar.gz -C /target"

# Bước 6: Khởi chạy PostgreSQL mới với volume đã restore
docker run -d --name pg-restored \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16-alpine

# Xác nhận dữ liệu đã được phục hồi
docker exec pg-restored psql -U postgres -d testdb -c "SELECT * FROM users;"
```

---

## Giai đoạn 7: Bảo Mật Docker (Ngày 33–39)

### LÀM trước

```bash
# 1. Chạy container KHÔNG phải root
docker run -d --name secure-app \
  --user 1000:1000 \
  nginx

# 2. Read-only filesystem
docker run -d --name readonly-app \
  --read-only \
  --tmpfs /tmp \
  --tmpfs /var/cache/nginx \
  --tmpfs /var/run \
  nginx

# 3. Drop tất cả capabilities, chỉ add những gì cần
docker run -d --name cap-app \
  --cap-drop ALL \
  --cap-add NET_BIND_SERVICE \
  nginx

# 4. Không cho phép leo quyền
docker run -d --name noprivesc \
  --security-opt no-new-privileges \
  nginx

# 5. Quét lỗ hổng bảo mật với Trivy
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image nginx:1.25

# Hoặc dùng Docker Scout
docker scout cves nginx:1.25

# 6. Dùng BuildKit secret mount (không bao giờ lưu secret vào layer)
docker build --secret id=mytoken,src=./token.txt -t secure-build .
```

```dockerfile
# Dockerfile sử dụng secret mount
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
# Secret chỉ tồn tại trong lúc RUN, không lưu vào layer
RUN --mount=type=secret,id=mytoken \
    NPM_TOKEN=$(cat /run/secrets/mytoken) npm ci
COPY . .
CMD ["node", "app.js"]
```

### HIỂU sau

- **Tại sao không chạy root?** Nếu attacker thoát ra khỏi container (container escape), quyền root trong container = quyền root trên host. Dùng non-root user giảm blast radius.
- **Linux Capabilities:** Thay vì cho full root privileges, Linux chia nhỏ thành các capability (NET_BIND_SERVICE, SYS_ADMIN, ...). `--cap-drop ALL` bỏ hết, chỉ `--cap-add` những gì cần.
- **Read-only filesystem:** Ngăn attacker ghi file lên filesystem (webshell, backdoor). Cần `tmpfs` cho thư mục ứng dụng phải ghi (tmp, cache, pid file).
- **Docker Content Trust (DCT):** Xác minh image đã được ký bởi publisher. Bật: `export DOCKER_CONTENT_TRUST=1`.
- **Trivy / Docker Scout:** Quét image để phát hiện CVE (lỗ hổng bảo mật đã biết) trong OS packages và application dependencies.
- **Secret mount trong BuildKit:** `--mount=type=secret` cho phép truy cập file bí mật trong quá trình build mà không lưu vào image layer — an toàn hơn nhiều so với `COPY` hoặc `ARG`.
- **Seccomp profile:** Giới hạn system call mà container có thể gọi. Docker có default profile chặn ~44 syscall nguy hiểm.
- **no-new-privileges:** Ngăn process trong container leo thang quyền (ví dụ: setuid binary).

### Bài tập 7.1 — Hardening một Dockerfile có lỗ hổng

**Đề bài:** Cho Dockerfile sau chứa nhiều vấn đề bảo mật. Hãy phân tích và sửa tất cả.

```dockerfile
# Dockerfile CÓ LỖ HỔNG
FROM ubuntu:latest
ENV DB_PASSWORD=supersecret123
COPY . /app
RUN apt-get update && apt-get install -y python3 python3-pip curl
RUN pip3 install -r /app/requirements.txt
EXPOSE 8000
CMD python3 /app/app.py
```

**Lời giải chi tiết — phân tích từng vấn đề:**

| # | Vấn đề | Mức độ | Giải pháp |
|---|--------|--------|-----------|
| 1 | `FROM ubuntu:latest` — Tag `latest` không ổn định | Trung bình | Dùng tag cụ thể, dùng image slim |
| 2 | `ENV DB_PASSWORD=supersecret123` — Secret bị lộ trong image layer | **Nghiêm trọng** | Dùng runtime env hoặc secret mount |
| 3 | `COPY . /app` trước khi cài deps — Phá cache | Thấp | Tách riêng COPY requirements |
| 4 | Không dọn dẹp apt cache — Tăng kích thước | Thấp | Thêm `rm -rf /var/lib/apt/lists/*` |
| 5 | Chạy dưới quyền root | **Nghiêm trọng** | Tạo và dùng non-root user |
| 6 | Shell form CMD — Không nhận SIGTERM | Trung bình | Dùng exec form |
| 7 | Không có HEALTHCHECK | Trung bình | Thêm HEALTHCHECK |
| 8 | Không có `.dockerignore` | Trung bình | Tạo .dockerignore |

```dockerfile
# Dockerfile ĐÃ HARDENING
FROM python:3.12-slim AS production

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Tạo non-root user
RUN groupadd -r appuser && useradd -r -g appuser -d /app -s /sbin/nologin appuser

WORKDIR /app

# Cài dependencies trước (cache-friendly)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY --chown=appuser:appuser . .

# Chuyển sang non-root user
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Exec form, nhận SIGTERM đúng cách
CMD ["python3", "app.py"]
```

```
# .dockerignore
.git
.env
*.pyc
__pycache__
.venv
Dockerfile
docker-compose.yml
*.md
.dockerignore
```

```bash
# Chạy container với hardening bổ sung
docker run -d \
  --name secure-app \
  --read-only \
  --tmpfs /tmp \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -e DB_PASSWORD=supersecret123 \
  -p 8000:8000 \
  myapp:secure
```

---

## Giai đoạn 8: Vận Hành Production (Ngày 40–46)

### LÀM trước

**Giới hạn tài nguyên:**

```bash
# Giới hạn memory (container bị OOM kill nếu vượt)
docker run -d --name limited \
  --memory 256m \
  --memory-swap 512m \
  nginx

# Giới hạn CPU
docker run -d --name cpu-limited \
  --cpus 0.5 \
  --cpu-shares 512 \
  nginx

# Giới hạn PID (chống fork bomb)
docker run -d --name pid-limited \
  --pids-limit 100 \
  nginx

# Theo dõi tài nguyên real-time
docker stats

# Thay đổi giới hạn container đang chạy
docker update --memory 512m --cpus 1.0 limited
```

**Logging:**

```bash
# Xem log với timestamp
docker logs --timestamps --since 1h myapp

# Cấu hình log driver khi chạy container
docker run -d \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  --name myapp nginx

# Cấu hình log rotation mặc định trong daemon.json
# /etc/docker/daemon.json
# {
#   "log-driver": "json-file",
#   "log-opts": {
#     "max-size": "10m",
#     "max-file": "5"
#   }
# }
```

**Monitoring stack:**

```yaml
# docker-compose.monitoring.yml
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.retention.time=15d'

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      GF_SECURITY_ADMIN_PASSWORD: admin

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'

volumes:
  prometheus_data:
  grafana_data:
```

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
```

### HIỂU sau

- **Resource limits:**
  - `--memory` — Hard limit. Container bị OOM kill nếu vượt quá.
  - `--memory-reservation` — Soft limit. Docker cố gắng giữ nhưng không bắt buộc.
  - `--cpus` — Số CPU core tối đa (ví dụ: `0.5` = 50% một core).
  - `--pids-limit` — Giới hạn số process, chống fork bomb.
- **Log driver:** Docker hỗ trợ nhiều log driver: `json-file` (mặc định), `syslog`, `fluentd`, `awslogs`, `splunk`, `gelf`. Trong production, nên dùng centralized logging (ELK, Loki, Fluentd).
- **Log rotation:** QUAN TRỌNG trong production! Nếu không cấu hình, log sẽ chiếm hết disk. Dùng `max-size` và `max-file`.
- **Monitoring:**
  - **cAdvisor:** Thu thập metrics từ Docker containers (CPU, memory, network, I/O).
  - **Prometheus:** Time-series database, scrape metrics từ cAdvisor và các exporter.
  - **Grafana:** Dashboard trực quan hóa metrics từ Prometheus.
  - **Node Exporter:** Thu thập metrics từ host machine (CPU, RAM, disk, network).
- **Docker events:** `docker events` — stream real-time tất cả event (create, start, stop, die...) của Docker daemon. Hữu ích cho audit và troubleshooting.

### Bài tập 8.1 — Triển khai monitoring stack hoàn chỉnh

**Đề bài:** Triển khai stack monitoring gồm Prometheus + cAdvisor + Grafana + Node Exporter. Sau đó:
1. Chạy một ứng dụng web và quan sát metrics.
2. Giới hạn memory 128MB cho ứng dụng, rồi cố tình gây OOM kill.
3. Quan sát hiện tượng trên Grafana dashboard.

**Lời giải:**

```bash
# Bước 1: Khởi chạy monitoring stack
docker compose -f docker-compose.monitoring.yml up -d

# Bước 2: Chạy ứng dụng với giới hạn memory
docker run -d --name stress-app \
  --memory 128m \
  --memory-swap 128m \
  python:3.12-slim \
  python -c "
data = []
while True:
    data.append('x' * 10**6)  # Cấp phát 1MB mỗi lần
"

# Bước 3: Quan sát
docker stats stress-app       # Xem memory tăng dần
docker events --filter container=stress-app  # Thấy event OOM kill

# Bước 4: Mở Grafana (http://localhost:3000)
# Import dashboard ID 893 (Docker monitoring) từ Grafana Labs
```

---

## Giai đoạn 9: CI/CD với Docker (Ngày 47–53)

### LÀM trước

**GitHub Actions pipeline hoàn chỉnh:**

```yaml
# .github/workflows/docker.yml
name: Build and Push Docker Image

on:
  push:
    branches: [main]
    tags: ['v*']
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata (tags, labels)
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=ref,event=branch

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          context: .
          platforms: linux/amd64,linux/arm64
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Scan for vulnerabilities
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload scan results
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'
```

### HIỂU sau

- **Multi-platform build:** `docker buildx` cho phép build image cho nhiều kiến trúc (amd64, arm64) từ một Dockerfile. Quan trọng khi deploy trên cả x86 server và ARM (Apple Silicon, Graviton).
- **Tag strategy:**
  - Git SHA — Truy vết chính xác commit nào tạo image.
  - SemVer (v1.2.3) — Quản lý phiên bản release.
  - Branch name — Cho development/staging.
  - **KHÔNG** dùng `latest` trong production.
- **Build cache trong CI:** Dùng GitHub Actions cache (`type=gha`) hoặc registry cache (`type=registry`) để tránh rebuild toàn bộ mỗi lần push.
- **Docker-in-Docker vs Socket mounting vs Kaniko:**
  - **DinD:** Chạy Docker daemon trong Docker. Cần `--privileged`, kém bảo mật.
  - **Socket mounting:** Mount `/var/run/docker.sock`. Đơn giản nhưng có rủi ro bảo mật (truy cập toàn bộ Docker daemon).
  - **Kaniko:** Build image không cần Docker daemon. An toàn nhất cho CI.
- **Build-once-deploy-many:** Build image một lần, dùng environment variables để cấu hình cho từng môi trường (dev, staging, production). Không build lại image cho mỗi môi trường.

### Bài tập 9.1 — Xây dựng CI/CD pipeline hoàn chỉnh

**Đề bài:** Tạo GitHub Actions workflow cho một ứng dụng Node.js:
1. Chạy lint và test trong container.
2. Build multi-platform image (amd64 + arm64).
3. Quét lỗ hổng bảo mật.
4. Push lên GitHub Container Registry với tag strategy: git SHA + semver.
5. Chỉ push khi merge vào main hoặc tạo tag.

**Lời giải:** Xem phần "GitHub Actions pipeline hoàn chỉnh" ở trên, bổ sung thêm step test:

```yaml
      - name: Run tests in container
        run: |
          docker build --target test -t myapp:test .
          docker run --rm myapp:test npm test
```

Dockerfile cần thêm test stage:

```dockerfile
FROM node:20-slim AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM deps AS test
COPY . .
RUN npm run lint
CMD ["npm", "test"]

FROM deps AS builder
COPY . .
RUN npm run build

FROM node:20-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules ./node_modules
USER node
CMD ["node", "dist/main.js"]
```

---

## Giai đoạn 10: BuildKit & Compose Nâng Cao (Ngày 54–60)

### LÀM trước

**BuildKit cache mount — Tăng tốc build 10x:**

```dockerfile
# Thay vì: RUN npm ci (tải lại toàn bộ node_modules mỗi lần)
# Dùng cache mount:
RUN --mount=type=cache,target=/root/.npm \
    npm ci

# Python:
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Go:
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    go build -o /app/server .

# Maven:
RUN --mount=type=cache,target=/root/.m2 \
    mvn package -B
```

**BuildKit SSH mount — Clone private repo trong build:**

```dockerfile
RUN --mount=type=ssh \
    git clone git@github.com:company/private-lib.git
```

```bash
docker build --ssh default -t myapp .
```

**Docker Compose profiles — Khác nhau theo môi trường:**

```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports:
      - "3000:3000"

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data

  # Chỉ bật trong development
  adminer:
    image: adminer
    ports:
      - "8080:8080"
    profiles:
      - dev

  # Chỉ bật cho debugging
  mailhog:
    image: mailhog/mailhog
    ports:
      - "1025:1025"
      - "8025:8025"
    profiles:
      - dev
      - debug

  # Chỉ bật trong môi trường monitoring
  prometheus:
    image: prom/prometheus
    profiles:
      - monitoring

volumes:
  pgdata:
```

```bash
# Chỉ chạy app + db
docker compose up -d

# Chạy app + db + adminer + mailhog (dev mode)
docker compose --profile dev up -d

# Chạy tất cả bao gồm monitoring
docker compose --profile dev --profile monitoring up -d
```

**Docker Compose watch — Hot reload cho development:**

```yaml
services:
  app:
    build: .
    develop:
      watch:
        # Sync source code (hot reload)
        - action: sync
          path: ./src
          target: /app/src

        # Rebuild khi dependencies thay đổi
        - action: rebuild
          path: ./package.json

        # Sync + restart khi config thay đổi
        - action: sync+restart
          path: ./config
          target: /app/config
```

```bash
docker compose watch
# Tự động sync file khi bạn sửa code, không cần restart container
```

### HIỂU sau

- **BuildKit:** Build engine mới của Docker (mặc định từ Docker Engine 23.0+). Nhanh hơn nhờ parallel execution, hỗ trợ cache mount, secret mount, SSH mount.
- **Cache mount:** Mount thư mục cache giữa các lần build. Package manager (npm, pip, maven, go) không cần tải lại từ đầu mỗi lần build.
- **Compose profiles:** Cho phép bật/tắt services theo môi trường. Service không có profile luôn chạy. Service có profile chỉ chạy khi profile được kích hoạt.
- **Compose watch:** Thay thế bind mount + volume watch. Docker tự sync file từ host vào container khi phát hiện thay đổi. 3 action: `sync` (copy file), `rebuild` (build lại image), `sync+restart` (copy file rồi restart container).
- **Compose extends:** Kế thừa cấu hình service, giảm trùng lặp.
- **Multiple Compose files:** Override pattern — `docker-compose.yml` (base) + `docker-compose.override.yml` (local overrides). Docker tự merge 2 file.

---

## Giai đoạn 11: Container Internals — Hiểu Bản Chất (Ngày 61–67)

### LÀM trước

**Tạo "container" thủ công không dùng Docker:**

```bash
# Tạo namespace riêng cho process (cần root)
sudo unshare --pid --fork --mount-proc bash
# Bạn đang ở trong PID namespace mới
ps aux  # Chỉ thấy bash và ps — không thấy process của host

# Xem namespace của container đang chạy
docker run -d --name test alpine sleep 3600
PID=$(docker inspect -f '{{.State.Pid}}' test)
ls -la /proc/$PID/ns/  # Liệt kê tất cả namespace

# Xem cgroup của container
cat /proc/$PID/cgroup
ls /sys/fs/cgroup/docker/$(docker inspect -f '{{.Id}}' test)/

# Vào namespace của container từ host
sudo nsenter -t $PID -m -u -i -n -p bash
# Bạn đang "bên trong" container nhưng không qua docker exec

# Xem filesystem overlay
docker inspect test | grep -A 10 GraphDriver
# Thấy LowerDir, UpperDir, MergedDir, WorkDir
```

### HIỂU sau

- **Container = Process + Isolation:** Container KHÔNG phải VM. Nó là process Linux thường, được cô lập bằng các cơ chế kernel.
- **Linux Namespaces — Cô lập tài nguyên:**
  - `pid` — Process ID riêng (PID 1 trong container).
  - `net` — Network stack riêng (interfaces, IP, routes, iptables).
  - `mnt` — Mount point riêng (filesystem riêng).
  - `uts` — Hostname riêng.
  - `ipc` — Inter-process communication riêng.
  - `user` — User/group ID mapping riêng.
  - `cgroup` — Cgroup view riêng.
- **cgroups — Giới hạn tài nguyên:**
  - Kiểm soát CPU, memory, I/O, network, PID mà process group có thể dùng.
  - cgroups v2 (unified hierarchy) — Phiên bản mới, đơn giản hơn v1.
  - Đây là cơ chế backend cho `--memory`, `--cpus`, `--pids-limit`.
- **Union Filesystem (OverlayFS):**
  - Image layers là read-only (LowerDir).
  - Container layer là read-write (UpperDir).
  - MergedDir là view hợp nhất mà container nhìn thấy.
  - Khi container ghi file, dùng copy-on-write: copy file từ lower lên upper rồi sửa.
- **Docker Architecture:**
  ```
  Docker CLI → Docker Daemon (dockerd) → containerd → runc
                                                        ↓
                                                   Container Process
  ```
  - `dockerd` — API server, quản lý image, volume, network.
  - `containerd` — Container runtime, quản lý vòng đời container.
  - `runc` — OCI runtime, tạo container (namespace + cgroup + pivot_root).
- **OCI (Open Container Initiative):** Tiêu chuẩn mở cho container format (image spec) và runtime (runtime spec). Đảm bảo image build bởi Docker chạy được trên Podman, Kubernetes, v.v.

### Bài tập 11.1 — Khám phá Container Internals

**Đề bài:** Khởi chạy một container và khám phá cách Docker cô lập nó ở mức kernel.

**Lời giải:**

```bash
# Chạy container
docker run -d --name internals --memory 256m --cpus 0.5 alpine sleep 3600

# Lấy PID thực của container process trên host
PID=$(docker inspect -f '{{.State.Pid}}' internals)
echo "Container PID on host: $PID"

# 1. Xem namespace
sudo ls -la /proc/$PID/ns/
# Mỗi file tượng trưng cho một namespace: ipc, mnt, net, pid, user, uts, cgroup

# 2. Xem cgroup memory limit
# cgroups v2:
cat /sys/fs/cgroup/system.slice/docker-$(docker inspect -f '{{.Id}}' internals).scope/memory.max
# Output: 268435456 (= 256MB tính bằng bytes)

# 3. Xem cgroup CPU limit
cat /sys/fs/cgroup/system.slice/docker-$(docker inspect -f '{{.Id}}' internals).scope/cpu.max
# Output: 50000 100000 (= 50% CPU, 50000/100000 microseconds)

# 4. Xem overlay filesystem
docker inspect internals --format '{{.GraphDriver.Data.MergedDir}}'
sudo ls $(docker inspect internals --format '{{.GraphDriver.Data.MergedDir}}')

# 5. So sánh PID bên trong và bên ngoài container
docker exec internals ps aux   # PID 1 = sleep
ps aux | grep $PID             # Trên host, PID khác hoàn toàn
```

---

## Giai đoạn 12: Hệ Sinh Thái & Công Cụ Thay Thế (Ngày 68–74)

### LÀM trước

```bash
# 1. Podman — Docker alternative, daemonless, rootless by default
podman pull nginx
podman run -d -p 8080:80 --name web nginx
podman ps
podman stop web
# CLI gần như tương thích 100% với Docker

# 2. Docker Contexts — Quản lý nhiều Docker host từ một CLI
docker context create remote-server \
  --docker "host=ssh://user@remote-server"
docker context ls
docker context use remote-server
docker ps  # Liệt kê container trên remote server!
docker context use default  # Quay lại local

# 3. Private Registry
docker run -d -p 5000:5000 --name registry \
  -v registry_data:/var/lib/registry \
  registry:2

# Push image lên private registry
docker tag myapp:v1 localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1

# Liệt kê images trong registry
curl http://localhost:5000/v2/_catalog
```

### HIỂU sau

- **Podman vs Docker:**
  - Podman **không có daemon** — mỗi container là child process trực tiếp.
  - Rootless by default — an toàn hơn Docker.
  - CLI tương thích Docker (`alias docker=podman`).
  - Hỗ trợ `pods` (nhóm container chia sẻ network namespace, giống Kubernetes pod).
  - Nhược điểm: Docker Compose hỗ trợ hạn chế hơn (dùng `podman-compose`).
- **Docker Desktop Alternatives:**
  - **Colima** — Nhẹ, chạy trên macOS/Linux. Dùng Lima VM.
  - **Rancher Desktop** — Bao gồm cả Kubernetes.
  - **OrbStack** — Tối ưu cho macOS, nhanh hơn Docker Desktop.
  - **nerdctl** — CLI tương thích Docker cho containerd.
  - Lý do dùng: Docker Desktop có **license fee** cho công ty lớn (>250 nhân viên hoặc >$10M doanh thu).
- **Docker Contexts:** Quản lý và chuyển đổi giữa nhiều Docker host (local, remote server, cloud) từ một CLI. Dùng SSH tunnel, không cần expose Docker port.
- **Private Registry:** Lưu trữ image nội bộ. Harbor là giải pháp enterprise với RBAC, vulnerability scanning, image replication, và image signing.
- **Cloud Registries:** AWS ECR, Google GAR, Azure ACR — tích hợp sẵn với cloud ecosystem, IAM-based access control.

---

## Giai đoạn 13: Debug & Xử Lý Sự Cố (Liên tục)

### Bộ công cụ debug

```bash
# 1. Xem log (luôn bắt đầu từ đây)
docker logs myapp                        # Toàn bộ log
docker logs --tail 50 -f myapp           # 50 dòng cuối, real-time
docker logs --since 30m myapp            # Log trong 30 phút gần nhất

# 2. Vào shell trong container đang chạy
docker exec -it myapp /bin/sh            # Alpine (không có bash)
docker exec -it myapp /bin/bash          # Debian/Ubuntu

# 3. Inspect chi tiết container
docker inspect myapp                     # Toàn bộ thông tin
docker inspect -f '{{.State.Status}}' myapp          # Trạng thái
docker inspect -f '{{.State.ExitCode}}' myapp        # Exit code
docker inspect -f '{{.NetworkSettings.IPAddress}}' myapp  # IP
docker inspect -f '{{json .Mounts}}' myapp | jq      # Volumes

# 4. Xem thay đổi filesystem
docker diff myapp
# A = Added, C = Changed, D = Deleted

# 5. Xem real-time resource usage
docker stats myapp

# 6. Copy file ra/vào container
docker cp myapp:/app/logs/error.log ./error.log
docker cp ./config.json myapp:/app/config.json

# 7. Xem events
docker events --filter container=myapp

# 8. Phân tích image layers
docker history myapp:latest
# Tool bên ngoài: dive (UI trực quan)
docker run --rm -it \
  -v /var/run/docker.sock:/var/run/docker.sock \
  wagoodman/dive myapp:latest

# 9. Debug network
docker network inspect bridge
docker exec myapp ping other-container
docker exec myapp nslookup db
docker exec myapp curl -v http://api:3000/health

# 10. Vào container từ host level (không cần docker exec)
PID=$(docker inspect -f '{{.State.Pid}}' myapp)
sudo nsenter -t $PID -m -u -i -n -p bash
```

### Các lỗi thường gặp và cách xử lý

| Triệu chứng | Nguyên nhân phổ biến | Cách debug |
|-------------|---------------------|------------|
| Container exit ngay lập tức | CMD/ENTRYPOINT sai, app crash khi start | `docker logs`, kiểm tra exit code |
| Container chạy nhưng không truy cập được | Port mapping sai, app listen sai interface | Kiểm tra `-p`, app phải listen `0.0.0.0` |
| Container không kết nối được container khác | Khác network, sai hostname | `docker network inspect`, dùng tên service |
| Image build chậm | Cache bị phá, thứ tự layer sai | Sắp xếp lại Dockerfile, dùng `.dockerignore` |
| Container bị OOM kill | Thiếu memory, memory leak | `docker stats`, tăng `--memory`, fix memory leak |
| Volume không mount đúng | Sai path, permission denied | `docker inspect`, kiểm tra ownership |
| Build fail "file not found" | File bị loại bởi `.dockerignore`, sai context path | Kiểm tra `.dockerignore`, kiểm tra build context |

### Bài tập 13.1 — Debug container bị lỗi

**Đề bài:** Bạn được đưa một ứng dụng đã đóng gói vào Docker image nhưng container khởi chạy rồi thoát ngay. Hãy tìm nguyên nhân và sửa.

```bash
# Tạo image bị lỗi (giả lập)
cat <<'DOCKERFILE' | docker build -t buggy-app -
FROM python:3.12-slim
WORKDIR /app
RUN echo 'from flask import Flask\napp = Flask(__name__)\n@app.route("/")\ndef hello(): return "Hello"\nif __name__ == "__main__": app.run(port=5000)' > app.py
CMD ["python", "app.py"]
DOCKERFILE
```

**Quy trình debug:**

```bash
# Bước 1: Chạy và quan sát
docker run -d --name buggy buggy-app
docker ps -a  # Thấy status "Exited"

# Bước 2: Xem log
docker logs buggy
# Output: ModuleNotFoundError: No module named 'flask'
# → Flask chưa được cài đặt

# Bước 3: Xác nhận nguyên nhân
docker run --rm -it buggy-app bash
pip list  # Không có flask

# Bước 4: Sửa — Thêm RUN pip install flask vào Dockerfile
cat <<'DOCKERFILE' | docker build -t fixed-app -
FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir flask
RUN echo 'from flask import Flask\napp = Flask(__name__)\n@app.route("/")\ndef hello(): return "Hello"\nif __name__ == "__main__": app.run(host="0.0.0.0", port=5000)' > app.py
EXPOSE 5000
CMD ["python", "app.py"]
DOCKERFILE

docker run -d -p 5000:5000 --name fixed fixed-app
curl http://localhost:5000  # Hello
```

---

## Phụ Lục A: Cheat Sheet Lệnh Docker

### Container Lifecycle

```bash
docker create <image>         # Tạo container (chưa chạy)
docker start <container>      # Chạy container đã tạo
docker run <image>            # = create + start
docker run -d                 # Chạy nền (detached)
docker run -it                # Chạy tương tác (interactive + tty)
docker run --rm               # Tự xóa khi dừng
docker run --name <name>      # Đặt tên
docker run -p 8080:80         # Map port
docker run -v data:/app       # Mount volume
docker run -e KEY=VAL         # Biến môi trường
docker run --network mynet    # Chọn network
docker stop <container>       # Dừng (SIGTERM → SIGKILL sau 10s)
docker kill <container>       # Dừng ngay (SIGKILL)
docker restart <container>    # Restart
docker pause/unpause          # Tạm dừng/tiếp tục
docker rm <container>         # Xóa container
docker rm -f <container>      # Buộc xóa (kể cả đang chạy)
```

### Image Management

```bash
docker build -t name:tag .        # Build image
docker build --no-cache .         # Build không dùng cache
docker images                     # Liệt kê images
docker rmi <image>                # Xóa image
docker tag <src> <dst>            # Tag image
docker push <image>               # Push lên registry
docker pull <image>               # Pull từ registry
docker save -o file.tar <image>   # Export image ra file
docker load -i file.tar           # Import image từ file
docker history <image>            # Xem layer history
docker image prune                # Xóa dangling images
```

### Docker Compose

```bash
docker compose up -d              # Khởi chạy tất cả services
docker compose down               # Dừng và xóa
docker compose down -v            # Dừng, xóa, bao gồm volumes
docker compose ps                 # Liệt kê services
docker compose logs -f            # Xem log real-time
docker compose build              # Build/rebuild services
docker compose pull               # Pull images mới nhất
docker compose exec <svc> bash    # Exec vào service
docker compose --profile dev up   # Chạy với profile
docker compose watch              # Watch mode (dev)
```

### System & Cleanup

```bash
docker system df                  # Xem disk usage
docker system prune               # Dọn dẹp (container, image, network)
docker system prune -a --volumes  # Dọn dẹp triệt để (cẩn thận!)
docker info                       # Thông tin Docker Engine
docker version                    # Phiên bản Docker
```

---

## Phụ Lục B: Checklist Trước Khi Đưa Lên Production

- [ ] Image dùng tag cụ thể (không dùng `latest`)
- [ ] Multi-stage build, image nhỏ gọn
- [ ] Non-root user trong container
- [ ] HEALTHCHECK được cấu hình
- [ ] `.dockerignore` loại bỏ file không cần thiết
- [ ] Không có secret trong image layer (dùng runtime env hoặc secret mount)
- [ ] Resource limits (memory, CPU, PID)
- [ ] Log rotation được cấu hình
- [ ] Image đã được quét lỗ hổng bảo mật
- [ ] Graceful shutdown (app xử lý SIGTERM đúng cách)
- [ ] Read-only filesystem (nếu có thể)
- [ ] Capabilities đã được drop (chỉ add những gì cần)
- [ ] `--security-opt no-new-privileges` được bật
- [ ] Restart policy phù hợp (`unless-stopped` hoặc `on-failure`)
- [ ] Monitoring và alerting đã thiết lập
- [ ] Backup strategy cho volumes chứa data quan trọng

---

## Phụ Lục C: Tài Nguyên Học Tập

| Tài nguyên | Mô tả |
|------------|--------|
| [Docker Official Docs](https://docs.docker.com/) | Tài liệu chính thức, luôn cập nhật |
| [Docker Labs (Play with Docker)](https://labs.play-with-docker.com/) | Thực hành Docker trên trình duyệt, miễn phí |
| [iximiuz Labs](https://labs.iximiuz.com/) | Bài lab container internals chất lượng cao |
| [roadmap.sh/docker](https://roadmap.sh/docker) | Roadmap tương tác, cộng đồng đánh giá cao |
| [Dive tool](https://github.com/wagoodman/dive) | Phân tích trực quan image layers |
| [Docker Slim](https://github.com/slimtoolkit/slim) | Tự động tối ưu kích thước image |
| [Trivy](https://github.com/aquasecurity/trivy) | Quét lỗ hổng bảo mật image |
| [Awesome Docker](https://github.com/veggiemonk/awesome-docker) | Tổng hợp tài nguyên Docker |
