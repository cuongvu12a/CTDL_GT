from collections import deque

def solve(matrix, from_x, from_y, to_x, to_y):
    queue= deque([(from_x, from_y, 0)])
    visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
    visited[from_x][from_y] = True
    while queue:
        curr_x, curr_y, step = queue.popleft()
        if curr_x == to_x and curr_y == to_y:
            return step
        for i in range(curr_x - 1, -1 , -1):
            if matrix[i][curr_y] == 'X': 
                break
            if not visited[i][curr_y]:
                visited[i][curr_y] = True
                queue.append((i, curr_y, step + 1))
        for i in range(curr_x + 1, len(matrix)):
            if matrix[i][curr_y] == 'X': 
                break
            if not visited[i][curr_y]:
                visited[i][curr_y] = True
                queue.append((i, curr_y, step + 1))

        for i in range(curr_y - 1, -1 , -1):
            if matrix[curr_x][i] == 'X': 
                break
            if not visited[curr_x][i]:
                visited[curr_x][i] = True
                queue.append((curr_x, i, step + 1))
        for i in range(curr_y + 1, len(matrix)):
            if matrix[curr_x][i] == 'X': 
                break
            if not visited[curr_x][i]:
                visited[curr_x][i] = True
                queue.append((curr_x, i, step + 1))
            
    return -1

def main():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append([c for c in input().strip()])
    from_x, from_y, to_x, to_y = map(int, input().strip().split())
    print(solve(matrix, from_x, from_y, to_x, to_y))

if __name__ == '__main__':
    main()