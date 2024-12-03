from unittest import TestCase

from day03 import filter_multiply_string, multiply_results, filter_conditional_multiply_string


class TestFilter(TestCase):
    example_string = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

    def test_filter_multiply_string(self):
        result = filter_multiply_string(self.example_string)
        self.assertEqual([(2, 4), (5, 5), (11, 8), (8, 5)], result)

    def test_multiply_results(self):
        factors = filter_multiply_string(self.example_string)
        result = multiply_results(factors)

        self.assertEqual(161, result)


class TestConditional(TestCase):
    example_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    def test_filter_conditional_mutliply_string(self):
        result = filter_conditional_multiply_string(self.example_string)
        self.assertEqual([(2,4), (8,5)], result)

    def test_multiply_results(self):
        factors = filter_conditional_multiply_string(self.example_string)
        result = multiply_results(factors)

        self.assertEqual(48, result)