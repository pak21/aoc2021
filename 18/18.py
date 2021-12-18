#!/usr/bin/env python3

import functools
import sys

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    @property
    def is_leaf(self):
        return isinstance(self.value, int)

    def __repr__(self):
        return str(self.value) if self.is_leaf else f'({self.left}, {self.right})'

def tree_from_list(l):
    return Node(tree_from_list(l[0]), tree_from_list(l[1]), None) if isinstance(l, list) else Node(None, None, l)

def send_value(n, v, recurse_left):
    if n.is_leaf:
        n.value += v
    else:
        child = n.left if recurse_left else n.right
        send_value(child, v, recurse_left)

def explode(x, parent, is_left, to_left, to_right, depth):
    if depth == 4:
        if to_left:
            send_value(to_left, x.left.value, False)
        if to_right:
            send_value(to_right, x.right.value, True)

        if is_left:
           parent.left = Node(None, None, 0)
        else:
           parent.right = Node(None, None, 0)

        return True

    if not x.left.is_leaf:
        done = explode(x.left, x, True, to_left, x.right, depth + 1)
        if done:
            return True

    if not x.right.is_leaf:
        done = explode(x.right, x, False, x.left, to_right, depth + 1)
        if done:
            return True

    return False

def split(x, parent, is_left):
    if x.is_leaf:
        if x.value >= 10:
            n = Node(Node(None, None, x.value // 2), Node(None, None, (x.value + 1) // 2), None)
            if is_left:
                parent.left = n
            else:
                parent.right = n
            return True
        return False

    split_left = split(x.left, x, True)
    if split_left:
        return True

    split_right = split(x.right, x, False)
    if split_right:
        return True

    return False

def add(a, b):
    c = Node(a, b, None)

    done = False
    while not done:
        can_explode = explode(c, None, None, None, None, 0)
        if not can_explode:
            can_split = split(c, None, None)
        done = not (can_explode or can_split)

    return c

def magnitude(a):
    return a.value if a.is_leaf else 3*magnitude(a.left) + 2*magnitude(a.right)

with open(sys.argv[1]) as f:
    lines = f.readlines()

numbers = [tree_from_list(eval(l.strip())) for l in lines]

result = functools.reduce(add, numbers)

print(magnitude(result))

result2 = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j:
            continue
        a = tree_from_list(eval(lines[i].strip()))
        b = tree_from_list(eval(lines[j].strip()))
        c = add(a, b)
        d = magnitude(c)
        if d > result2:
            result2 = d

print(result2)
