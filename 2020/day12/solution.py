import sys

class Ferry:
    def _change_direction(self, coord, value):
        if coord == "x":
            self.x += value
        else:
            self.y += value

    def _rotate_right(self, amount):
        # self.bearing = (self.bearing + (amount / 90)) % 4

        repeat = amount / 90

        temp_wx = self.w_x
        temp_wy = self.w_y

        # translate waypoint
        temp_wx -= self.x
        temp_wy -= self.y

        for _ in range(repeat):
            _x = temp_wx
            _y = temp_wy

            if temp_wx >= 0 and temp_wy >= 0:
                temp_wx = _x
                temp_wy = - _y

            elif temp_wx >= 0 and temp_wy < 0:
                temp_wx = - _x
                temp_wy = _y

            elif temp_wx < 0 and temp_wy < 0:
                temp_wx = _x
                temp_wy = - _y

            elif temp_wx < 0 and temp_wy >= 0:
                temp_wx = - _x
                temp_wy = _y

        temp_wx += self.x
        temp_wy += self.y

        self.w_x = temp_wx
        self.w_y = temp_wy

    def _rotate_left(self, amount):
        # self.bearing = (self.bearing + (amount / 90)) % 4

        repeat = amount / 90

        temp_wx = self.w_x
        temp_wy = self.w_y

        # translate waypoint
        temp_wx -= self.x
        temp_wy -= self.y

        for _ in range(repeat):
            _x = temp_wx
            _y = temp_wy

            if temp_wx >= 0 and temp_wy >= 0:
                temp_wx = - _x
                temp_wy = _y

            elif temp_wx >= 0 and temp_wy < 0:
                temp_wx = _x
                temp_wy = - _y

            elif temp_wx < 0 and temp_wy < 0:
                temp_wx = - _x
                temp_wy = _y

            elif temp_wx < 0 and temp_wy >= 0:
                temp_wx = _x
                temp_wy = - _y

        temp_wx += self.x
        temp_wy += self.y

        self.w_x = temp_wx
        self.w_y = temp_wy

    def _forward(self, amount):
        # direction = self.bearing_map[self.bearing]
        # self.actions[direction](amount)
        self.x = self.w_x * amount
        self.y = self.w_y * amount
        self.w_x = self.w_x * amount
        self.w_y = self.w_y * amount

    def __init__(self):
        self.w_x = 10
        self.w_y = 1
        self.x = 0
        self.y = 0
        self.bearing = 0
        self.bearing_map = {
            0: 'E',
            1: 'S',
            2: 'W',
            3: 'N' 
        }
        self.actions = {
            'N': lambda k: self._change_direction('y', k),
            'S': lambda k: self._change_direction('y', -k),
            'E': lambda k: self._change_direction('x', k),
            'W': lambda k: self._change_direction('x', -k),
            'L': lambda k: self._rotate_left(k),
            'R': lambda k: self._rotate_right(k),
            'F': lambda k: self._forward(k)
        }

    def do(self, action, amount):
        self.actions[action](amount)


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()



if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, lambda x: x.strip())

    ferry = Ferry()

    for line in input_data:
        import pdb; pdb.set_trace()
        action = line[0]
        amount = int(line[1:])

        ferry.do(action, amount)

    print(abs(ferry.x) + abs(ferry.y))