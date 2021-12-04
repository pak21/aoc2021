#!/usr/bin/env python3

import sys

import numpy as np

with open(sys.argv[1]) as f:
    numbers = [int(x) for x in f.readline().strip().split(',')]

    lines = f.readlines()
    numboards = len(lines) // 6

    boards = [np.array([[int(x) for x in l.strip().split()] for l in lines[6*i+1:6*i+6]]) for i in range(numboards)]

done = [False] * numboards

for n in numbers:
    for i, b in enumerate(boards):
        if not done[i]:
            matches = np.argwhere(b == n)
            for m in matches:
                b[tuple(m)] = -1

            matched = b == -1
            rows = np.sum(matched, 1) == 5
            columns = np.sum(matched, 0) == 5
            if np.any(rows) or np.any(columns):
                unmarked = np.sum(b[b != -1])
                print(n * unmarked)
                done[i] = True
