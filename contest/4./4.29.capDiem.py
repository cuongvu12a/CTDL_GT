import math

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)
    
    mid = len(points) // 2
    mid_point = points[mid]
    
    left_points = points[:mid]
    right_points = points[mid:]
    
    min_dist_left = closest_pair(left_points)
    min_dist_right = closest_pair(right_points)
    
    min_dist = min(min_dist_left, min_dist_right)
    
    strip = []
    for point in points:
        if abs(point[0] - mid_point[0]) < min_dist:
            strip.append(point)
            
    strip.sort(key=lambda x: x[1])
    
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            min_dist = min(min_dist, distance(strip[i], strip[j]))
    return min_dist

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        points = []
        while n > 0:
            n -= 1
            x, y = map(int, input().split())
            points.append((x, y))
    
        points.sort()
        print("{:.6f}".format(closest_pair(points)))

if __name__ == "__main__":
    main()

'''
Input:
---
2
6
2 3
12 30
40 50
5 1
12 10
3 4
3
0 0
3 0
4 0

---
Output:
1.414214
1.000000

'''