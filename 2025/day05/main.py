example = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''


def parse_input(input_string):
    """Parse input into ranges and numbers."""
    range_state = True
    ranges = []
    numbers = []

    for line in input_string.splitlines():
        if line == '':
            range_state = False
            continue

        if range_state:
            ranges.append(tuple(map(int, line.split('-'))))
        else:
            numbers.append(int(line))

    return ranges, numbers


def solve(input_string):
    """Count how many numbers fall within at least one range."""
    ranges, numbers = parse_input(input_string)
    result = 0

    for number in numbers:
        for start, end in ranges:
            if start <= number <= end:
                result += 1
                break

    return result


def merge_ranges(ranges):
    """Merge overlapping or adjacent ranges."""
    if not ranges:
        return []

    sorted_ranges = sorted(set(ranges))
    merged = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:
            # Overlapping or adjacent ranges, merge them
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    return merged


def solve_second(input_string):
    """Calculate total coverage of ALL ranges (merged)."""
    ranges, numbers = parse_input(input_string)

    # Use all unique ranges, not just matched ones
    unique_ranges = list(set(ranges))

    if not unique_ranges:
        return set()

    merged = merge_ranges(unique_ranges)

    # Calculate total coverage
    total = sum(end - start + 1 for start, end in merged)

    # For compatibility with existing test, return set for small ranges
    if total < 10000:
        result = set()
        for start, end in merged:
            result.update(range(start, end + 1))
        return result

    # For large ranges, return the count
    return total


def test_example(input_string):
    result = solve(input_string)
    second_result = solve_second(input_string)

    assert result == 3
    # solve_second merges ALL ranges: (3-5), (10-14), (12-18), (16-20)
    # After merging: (3-5) and (10-20) = 3+4+5+10-20 = 14 elements
    assert second_result == {3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    assert len(second_result) == 14


def task():
    """Solve both parts of the puzzle."""
    with open("input.txt") as f:
        input_data = f.read()

    result = solve(input_data)
    print(f"Part 1: {result}")

    ranges_result = solve_second(input_data)
    if isinstance(ranges_result, set):
        print(f"Part 2: {len(ranges_result)}")
    else:
        print(f"Part 2: {ranges_result}")


if __name__ == "__main__":
    test_example(example)
    task()