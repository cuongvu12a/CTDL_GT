def solve(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
            
        if stack:
            result[i] = stack[-1]
            
        stack.append(nums[i])
        
    return ' '.join(map(str, result))

def main():
    t = int(input())
    result = []
    while t:
        t -= 1
        n = input()
        nums = [int(c) for c in input().strip().split(' ')]
        result.append(solve(nums))
    print('\n'.join(result))

if __name__ == '__main__':
    main()
        
        