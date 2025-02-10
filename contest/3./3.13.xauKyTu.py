from queue import PriorityQueue

def main():
    n = int(input())
    while n > 0:
        n -= 1
        d = int(input())
        s = input()
        chars = {}
        for c in s:
            if c in chars:
                chars[c] += 1
                # if chars[c] > maxLen:
                #     maxLen = chars[c]
            else:
                chars[c] = 1
        
        pq = PriorityQueue()
        for c in chars:
            pq.put((-chars[c], chars[c]))
            
        print(pq.get())

main()

'''
Input:
---
2
2
aaaabbcc
2
aaaabbbc

---
Output:
1
-1
'''