def count_ways(A, K):
    dp = [0] * (K + 1)
    dp[0] = 1

    for i in range(1, K + 1):
        for a in A:
            if i >= a:
                dp[i] += dp[i - a]

    return dp[K]

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        A = list(map(int, input().split()))
        print(count_ways(A, k))

if __name__ == "__main__":
    main()