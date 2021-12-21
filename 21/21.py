#!/usr/bin/env python3

import collections
import functools
import itertools
import sys

import numpy as np

with open(sys.argv[1]) as f:
    positions = [int(l.strip().split()[4]) for l in f.readlines()]

scores = [0] * len(positions)

die = 1
player = 0
rolls = 0
while True:
    move = 0
    for i in range(3):
        move += die
        die += 1
        if die == 101:
            die = 1
    positions[player] += move
    positions[player] = ((positions[player] - 1) % 10) + 1
    scores[player] += positions[player]

    rolls += 3

    if scores[player] >= 1000:
        break

    player = (player + 1) % len(positions)

print(rolls * min(scores))
