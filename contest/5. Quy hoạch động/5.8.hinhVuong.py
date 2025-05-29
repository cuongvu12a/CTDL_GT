def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = [list(map(int, input().split())) for _ in range(n)]
        dp = [[0] * m for _ in range(n)]
        max_size = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                        max_size = max(max_size, dp[i][j])

        print(max_size)
if __name__ == "__main__":
    main()
    
    
'''
Input:
---
2
6 5
0 1 1 0 1
1 1 0 1 0
0 1 1 1 0
1 1 1 1 0
1 1 1 1 1
0 0 0 0 0
2 2
0 0
0 0

---
Output:
3
0
'''