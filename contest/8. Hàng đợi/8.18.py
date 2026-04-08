from collections import deque

def solve(matrix, R, C):
    queue = deque()
    fresh_seeds = 0
    
    # Bước 1: Đưa tất cả cây non vào hàng đợi và đếm số hạt mầm
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 2:
                queue.append((r, c, 0)) # (hàng, cột, ngày)
            elif matrix[r][c] == 1:
                fresh_seeds += 1
                
    if fresh_seeds == 0: return 0
    
    max_days = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Bước 2: BFS lan truyền
    while queue:
        r, c, days = queue.popleft()
        max_days = max(max_days, days)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == 1:
                matrix[nr][nc] = 2 # Đánh dấu đã nảy mầm
                fresh_seeds -= 1
                queue.append((nr, nc, days + 1))
                
    # Nếu còn hạt mầm chưa nảy mầm thì trả về -1
    return max_days if fresh_seeds == 0 else -1
                

def main():
    x, y = map(int, input().strip().split())
    matrix = []
    for i in range(x):
        matrix.append([int(c) for c in input().strip().split()])
    print(solve(matrix, x, y))
    
if __name__ == '__main__':
    main()