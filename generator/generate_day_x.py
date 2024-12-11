import os

day_num = 12
day_name = f"day{day_num}"
day_name_up = f"Day{day_num}"

os.makedirs(f"../solutions/{day_name}")
os.makedirs(f"../tests/{day_name}")
open(f"../solutions/{day_name}/__init__.py", 'a').close()
open(f"../solutions/{day_name}/solution_{day_name}.py", 'a').close()
open(f"../solutions/{day_name}/solution_{day_name}.py", 'w').write(f"""
def solution_{day_name}(data) -> int:
    return 0
    
def solution_{day_name}_part2(data) -> int:
    return 0
""")


test_content = f"""
import unittest

from solutions.common.readers import read
from solutions.{day_name}.solution_{day_name} import solution_{day_name}, solution_{day_name}_part2


class TestDay{day_num}Unit(unittest.TestCase):
    def test_stub(self):
        self.assertEqual(True, True)

class TestDay{day_num}Solution(unittest.TestCase):
    def test_on_test_data_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(0, solution_{day_name}(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(solution_{day_name}(_input))

    def test_on_test_data_part2(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(0, solution_{day_name}_part2(input_test_1))

    def test_result_on_real_input_part2(self):
        _input = read("input.txt")
        print(solution_{day_name}_part2(_input))


if __name__ == '__main__':
    unittest.main()
"""

open(f"../tests/{day_name}/__init__.py", 'a').close()
open(f"../tests/{day_name}/input.txt", 'a').close()
open(f"../tests/{day_name}/test1.txt", 'a').close()
open(f"../tests/{day_name}/test_solution_{day_name}.py", 'a').close()
open(f"../tests/{day_name}/test_solution_{day_name}.py", 'w').write(test_content)

