from math import floor


class Password:
    def __init__(self):
        self.value = 50
        self.password = 0
        self.password_part2 = 0

    def action(self, input_line):
        direction, amount = input_line[:1], int(input_line[1:])

        self.password_part2 += floor( amount / 100 )
        amount %= 100
        if direction == "L":
            self.value -= amount
        else:
            self.value += amount

        if self.value > 99:
            self.password_part2 += 1
            self.value = self.value - 100
        if self.value < 0:
            self.password_part2 += 1
            self.value = 100 + self.value

        # For part 1
        if self.value == 0:
            self.password += 1



if __name__ == "__main__":
    password = Password()
    with open("input.txt") as f:
        for line in f:
            password.action(line.strip())

    print(password.password, password.password_part2)