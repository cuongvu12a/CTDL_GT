"""
BÀI 6. Sorting 6

Đề bài:
Cho mảng A[] gồm n phần tử. Các phần tử của mảng A[] chỉ bao gồm các số 0, 1, 2.  
Hãy sắp xếp mảng A[] theo thứ tự tăng dần.  

Ví dụ:  
A = [0, 2, 1, 2, 0]  
=> Kết quả: A = [0, 0, 1, 2, 2]

Input:
- Dòng đầu tiên: số lượng bộ test T (1 ≤ T ≤ 100).
- Với mỗi test:
    + Dòng đầu: n (số phần tử của mảng, 1 ≤ n ≤ 10^6).
    + Dòng tiếp: n số nguyên A[i] (0 ≤ A[i] ≤ 2), cách nhau bởi khoảng trắng.

Output:
- Với mỗi test, in ra mảng đã được sắp xếp tăng dần trên một dòng.

Ví dụ:
Input:
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1
"""

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    place_of_value = [0] + count[:-1]
    result = [0] * len(arr)
    for num in arr:
        result[place_of_value[num]] = num
        place_of_value[num] += 1
    
    return result

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        result = counting_sort(arr)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
