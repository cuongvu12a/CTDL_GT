def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n or j == m:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        results.append(dp[0][0])
        
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()

'''
Input:
3
3 2
3 6
3 0

---
Output:
10
84
1
'''