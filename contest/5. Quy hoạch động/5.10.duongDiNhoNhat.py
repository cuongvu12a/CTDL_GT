def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = [list(map(int, input().split())) for _ in range(n)]
        dp = [[float('inf')] * m for _ in range(n)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(m):
                left = float('inf') if j == 0 else dp[i][j - 1]
                up = float('inf') if i == 0 else dp[i - 1][j]
                left_up = float('inf') if i == 0 or j == 0 else dp[i - 1][j - 1]
                dp[i][j] = min(dp[i][j], left, up, left_up) + a[i][j]
        
        print(dp[n - 1][m - 1])

if __name__ == "__main__":
    main()
    
'''
Input:
---
1
3 3
1 2 3
4 8 2
1 5 3
---
Output:
8
'''