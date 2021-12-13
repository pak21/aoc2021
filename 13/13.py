#!/usr/bin/env python3

import collections
import sys

import numpy as np

with open(sys.argv[1]) as f:
    text = f.read()
    dotlines, foldlines = text.split('\n\n')
    dots = [tuple([int(x) for x in l.split(',')]) for l in dotlines.split('\n')]
    folds = [l.split(' ')[-1].split('=') for l in foldlines.split('\n')[:-1]]

paper = {}
for d in dots:
    paper[d] = 1

for fold in folds:
    direction = fold[0]
    v = int(fold[1])

    if direction == 'y':
        for dot in list(paper.keys()):
            if dot[1] > v:
                paper[(dot[0], 2*v - dot[1])] = 1
                del paper[dot]
    elif direction == 'x':
        for dot in list(paper.keys()):
            if dot[0] > v:
                paper[(2*v - dot[0], dot[1])] = 1
                del paper[dot]

    print(len(paper))

maxx = max([d[0] for d in paper.keys()])
maxy = max([d[1] for d in paper.keys()])

folded = np.full((maxy+1, maxx+1), ' ')

for d in paper:
    folded[d[1], d[0]] = '$'

print()
print('\n'.join([''.join(l) for l in folded]))
