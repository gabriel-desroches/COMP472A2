import time


# determine heuristic to use
def setup_heuristic(heuristic):
    if heuristic == 'M':
        return Heuristic('Manhattan')
    elif heuristic == 'SPI':
        return Heuristic('Sum of Permutation Inversion')
    elif heuristic == 'H':
        return Heuristic('Hamming')
    else:
        return 'error'


# method to help determine possible moves
def element_swap(state, i, j, newI, newJ):
    # Tuples are immutable so create a list and then convert
    newList = [list(y) for y in state]
    newList[i][j], newList[newI][newJ] = newList[newI][newJ], newList[i][j]

    return tuple(tuple(x) for x in newList)


# verify if heuristic and puzzle size are okay
def valid_input(puzzle, heuristic) -> bool:
    if heuristic != 'M' and heuristic != 'SPI' and heuristic != 'H':
        print('The heuristic proposed is not supported. A* search is aborted.')
        return False
    for row in puzzle:
        if len(puzzle) != len(row):
            print('The puzzle proposed is not NxN. A* search is aborted.')
            return False
    else:
        return True


class AStar:

    def __init__(self, puzzle, heuristic):
        if not valid_input(puzzle, heuristic):
            return
        self.heuristic = setup_heuristic(heuristic)
        self.size = len(puzzle)
        self.initialState = State(puzzle, self.heuristic, None)
        self.currentState = self.initialState
        self.endState = ((1, 2, 3), (4, 5, 6), (7, 8, 9))  # TODO: generate this according to size
        self.searchPathLength = 0
        self.searchFile = open("AStar Search Path.txt", 'w')
        self.searchFile.write('Here is the a* search path:\n\n')
        self.solutionFile = open("AStar Solution Path.txt", 'w')
        self.solutionFile.write('Here is the a* solution path:\n')
        self.openList = []
        self.openList.append(self.initialState)
        self.closedList = set()
        self.startTime = time.time()
        self.run()

    # called after creating the a* search object to run the search
    def run(self):
        print('\nStarting AStar search for ' + str(self.size) + 'X' + str(self.size) + ' puzzle using heuristic: ' +
              self.heuristic.name + '\n')
        print(self.initialState.puzzleState)
        # keep searching trough the states until goal state is found or time exceeded
        while True:
            if self.endState == self.currentState.puzzleState:
                print("Successfully reached goal state!")
                self.post_search_info()
                break
            if time.time() - self.startTime > 60:
                print("Exceeded 60 seconds. Solution not found!")
                break
            self.execute_move()

    # this method executes a move (pops it from the priority list) and considers further possible moves
    def execute_move(self):
        self.openList.sort(key=lambda state: state.cost, reverse=True)
        self.currentState = self.openList.pop()
        self.searchFile.write(str(self.currentState.puzzleState) + '\n')
        self.searchPathLength = self.searchPathLength + 1
        self.closedList.add(self.currentState)
        possible_moves = self.generate_children(self.currentState.puzzleState)
        for possible_move in possible_moves:
            possible_move = State(possible_move, self.heuristic, self.currentState)
            move_not_considered = False
            # check if the state is already in the closed list with a smaller cost
            for closedListState in self.closedList:
                if possible_move.puzzleState == closedListState.puzzleState:
                    if possible_move.cost > closedListState.cost:
                        move_not_considered = True
                        break
            if move_not_considered:
                continue
            # check if the state is already in the open list with a smaller cost
            for openListState in self.openList:
                if possible_move.puzzleState == openListState.puzzleState and possible_move.cost > openListState.cost:
                    move_not_considered = True
                    break
            if move_not_considered:
                continue
            # append possible move to open list if it has not already been encountered with a smaller cost
            self.openList.append(possible_move)

    # display statistics after search is completed
    def post_search_info(self):
        print("--- %s seconds ---" % (time.time() - self.startTime) + '\n')
        self.solutionFile.write(self.currentState.get_solution_path())
        print('Length of search path: ' + str(self.searchPathLength))
        print('Length of solution path: ' + str(self.currentState.depth))
        print('Cost of the solution: ' + str(self.currentState.cost))

    # generate possible moves from a current state
    def generate_children(self, state):
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if i < self.size - 1:
                    moves.append(element_swap(state, i, j, i + 1, j))  # vertical
                if j < self.size - 1:
                    moves.append(element_swap(state, i, j, i, j + 1))  # horizontal

        return moves


class State:
    def __init__(self, puzzle_state, heuristic, state):
        self.puzzleState = puzzle_state
        self.parent = state
        if state is not None:
            self.depth = state.depth + 1
        else:
            self.depth = 1
        self.cost = heuristic.calculate_cost(puzzle_state, self.depth)

    def get_solution_path(self) -> str:
        solution_path = ''
        if self.parent is not None:
            solution_path = self.parent.get_solution_path()
        return solution_path + '\n' + str(self.puzzleState)


def manhattan_distance(state) -> int:
    size = len(state)
    cost = 0
    x_position = 0
    for row in state:
        y_position = 0
        for number in row:
            goal_row = (number - 1) // size
            goal_column = (number - 1) % size
            horizontal_distance = abs(x_position - goal_row)
            vertical_distance = abs(y_position - goal_column)
            cost += vertical_distance + horizontal_distance
            y_position = y_position + 1
        x_position = x_position + 1
    return cost


def hamming(state) -> int:
    cost = 0
    expected_value = 1
    for row in state:
        for number in row:
            if number != expected_value:
                cost = cost + 1
            expected_value = expected_value + 1
    return cost


def sum_of_permutation_inversion(state) -> int:
    size = len(state)
    cost = 0
    x_position = 0
    for row in state:
        y_position = 0
        for number in row:
            x_on_right = x_position
            y_on_right = y_position + 1
            while x_on_right < size:
                while y_on_right < size:
                    if state[x_on_right][y_on_right] < number:
                        cost = cost + 1
                    y_on_right = y_on_right + 1
                y_on_right = 0
                x_on_right = x_on_right + 1
            y_position = y_position + 1
        x_position = x_position + 1
    return cost


class Heuristic:
    def __init__(self, name):
        self.name = name

    def calculate_cost(self, state, depth) -> int:
        if self.name == 'Manhattan':
            return manhattan_distance(state) + depth
        if self.name == 'Sum of Permutation Inversion':
            return sum_of_permutation_inversion(state) + depth
        if self.name == 'Hamming':
            return hamming(state) + depth
        else:
            print('Error calculating cost')
            return 0
