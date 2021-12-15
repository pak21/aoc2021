#!/usr/bin/env python3

import heapq
import sys

import numpy as np

DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

with open(sys.argv[1]) as f:
    small_cavern = np.array([[int(x) for x in l.strip()] for l in f.readlines()])

size_multiplier = int(sys.argv[2])

cavern = np.full((small_cavern.shape[0] * size_multiplier, small_cavern.shape[1] * size_multiplier), -1)

for dx in range(size_multiplier):
    for dy in range(size_multiplier):
        small_cavern_copy = (small_cavern - 1 + dx + dy) % 9 + 1
        cavern[
            dy * small_cavern.shape[0] : (dy+1) * small_cavern.shape[0],
            dx * small_cavern.shape[1] : (dx+1) * small_cavern.shape[1]
        ] = small_cavern_copy

todo = [(0, 0, 0)]
best = np.full(cavern.shape, 10 * cavern.size) # Guaranteed to be larger than any path
best[0, 0] = 0

while todo:
    risk, x, y = heapq.heappop(todo)

    for d in DIRS:
        newx = x + d[0]
        newy = y + d[1]
        if newx < 0 or newx >= cavern.shape[1] or newy < 0 or newy >= cavern.shape[0]:
            continue

        new_risk = risk + cavern[newy, newx]

        if new_risk < best[newy, newx]:
            best[newy, newx] = new_risk
            heapq.heappush(todo, (new_risk, newx, newy))

print(best[-1, -1])
