import sys

from itertools import permutations


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


def check_nr_validity(input_data, nr_index):
    sought_slice = input_data[nr_index - 25: nr_index]
    summed_perms = map(sum, permutations(sought_slice, 2))
    if input_data[nr_index] in summed_perms:
        return True

    return False


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, int)
    
    for i in range(25, len(input_data)):
        if not check_nr_validity(input_data, i):
            invalid_nr = input_data[i]
            # This is a semi-fair presumption
            invalid_idx = i
            print("It's ", input_data[i])
            break

    for perm in permutations(range(invalid_idx), 2):
        tested_slice = input_data[perm[0]:perm[1]]
        if sum(tested_slice) == invalid_nr:
            print(min(tested_slice) + max(tested_slice))
            break