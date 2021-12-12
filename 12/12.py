#!/usr/bin/env python3

import collections
import sys

import numpy as np

with open(sys.argv[1]) as f:
    connl = [l.strip().split('-') for l in f.readlines()]

conns = collections.defaultdict(list)
for a, b in connl:
    conns[a].append(b)
    conns[b].append(a)

seen = set()
todo = [['start']]
completed = []

while todo:
    foo = todo.pop()
    seen.add(tuple(foo))

    if foo[-1] == 'end':
        completed.append(foo)
        continue

    for bar in conns[foo[-1]]:
        if bar.islower() and bar in foo:
            continue

        new_state = foo + [bar]
        if tuple(new_state) not in seen:
            todo.append(new_state)

print(len(completed))
