import os

day_num = 11
day_name = f"day{day_num}"

os.makedirs(f"../solutions/{day_name}")
os.makedirs(f"../tests/{day_name}")
open(f"../solutions/{day_name}/__init__.py", 'a').close()
open(f"../solutions/{day_name}/solution_{day_name}.py", 'a').close()
open(f"../solutions/{day_name}/solution_{day_name}.py", 'w').write("""
def solution_day11(data) -> int:
    return 0
    
def solution_day11_part2(data) -> int:
    return 0
""")

open(f"../tests/{day_name}/__init__.py", 'a').close()
open(f"../tests/{day_name}/input.txt", 'a').close()

open(f"../tests/{day_name}/test1.txt", 'a').close()
open(f"../tests/{day_name}/test1.txt", 'w').write("hello")
open(f"../tests/{day_name}/test_solution_{day_name}.py", 'a').close()
