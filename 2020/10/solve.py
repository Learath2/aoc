#!/usr/bin/python3

import sys
from collections import defaultdict

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    joltages = sorted([0] + [int(l) for l in lines])
    joltages += [max(joltages) + 3]

    diffs = [0, 0, 0, 0]
    for (v, k) in zip(joltages, joltages[1:]):
        diffs[k - v] += 1

    print(diffs[1] * diffs[3]) # Part 1

    routes = defaultdict(int)
    routes[0] = 1
    for i in joltages[1:]:
        routes[i] = routes[i-1] + routes[i-2] + routes[i-3]

    print(routes[max(joltages)])
