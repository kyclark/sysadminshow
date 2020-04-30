#!/bin/bash

# 
# Author : Ken Youens-Clark <kyclark@gmail.com>
# Purpose: bash implementation of `head`
# 

# Die on use of uninitialize variables
set -u

# Default value for the argument
NUM_LINES=10

# A function to print the "usage"
function USAGE() {
    printf "Usage:\n  %s -n NUM_LINES [FILE ...]\n\n" "$(basename "$0")"

    echo "Required arguments:"
    echo " -n NUM_LINES"
    echo
    exit "${1:-0}"
}

# Die if we have no arguments at all
[[ $# -eq 0 ]] && USAGE 1

# Process command line options
while getopts :n:h OPT; do
    case $OPT in
        n)
            NUM_LINES="$OPTARG"
            shift 2
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

# Verify that NUM_LINES looks like a positive integer
if [[ $NUM_LINES -lt 1 ]]; then
    echo "-n \"${NUM_LINES}\" must be > 0"
    exit 1
fi

# Process the positional arguments
for FILE in "$@"; do
    # Verify this argument is a readable file
    if [[ ! -f "$FILE" ]] || [[ ! -r "$FILE" ]]; then
        echo "\"${FILE}\" is not a readable file"
        continue
    fi

    # Print a header in case of mulitiple files
    echo "==> ${FILE} <=="

    # Initialize a counter variable
    i=0

    # Loop through each line of the file
    while read -r LINE; do
        echo $LINE

        # Increment the counter and see if it's time to break
        i=$((i+1))
        [[ $i -eq $NUM_LINES ]] && break
    done < "$FILE"
done
