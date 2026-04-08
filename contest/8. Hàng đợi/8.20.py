from collections import deque

def rotate_left(state, forward=True):
    s = list(state)
    if forward:
        # Xuôi: 0->1, 1->5, 5->8, 8->7, 7->3, 3->0
        s[1], s[5], s[8], s[7], s[3], s[0] = s[0], s[1], s[5], s[8], s[7], s[3]
    else:
        # Ngược: 1->0, 5->1, 8->5, 7->8, 3->7, 0->3
        s[0], s[1], s[5], s[8], s[7], s[3] = s[1], s[5], s[8], s[7], s[3], s[0]
    return tuple(s)

def rotate_right(state, forward=True):
    s = list(state)
    if forward:
        # Xuôi: 1->2, 2->6, 6->9, 9->8, 8->4, 4->1
        s[2], s[6], s[9], s[8], s[4], s[1] = s[1], s[2], s[6], s[9], s[8], s[4]
    else:
        # Ngược: 2->1, 6->2, 9->6, 8->9, 4->8, 1->4
        s[1], s[2], s[6], s[9], s[8], s[4] = s[2], s[6], s[9], s[8], s[4], s[1]
    return tuple(s)

def solve(matrix, target):
    queue = deque([matrix])
    visisted = {matrix: 0}
    
    while queue:
        curr = queue.popleft()
        if target in visisted:
            return visisted[target]
        for move in [rotate_left(curr, True), rotate_right(curr, True)]:
            if move not in visisted:
                visisted[move] = visisted[curr] + 1
                queue.append(move)
    return -1

def solve_2(matrix, target):
    queue_forward = deque([matrix])
    visisted_forward = {matrix: 0}
    
    while queue_forward:
        curr = queue_forward.popleft()
        if visisted_forward[curr] >= 15:
            break
        if target in visisted_forward:
            return visisted_forward[target]
        for move in [rotate_left(curr, True), rotate_right(curr, True)]:
            if move not in visisted_forward:
                visisted_forward[move] = visisted_forward[curr] + 1
                queue_forward.append(move)
                
    visited_backward = {target: 0}
    queue_backward = deque([target])
    while queue_backward:
        curr = queue_backward.popleft()
        if curr in visisted_forward:
            return visisted_forward[curr] + visited_backward[curr]
        for move in [rotate_left(curr, False), rotate_right(curr, False)]:
            if move not in visited_backward:
                visited_backward[move] = visited_backward[curr] + 1
                queue_backward.append(move)
    
    return -1

def main():
    arr_input = [int(x) for _ in range(3) for x in input().split()]
    maxtrix = tuple(arr_input)
    target = (1,2,3,8,0,0,4,7,6,5)
    print(solve(maxtrix, target))

if __name__ == '__main__':
    main()