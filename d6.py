import re
import sys

#longer code on purpose

class Light:
    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):  #XOR function is screwing something?
        if self.on:
            self.on = False
        else:
            self.on = True


class Grid:
    def __init__(self):
        self.grid = [[Light() for x in range(1000)] for x in range(1000)]

    def no_turned_on(self):
        no = 0
        for line in self.grid:
            for x in line:
                if x.on:
                    no = no + 1
        return no


global grid
grid = Grid()  #yolo


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
    stream = open(sys.argv[1]).readlines()
    for line in stream:
        parse(line)
    print grid.no_turned_on()


if __name__ == '__main__':
    main()
