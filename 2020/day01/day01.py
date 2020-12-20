# Solution for day on of Advent Of Code 2020

import sys


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


def sum_until2(input_data, target_sum=2020):
    input_len = len(input_data)
    for i in range(input_len):
        first_nr = input_data[i]
        for j in range(i + 1, input_len):
            second_nr = input_data[j]
            if first_nr + second_nr == target_sum:
                return first_nr, second_nr

            elif first_nr + second_nr > target_sum:
                break

    raise Exception("Something is bad")


def sum_until3(input_data, target_sum=2020):
    input_len = len(input_data)
    for i in range(input_len):
        first_nr = input_data[i]
        for j in range(i + 1, input_len):
            second_nr = input_data[j]
            for k in range(j + 1, input_len):
                third_nr = input_data[k]
                if first_nr + second_nr + third_nr == target_sum:
                    return first_nr, second_nr, third_nr

                if first_nr + second_nr + third_nr > target_sum:
                    break

    raise Exception("Something is bad")


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, int)
    sorted_data = sorted(input_data)

    x2, y2 = sum_until2(sorted_data, target_sum=2020)
    print(x2 * y2)

    x3, y3, z3 = sum_until3(sorted_data, target_sum=2020)
    print(x3 * y3 * z3)
