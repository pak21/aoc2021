#!/usr/bin/env python3

import sys

import numpy as np

def g(a, y, x):
    return (a[y, x] if x >= 0 and x < a.shape[1] else 10) if y >= 0 and y < a.shape[0] else 10

def process(heights, done, y, x, current_height, todo):
    new_height = g(heights, y, x)
    if new_height >= 9 or new_height <= current_height:
        return

    if done[y, x] or (y, x) in todo:
        return

    todo.append((y, x))

with open(sys.argv[1]) as f:
    heights = np.array([[int(y) for y in x.strip()] for x in f.readlines()])

risk = 0
basin_sizes = []
done = np.full(heights.shape, False)

for (y, x), point in np.ndenumerate(heights):
    right = g(heights, y, x+1)
    up = g(heights, y-1, x)
    left = g(heights, y, x-1)
    down = g(heights, y+1, x)

    if point < up and point < down and point < left and point < right:
        risk += 1 + point

        basin_size = 0
        todo = [(y, x)]
        while todo:
            basin_size += 1
            y2, x2 = todo.pop()
            done[y2, x2] = True
            process(heights, done, y2, x2+1, point, todo)
            process(heights, done, y2-1, x2, point, todo)
            process(heights, done, y2, x2-1, point, todo)
            process(heights, done, y2+1, x2, point, todo)

        basin_sizes.append(basin_size)

print(risk)
print(np.product(sorted(basin_sizes)[-3:]))
