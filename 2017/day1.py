#! /usr/bin/env python3

RESULTING_SUM_FIRST = 0
RESULTING_SUM_SECOND = 0

for line in open('/dev/stdin').readlines():
    line_length = len(line) - 1
    for index in range(line_length):
        if line[index] == line[(index + 1) % (line_length)]:
            RESULTING_SUM_FIRST += int(line[index])
        if line[index] == line[int((index + line_length / 2) % line_length)]:
            RESULTING_SUM_SECOND += int(line[index])

    # Result for the first part
    print(RESULTING_SUM_FIRST)
    # Result for the second part
    print(RESULTING_SUM_SECOND)
