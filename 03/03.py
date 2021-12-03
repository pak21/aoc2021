#!/usr/bin/env python3

import sys

import numpy as np

def to_int(x):
    return sum([2**i for i, b in enumerate(reversed(x)) if b])

def part2(data, find_least):
    active = np.full(data.shape[0], True)
    still_active = data.shape[0]
    for column in range(data.shape[1]):
        most_common = sum(data[active,column]) >= (still_active / 2)
        if find_least:
            most_common = ~most_common
        filtered = data[:,column] == most_common
        active = active & filtered
        still_active = sum(active)
        if still_active == 1:
            break
    return to_int(data[active,:][0])

with open(sys.argv[1]) as f:
    data = np.array([[x == '1' for x in l.strip()] for l in f.readlines()])

gamma = np.sum(data, 0) > (data.shape[0] / 2)
epsilon = ~gamma

print(to_int(gamma) * to_int(epsilon))

o2 = part2(data, False)
co2 = part2(data, True)

print(o2 * co2)
