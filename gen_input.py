from codecs import open
import random
import argparse

def gen_input(args):
    '''Generate 20 random puzzles for which will be used as input'''
    n = args.row * args.col
    with open('input.txt', 'w',  encoding='utf-8') as f:
        f.write(f'# {args.row} {args.col}\n')
        for _ in range(20):
            puzzle = random.sample(range(1, n + 1), n)
            p_str = ' '.join(map(str, puzzle))
            f.write(f'{p_str}\n')

# gen_input()

if __name__ == "__main__":
    '''
    Parse your command line arguments here for number of rows and columns w/ default 3x3
    ''' 
    parser = argparse.ArgumentParser(description='Generate N random puzzles \
        with size ROW * COL with default 3x3.')
    parser.add_argument('n', metavar='N', type=int, nargs='?', default=20,
                        help='Number of columns (default: 3)')
    parser.add_argument('row', metavar='ROW', type=int, nargs='?', default=3,
                        help='Number of rows (default: 3)')
    parser.add_argument('col', metavar='COL', type=int, nargs='?', default=3,
                        help='Number of columns (default: 3)')
    args = parser.parse_args()
    assert(args.row > 0)
    assert(args.col > 0)
    gen_input(args)