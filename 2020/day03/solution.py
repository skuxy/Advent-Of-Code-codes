import sys


class Toboggan:
    def __init__(self, move):
        self.x = 0
        self.y = 0
        self.x_step, self.y_step = move

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

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

    max_y = len(input_data) - 1
    max_x = len(input_data[0])

    product = 1
    for step in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        trees_count = 0
        toboggan = Toboggan(step)

        while True:
            toboggan.move()
            if toboggan.y > max_y:
                break

            if input_data[toboggan.y][toboggan.x % max_x] == '#':
                trees_count += 1

        product *= trees_count
    
    print(product)