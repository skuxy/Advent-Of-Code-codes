#! /usr/bin/env python3


class node:
    def __init__(self, name, connected_nodes):
        self.name = name.strip()
        self.connected_nodes = connected_nodes

    def add_nodes(self, nodes):
        self.connected_nodes += nodes


class path:
    def __init__(self, all_nodes, root_node):
        self.passed_nodes = []
        self.all_nodes = all_nodes
        self.current_node = root_node

    def walk_the_path(self):
        self.passed_nodes.append(self.current_node)
        for connected_node in self.current_node.connected_nodes:
            if connected_node not in self.passed_nodes:
                self.current_node = connected_node
                self.walk_the_path()

    def count(self):
        return len(self.passed_nodes)


if __name__ == "__main__":
    with open('/dev/stdin') as stdin:
        existing_nodes = []
        for line in stdin.readlines():
            line = line.strip()
            orig_node, connected_nodes = line.split('<->')
            orig_node = orig_node.strip()
            connected_nodes = connected_nodes.split(',')
            connected_nodes = [x.strip() for x in connected_nodes]

            if orig_node not in [x.name for x in existing_nodes]:
                new_node = node(orig_node, [])
                existing_nodes.append(new_node)
            else:
                new_node = list(filter(lambda x: x.name == orig_node, existing_nodes))[0]

            for connected_node in connected_nodes:
                if connected_node not in [x.name for x in existing_nodes]:
                    connected_node = node(connected_node, [])
                    existing_nodes.append(connected_node)
                else:
                    connected_node = list(filter(lambda x: x.name == connected_node, existing_nodes))[0]
                new_node.add_nodes([connected_node])

    paths = []
    for root_node in existing_nodes:
        if len(list(filter(lambda x: root_node in x.passed_nodes, paths))) > 0:
            continue
        path_inst = path(existing_nodes, root_node)
        path_inst.walk_the_path()
        paths.append(path_inst)

    print(len(paths))
