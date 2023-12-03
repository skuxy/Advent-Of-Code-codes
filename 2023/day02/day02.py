class Game:
    RedLimit = 12
    GreenLimit = 13
    BlueLimit = 14

    FewestRed = 12
    FewestGreen = 13
    FewestBlue = 14

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def add(self, color, amount):
        if color == "red":
            self.red += amount
        elif color == "green":
            self.green += amount
        elif color == "blue":
            self.blue += amount

    def is_over(self):
        return self.red > self.RedLimit or self.green > self.GreenLimit or self.blue > self.BlueLimit

    def is_fewest_red(self):
        return self.red < self.FewestRed

    def is_fewest_green(self):
        return self.green < self.FewestGreen

    def is_fewest_blue(self):
        return self.blue < self.FewestBlue


def part2(lines):
    power_sum = 0

    for line in lines:
        id_part, games = line.split(":")
        games_list = games.split(";")

        # Reset the fewest values
        Game.FewestRed = 0
        Game.FewestGreen = 0
        Game.FewestBlue = 0

        for draw in games_list:
            game = Game()
            colors = draw.split(",")

            for color in colors:
                amount, color_name = color.split()
                game.add(color_name, int(amount))

                if game.red > Game.FewestRed:
                    Game.FewestRed = game.red
                if game.green > Game.FewestGreen:
                    Game.FewestGreen = game.green
                if game.blue > Game.FewestBlue:
                    Game.FewestBlue = game.blue

        power_sum += Game.FewestRed * Game.FewestGreen * Game.FewestBlue

    return power_sum


def part1(lines):
    id_sum = 0
    for line in lines:

        id_part, games = line.split(":")

        games_list = games.split(";")
        over = False
        for draw in games_list:
            game = Game()
            colors = draw.split(",")
            for color in colors:
                amount, color_name = color.split()
                game.add(color_name, int(amount))

            if game.is_over():
                over = True
                break
        if not over:
            id_sum += int(id_part.split()[1])

    return id_sum


with open("input.txt") as f:
    lines = f.read().splitlines()

    # Part 1
    print(part1(lines))
    print(part2(lines))
