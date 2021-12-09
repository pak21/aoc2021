#!/usr/bin/env python3

import collections
import sys

import numpy as np

with open(sys.argv[1]) as f:
    heights = np.array([[int(y) for y in x.strip()] for x in f.readlines()])

def g(a, y, x):
    if y >= 0 and y < a.shape[0]:
        if x >= 0 and x < a.shape[1]:
            return a[y,x]
        else:
            return 10
    else:
        return 10

risk = 0

done = np.full(heights.shape, False)

def process(heights, done, y, x, current_height, todo):
    if y < 0 or y >= heights.shape[0] or x < 0 or x >= heights.shape[1]:
        return

    if done[y, x] or (y, x) in todo:
        return

    new_height = heights[y, x]
    if new_height == 9 or new_height <= current_height:
        return

    todo.append((y, x))
    return

basin_sizes = []

for y in range(heights.shape[0]):
    for x in range(heights.shape[1]):
        point = heights[y,x]

        up = g(heights, y-1, x)
        down = g(heights, y+1, x)
        left = g(heights, y, x-1)
        right = g(heights, y, x+1)

        if point < up and point < down and point < left and point < right:
            risk += 1 + point

            basin_size = 0
            todo = [(y, x)]
            while todo:
                basin_size += 1
                y2, x2 = todo[0]
                todo = todo[1:]
                done[y2, x2] = True
                process(heights, done, y2, x2+1, heights[y, x], todo)
                process(heights, done, y2-1, x2, heights[y, x], todo)
                process(heights, done, y2, x2-1, heights[y, x], todo)
                process(heights, done, y2+1, x2, heights[y, x], todo)

            basin_sizes.append(basin_size)

print(risk)
print(np.product(sorted(basin_sizes)[-3:]))
