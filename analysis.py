from DepthFirst import *
from IterativeDeepening import *
from AStar import *
import argparse
import numpy as np
import os

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

    # Generate expected solution
    end_list = list()
    i = 1
    for _ in range(col):
        end_list.append(tuple(range(i, i + row)))
        i = i + row
    end_state = tuple(end_list)
    # print(*end_state, sep = "\n")

    # Compile analysis data for the input puzzles
    if not os.path.exists('Outputs'):
        os.makedirs('Outputs')
    with open('./Outputs/analysis.txt', 'w',  encoding='utf-8') as f:
        for a in ['DFS', 'IDS', 'M', 'H', 'SPI']:
            totals = np.zeros(5) # total length of the solution and search paths, cost, execution time, and number of no solution.
            if a == 'DFS':
                for puzzle in puzzle_list:
                    d = DFS(puzzle, end_state)
                    puzzle_info = d.run()
                    if puzzle_info is not None:
                        totals += puzzle_info
                    else: 
                        totals[4] += 1
            elif a == 'IDS':
                for puzzle in puzzle_list:
                    i = IDS(puzzle, end_state, True)
                    puzzle_info = i.run()
                    if puzzle_info is not None:
                        totals += puzzle_info
                    else: 
                        totals[4] += 1
            else:
                for puzzle in puzzle_list:
                    a_star = AStar(puzzle, a, end_state)
                    puzzle_info = a_star.run()
                    if puzzle_info is not None:
                        totals += puzzle_info
                    else: 
                        totals[4] += 1
    
            avg = totals / len(puzzle_list)
            f.write(f'Analysis for algorithm {a}:\n')
            f.write(f'Average & total length of the solution paths: {avg[0]}, {totals[0]}\n')
            f.write(f'Average & total length of the search paths: {avg[1]}, {totals[1]}\n')
            f.write(f'Average & total number of no solution: {avg[4]}, {totals[4]}\n')
            f.write(f'Average & total cost: {avg[2]}, {totals[2]}\n')
            f.write(f'Average & total execution time: {avg[3]}, {totals[3]}\n')

        f.write(f'\nOptimality of the solution path: \n')
        for puzzle in puzzle_list:
            j = IDS(puzzle, end_state, False)
            puzzle_info = j.run()
            f.write(f'{puzzle}: {puzzle_info[0]} moves minimal\n')
            
if __name__ == "__main__":
    '''
    Parse your command line arguments here for the input file and algorithm
    '''
    parser = argparse.ArgumentParser(description='Generate an analysis over S-Puzzle games \
        for all different search algorithms')
    parser.add_argument('-i', metavar='FILENAME', required=True,
                        type=argparse.FileType('r'),
                        help='filename of the puzzles')
    args = parser.parse_args()
    main(args)
