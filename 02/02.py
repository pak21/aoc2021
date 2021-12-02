#!/usr/bin/env python3

import sys

horizontal = 0
p1_depth = 0
p2_depth = 0

with open(sys.argv[1]) as f:
    for l in f:
        command, str_arg = l.split(' ')
        arg = int(str_arg)

        if command == 'forward':
            horizontal += arg
            p2_depth += p1_depth * arg
        elif command == 'down':
            p1_depth += arg
        elif command == 'up':
            p1_depth -= arg

print(horizontal * p1_depth)
print(horizontal * p2_depth)
