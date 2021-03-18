from DepthFirst import *
from IterativeDeepening import *
from AStar import *
import time
print("Please enter a grid by entering numbers in the form: 1 2 3 4 5 6 7 8 9")
print("| 1 2 3 |\n"
      "| 4 5 6 |\n"
      "| 7 8 9 |")

# temp hardcoded puzzle just to test things out
puzzle = ((1, 2, 8), (4, 5, 6), (3, 9, 7))
start_time = time.time()
depthSearch(puzzle)
print("--- %s seconds ---" % (time.time() - start_time))
