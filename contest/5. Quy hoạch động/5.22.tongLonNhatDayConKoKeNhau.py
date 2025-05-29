def main():
    t = int(input())
    results = []
    for _ in range(t):
        n  = int(input())
        a = list(map(int, input().split()))
        dp = [0] * n
        dp[0] = a[0]
        dp[1] = max(a[0], a[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
                
        results.append(dp[n-1])
        
    print('\n'.join(map(str, results)))
    
if __name__ == "__main__":
    main()
    
'''
Input:
2
6
5 5 10 100 10 5
4
3 2 7 10

---
Output:
110
13
'''