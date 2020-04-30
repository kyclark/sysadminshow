#!/usr/bin/env python3
"""Python implementation of head"""

import argparse
import io


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
    show_header = len(args.file) > 1
    heads = [head(fh, args.num, show_header) for fh in args.file]
    print('\n'.join(heads))


# --------------------------------------------------
def head(fh, num, show_header):
    """Return num lines from file handle"""

    lines = [f'==> {fh.name} <==\n'] if show_header else []
    for line_num, line in enumerate(fh, start=1):
        lines.append(line)
        if line_num == num:
            break

    return ''.join(lines)


# --------------------------------------------------
def test_head():
    """Test head"""

    assert head(io.StringIO('foo\nbar\nbaz\n'), 1, False) == 'foo\n'
    assert head(io.StringIO('foo\nbar\nbaz\n'), 2, False) == 'foo\nbar\n'


# --------------------------------------------------
if __name__ == '__main__':
    main()
