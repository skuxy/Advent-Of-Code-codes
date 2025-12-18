import pytest
from main import solve, solve_second


EXAMPLE = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''


class TestSolve:
    def test_solve_example(self):
        """Test that solve correctly counts numbers within ranges"""
        result = solve(EXAMPLE)
        assert result == 3, f"Expected 3 matches, got {result}"

    def test_solve_empty_input(self):
        """Test solve with no numbers"""
        input_str = '''3-5
10-14

'''
        result = solve(input_str)
        assert result == 0

    def test_solve_no_matches(self):
        """Test solve with numbers outside ranges"""
        input_str = '''3-5
10-14

1
2
15
20
'''
        result = solve(input_str)
        assert result == 0

    def test_solve_all_matches(self):
        """Test solve where all numbers match"""
        input_str = '''1-10

5
7
9
'''
        result = solve(input_str)
        assert result == 3


class TestSolveSecond:
    def test_solve_second_example(self):
        """Test that solve_second correctly identifies matched ranges"""
        result = solve_second(EXAMPLE)
        expected = {3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        assert result == expected, f"Expected {expected}, got {result}"
        assert len(result) == 14

    def test_solve_second_overlapping_ranges(self):
        """Test that overlapping ranges are merged correctly"""
        input_str = '''1-5
4-8
10-15

3
7
12
'''
        result = solve_second(input_str)
        # Should merge 1-5 and 4-8 into 1-8, and include 10-15
        expected = set(range(1, 9)) | set(range(10, 16))
        assert result == expected

    def test_solve_second_adjacent_ranges(self):
        """Test that adjacent ranges are merged correctly"""
        input_str = '''1-5
6-10

3
8
'''
        result = solve_second(input_str)
        # Should merge 1-5 and 6-10 into 1-10
        expected = set(range(1, 11))
        assert result == expected

    def test_solve_second_no_matches(self):
        """Test solve_second with no matching numbers - still returns all ranges merged"""
        input_str = '''3-5
10-14

1
2
20
'''
        result = solve_second(input_str)
        # Even with no matches, solve_second merges ALL ranges
        expected = set(range(3, 6)) | set(range(10, 15))
        assert result == expected

    def test_solve_second_single_range(self):
        """Test solve_second with a single range"""
        input_str = '''5-10

7
8
'''
        result = solve_second(input_str)
        expected = set(range(5, 11))
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

