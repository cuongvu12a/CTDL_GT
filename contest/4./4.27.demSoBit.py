def val(centers, idx, n, currCenters):
    if idx % 2 == 1: return 1
    if idx == centers[currCenters]: return n % 2
    if idx < centers[currCenters]: return val(centers, idx, n // 2, currCenters - 1)
    return val(centers, 2 * centers[currCenters] - idx, n, currCenters)

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, l, r = map(int, input().split())
        centers = []
        temp = 2
        while temp <= n:
            centers.append(temp)
            temp *= 2
        sum =0
        for i in range(l, r+1, 1):
            sum += val(centers, i, n, len(centers) - 1)
        
        print(sum)

main()

'''
Input:
---
2
7 2 5
10 3 10

---
Output:
'''