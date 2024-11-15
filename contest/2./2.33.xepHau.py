import copy

def handle(*, n, curr = [], arr= None, xuoi= None, nguoc= None):
    if arr == None:
        arr = [True for _ in range(n)]
        xuoi = [True for _ in range(2 * n)]
        nguoc = [True for _ in range(2 * n)]
        
    row = len(curr)
    
    if row == n:
        yield curr
    
    for col in range(n):
        if arr[col] and xuoi[row - col + n] and nguoc[row + col] :
            arr[col] = False
            xuoi[row - col + n] = False
            nguoc[row + col] = False
            curr.append(col)
            yield from handle(n=n, curr= curr, arr= arr, xuoi= xuoi, nguoc= nguoc)
            arr[col] = True
            xuoi[row - col + n] = True
            nguoc[row + col] = True
            curr.pop()    

def main():
    result = handle(n= 4)
    for i in result:
        print(i)

main()