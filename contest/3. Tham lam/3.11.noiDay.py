def main():
    n = int(input())
    nums = list(map(int, input().split()))
    res = 0
    while len(nums) > 1:
        nums.sort(reverse=True)
        first = nums.pop(-1)
        second = nums.pop(-1)
        res += first + second
        nums.append(first + second)
        
    print(res)
    
main()

''' 
Input:
---
7
2 4 1 2 10 2 3

---
Output:
59
'''