import time


def setup_heuristic(heuristic):
    if heuristic == 'M':
        return Heuristic('Manhattan')
    elif heuristic == 'SPI':
        return Heuristic('Sum of Permutation Inversion')
    else:
        return 'error'


def element_swap(state, i, j, newI, newJ):
    # Tuples are immutable so create a list and then convert
    newList = [list(y) for y in state]
    newList[i][j], newList[newI][newJ] = newList[newI][newJ], newList[i][j]

    return tuple(tuple(x) for x in newList)


def valid_input(puzzle, heuristic) -> bool:
    if heuristic != 'M' and heuristic != 'SPI':
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
        self.endState = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        self.searchFile = open("AStar Search Path.txt", 'w')
        self.solutionFile = open("AStar Solution Path.txt", 'w')
        self.openList = []
        self.openList.append(self.initialState)
        self.closedList = set()
        self.startTime = time.time()
        self.run()

    def run(self):
        print('\nStarting AStar search for ' + str(self.size) + 'X' + str(self.size) + ' puzzle using heuristic: ' +
              self.heuristic.name + '\n')
        print(self.initialState.puzzleState)
        while True:
            if self.endState == self.currentState.puzzleState:
                print("Successfully reached goal state!")
                self.post_search_info()
                break
            if time.time() - self.startTime > 60:
                print("Exceeded 60 seconds. Solution not found!")
                break
            self.execute_move()

    def execute_move(self):
        self.openList.sort(key=lambda state: state.cost, reverse=True)
        self.currentState = self.openList.pop()
        self.closedList.add(self.currentState)
        possible_moves = self.generate_children(self.currentState.puzzleState)
        for possible_move in possible_moves:
            possible_move = State(possible_move, self.heuristic, self.currentState)
            move_not_considered = False
            for closedListState in self.closedList:
                if possible_move.puzzleState == closedListState.puzzleState:
                    if possible_move.cost > closedListState.cost:
                        move_not_considered = True
                        break
            if move_not_considered:
                continue
            for openListState in self.openList:
                if possible_move.puzzleState == openListState.puzzleState and possible_move.cost > openListState.cost:
                    move_not_considered = True
                    break
            if move_not_considered:
                continue
            self.openList.append(possible_move)

    def post_search_info(self):
        print("--- %s seconds ---" % (time.time() - self.startTime))
        # more stuff

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
            self.depth = 0
        self.cost = heuristic.calculate_cost(puzzle_state, self.depth)


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


# not real sum of permutation, this is hamming
def sum_of_permutation_inversion(state) -> int:
    cost = 0
    expected_value = 1
    for row in state:
        for number in row:
            if number != expected_value:
                cost = cost + 1
            expected_value = expected_value + 1
    return cost


class Heuristic:
    def __init__(self, name):
        self.name = name

    def calculate_cost(self, state, depth) -> int:
        if self.name == 'Manhattan':
            return manhattan_distance(state) + depth
        if self.name == 'Sum of Permutation Inversion':
            return sum_of_permutation_inversion(state) + depth
        else:
            print('Error calculating cost')
            return 0
