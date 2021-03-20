import time

def setup_heuristic(heuristic):
    if heuristic == 'M':
        return Heuristic('Manhattan')
    elif heuristic == 'SPI':
        return Heuristic('SumOfPermutationInversion')
    else:
        return 'error'


def element_swap(state, i, j, newI, newJ):
    # Tuples are immutable so create a list and then convert
    newList = [list(y) for y in state]
    newList[i][j], newList[newI][newJ] = newList[newI][newJ], newList[i][j]

    return tuple(tuple(x) for x in newList)


class AStar:

    def __init__(self, puzzle, heuristic):
        self.heuristic = setup_heuristic(heuristic)
        # make local
        self.currentState = State(puzzle, self.heuristic.calculate_cost(puzzle))
        self.size = len(puzzle)
        self.initialState = State(puzzle, self.heuristic.calculate_cost(puzzle))
        self.endState = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        self.searchFile = open("AStar Search Path.txt", 'w')
        self.solutionFile = open("AStar Solution Path.txt", 'w')
        # self.path = set()
        # self.visited = set()
        self.openList = []
        self.openList.append(self.currentState)
        self.closedList = set()
        self.startTime = time.time()
        self.run()

    def run(self):
        if not self.valid_input():
            return
        print('\nStarting AStar search for ' + str(self.size) + 'X' + str(self.size) + ' puzzle using heuristic:' +
              self.heuristic.name + '\n')
        while True:
            if self.endState == self.currentState.puzzleState:
                print("Successfully reached goal state!")
                self.post_search_info()
                break
            if time.time() - self.startTime > 60:
                print("Exceeded 60 seconds. Solution not found!")
                break
            self.execute_move()

    # perhaps make current node local
    def execute_move(self):
        self.openList.sort(key=lambda state: state.cost, reverse=True)
        self.currentState = self.openList.pop()
        self.closedList.add(self.currentState)
        possible_moves = self.generate_children(self.currentState.puzzleState)
        for possible_move in possible_moves:
            possible_move = State(possible_move, self.heuristic.calculate_cost(possible_move))
            move_not_considered = False
            for closedListState in self.closedList:
                if possible_move.puzzleState == closedListState and possible_move.cost > closedListState.cost:
                    move_not_considered = True
                    break
            if move_not_considered:
                continue
            for openListState in self.openList:
                if possible_move.puzzleState == openListState and possible_move.cost > openListState.cost:
                    move_not_considered = True
                    break
            if move_not_considered:
                continue
            self.openList.append(possible_move)

    def valid_input(self) -> bool:
        #maybe change this
        if 'name' not in self.heuristic.__dict__:
            print('The heuristic proposed is not supported. A* search is aborted.')
            return False
        for row in self.initialState.puzzleState:
            if self.size != len(row):
                print('The puzzle proposed is not NxN. A* search is aborted.')
                return False
        else:
            return True

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

    # helper function to swap perform a swap


class State:
    def __init__(self, puzzle_state, cost):
        self.puzzleState = puzzle_state
        self.cost = cost


class Heuristic:
    def __init__(self, name):
        self.name = name

    def calculate_cost(self, move) -> int:
        if self.name== 'Manhattan':
            #call cost method
            return 0
        if self.name == 'Sum of Permutation Inversion':
            # call cost method
            return 0
        else:
            print('Error calculating cost')
            return 0


# class Manhattan(Heuristic):
#     def __init__(self):
#         self.name = 'Manhattan'
#
#     def calculate_cost(self, move) -> int:
#         # return cost
#         pass
#
#
# class SumOfPermutationInversion(Heuristic):
#     def __init__(self):
#         self.name = 'Sum of Permutation Inversion'
#
#     def calculate_cost(self, move) -> int:
#         # return cost
#         pass
