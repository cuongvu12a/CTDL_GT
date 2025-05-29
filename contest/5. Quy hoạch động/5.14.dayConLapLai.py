def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        s = " " + s
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i] == s[j] and i != j:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        print(dp[n][n])
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
3
abc
5
axxxy

---
Output:
0
2
'''