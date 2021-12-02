class Sub:
    def _change_aim(self, d):
        self.aim += d

    def _change_all(self, d):
        self.x += d
        self.y += self.aim * d

    def __init__(self):
        self.x, self.y = 0, 0
        self.aim = 0
        self.command_map = {
                'forward': lambda x: self._change_all(x),
                'up': lambda x: self._change_aim(-x),
                'down': lambda x: self._change_aim(x)
            }

sub = Sub()
with open('input.txt') as input_file:
    for line in input_file:
        command, amount = line.split()
        amount = int(amount)

        sub.command_map[command](amount)

print("Answer #2: {}", sub.x * sub.y)