
import unittest

from solutions.common.readers import read
from solutions.day15.solution_day15 import solution_day15, solution_day15_part2, parse_input

example = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

class TestDay15Unit(unittest.TestCase):
    def test_stub(self):
        parsed = parse_input(example)
        print(parsed)
        self.assertEqual(True, True)

class TestDay15Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(10092, solution_day15(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_day15(_input))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(0, solution_day15_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_day15_part2(_input))


if __name__ == '__main__':
    unittest.main()
