#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as f:
    bounds = re.split('[^-0-9]+', f.readline().strip())
    xmin, xmax, ymin, ymax = [int(s) for s in bounds[1:]]

def simulate(vx, vy, xmin, xmax, ymin, ymax):
    x = 0
    y = 0
    highest = y
    while x < xmax and y > ymin:
        x += vx
        y += vy
        vx = vx - 1 if vx > 0 else 0
        vy -= 1

        if y > highest:
            highest = y

        if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
            return True, highest

    return False, None

part1 = None
part2 = 0
for vx in range(0, xmax+1):
    for vy in range(ymin, 100): # TODO: how to set the upper limit here?
        in_area, highest = simulate(vx, vy, xmin, xmax, ymin, ymax)
        if in_area:
            part2 += 1
            if not part1 or highest > part1:
                part1 = highest

print(part1, part2)
