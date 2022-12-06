def process_line(line):
    for i in range(len(line)):
        window = line[i:i+4]

        if len(window) == len(set(window)):
            # offset because we start with 1, and add 4 as it's "marker processed"
            return i + 4

def process_line_2(line):
    for i in range(len(line)):
        window = line[i:i+14]

        if len(window) == len(set(window)):
            # offset because we start with 1, and add 4 as it's "marker processed"
            return i + 14


with open('/dev/stdin') as input_file:
    for line in input_file:
        print(process_line(line))
        print(process_line_2(line))