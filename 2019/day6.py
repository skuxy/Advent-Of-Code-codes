#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent_node = parent

        self.children_orbits = []

    def __str__(self):
        return str((self.name, self.parent_node, [child.name for child in self.children_orbits]))

    def get_children_orbits(self):
        all_children_orbits = []
        all_children_orbits += self.children_orbits

        for child in self.children_orbits:
            all_children_orbits += child.get_children_orbits()

        return all_children_orbits

    def get_parent_orbits(self):
        if self.parent_node:
            return self.parent_node.get_parent_orbits() + 1

        return 0


if __name__ == "__main__":
    COM = None
    nodes = {}
    with open("input6.txt") as f:
        for line in f:
            parent, child = line.strip().split(')')

            if parent not in nodes:
                nodes[parent] = Node(parent)
                if parent == 'COM':
                    COM = nodes[parent]

            if child not in nodes:
                nodes[child] = Node(child, nodes[parent])

            nodes[parent].children_orbits.append(nodes[child])

    total_orbits = 0
    for planet in nodes:
        total_orbits += nodes[planet].get_parent_orbits()

    print(total_orbits)

