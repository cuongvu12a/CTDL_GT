"""
BÀI 7. Sorting 7

Đề bài:
Cho mảng A[] gồm n phần tử. 
Hãy tìm dãy con liên tục A[L..R] sao cho khi sắp xếp lại dãy con này 
thì toàn bộ mảng A sẽ trở thành mảng được sắp xếp tăng dần.

Ví dụ:
A = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
=> Chỉ cần sắp xếp dãy con A[4..9] = [30, 25, 40, 32, 31, 35]
=> Sau khi sắp xếp lại dãy con này, toàn bộ mảng trở thành có thứ tự tăng.

Input:
- Dòng đầu tiên: số lượng bộ test T (1 ≤ T ≤ 100).
- Với mỗi test:
    + Dòng đầu: n (số phần tử của mảng, 1 ≤ n ≤ 10^6).
    + Dòng tiếp: n số nguyên A[i] (0 ≤ A[i] ≤ 10^7), cách nhau bởi khoảng trắng.

Output:
- Với mỗi test, in ra chỉ số L và R (vị trí bắt đầu và kết thúc của đoạn con cần sắp xếp).
- Chỉ số tính theo mảng 1-based (A[1]..A[n]).

Ví dụ:
Input:
2
11
10 12 20 30 25 40 32 31 35 50 60
9
0 1 15 25 6 7 30 40 50

Output:
4 9
3 6
"""

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        left, right = 0, n - 1
        for i in range(n - 2):
            if arr[i] > arr[i + 1]:
                left = i
                break
            
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                right = i
                break
        
        min, max = arr[left], arr[left]
        for i in range(left, right + 1):
            if arr[i] < min:
                min = arr[i]
            if arr[i] > max:
                max = arr[i]
        
        for i in range(left):
            if arr[i] > min:
                left = i
                break
        
        for i in range(n - 1, right, -1):
            if arr[i] < max:
                right = i
                break
        
        print(left + 1, right + 1)

if __name__ == "__main__":
    main()
