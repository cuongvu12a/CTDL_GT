def maze(*, curr = [0, 0], map, way= []):
    step = [
        {
            'name': 'D',
            'x': 0,
            'y': 1,
        },
        {
            'name': 'R',
            'x': 1,
            'y': 0,
        },
        {
            'name': 'L',
            'x': -1,
            'y': 0,
        },
        {
            'name': 'U',
            'x': 0,
            'y': -1,
        },
    ]
    xLen = len(map)
    yLen = len(map[0])
    if curr[0] == xLen - 1 and curr[1] == yLen - 1:
        yield way
    
    for ne in step:
        xNe= curr[0] + ne['x']
        yNe= curr[1] + ne['y']
        
        if xNe >= xLen or yNe >= yLen or xNe < 0 or yNe < 0:
            continue
        
        if(map[yNe][xNe] == 1):
            map[yNe][xNe] = 0
            way.append(ne['name'])
            yield from maze(curr=[xNe, yNe], map= map)
            way.pop()
            map[yNe][xNe] = 1
    else:
        return
            
    
def main():
    # maze(map= [
    #     [1, 0, 0, 0],
    #     [1, 1, 0, 1],
    #     [0, 1, 0, 0],
    #     [0, 1, 1, 1],
    # ])
    
    # maze(map= [
    #     [1, 0, 0, 0],
    #     [1, 1, 0, 1],
    #     [1, 1, 0, 0],
    #     [0, 1, 1, 1],
    # ])
    ways = maze(map= [
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
    ])
    
    for way in ways:
        print(''.join(way))    
       
main()