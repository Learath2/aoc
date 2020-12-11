#!/usr/bin/python3

import sys

from collections import deque
from itertools import combinations

if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[2].isnumeric():
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    l = int(sys.argv[2])
    if len(lines) < l:
        sys.exit(1)

    numbers = [int(l) for l in lines]
    d = deque(numbers[:l], l)

    i_elem = -1
    for n in numbers[l:]:
        valid = False
        for (a, b) in combinations(d, 2):
            if a + b == n:
                valid = True
                break
        if not valid:
            print("First invalid element =", n) # Part 1
            i_elem = n
            break

        d.append(n)

    m = [0 for i in range(len(numbers))]
    for i, n in enumerate(numbers[:-1]):
        m[i] = sum(numbers[i:i + 2])
        if m[i] == i_elem:
            print("Solution =", m[i]) # Part 2 trivial
            sys.exit(0)

    for r in range(3, len(numbers)):
        for i, n in enumerate(numbers):
            if i + r > len(numbers):
                break
            m[i] += numbers[i + r - 1]
            if m[i] == i_elem:
                print("Solution =", min(numbers[i:i+r]) + max(numbers[i:i+r])) # Part 2
                sys.exit(0)


