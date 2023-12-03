import re

number_map = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five ": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

number_regex = r"zero|one|two|three|four|five|six|seven|eight|nine"


def parse_line_1(line):
    first_c, second_c = None, None
    for c in line:
        if c.isdigit():
            first_c = c
            break

    for c in line[::-1]:
        if c.isdigit():
            second_c = c
            break

    return int(first_c + second_c)


def part1(input_data):
    result_sum = 0
    for line in input_data:
        result_sum += parse_line_1(line)

    return result_sum


def parse_line_2(line):
    result = 0
    matches = re.match(number_regex, line)

    first_result = matches.group(1)
    last_result = matches.group(-1)

    return result


def part2(input_data):
    result_sum = 0
    for line in input_data:
        result_sum += parse_line_2(line)

    return result_sum


if __name__ == "__main__":
    input_file = open("input.txt").read().splitlines()
    print("2023, day 1")
    print("===========")
    print("Part 1:", part1(input_file))
    print("Part 2:", part2(input_file))
