
def get_distance(left_elem, right_elem):
    return abs(left_elem - right_elem)

def get_list_distance(left_list, right_list):
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    list_distance = map(get_distance, left_list_sorted, right_list_sorted)

    return sum(list_distance)

def get_similarity_element(element, list_for_comparison):
    return list_for_comparison.count(element) * element


def get_list_similarity(left_list, right_list):
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    list_similarity = 0
    for element in left_list_sorted:
        list_similarity += get_similarity_element(element, right_list_sorted)


    return list_similarity


if __name__ == '__main__':
    left_list = []
    right_list = []
    with open('input.txt') as f:
        for line in f:
            left_element, right_element = map(int, line.split())
            left_list += [left_element]
            right_list += [right_element]

    distance = get_list_distance(left_list, right_list)
    print(distance)

    similarity = get_list_similarity(left_list, right_list)
    print(similarity)

