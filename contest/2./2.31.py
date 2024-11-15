def maze(*, curr = [0, 0], map, way= [], target, temp = None):
    step = [
        {
            'x': 0,
            'y': 1,
        },
        {
            'x': 1,
            'y': 0,
        },
        {
            'x': -1,
            'y': 0,
        },
        {
            'x': 0,
            'y': -1,
        },
        {
            'x': -1,
            'y': -1,
        },
        {
            'x': 1,
            'y': -1,
        },
        {
            'x': 1,
            'y': 1,
        },
        {
            'x': -1,
            'y': 1,
        }
    ]
    
    if temp == None:
        temp = [[1 for _ in row] for row in map]
    
    if len(target) == len(way) and all(target[i] == way[i] for i, v in enumerate(target)):
        yield ''.join(target)
        return
    
    xLen = len(map)
    yLen = len(map[0])
    
    for ne in step:
        xNe= curr[0] + ne['x']
        yNe= curr[1] + ne['y']
        
        if xNe >= xLen or yNe >= yLen or xNe < 0 or yNe < 0:
            continue
        
        if temp[yNe][xNe] == 1 and map[yNe][xNe] == target[len(way)]:
            temp[yNe][xNe] = 0
            way.append(map[yNe][xNe])
            yield from maze(curr=[xNe, yNe], map= map, target= target, way= way, temp= temp)
            way.pop()
            temp[yNe][xNe] = 1
        
def handle(*, map, dic):
    for i in dic:
        target = [s for s in i]
        for y, arrY in enumerate(map):
            for x, value in enumerate(arrY):
                if(map[x][y] == target[0]):
                    for result in maze(map= map, curr=[y, x], target= target, way=[target[0]]):
                        print(result)

def main():
    handle(map= [
    ['G', 'I', 'Z'],
    ['U', 'E', 'K'],
    ['Q', 'S', 'E'],
], dic= ['GEEKS', 'FOR', 'QUIZ', 'GO'])
    
main()
                    