#!/usr/bin/env python3

import collections
import math
import sys

def parse_vent(text):
    a, _, b = text.split()
    x1, y1 = a.split(',')
    x2, y2 = b.split(',')
    return [int(v) for v in [x1, y1, x2, y2]]

def get_step(v1, v2):
    step = 0 if v1 == v2 else math.copysign(1, v2-v1)
    return (step, v2 + step) if step else (0, None)

with open(sys.argv[1]) as f:
    vents = [parse_vent(l) for l in f.readlines()]

data1 = collections.defaultdict(lambda: 0)
data2 = collections.defaultdict(lambda: 0)
for x1, y1, x2, y2 in vents:
    xstep, xend = get_step(x1, x2)
    ystep, yend = get_step(y1, y2)

    x = x1
    y = y1
    while True:
        if xstep == 0 or ystep == 0:
            data1[(x, y)] += 1
        data2[(x, y)] += 1
        x += xstep
        y += ystep
        if x == xend or y == yend:
            break

print(len([p for p in data1.values() if p > 1]))
print(len([p for p in data2.values() if p > 1]))
