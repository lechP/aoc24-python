
import unittest

from solutions.common.readers import read
from solutions.day17.solution_day17 import solution_day17, solution_day17_part2


class TestDay17Unit(unittest.TestCase):
    def test_stub(self):
        self.assertEqual(True, True)

class TestDay17Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual("4,6,3,5,6,3,5,2,1,0", solution_day17(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_day17(_input))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(0, solution_day17_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_day17_part2(_input))


if __name__ == '__main__':
    unittest.main()
