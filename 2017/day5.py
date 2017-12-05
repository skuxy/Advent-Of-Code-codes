#! /usr/bin/env python3


with open('/dev/stdin') as stdin:
    num_list = stdin.readlines()
    num_list = list(map(int, num_list))
    jumps_before_exit = 0
    current_index = 0
    while True:
        next_index = num_list[current_index] + current_index

        if num_list[current_index] >= 3:
            num_list[current_index] -= 1
        else:
            num_list[current_index] += 1

        current_index = next_index
        jumps_before_exit += 1

        if current_index < 0 or current_index >= len(num_list):
            break

    print(jumps_before_exit)
