"""
BÀI 10. Sorting 10

Đề bài:
Cho mảng A[] gồm n phần tử.
Nhiệm vụ: đưa ra mảng đã được sắp xếp bao gồm các chữ số của mỗi phần tử trong A[].

Ví dụ:
A[] = {110, 111, 112, 113, 114}
→ Kết quả: {0, 1, 2, 3, 4}

Input:
- Dòng đầu tiên đưa vào số lượng bộ test T.
- Những dòng tiếp theo đưa vào T bộ test:
    + Mỗi bộ test gồm hai dòng:
        * Dòng 1: n là số phần tử của mảng A[].
        * Dòng 2: n số A[i], các số cách nhau bởi khoảng trắng.
- Ràng buộc:
    1 ≤ T ≤ 100
    1 ≤ n ≤ 10^7
    0 ≤ A[i] ≤ 10^16

Output:
- Đưa ra kết quả mỗi test theo từng dòng (danh sách chữ số sắp xếp tăng dần, không lặp).

Ví dụ:
Input:
2
3
131 11 48
4
111 222 333 446

Output:
1 3 4 8
1 2 3 4 6
"""

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        seen = [False] * 10
        for i in arr:
            chars = str(i)
            for c in chars:
                seen[int(c)] = True
        
        result = [str(i) for i in range(10) if seen[i]]
        results.append(" ".join(result))
        
    print("\n".join(results))

if __name__ == "__main__":
    main()