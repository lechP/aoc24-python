import unittest

from solutions.common.readers import read
from solutions.day13.solution_day13 import solution_day13, solution_day13_part2, parse_game, cost_of_win_bf


class TestDay13Unit(unittest.TestCase):
    def test_parse_game(self):
        game = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400"""
        self.assertEqual([[94, 34], [22, 67], [8400, 5400]], parse_game(game))

    def test_cost_of_win_bf(self):
        self.assertEqual(280, cost_of_win_bf([94, 34], [22, 67], [8400, 5400]))
        self.assertEqual(0, cost_of_win_bf([26, 66], [67, 21], [12748, 12176]))

class TestDay13Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(480, solution_day13(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_day13(_input))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(0, solution_day13_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_day13_part2(_input))


if __name__ == '__main__':
    unittest.main()
