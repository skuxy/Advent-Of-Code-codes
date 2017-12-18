#! /usr/bin/env python3


class program:
    def __init__(self, instructions):
        letters = "abcdefghijklmnopqrstuvwxyz"
        self.registers = {}
        for letter in letters:
            self.registers[letter] = 0

        # self.last_sound = None
        self.instructions = instructions
        self.instruction_index = 0
        # self.rcv_occured = False
        self.instruction_map = {
            'set': self.set,
            'add': self.add,
            'mul': self.mul,
            'snd': self.snd,
            'rcv': self.rcv,
            'jgz': self.jgz,
            'mod': self.mod
        }
        self.queue = []
        self.waiting = False
        self.tied_program = None
        self.times_sent = 0

    def tie_program(self, program):
        self.tied_program = program

    def execute(self):
        instruction_line = self.instructions[self.instruction_index].split()
        instruction = instruction_line[0]
        self.instruction_map[instruction](*instruction_line[1:])
        self.instruction_index += 1

    def set(self, register, value):
        if value in self.registers:
            self.registers[register] = self.registers[value]
        else:
            self.registers[register] = int(value)

    def snd(self, register):
        self.queue.append(self.registers[register])
        self.times_sent += 1

    def add(self, register, value):
        if value in self.registers:
            self.registers[register] += self.registers[value]
        else:
            self.registers[register] += int(value)

    def mul(self, register, value):
        if value in self.registers:
            self.registers[register] *= self.registers[value]
        else:
            self.registers[register] *= int(value)

    def mod(self, register, value):
        if value in self.registers:
            self.registers[register] %= self.registers[value]
        else:
            self.registers[register] %= int(value)

    def rcv(self, register):
        if self.tied_program.queue:
            self.registers[register] = self.tied_program.queue.pop(0)
            self.waiting = False
        else:
            self.waiting = True
            self.instruction_index -= 1

    def jgz(self, register, offset):
        if register in self.registers:
            value = self.registers[register]
        else:
            value = int(register)

        if offset in self.registers:
            offset_value = self.registers[offset]
        else:
            offset_value = int(offset)

        if value > 0:
            self.instruction_index += offset_value - 1


if __name__ == "__main__":
    with open('input18.txt') as stdin:
        instructions = stdin.readlines()
        instructions = [x.strip() for x in instructions]
        program0 = program(instructions)
        program1 = program(instructions)
        program0.registers['p'] = 0
        program1.registers['p'] = 1
        program0.tie_program(program1)
        program1.tie_program(program0)

    while not program0.waiting or not program1.waiting:
        program0.execute()
        program1.execute()

    print(program1.times_sent)
