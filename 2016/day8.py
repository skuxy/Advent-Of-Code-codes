#! /usr/bin/env python3


class grid():
    def __init__(self):
        self.pixels = [['-' for _ in range(50)] for _ in range(6)]  # "-" for off, "x" for on

    def rectangle(self, size_x, size_y):
        for y in range(size_y):
            for x in range(size_x):
                self.pixels[y][x] = 'x'

    def rotate_x(self, x_coord, offset):
        new_column = [None] * 6
        for y in range(6):
            new_column[(y + offset) % 6] = self.pixels[y][x_coord]
        for y in range(6):
            self.pixels[y][x_coord] = new_column[y]

    def rotate_y(self, y_coord, offset):
        new_row = [None] * 50
        for x in range(50):
            new_row[(x + offset) % 50] = self.pixels[y_coord][x]
        for x in range(50):
            self.pixels[y_coord][x] = new_row[x]


with open('/dev/stdin') as stdin:
    grid_instance = grid()
    for line in stdin.readlines():
        if "rect" in line:
            coord = line.split()[1]
            x, y = coord.split('x')
            x, y = int(x), int(y)

            grid_instance.rectangle(x, y)
        elif "row" in line:
            split_line = line.split()
            offset = int(split_line[-1])
            row = int(split_line[2].split('=')[-1])

            grid_instance.rotate_y(row, offset)

        else:
            split_line = line.split()
            offset = int(split_line[-1])
            column = int(split_line[2].split('=')[-1])

            grid_instance.rotate_x(column, offset)

    count_lit = 0
    for row in grid_instance.pixels:
        for column in row:
            if column == 'x':
                count_lit += 1

    print(count_lit)
