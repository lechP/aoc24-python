
import unittest

from solutions.common.readers import read
from solutions.day14.solution_day14 import solution_day14, solution_day14_part2, parse_input


class TestDay14Unit(unittest.TestCase):
    def test_stub(self):
        print(solution_day14(read("test1.txt")))
        self.assertEqual(True, True)

class TestDay14Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(12, solution_day14(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_day14(_input))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(0, solution_day14_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_day14_part2(_input))


if __name__ == '__main__':
    unittest.main()
