import re

# Crap I need a global state and I am lazy to refactor the code
accepting = True

def filter_multiply_string(s: str) -> [(int, int)]:
    matches = re.findall(r'mul\((\d+),(\d+)\)', s)
    return [(int(match[0]), int(match[1])) for match in matches]


def multiply_results(factors_tuple: [(int, int)]) -> int:
    return sum([a * b for a, b in factors_tuple])


def filter_conditional_multiply_string(s: str) -> [(int, int)]:
    global accepting
    pattern = r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))'

    matches = re.findall(pattern, s)

    # State machine
    acceptable_pairs = []
    for match in matches:
        if match[0] == 'do()':
            accepting = True
        elif match[0] == "don't()":
            accepting = False
        elif accepting:
            acceptable_pairs.append((int(match[1]), int(match[2])))

    return acceptable_pairs


def accept_pair(acceptable_pairs, i, match):
    acceptable_pairs.append((int(match[1]), int(match[2])))
    last_mul = i
    return last_mul


if __name__ == '__main__':
    result = 0
    conditional_result = 0
    for line in open('input.txt'):
        factors = filter_multiply_string(line)
        line_result = multiply_results(factors)

        conditional_factors = filter_conditional_multiply_string(line)
        conditional_line_result = multiply_results(conditional_factors)

        result += line_result
        conditional_result += conditional_line_result

    print(result)
    print(conditional_result)
