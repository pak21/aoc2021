#!/usr/bin/env python3

import collections
import itertools
import sys

MOVES = collections.Counter([sum(x) for x in itertools.product(range(1, 4), repeat=3)])

def next_state(state, roll):
    new_pos = (state[0][state[1]][0] + roll - 1) % 10 + 1
    new_score = state[0][state[1]][1] + new_pos

    if state[1] == 0:
        return (((new_pos, new_score), state[0][1]), 1)
    else:
        return ((state[0][0], (new_pos, new_score)), 0)

with open(sys.argv[1]) as f:
    positions = tuple([int(l.strip().split()[4]) for l in f.readlines()])

player_states = tuple([(p, 0) for p in positions])

states = {(player_states, 0): 1}

win_counts = [0, 0]
while states:
    new_states = collections.defaultdict(int)
    for old_state, old_count in states.items():
        evolved_states = {next_state(old_state, roll): count for roll, count in MOVES.items()}
        for evolved_state, evolved_count in evolved_states.items():
            new_count = old_count * evolved_count
            if evolved_state[0][1 - evolved_state[1]][1] >= 21:
                win_counts[1 - evolved_state[1]] += new_count
            else:
                new_states[evolved_state] += new_count

    states = new_states

print(max(win_counts))
