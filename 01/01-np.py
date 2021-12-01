#!/usr/bin/env python3

import sys

import numpy as np

with open(sys.argv[1]) as f:
    readings = np.array([int(x) for x in f.readlines()])

part1 = np.sum((readings[1:] - readings[:-1]) > 0)
print(part1)

cumsum = np.insert(np.cumsum(readings), 0, 0)
partials = cumsum[3:] - cumsum[:-3]
part2 = np.sum((partials[1:] - partials[:-1]) > 0)
print(part2)
