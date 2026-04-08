from collections import deque
import copy

def left_rotate(matrix):
    res = [row[:] for row in matrix]
    # Xoay cụm 2x2 bên trái (kim đồng hồ): 
    # (0,0)->(0,1), (0,1)->(1,1), (1,1)->(1,0), (1,0)->(0,0)
    res[0][0], res[0][1], res[1][1], res[1][0] = \
    matrix[1][0], matrix[0][0], matrix[0][1], matrix[1][1]
    return res

def right_rotate(matrix):
    res = [row[:] for row in matrix]
    # Xoay cụm 2x2 bên phải (kim đồng hồ):
    # (0,1)->(0,2), (0,2)->(1,2), (1,2)->(1,1), (1,1)->(0,1)
    res[0][1], res[0][2], res[1][2], res[1][1] = \
    matrix[1][1], matrix[0][1], matrix[0][2], matrix[1][2]
    return res

def matrix_to_tuple(matrix):
    # Chuyển ma trận 2x2 thành tuple để lưu vào set/queue
    return (tuple(matrix[0]), tuple(matrix[1]))

def solve(start_matrix, target_matrix):
    start_node = matrix_to_tuple(start_matrix)
    target_node = matrix_to_tuple(target_matrix)
    
    if start_node == target_node:
        return 0
    
    # Queue lưu (ma trận hiện tại, số bước)
    queue = deque([(start_matrix, 0)])
    visited = {start_node}
    
    while queue:
        curr_matrix, steps = queue.popleft()
        
        # Thử 2 phép quay
        for move_func in [left_rotate, right_rotate]:
            next_matrix = move_func(curr_matrix)
            next_node = matrix_to_tuple(next_matrix)
            
            if next_node == target_node:
                return steps + 1
            
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_matrix, steps + 1))
    return -1

def main():
    # Giả sử đầu vào là 6 số trên 1 dòng cho mỗi trạng thái
    try:
        a = [int(c) for c in input().strip().split()]
        b = [int(c) for c in input().strip().split()]
        
        # Chuyển list 6 số thành ma trận 2x3
        matrix = [a[:3], a[3:]]
        target = [b[:3], b[3:]]
        
        print(solve(matrix, target))
    except EOFError:
        pass

if __name__ == '__main__':
    main()