#!/usr/bin/env python3

import collections
import sys

import numpy as np

def parse_vent(text):
    a, _, b = text.split()
    x1, y1 = a.split(',')
    x2, y2 = b.split(',')
    return (int(x1), int(y1), int(x2), int(y2))

def get_step(v1, v2):
    return 1 if v2 > v1 else (-1 if v2 < v1 else 0)

with open(sys.argv[1]) as f:
    lines = f.readlines()

vents = [parse_vent(t) for t in lines]

data1 = collections.defaultdict(lambda: 0)
data2 = collections.defaultdict(lambda: 0)
for v in vents:
    x1, y1, x2, y2 = v
    xstep = get_step(x1, x2)
    ystep = get_step(y1, y2)
    xend = x2 + xstep if xstep else None
    yend = y2 + ystep if ystep else None

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
