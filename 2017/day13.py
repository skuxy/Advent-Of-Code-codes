#! /usr/bin/env python3


class firewall:
    def __init__(self, layers, delay):
        self.layers = layers
        self.starting_layers = layers
        self.layer_directions = ['+' for _ in range(len(self.layers))]
        self.packet_position = -1
        self.cost = 0
        self.delay = delay

    def walk_with_breaking(self):
        for _ in range(self.delay):
            self.step_scanners()
        while self.packet_position < len(self.layers) - 1:
            if self.step_with_break():
                return False
        return True

    def walk_the_firewall(self):
        self.cost = 0
        while self.packet_position < len(self.layers) - 1:
            self.step()
        return self.cost

    def step_with_break(self):
        self.packet_position += 1
        if self.layers[self.packet_position]:
            if self.layers[self.packet_position][0] == 'S':
                return True
        self.step_scanners()
        return False

    def step(self):
        self.packet_position += 1
        if self.layers[self.packet_position]:
            if self.layers[self.packet_position][0] == 'S':
                self.cost += len(self.layers[self.packet_position]) * self.packet_position
        self.step_scanners()

    def step_scanners(self):
        for i in range(len(self.layers)):
            if not self.layers[i]:
                continue

            if self.layer_directions[i] == '+':
                self.layer_directions[i] = self.move_scanner_down(i)
            else:
                self.layer_directions[i] = self.move_scanner_up(i)

    def move_scanner_down(self, layer_index):
        scanner_position = self.layers[layer_index].index('S')
        if scanner_position + 1 >= len(self.layers[layer_index]):
            self.layers[layer_index][scanner_position - 1] = 'S'
            self.layers[layer_index][scanner_position] = '-'
            return '-'
        self.layers[layer_index][scanner_position + 1] = 'S'
        self.layers[layer_index][scanner_position] = '-'
        return '+'

    def move_scanner_up(self, layer_index):
        scanner_position = self.layers[layer_index].index('S')
        if scanner_position - 1 < 0:
            self.layers[layer_index][scanner_position + 1] = 'S'
            self.layers[layer_index][scanner_position] = '-'
            return '+'
        self.layers[layer_index][scanner_position - 1] = 'S'
        self.layers[layer_index][scanner_position] = '-'
        return '-'


if __name__ == "__main__":
    layers = [None for _ in range(100)]
    with open('/dev/stdin') as stdin:
        for line in stdin.readlines():
            line = line.strip()

            layer_depth, layer_range = line.split(': ')
            layers[int(layer_depth)] = ['-' for _ in range(int(layer_range))]
            layers[int(layer_depth)][0] = 'S'

    delay = 0
    firewall_obj = firewall(layers[:], delay)
    firewall_obj.walk_the_firewall()
    print(firewall_obj.cost)

    delay = 12
    firewall_obj = firewall(layers[:], delay)
    print(firewall_obj.walk_with_breaking(), firewall_obj.delay)
