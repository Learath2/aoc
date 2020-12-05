#!/usr/bin/python3

import sys
from typing import Tuple

Seat = Tuple[int, int]

def get_seat(s: str) -> Seat:
    row = (0, 128)
    col = (0, 8)
    for c in s:
        if c == "F":
            row = (row[0], row[1] // 2)
        elif c == "B":
            row = (row[0] + row[1] // 2, row[1] // 2)
        elif c == "L":
            col = (col[0], col[1] // 2)
        elif c == "R":
            col = (col[0] + col[1] // 2, col[1] // 2)

    assert row[1] == 1 and col[1] == 1, "Error: {} {}".format(row, col)

    return (row[0], col[0])

def get_seat_id(s: Seat) -> int:
    return s[0] * 8 + s[1]

def dbg_seat_map(seats: List[Seat]):
    seat_map = [[False for j in range(8)] for i in range(128)]
    for s in seats:
        seat_map[s[0]][s[1]] = True

    for i, r in enumerate(seat_map):
        print(i, end=' ')
        for c in r:
            print("#" if c else ".", end='')
        print("")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    seats = [get_seat(l) for l in lines]
    seat_ids = [get_seat_id(s) for s in seats]
    print(max(seat_ids))

    seat_ids = sorted(seat_ids)
    for i in range(min(seat_ids), max(seat_ids)):
        if not i in seat_ids:
            print(i)
