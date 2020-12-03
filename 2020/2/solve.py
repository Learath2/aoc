#!/usr/bin/python3

import sys
import re
from typing import Tuple

def is_valid_sled(policy: Tuple[Tuple[int, int], str], password: str) -> bool:
    (min, max, char) = policy
    t = password.count(char)

    return t >= min and t <= max

def is_valid_tobo(policy: Tuple[Tuple[int, int], str], password: str) -> bool:
    (pos1, pos2, char) = policy

    return (password[pos1 - 1] == char) != (password[pos2 - 1] == char)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    p = re.compile(r"^(\d*)-(\d*) ([a-z]): ([a-z]*)$")
    matches = [p.match(l) for l in lines]
    passwords = [((int(m.group(1)), int(m.group(2)), m.group(3)), m.group(4)) for m in matches]

    is_pw_valid = [is_valid_tobo(p[0], p[1]) for p in passwords]
    print([(x, is_pw_valid[i]) for i, x in enumerate(passwords)])
    print(sum(is_pw_valid))
    sys.exit(0)
