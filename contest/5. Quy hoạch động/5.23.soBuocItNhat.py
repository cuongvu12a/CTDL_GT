import bisect

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        lis = []
        for num in a:
            pos = bisect.bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        print(lis)
        results.append(n - len(lis))
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
    
'''
Input:
1
7
2 3 5 1 4 7 6

---
Output:
3
'''