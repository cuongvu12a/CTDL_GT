DEADLINE_KEY = 1
PROFIT_KEY = 2

def max_profit():
    n = int(input())
    while n > 0:
        n -= 1
        m = int(input())
        jobs = []
        maxDeadline = 0

        for _ in range(m):
            jobId, deadline, profit = map(int, input().split())
            jobs.append((jobId, deadline, profit))
            maxDeadline = max(maxDeadline, deadline)

        jobs.sort(key=lambda x: x[PROFIT_KEY], reverse=True)

        slots = [False] * (maxDeadline + 1)
        count = 0
        sumProfit = 0

        for job in jobs:
            jobId, deadline, profit = job

            for t in range(min(deadline, maxDeadline), 0, -1):
                if not slots[t]:
                    slots[t] = True
                    count += 1
                    sumProfit += profit
                    break
        
        print(count, sumProfit)

max_profit()

''' 
Input:
---
2
4
1 4 20
2 1 10
3 1 40
4 1 30
5
1 2 100
2 1 19
3 2 27
4 1 25
5 1 15

---
Output:
2 60
2 127
'''