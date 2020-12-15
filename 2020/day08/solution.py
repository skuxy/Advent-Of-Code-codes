import sys


class Gameboy:
    def _acc(self, val):
        self.accumulator += val
        self.instruction += 1

    def _jmp(self, val):
        self.instruction += val

    def _nop(self, val=None):
        self.instruction += 1

    def __init__(self):
        self.instruction = 0
        self.accumulator = 0
        self.history = {}
        self.operations = {
            'acc': self._acc,
            'jmp': self._jmp,
            'nop': self._nop
        }

    def step(self, cmd, arg):
        if self.instruction in self.history:
            return self.accumulator

        self.history[self.instruction] = None
        self.operations[cmd](arg)
        return 0


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()

def swap_cmd(input_data, line_nr):
    cmd, value = input_data[line_nr].split()
    new_cmd = None

    if cmd == 'jmp':
        new_cmd = 'nop'
    elif cmd == 'nop':
        new_cmd = 'jmp'

    new_line = "%s %s" % (new_cmd, value)
    input_data[line_nr] = new_line


def find_next_line(input_data, line_nr):
    while True:
        line_nr += 1
        cmd, _ = input_data[line_nr].split()

        if cmd in ('jmp, nop'):
            swap_cmd(input_data, line_nr)
            return line_nr
    

if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, lambda x: x.strip())
    gameboy = Gameboy()
    changed_cmd_line = -1

    while True:
        if gameboy.instruction >= len(input_data):
            print("Sucessfull! Breaking with ", gameboy.accumulator)
            break
        cmd, value = input_data[gameboy.instruction].split()
        ret = gameboy.step(cmd, int(value))
        if ret:
            gameboy = Gameboy()
            if changed_cmd_line >= 0:
                swap_cmd(input_data, changed_cmd_line)

            changed_cmd_line = find_next_line(input_data, changed_cmd_line)