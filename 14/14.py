#!/usr/bin/env python3

import collections
import sys

with open(sys.argv[1]) as f:
    template, rules_s = f.read().split('\n\n')

rules_l = [x.split(' -> ') for x in rules_s.strip().split('\n')]
rules = {a: b for a, b in rules_l}

pairs = collections.Counter([t[0] + t[1] for t in zip(template[:-1], template[1:])])

for i in range(int(sys.argv[2])):
    new_pairs = collections.defaultdict(int)
    for p, v in pairs.items():
        if p in rules:
            new_pairs[p[0] + rules[p]] += v
            new_pairs[rules[p] + p[1]] += v
        else:
            new_pairs[p] += v

    pairs = new_pairs

counts = collections.defaultdict(int)
for p, v in pairs.items():
    counts[p[0]] += v
    counts[p[1]] += v

counts[template[0]] += 1
counts[template[-1]] += 1

print((max(counts.values()) - min(counts.values())) // 2)
