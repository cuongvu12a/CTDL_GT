def handle(*, maze, curr = None, count = 0, min = float('inf'), visited = set()):
    if curr is None:
        curr = 0
        visited.add(curr)
        
    if(len(visited) == len(maze)):
        if count + maze[curr][0] < min:
            min = count + maze[curr][0]
        return min
    
    for i in range (len(maze)):
        if i not in visited:
            visited.add(i)
            count += maze[curr][i]
            min = handle(maze=maze, curr=i, count=count, min=min, visited=visited)
            count -= maze[curr][i]
            visited.remove(i)
    return min

def main():
    maze = [
        [0, 20, 35, 10],
        [20, 0, 90, 50],
        [35, 90, 0, 12],
        [10, 50, 12, 0],
    ]
    
    print(handle(maze=maze))
    
main()