import re


def get_strongest(line):
    # Get the largest combination of two digits, whether 
    # they are right next to each other or separated by several digits
    
    digits = [char for char in line if char.isdigit()]
    
    if len(digits) < 2:
        return None
    
    # Find all possible two-digit combinations
    max_combination = 0
    
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            # Create two-digit number from digits[i] and digits[j]
            combination = int(digits[i] + digits[j])
            max_combination = max(max_combination, combination)
    
    return max_combination

def find_joltage(lines, needed_bats):
    joltage = 0
    for bank in lines:
        need_to_remove = len(bank) - needed_bats
        while need_to_remove > 0:
            for i in range(len(bank) - 1): 
                if bank[i] < bank[i+1]:
                    bank = bank[:i] + bank[i+1:]
                    break
            need_to_remove -= 1
        joltage += int(bank[:needed_bats])
    return joltage


def solve(input_file: str):
    result = 0
    result2 = 0
    with open(input_file) as f:
        for line in f:
            result += get_strongest(line)

        result2 = find_joltage([line.strip() for line in open(input_file)], 12)
    return result, result2


if __name__ == "__main__":
    print(solve("input.txt"))