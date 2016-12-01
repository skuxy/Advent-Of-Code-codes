import re
import sys

#longer code on purpose

class Light:
    def __init__(self):
        self.on = 0

    def turn_on(self):
        self.on = self.on + 1

    def turn_off(self):
        if self.on > 0:
            self.on = self.on - 1

    def toggle(self):  #XOR function is screwing something?
        if self.on:
            self.on = self.on + 2


class Grid:
    def __init__(self):
        self.grid = [[Light() for x in range(1001)] for x in range(1001)]

    def no_turned_on(self):
        no = 0
        for line in self.grid:
            for x in line:
                no = no + x.on
        return no


global grid  #yolo
grid = Grid()


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, ul, dr):
        self.ul = ul
        self.dr = dr

    def turn_on(self):
        for i in range(self.ul.x, self.dr.x + 1):
            for j in range(self.ul.y, self.dr.y + 1):
                grid.grid[i][j].turn_on()

    def turn_off(self):
        for i in range(self.ul.x, self.dr.x + 1):
            for j in range(self.ul.y, self.dr.y + 1):
                grid.grid[i][j].turn_off()

    def toggle(self):
        for i in range(self.ul.x, self.dr.x + 1):
            for j in range(self.ul.y, self.dr.y + 1):
                grid.grid[i][j].toggle()


def parse(line):
    if re.match(r'toggle.*', line):
        p1, p2 = re.match(r'toggle (.*) through (.*)', line).group(1, 2)
        p1 = [int(x) for x in p1.split(',')]
        p2 = [int(x) for x in p2.split(',')]
        rectangle = Rectangle(Coordinate(p1[0], p1[1]), Coordinate(p2[0], p2[1]))
        rectangle.toggle()
    if re.match(r'turn off.*', line):
        p1, p2 = re.match(r'turn off (.*) through (.*)', line).group(1, 2)
        p1 = [int(x) for x in p1.split(',')]
        p2 = [int(x) for x in p2.split(',')]
        rectangle = Rectangle(Coordinate(p1[0], p1[1]), Coordinate(p2[0], p2[1]))
        rectangle.turn_off()
    if re.match(r'turn on.*', line):
        p1, p2 = re.match(r'turn on (.*) through (.*)', line).group(1, 2)
        p1 = [int(x) for x in p1.split(',')]
        p2 = [int(x) for x in p2.split(',')]
        rectangle = Rectangle(Coordinate(p1[0], p1[1]), Coordinate(p2[0], p2[1]))
        rectangle.turn_on()


def main():
    for line in open(sys.argv[1]).readlines():
        parse(line)
    print grid.no_turned_on()


if __name__ == '__main__':
    main()
