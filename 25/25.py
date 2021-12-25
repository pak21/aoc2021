#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    sea = [l.strip() for l in f.readlines()]

right = set()
down = set()
for y, row in enumerate(sea):
    for x, c in enumerate(row):
        if c == '>':
            right.add((x, y))
        elif c == 'v':
            down.add((x, y))

maxy = len(sea)
maxx = len(sea[0])

def iterate(right, down, maxx, maxy):
    moved = False
    new_right = set()
    for x0, y0 in right:
        x1 = (x0 + 1) % maxx
        if (x1, y0) in right or (x1, y0) in down:
            new_right.add((x0, y0))
        else:
            moved = True
            new_right.add((x1, y0))

    new_down = set()
    for x0, y0 in down:
        y1 = (y0 + 1) % maxy
        if (x0, y1) in new_right or (x0, y1) in down:
            new_down.add((x0, y0))
        else:
            moved = True
            new_down.add((x0, y1))

    return new_right, new_down, moved

steps = 0
while True:
    steps += 1
    right, down, moved = iterate(right, down, maxx, maxy)
    if not moved:
        break

print(steps)
