from DepthFirst import *
from IterativeDeepening import *
from AStar import *
import argparse
import numpy as np

def main(args):
    '''
    Main configuration set here
    '''
    puzzle_list = list()

    with args.i as f:  # read input file
        first_line = f.readline().strip().split()
        assert len(first_line) == 3
        assert first_line[0] == '#'
        col, row = int(first_line[1]), int(first_line[2])
        assert col > 0
        assert row > 0

        for line in f:  # Add input puzzles into puzzle list
            puzzle = tuple(tuple(map(int, x.strip().split())) for x in line.strip().split(','))
            puzzle_list.append(puzzle)
    # print(*puzzle_list, sep = "\n")

    # TODO -------------------------------------------- 
    # format solution path to display important info
    # --------------------------------------------------

    # Generate expected solution
    end_list = list()
    i = 1
    for _ in range(col):
        end_list.append(tuple(range(i, i + row)))
        i = i + row
    end_state = tuple(end_list)
    # print(*end_state, sep = "\n")

    # Compile analysis data for the input puzzles
    totals = np.zeros(5) # total length of the solution and search paths, cost, execution time, and number of no solution.
    if args.a == 'DFS':
        for puzzle in puzzle_list:
            depthSearch(puzzle, end_state)
    elif args.a == 'IDS':
        for puzzle in puzzle_list:
            depthSearch(puzzle, end_state)
    else:
        for puzzle in puzzle_list:
            a = AStar(puzzle, args.a, end_state)
            puzzle_info = a.run()
            if (puzzle_info[0] != "error"):
                totals += puzzle_info
            else: 
                totals[4] += 1
    
    analysis = True
    if analysis: # For part 2.5 for analysis
        with open('analysis.txt', 'w',  encoding='utf-8') as f:
            avg = totals / len(puzzle_list)
            f.write(f'Average & total length of the solution paths: {avg[0]}, {totals[0]}\n')
            f.write(f'Average & total length of the search paths: {avg[1]}, {totals[1]}\n')
            f.write(f'Average & total number of no solution: {avg[4]}, {totals[4]}\n')
            f.write(f'Average & total cost: {avg[2]}, {totals[2]}\n')
            f.write(f'Average & total execution time: {avg[3]}, {totals[3]}\n')
            f.write(f'Optimality of the solution path: ??')

if __name__ == "__main__":
    '''
    Parse your command line arguments here for the input file and algorithm
    '''
    parser = argparse.ArgumentParser(description='S-Puzzle game which finds a solution \
        for each puzzles in the selected file given the different search algorithms')
    parser.add_argument('-i', metavar='FILENAME', required=True,
                        type=argparse.FileType('r'),
                        help='filename of the puzzles')
    parser.add_argument('-a', metavar='ALGORITHM', required=True,
                        choices=['DFS', 'IDS', 'M', 'SPI', 'H'],
                        help='search algorithms (DFS, IDS, M, SPI, H)')
    args = parser.parse_args()
    main(args)
