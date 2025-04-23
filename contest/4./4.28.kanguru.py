def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        middle = n // 2
        seeding = 0
        idx = middle
        for i in range(middle):
            if idx >= n:
                seeding += 1
                continue
            
            while idx < n and a[i] // 2 < a[idx]:
                seeding += 1
                idx += 1
                
            if idx < n and a[i] // 2 >= a[idx]:
                seeding += 1
                idx += 1
            
        print(seeding)

if __name__ == "__main__":
    main()

'''
Input:
---
2
8
2 5 7 6 9 8 4 2
8
9 1 6 2 6 5 8 3

---
Output:
5
5

VD: [9, 8, 7, 6, 5, 4, 2, 2]
    - X chứa Y ở trong túi
    tối ưu nhất là chia đôi mảng X chạy từ 9 đến 6 và Y chạy từ 5 về 2
    xét X lần lượt:
        - nếu X // 2 >= Y thì có 1 cặp => seeding += 1 và duyệt đến Y tiếp theo idx += 1 (số lượng phần tử giảm được là ở cặp này)
        - nếu X // 2 < Y thì duyệt đến Y tiếp theo (Y giảm dần) idx += 1, Y hiện tại ko có túi để chui vào nên seeding += 1
        - nếu đã hết Y còn thừa X thì mặc định mỗi X là 1 seeding += 1
'''

