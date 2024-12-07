import unittest

from solutions.common.readers import read
from solutions.day05.solution_day05 import parse_input, is_page_valid, sum_valid_pages, revalidate, \
    sum_revalidated_pages

example = read("test1.txt")


class TestDay05Unit(unittest.TestCase):
    def test_parse_input(self):
        rules, pages = parse_input(example)
        self.assertEqual([53, 13, 61, 29], rules[47])
        self.assertEqual([75, 29, 13], pages[2])

    def test_is_page_valid(self):
        rules, pages = parse_input(example)
        self.assertTrue(is_page_valid(rules, pages[0]))
        self.assertTrue(is_page_valid(rules, pages[1]))
        self.assertTrue(is_page_valid(rules, pages[2]))
        self.assertFalse(is_page_valid(rules, pages[3]))
        self.assertFalse(is_page_valid(rules, pages[4]))

    def test_revalidate(self):
        rules, pages = parse_input(example)
        self.assertEqual([97, 75, 47, 61, 53], revalidate(rules, pages[3]))
        self.assertEqual([61, 29, 13], revalidate(rules, pages[4]))


class TestDay05Solution(unittest.TestCase):
    def test_sum_valid_pages(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(143, sum_valid_pages(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(sum_valid_pages(_input))

    def test_count_mas_cross(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(123, sum_revalidated_pages(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(sum_revalidated_pages(_input))


if __name__ == '__main__':
    unittest.main()
