#! /usr/bin/env python3


class program:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, new_position):
        self.position = new_position


class grid:
    def __init__(self):
        program_names = "a b c d e f g h i j k l m n o p".split()
        program_positions = [x for x in range(len(program_names))]

        program_args = zip(program_names, program_positions)

        self.programs = []
        for program_args in program_args:
            name, position = program_args
            self.programs.append(program(name, position))

    def update_positions(self):
        for x in range(len(self.programs)):
            self.programs[x].position = x

    def rotate(self, how_much):
        self.programs = self.programs[-how_much:] + self.programs[:-how_much]
        self.update_positions()

    def swap_places(self, A, B):
        first, second = self.programs[A:][0], self.programs[B:][0]
        self.programs[B] = first
        self.programs[A] = second
        self.update_positions()

    def swap_names(self, first_name, second_name):
        first = list(filter(lambda x: x.name == first_name, self.programs))[0]
        second = list(filter(lambda x: x.name == second_name, self.programs))[0]
        self.programs[second.position] = first
        self.programs[first.position] = second
        self.update_positions()


if __name__ == "__main__":
    with open('/dev/stdin') as stdin:
        in_data = stdin.read().strip().split(',')
        grid_inst = grid()
        existing = []
        for x in range(1000000000):
            for move in in_data:
                if move[0] == 's':
                    how_much = int(move[1:])
                    grid_inst.rotate(how_much)
                elif move[0] == 'x':
                    a, b = move[1:].split('/')
                    a, b = int(a), int(b)
                    grid_inst.swap_places(a, b)
                elif move[0] == 'p':
                    a, b = move[1:].split('/')
                    grid_inst.swap_names(a, b)

            if ''.join([x.name for x in grid_inst.programs]) in existing:
                break

            existing.append(''.join([x.name for x in grid_inst.programs]))
            print(x)

        for y in range(1000000000%x - 1):
            for move in in_data:
                if move[0] == 's':
                    how_much = int(move[1:])
                    grid_inst.rotate(how_much)
                elif move[0] == 'x':
                    a, b = move[1:].split('/')
                    a, b = int(a), int(b)
                    grid_inst.swap_places(a, b)
                elif move[0] == 'p':
                    a, b = move[1:].split('/')
                    grid_inst.swap_names(a, b)



    print(''.join([x.name for x in grid_inst.programs]))
