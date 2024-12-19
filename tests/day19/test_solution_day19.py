
import unittest

from solutions.common.readers import read
from solutions.day19.solution_day19 import solution_day19, solution_day19_part2, parse_input, possible_ways


class TestDay19Unit(unittest.TestCase):
    def test_possible_ways(self):
        input_test_1 = read("test1.txt")
        towels, patterns = parse_input(input_test_1)
        self.assertEqual(2, possible_ways(patterns[0], towels))

class TestDay19Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(6, solution_day19(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_day19(_input))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(16, solution_day19_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_day19_part2(_input))


if __name__ == '__main__':
    unittest.main()
