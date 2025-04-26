START_TIME_KEY = 0
END_TIME_KEY = 1

def main():
    n = int(input())
    while n > 0:
        n -= 1
        m = int(input())
        startTimes = list(map(int, input().split()))
        endTimes = list(map(int, input().split()))
        jobs = []
        for i in range(m):
            jobs.append((startTimes[i], endTimes[i]))
        
        jobs.sort(key=lambda x: x[END_TIME_KEY])

        count = 0
        currTime = 0
        for job in jobs:
            if job[START_TIME_KEY] >= currTime:
                count += 1
                currTime = job[END_TIME_KEY]
        
        print(count)
        
main()

''' 
Input:
---
1
6
1 3 0 5 8 5
2 4 6 7 9 9

---
Output:
4
'''