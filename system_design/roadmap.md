# Lộ Trình Học System Design — Từ Người Mới Bắt Đầu Đến Thực Chiến

> Được biên soạn bởi kinh nghiệm 12+ năm thiết kế hệ thống quy mô lớn.  
> Mục tiêu: Giúp bạn xây dựng tư duy kiến trúc hệ thống một cách bài bản, từng bước.

---

## Mục Lục

1. [Tổng Quan & Kiến Thức Nền Tảng](#1-tổng-quan--kiến-thức-nền-tảng)
2. [Lộ Trình Học Tập](#2-lộ-trình-học-tập)
3. [Chi Tiết Từng Chủ Đề](#3-chi-tiết-từng-chủ-đề)
4. [Tài Nguyên Học Tập](#4-tài-nguyên-học-tập)

---

## 1. Tổng Quan & Kiến Thức Nền Tảng

Trước khi bước vào System Design, bạn cần nắm vững các nền tảng sau. Đây **không phải kiến thức tùy chọn** — thiếu bất kỳ mảng nào sẽ khiến bạn thiết kế "bề nổi" mà không hiểu bản chất.

### 1.1 Mạng Máy Tính (Networking)

| Khái niệm | Mức độ cần thiết |
|---|---|
| Mô hình OSI / TCP-IP | Bắt buộc |
| HTTP/1.1, HTTP/2, HTTP/3, HTTPS | Bắt buộc |
| DNS — cách hoạt động, TTL, record types | Bắt buộc |
| TCP vs UDP — khi nào dùng cái nào | Bắt buộc |
| WebSocket, Long Polling, SSE | Quan trọng |
| CDN — cơ chế hoạt động | Quan trọng |
| gRPC, REST, GraphQL | Quan trọng |

### 1.2 Cơ Sở Dữ Liệu (Databases)

| Khái niệm | Mức độ cần thiết |
|---|---|
| SQL cơ bản — JOIN, INDEX, TRANSACTION | Bắt buộc |
| ACID properties | Bắt buộc |
| NoSQL — các loại (Document, KV, Column, Graph) | Bắt buộc |
| Index — B-Tree, LSM-Tree | Quan trọng |
| Replication & Sharding | Quan trọng |
| CAP Theorem | Quan trọng |

### 1.3 Hệ Điều Hành & Hạ Tầng (OS & Infrastructure)

| Khái niệm | Mức độ cần thiết |
|---|---|
| Process vs Thread, concurrency | Bắt buộc |
| Memory — RAM, disk, cache hierarchy | Bắt buộc |
| I/O — blocking vs non-blocking | Quan trọng |
| Linux cơ bản (file system, process management) | Quan trọng |
| Docker & container cơ bản | Quan trọng |

### 1.4 Lập Trình & Thuật Toán

Bạn không cần giỏi LeetCode Hard, nhưng cần hiểu:
- Độ phức tạp O(n), tại sao một số thao tác tốn kém hơn
- Hash map, queue, heap — cách chúng được dùng trong hệ thống thực tế
- Consistent Hashing — thuật toán nền tảng của distributed systems

---

## 2. Lộ Trình Học Tập

```
GIAI ĐOẠN 1          GIAI ĐOẠN 2           GIAI ĐOẠN 3           GIAI ĐOẠN 4
(4–6 tuần)           (6–8 tuần)            (8–10 tuần)           (Liên tục)
─────────────        ──────────────        ───────────────       ────────────
Nền tảng kỹ thuật → Các building block  → Thiết kế hệ thống   → Thực chiến &
                     phân tán              cụ thể                  Nâng cao
```

### Giai Đoạn 1 — Nền Tảng Kỹ Thuật (4–6 tuần)

Mục tiêu: Hiểu rõ HTTP, database, và các thành phần cơ bản.

- [ ] HTTP request/response lifecycle
- [ ] SQL fundamentals + indexing
- [ ] DNS + CDN hoạt động thế nào
- [ ] Latency numbers every programmer should know
- [ ] Đọc: *"Designing Data-Intensive Applications"* — Chương 1 & 2

### Giai Đoạn 2 — Các Building Block Phân Tán (6–8 tuần)

Mục tiêu: Hiểu các thành phần tạo nên mọi hệ thống lớn.

- [ ] Load Balancer (Layer 4 vs Layer 7)
- [ ] Caching — Redis, Memcached, các chiến lược cache
- [ ] Message Queue — Kafka, RabbitMQ
- [ ] Database Replication & Sharding
- [ ] Consistent Hashing
- [ ] Rate Limiting
- [ ] API Gateway

### Giai Đoạn 3 — Thiết Kế Hệ Thống Cụ Thể (8–10 tuần)

Mục tiêu: Áp dụng kiến thức vào các bài toán thực tế.

- [ ] Thiết kế URL Shortener (TinyURL)
- [ ] Thiết kế Twitter/News Feed
- [ ] Thiết kế YouTube / Netflix
- [ ] Thiết kế hệ thống Chat (WhatsApp)
- [ ] Thiết kế Search Engine (Elasticsearch)
- [ ] Thiết kế Payment System
- [ ] Thiết kế Notification System

### Giai Đoạn 4 — Nâng Cao & Thực Chiến (Liên tục)

- [ ] Distributed consensus — Raft, Paxos
- [ ] Event sourcing & CQRS
- [ ] Service Mesh, Observability (metrics, tracing, logging)
- [ ] Chaos Engineering
- [ ] Đọc engineering blogs từ Netflix, Uber, Airbnb, Meta

---

## 3. Chi Tiết Từng Chủ Đề

---

### 3.1 HTTP & Giao Thức Mạng

#### Khái niệm cốt lõi

Mọi hệ thống web đều giao tiếp qua HTTP. Hiểu HTTP không chỉ là biết GET/POST — bạn cần biết *tại sao* HTTP/2 nhanh hơn HTTP/1.1, và khi nào nên dùng WebSocket.

**HTTP/1.1**: Mỗi request mở một kết nối TCP, chờ response rồi mới gửi tiếp. Chậm vì "head-of-line blocking".

**HTTP/2**: Multiplexing — gửi nhiều request song song trên cùng một kết nối TCP. Nhanh hơn đáng kể.

**HTTP/3**: Thay TCP bằng QUIC (chạy trên UDP). Giải quyết head-of-line blocking ở tầng transport.

**WebSocket**: Kết nối hai chiều (bidirectional) và liên tục. Dùng cho chat, real-time dashboard, game.

**Long Polling**: Client hỏi server, server giữ kết nối đến khi có data mới rồi mới trả về. Cách đơn giản hơn WebSocket nhưng kém hiệu quả.

**Server-Sent Events (SSE)**: Server đẩy data liên tục về client, client không gửi ngược lại. Dùng cho notification, live feed.

#### Bài Tập Thực Hành

1. Mở browser DevTools → Network tab, vào một trang web và quan sát: request waterfall, status code, headers (`Content-Type`, `Cache-Control`, `Authorization`).
2. Dùng `curl -v https://google.com` và giải thích từng dòng output.
3. Viết một HTTP server đơn giản (Python Flask hoặc Node.js Express) và thử gọi bằng Postman.
4. So sánh: khi nào dùng REST, khi nào dùng WebSocket, khi nào dùng gRPC?

#### Tiêu Chí Sẵn Sàng Chuyển Tiếp

- [ ] Giải thích được HTTP request/response lifecycle đầy đủ (từ DNS lookup đến nhận response)
- [ ] Nêu được 3 sự khác biệt cốt lõi giữa HTTP/1.1 và HTTP/2
- [ ] Biết khi nào dùng REST vs WebSocket vs gRPC

---

### 3.2 DNS & CDN

#### Khái niệm cốt lõi

**DNS (Domain Name System)** là "danh bạ điện thoại" của internet. Khi bạn gõ `google.com`, DNS resolver tra cứu và trả về địa chỉ IP tương ứng.

Thứ tự tra cứu DNS:
```
Browser cache → OS cache → Router cache → ISP DNS → Root DNS → TLD DNS → Authoritative DNS
```

**TTL (Time-To-Live)**: Bản ghi DNS được cache trong bao lâu. TTL thấp → cập nhật nhanh nhưng tốn băng thông. TTL cao → ổn định nhưng chậm cập nhật.

**CDN (Content Delivery Network)**: Mạng lưới các server phân tán toàn cầu. Khi user tải file (ảnh, video, JS), CDN phục vụ từ server gần nhất thay vì server gốc (origin).

Lợi ích CDN:
- Giảm latency (server gần user hơn)
- Giảm tải cho origin server
- Tăng khả năng chịu lỗi

**Push CDN vs Pull CDN**:
- Push: Bạn chủ động đẩy file lên CDN trước khi có request
- Pull: CDN lấy file từ origin khi có request đầu tiên, sau đó cache lại

#### Bài Tập Thực Hành

1. Dùng `nslookup google.com` và `dig google.com` để xem DNS record.
2. Thử `dig +trace google.com` để thấy toàn bộ quá trình phân giải DNS.
3. Vẽ sơ đồ: Khi user ở Hà Nội truy cập Netflix, request đi qua những đâu?
4. Câu hỏi tư duy: Nếu bạn đổi IP server, tại sao phải đợi vài tiếng mới có hiệu lực toàn cầu?

#### Tiêu Chí Sẵn Sàng Chuyển Tiếp

- [ ] Giải thích đầy đủ quá trình DNS resolution
- [ ] Biết CDN giúp gì và không giúp gì (CDN không cache API động)
- [ ] Phân biệt Push CDN và Pull CDN, biết khi nào dùng cái nào

---

### 3.3 Load Balancer

#### Khái niệm cốt lõi

Load Balancer phân phối traffic đến nhiều server để tránh một server bị quá tải.

**Layer 4 Load Balancer** (Transport Layer): Hoạt động dựa trên IP và TCP/UDP port. Nhanh, nhưng không đọc được nội dung request.

**Layer 7 Load Balancer** (Application Layer): Đọc được HTTP header, URL path, cookie. Có thể route dựa trên nội dung (vd: `/api/*` đến server A, `/static/*` đến CDN).

**Các thuật toán cân bằng tải:**

| Thuật toán | Cách hoạt động | Khi nào dùng |
|---|---|---|
| Round Robin | Lần lượt theo vòng | Server có cùng năng lực |
| Weighted Round Robin | Giống Round Robin nhưng ưu tiên server mạnh hơn | Server khác năng lực |
| Least Connections | Gửi đến server có ít kết nối nhất | Request có thời gian xử lý khác nhau |
| IP Hash | Hash IP user → cùng user → cùng server | Cần sticky session |
| Random | Chọn ngẫu nhiên | Đơn giản, server đồng nhất |

**Health Check**: Load balancer định kỳ ping các server backend. Nếu server không phản hồi → loại khỏi pool.

**Sticky Session (Session Affinity)**: Đảm bảo cùng user luôn được route đến cùng server. Cần thiết nếu session được lưu in-memory trên server (nhưng đây là anti-pattern — nên lưu session ở Redis thay vì).

#### Bài Tập Thực Hành

1. Cài Nginx và cấu hình upstream với 3 server giả lập, thử các thuật toán khác nhau.
2. Câu hỏi thiết kế: Bạn có 3 server, server A mạnh gấp đôi B và C. Dùng thuật toán nào?
3. Câu hỏi tư duy: Nếu bản thân Load Balancer bị chết thì sao? → Tìm hiểu về Active-Passive và Active-Active LB.

#### Tiêu Chí Sẵn Sàng Chuyển Tiếp

- [ ] Giải thích Layer 4 vs Layer 7 LB với ví dụ cụ thể
- [ ] Nêu được ít nhất 3 thuật toán LB và khi nào dùng
- [ ] Biết cách tránh single point of failure cho LB

---

### 3.4 Caching

#### Khái niệm cốt lõi

Cache là lưu trữ tạm thời dữ liệu đã tính toán hoặc lấy từ DB, để lần sau trả về nhanh hơn mà không cần tính lại.

**Cache hit**: Data có trong cache → trả về ngay.  
**Cache miss**: Data không có trong cache → lấy từ nguồn gốc → lưu vào cache → trả về.

**Vị trí đặt cache:**
```
Client → [Browser Cache] → CDN → [CDN Cache] → Server → [Server Cache / Redis] → Database
```

**Các chiến lược đọc (Read strategies):**

- **Cache-Aside (Lazy Loading)**: Application tự quản lý cache. Miss → query DB → write vào cache. Đây là pattern phổ biến nhất.
- **Read-Through**: Cache tự động query DB khi miss. Application chỉ nói chuyện với cache.

**Các chiến lược ghi (Write strategies):**

- **Write-Through**: Ghi đồng thời vào cache và DB. Data luôn nhất quán nhưng chậm hơn.
- **Write-Back (Write-Behind)**: Ghi vào cache trước, DB sau (async). Nhanh nhưng có risk mất data.
- **Write-Around**: Bỏ qua cache, ghi thẳng vào DB. Dùng khi data ít khi được đọc lại.

**Cache Eviction Policies** (Khi cache đầy, xóa gì trước?):

| Policy | Xóa gì | Dùng khi |
|---|---|---|
| LRU (Least Recently Used) | Ít được dùng gần đây nhất | Phổ biến nhất |
| LFU (Least Frequently Used) | Ít được dùng nhất tổng thể | Data có tần suất ổn định |
| TTL-based | Hết thời gian sống | Data có thể stale sau X giây |
| FIFO | Vào trước xóa trước | Đơn giản, ít dùng |

**Cache Stampede / Thundering Herd**: Khi một cache entry hết hạn, hàng nghìn request cùng lúc query DB. Giải pháp: mutex lock, probabilistic early expiration, hoặc background refresh.

#### Bài Tập Thực Hành

1. Cài Redis, thử các lệnh: `SET`, `GET`, `EXPIRE`, `TTL`, `INCR`, `LPUSH`, `ZADD`.
2. Implement Cache-Aside trong code: đọc từ Redis, nếu miss thì query "DB" (mock), lưu vào Redis.
3. Câu hỏi: Nếu cache Twitter feed, bạn invalidate cache thế nào khi có tweet mới?
4. Câu hỏi: Bạn cache user profile với TTL 1 giờ. User đổi avatar, làm sao cập nhật ngay?

#### Tiêu Chí Sẵn Sàng Chuyển Tiếp

- [ ] Giải thích Cache-Aside, Read-Through, Write-Through, Write-Back
- [ ] Biết LRU hoạt động thế nào và implement được bằng HashMap + LinkedList
- [ ] Nêu được 3 vấn đề phổ biến với cache (stampede, stale data, cold start)

---

### 3.5 Database — SQL, NoSQL & Sharding

#### Khái niệm cốt lõi

**SQL (Relational Database)**: Dữ liệu có cấu trúc, quan hệ giữa các bảng, hỗ trợ ACID transaction. Ví dụ: PostgreSQL, MySQL.

**NoSQL**: Nhiều loại, mỗi loại giải quyết vấn đề khác nhau:

| Loại | Ví dụ | Dùng cho |
|---|---|---|
| Document | MongoDB, CouchDB | User profile, product catalog |
| Key-Value | Redis, DynamoDB | Cache, session, shopping cart |
| Column-family | Cassandra, HBase | Time-series, IoT, analytics |
| Graph | Neo4j | Social network, recommendation |
| Search | Elasticsearch | Full-text search |

**ACID vs BASE:**
- ACID (SQL): Atomicity, Consistency, Isolation, Durability — ưu tiên correctness
- BASE (NoSQL): Basically Available, Soft state, Eventual consistency — ưu tiên availability

**Index:**
- **B-Tree Index**: Tốt cho range query (`WHERE age > 25`). Được dùng trong PostgreSQL, MySQL.
- **LSM-Tree Index**: Tốt cho write-heavy workload. Được dùng trong Cassandra, RocksDB.
- **Composite Index**: Index trên nhiều column. Thứ tự column quan trọng.

**Database Replication:**
- **Primary-Replica (Master-Slave)**: Tất cả write vào Primary, Replica đồng bộ và phục vụ read. Tăng read throughput.
- **Multi-Primary**: Nhiều node có thể nhận write. Phức tạp hơn, cần giải quyết conflict.

**Database Sharding** (Horizontal Partitioning): Chia data ra nhiều database server.

```
Ví dụ: User với ID 1–1000000 → Shard A
        User với ID 1000001–2000000 → Shard B
```

Các chiến lược sharding:
- **Range-based**: Chia theo range của key. Đơn giản nhưng có thể không đều (hotspot).
- **Hash-based**: Hash(key) % số_shard. Phân bổ đều hơn.
- **Directory-based**: Có một bảng mapping key → shard. Linh hoạt nhất.

**Consistent Hashing**: Giải quyết vấn đề khi thêm/bớt shard — chỉ cần di chuyển một phần nhỏ data thay vì rehash toàn bộ.

#### Bài Tập Thực Hành

1. Tạo một bảng `users` trong PostgreSQL, tạo index trên `email`, dùng `EXPLAIN ANALYZE` để thấy index được dùng không.
2. So sánh: Thiết kế lưu trữ Twitter tweet — dùng SQL hay NoSQL? Tại sao?
3. Câu hỏi: Bạn có 100 triệu user. Cần shard. Dùng chiến lược nào? Điều gì xảy ra nếu một shard bị "hot"?
4. Implement Consistent Hashing đơn giản bằng code.

#### Tiêu Chí Sẵn Sàng Chuyển Tiếp

- [ ] Phân biệt SQL và NoSQL — biết khi nào dùng cái nào
- [ ] Giải thích ACID và tại sao nó quan trọng trong payment system
- [ ] Mô tả Sharding và Consistent Hashing, nêu trade-off

---

### 3.6 Message Queue & Event-Driven Architecture

#### Khái niệm cốt lõi

Message Queue (MQ) tách biệt producer (người gửi) và consumer (người xử lý), cho phép xử lý bất đồng bộ.

**Tại sao cần Message Queue?**
- **Decoupling**: Service A không cần biết Service B tồn tại
- **Buffer**: Hấp thụ spike traffic, tránh DB bị quá tải
- **Retry**: Nếu consumer lỗi, message được xử lý lại
- **Fan-out**: Một event → nhiều consumer xử lý độc lập

**Kafka vs RabbitMQ:**

| | Kafka | RabbitMQ |
|---|---|---|
| Mô hình | Log-based, pull | Message broker, push |
| Throughput | Rất cao (millions/sec) | Cao nhưng thấp hơn Kafka |
| Retention | Lưu lâu dài (configurable) | Xóa sau khi consumer ack |
| Use case | Event streaming, analytics, audit log | Task queue, RPC |
| Ordering | Trong một partition | Trong một queue |

**Các khái niệm Kafka:**
- **Topic**: Danh mục message (vd: `user-signup`, `order-created`)
- **Partition**: Topic được chia thành nhiều partition để song song hóa
- **Consumer Group**: Nhiều consumer cùng group đọc song song từ các partition khác nhau
- **Offset**: Vị trí đọc của consumer trong partition

**At-most-once, At-least-once, Exactly-once:**
- At-most-once: Không bao giờ gửi lại → có thể mất message
- At-least-once: Gửi lại nếu không ack → có thể trùng lặp (cần idempotent consumer)
- Exactly-once: Đảm bảo đúng một lần → phức tạp, tốn kém

#### Bài Tập Thực Hành

1. Cài Kafka với Docker, tạo topic, viết producer gửi 1000 messages, viết consumer đọc và in ra.
2. Câu hỏi thiết kế: Hệ thống gửi email khi user đăng ký. Nên dùng sync hay async? Tại sao?
3. Câu hỏi: Nếu consumer xử lý trùng lặp message, làm sao thiết kế để idempotent?
4. Vẽ sơ đồ: Khi user đặt hàng trên Shopee, những event nào được publish lên Kafka?

#### Tiêu Chí Sẵn Sàng Chuyển Tiếp

- [ ] Giải thích tại sao cần MQ thay vì gọi API trực tiếp
- [ ] Phân biệt Kafka và RabbitMQ, biết khi nào dùng cái nào
- [ ] Hiểu idempotency và tại sao nó quan trọng với at-least-once delivery

---

### 3.7 Rate Limiting

#### Khái niệm cốt lõi

Rate Limiting giới hạn số lượng request mà user/IP/service có thể gửi trong một khoảng thời gian.

**Mục đích:**
- Bảo vệ hệ thống khỏi bị quá tải (DoS/DDoS)
- Đảm bảo fair usage giữa các user
- Kiểm soát chi phí (với paid APIs)

**Các thuật toán Rate Limiting:**

**1. Fixed Window Counter:**
```
Mỗi phút là một window. Đếm request trong window hiện tại.
Vấn đề: Burst ở boundary (cuối phút này + đầu phút sau = 2x limit)
```

**2. Sliding Window Log:**
```
Lưu timestamp của mỗi request. Đếm trong cửa sổ trượt.
Chính xác nhưng tốn bộ nhớ.
```

**3. Sliding Window Counter:**
```
Kết hợp fixed window + tính tỉ lệ. Hiệu quả và gần đúng.
```

**4. Token Bucket:**
```
Bucket chứa token. Mỗi request lấy 1 token. Token được nạp theo tốc độ cố định.
Cho phép burst ngắn hạn. Dùng bởi AWS, Stripe.
```

**5. Leaky Bucket:**
```
Queue request và xử lý với tốc độ cố định.
Không cho phép burst. Output ổn định.
```

**Rate Limiting trong Distributed System:**
- Dùng Redis để lưu counter dùng chung giữa các server
- Lua script trong Redis để atomic increment + check

#### Bài Tập Thực Hành

1. Implement Token Bucket bằng code (Python/Go) với Redis.
2. Câu hỏi: Twitter giới hạn 300 tweet/3 giờ. Dùng thuật toán nào? Lưu state ở đâu?
3. Câu hỏi thiết kế: Thiết kế Rate Limiter cho API Gateway phục vụ 10 triệu user.

#### Tiêu Chí Sẵn Sàng Chuyển Tiếp

- [ ] Giải thích được 4 thuật toán rate limiting và trade-off
- [ ] Biết cách implement distributed rate limiting với Redis
- [ ] Nêu được các điểm đặt rate limiter trong hệ thống (API Gateway, service level)

---

### 3.8 Thiết Kế Hệ Thống — Bài Toán Thực Tế

#### Framework Tiếp Cận Bài Toán System Design

Khi được hỏi "Thiết kế Twitter", đừng nhảy vào solution ngay. Dùng framework này:

```
1. Clarify Requirements (5 phút)
   ├── Functional: Những tính năng nào cần thiết kế?
   └── Non-functional: Scale bao nhiêu? Latency? Availability?

2. Estimate Scale (3 phút)
   ├── Daily Active Users (DAU)?
   ├── Requests per second (RPS)?
   └── Storage cần bao nhiêu?

3. High-Level Design (10 phút)
   └── Vẽ sơ đồ các thành phần chính

4. Deep Dive (20 phút)
   └── Đào sâu vào component phức tạp nhất

5. Identify Bottlenecks & Trade-offs (5 phút)
   └── Single point of failure? Scale bottleneck? Trade-off nào?
```

#### Bài Toán Mẫu: Thiết Kế URL Shortener (như TinyURL)

**Bước 1 — Clarify Requirements:**
- Functional: Rút gọn URL, redirect từ short URL → original URL
- Non-functional: 100M URL/ngày, latency < 10ms khi redirect, high availability

**Bước 2 — Estimate:**
```
Writes: 100M URL/ngày = ~1,200 URL/giây
Reads:  Giả sử read:write = 10:1 → 12,000 redirect/giây
Storage: 100M * 365 * 5 năm * 500 bytes = ~91 TB
```

**Bước 3 — High-Level Design:**
```
User → Load Balancer → API Server → [Cache (Redis)] → Database
                                                    ↘ (cache miss) → DB
```

**Bước 4 — Deep Dive: Tạo Short URL**

Cách 1 — Hash (MD5/SHA256): Hash URL gốc, lấy 7 ký tự đầu.
- Vấn đề: Collision (2 URL khác nhau có thể cho cùng hash)

Cách 2 — Base62 Encode từ ID: DB auto-increment ID, encode sang Base62.
- 7 ký tự Base62 = 62^7 ≈ 3.5 nghìn tỷ URL — đủ dùng nhiều thập kỷ
- Không có collision

**Bước 5 — Bottlenecks:**
- DB là bottleneck → Cache redirect mapping vào Redis (hot URLs)
- Single DB → Replication để scale read
- Nếu cần global → Mỗi region tạo ID độc lập với prefix khác nhau

---

#### Bài Toán Mẫu: Thiết Kế News Feed (Twitter/Facebook)

**Core problem**: Khi user mở app, làm sao hiển thị bài viết từ những người họ follow, theo thứ tự thời gian?

**Approach 1 — Pull (Fan-out on Read):**
```
User open app → Query tất cả người họ follow → Lấy tweet của mỗi người → Merge → Sort → Return
```
Vấn đề: Nếu user follow 1000 người → 1000 DB query mỗi lần mở app → chậm.

**Approach 2 — Push (Fan-out on Write):**
```
Khi user A đăng tweet → Push ngay vào feed cache của tất cả follower
User B mở app → Chỉ cần đọc feed cache của B → Nhanh
```
Vấn đề: User nổi tiếng (celebrity) có 10M follower → đăng 1 tweet → phải write vào 10M cache entry → chậm.

**Hybrid Approach (Twitter thực tế dùng):**
- User bình thường → Fan-out on Write
- Celebrity (nhiều follower) → Fan-out on Read khi user mở app
- Merge kết quả của 2 phương pháp

---

## 4. Tài Nguyên Học Tập

### Sách (Quan trọng nhất)

| Sách | Đánh giá | Nên đọc khi |
|---|---|---|
| **Designing Data-Intensive Applications** — Martin Kleppmann | ⭐⭐⭐⭐⭐ Kinh điển. Giải thích sâu nhất về distributed systems | Giai đoạn 2–3 |
| **System Design Interview** — Alex Xu (Vol 1 & 2) | ⭐⭐⭐⭐ Tốt cho interview prep, nhiều case study | Giai đoạn 3 |
| **The Art of Scalability** | ⭐⭐⭐⭐ Thực tế, nhiều kinh nghiệm từ Yahoo | Giai đoạn 4 |

### Nền Tảng Trực Tuyến

| Nền tảng | Đánh giá | Ghi chú |
|---|---|---|
| **ByteByteGo** (bytebytego.com) | ⭐⭐⭐⭐⭐ | Visualizations xuất sắc, giải thích trực quan. Newsletter miễn phí rất tốt. |
| **System Design Primer** (GitHub) | ⭐⭐⭐⭐⭐ | Miễn phí, toàn diện, có Anki flashcard. Bắt đầu từ đây. |
| **Grokking System Design** (Educative) | ⭐⭐⭐⭐ | Có phí, structured learning path tốt. |
| **High Scalability Blog** | ⭐⭐⭐⭐ | Case study từ các công ty thực tế (Netflix, Uber...). |

### YouTube Channels

| Channel | Đánh giá | Nội dung |
|---|---|---|
| **ByteByteGo** | ⭐⭐⭐⭐⭐ | Animation đẹp, giải thích cô đọng, rất phù hợp cho beginner |
| **Gaurav Sen** | ⭐⭐⭐⭐⭐ | Giải thích sâu, tư duy tốt |
| **Tech Dummies** | ⭐⭐⭐⭐ | System design interview practice |
| **Hussein Nasser** | ⭐⭐⭐⭐ | Backend & networking chuyên sâu |

### Engineering Blogs (Đọc để hiểu thực tế)

| Blog | Tại sao nên đọc |
|---|---|
| **engineering.atspotify.com** | Kafka, microservices tại Spotify |
| **netflixtechblog.com** | Video streaming, chaos engineering, ML |
| **eng.uber.com** | Geospatial, real-time dispatch |
| **airbnb.io** | Data platform, ML, payments |
| **developers.facebook.com/blog** | Social graph, caching tại scale |

### Lộ Trình Học Theo Tuần (Gợi Ý Cụ Thể)

```
Tuần 1–2:  Đọc System Design Primer phần Overview
           Xem hết ByteByteGo Basic playlist
Tuần 3–4:  DDIA Chương 1–4 (Storage, Replication)
           Thực hành Redis + PostgreSQL
Tuần 5–6:  DDIA Chương 5–7 (Distributed systems)
           Thực hành Kafka
Tuần 7–8:  Alex Xu Vol 1 — Đọc và tự thiết kế trước khi xem đáp án
Tuần 9–10: Tự thiết kế 5 hệ thống không xem gợi ý
           Nhờ người review hoặc so sánh với tài liệu
Tuần 11+:  Đọc engineering blog hàng tuần
           Contribute vào open source để hiểu code thực tế
```

---

## Lời Kết

System Design không phải môn học có đáp án đúng/sai tuyệt đối. Mỗi quyết định là một **trade-off** — đánh đổi giữa consistency và availability, giữa latency và throughput, giữa đơn giản và linh hoạt.

**Tư duy quan trọng nhất cần xây dựng:**

> "Tại sao?" trước "Như thế nào?"

Trước khi thêm một cache, hỏi: *Tại sao cần cache? Vấn đề cụ thể là gì?*  
Trước khi sharding, hỏi: *Đã thử vertical scaling chưa? Bottleneck thực sự là gì?*

Hệ thống tốt nhất không phải hệ thống phức tạp nhất — mà là hệ thống **đơn giản nhất giải quyết được bài toán thực tế**.

---

*Cập nhật lần cuối: 2026-04-01*
