from collections import deque

def solve(num):
    queue = deque()
    queue.append(9)
    while True:
        first = queue.popleft()
        next_one, next_two = first * 10, first * 10 + 9
        if first % num == 0:
            return str(first)
        queue.append(next_one)
        queue.append(next_two)
    

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