from typing import List

class LineState:
    increasing: bool
    line: List[int]
    state: int = 0

    def __init__(self, line):
        self.line = [int(x) for x in line.split()]
        self.line_len = len(self.line)

    def check_direction(self, first_two):
        self.increasing = first_two[0] < first_two[1]

    def check_distance(self) -> bool:
        if self.state + 1 < self.line_len:
            return 1 <= abs(self.line[self.state + 1] - self.line[self.state]) <= 3
        return False

    def step(self) -> bool:
        if self.state + 1 >= self.line_len:
            return False

        if self.increasing and self.line[self.state] > self.line[self.state + 1]:
            return False

        if not self.increasing and self.line[self.state] < self.line[self.state + 1]:
            return False

        if self.check_distance():
            self.state += 1
            return True

        return False

    def run(self) -> bool:
        self.check_direction(self.line[:2])
        while self.state < self.line_len - 1 and self.step():
            pass

        return self.state == self.line_len - 1

class LineStateDampened(LineState):
    # We can tolerate one bad level in final run
    dampened_levels: int = 0

    def step(self) -> bool:
        if self.state + 1 >= self.line_len:
            return False

        if self.increasing  and self.line[self.state] > self.line[self.state + 1]:
            if self.dampened_levels == 0:
                self.dampened_levels += 1

                del(self.line[self.state + 1])
                return self.step()

            return False

        if not self.increasing and self.line[self.state] < self.line[self.state + 1]:
            if self.dampened_levels == 0:
                self.dampened_levels += 1

                del (self.line[self.state + 1])
                return self.step()

            return False

        if self.check_distance():
            self.state += 1
            return True

        return False


if __name__ == '__main__':
    with open('input.txt') as f:
        sum_true = 0
        for line in f:
            line_state = LineState(line)
            if line_state.run():
                sum_true += 1

        print(sum_true)