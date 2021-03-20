from DepthFirst import *
from IterativeDeepening import *
from AStar import *
import argparse

def main(args):
    '''
    Main configuration set here
    '''
    with args.i as f:
        print(f.read())

    # TODO build list of puzzle input
    #      create algo class according to args.a
    #      format solution path to display important info
    #      compile analysis data for the input puzzles


    # puzzle = ((9, 2, 8), (4, 1, 6), (3, 5, 7))
    # depthSearch(puzzle)

if __name__ == "__main__":
    '''
    Parse your command line arguments here for the input file and algorithm
    ''' 
    parser = argparse.ArgumentParser(description='S-Puzzle game which finds a solution \
        for each puzzles in the selected file given the different search algorithms')
    parser.add_argument('--i', metavar='FILENAME', required=True,
                        type=argparse.FileType('r'),
                        help='filename of the puzzles')
    parser.add_argument('--a', metavar='ALGORITHM', required=True,
                        choices=['DFS', 'IDS', 'A1', 'A2'],
                        help='search algorithms (DFS, IDS, A1, A2)')
    args = parser.parse_args()
    main(args)
