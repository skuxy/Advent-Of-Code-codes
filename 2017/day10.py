#! /usr/bin/env python3


class knot_hash:
    def __init__(self, lenghts_sequence):
        self.circular_list = list(range(256))
        self.lenghts_sequence = lenghts_sequence
        self.current_index = 0
        self.skip = 0

    def reverse_slice(self, length):
        if 256 - self.current_index > length:
            reversed_slice = \
                list(reversed(
                    self.circular_list[self.current_index:self.current_index + length]
                ))
            self.circular_list[self.current_index:self.current_index + length] = reversed_slice
        else:
            until_end = 256 - self.current_index
            from_beginning = length - until_end
            reversed_slice = list(reversed(
                self.circular_list[self.current_index:] + self.circular_list[:from_beginning]
            ))
            self.circular_list[self.current_index:] = reversed_slice[:until_end]
            self.circular_list[:from_beginning] = reversed_slice[until_end:]

        self.current_index += length + self.skip
        self.current_index %= 256
        self.skip += 1

    def calculate_knot_hash(self):
        for _ in range(64):
            for length in self.lenghts_sequence:
                self.reverse_slice(length)

        splitted_list = split_list(self.circular_list)
        xored_lists = [xor_over_list(elem) for elem in splitted_list]

        hex_string = ''.join(["%02x" % x for x in xored_lists])

        return hex_string


def xor_over_list(list_of_numbers):
    xor_result = 0
    for number in list_of_numbers:
        xor_result ^= number

    return xor_result


def split_list(list_of_numbers, number_of_pieces=16):
    split_len = int(len(list_of_numbers) / number_of_pieces)
    chunks = [list_of_numbers[index:index+split_len] for index in range(0, len(list_of_numbers), split_len)]

    return chunks


if __name__ == "__main__":
    with open('/dev/stdin') as stdout:
        lenghts_sequence = stdout.read().strip()
        lenghts_sequence = list(map(ord, lenghts_sequence))
        lenghts_sequence += [17, 31, 73, 47, 23]

    knot = knot_hash(lenghts_sequence)
    for _ in range(64):
        for length in knot.lenghts_sequence:
            knot.reverse_slice(length)

    splitted_list = split_list(knot.circular_list)
    xored_lists = [xor_over_list(elem) for elem in splitted_list]

    hex_string = ''.join(["%02x" % x for x in xored_lists])

    print(hex_string)
