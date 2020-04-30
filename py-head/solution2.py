#!/usr/bin/env python3
"""Python implementation of head"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python implementation of head',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file')

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_files = len(args.file)

    for fnum, fh in enumerate(args.file, start=1):
        if num_files > 1:
            print(f'==> {fh.name} <==')

        for line_num, line in enumerate(fh, start=1):
            print(line, end='')
            if line_num == args.num:
                break

        if num_files > 1 and fnum < num_files:
            print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
