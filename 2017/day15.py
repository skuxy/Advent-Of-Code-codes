#! /usr/bin/env python3


class generator:
    def __init__(self, seed, factor, term):
        self.value = seed
        self.factor = factor
        self.term = term

        self.divider = 2147483647

    def next(self):
        self.value *= self.factor
        self.value %= self.divider

        return self.value

    def next_with_condition(self):
        while self.next() % self.term != 0:
            pass
        return self.value

    def to_bin(self):
        return bin(self.value)


def compare_generators(generatorA_value, generatorB_value):
    return (generatorA_value & 65535) == (generatorB_value & 65535)


if __name__ == "__main__":
    generatorA = generator(783, 16807, 4)
    generatorB = generator(325, 48271, 8)

    count = 0
    for _ in range(5000000):
        if compare_generators(generatorA.value, generatorB.value):
            count += 1
        generatorA.next_with_condition()
        generatorB.next_with_condition()

    print(count)
