import unittest

from solutions.common.readers import read_strings
from solutions.day03.solution_day03 import get_multiplies, eval_multiplier, sum_multiplies, sum_multiplies_v2

example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

class TestDay03Unit(unittest.TestCase):
    def test_get_multiplies(self):
        self.assertEqual(["mul(2,4)","mul(5,5)", "mul(11,8)", "mul(8,5)"], get_multiplies(example))

    def test_eval_multiplier(self):
        self.assertEqual(88, eval_multiplier("mul(11,8)"))

    def test_sum_multipliers(self):
        self.assertEqual(161, sum_multiplies(example))

class TestDay03Solution(unittest.TestCase):
    def test_count_safe_reports(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(161, sum_multiplies(input_test_1[0]))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(sum_multiplies(_input[0]))

    def test_solution_part2(self):
        _input = read_strings("test1.txt")
        self.assertEqual(48, sum_multiplies_v2(_input[0]))

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(sum_multiplies_v2(_input[0]))

if __name__ == '__main__':
    unittest.main()