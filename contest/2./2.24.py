def handle(*, curr, input, target, arr= []):
    # total = sum(num for index, num in enumerate(input) if curr[index] == 1)
    total = sum(arr)
    if total > target:
        return
    if total == target:
        yield arr
        
    for index, num in enumerate(input):
        if curr[index] == 1:
            continue
        
        for i in range(index + 1):
            curr[i] = 1    
        arr.append(num)
        yield from handle(curr=curr, input=input, target=target)
        for i in range(index + 1):
            curr[i] = 0
        arr.pop()

def main():
    # target = 50
    # input= [5, 10, 15, 20, 25]
    target = 53
    input= [15, 22, 14, 26, 32, 9, 16, 8]
    curr= [0] * len(input)
    result = handle(input=input, curr=curr, target= target)
    for i in result:
        print(i)
        
main()