import sys


class Boarding_pass:
    def __init__(self):
        self.min_row = 0
        self.max_row = 127
        self.min_column = 0
        self.max_column = 7
        self.actions = {
                'F': self.lower_half_rows,
                'B': self.upper_half_rows,
                'R': self.upper_half_columns,
                'L': self.lower_half_columns
                }

    def lower_half_rows(self):
        range_middle = int((self.min_row + self.max_row) / 2)
        self.max_row = range_middle

    def upper_half_rows(self):
        range_middle = int((self.min_row + self.max_row) / 2)
        self.min_row = range_middle + 1

    def lower_half_columns(self):
        range_middle = int((self.min_column + self.max_column) / 2)
        self.max_column = range_middle

    def upper_half_columns(self):
        range_middle = int((self.min_column + self.max_column) / 2)
        self.min_column = range_middle + 1

    def get_id(self):
        assert self.min_row == self.max_row
        assert self.min_column == self.max_column
        return self.min_row * 8 + self.min_column


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


def parse_input_data(input_data):
    max_id = 0
    all_ids = {}
    for line in input_data:
        boarding_pass = Boarding_pass()
        for char in line:
            boarding_pass.actions[char]()

        new_id = boarding_pass.get_id()
        all_ids[new_id] = 0

        if new_id > max_id:
            max_id = new_id

    your_place = None
    for x in range(max_id, 0, -1):
        if x not in all_ids:
            your_place = x
            break

    return max_id, your_place


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, lambda x: x.strip())
    print(parse_input_data(input_data))
