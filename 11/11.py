#!/usr/bin/env python3

import collections
import sys

import numpy as np

def process(levels, flashed, y, x):
    if y < 0 or y >= levels.shape[0] or x < 0 or x >= levels.shape[1] or flashed[y,x]:
        return

    levels[y,x] += 1
    if levels[y,x] > 9:
        flashed[y,x] = True
        levels[y,x] = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue
                process(levels, flashed, y+dy, x+dx)

with open(sys.argv[1]) as f:
    levels = np.array([[int(x) for x in l.strip()] for l in f.readlines()])

overall = 0

for n in range(int(sys.argv[2])):
    flashed = np.full(levels.shape, False)
    for (y, x), level in np.ndenumerate(levels):
        process(levels, flashed, y, x)
    count = np.sum(flashed)
    if count == levels.size:
        raise Exception(n+1)
    overall += count

print(overall)
