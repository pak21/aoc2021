#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    chunks = f.readlines()

score = 0
incompletes = []

for chunk in chunks:
    state = []
    corrupt = False
    for c in chunk.strip():
        if c == '(' or c == '[' or c == '{' or c == '<':
            state.append(c)
        elif c == ')':
            if state[-1] == '(':
                state.pop()
            else:
                score += 3
                corrupt = True
                break
        elif c == ']':
            if state[-1] == '[':
                state.pop()
            else:
                score += 57
                corrupt = True
                break
        elif c == '}':
            if state[-1] == '{':
                state.pop()
            else:
                score += 1197
                corrupt = True
                break
        elif c == '>':
            if state[-1] == '<':
                state.pop()
            else:
                score += 25137
                corrupt = True
                break
        else:
            print('***', c, '***')
            raise Exception(chunk)

    if not corrupt:
        a = 0
        for c in state[::-1]:
            a *= 5
            if c == '(':
                a += 1
            elif c == '[':
                a += 2
            elif c == '{':
                a += 3
            elif c == '<':
                a += 4
            else:
                raise Exception('boom')
        incompletes.append(a)

print(score)
print(sorted(incompletes)[len(incompletes)//2])
