import unittest
from unittest import TestCase

from day02 import LineState, LineStateDampened

example_matrix = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


class TestLineState(unittest.TestCase):
    def test_run(self):
        test_cases = example_matrix.split('\n')
        expected_results = [True, False, False, False, False, True]

        for i, test_case in enumerate(test_cases):
            line_state = LineState(test_case)
            self.assertEqual(expected_results[i], line_state.run())

    def test_run_dampened(self):
        test_cases = example_matrix.split('\n')
        expected_results = [True, False, False, True, True, True]

        for i, test_case in enumerate(test_cases):
            line_state = LineStateDampened(test_case)
            self.assertEqual(expected_results[i], line_state.run())


if __name__ == '__main__':
    unittest.main()