from collections import defaultdict


def parse_input(data: str):
    towels, patterns = data.split("\n\n")
    towels = towels.split(", ")
    patterns = patterns.splitlines()
    return towels, patterns


def solution_day19(data) -> int:
    towels, patterns = parse_input(data)
    result = 0
    for pattern in patterns:
        if possible_ways(pattern, towels) > 0:
            result += 1
    return result

def solution_day19_part2(data) -> int:
    towels, patterns = parse_input(data)
    result = 0
    i = 0
    for pattern in patterns:
        i += 1
        r = possible_ways(pattern, towels)
        result += r
        print(f"{i}:{r}")
    return result


def possible_ways(pattern: str, towels: list[str]) -> int:
    to_check = defaultdict(int)
    to_check[pattern] = 1
    applicable_towels = {x for x in towels if x in pattern}
    count = 0
    while to_check:
        next_to_check = defaultdict(int)
        for testing in to_check:
            if testing in applicable_towels:
                count += to_check[testing]
            for towel in applicable_towels:
                if testing.startswith(towel):
                    next_pattern = testing[len(towel):]
                    next_to_check[next_pattern] += to_check[testing]
        to_check = next_to_check
    return count
