#!/usr/bin/env python3

import collections
import sys

import numpy as np

with open(sys.argv[1]) as f:
    positions = np.array([int(x) for x in f.readline().strip().split(',')])

def part1(x, positions):
    return np.sum(np.abs(positions - x))

def part2(x, positions):
    diffs = np.abs(positions - x)
    return int(np.sum(diffs * (diffs + 1) / 2))

print(np.min([part1(x, positions) for x in range(max(positions))]))
print(np.min([part2(x, positions) for x in range(max(positions))]))
