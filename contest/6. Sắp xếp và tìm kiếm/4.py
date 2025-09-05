"""
BÀI 4. Sorting 4

Đề bài:
Cho mảng A[] gồm n phần tử, mảng B[] gồm m phần tử khác nhau.  
Các phần tử của mảng A[] và B[] đã được sắp xếp tăng dần.  

Hãy tìm:
- Mảng hợp (Union): chứa tất cả phần tử của A và B, không trùng lặp, sắp xếp tăng dần.  
- Mảng giao (Intersection): chứa các phần tử xuất hiện trong cả A và B, sắp xếp tăng dần.  

Ví dụ:
A = [1, 3, 4, 5, 7]  
B = [2, 3, 5, 6]  
Union = [1, 2, 3, 4, 5, 6, 7]  
Intersection = [3, 5]  

Input:
- Dòng đầu tiên: số lượng bộ test T (1 ≤ T ≤ 100).
- Với mỗi test:
    + Dòng đầu: n, m (số phần tử của mảng A và B, 1 ≤ n, m ≤ 10^5).
    + Dòng thứ 2: n số nguyên A[i], sắp xếp tăng dần.
    + Dòng thứ 3: m số nguyên B[i], sắp xếp tăng dần.
    + Các số cách nhau bởi khoảng trắng.

Output:
- Với mỗi test, in ra 2 dòng:
    + Dòng 1: mảng Union
    + Dòng 2: mảng Intersection

Ví dụ:
Input:
1
5 3
1 2 3 4 5
1 2 3

Output:
1 2 3 4 5
1 2 3
"""

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        giao = []
        hop = []
        i, j = 0, 0
        while i < n and j < m:
            if a[i] < b[j]:
                hop.append(a[i])
                i += 1
            elif a[i] > b[j]:
                hop.append(b[j])
                j += 1
            else:
                giao.append(a[i])
                hop.append(a[i])
                i += 1
                j += 1
        while i < n:
            hop.append(a[i])
            i += 1
        while j < m:
            hop.append(b[j])
            j += 1  
        
        results.append(f"{' '.join(map(str, hop))}\n{' '.join(map(str, giao))}")
    print("\n".join(results))

if __name__ == "__main__":
    main()
