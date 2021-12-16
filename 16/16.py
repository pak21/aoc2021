#!/usr/bin/env python3

import functools
import sys

OPERATORS = [
    sum,
    lambda vs: functools.reduce(lambda a, b: a * b, vs, 1),
    min,
    max,
    None, # direct value handled elsewhere
    lambda vs: 1 if vs[0] > vs[1] else 0,
    lambda vs: 1 if vs[0] < vs[1] else 0,
    lambda vs: 1 if vs[0] == vs[1] else 0,
]

def foo(string, start, version_sum, values):
    start, version, value = get_packet_value(string, start)
    return (start, version_sum + version, values + [value])

def length_handler(string, start, loop_fn):
    version_sum = 0
    subvalues = []
    n = 0

    while loop_fn(start, n):
        start, version_sum, subvalues = foo(string, start, version_sum, subvalues)
        n += 1

    return start, version_sum, subvalues
    
LENGTH_HANDLERS = [
    (15, lambda string, start, length_value: length_handler(string, start, lambda s, _: s < start + length_value)),
    (11, lambda string, start, length_value: length_handler(string, start, lambda _, n: n < length_value)),
]

def get_bits(string, start, offset):
    first = start // 4
    last = (start + offset - 1) // 4

    start_bits = start % 4
    end_bits = start_bits + offset

    to_shift = 4 * (last - first + 1) - end_bits
    mask = (1 << offset) - 1

    return (start + offset, (int(string[first:last+1], 16) >> to_shift) & mask)

def get_packet_value(string, start):
    start, version = get_bits(string, start, 3)
    start, typeid = get_bits(string, start, 3)

    if typeid == 4:
        more = True
        value = 0
        while more:
            start, more = get_bits(string, start, 1)
            start, next_value = get_bits(string, start, 4)
            value = (value << 4) | next_value
    else:
        subvalues = []
        start, length_typeid = get_bits(string, start, 1)
        length_bits, length_fn = LENGTH_HANDLERS[length_typeid]
        start, length_value = get_bits(string, start, length_bits)

        start, version_sum, subvalues = length_fn(string, start, length_value)
        version += version_sum

        value = OPERATORS[typeid](subvalues)

    return start, version, value

with open(sys.argv[1]) as f:
    for packet in [p.strip() for p in f.readlines()]:
        _, version, value = get_packet_value(packet, 0)
        print(packet, version, value)
