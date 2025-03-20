def genLengths(n): 
    lengths = [1]
    for i in range(1, n):
        lengths.append(lengths[i-1]*2+1)
    
    return lengths

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        lengths = genLengths(n)
        for i in range(len(lengths)-1, -1, -1):
            if k < lengths[i]:
                continue
            
            if k == lengths[i] + 1:
                print(i + 2)
                break
            
            k = k - lengths[i] - 2
        else:
            print(-1)
        
# main()

def pow(n, k):
    if k == 0:
        return 1
    
    temp = pow(n, k//2)
    if k % 2 == 0:
        return temp * temp
    return n * temp * temp


def main2():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        middle = pow(2, n-1)
        while True:
            if k == middle:
                print(n)
                break
            elif k > middle:
                k = 2 * middle - k

            n -= 1
            middle /= 2
            
main2()

'''
Input:
---
2
3 2
4 8

---
Output:
2
4
'''