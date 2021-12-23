#!/usr/bin/env python3

import heapq
import sys

CREATURE_TYPES = 4

def creature_x(creature_type):
    return 3 + 2 * creature_type

def check_hallway(current_x, target_x, creature_positions):
    start, end = (current_x+1, target_x+1) if target_x > current_x else (target_x, current_x)
    for x in range(start, end):
        if (x, 1) in creature_positions:
            return False
    return True

def valid_moves(creature_type, creature_map, creature_count, x0, y0):
    creature_positions = creature_map.keys() # Quicker than converting to a set
    cx = creature_x(creature_type)

    if x0 == cx: # Don't move out if we're in the right place (and so is everything below us)
        early_exit = True
        for y in range(y0+1, creature_count+2):
            creature = creature_map.get((cx, y))
            if creature != creature_type:
                early_exit = False
                break
        if early_exit:
            return

    if y0 == 1: # In hallway, must move into correct room
        # First check if we can move to our column
        if check_hallway(x0, cx, creature_positions):
            # Now find if we can move into our column
            for y in range(creature_count+1, 1, -1):
                creature = creature_map.get((cx, y))
                if creature == None:
                    # Space is empty, can move in
                    yield (cx, y)
                    break
                else:
                    if creature == creature_type:
                        # Side room is being filled with right type, look at next space
                        continue
                    else:
                        # Side room has wrong creature type in, cannot move in
                        break
    else: # In room, try to move into hallway
        # Can't move if there are any creatures between us and the hallway
        for y1 in range(2, y0):
            if (x0, y1) in creature_positions:
                return

        for x1 in [1, 2, 4, 6, 8, 10, 11]:
            if check_hallway(x0, x1, creature_positions):
                yield (x1, 1)

def move_cost(old, new, creature_type):
    return 10**creature_type * (abs(new[0] - old[0]) + abs(new[1] - old[1]))

with open(sys.argv[1]) as f:
    burrow = [list(l) for l in f.readlines()]

creatures = tuple(sorted([
    (ord(c) - 65, (x, y))
    for y, row in enumerate(burrow)
    for x, c in enumerate(row)
    if c >= 'A' and c <= 'D'
]))
creature_count = max([y for _, (_, y) in creatures]) - 1

final_state = tuple([(c, (creature_x(c), y)) for c in range(CREATURE_TYPES) for y in range(2, creature_count+2)])

todo = [(0, creatures)]
seen = {creatures: 0}

best = None
while todo:
    energy, creatures = heapq.heappop(todo)

    if best and energy >= best:
        break

    if seen[creatures] < energy:
        continue

    creature_map = {v: k for k, v in creatures}
    for i, (creature_type, position) in enumerate(creatures):
        for new_position in valid_moves(creature_type, creature_map, creature_count, *position):
            new_energy = energy + move_cost(position, new_position, creature_type)

            new_creatures = tuple(sorted((creatures[:i] + creatures[i+1:] + ((creature_type, new_position),))))

            if best and new_energy > best:
                continue

            if new_creatures in seen and seen[new_creatures] <= new_energy:
                continue

            if new_creatures == final_state:
                if not best or new_energy < best:
                    best = new_energy
                continue

            heapq.heappush(todo, (new_energy, new_creatures))
            seen[new_creatures] = new_energy

print(best)
