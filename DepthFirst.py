import time
import os

# helper function to swap perform a swap
def elem_swap(node, i, j, newI, newJ):
    # Tuples are immutable so create a list and then convert
    newList = [list(y) for y in node]
    newList[i][j], newList[newI][newJ] = newList[newI][newJ], newList[i][j]

    return tuple(tuple(x) for x in newList)

class DFS:
    def __init__(self, puzzle, end_state):
        self.puzzle = puzzle
        self.N_COL  = len(puzzle)
        self.N_ROW  = len(puzzle[0])
        self.end_state = end_state
        self.searchPathLength = 0
        self.open_list = {puzzle: 'root'} # Open
        self.closed_list = {} # Closed
        if not os.path.exists('Outputs'):
            os.makedirs('Outputs')
        self.searchFile = open("./Outputs/DFS Search Path.txt", 'w')
        self.searchFile.write('Here is the DFS search path:\n\n')
        self.solutionFile = open("./Outputs/DFS Solution Path.txt", 'w')
        self.solutionFile.write('Here is the DFS solution path:\n\n')
        self.startTime = time.time()

    # Non recursive depthFirstSearch because otherwise recursion depth limit is exceeded
    def run(self):
        # end_state info
        print(f'\nStarting AStar search for {self.N_COL}X{self.N_ROW}\n{self.puzzle}\n')
        while self.open_list:
            if time.time() - self.startTime > 60:
                print("Exceeded 60 seconds. Solution not found!")
                self.searchFile.write('no solution')
                self.solutionFile.write('no solution')
                return None

            node = self.open_list.popitem()
            self.searchPathLength += 1
            self.searchFile.write(str(node[0]) + '\n')

            if node[0] == self.end_state:
                return self.post_search_info(node)

            # Generate children of current puzzle state
            children = self.generateChildren(node[0])

            self.closed_list[node[0]] = node[1]  # Add to Closed Set
            
            for child in children:
                if child in self.closed_list:
                    continue
                if child in self.open_list:
                    continue
                self.open_list[child] = node[0]

    # Helper function to generate children
    def generateChildren(self, node):
        moves = set()
        for i in range(self.N_COL):
            for j in range(self.N_ROW):
                if i < self.N_COL - 1:
                    moves.add(elem_swap(node, i, j, i + 1, j))  # vertical
                if j < self.N_ROW - 1:
                    moves.add(elem_swap(node, i, j, i, j + 1))  # horizontal

        return moves
    
    # display statistics after search is completed
    def post_search_info(self, node):
        execution_time = (time.time() - self.startTime)
        print("--- %s seconds ---" % execution_time + '\n')
        # Retrace solution path
        solution = [node[0]]
        solution_length = 0
        previousState = node[1]
        while True:
            if previousState == 'root':
                break
            else:
                solution.append(previousState)
                previousState = self.closed_list[previousState]
                solution_length += 1

        for x in reversed(solution):
            self.solutionFile.write(str(x) + '\n')
        print(f'Length of search path: {self.searchPathLength}')
        print(f'Length of solution path: {solution_length}')
        print(f'Cost of the solution: {self.searchPathLength}')
        return solution_length, self.searchPathLength, self.searchPathLength, execution_time, 0
