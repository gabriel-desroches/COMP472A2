import time

endState = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
N_SIZE = len(endState)
searchFile = open("DFS Search Path.txt", 'w')
solutionFile = open("DFS Solution Path.txt", 'w')


class Node():
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


# Non recursive depthFirstSearch because otherwise recursion depth limit is exceeded
def depthSearch(state):
    path = set()
    visited = set()
    rootNode = Node(state)
    stack = [rootNode]
    count = 0
    start_time = time.time()
    while (len(stack)) != 0:
        if time.time() - start_time > 60:
            print("Exceeded 60 seconds. Solution not found!")
            return path

        node = stack.pop()
        count += 1
        # print(f"{count}: stack({len(stack)}), visited({len(visited)})")
        searchFile.write(str(node.state) + '\n')

        if node not in path:
            visited.add(node.state)
            path.add(node)

        if node.state == endState:
            print("Found!")
            print(f"{count}: stack({len(stack)}), visited({len(visited)})")
            print("--- %s seconds ---" % (time.time() - start_time))
            retraceSolution(node)
            return path

        # Generate children of current puzzle state
        children = generateChildren(node)

        for child in children:
            if child.state not in visited:
                stack.append(child)

    return path


# Helper function to generate children
def generateChildren(node):
    moves = []
    for i in range(N_SIZE):
        for j in range(N_SIZE):
            if i < N_SIZE - 1:
                moves.append(elem_swap(node, i, j, i + 1, j))  # vertical
            if j < N_SIZE - 1:
                moves.append(elem_swap(node, i, j, i, j + 1))  # horizontal

    for x in moves:
        x.parent = node
    return moves


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

if __name__ == "__main__":
    puzzle = ((9, 2, 8), (4, 1, 6), (3, 5, 7))
    depthSearch(puzzle)
