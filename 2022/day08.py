import sys


with open(sys.argv[1]) as input_file:
    grid = input_file.readlines()

max_height = [-1] * 99
visible = set()

for y in range(len(grid)):
    for x in range(len(grid[0].strip())):
        current_h = int(grid[y][x])
        if max_height[y] < current_h:
            max_height[y] = current_h
            visible.add((x,y))

max_height = [-1] * 99
for y in range(len(grid)):
    for x in reversed(range(len(grid[0].strip()))):
        current_h = int(grid[y][x])
        if max_height[y] < current_h:
            max_height[y] = current_h
            visible.add((x,y))

max_height = [-1] * 99
for y in range(len(grid)):
    for x in range(len(grid[0].strip())):
        current_h = int(grid[y][x])
        if max_height[x] < current_h:
            max_height[x] = current_h
            visible.add((x,y))

max_height = [-1] * 99
for y in reversed(range(len(grid))):
    for x in range(len(grid[0].strip())):
        current_h = int(grid[y][x])
        if max_height[x] < current_h:
            max_height[x] = current_h
            visible.add((x,y))

print(len(visible))