import unittest

from solutions.common.readers import read_strings
from solutions.day07.solution_day07 import total_calibration_result, parse_line, check_equation, to_operators, \
    is_result_possible, total_calibration_result_v2, is_result_possible_v2

example = read_strings("test1.txt")


class TestDay07Unit(unittest.TestCase):
    def test_parse_input(self):
        result, operands = parse_line(example[0])
        self.assertEqual(190, result)
        self.assertEqual([10, 19], operands)

    def test_check_equation(self):
        result, operands = parse_line(example[0])
        self.assertTrue(check_equation(result, operands, ["*"]))
        result, operands = parse_line(example[8])
        self.assertTrue(check_equation(result, operands, ["+", "*", "+"]))
        self.assertFalse(check_equation(result, operands, ["+", "+", "+"]))

    def test_to_operators(self):
        self.assertEqual(["*", "+", "*"], to_operators("101"))

    def test_is_result_possible(self):
        result, operands = parse_line(example[0])
        self.assertTrue(is_result_possible(result, operands))
        result, operands = parse_line(example[4])
        self.assertFalse(is_result_possible(result, operands))
        result, operands = parse_line(example[8])
        self.assertTrue(is_result_possible(result, operands))

    def test_is_result_possible_v2(self):
        result, operands = parse_line(example[0])
        self.assertTrue(is_result_possible_v2(result, operands))
        result, operands = parse_line(example[3])
        self.assertTrue(is_result_possible_v2(result, operands))

class TestDay07Solution(unittest.TestCase):
    def test_total_calibration_result(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(3749, total_calibration_result(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(total_calibration_result(_input))

    def test_total_calibration_result_v2(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(11387, total_calibration_result_v2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(total_calibration_result_v2(_input))


if __name__ == '__main__':
    unittest.main()
