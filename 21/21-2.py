#!/usr/bin/env python3

import collections
import itertools
import sys

MOVES = collections.Counter([sum(x) for x in itertools.product(range(1, 4), repeat=3)])

def next_state(state, roll):
    new_pos = (state[0][state[2]] + roll - 1) % 10 + 1
    new_score = state[1][state[2]] + new_pos

    if state[2] == 0:
        return ((new_pos, state[0][1]), (new_score, state[1][1]), 1)
    else:
        return ((state[0][0], new_pos), (state[1][0], new_score), 0)

with open(sys.argv[1]) as f:
    positions = tuple([int(l.strip().split()[4]) for l in f.readlines()])

states = {(positions, (0, 0), 0): 1}

win_counts = [0, 0]
while states:
    new_states = collections.defaultdict(int)
    for old_state, old_count in states.items():
        evolved_states = {next_state(old_state, roll): count for roll, count in MOVES.items()}
        for evolved_state, evolved_count in evolved_states.items():
            new_count = old_count * evolved_count
            if evolved_state[1][1 - evolved_state[2]] >= 21:
                win_counts[1 - evolved_state[2]] += new_count
            else:
                new_states[evolved_state] += new_count

    states = new_states

print(max(win_counts))
