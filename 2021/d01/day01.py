### Part 1
last_number = None
deepers = 0

with open('input.txt') as input_file:
    for line in input_file:
        parsed_num = int(line)

        if last_number and parsed_num > last_number:
            deepers += 1
        
        last_number = parsed_num

print("Answer #1: {}".format(deepers))

### Part 2
last_sum = None
deepers = 0

with open('input.txt') as input_file:
    nums = [int(x) for x in input_file.readlines()] 

    for idx in range(len(nums) - 2):
        current_sum = nums[idx] + nums[idx + 1] + nums[idx + 2]

        if last_sum and current_sum > last_sum:
            deepers += 1

        last_sum = current_sum

print("Answer #2: {}".format(deepers))