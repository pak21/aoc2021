#!/usr/bin/env python3

import collections
import sys

import numpy as np

OUTPUTS = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9',
}

def invert(x):
    return set(['a', 'b', 'c', 'd', 'e', 'f', 'g']) - set([y for y in x])

with open(sys.argv[1]) as f:
    notes = [[part.split(' ') for part in line.strip().split(' | ')] for line in f.readlines()]

segment_counts = collections.Counter([len(digit) for note in notes for digit in note[1]])

print(segment_counts[2] + segment_counts[3] + segment_counts[4] + segment_counts[7])

answer = 0

for note in notes:
    possible = {
        'a': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'b': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'c': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'd': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'e': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'f': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
        'g': set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    }

    for digit in note[0]:
        if len(digit) == 2:
            for segment in digit:
                possible[segment] = possible[segment].intersection(['c', 'f'])
            for segment in invert(digit):
                possible[segment] = possible[segment].intersection(['a', 'b', 'd', 'e', 'g'])
        elif len(digit) == 3:
            for segment in digit:
                possible[segment] = possible[segment].intersection(['a', 'c', 'f'])
            for segment in invert(digit):
                possible[segment] = possible[segment].intersection(['b', 'd', 'e', 'g'])
        elif len(digit) == 4:
            for segment in digit:
                possible[segment] = possible[segment].intersection(['b', 'c', 'd', 'f'])
            for segment in invert(digit):
                possible[segment] = possible[segment].intersection(['a', 'e', 'g'])
        elif len(digit) == 5:
            for segment in invert(digit):
                possible[segment] = possible[segment].intersection(['b', 'c', 'e', 'f'])
        elif len(digit) == 6:
            for segment in invert(digit):
                possible[segment] = possible[segment].intersection(['d', 'c', 'e'])

    definite = {}

    while True:
        can_process = [x for x in possible.items() if len(x[1]) == 1]
        if not can_process:
            raise Exception('No unique mapping found')

        input_segment, output_segments = can_process[0]
        definite[input_segment] = list(output_segments)[0]
        del possible[input_segment]
        for key in possible:
            possible[key] -= output_segments

        if len(definite) == 7:
            break

    displayed = int(''.join([OUTPUTS[''.join(sorted([definite[key] for key in digit]))] for digit in note[1]]))
    answer += displayed

print(answer)
