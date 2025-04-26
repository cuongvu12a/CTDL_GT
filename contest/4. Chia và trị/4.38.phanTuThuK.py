def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        i = 0
        j = 0
        while i < m and j < n:
            k -= 1
            curr = None
            if a[i] < b[j]:
                curr = a[i]
                i += 1
            else:
                curr = b[j]
                j += 1
            
            if k == 0:
                print(curr)
                break
        else:
            if i < m:
                print(a[i + k])
            else:
                print(b[j + k])
                
if __name__ == "__main__":
    main()
    
'''
Input:
---
1
5 4 5
2 3 6 7 9
1 4 8 10

---
Output:
6
'''
            