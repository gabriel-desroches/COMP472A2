import time

searchFile = open("DFS Search Path.txt", 'w')
solutionFile = open("DFS Solution Path.txt", 'w')


class Node():
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


# Non recursive depthFirstSearch because otherwise recursion depth limit is exceeded
def depthSearch(state, end_state):
    visited = set()  # Closed Set
    rootNode = Node(state)
    stack = [rootNode]  # Open Set
    count = 0
    # end_state info
    N_COL = len(end_state)
    N_ROW = len(end_state[0])

    start_time = time.time()
    while (len(stack)) != 0:
        if time.time() - start_time > 60:
            print("Exceeded 60 seconds. Solution not found!")
            return None

        node = stack.pop()
        count += 1
        # print(f"{count}: stack({len(stack)}), visited({len(visited)})")
        searchFile.write(str(node.state) + '\n')

        if node.state == end_state:
            print("Found!")
            print(f"{count}: stack({len(stack)}), visited({len(visited)})")
            print("--- %s seconds ---" % (time.time() - start_time))
            retraceSolution(node)
            return

        visited.add(node.state)  # Add to Closed Set

        # Generate children of current puzzle state
        children = generateChildren(node, N_COL, N_ROW)

        # Reject any children already present in open or closed sets. Optimize
        for child in children:
            appendChild = True
            if child.state in visited:
                appendChild = False
            else: #using else to try and improve performance. Will skip the second check if it isn't needed
                for nodes in stack:
                    if child.state == nodes.state:
                        appendChild = False
            if appendChild:
                stack.append(child)

    return None


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
