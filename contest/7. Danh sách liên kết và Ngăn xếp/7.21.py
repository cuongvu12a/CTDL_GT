def solve(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    store_min = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1][0] <= nums[i]:
            stack.pop()
        
        while store_min and store_min[-1] >= nums[i]:
            store_min.pop()
            
        if stack:
            result[i] = stack[-1][1]
        
        temp = store_min[-1] if store_min else -1
        stack.append((nums[i], temp))
        store_min.append(nums[i])
                
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
        
        