#! /usr/bin/env python3

INPUT = 359
BUFFER_LEN = 2018


class spinlock:
    def __init__(self):
        self.buffer = [0]
        self.current_step = 0
        self.index = 0

    def step(self):
        self.current_step += 1

        self.index = (self.index + INPUT) % self.current_step
        self.index += 1

        self.buffer.insert(
            self.index,
            self.current_step
        )

        self.first_index = None

    def step_without_buffer(self):
        self.current_step += 1

        self.index = (self.index + INPUT) % self.current_step
        self.index += 1

        if self.index == 1:
            self.first_index = self.current_step


if __name__ == "__main__":
    sp = spinlock()

    #  First part
    #  while sp.current_step < BUFFER_LEN:
    #      sp.step()
    #
    # Second part
    while sp.current_step < 50000000:
        sp.step_without_buffer()

    print(sp.first_index)
