import unittest

from day01 import get_distance, get_list_distance, get_similarity_element, get_list_similarity


class MyTestCase(unittest.TestCase):
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9 ,3]
    def test_distance(self):
        distance = get_distance(1, 3)
        self.assertEqual(2, distance)

    def test_list_distance(self):
        distance = get_list_distance(self.left_list, self.right_list)
        self.assertEqual(11, distance)

    def test_similarity_element(self):
        similarity = get_similarity_element(3, self.right_list)
        self.assertEqual(9, similarity)

    def test_similarity_list(self):
        similarity = get_list_similarity(self.left_list, self.right_list)
        self.assertEqual(31, similarity)


if __name__ == '__main__':
    unittest.main()
