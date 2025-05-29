def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(max(0, i - 3), i):
                dp[i] += dp[j]
        results.append(dp[n])
    
    print('\n'.join(map(str, results)))
    
if __name__ == "__main__":
    main()
    
'''
Input:
2
1
5

---
Output:
1
13
'''