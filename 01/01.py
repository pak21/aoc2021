#!/usr/bin/env python3

import sys

old = None
count1 = 0

d0 = None
d1 = None
old2 = None
count2 = 0

with open(sys.argv[1]) as f:
    for line in f.readlines():

        depth = int(line)
        if old and depth > old:
            count1 += 1
        old = depth

        if not d0:
            d0 = depth
            continue

        if not d1:
            d1 = depth
            continue

        total = d0 + d1 + depth
        if old2 and total > old2:
            count2 += 1
        d0 = d1
        d1 = depth
        old2 = total

print(count1, count2)
