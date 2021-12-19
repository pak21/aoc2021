#!/usr/bin/env python3

import collections
import sys

import numpy as np

def views(s):
    for x in [1, -1]:
        for y in [1, -1]:
            for z in [1, -1]:
                for direction in [[0, 1, 2], [1, 2, 0], [2, 0, 1], [0, 2, 1], [2, 1, 0], [1, 0, 2]]:
                    v = np.array([x, y, z])
                    parity1 = np.product(v)
                    parity2 = 1 if direction in [[0, 1, 2], [1, 2, 0], [2, 0, 1]] else -1
                    if parity1 != parity2:
                        continue
                    out = (s * v)[:, direction]
                    yield out, (v, direction)

def find_match(scanners, i, j):
    best_count = 0
    best_match = None
    for s1prime, rotation in views(scanners[j]):
        offsets = collections.defaultdict(int)
        for a in scanners[i]:
            for b in s1prime:
                diff = a - b
                offsets[tuple(diff)] += 1

        for offset, count in offsets.items():
            if count > best_count:
                best_count = count
                best_match = (rotation, np.array(offset))

    print(j, best_count, best_match)
    return best_match if best_count >= 12 else None

with open(sys.argv[1]) as f:
    scanners = [np.array([[int(x) for x in l.split(',')] for l in x.strip().split('\n')[1:]]) for x in f.read().split('\n\n')]

locations = {0: np.array([0, 0, 0])}
todo = set(range(1, len(scanners)))

while todo:
    good = False
    print(todo)
    for scanner in todo:
        match = find_match(scanners, 0, scanner)
        if match:
            (v, direction), offset = match
            beacons = (scanners[scanner] * v)[:, direction] + offset

            merged = np.unique(np.vstack((scanners[0], beacons)), axis=0)

            scanners[0] = merged
            locations[scanner] = offset
            todo = todo - {scanner}

            good = True

    if not good:
        raise Exception('No progress made')

print(len(scanners[0]))

biggest = 0
for x in locations.values():
    for y in locations.values():
        dist = sum(np.abs(x - y))
        if dist > biggest:
            biggest = dist

print(biggest)
