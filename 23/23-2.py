#!/usr/bin/env python3

import heapq
import sys

VALID_HALLWAY_X = set([1, 2, 4, 6, 8, 10, 11])
CREATURE_X = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
MOVE_COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def check_hallway(current_x, target_x, creature_positions):
    start, end = (current_x+1, target_x+1) if target_x > current_x else (target_x, current_x)
    for x in range(start, end):
        if (x, 1) in creature_positions:
            return False
    return True

def valid_moves(creature_type, current_location, creatures):
    map2 = {v: k for k, v in creatures}
    if current_location[1] == 1: # In hallway, must move into correct room
        if check_hallway(current_location[0], CREATURE_X[creature_type], map2.keys()):
            for y in range(5, 1, -1):
                creature = map2.get((CREATURE_X[creature_type], y))
                if creature:
                    if creature == creature_type:
                        # Side room is being filled with right type, look at next space
                        continue
                    else:
                        # Side room has wrong creature type in, cannot move in
                        break
                else:
                    yield (CREATURE_X[creature_type], y)
                    break
    else:
        good = True
        for y in range(2, current_location[1]):
            if (current_location[0], y) in map2.keys():
                good = False
                break
        if good:
            for x in VALID_HALLWAY_X:
                if check_hallway(current_location[0], x, map2.keys()):
                    yield (x, 1)

def move_cost(old, new, creature_type):
    return MOVE_COSTS[creature_type] * (abs(new[0] - old[0]) + abs(new[1] - old[1]))

with open(sys.argv[1]) as f:
    burrow = [list(l) for l in f.readlines()]

walls = set()
creatures = []
for y, row in enumerate(burrow):
    for x, c in enumerate(row):
        if c == '#':
            walls.add((x, y))
        elif c in ['A', 'B', 'C', 'D']:
            creatures.append((c, (x, y)))

creatures = sorted(creatures)

final_state = (
    ('A', (3, 2)),
    ('A', (3, 3)),
    ('A', (3, 4)),
    ('A', (3, 5)),
    ('B', (5, 2)),
    ('B', (5, 3)),
    ('B', (5, 4)),
    ('B', (5, 5)),
    ('C', (7, 2)),
    ('C', (7, 3)),
    ('C', (7, 4)),
    ('C', (7, 5)),
    ('D', (9, 2)),
    ('D', (9, 3)),
    ('D', (9, 4)),
    ('D', (9, 5))
)

creatures_t = tuple(sorted(creatures))
initial_state = (0, creatures_t)
todo = [initial_state]
seen = {creatures_t: 0}

best = None
while todo:
    energy, creatures = heapq.heappop(todo)

    if best and energy >= best:
        break

    if seen[creatures] < energy:
        continue

    for i, (creature_type, position) in enumerate(creatures):
        for new_position in valid_moves(creature_type, position, creatures):
            new_energy = energy + move_cost(position, new_position, creature_type)

            new_creatures = list(creatures)
            new_creatures[i] = (creature_type, new_position)
            new_creatures_t = tuple(sorted(new_creatures))

            if new_creatures_t == final_state:
                if not best or new_energy < best:
                    print(new_energy)
                    best = new_energy
                continue

            if best and new_energy > best:
                continue

            if new_creatures_t in seen and seen[new_creatures_t] <= new_energy:
                continue

            heapq.heappush(todo, (new_energy, new_creatures_t))
            seen[new_creatures_t] = new_energy

if False:
    while todo:
        print(heapq.heappop(todo))

print(len(seen))
