#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = [l.strip().split(' ') for l in f]

horizontal = 0
depth = 0
aim = 0

for x in lines:
    a, b = x
    c = int(b)

    print(a, c)

    if a == 'forward':
        horizontal += c
        depth += aim * c
    elif a == 'down':
        aim += c
    elif a == 'up':
        aim -= c
        if depth < 0:
            raise Exception('boom')
    else:
        raise Exception('boom 2')

    print(horizontal, depth)

print(horizontal * depth)
