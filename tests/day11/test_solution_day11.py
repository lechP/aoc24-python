import unittest

from solutions.common.readers import read
from solutions.day11.solution_day11 import process_list, solution_day11


class TestDay11Unit(unittest.TestCase):
    def test_process_list(self):
        self.assertEqual([253000, 1, 7], process_list([125, 17]))
        self.assertEqual([512072, 1, 20, 24, 28676032], process_list([253, 0, 2024, 14168]))
        self.assertEqual([2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2],
                         process_list([1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32]))

class TestDay11Solution(unittest.TestCase):
    def test_total_calibration_result(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(55312, solution_day11(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_day11(_input))

    # def test_total_calibration_result_v2(self):
    #     input_test_1 = read_strings("test1.txt")
    #     self.assertEqual(81, solution_day10_part2(input_test_1))
    #
    # def test_result_on_real_input_part2(self):
    #     _input = read_strings("input.txt")
    #     print(solution_day10_part2(_input))


if __name__ == '__main__':
    unittest.main()