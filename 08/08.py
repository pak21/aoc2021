#!/usr/bin/env python3

import collections
import sys

import numpy as np

OUTPUTS = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def invert(x):
    return set(['a', 'b', 'c', 'd', 'e', 'f', 'g']) - set([y for y in x])

with open(sys.argv[1]) as f:
    foo = [[y.split(' ') for y in x.strip().split(' | ')] for x in f.readlines()]

bar = collections.Counter([len(y) for x in foo for y in x[1]])

print(bar[2] + bar[3] + bar[4] + bar[7])

answer = 0

for x in foo:
    possible = {
        'a': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'b': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'c': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'd': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'e': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'f': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'g': set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    }

    for z in x[0]:
        if len(z) == 2:
            for a in z:
                possible[a] = possible[a].intersection(['c', 'f'])
            for a in invert(z):
                possible[a] = possible[a].intersection(['a', 'b', 'd', 'e', 'g'])
        elif len(z) == 3:
            for a in z:
                possible[a] = possible[a].intersection(['a', 'c', 'f'])
            for a in invert(z):
                possible[a] = possible[a].intersection(['b', 'd', 'e', 'g'])
        elif len(z) == 4:
            for a in z:
                possible[a] = possible[a].intersection(['b', 'c', 'd', 'f'])
            for a in invert(z):
                possible[a] = possible[a].intersection(['a', 'e', 'g'])
        elif len(z) == 5:
            for a in invert(z):
                possible[a] = possible[a].intersection(['b', 'c', 'e', 'f'])
        elif len(z) == 6:
            for a in invert(z):
                possible[a] = possible[a].intersection(['d', 'c', 'e'])

    definite = {}

    while True:
        can_process = [(a, b) for a, b in possible.items() if len(b) == 1]
        if not can_process:
            raise Exception('boom')

        a, b = can_process[0]
        definite[a] = list(b)[0]
        del possible[a]
        for c in possible:
            possible[c] -= b    

        if len(definite) == 7:
            break

    c = int(''.join([str(OUTPUTS[''.join(sorted([definite[a] for a in z]))]) for z in x[1]]))
    answer += c

print(answer)
