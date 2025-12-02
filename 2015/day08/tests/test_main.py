import unittest
from unittest import TestCase

from ..main import Stringify

class TestStringify(TestCase):
    def test_stringify(self):
        assert(Stringify("").string_literal == 2)
        assert(Stringify("").string_memory == 0)


if __name__ == "__main__":
    unittest.main()