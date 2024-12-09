import unittest

from solutions.common.readers import read_strings, read
from solutions.day09.solution_day09 import count_checksum

example = read_strings("test1.txt")


class TestDay07Unit(unittest.TestCase):
    def test_count_checksum(self):
        self.assertEqual(2+4+3+4+5+12+14+16, count_checksum("12345"))
        self.assertEqual(1928, count_checksum("2333133121414131402"))

class TestDay07Solution(unittest.TestCase):
    def test_total_calibration_result(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(1928, count_checksum(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(count_checksum(_input))

    # def test_total_calibration_result_v2(self):
    #     input_test_1 = read_strings("test1.txt")
    #     self.assertEqual(11387, total_calibration_result_v2(input_test_1))
    #
    # def test_result_on_real_input_part2(self):
    #     _input = read_strings("input.txt")
    #     print(total_calibration_result_v2(_input))


if __name__ == '__main__':
    unittest.main()
