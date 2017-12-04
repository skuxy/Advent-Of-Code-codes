#! /usr/bin/env python3


def there_are_duplicates(words):
    return len(set(words)) != len(words)


def there_are_anagrams(words):
    sorted_words = list(map(sorted, words))
    while sorted_words:
        sorted_word = sorted_words.pop()

        for candidate_word in sorted_words:
            if candidate_word == sorted_word:
                return True
    return False


if __name__ == "__main__":
    with open('/dev/stdin') as stdin:
        """ export IFS=$'\n' """
        correct_passwords = 0
        for line in stdin:
            words = line.split()

            if there_are_duplicates(words):
                continue
            if not there_are_anagrams(words):
                correct_passwords += 1

    print(correct_passwords)
