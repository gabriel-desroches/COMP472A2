import time
import os

# helper function to swap perform a swap
def elem_swap(node, i, j, newI, newJ):
    # Tuples are immutable so create a list and then convert
    newList = [list(y) for y in node]
    newList[i][j], newList[newI][newJ] = newList[newI][newJ], newList[i][j]

    return tuple(tuple(x) for x in newList)

class Node:
    '''Node class containing parent state and current depth; used as value to a dict'''
    __slots__ = ('parent', 'depth')

    def __init__(self, parent, depth):
        self.parent = parent
        self.depth = depth

class IDS:
    '''IDS implementation'''
    def __init__(self, puzzle, end_state):
        # info about the puzzle configuration
        self.puzzle = puzzle
        self.N_COL  = len(puzzle)
        self.N_ROW  = len(puzzle[0])
        self.end_state = end_state
        # analytical info
        self.searchPathLength = 0
        self.startTime = time.time()
        # search algorithm param 
        self.max_depth = 0
        # output param
        if not os.path.exists('Outputs'):
            os.makedirs('Outputs')
        self.searchFile = open("./Outputs/IDS Search Path.txt", 'w')
        self.searchFile.write('Here is the IDS search path:\n\n')
        self.solutionFile = open("./Outputs/IDS Solution Path.txt", 'w')
        self.solutionFile.write('Here is the IDS solution path:\n\n')

    def run(self):
        '''
        pop top element in open list and insert on top its children until open list is empty or time exceeds
        '''
        print(f'\nStarting IDS search for {self.N_COL}X{self.N_ROW}\n{self.puzzle}\n')
        while True:
            if time.time() - self.startTime > 60:
                print("Exceeded 60 seconds. Solution not found!")
                self.searchFile.write('no solution')
                self.solutionFile.write('no solution')
                return None
            # reset search algorithm param 
            self.open_list = {self.puzzle: Node('root', 0)} # Open dict using key as current state and value as node info
            self.closed_list = {} # Closed/visited set
            while self.open_list:   # Search graph until no more to search depending on max_depth
                if time.time() - self.startTime > 60:
                    print("Exceeded 60 seconds. Solution not found!")
                    self.searchFile.write('no solution')
                    self.solutionFile.write('no solution')
                    return None

                # pop top element from open_list as a tuple of (current_state, Node(parent, depth))
                node = self.open_list.popitem()
                self.searchPathLength += 1
                self.searchFile.write(str(node[0]) + '\n')

                if node[0] == self.end_state:
                    return self.post_search_info(node)
                
                # Generate children of current puzzle state if its depth is less than the limit max depth
                if node[1].depth < self.max_depth:
                    children = self.generateChildren(node[0])
                    # Add to Closed Set
                    self.closed_list[node[0]] = node[1].parent
                    
                    for child in children:
                        if child in self.closed_list:
                            continue
                        if child in self.open_list:
                            continue
                        self.open_list[child] = Node(node[0], node[1].depth + 1)
            
            # increment max depth given open has been all searched
            self.max_depth += 1

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
        previousState = node[1].parent
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
