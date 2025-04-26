def main():
    t = int(input())
    while t > 0:
        t-=1
        tu, mau = map(int, input().split())
        result = []
        while True:
            if mau % tu == 0:
                result.append(f'1 / {mau // tu}')
                break
            temp = mau // tu  + 1
            result.append(f'1 / {temp}')
            tu = tu * temp - mau
            mau = mau * temp
        print(' + '.join(result))
        
main()

'''
Input:
---
2
2 3
1 3

---
Output:
1/2 + 1/6
1/3
'''