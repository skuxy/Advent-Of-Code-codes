
import sys


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, lambda x: x.strip())[0].split(',')

    turn = 1
    # number: last_turn
    numbers = {}
    last_number = None

    for number in input_data:
        number = int(number)
        numbers[number] = turn
        last_number = number
        print(last_number)
        turn += 1

    while True:
        if turn == 11:
            break

        if last_number not in numbers:
            last_number = 0

        else:
            last_number = turn - numbers[last_number] - 1

        print(last_number)
        
        numbers[number] = turn
        turn += 1
