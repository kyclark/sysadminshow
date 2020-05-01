#!/usr/bin/env python3
"""Write a bash script"""

import os
import sys
import re
import subprocess

# --------------------------------------------------
def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1 or args[0] == '-h':
        print('Usage: {} PROGRAM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    out_file = args[0]

    if len(out_file.strip()) < 1:
        print('Not a usable filename "{}"'.format(out_file))
        sys.exit(1)

    if not re.search(r'\.sh$', out_file):
        out_file = out_file + '.sh'

    if os.path.isfile(out_file):
        answer = input('"{}" exists.  Overwrite? [yN] '.format(out_file))
        if not re.match('^[yY]', answer):
            print('Will not overwrite. Bye!')
            sys.exit()

    fh = open(out_file, 'w')

    fh.write(bash())
    subprocess.run(['chmod', '+x', out_file])
    print('Done, see new script "{}."'.format(out_file))


# --------------------------------------------------
def bash():
    """bash template"""
    return r"""#!/bin/bash

set -u

ARG1=""

function USAGE() {
    printf "Usage:\n  %s -a ARG\n\n" "$(basename "$0")"

    echo "Required arguments:"
    echo " -a ARG"
    echo
    exit "${1:-0}"
}

[[ $# -eq 0 ]] && USAGE 1

while getopts :a:h OPT; do
    case $OPT in
        a)
            ARG="$OPTARG"
            ;;
        h)
            USAGE
            ;;
        :)
            echo "Error: Option -$OPTARG requires an argument."
            exit 1
            ;;
        \?)
            echo "Error: Invalid option: -${OPTARG:-""}"
            exit 1
    esac
done

echo "ARG \"$ARG\""

"""

# --------------------------------------------------
if __name__ == '__main__':
    main()
