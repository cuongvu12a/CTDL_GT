from collections import Counter

def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        
        counts = Counter(a)
        
        arr = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        
        print(*(key for key, value in arr for _ in range(value)))

if __name__ == "__main__":
    main()
