from DepthFirst import *
from IterativeDeepening import *
from AStar import *
import argparse


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
    if args.a == 'DFS':
        for puzzle in puzzle_list:
            d = DFS(puzzle, end_state)
            d.run()
    elif args.a == 'IDS':
        for puzzle in puzzle_list:
            # i = IDS(puzzle, end_state)
            # i.run()
            return
    else:
        for puzzle in puzzle_list:
            a = AStar(puzzle, args.a, end_state)
            a.run()


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
