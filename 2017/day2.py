#! /usr/bin/env python3

checksum = 0
evenly_divisibles_sum = 0

for line in open('/dev/stdin').readlines():
    all_values = sorted(set([int(x) for x in line.split()]))

    print(all_values)
    for x, y in [(x, y) for x in all_values for y in all_values]:
        if x == y:
            continue
        if x % y == 0:
            evenly_divisibles_sum += x/y

    checksum += all_values[-1] - all_values[0]

print(checksum)
print(evenly_divisibles_sum)
