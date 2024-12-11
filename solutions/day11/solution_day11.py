def process_num(num: int) -> list[int]:
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        s = str(num)
        half = len(s) // 2
        return [int(s[:half]), int(s[half:])]

    return [num * 2024]


def process_list(nums: list[int]) -> list[int]:
    i = 0
    while i < len(nums):
        pn = process_num(nums[i])
        nums = nums[:i] + pn + nums[(i + 1):]
        i += len(pn)
    return nums


def solution_day11(data) -> int:
    nums = list(map(int, data.split(" ")))
    loops = 25
    for i in range(loops):
        print(f"Loop {i + 1}")
        nums = process_list(nums)
    return len(nums)


def solution_day11_part2(data) -> int:
    return 0
