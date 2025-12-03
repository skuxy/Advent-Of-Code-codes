import os
import unittest
from unittest import TestCase
from ..day03 import get_strongest, solve


class Test(TestCase):
    def test_get_strongest(self) -> None:
        self.assertEqual(get_strongest("987654321111111"), 98)
        self.assertEqual(get_strongest("811111111111119"), 89)

    def test_case(self):
        self.assertEqual(solve(os.path.join(os.path.dirname(__file__),"test.txt")), 357)


if __name__ == "__main__":
    unittest.main()