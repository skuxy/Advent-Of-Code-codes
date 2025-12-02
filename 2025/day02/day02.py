from re import match
from typing import Any, Generator


def process_ranges(range_tuple):
    result = 0
    for i in range(range_tuple[0], range_tuple[1] + 1):
        stringed_i = str(i)
        if len(stringed_i) % 2 == 1:
            continue

        if stringed_i[:len(stringed_i)//2] == stringed_i[len(stringed_i)//2:]:
            result += i

    return result

def  process_ranges_2(range_tuple) -> int:
    result = 0
    for i in range(range_tuple[0], range_tuple[1] + 1):
        stringed_i = str(i)
        if match(r'^(\d+)\1+$', stringed_i): result += i

    return result

def solve(file_path: str) -> tuple[int, int]:
    result = 0
    result_2 = 0
    with open(file_path) as f:
        for line in f:
            ranges = split_ranges(line)
            for range_tuple in ranges:
              result += process_ranges(range_tuple)
              result_2 += process_ranges_2(range_tuple)

    return result, result_2


def split_ranges(line: str) -> Generator[tuple[int, int], Any, None]:
    ranges = line.strip().split(",")
    for r in ranges:
        start, end = r.split("-")
        yield int(start), int(end)


if __name__ == "__main__":
    print(solve("input.txt"))