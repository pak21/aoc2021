#!/usr/bin/env python3

import collections
import sys

import numpy as np

with open(sys.argv[1]) as f:
    days = collections.Counter([int(x) for x in f.readline().split(',')])

n = int(sys.argv[2])

for i in range(n):
    x = {(a-1): b for a, b in days.items()}
    x[6] = x.get(6, 0) + x.get(-1, 0)
    x[8] = x.get(-1, 0)
    if -1 in x:
        del x[-1]
    days = x

print(sum(days.values()))
