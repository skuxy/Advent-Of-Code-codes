import os
import unittest
from .. import day02


class TestPassword(unittest.TestCase):
    def test_ranges(self):
        self.assertEqual(day02.process_ranges((11,22)), 33)
        self.assertEqual(day02.process_ranges((95,115)), 99)
        self.assertEqual(day02.process_ranges((38593856,38593862)), 38593859)
    def test_case(self):
        input_path = os.path.join(os.path.dirname(__file__), "test.txt")
        self.assertEqual(day02.solve(input_path), 1227775554)

if __name__ == "__main__":
    unittest.main()
