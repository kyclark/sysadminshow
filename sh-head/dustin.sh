#!/bin/bash

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

