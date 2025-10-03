def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        dict_temp = {}
        count = 0
        for i in arr:
            if i in dict_temp:
                count += dict_temp[i]
            dict_temp[k - i] = dict_temp.get(k - i, 0) + 1
        
        results.append(count)
        
    print('\n'.join(map(str, results)))
        
if __name__ == "__main__":
    main()