def solve(nums):
    stack = []
    max_area = 0
    for i in range(len(nums) + 1):
        current_height = nums[i] if i < len(nums) else 0
        while stack and nums[stack[-1]] > current_height:
            height = nums[stack.pop()]
            width = i if not stack else i - stack[-1] -1
            max_area = max(max_area, width * height)
        stack.append(i)
    return max_area

def main():
    t = int(input())
    result = []
    while t:
        t -= 1
        n = input()
        nums = [int(c) for c in input().strip().split()]
        result.append(str(solve(nums)))
    print('\n'.join(result))

if __name__ == '__main__':
    main()