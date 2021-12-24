#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    program = [l.strip().split() for l in f.readlines()]

min_digits = [None] * 14
max_digits = [None] * 14

stack = []
for digit in range(14):
    div_op = program[digit * 18 + 4]
    if div_op[2] == '1':
        add_op = program[digit * 18 + 15]
        stack.append((digit, int(add_op[2])))
    else:
        old_digit, difference = stack.pop()
        add_op = program[digit * 18 + 5]
        difference += int(add_op[2])

        if difference > 0:
            max_digits[digit] = 9
            max_digits[old_digit] = 9 - difference

            min_digits[digit] = 1 + difference
            min_digits[old_digit] = 1
        else:
            max_digits[digit] = 9 + difference
            max_digits[old_digit] = 9

            min_digits[digit] = 1
            min_digits[old_digit] = 1 - difference

        print(f'model[{digit}] = model[{old_digit}] + {difference}')

print()
print(''.join([str(x) for x in max_digits]))
print(''.join([str(x) for x in min_digits]))
