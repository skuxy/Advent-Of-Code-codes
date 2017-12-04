#! /usr/bin/env python3

import sys


class node(object):
    def __init__(self, node_value, x_coord, y_coord):
        self.node_value = node_value
        self.x_coord = x_coord
        self.y_coord = y_coord


class grid(object):
    def __init__(self):
        self.nodes = [node(1, 0, 0)]  # first node.
        self.node_value = 1
        self.orientation = 'R'  # possibles are R L U D. Go figure
        self.next_orientation = {
            'R': 'U',
            'U': 'L',
            'L': 'D',
            'D': 'R'
        }
        self.current_coord = (0, 0)
        self.forward_steps_remaining = 1
        self.current_forward_step_limit = 1
        self.rotations = 0

    def move_turtle(self):
        """ rewritten for 2nd part """
        # self.value += 1
        x, y = self.current_coord
        if self.orientation == 'R':
            x += 1
        elif self.orientation == 'U':
            y += 1
        elif self.orientation == 'L':
            x -= 1
        elif self.orientation == 'D':
            y -= 1

        self.current_coord = (x, y)

        self.node_value = sum([node.node_value for node in self.filter_all_adjacent_to_current()])

        self.nodes.append(node(self.node_value, x, y))

        self.forward_steps_remaining -= 1

        if self.forward_steps_remaining > 0:
            return self.node_value

        self.orientation = self.next_orientation[self.orientation]
        self.rotations += 1

        if self.rotations % 2 == 0:
            self.current_forward_step_limit += 1

        self.forward_steps_remaining = self.current_forward_step_limit
        return self.node_value

    def is_adjacent_to_current(self, existing_x, existing_y):
        x, y = self.current_coord

        if abs(x - existing_x) <= 1 and abs(y - existing_y) <= 1:
            return True

        return False

    def filter_all_adjacent_to_current(self):
        all_adjacent = filter(lambda n: self.is_adjacent_to_current(n.x_coord, n.y_coord), self.nodes)

        return list(all_adjacent)

    def calculate_manhattan(self):
        x, y = map(abs, self.current_coord)
        return x + y


if __name__ == "__main__":
    max_node_value = int(sys.argv[1])

    grid_instance = grid()

    while grid_instance.node_value < max_node_value:
        grid_instance.move_turtle()

    # print(grid_instance.calculate_manhattan())
    print(grid_instance.node_value)
