#! /usr/bin/env python3


class node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.parent = None
        self.children = []

    def assign_parent(self, parent):
        self.parent = parent

    def assign_child(self, child):
        self.children.append(child)

    def sum_subvalues(self):
        if not self.children:
            return self.value

        sum_result = self.value
        for child in self.children:
            sum_result += child.sum_subvalues()

        return sum_result

    def locate_broken(self):
        if not self.children:
            return self.name, self.value, [x.sum_subvalues() for x in self.parent.children]

        if len(set([x.sum_subvalues() for x in self.children])) == 1:
            return self.name, self.value, set([x.sum_subvalues() for x in self.parent.children])

        child_values = {}
        for child in self.children:
            child_values[child.sum_subvalues()] = child

        return child_values[sorted(child_values.keys())[-1]].locate_broken()


def extract_root(node):
    while node.parent:
        node = node.parent

    return node


if __name__ == "__main__":
    with open('/dev/stdin') as stdin:
        input_data = list(map(lambda z: z.split(), stdin.readlines()))
        nodes = list(map(lambda elems: node(elems[0], int(elems[1][1:-1])), input_data))

        for line in input_data:
            if len(line) < 3:
                continue

            parent = list(filter(lambda node: node.name == line[0], nodes))[0]
            for potential_child in nodes:
                if potential_child.name in [x.strip(',') for x in line[3:]]:
                    potential_child.assign_parent(parent)
                    parent.assign_child(potential_child)

        root = extract_root(nodes[0])  # any ol node will do

        print(root.name)

        # part 2

        print(root.locate_broken())
