#!/usr/bin/python3

import sys
import re
from typing import List, Dict

def split_list(l: List, d) -> List:
    result = []
    t = []
    for i in l:
        if i != d:
            t += [i]
        else:
            result += [t]
            t = []

    return result

Passport = [str, str]
def is_valid(p: Passport) -> bool:
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    if not set(p.keys()).issuperset(required_fields):
        return False

    # Part 1
    # return True

    if p['byr'].isnumeric() and not 1920 <= int(p['byr']) <= 2002:
        return False

    if p['iyr'].isnumeric() and not 2010 <= int(p['iyr']) <= 2020:
        return False

    if p['eyr'].isnumeric() and not 2020 <= int(p['eyr']) <= 2030:
        return False

    if not (m := re.match(r"^(\d{2,3})(in|cm)$", p['hgt'])):
        return False

    hgt_u = m.group(2)
    hgt = int(m.group(1))
    if hgt_u == "in" and not 59 <= hgt <= 76:
        return False
    elif hgt_u == "cm" and not 150 <= hgt <= 193:
        return False

    if not re.match(r"^#[0-9a-f]{6}$", p['hcl']):
        return False

    if not p['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if not re.match(r"^\d{9}$", p['pid']):
        return False

    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    lines = [l.rstrip() for l in lines]

    passports = split_list(lines, "")
    passports = [" ".join(p).split(" ") for p in passports]
    passports = [{s[0]:s[1] for s in [t.split(":") for t in p]} for p in passports]

    print(len(list(filter(is_valid, passports))))
