#! /usr/bin/env python3

MOVING_DICT = {
    'n': lambda x, y, z: (x, y + 1, z - 1),
    's': lambda x, y, z: (x, y - 1, z + 1),
    'ne': lambda x, y, z: (x + 1, y, z - 1),
    'sw': lambda x, y, z: (x - 1, y, z + 1),
    'nw': lambda x, y, z: (x - 1, y + 1, z),
    'se': lambda x, y, z: (x + 1, y - 1, z)
}


def get_distance_from_start(point):
    x, y, z = point
    distance = abs(x) + abs(y) + abs(z)
    distance /= 2
    return distance


if __name__ == "__main__":

    with open('/dev/stdin') as stdin:
        for line in stdin.readlines():
            current_point = (0, 0, 0)
            line = line.strip()
            directions = line.split(',')

            distances = []
            for direction in directions:
                x, y, z = current_point
                current_point = MOVING_DICT[direction](x, y, z)
                distances.append(get_distance_from_start(current_point))

            print(max(distances), get_distance_from_start(current_point))
