def handle(*, graph, curr = 0, count = 0, maximum = 0):
    if len(graph[curr]) == 0:
        if count > maximum:
            maximum = count
        return maximum
    
    nextRange = [i for i in graph[curr]]
    for next in nextRange:
        count += 1
        graph[curr].remove(next)
        graph[next].remove(curr)
        maximum = max(maximum, handle(graph=graph, curr=next, count=count, maximum=maximum))
        graph[curr].append(next)
        graph[next].append(curr)
        count -= 1
    
    return maximum

def main():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    print(graph)
    print(handle(graph=graph))
    
main()
