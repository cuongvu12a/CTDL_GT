def solve(size, nums):
    stack = []
    result = [1] * size
    for i in range(size - 1, -2, -1):
        if i == -1 or (stack and nums[stack[-1]] < nums[i]):
            while stack and nums[stack[-1]] < nums[i]:
                last_idx = stack.pop()
                result[last_idx] = last_idx - i
            stack.append(i)                
        else:
            stack.append(i)
    return result    

def main():
    size = int(input())
    nums = [int(c) for c in input().strip().split(" ")]
    print(' '.join(str(i) for i in solve(size, nums)))

if __name__ == '__main__':
    main()