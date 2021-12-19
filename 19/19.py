#!/usr/bin/env python3

import collections
import itertools
import sys

import numpy as np

def do_transform(s, t):
    return (s * t[0])[:, t[1]]

def views(s):
    for x, y, z in itertools.product([-1, 1], repeat=3):
        for direction in itertools.permutations([0, 1, 2]):
            flips = np.array([x, y, z])
            parity2 = 1 if direction in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1
            if np.product(flips) != parity2:
                continue
            transform = (flips, direction)
            yield (do_transform(s, transform), transform)

def find_match(base, target):
    best_count = 0
    best_match = None
    for target_prime, rotation in views(target):
        offsets = collections.defaultdict(int)
        for a in base:
            for b in target_prime:
                offset = a - b
                key = tuple(offset)
                offsets[key] += 1
                if offsets[key] >= 12:
                    return rotation, offset

    return None, None
        
with open(sys.argv[1]) as f:
    scanners = [np.array([[int(x) for x in l.split(',')] for l in x.strip().split('\n')[1:]]) for x in f.read().split('\n\n')]

locations = {0: np.array([0, 0, 0])}
todo = set(range(1, len(scanners)))

while todo:
    for scanner in todo:
        transform, offset = find_match(scanners[0], scanners[scanner])
        if transform:
            beacons = do_transform(scanners[scanner], transform) + offset
            scanners[0] = np.unique(np.vstack((scanners[0], beacons)), axis=0)

            locations[scanner] = offset
            todo = todo - {scanner}

print(len(scanners[0]))
print(max([sum(np.abs(x - y)) for x in locations.values() for y in locations.values()]))
