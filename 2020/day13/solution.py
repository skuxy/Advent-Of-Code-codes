import sys


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()

def check_busses(timestamp, busses):
    for bus in busses:
        if not (timestamp + busses[bus]) % bus == 0:
            return False

    return True


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    with open(input_file_name) as input_file:
        input_file = input_file.readlines()

    # timestamp = int(input_file[0])
    # busses = {}
    # min_waiting_bus = None

    # # part 1
    # for bus in input_file[1].strip().split(','):
    #     if bus == 'x':
    #         continue
    #     
    #     bus_id = int(bus)
    #     busses[bus_id] = bus_id - (timestamp % bus_id)

    #     if not min_waiting_bus or busses[min_waiting_bus] > busses[bus_id]:
    #         min_waiting_bus = bus_id
    
    # min_wait = min_waiting_bus - (timestamp % min_waiting_bus)
    # print(min_wait * min_waiting_bus)
    
    # part 2
    timestamp = 0

    # busses[bus] = delay
    busses = {}
    delay = 0
    first_bus = None

    for bus in input_file[1].strip().split(','):
        if bus != 'x':
            bus_id = int(bus)

            if not first_bus:
                first_bus = bus_id

            busses[bus_id] = timestamp + delay

        delay += 1

    timestamp += first_bus
    while True:
        if check_busses(timestamp, busses):
            break

        timestamp += first_bus

    print(timestamp)