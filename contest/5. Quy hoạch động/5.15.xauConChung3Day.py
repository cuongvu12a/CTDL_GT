def main():
    t = int(input())
    for _ in range(t):
        n,m,k = map(int, input().split())
        s1, s2, s3 = input().split()
        s1 = " " + s1
        s2 = " " + s2
        s3 = " " + s3
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for l in range(1, k + 1):
                    if s1[i] == s2[j] and s2[j] == s3[l]:
                        dp[i][j][l] = dp[i - 1][j - 1][l - 1] + 1
                    else:
                        dp[i][j][l] = max(dp[i - 1][j][l], dp[i][j - 1][l], dp[i][j][l - 1])
        
        print(dp[n][m][k])
if __name__ == "__main__":
    main()

'''
Input:
---
2
5 8 13
geeks geeksfor geeksforgeeks
7 6 5
abcd1e2 bc12ea bd1ea

---
Output:
5
3
'''