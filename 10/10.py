#!/usr/bin/env python3

import sys

OPENS = {'(': 1, '[': 2, '{': 3, '<': 4}
CLOSES = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137)
}

with open(sys.argv[1]) as f:
    chunks = f.readlines()

score = 0
incompletes = []

for chunk in chunks:
    state = []
    corrupt = False
    for c in chunk.strip():
        if c in OPENS:
            state.append(c)
        elif state[-1] == CLOSES[c][0]:
            state.pop()
        else:
            score += CLOSES[c][1]
            corrupt = True
            break

    if not corrupt:
        incompletes.append(sum([5**i * OPENS[c] for i, c in enumerate(state)]))

print(score)
print(sorted(incompletes)[len(incompletes)//2])
