import unittest

from solutions.common.readers import read_strings
from solutions.day01.solution_day01 import read_two_lists_of_integers, distance, solution_distance, \
    solution_similarity

strings = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
]

class TestDay01Unit(unittest.TestCase):
    def test_read_two_lists_of_integers(self):
        list1, list2 = read_two_lists_of_integers(strings)
        self.assertEqual([3, 4, 2, 1, 3, 3], list1)
        self.assertEqual([4, 3, 5, 3, 9, 3], list2)

    def test_distance(self):
        l1 = [3, 4, 2, 1, 3, 3]
        l2 = [4, 3, 5, 3, 9, 3]
        self.assertEqual(11, distance(l1, l2))

class TestDay01Solution(unittest.TestCase):

    def test_solution_part1(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(11, solution_distance(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(solution_distance(_input))

    def test_solution_part2(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(31, solution_similarity(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(solution_similarity(_input))

if __name__ == '__main__':
    unittest.main()