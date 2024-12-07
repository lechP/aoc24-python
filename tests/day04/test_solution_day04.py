import unittest

from solutions.common.readers import read_strings
from solutions.day04.solution_day04 import count_xmas, count_mas_cross

example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

class TestDay04Unit(unittest.TestCase):
    def test_count_xmas(self):
        self.assertEqual(18, count_xmas(example))

    def test_count_mas_cross(self):
        self.assertEqual(9, count_mas_cross(example))


class TestDay04Solution(unittest.TestCase):
    def test_count_xmas(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(18, count_xmas(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(count_xmas(_input))

    def test_count_mas_cross(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(9, count_mas_cross(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(count_mas_cross(_input))


if __name__ == '__main__':
    unittest.main()