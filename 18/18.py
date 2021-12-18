#!/usr/bin/env python3

import functools
import sys

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    @staticmethod
    def with_children(l, r):
        return Node(l, r, None)

    @staticmethod
    def with_value(v):
        return Node(None, None, v)

    @property
    def is_leaf(self):
        return isinstance(self.value, int)

    @property
    def magnitude(self):
        return self.value if self.is_leaf else 3 * self.left.magnitude + 2 * self.right.magnitude

    def set_lr(self, set_left, n):
        if set_left:
            self.left = n
        else:
            self.right = n

def tree_from_list(l):
    return Node.with_children(tree_from_list(l[0]), tree_from_list(l[1])) if isinstance(l, list) else Node.with_value(l)

def send_value(n, v, child_fn):
    if n:
        if n.is_leaf:
            n.value += v
        else:
            send_value(child_fn(n), v, child_fn)

def explode(x, parent, is_left, to_left, to_right, depth):
    if depth == 4:
        send_value(to_left, x.left.value, lambda n: n.right)
        send_value(to_right, x.right.value, lambda n: n.left)
        parent.set_lr(is_left, Node.with_value(0))
        return True

    if not x.left.is_leaf:
        done = explode(x.left, x, True, to_left, x.right, depth + 1)
        if done:
            return True

    return not x.right.is_leaf and explode(x.right, x, False, x.left, to_right, depth + 1)

def split(x, parent, is_left):
    if x.is_leaf:
        if x.value >= 10:
            n = Node.with_children(Node.with_value(x.value // 2), Node.with_value((x.value + 1) // 2))
            parent.set_lr(is_left, n)
            return True
        return False

    split_left = split(x.left, x, True)
    if split_left:
        return True

    return split(x.right, x, False)

def add(a, b):
    c = Node.with_children(a, b)

    done = False
    while not done:
        can_explode = explode(c, None, None, None, None, 0)
        if not can_explode:
            can_split = split(c, None, None)
        done = not (can_explode or can_split)

    return c

def magnitude(a):
    return a.value if a.is_leaf else 3 * magnitude(a.left) + 2 * magnitude(a.right)

with open(sys.argv[1]) as f:
    lists = [eval(l) for l in f.readlines()]

print(functools.reduce(add, [tree_from_list(l) for l in lists]).magnitude)

part2 = 0
for i, a in enumerate(lists):
    for j, b in enumerate(lists):
        if i == j:
            continue
        m = add(tree_from_list(a), tree_from_list(b)).magnitude
        if m > part2:
            part2 = m

print(part2)
