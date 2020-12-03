#!/usr/bin/python3

import sys
import operator
from typing import Tuple, List

def check(tmap: List[List[bool]], coords: Tuple[int, int]) -> bool:
    (x, y) = coords
    x %= len(tmap[0])

    return tmap[y][x]

def check_slope(tmap: List[List[bool]], slope: Tuple[int, int]) -> int:
    trees = 0
    cur = (0, 0)
    while cur[1] < len(tmap):
        if check(tmap, cur):
            trees += 1
        cur = tuple(map(operator.add, cur, slope))

    return trees

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    lines = [l.rstrip() for l in lines]
    tmap = [[c == '#' for c in s] for s in lines]

    result = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for s in slopes:
        result *= check_slope(tmap, s)

    print(result)
