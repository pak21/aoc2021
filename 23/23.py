#!/usr/bin/env python3

import heapq
import sys

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

VALID_HALLWAY_X = set([1, 2, 4, 6, 8, 10, 11])
CREATURE_X = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
MOVE_COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def check_hallway(current_x, target_x, creature_positions):
    start, end = (current_x+1, target_x+1) if target_x > current_x else (target_x, current_x)
    for x in range(start, end):
        if (x, 1) in creature_positions:
            return False
    return True

def valid_moves(creature_type, current_location, creature_positions):
    if current_location[1] == 1: # In hallway, must move into correct room
        if check_hallway(current_location[0], CREATURE_X[creature_type], creature_positions):
            if (CREATURE_X[creature_type], 2) not in creature_positions:
                yield (CREATURE_X[creature_type], 2)
                if (CREATURE_X[creature_type], 3) not in creature_positions:
                    yield (CREATURE_X[creature_type], 3)
    else:
        good = True
        for y in range(2, current_location[1]):
            if (current_location[0], y) in creature_positions:
                good = False
                break
        if good:
            for x in VALID_HALLWAY_X:
                if check_hallway(current_location[0], x, creature_positions):
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
    ('B', (5, 2)),
    ('B', (5, 3)),
    ('C', (7, 2)),
    ('C', (7, 3)),
    ('D', (9, 2)),
    ('D', (9, 3))
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

    creature_positions = {p for _, p in creatures}
    for i, (creature_type, position) in enumerate(creatures):
        for new_position in valid_moves(creature_type, position, creature_positions):
            new_energy = energy + move_cost(position, new_position, creature_type)

            new_creatures = list(creatures)
            new_creatures[i] = (creature_type, new_position)
            new_creatures_t = tuple(sorted(new_creatures))

            if new_creatures_t == final_state:
                if not best or new_energy < best:
                    print(new_energy)
                    best = new_energy
                continue

            if new_creatures_t in seen and seen[new_creatures_t] <= new_energy:
                continue

            heapq.heappush(todo, (new_energy, new_creatures_t))
            seen[new_creatures_t] = new_energy

if False:
    while todo:
        print(heapq.heappop(todo))
