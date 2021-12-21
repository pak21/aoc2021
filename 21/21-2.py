#!/usr/bin/env python3

import collections
import itertools
import sys

NUM_DICE = 3
DICE_SIZE = 3
WINNING_SCORE = 21

PlayerState = collections.namedtuple('PlayerState', ['position', 'score'])
GameState = collections.namedtuple('GameState', ['playerstates', 'next'])

MOVES = collections.Counter([sum(dice) for dice in itertools.product(range(1, DICE_SIZE+1), repeat=NUM_DICE)])

def next_state(state, roll):
    ps = state.playerstates[state.next]
    new_pos = (ps.position + roll - 1) % 10 + 1
    new_score = ps.score + new_pos

    if state.next:
        return (state.playerstates[0], PlayerState(new_pos, new_score))
    else:
        return (PlayerState(new_pos, new_score), state.playerstates[1])

with open(sys.argv[1]) as f:
    player_states = tuple([PlayerState(int(l.strip().split()[-1]), 0) for l in f.readlines()])

states = {GameState(player_states, 0): 1}

win_counts = [0, 0]
while states:
    new_states = collections.defaultdict(int)
    for old_state, old_count in states.items():
        evolved_states = {next_state(old_state, roll): count for roll, count in MOVES.items()}
        for evolved_state, evolved_count in evolved_states.items():
            new_count = old_count * evolved_count
            if evolved_state[old_state.next].score >= WINNING_SCORE:
                win_counts[old_state.next] += new_count
            else:
                new_states[GameState(evolved_state, 1 - old_state.next)] += new_count

    states = new_states

print(max(win_counts))
