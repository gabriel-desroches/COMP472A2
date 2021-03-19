from AStar import *

print("Please enter a grid by entering numbers in the form: 1 2 3 4 5 6 7 8 9")
print("| 1 2 3 |\n"
      "| 4 5 6 |\n"
      "| 7 8 9 |")

puzzle = ((6, 1, 2), (7, 8, 3), (5, 4, 9))

# a* heuristic: enter M for Manhattan or SPI for Sum of Permutation Inversion
astarSearch = AStar(puzzle, 'M')

