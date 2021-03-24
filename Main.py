# from DepthFirst import *
# from IterativeDeepening import *
# from AStar import *
import argparse

def main(args):
    '''
    Main configuration set here
    '''
    puzzle_list = list()

    with args.i as f:   # read input file
        first_line = f.readline().strip().split()
        assert len(first_line) == 3
        assert first_line[0] == '#'
        row, col = int(first_line[1]), int(first_line[2])
        assert row > 0
        assert col > 0
        
        for line in f:  # Add input puzzles into puzzle list
            puzzle = tuple(tuple(map(int,x.strip().split())) for x in line.strip().split(','))
            puzzle_list.append(puzzle)
    # print(*puzzle_list, sep = "\n")
    # TODO 
    # create algo class according to args.a
    # format solution path to display important info
    # compile analysis data for the input puzzles

    if args.a == 'DFS':
        # for puzzle in puzzle_list:
        #   depthSearch(puzzle)
        pass
    elif args.a == 'IDS':
        # for puzzle in puzzle_list:
        #   depthSearch(puzzle)
        pass
    elif args.a == 'A1':
        # for puzzle in puzzle_list:
        #   depthSearch(puzzle)
        pass
    elif args.a == 'A2':
        # for puzzle in puzzle_list:
        #   AStar(puzzle, 'M')
        pass

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
                        choices=['DFS', 'IDS', 'A1', 'A2'],
                        help='search algorithms (DFS, IDS, A1, A2)')
    args = parser.parse_args()
    main(args)