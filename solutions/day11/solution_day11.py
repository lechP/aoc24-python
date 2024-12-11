def process_num(num: int) -> list[int]:
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        s = str(num)
        half = len(s) // 2
        return [int(s[:half]), int(s[half:])]

    return [num * 2024]


# naive approach with keeping whole list in memory
def process_list(nums: list[int]) -> list[int]:
    i = 0
    while i < len(nums):
        pn = process_num(nums[i])
        nums = nums[:i] + pn + nums[(i + 1):]
        i += len(pn)
    return nums


# suboptimal solution - takes ~3minutes to run for part1
def solution_day11_naive(data) -> int:
    nums = list(map(int, data.split(" ")))
    loops = 25
    for i in range(loops):
        print(f"Loop {i + 1}")
        nums = process_list(nums)
    return len(nums)


def solution_day11(data) -> int:
    nums = list(map(int, data.split(" ")))
    total = 0
    for num in nums:
        total += process_num_v2(num, 25)
    return total

# simple recursive approach - count the length for given initial number
def process_num_v2(num: int, loops: int) -> int:
    if loops == 0:
        return 1
    else:
        if num == 0:
            return process_num_v2(1, loops - 1)
        elif len(str(num)) % 2 == 0:
            s = str(num)
            half = len(s) // 2
            return process_num_v2(int(s[:half]), loops - 1) + process_num_v2(int(s[half:]), loops - 1)
        else:
            return process_num_v2(num * 2024, loops - 1)


def solution_day11_part2(data) -> int:
    nums = list(map(int, data.split(" ")))
    total = 0
    for num in nums:
        total += process_num_with_memo(num, 75)
    return total


# third approach using memoization
cache = {}

def process_num_with_memo(num: int, loops: int) -> int:
    key = (num, loops)
    if key in cache:
        return cache[key]

    if loops == 0:
        res = 1
    else:
        if num == 0:
            res = process_num_with_memo(1, loops - 1)
        elif len(str(num)) % 2 == 0:
            s = str(num)
            half = len(s) // 2
            res = process_num_with_memo(int(s[:half]), loops - 1) + process_num_with_memo(int(s[half:]), loops - 1)
        else:
            res = process_num_with_memo(num * 2024, loops - 1)

    cache[key] = res
    return res
