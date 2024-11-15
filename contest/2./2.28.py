
def handle(*, input, total, count, curr = [], lastIndex = 0):
    if sum(curr) == total:
        yield curr
        return
    
    if sum(curr) > total or count == len(curr):
        return
    
    for index, num in enumerate(input):
        if(index < lastIndex):
            continue
        
        curr.append(num)
        yield from handle(input= input, total= total, count= count, curr= curr, lastIndex=index)
        curr.pop()
        
def main():
    for i in handle(input= [2, 4, 6, 8], total= 8, count= 4):
        print(i)
        
main()