def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        giao = []
        hop = []
        i, j = 0, 0
        while i < n and j < m:
            if a[i] < b[j]:
                hop.append(a[i])
                i += 1
            elif a[i] > b[j]:
                hop.append(b[j])
                j += 1
            else:
                giao.append(a[i])
                hop.append(a[i])
                i += 1
                j += 1
        while i < n:
            hop.append(a[i])
            i += 1
        while j < m:
            hop.append(b[j])
            j += 1  
        
        results.append(f"{' '.join(map(str, hop))}\n{' '.join(map(str, giao))}")
    print("\n".join(results))

if __name__ == "__main__":
    main()
