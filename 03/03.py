#!/usr/bin/env python3

import sys

import numpy as np

def to_int(x):
    return sum([2**i for i, b in enumerate(reversed(x)) if b])

def part2(data, which):
    data2 = np.copy(data)
    for column in range(data2.shape[1]):
        most_common = 1 if sum(data2[:,column]) >= (data2.shape[0] / 2) else 0
        if which:
            most_common = 1 - most_common
        data2 = data2[data2[:,column] == most_common, :]
        if data2.shape[0] == 1:
            break
    return to_int(data2[0,:])

with open(sys.argv[1]) as f:
    data = np.array([[int(x) for x in l.strip()] for l in f.readlines()])

gamma = np.sum(data, 0) > (data.shape[0] / 2)
epsilon = ~gamma

print(to_int(gamma) * to_int(epsilon))

o2 = part2(data, False)
co2 = part2(data, True)

print(o2 * co2)
