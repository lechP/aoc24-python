import unittest

from solutions.common.readers import read_strings, read
from solutions.day08.solution_day08 import solution_day08, solution_day08_part2


class TestDay08Solution(unittest.TestCase):
    def test_solution(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(14, solution_day08(input_test_1))

    def test_solution_on_real_input(self):
        _input = read_strings("input.txt")
        print(solution_day08(_input))

    def test_solution_part2(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(34, solution_day08_part2(input_test_1))

    def test_solution_part2_on_real_input(self):
        _input = read_strings("input.txt")
        print(solution_day08_part2(_input))


if __name__ == '__main__':
    unittest.main()
