from collections import deque

def solve(matrix, m, n):
    # Bắt đầu từ 0,0 với 0 bước
    queue = deque([(0, 0, 0)])
    # Mảng đánh dấu đã thăm để tránh lặp vô hạn và tối ưu tốc độ
    visited = [[False for _ in range(n)] for _ in range(m)]
    visited[0][0] = True
    
    while queue:
        r, c, steps = queue.popleft()
        
        # Kiểm tra nếu đã đến đích A[M-1][N-1]
        if r == m - 1 and c == n - 1:
            return steps
            
        curr_value = matrix[r][c]
        if curr_value == 0: continue # Không thể di chuyển nếu giá trị là 0
        
        # Di chuyển xuống dưới (theo hàng)
        next_r = r + curr_value
        if next_r < m and not visited[next_r][c]:
            visited[next_r][c] = True
            queue.append((next_r, c, steps + 1))
            
        # Di chuyển sang phải (theo cột)
        next_c = c + curr_value
        if next_c < n and not visited[r][next_c]:
            visited[r][next_c] = True
            queue.append((r, next_c, steps + 1))
            
    return -1

def main():
    import sys
    # Sử dụng sys.stdin.read để đọc nhanh hơn nếu dữ liệu lớn
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        m = int(input_data[idx])
        n = int(input_data[idx+1])
        idx += 2
        
        matrix = []
        for i in range(m):
            row = [int(x) for x in input_data[idx : idx + n]]
            matrix.append(row)
            idx += n
            
        results.append(str(solve(matrix, m, n)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()