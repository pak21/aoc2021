#!/usr/bin/env python3

import collections
import sys

PART2 = True

State = collections.namedtuple('State', ['path', 'visited', 'double_visit'])

def can_visit(state, next_cave):
    return not (next_cave in state.visited and state.double_visit)

def visit(state, next_cave):
    return State(
        [next_cave] + state.path,
        state.visited if next_cave.isupper() else state.visited | set([next_cave]),
        state.double_visit or next_cave in state.visited
    )

conns = collections.defaultdict(list)
with open(sys.argv[1]) as f:
    for a, b in [l.strip().split('-') for l in f.readlines()]:
        if a != 'end' and b != 'start':
            conns[a].append(b)
        if b != 'end' and a != 'start':
            conns[b].append(a)

todo = [State(['start'], set(), not PART2)]
paths = 0

while todo:
    old_state = todo.pop()

    for next_cave in conns[old_state.path[0]]:
        if next_cave == 'end':
            paths += 1
        elif can_visit(old_state, next_cave):
            new_state = visit(old_state, next_cave)
            todo.append(new_state)

print(paths)
