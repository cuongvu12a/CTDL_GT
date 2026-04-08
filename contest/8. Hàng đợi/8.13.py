from collections import deque

def solve(l, r):
    queue = deque([1,2,3,4,5])
    count = 0
    while queue:
        curr = queue.popleft()
        if l <= curr <= r:
            count += 1
        
        if curr * 10 > r:
            continue
        
        curr_str = str(curr)
        for next in range(6):
            next_str = str(next)
            if next_str not in curr_str:
                new_num = curr * 10 + next
                if int(new_num) <= r:
                    queue.append(new_num)
    return count

def main():
    t = int(input())
    result = []
    while t:
        t -= 1
        l,r = map(int, input().strip().split())
        result.append(str(solve(l, r)))
    print('\n'.join(result))

if __name__ == '__main__':
    main()