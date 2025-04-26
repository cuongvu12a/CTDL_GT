from queue import PriorityQueue

def main():
    n = int(input())
    while n > 0:
        n -= 1
        m = int(input())
        nums = list(map(int, input().split()))
        pq = PriorityQueue()
        for num in nums:
            pq.put(num)
            
        res = 0
        while pq.qsize() > 1:
            first = pq.get()
            second = pq.get()
            res += first + second
            pq.put(first + second)
            
        print(res)
            

main()

''' 
Input:
---
2
4
4 3 2 6
5
4 2 7 6 9

---
Output:
29
62
'''