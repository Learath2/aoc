#!/usr/bin/python3

import sys
import operator
import functools
from itertools import combinations

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    ints = [int(x) for x in lines]
    for c in combinations(ints, int(sys.argv[2])):
        if sum(c) == 2020:
            print(functools.reduce(operator.mul, c, 1))
            sys.exit(0)

    sys.exit(1)
