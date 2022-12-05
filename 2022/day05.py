import sys
import re


crates_1 = [[],[],[],[],[],[],[],[],[]]
crates_2 = [[],[],[],[],[],[],[],[],[]]
def process_crate(line):
    for i in range(len(line)):
        c = line[i]
        if c.isalpha():
            idx = int((i-1)/4) if i > 2 else i - 1
            crates_1[idx].insert(0,c)
            crates_2[idx].insert(0,c)


def process_move(line):
    regex = r'move (\d+) from (\d+) to (\d+)'
    numbers = re.match(regex, line)
    amount, start, target = [int(x) for x in numbers.groups()]

    for _ in range(amount):
        crates_1[target-1].append(crates_1[start - 1].pop())

    crates_2[target-1] += crates_2[start - 1][-amount:]
    del crates_2[start-1][-amount:]
    print(crates_2)
    

with open(sys.argv[1]) as input_file:
    moving_crates = False
    for line in input_file:
        line = line.strip()
        if line == "":
            moving_crates = True
            continue

        if moving_crates:
            process_move(line)
        else:
            process_crate(line)

print("".join([x[-1] for x in crates_1]))
print("".join([x[-1] for x in crates_2]))
            