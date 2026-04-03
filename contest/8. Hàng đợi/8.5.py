from collections import deque

def solve(num):
    result = []
    queue = deque()
    queue.append('1')
    while len(result) < num:
        first = queue.popleft()
        next_one, next_two = first + '0', first + '1'
        result.append(first)
        queue.append(next_one)
        queue.append(next_two)
    
    return ' '.join(result)

def main():
    t = int(input())
    result = []
    while t:
        t -= 1
        num = int(input())
        result.append(solve(num))
    print('\n'.join(result))
        

if __name__ == '__main__':
    main()