import sys

#returns number depending on input parentheses, where '('
#increments, and ')' decrements number
def parse_parentheses(parentheses):
    result = 0
    for character in parentheses:
        if character == '(':
            result = result + 1
        elif character == ')':
            result = result - 1
    return result


#similar function, returns position of parenthese that first threw
#result below zero
def find_basement(parentheses):
    result = 0
    position = 0
    for character in parentheses:
        position = position + 1
        if character == '(':
            result = result + 1
        elif character == ')':
            if result == 0:
                break
            result = result - 1
    return position


def main():
    data = open(sys.argv[1]).read()
    print parse_parentheses(data)
    print find_basement(data)


if __name__ == '__main__':
    main()
