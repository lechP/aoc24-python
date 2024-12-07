import unittest

from solutions.common.readers import read_strings
from solutions.day02.solution_day02 import count_safe_reports, count_safe_reports_with_dampener

strings = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
]

class TestDay02Unit(unittest.TestCase):
    def test_placeholder(self):
        pass

class TestDay02Solution(unittest.TestCase):
    def test_count_safe_reports(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(2, count_safe_reports(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(count_safe_reports(_input))

    def test_solution_part2(self):
        _input = read_strings("test1.txt")
        self.assertEqual(4, count_safe_reports_with_dampener(_input))

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(count_safe_reports_with_dampener(_input))

if __name__ == '__main__':
    unittest.main()