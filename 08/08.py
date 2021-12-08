#!/usr/bin/env python3

import collections
import sys

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
    return {'a', 'b', 'c', 'd', 'e', 'f', 'g'} - set(x)

with open(sys.argv[1]) as f:
    notes = [[part.split(' ') for part in line.strip().split(' | ')] for line in f.readlines()]

segment_counts = collections.Counter([len(digit) for note in notes for digit in note[1]])

print(segment_counts[2] + segment_counts[3] + segment_counts[4] + segment_counts[7])

answer = 0

# Each segment count gives us a set of constraints from both the set segments and unset
# segments
#
# For example, if the segment count is 2 we know that:
# 1) the two segments must correspond to segments 'c' and 'f'
# 2) the five unset segments must correspond to segments 'a', 'b', 'd', 'e' and 'g'
#
# For the segment counts with multiple digits, the constraints are slightly less obvious
# but are effectively the union of all the digits with that segment count. For example,
# for a segment ocunt of 5:
# 1) we know nothing from the set segments, because all 7 segments are set in one of
#    {2, 3, 5}
# 2) the unset segments must be one of 'b', 'c', 'e' or 'f' because they are the only
#    segments which are unset in any of the digits {2, 3, 5}.
CONSTRAINTS = {
    2: [
        {'c', 'f'},
        {'a', 'b', 'd', 'e', 'g'}
    ],
    3: [
        {'a', 'c', 'f'},
        {'b', 'd', 'e', 'g'}
    ],
    4: [
        {'b', 'c', 'd', 'f'},
        {'a', 'e', 'g'}
    ],
    5: [
        {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        {'b', 'c', 'e', 'f'}
    ],
    6: [
        {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        {'d', 'c', 'e'}
    ],
    7: [
        {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        {}
    ],
}

for note in notes:
    possible = {chr(97 + i): {'a', 'b', 'c', 'd', 'e', 'f', 'g'} for i in range(7)}

    for digit in note[0]:
        positive_constraint, negative_constraint = CONSTRAINTS[len(digit)]
        for segment in digit:
            possible[segment] = possible[segment].intersection(positive_constraint)
        for segment in invert(digit):
            possible[segment] = possible[segment].intersection(negative_constraint)

    definite = {}

    # We've now have a (relatively) small set of possible mappings for each wire; use
    # a greedy algorithm to get the individual mappings
    while possible:
        can_process = [x for x in possible.items() if len(x[1]) == 1]
        if not can_process:
            raise Exception('No unique mapping found')

        input_segment, output_segments = can_process[0]
        definite[input_segment] = list(output_segments)[0]
        del possible[input_segment]
        for key in possible:
            possible[key] -= output_segments

    displayed = int(''.join([OUTPUTS[''.join(sorted([definite[key] for key in digit]))] for digit in note[1]]))
    answer += displayed

print(answer)
