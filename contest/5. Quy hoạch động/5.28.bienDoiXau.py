def main():
    t = int(input())
    for _ in range(t):
        str1, str2 = input().split()
        n = len(str1)
        m = len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        print(dp[n][m])
        
if __name__ == "__main__":
    main()
    
'''
Input:
1
geek gesek

---
Output:
1
'''