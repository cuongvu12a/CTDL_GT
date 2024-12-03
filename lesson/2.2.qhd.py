n, S = map(int, input().split())
w = list(map(int, input().split()))
dp = [0] * (S + 1)
dp[0] = 0

for P in range(1, S + 1):
    dp[P] = min(dp[P - x] for x in w if x <= P) + 1

print(dp)
print(dp[S])