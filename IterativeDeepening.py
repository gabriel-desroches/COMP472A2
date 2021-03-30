import time
from DepthFirst import generateChildren
from DepthFirst import element_swap
searchPath = open("IDS_Search_Path.txt", "w")
solutionPath = open("IDS_Solution_Path", "w")

def iterativeDeepening(initState, endState, maxDepth):
    path = set()
    visited = set()
    openList = [initState]
    count = 0
    level = 0
    start_time = time.time()
    while (len(openList)) != 0:
        if time.time() - start_time > 60:
            print("Exceeded 60 seconds. Solution not found!")
            return path

        node = openList.pop()
        count += 1
        searchPath.write(str(node)+'\n')

        if node not in path:
            visited.add(node)
            path.add(node)

        if node == endState:
            print("Found!")
            print(f"{count}: openList({len(openList)}), visited({len(visited)})")
            print("--- %s seconds ---" % (time.time() - start_time))
            return path

        if level < maxDepth:
            children = generateChildren(node, len(endState), len(endState[0]))
            for child in children:
                if child not in visited:
                    openList.append(child)
            level = level + 1

    return path
