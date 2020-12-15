import sys


bags = {}

class Bag:
    def __repr__(self):
        return " ".join([self.name, str([x[0].name for x in self.contains]), str([x.name for x in self.parents])]) + "\n"

    def __str__(self):
        return self.__repr__()

    def __init__(self, name, contains = [], parent = None):
        self.name = name
        self.contains = []
        self.parents = []
        if name not in bags:
            bags[name] = self

        if contains:
            for child_bag_name, quantity in contains:
                if child_bag_name in bags:
                    bags[child_bag_name].parents.append(self)

                else:
                    bags[child_bag_name] = Bag(child_bag_name, parent = [self])
                
                bags[name].contains.append((Bag(child_bag_name, parent=self), quantity))
        
        if parent:
            bags[name].parents.append(parent)

    def add_child(self, child_bag_name, quantity):
        bags[self.name].contains.append((Bag(child_bag_name, parent=self), quantity))


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


def parse_input_data(input_data):
    wanted_bag = Bag("shiny gold")
    for line in input_data:
        parent_bag_name, child_bags = line.split(" bags contain ")
        parent = Bag(parent_bag_name)

        if child_bags == "no other bags.":
            continue

        for parts in child_bags.split(", "):
            splitted_parts = parts.split()
            quantity = int(splitted_parts[0])
            child_name = " ".join([splitted_parts[1], splitted_parts[2]])
            parent.add_child(child_name, quantity)

    return get_parent_count(wanted_bag)
    

def get_parent_count(bag):
    cnt = 0
    if not bag.parents:
        return 1

    for parent in bag.parents:
        cnt += get_parent_count(parent)
    
    print(bag.name, bag.parents)
    return 1 + cnt


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, lambda x: x.strip())
    print(parse_input_data(input_data))