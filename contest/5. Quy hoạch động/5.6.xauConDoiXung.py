def main():
    t = int(input())
    for _ in range(t):
        s = input()
        dp = [[False] * len(s) for _ in range(len(s))]
        max_len = 1
        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_len = 2
                
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    max_len = length
        
        print(max_len)
    
    
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
abcbadd
aaaaa

---
Output:
5
5
'''