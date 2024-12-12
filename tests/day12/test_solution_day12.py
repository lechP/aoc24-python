
import unittest

from solutions.common.readers import read, read_strings
from solutions.day12.solution_day12 import solution_day12, solution_day12_part2, price


class TestDay12Unit(unittest.TestCase):
    def test_stub(self):
        region_r = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (2, 4), (3, 2)]
        self.assertEqual(216, price(region_r))
        region_e = [(9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (9, 7), (8, 7)]
        self.assertEqual(234, price(region_e))
        region_j =  [(9, 6), (8, 6), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (4, 5), (5, 7), (6, 7), (7, 7)]
        self.assertEqual(220, price(region_j))

class TestDay12Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(1930, solution_day12(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(solution_day12(_input))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(0, solution_day12_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_day12_part2(_input))


if __name__ == '__main__':
    unittest.main()
