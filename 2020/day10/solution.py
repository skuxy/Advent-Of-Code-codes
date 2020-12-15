import sys


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, int)

    sorted_input_data = sorted(input_data)

    sorted_input_data.insert(0, 0)
    device_joltage = max(sorted_input_data) + 3
    sorted_input_data.append(device_joltage)

    differences = []
    data_len = len(sorted_input_data)

    for i in range(1,data_len):
        difference = sorted_input_data[i] - sorted_input_data[i - 1]
        differences.append(difference)

    print(differences.count(1) * differences.count(3))

    # Better than previous recursive solution which took some 20mins
    routes = {}
    routes[0] = 1

    for joltage in sorted_input_data[1:]:
        routes[joltage] = \
            routes.get(joltage - 1, 0) + \
            routes.get(joltage - 2, 0) + \
            routes.get(joltage - 3, 0)

    print(routes[device_joltage])
