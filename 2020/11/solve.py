#!/usr/bin/python

import sys
import os
import time
from typing import List
from itertools import product
from copy import deepcopy

SeatMap = List[List[str]]
def print_map(seat_map: SeatMap):
    for r in seat_map:
        for s in r:
            print(s, end="")
        print("")

def get_seat_state(seat_map: SeatMap, i: int, j: int) -> str:
    if (0 <= i < len(seat_map)) and (0 <= j < len(seat_map[i])):
        return seat_map[i][j]

    return "oob"

def advance(seat_map: SeatMap) -> SeatMap:
    next_state = [['.' for c in r] for r in seat_map]
    for i, r in enumerate(seat_map):
        for j, s in enumerate(r):
            occ = 0
            for (v, k) in product([-1, 0, 1], repeat=2):
                if get_seat_state(seat_map, i + v, j + k) == "#":
                    occ += 1

            if s == "L" and occ == 0:
                next_state[i][j] = "#"
            elif s == "#" and occ >= 5: # +1 for the seat itself
                next_state[i][j] = "L"
            else:
                next_state[i][j] = s

    return next_state

def advance2(seat_map: SeatMap) -> SeatMap:
    next_state = [['.' for c in r] for r in seat_map]
    for i, r in enumerate(seat_map):
        for j, s in enumerate(r):
            occ = 0
            for (v, k) in product([-1, 0, 1], repeat=2):
                if v == k == 0:
                    continue

                mul = 1
                while (t := get_seat_state(seat_map, i + mul * v, j + mul * k)) != "oob":
                    if t == "#":
                        occ += 1
                        break
                    elif t == "L":
                        break
                    mul += 1

            if s == "L" and occ == 0:
                next_state[i][j] = "#"
            elif s == "#" and occ >= 5:
                next_state[i][j] = "L"
            else:
                next_state[i][j] = s

    return next_state

def count_occ(seat_map: SeatMap) -> int:
    occ = 0
    for r in seat_map:
        for s in r:
            if s == '#':
                occ += 1

    return occ

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    seat_map = [[c for c in l] for l in lines]

    p1 = deepcopy(seat_map)
    while True:
        t = advance(p1)
        if t == p1:
            print(count_occ(t))
            break

        p1 = t

    while True:
        t = advance2(seat_map)
        if t == seat_map:
            print(count_occ(t))
            break

        seat_map = t
