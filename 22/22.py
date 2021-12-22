#!/usr/bin/env python3

import re
import sys

def volume(c):
    v = (c[1]+1-c[0]) * (c[3]+1-c[2]) * (c[5]+1-c[4])
    if c[6] == 'off':
        v *= -1
    return v

with open(sys.argv[1]) as f:
    commands = [l.strip().split() for l in f.readlines()]

cubes = []
count = 0
for action, coords in commands:
    foo = [re.split(r'[=.]+', x) for x in coords.split(',')]
    x0 = int(foo[0][1])
    x1 = int(foo[0][2])
    y0 = int(foo[1][1])
    y1 = int(foo[1][2])
    z0 = int(foo[2][1])
    z1 = int(foo[2][2])

    cube = (x0, x1, y0, y1, z0, z1, action)

    to_append = []
    for c in cubes:
        overlap_x0 = max(x0, c[0])
        overlap_x1 = min(x1, c[1])
        overlap_y0 = max(y0, c[2])
        overlap_y1 = min(y1, c[3])
        overlap_z0 = max(z0, c[4])
        overlap_z1 = min(z1, c[5])

        if overlap_x1 >= overlap_x0 and overlap_y1 >= overlap_y0 and overlap_z1 >= overlap_z0:
            correction_type = None
            if action == 'on':
                if c[6] == 'on':
                    correction_type = 'off'
                else:
                    correction_type = 'on'
            elif action == 'off':
                if c[6] == 'on':
                    correction_type = 'off'
                else:
                    correction_type = 'on'

            if correction_type:
                to_append.append((overlap_x0, overlap_x1, overlap_y0, overlap_y1, overlap_z0, overlap_z1, correction_type))

    if cube[6] == 'on':
        cubes.append(cube)

    cubes = cubes + to_append

print(sum([volume(c) for c in cubes]))
