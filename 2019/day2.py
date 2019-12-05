#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Second day of 2019 AoC
"""

OPCODE_MAP = {
    1: lambda a, b: a + b,
    2: lambda a, b: a * b
}


class ShipComputer:
    """
    Representing our ships computer
    For I'm lazy
    """
    def __init__(self, intcode):
        self.intcode = intcode
        self.position = 0

    def parse_sequence(self):
        """Parse opcode sequence"""
        operation = self.intcode[self.position]

        if operation == 99:
            return False

        first_operand = self.intcode[self.intcode[self.position + 1]]
        second_operand = self.intcode[self.intcode[self.position + 2]]
        result = self.intcode[self.position + 3]

        self.intcode[result] = \
            OPCODE_MAP[operation](first_operand, second_operand)

        return True

    def step(self):
        """Execute opcode"""
        if self.parse_sequence():
            self.position += 4
            return True

        return False

    def play(self):
        """Parse whole intcode"""
        while self.step():
            pass


if __name__ == "__main__":
    # Part one
    SC1 = ShipComputer([1, 0, 0, 0, 99])
    SC1.play()
    assert SC1.intcode == [2, 0, 0, 0, 99]
    SC2 = ShipComputer([2, 3, 0, 3, 99])
    SC2.play()
    assert SC2.intcode == [2, 3, 0, 6, 99]
    SC3 = ShipComputer([2, 4, 4, 5, 99, 0])
    SC3.play()
    assert SC3.intcode \
        == [2, 4, 4, 5, 99, 9801]
    SC4 = ShipComputer([1, 1, 1, 4, 99, 5, 6, 0, 99])
    SC4.play()
    assert SC4.intcode \
        == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    with open('2019/input2.txt') as input_file:
        SC = ShipComputer(
            list(map(int, input_file.read().split(',')))
        )

        SC.intcode[1] = 12
        SC.intcode[2] = 2

        SC.play()

        print(SC.intcode[0])

    # Part 2
    for x in range(100):
        for y in range(100):

            with open('2019/input2.txt') as input_file:
                SC = ShipComputer(
                    list(map(int, input_file.read().split(',')))
                )

                SC.intcode[1] = x
                SC.intcode[2] = y

                SC.play()

                if SC.intcode[0] == 19690720:
                    print(100 * x + y)
                    break
