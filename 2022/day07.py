import sys


current_directory = None
root = None

commands_map = {
    "ls": lambda x: None,
    "cd": lambda x: change_dir(x[2])
}


def change_dir(name):
    global current_directory
    global root


    if name == '..':
        current_directory = current_directory.parent
        return

    elif name == '/':
        if not current_directory:
            root = Directory(None, name)

        current_directory = root
        return

    current_directory = current_directory.content[name]


def process_line(line):
    parts = line.split(' ')
    if parts[0] == '$':
        commands_map[parts[1]](parts)

    else:
        if parts[0] == 'dir':
            current_directory.content[parts[1]] = Directory(current_directory, parts[1])

        else:
            current_directory.content[parts[1]] = File(parts[1], int(parts[0]))



class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.content = {}


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


with open(sys.argv[1]) as file_input:
    for line in file_input:
        line = line.strip()
        process_line(line)

dirs_under_100000 = []
dirs = []
min_space = 30000000
max_space = 70000000

def calculate_size(node):
    global dirs_under_100000
    global dirs
    size = 0
    for c in node.content:
        if isinstance(node.content[c], Directory):
            size += calculate_size(node.content[c])

        else:
            size += node.content[c].size

    if size < 100000:
        dirs_under_100000.append(size)

    dirs.append(size)

    return size


calculate_size(root)
print(sum(dirs_under_100000))
biggest = dirs[-1]
for d in sorted(dirs):
    if (biggest - d) < (max_space - min_space):
        print(d)
        break