def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def find_prime_pair(N):
    prime = sieve(N)
    for p in range(2, N // 2 + 1):
        if prime[p] and prime[N - p]:
            return (p, N - p)
    return -1

# Thử nghiệm
print(find_prime_pair(10))  # (3, 7)
print(find_prime_pair(11))  # (5, 6) => 6 không phải prime -> (11 không có) => -1
print(find_prime_pair(28))  # (5, 23)
