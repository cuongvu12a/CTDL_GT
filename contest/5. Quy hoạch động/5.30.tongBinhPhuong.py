import math

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = [math.pow(x, 2) for x in range(1, math.floor(math.sqrt(n) + 1))]
        if n == a[-1]:
            results.append(1)
        else:
            dp = [float('inf')] * (n + 1)
            dp[1] = 1
            for i in range(2, n + 1):
                for j in range(len(a) -1, -1, -1):
                    if a[j] <= i:
                        dp[i] = min(dp[i], dp[i - int(a[j])] + 1)
            results.append(dp[n])
        
    print('\n'.join(map(str, results)))
    
if __name__ == "__main__":
    main()
    
'''
Input:
3
100
6
25

---
Output:
1
3
1
'''