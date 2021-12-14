#!/usr/bin/env python3

import collections
import sys

with open(sys.argv[1]) as f:
    template, rules_s = f.read().split('\n\n')

rules = {
    tuple(pair): [(pair[0], to_add), (to_add, pair[1])]
    for pair, to_add
    in [
        line.split(' -> ')
        for line
        in rules_s.strip().split('\n')
    ]
}

pairs = collections.Counter(zip(template[:-1], template[1:]))

for i in range(int(sys.argv[2])):
    new_pairs = collections.defaultdict(int)
    for pair, count in pairs.items():
        for new_pair in rules[pair]:
            new_pairs[new_pair] += count

    pairs = new_pairs

counts = collections.defaultdict(int)
for pair, count in pairs.items():
    counts[pair[0]] += count
    counts[pair[1]] += count

# Note for future Phil: every character _except_ the first and last is a part of
# two pairs, so the above double counts everything except the first and last
# characters. Easiest just to make everything double-counted, so we increment
# the counts of the first and last characters by one.
counts[template[0]] += 1
counts[template[-1]] += 1

print((max(counts.values()) - min(counts.values())) // 2)
