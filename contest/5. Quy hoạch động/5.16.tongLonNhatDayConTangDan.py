def main():
    t = int(input())
    output = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        dp = [i for i in a]
        dp[0] = a[0]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if a[i] > a[j]:
                    dp[i] = max(dp[i], dp[j] + a[i])
        output.append(str(max(dp)))

    print("\n".join(output))
        
if __name__ == "__main__":
    main()

'''
Input:
---
3
7
1 101 2 3 100 4 5
3
10 7 5
4
1 2 3 5

---
Output:
106
10
11

'''