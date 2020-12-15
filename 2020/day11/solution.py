import sys


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


def check_seats(input_data):
    y_max = len(input_data)
    x_max = len(input_data[0])

    for y in range(y_max):
        for x in range(x_max):
            if check_adjacent(input_data, x, y):
                yield (x,y)

def check_adjacent(input_data, x, y):
    mode = 0
    if input_data[y][x] == 'L':
        mode = 1

    elif input_data[y][x] == '#':
        mode = 2

    if mode == 0:
        return False

    if mode == 1:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                try:
                    if input_data[j][i] == '#':
                        return False
                except IndexError:
                    pass

        return True

    if mode == 2:
        cnt_occ = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                try:
                    if input_data[j][i] == '#':
                        cnt_occ += 1
                except IndexError:
                    pass

        if cnt_occ >= 4:
            return True
        return False
        

def toggle_seats(input_data, changed_seats):
    count_changed = 0
    for coordinates in changed_seats:
        x, y = coordinates
        if input_data[y][x] == '#':
            input_data[y][x] = 'L'

        else:
            input_data[y][x] = '#'

        count_changed += 1

    return input_data, count_changed


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, lambda x: list(x.strip()))

    while True:
        changed_seats = list(check_seats(input_data))
        input_data, toggled = toggle_seats(input_data, changed_seats)
        if not toggled:
            break

    occupied_seats = 0
    for row in input_data:
        occupied_seats += row.count('#')
        print(''.join(row))
    print(occupied_seats)