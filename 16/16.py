#!/usr/bin/env python3

import collections
import sys

import numpy as np

def get_bits(string, start, offset):
    first = start // 4
    last = (start + offset - 1) // 4

    start_bits = start % 4
    end_bits = start_bits + offset

    to_shift = 4 * (last - first + 1) - end_bits
    mask = (1 << offset) - 1

    chars = string[first:last+1]
    value = (int(chars, 16) >> to_shift) & mask
    return value

def get_value(string, start, offset):
    more = get_bits(string, start, 1)
    v = get_bits(string, start + 1, offset - 1)
    return (more == 1, v)

def get_packet_value(string, start):
    version = get_bits(string, start, 3)
    typeid = get_bits(string, start + 3, 3)

    if typeid == 4:
        more = True
        start += 6
        value = 0
        while more:
            more, v = get_value(packet, start, 5)
            value = (value << 4) | v
            start += 5
    else:
        subvalues = []#
        length_typeid = get_bits(string, start + 6, 1)
        if length_typeid == 0:
            bits_to_parse = get_bits(string, start + 7, 15)
            start += 22
            end_offset = start + bits_to_parse
            while start < end_offset:
                start, ver, v = get_packet_value(string, start)
                version += ver
                subvalues.append(v)
        else:
            packets_to_parse = get_bits(string, start + 7, 11)
            start += 18
            for i in range(packets_to_parse):
                start, ver, v = get_packet_value(string, start)
                version += ver
                subvalues.append(v)

        if typeid == 0:
            value = sum(subvalues)
        elif typeid == 1:
            value = 1
            for x in subvalues:
                value *= x
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
        else:
            raise Exception(typeid)

    return start, version, value

with open(sys.argv[1]) as f:
    for packet in [p.strip() for p in f.readlines()]:
        _, version, value = get_packet_value(packet, 0)
        print(packet, version, value)
