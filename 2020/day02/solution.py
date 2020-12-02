import sys


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


def parse_line(input_line):
    meta, password = input_line.split(':')
    password = password.strip()

    range, letter = meta.split()
    range_begin, range_end = range.split('-')

    return int(range_begin), int(range_end), letter, password


def validate_line1(input_line):
    range_begin, range_end, letter, password = input_line
    if password.count(letter) >= range_begin and password.count(letter) <= range_end:
        return True
    return False


def validate_line2(input_line):
    range_begin, range_end, letter, password = input_line
    print(input_line)
    return (password[range_begin - 1] == letter) ^ (password[range_end - 1] == letter)


def count_valid(input_data):
    valid_count1 = 0
    valid_count2 = 0
    for input_line in input_data:
        if validate_line1(input_line):
            valid_count1 += 1
        if validate_line2(input_line):
            valid_count2 += 1

    return valid_count1, valid_count2


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, parse_line)
    print(count_valid(input_data))