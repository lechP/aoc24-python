
import unittest

from solutions.common.readers import read
from solutions.day16.solution_day16 import solution_day16, solution_day16_part2

example = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

class TestDay16Unit(unittest.TestCase):
    def test_example(self):
        self.assertEqual((11048, 64), solution_day16(example, 11048))

class TestDay16Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual((7036, 45), solution_day16(input_test_1, 7036))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_day16(_input, 73404))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(0, solution_day16_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_day16_part2(_input))


if __name__ == '__main__':
    unittest.main()
