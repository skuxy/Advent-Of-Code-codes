#! /usr/bin/env python3

import sys

init_banks = sys.argv[1:]

banks = list(map(int, init_banks))


step = 0
bank_length = len(banks)

seen_banks = {tuple(banks): step}
# Refactor to couple of functions plox
while True:
    step += 1
    max_value = max(banks)
    for index in range(bank_length):
        if banks[index] == max_value:
            break
    banks[index] = 0
    while max_value:
        index = (index + 1) % bank_length
        banks[index] += 1
        max_value -= 1

    if tuple(banks) in seen_banks:
        break

    seen_banks[tuple(banks)] = step

print(step)
print(step - seen_banks[tuple(banks)])
