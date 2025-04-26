def sum (k, first, second): 
    firstStr = str(first)
    secondStr = str(second)
    length = len(firstStr) if len(firstStr) > len(secondStr) else len(secondStr)
    firstStr = firstStr.zfill(length)
    result = []
    temp = 0
    for i in range(length - 1, -1, -1):
        curr = int(firstStr[i]) + int(secondStr[i]) + temp
        result.append(curr % k)
        temp = curr // k
        
    if(temp > 0):
        result.append(temp)
    
    return ''.join(map(str, result[::-1]))


def main():
    k,a,b = map(int,input().split())
    print(sum(k,a,b))

main()

'''
Input:
---
2 1 10

---
Output:
11
'''