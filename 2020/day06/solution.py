import sys

def parse_input_entry_by_line(input_file_name, cast=None):
    # Input files should be small enough for us not to care
    with open(input_file_name) as input_file:
        if cast:
            return [cast(x) for x in input_file.readlines()]
        else:
            return input_file.readlines()


def parse_input_data(input_data):
    group_answers = set()
    group_answered_all = []
    at_least_one_answer = []
    all_answers = []
    for line in input_data:
        if line == "":
            at_least_one_answer.append(group_answers)
            group_answers = set()

            # all_answers.append(group_answered_all) 
            all_answers.append(set.intersection(*group_answered_all))
            group_answered_all = []
            continue

        group_answers.update(line)
        group_answered_all.append(set(line))
        
    
    one_answers_count = sum([len(x) for x in at_least_one_answer])
    all_answers_count = sum([len(x) for x in all_answers])

    return one_answers_count, all_answers_count


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    input_data = parse_input_entry_by_line(input_file_name, lambda x: x.strip())
    print(parse_input_data(input_data))