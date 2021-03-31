import time
import collections

searchFile = open("DFS Search Path.txt", 'w')
solutionFile = open("DFS Solution Path.txt", 'w')

class Node():
    __slots__ = ['state', 'parent']

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

# Non recursive depthFirstSearch because otherwise recursion depth limit is exceeded
def depthSearch1(state, end_state):
    open_list = {state: 'root'} # Open
    closed_list = {} # Closed
    searchPathLength = 0
    # end_state info
    N_COL = len(end_state)
    N_ROW = len(end_state[0])
    print(f'Starting AStar search for {N_COL}X{N_ROW}\n{state}\n')
    start_time = time.time()
    while open_list:
        if time.time() - start_time > 60:
            print("Exceeded 60 seconds. Solution not found!")
            return None

        node = open_list.popitem()
        searchPathLength += 1
        # print(f"{count}: stack({len(stack)}), closed_list({len(closed_list)})")
        searchFile.write(str(node[0]) + '\n')

        if node[0] == end_state:
            print("Found!")
            print(f"{searchPathLength}: open_list({len(open_list)}), closed_list({len(closed_list)})")
            print("--- %s seconds ---" % (time.time() - start_time))
            solution = [node[0]]
            previousState = node[1]
            while True:
                solution.append(previousState)
                if previousState == 'root':
                    break
                else:
                    previousState = closed_list[previousState]

            for x in reversed(solution):
                solutionFile.write(str(x) + '\n')

            return

        # Generate children of current puzzle state
        children = generateChildren1(node[0], N_COL, N_ROW)

        closed_list[node[0]] = node[1]  # Add to Closed Set
        
        for child in children:
            if child in closed_list:
                continue
            if child in open_list:
                continue
            open_list[child] = node[0]

# Non recursive depthFirstSearch because otherwise recursion depth limit is exceeded
def depthSearch(state, end_state):
    rootNode = Node(state)
    open_list = collections.deque([rootNode]) # Open
    closed_list = set() # Closed
    searchPathLength = 0
    # end_state info
    N_COL = len(end_state)
    N_ROW = len(end_state[0])
    print(f'Starting AStar search for {N_COL}X{N_ROW}\n{state}\n')
    start_time = time.time()
    while open_list:
        if time.time() - start_time > 60:
            print("Exceeded 60 seconds. Solution not found!")
            return None

        node = open_list.popleft()
        searchPathLength += 1
        # print(f"{count}: stack({len(stack)}), closed_list({len(closed_list)})")
        searchFile.write(str(node.state) + '\n')

        if node.state == end_state:
            print("Found!")
            print(f"{searchPathLength}: open_list({len(open_list)}), closed_list({len(closed_list)})")
            print("--- %s seconds ---" % (time.time() - start_time))
            retraceSolution(node)
            return

        # Generate children of current puzzle state
        children = generateChildren(node, N_COL, N_ROW)

        closed_list.add(node.state)  # Add to Closed Set
        
        for child in children:
            if child.state in closed_list:
                continue
            # if child.state in open_list:
            #     continue
            # open_list.appendleft(child)
            appendChild = True
            for nodes in open_list:
                if child.state == nodes.state:
                    appendChild = False
            if appendChild:
                open_list.appendleft(child)

# Helper function to generate children
def generateChildren1(node, N_COL, N_ROW):
    moves = set()
    for i in range(N_COL):
        for j in range(N_ROW):
            if i < N_COL - 1:
                moves.add(elem_swap1(node, i, j, i + 1, j))  # vertical
            if j < N_ROW - 1:
                moves.add(elem_swap1(node, i, j, i, j + 1))  # horizontal

    return moves

# Helper function to generate children
def generateChildren(node, N_COL, N_ROW):
    moves = []
    for i in range(N_COL):
        for j in range(N_ROW):
            if i < N_COL - 1:
                moves.append(elem_swap(node, i, j, i + 1, j))  # vertical
            if j < N_ROW - 1:
                moves.append(elem_swap(node, i, j, i, j + 1))  # horizontal

    for x in moves:
        x.parent = node
    return moves

# helper function to swap perform a swap
def elem_swap1(node, i, j, newI, newJ):
    # Tuples are immutable so create a list and then convert
    newList = [list(y) for y in node]
    newList[i][j], newList[newI][newJ] = newList[newI][newJ], newList[i][j]

    return tuple(tuple(x) for x in newList)

# helper function to swap perform a swap
def elem_swap(node, i, j, newI, newJ):
    # Tuples are immutable so create a list and then convert
    newList = [list(y) for y in node.state]
    newList[i][j], newList[newI][newJ] = newList[newI][newJ], newList[i][j]

    return Node(tuple(tuple(x) for x in newList))

# Traces Solution Path Backwards
def retraceSolution(node):
    solution = []
    currentNode = node
    while True:
        solution.append(currentNode.state)
        if currentNode.parent is None:
            break
        else:
            currentNode = currentNode.parent

    for x in reversed(solution):
        solutionFile.write(str(x) + '\n')