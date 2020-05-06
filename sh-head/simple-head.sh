#!/bin/bash

# 
# Author : Ken Youens-Clark <kyclark@gmail.com>
# Purpose: simple bash implementation of `head`
# 

# Check number of arguments is 1 or 2
if [[ $# -lt 1 ]] || [[ $# -gt 2 ]]; then
    echo "Usage: $(basename "$0") FILE [NUM]"
    exit 1
fi

FILE=$1
NUM=${2:-10}
LINE_NUM=0

while read -r LINE; do
    echo "$LINE"
    LINE_NUM=$((LINE_NUM+1))
    if [[ $LINE_NUM -eq $NUM ]]; then
        break
    fi
done < "$FILE"
