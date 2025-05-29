def greedy(pairs):
    pairs.sort(key=lambda x: x[1])
    
    count = 1
    last_end = pairs[0][1]

    for i in range(1, len(pairs)):
        if pairs[i][0] > last_end:
            count += 1
            last_end = pairs[i][1]

    return count

def main():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        a = []
        temp = list(map(int, input().split()))
        for i in range(n):
            x, y = temp[i * 2], temp[i * 2 + 1]
            a.append((x, y))
            
        a.sort(key=lambda x: x[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if a[i][0] > a[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        result.append(str(max(dp)))
        
    print("---")
    print("\n".join(result))

if __name__ == "__main__":
    main()