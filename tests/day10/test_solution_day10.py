import unittest

from solutions.common.readers import read_strings
from solutions.day10.solution_day10 import solution_day10, solution_day10_part2


class TestDay10Solution(unittest.TestCase):
    def test_total_calibration_result(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(36, solution_day10(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(solution_day10(_input))

    def test_total_calibration_result_v2(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(81, solution_day10_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(solution_day10_part2(_input))


if __name__ == '__main__':
    unittest.main()
