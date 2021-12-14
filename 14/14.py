#!/usr/bin/env python3

import collections
import sys

with open(sys.argv[1]) as f:
    template, rules_s = f.read().split('\n\n')

rules = {tuple(a): b for a, b in [x.split(' -> ') for x in rules_s.strip().split('\n')]}

pairs = collections.Counter(zip(template[:-1], template[1:]))

for i in range(int(sys.argv[2])):
    new_pairs = collections.defaultdict(int)
    for p, v in pairs.items():
        new_pairs[(p[0], rules[p])] += v
        new_pairs[(rules[p], p[1])] += v

    pairs = new_pairs

counts = collections.defaultdict(int)
for p, v in pairs.items():
    counts[p[0]] += v
    counts[p[1]] += v

# Note for future Phil: every character _except_ the first and last is a part of
# two pairs, so the above double counts everything except the first and last
# characters. Easiest just to make everything double-counted, so we increment
# the counts of the first and last characters by one.
counts[template[0]] += 1
counts[template[-1]] += 1

print((max(counts.values()) - min(counts.values())) // 2)
