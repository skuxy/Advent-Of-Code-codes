#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Day three"""


class Wire:
    """In order to ease our coordinate transformations"""
    def __init__(self):
        self.step_functions = {
            'R': lambda dist: (self.coord[0] + dist, self.coord[1]),
            'D': lambda dist: (self.coord[0], self.coord[1] - dist),
            'L': lambda dist: (self.coord[0] - dist, self.coord[1]),
            'U': lambda dist: (self.coord[0], self.coord[1] + dist)
        }
        self.coord = (0, 0)
        self.passed = {}
        self.no_of_steps = 0

    def _append_x(self, x_coord, new_coord):
        if (x_coord, new_coord[1]) not in self.passed:
            self.passed[(x_coord, new_coord[1])] = self.no_of_steps

        self.no_of_steps += 1

    def _append_y(self, y_coord, new_coord):
        if (new_coord[0], y_coord) not in self.passed:
            self.passed[(new_coord[0], y_coord)] = self.no_of_steps

        self.no_of_steps += 1

    def step(self, step_data):
        """ Perform a step """
        direction = step_data[0]
        distance = int(step_data[1:])

        new_coord = self.step_functions[direction](distance)

        if self.coord[0] != new_coord[0]:
            if new_coord[0] < self.coord[0]:
                for x_coord in range(new_coord[0] + 1, self.coord[0]):
                    self._append_x(x_coord, new_coord)

            else:
                for x_coord in range(self.coord[0] + 1, new_coord[0]):
                    self._append_x(x_coord, new_coord)

        else:
            if new_coord[1] < self.coord[1]:
                for y_coord in range(new_coord[1] + 1, self.coord[1]):
                    self._append_y(y_coord, new_coord)

            else:
                for y_coord in range(self.coord[1] + 1, new_coord[1]):
                    self._append_y(y_coord, new_coord)

        self.coord = new_coord

    def intersect(self, wire2):
        """ Get intersections with another wire """
        first = set(self.passed.keys())
        second = wire2.passed.keys()
        return first.intersection(second)


def manhattan_distance(point):
    """ Get manhattan distance between points """
    return abs(point[0]) + abs(point[1])


if __name__ == "__main__":
    WB1 = Wire()
    WB2 = Wire()

    for step in ['R8', 'U5', 'L5', 'D3']:
        WB1.step(step)
    for step in ['U7', 'R6', 'D4', 'L4']:
        WB2.step(step)

    assert manhattan_distance(min(WB1.intersect(WB2))) == 6

    # First part
    with open('2019/input3.txt') as input_file:
        WB3 = Wire()
        WB4 = Wire()

        WIRES = input_file.readlines()
        for step in WIRES[0].split(','):
            WB3.step(step)

        for step in WIRES[1].split(','):
            WB4.step(step)

        print(min(map(manhattan_distance, WB3.intersect(WB4))))

    # Second part
    with open('2019/input3.txt') as input_file:
        WB3 = Wire()
        WB4 = Wire()

        WIRES = input_file.readlines()
        for step in WIRES[0].split(','):
            WB3.step(step)

        for step in WIRES[1].split(','):
            WB4.step(step)

    INTERSECTIONS = WB3.intersect(WB4)
    DISTANCES = map(lambda x: (WB3.passed[x], WB4.passed[x]), INTERSECTIONS)

    print(min(map(sum, DISTANCES)))
