def main():
    n = int(input())
    while n > 0:
        n -= 1
        d = int(input())
        s = input()
        chars = {}
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        nums = []
        for c in chars:
            nums.append(chars[c])            

        nums.sort()
        max = nums.pop(-1)
        for i in range(max - 1): 
            temp = d - 1
            for idx in range(len(nums)):
                if temp == 0:
                    break
                if not nums[idx] == 0:
                    nums[idx] -= 1
                    temp -= 1
            
            if temp != 0:
                print(-1)
                break
        else:
            print(1)
            
                
        
main()

'''
Input:
---
2
3
abcabcabca
3
abcabcabba

---
Output:
1
-1
'''