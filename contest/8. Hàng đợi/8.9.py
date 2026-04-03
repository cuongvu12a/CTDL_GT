from collections import deque

def solve(S, T):
    # Trường hợp đặc biệt: Nếu S >= T, chỉ có một cách duy nhất là trừ 1 liên tục
    if S >= T:
        return str(S - T)
    
    # Giới hạn mảng visited. Vì T < 10000, ngưỡng 20000 là an toàn
    # để thực hiện phép nhân 2 rồi trừ dần về T nếu cần.
    limit = 20000
    visited = [False] * (limit + 1)
    
    # Queue lưu (giá trị hiện tại, số bước)
    queue = deque([(S, 0)])
    visited[S] = True
    
    while queue:
        curr_val, curr_step = queue.popleft()
        
        # Nếu đạt đến mục tiêu, trả về số bước
        if curr_val == T:
            return str(curr_step)
        
        # 1. Thao tác Nhân 2 (b):
        # Chỉ nhân nếu giá trị hiện tại nhỏ hơn T và chưa vượt quá giới hạn an toàn
        # (Nếu curr_val > T, nhân 2 chỉ làm tốn thêm bước)
        mult_val = curr_val * 2
        if curr_val < T and mult_val <= limit and not visited[mult_val]:
            visited[mult_val] = True
            queue.append((mult_val, curr_step + 1))
            
        # 2. Thao tác Trừ 1 (a):
        # Chỉ trừ nếu giá trị > 0 và chưa từng ghé thăm
        sub_val = curr_val - 1
        if sub_val > 0 and not visited[sub_val]:
            visited[sub_val] = True
            queue.append((sub_val, curr_step + 1))

def main():
    try:
        # Đọc số lượng bộ test
        line = input().strip()
        if not line:
            return
        t = int(line)
        
        results = []
        for _ in range(t):
            # Đọc S và T
            data = input().strip().split()
            if not data:
                continue
            s_val, t_val = map(int, data)
            results.append(solve(s_val, t_val))
            
        # In tất cả kết quả, mỗi kết quả trên 1 dòng
        print('\n'.join(results))
    except EOFError:
        pass

if __name__ == '__main__':
    main()