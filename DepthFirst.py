import heapq

endState = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

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
        print(count)
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
    for i in range(len(state)):
        for j in range (len(state)):
            #Optimize this section to use a loop?
            move1 = swap(state, i, j, i + 1, j)
            move2 = swap(state, i, j, i - 1, j)
            move3 = swap(state, i, j, i, j + 1)
            move4 = swap(state, i, j, i, j - 1)

            # Add to moves but don't list duplicates
            # Also needs optimization
            if move1 is not None and move1 not in moves:
                moves.append(move1)
            if move2 is not None and move2 not in moves:
                moves.append(move2)
            if move3 is not None and move3 not in moves:
                moves.append(move3)
            if move4 is not None and move4 not in moves:
                moves.append(move4)

    return moves


# helper function to swap perform a swap
def swap(state, i, j, newI, newJ):
    # Check if move is valid, use len to allow for bigger or smaller puzzles
    if (newI < 0 or newI >= len(state)) or (newJ < 0 or newJ >= len(state)):
        return None

    # Tuples are immutable so create a list and then convert
    newList = [[0 for x in range(len(state))] for y in range(len(state))]

    for x in range(len(state)):
        for y in range(len(state)):
            if(x == i and y == j):
                newList[x][y] = state[newI][newJ]
            elif((x == newI and y == newJ)):
                newList[x][y] = state[i][j]
            else:
                newList[x][y] = state[x][y]

    return tuple(tuple(x) for x in newList)
