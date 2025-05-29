def main():
    t = int(input())
    result = []
    for _ in range(t):
        s = input()
        arr = [int(char) for char in s]
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            for j in range(i - 1, -1, -1):
                sum += int(''.join(str(digit) for digit in arr[j:i+1]))
        result.append(sum)
        
    print('\n'.join(map(str, result)))    
    
if __name__ == "__main__":
    main()

'''
Input:
2
1234
421

---
Output:
1670
491
'''