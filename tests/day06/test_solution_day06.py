import unittest

from solutions.common.readers import read, read_strings
from solutions.day06.solution_day06 import solution_day06, solution_day06_part2

example = read("test1.txt")


class TestDay06Unit(unittest.TestCase):
    def test_(self):
        pass

class TestDay06Solution(unittest.TestCase):
    def test_part1(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(41, solution_day06(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(solution_day06(_input))

    def test_part2(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(6, solution_day06_part2(input_test_1))

    def test_part2_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(solution_day06_part2(_input))


if __name__ == '__main__':
    unittest.main()
