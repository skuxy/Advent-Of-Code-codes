#! /usr/bin/env python3


COMP_OPS_MAP = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '<=': lambda x, y: x <= y,
    '>=': lambda x, y: x >= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y
}

OPS_MAP = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y
}

REGISTERS = {}

with open('/dev/stdin') as stdin:
    for line in stdin.readlines():
        line = line.split()

        value_to_check = int(line[6])
        comparison_op = line[5]
        register_to_check = line[4]

        if register_to_check not in REGISTERS:
            REGISTERS[register_to_check] = [0, 0]

        if not COMP_OPS_MAP[comparison_op](REGISTERS[register_to_check][0], value_to_check):
            continue

        register_to_modify = line[0]
        op = line[1]
        modifier_value = int(line[2])

        if register_to_modify not in REGISTERS:
            REGISTERS[register_to_modify] = [0, 0]

        REGISTERS[register_to_modify][0] = OPS_MAP[op](REGISTERS[register_to_modify][0], modifier_value)

        if REGISTERS[register_to_modify][0] > REGISTERS[register_to_modify][1]:
            REGISTERS[register_to_modify][1] = REGISTERS[register_to_modify][0]

    print(max([x[1] for x in REGISTERS.values()]))
