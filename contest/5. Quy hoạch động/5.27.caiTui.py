def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, v = map(int, input().split())
        a_v = list(map(int, input().split()))
        a = list(map(int, input().split()))
        dp = [0] * (v + 1)
        for i in range(n):
            for j in range(v, a_v[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - a_v[i]] + a[i])
            
        results.append(dp[v])
    print('\n'.join(map(str, results)))
    
if __name__ == "__main__":
    main()
    
'''
Input:
1
15 10
5 2 1 3 5 2 5 8 9 6 3 1 4 7 8
1 2 3 5 1 2 5 8 7 4 1 2 3 2 1

---
Output:
15
'''