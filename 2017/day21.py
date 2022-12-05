import sys

start_pattern = """.#.
..#
###"""

class Pattern:
    def __init__(self, pattern):
        self.isOdd = len(pattern[0]) == 2
        self.initPattern = [x.split('/') for x in pattern[0]]
        self.resultPattern = [x.split('/') for x in pattern[1]]

    def rotate(pattern):
        result_pattern = pattern.copy()
        for i in range(len(result_pattern)):
            result_pattern[i].reverse()

        return result_pattern

    def flip(pattern):
        pass

        

pattern_book_even = []
pattern_book_odd = []
with open(sys.argv[1]) as input_file:
    pattern_book = [x.strip().split(" => ") for x in input_file.readlines()]
    pattern_book_even = [x for x in pattern_book if len(x[0]) == 5]
    pattern_book_odd = [x for x in pattern_book if len(x[0]) == 11]

print(pattern_book_even)
print(pattern_book_odd)