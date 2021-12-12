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
        if bar == 'start':
            continue

        if bar.islower() and bar in foo:
            x = collections.Counter(foo)
            small_visits = [True for k, v in x.items() if k.islower() and v > 1]
            if len(small_visits):
                continue

        new_state = foo + [bar]
        if tuple(new_state) not in seen:
            todo.append(new_state)

print(len(completed))
