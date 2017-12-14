#! /usr/bin/env python3

from scipy.ndimage.measurements import label
import numpy as np
from day10 import knot_hash


class grid:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def get_hashes(self):
        for i in range(128):
            i = str(i)
            knot_hash_generator = knot_hash(self.puzzle_input + '-' + i)
            yield knot_hash_generator.calculate_knot_hash()

    def convert_to_binary(self):
        for knot_hash_string in self.get_hashes():
            yield "{0:0128b}".format(int(knot_hash_string, 16))

    def convert_to_grid(self):
        for bin_hash in self.convert_to_binary():
            yield bin_hash.replace("1", "#").replace("0", ".")


if __name__ == "__main__":
    grid_inst = grid("uugsqrei")

    print(sum([x.count('#') for x in grid_inst.convert_to_grid()]))

    grid_inst = grid("uugsqrei")
    print(label(np.fromiter(''.join(grid_inst.convert_to_binary()), dtype=int).reshape(128, 128))[1])
