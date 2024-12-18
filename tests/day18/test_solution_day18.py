
import unittest

from solutions.common.readers import read
from solutions.day18.solution_day18 import solution_day18, solution_day18_part2


class TestDay18Unit(unittest.TestCase):
    def test_stub(self):
        self.assertEqual(True, True)

class TestDay18Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(22, solution_day18(input_test_1, 12, 7))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_day18(_input, 1024, 71))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual((6, 1), solution_day18_part2(input_test_1, 7))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_day18_part2(_input, 71))


if __name__ == '__main__':
    unittest.main()