from DepthFirst import *
from IterativeDeepening import *
from AStar import *

print("Please enter a grid by entering numbers in the form: 1 2 3 4 5 6 7 8 9")
print("| 1 2 3 |\n"
      "| 4 5 6 |\n"
      "| 7 8 9 |")

# temp hardcoded puzzle just to test things out
puzzle = ((9, 2, 8), (4, 1, 6), (7, 5, 3))
depthSearch(puzzle)
