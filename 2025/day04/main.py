example = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

def solve(input_matrix: str) -> (int, list):
    accessible_count = 0
    accessibled = []

    for y, line in enumerate(input_matrix.splitlines()):
        for x, char in enumerate(line):
            if char == '@':
                if is_accessible(input_matrix, x, y):
                    accessible_count += 1
                    accessibled.append((x, y))


    return accessible_count, accessibled


def is_accessible(input_matrix_str: str, coordinate_x: int, coordinate_y: int) -> bool:
    surrounding = 0
    input_matrix = input_matrix_str.splitlines()
    for y in range(coordinate_y - 1, coordinate_y + 2):
        for x in range(coordinate_x - 1, coordinate_x + 2):
            if x == coordinate_x and y == coordinate_y: continue
            if x < 0 or y < 0 or x >= len(input_matrix[0]) or y >= len(input_matrix) or input_matrix[y][x] != '@': continue

            surrounding += 1
            if surrounding >= 4:
                return False

    return True


def test_example():
    result, _ = solve(example)
    assert result == 13

def task():
    result, _ = solve(open("input.txt").read())
    print(result)

def task2():
    initial_matrix = open("input.txt").read()
    total_result = 0
    while True:
        intermediate_result, accessed = solve(initial_matrix)
        if intermediate_result == 0: break

        total_result += intermediate_result

        temporary_matrix = [ list(x) for x in initial_matrix.splitlines()]
        for x,y in accessed:
            temporary_matrix[y][x] = '.'

        initial_matrix = '\n'.join([''.join(x) for x in temporary_matrix])
    print(total_result)



if __name__ == "__main__":
    test_example()
    task()
    task2()
