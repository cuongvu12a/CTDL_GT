import bisect

def longest_increasing_subsequence(arr):
    tail = []
    for num in arr:
        # Tìm vị trí cần chèn num vào để giữ tail tăng
        idx = bisect.bisect_left(tail, num)
        if idx == len(tail):
            tail.append(num)
        else:
            tail[idx] = num
        print(num, idx, tail)
    return len(tail)

def main():
    int(input())
    n = list(map(int, input().split()))
    res = {}
    for i in n:
        max_end = 1
        for j in res:
            if i > j:
                max_end = max(max_end, res[j] + 1)
        res[i] = max_end
                
    print(max(res.values()))
    print(longest_increasing_subsequence(n))
    

if __name__ == "__main__":
    main()
    
'''
Input:
---
6
1 2 5 4 6 2

---
Output:
4
'''
