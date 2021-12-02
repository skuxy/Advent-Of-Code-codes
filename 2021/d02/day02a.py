class Sub:
    def _change_x(self, d):
        self.x += d

    def _change_y(self, d):
        self.y += d

    def __init__(self):
        self.x, self.y = 0, 0
        self.command_map = {
                'forward': lambda x: self._change_x(x),
                'up': lambda x: self._change_y(-x),
                'down': lambda x: self._change_y(x)
            }

sub = Sub()
with open('input.txt') as input_file:
    for line in input_file:
        command, amount = line.split()
        amount = int(amount)

        sub.command_map[command](amount)

print("Answer #1: {}", sub.x * sub.y)