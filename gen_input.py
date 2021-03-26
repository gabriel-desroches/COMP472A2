from codecs import open
import random
import argparse

def gen_input(args):
    '''Generate 20 random puzzles for which will be used as input'''
    n = args.row * args.col
    with open('input.txt', 'w',  encoding='utf-8') as f:
        f.write(f'# {args.col} {args.row}\n')
        for _ in range(args.n):
            puzzle = random.sample(range(1, n + 1), n)
            # denote new row with a comma
            pos = args.row 
            for _ in range(args.col - 1):
                puzzle.insert(pos,',')
                pos = pos + args.row + 1
            p_str = ' '.join(map(str, puzzle))
            f.write(f'{p_str}\n')

if __name__ == "__main__":
    '''
    Parse your command line arguments here for number of rows and columns w/ default 3x3
    ''' 
    parser = argparse.ArgumentParser(description='Generate N random puzzles \
        with size COL * ROW with default 3x3.')
    parser.add_argument('n', metavar='N', type=int, nargs='?', default=20,
                        help='Number of columns (default: 3)')
    parser.add_argument('col', metavar='COL', type=int, nargs='?', default=3,
                        help='Number of columns (default: 3)')
    parser.add_argument('row', metavar='ROW', type=int, nargs='?', default=3,
                        help='Number of rows (default: 3)')
    args = parser.parse_args()
    assert args.col > 0
    assert args.row > 0
    gen_input(args)