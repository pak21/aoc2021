#!/usr/bin/env python3

import collections
import sys

PART2 = True

class State:
    def __init__(self, path, visited, double_visit):
        self.path = path
        self.visited = visited
        self.double_visit = double_visit

def zero():
    return State([], set(), False)

def can_visit(state, next_cave):
    return \
        next_cave.isupper() or \
        next_cave not in state.visited or \
        (PART2 and not state.double_visit)

def visit(state, next_cave):
    return State(
        [next_cave] + state.path,
        state.visited | set([next_cave]),
        state.double_visit or (state.double_visit if next_cave.isupper() else (next_cave in state.visited))
    )

conns = collections.defaultdict(list)
with open(sys.argv[1]) as f:
    for a, b in [l.strip().split('-') for l in f.readlines()]:
        if b != 'start':
            conns[a].append(b)
        if a != 'start':
            conns[b].append(a)

seen = set()
todo = [visit(zero(), 'start')]
paths = 0

while todo:
    old_state = todo.pop()
    seen.add(old_state)

    for next_cave in conns[old_state.path[0]]:
        if next_cave == 'end':
            paths += 1
            continue

        if can_visit(old_state, next_cave):
            new_state = visit(old_state, next_cave)
            if new_state not in seen:
                todo.append(new_state)

print(paths)
