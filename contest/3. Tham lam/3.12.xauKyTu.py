def main():
    n = int(input())
    while n > 0:
        n -= 1
        s = input()
        chars = {}
        maxLen = 0
        for c in s:
            if c in chars:
                chars[c] += 1
                if chars[c] > maxLen:
                    maxLen = chars[c]
            else:
                chars[c] = 1
        
        if maxLen <= (len(s) - maxLen + 1):
            print(1)
        else:
            print(-1)

main()

'''
Input:
---
5
geeksforgeeks
bbbabaaacd
bbbbb
abab
aba

---
Output:
1
1
-1
'''