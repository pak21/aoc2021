#!/usr/bin/env python3

import functools
import sys

def get_bits(string, start, offset):
    first = start // 4
    last = (start + offset - 1) // 4

    start_bits = start % 4
    end_bits = start_bits + offset

    to_shift = 4 * (last - first + 1) - end_bits
    mask = (1 << offset) - 1

    return (int(string[first:last+1], 16) >> to_shift) & mask

def get_packet_value(string, start):
    version = get_bits(string, start, 3)
    typeid = get_bits(string, start + 3, 3)
    start += 6

    if typeid == 4:
        more = True
        value = 0
        while more:
            more = get_bits(string, start, 1)
            value = (value << 4) | get_bits(string, start + 1, 4)
            start += 5
    else:
        subvalues = []
        length_typeid = get_bits(string, start, 1)
        if length_typeid == 0:
            bits_to_parse = get_bits(string, start + 1, 15)
            start += 16
            end_offset = start + bits_to_parse
            while start < end_offset:
                start, ver, v = get_packet_value(string, start)
                version += ver
                subvalues.append(v)
        else:
            packets_to_parse = get_bits(string, start + 1, 11)
            start += 12
            for i in range(packets_to_parse):
                start, ver, v = get_packet_value(string, start)
                version += ver
                subvalues.append(v)

        if typeid == 0:
            value = sum(subvalues)
        elif typeid == 1:
            value = functools.reduce(lambda a, b: a * b, subvalues, 1)
        elif typeid == 2:
            value = min(subvalues)
        elif typeid == 3:
            value = max(subvalues)
        elif typeid == 5:
            value = 1 if subvalues[0] > subvalues[1] else 0
        elif typeid == 6:
            value = 1 if subvalues[0] < subvalues[1] else 0
        elif typeid == 7:
            value = 1 if subvalues[0] == subvalues[1] else 0

    return start, version, value

with open(sys.argv[1]) as f:
    for packet in [p.strip() for p in f.readlines()]:
        _, version, value = get_packet_value(packet, 0)
        print(packet, version, value)
