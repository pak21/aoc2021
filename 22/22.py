#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as f:
    commands = [l.strip().split() for l in f.readlines()]

cubes = []
count = 0
for action, coords in commands:
    values = [int(x) for x in re.split(r'[^-0-9]+', coords)[1:]]
    cube = tuple(values + [action == 'on'])

    corrections = []
    for c in cubes:
        overlap_x0 = max(cube[0], c[0])
        overlap_x1 = min(cube[1], c[1])
        overlap_y0 = max(cube[2], c[2])
        overlap_y1 = min(cube[3], c[3])
        overlap_z0 = max(cube[4], c[4])
        overlap_z1 = min(cube[5], c[5])

        if overlap_x1 >= overlap_x0 and overlap_y1 >= overlap_y0 and overlap_z1 >= overlap_z0:
            corrections.append((overlap_x0, overlap_x1, overlap_y0, overlap_y1, overlap_z0, overlap_z1, not c[6]))

    if cube[6]:
        cubes.append(cube)

    cubes = cubes + corrections

print(sum([(c[1]+1-c[0]) * (c[3]+1-c[2]) * (c[5]+1-c[4]) * (1 if c[6] else -1) for c in cubes]))
