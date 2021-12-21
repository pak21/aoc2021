#!/usr/bin/env python3

import collections
import itertools
import sys

MOVES = collections.Counter([sum(x) for x in itertools.product(range(1, 4), repeat=3)])

def evolve(state):
    old_pos = state[0][state[2]]
    old_score = state[1][state[2]]
    new_states = {}
    for roll, count in MOVES.items():
        new_pos = (old_pos + roll - 1) % 10 + 1
        new_score = old_score + new_pos

        if state[2] == 0:
            new_state = ((new_pos, state[0][1]), (new_score, state[1][1]), 1)
        else:
            new_state = ((state[0][0], new_pos), (state[1][0], new_score), 0)

        new_states[new_state] = count

    return new_states

with open(sys.argv[1]) as f:
    positions = tuple([int(l.strip().split()[4]) for l in f.readlines()])

scores = tuple([0] * len(positions))

states = {(positions, scores, 0): 1}

win_counts = [0, 0]
while states:
    new_states = collections.defaultdict(int)
    for old_state, old_count in states.items():
        for evolved_state, evolved_count in evolve(old_state).items():
            new_states[evolved_state] += old_count * evolved_count

    states = new_states

    wins = [(state, count) for state, count in states.items() if state[1][1 - state[2]] >= 21]
    for state, count in wins:
        win_counts[1 - state[2]] += count
        del states[state]

print(max(win_counts))
