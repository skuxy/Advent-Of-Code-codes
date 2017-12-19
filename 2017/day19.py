#! /usr/bin/env python3


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

DIRECTION_MAP = {
    'D': lambda x, y: (x, y + 1),
    'U': lambda x, y: (x, y - 1),
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y)
}

NEW_DIRECTION_MAP = {
    'D': ['R', 'L'],
    'U': ['R', 'L'],
    'R': ['U', 'D'],
    'L': ['U', 'D']
}


class path:
    def __init__(self, map_matrix):
        self.map_matrix = map_matrix
        self.direction = 'D'
        self.position = (self.map_matrix[0].index('|'), 0)
        self.letters = []
        self.steps = 0

    def move(self):
        x, y = self.position

        if self.map_matrix[y][x] == ' ':
            return False

        if self.map_matrix[y][x] in LETTERS:
            self.letters.append(map_matrix[y][x])

        if self.map_matrix[y][x] == "+":
            for new_direction in NEW_DIRECTION_MAP[self.direction]:
                new_x, new_y = DIRECTION_MAP[new_direction](x, y)

                if self.map_matrix[new_y][new_x] in LETTERS + "-|":
                    self.direction = new_direction

        x, y = DIRECTION_MAP[self.direction](x, y)
        self.position = (x, y)
        self.steps += 1
        return True


with open('input19.txt') as stdin:
    map_matrix = stdin.readlines()
    pth = path(map_matrix)

    while True:
        if not pth.move():
            break
    print(''.join(pth.letters))
    print(pth.steps)
