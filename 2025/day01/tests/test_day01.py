import os
import unittest
from .. import day01


class TestPassword(unittest.TestCase):
    def setUp(self):
        self.password = day01.Password()

    def test_single_action(self):
        self.assertIsNone(self.password.action("L1"))
        self.assertEqual(self.password.value, 49)

    # Part one had value of 3
    def test_actions_from_file(self):
        input_path = os.path.join(os.path.dirname(__file__), "test01.txt")
        with open(input_path) as test_input:
            for line in test_input:
                self.assertIsNone(self.password.action(line))
        self.assertEqual(self.password.password, 3)

    def test_actions_from_file_part2(self):
        input_path = os.path.join(os.path.dirname(__file__), "test01.txt")
        with open(input_path) as test_input:
            for line in test_input:
                self.assertIsNone(self.password.action(line))
        self.assertEqual(self.password.password_part2, 6)


if __name__ == "__main__":
    unittest.main()
