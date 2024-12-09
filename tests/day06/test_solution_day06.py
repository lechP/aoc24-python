import unittest

from solutions.common.readers import read, read_strings
from solutions.day06.solution_day06 import count_visited

example = read("test1.txt")


class TestDay06Unit(unittest.TestCase):
    def test_(self):
        pass

class TestDay06Solution(unittest.TestCase):
    def test_sum_valid_pages(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(41, count_visited(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(count_visited(_input))

    # def test_count_mas_cross(self):
    #     input_test_1 = read("test1.txt")
    #     self.assertEqual(123, sum_revalidated_pages(input_test_1))
    #
    # def test_result_on_real_input_part2(self):
    #     _input = read("input.txt")
    #     print(sum_revalidated_pages(_input))


if __name__ == '__main__':
    unittest.main()
