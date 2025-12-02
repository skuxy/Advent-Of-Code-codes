class Stringify:
    def __init__(self, string):
        self.string = string
        self.string_literal = len(string)
        self.string_memory = len(repr(string))


def main():
    result = 0
    with open("input.txt") as f:
        for line in f:


if __name__ == "__main__":
    print(Stringify("abc").string_literal)