#!/usr/bin/env python3

import collections
import sys

import numpy as np

with open(sys.argv[1]) as f:
    algo_s, data_s = f.read().split('\n\n')

algo = [c == '#' for c in algo_s.strip()]
data_a = [[c == '#' for c in l] for l in data_s.strip().split('\n')]
data = {(x, y) for y, row in enumerate(data_a) for x, c in enumerate(row) if c}

for i in range(int(sys.argv[2])):
    keys = np.array(list(data))
    minx, miny = keys.min(axis=0)
    maxx, maxy = keys.max(axis=0)

    field_set = i % 2 if algo[0] else False

    new_data = set()
    for x in range(minx-1, maxx+2):
        for y in range(miny-1, maxy+2):
            v = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    v *= 2
                    newx, newy = x+dx, y+dy
                    if newx >= minx and newx <= maxx and newy >= miny and newy <= maxy:
                        if (newx, newy) in data:
                            v += 1
                    elif field_set:
                        v += 1

            if algo[v]:
                new_data.add((x, y))

    data = new_data

print(len(data))
