import sys
import re


expected_fields = {
    'byr': "Required",
    'iyr': "Required",
    'eyr': "Required",
    'hgt': "Required",
    'hcl': "Required",
    'ecl': "Required",
    'pid': "Required",
    'cid': "Optional"
}

def validate_height(hgt):
    if hgt[-2:] == 'cm':
        height = int(hgt[:-2])
        if height >= 150 and height <= 193:
            return True

    elif hgt[-2:] == 'in':
        height = int(hgt[:-2])
        if height >= 59 and height <= 76:
            return True

    return False

field_validation = {
    'byr': lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and int(x) >= 2020 and int(x) <= 2030,
    'hgt': validate_height,
    'hcl': lambda x: re.match("#[0-9a-f]{6}",x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.match('[0-9]{9}', x),
    'cid': lambda x: x == x
}


def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


def parse_input_data(input_data):
    user_data = {}
    complete_passports = 0
    valid_passports = 0
    for line in input_data:
        if not line:
            verdict = process_data_presentness(user_data)
            if verdict:
                complete_passports += 1
                valid = process_data_validity(user_data)
                if valid:
                    valid_passports += 1

            user_data = {}
            continue

        for pair in line:
            key, value = pair.split(':')
            user_data[key] = value

    verdict = process_data_presentness(user_data)
    if verdict:
        complete_passports += 1
        valid = process_data_validity(user_data)
        if valid:
            valid_passports += 1

    return complete_passports, valid_passports


def process_data_presentness(user_data):
    present_fields = {}
    for key in user_data:
        if expected_fields[key] == 'Required':
            present_fields[key] = True

    return len(present_fields) == 7
    

def process_data_validity(user_data):
    for key in user_data:
        if not field_validation[key](user_data[key]):
            return False

    return True


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, lambda x: x.split())
    print(parse_input_data(input_data))
