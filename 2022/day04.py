import sys

def process_line(line):
    elf_one, elf_two = line.split(',')
    elf_one = [int (x) for x in elf_one.split('-')]
    elf_two = [int (x) for x in elf_two.split('-')]

    if elf_one[0] >= elf_two[0] and elf_one[1] <= elf_two[1]:
        return 1

    if elf_one[0] <= elf_two[0] and elf_one[1] >= elf_two[1]:
        return 1

    return 0

def process_line2(line):
    elf_one, elf_two = line.split(',')
    elf_one = [int (x) for x in elf_one.split('-')]
    elf_two = [int (x) for x in elf_two.split('-')]

    if elf_one[0] <= elf_two[0] and elf_one[1] >= elf_two[0]:
        return 1
    
    if elf_two[0] <= elf_one[0] and elf_two[1] >= elf_one[0]:
        return 1

    return 0


fully_contain = 0
overlap = 0

with open(sys.argv[1]) as file_input:
    for line in file_input:
        fully_contain += process_line(line)
        overlap += process_line2(line)

print(fully_contain)
print(overlap)