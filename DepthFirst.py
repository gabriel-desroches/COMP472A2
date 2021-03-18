import heapq

endState = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
N_SIZE = 3
searchFile = open("DFS Search Path.txt", 'w')
solutionFile = open("DFS Solution Path.txt", 'w')

# Non recursive depthFirstSearch because otherwise recursion depth limit is exceeded
def depthSearch(state):
    path = []
    visited = []
    heapq.heapify(visited)
    stack = [state]
    count = 0
    while (len(stack)) != 0:
        node = ()
        node = stack.pop()
        count += 1
        # print(count)
        searchFile.write(str(node)+'\n')

        if node not in path:
            visited.append(node)
            path.append(node)

        if node == endState:
            print("Found!")
            return path

        # Generate children of current puzzle state
        children = generateChildren(node)

        for child in children:
            if child not in visited:
                stack.append(child)


    return path


# Helper function to generate children
def generateChildren(state):
    moves = []
    for i in range(N_SIZE):
        for j in range (N_SIZE):
            if i < N_SIZE - 1:
                moves.append(swap(state, i, j, i + 1, j)) # vertical
            if j < N_SIZE - 1:
                moves.append(swap(state, i, j, i, j + 1)) # horizontal

    return moves


# helper function to swap perform a swap
def swap(state, i, j, newI, newJ):
    # Tuples are immutable so create a list and then convert
    newList = [list(y) for y in state]
    newList[i][j], newList[newI][newJ] = newList[newI][newJ], newList[i][j]

    return tuple(tuple(x) for x in newList)
