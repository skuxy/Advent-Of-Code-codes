#! /usr/bin/env python3


def eliminate_comments(stream):
    index = 0
    stream = list(stream)
    while index < len(stream):
        if stream[index] == '!':
            stream.pop(index)
            stream.pop(index)
            index -= 1

        index += 1
    return ''.join(stream)


def eliminate_and_count_garbage(stream):
    index = 0
    garbage_count = 0
    while('<') in stream:  # assuming they are all canceled or removed
        if stream[index] == '<':
            next_closing = stream.find('>', index)
            garbage_count += len(eliminate_comments(stream[index:next_closing])) - 1   # -1 due to extra '' in every comm
            stream = stream[:index] + stream[next_closing + 1:]

        index += 1
    return stream, garbage_count


def check_and_count_groups(stream):
    stream = list(stream)
    stack = []
    count = 0
    depth = 0
    while stream:
        char = stream.pop(0)
        if char == '{':
            depth += 1
            stack.append(char)
            continue
        if char == '}':
            if stack:
                stack.pop()
                count += depth
                depth -= 1
    return count


if __name__ == '__main__':
    with open('/dev/stdin') as stdin:
        input_text = stdin.read()

        input_text = eliminate_comments(input_text)
        input_text, garbage_count = eliminate_and_count_garbage(input_text)

        print(check_and_count_groups(input_text), garbage_count)
