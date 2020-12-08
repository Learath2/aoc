#!/usr/bin/python3

import sys
import re
from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class State:
    acc: int = 0
    pc: int = 0
    err: bool = False
    halt: bool = False

Instruction = Tuple[str, int]
def decode(s: str) -> Instruction:
    m = re.match(r"^([a-z]+) ([+-]\d+)$", s)
    if not m:
        raise RuntimeError("Match fail")

    return (m.group(1), int(m.group(2)))

def execute(inst: Instruction, state: State):
    if inst[0] == "acc":
        state.acc += inst[1]
    elif inst[0] == "jmp":
        state.pc += inst[1]
        return
    elif inst[0] == "nop":
        pass
    else:
        state.halt = True
        state.err = True

    state.pc += 1

Program = List[Instruction]
def run(program: Program) -> State:
    state = State()
    visited = []
    while not state.halt and state.pc < len(program):
        inst = program[state.pc]
        if state.pc in visited:
            state.err = True
            break
        else:
            visited += [state.pc]
        execute(inst, state)

    return state

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    program = [decode(l) for l in lines]
    s = run(program)
    print(s)

    found = False

    nops = [n for n, i in enumerate(program) if i[0] == "nop"]
    jmps = [n for n, i in enumerate(program) if i[0] == "jmp"]

    for n in nops:
        patched = program.copy()
        patched[n] = ("jmp", program[n][1])
        s = run(patched)
        if not s.err and s.pc == len(program):
            print("Found fix", s)
            found = True
            break

    if not found:
        for n in jmps:
            patched = program.copy()
            patched[n] = ("nop", program[n][1])
            s = run(patched)
            if not s.err and s.pc == len(program):
                print("Found fix", s)
                break

