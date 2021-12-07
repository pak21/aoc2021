#!/usr/bin/env python3

import collections
import sys

with open(sys.argv[1]) as f:
    days = collections.Counter([int(x) for x in f.readline().split(',')])

n = int(sys.argv[2])

for i in range(n):
    days = {(a-1): b for a, b in days.items()}
    days[6] = days.get(6, 0) + days.get(-1, 0)
    days[8] = days.get(-1, 0)
    if -1 in days:
        del days[-1]

print(sum(days.values()))
