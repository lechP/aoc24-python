def parse_input(data: str):
    towels, patterns = data.split("\n\n")
    towels = towels.split(", ")
    patterns = patterns.splitlines()
    return towels, patterns


def solution_day19(data) -> int:
    towels, patterns = parse_input(data)
    result = 0
    for pattern in patterns:
        if is_possible(pattern, towels):
            result += 1
    return result

def is_possible(pattern: str, towels: list[str]) -> bool:
    to_check = set()
    to_check.add(pattern)
    while len(to_check)>0:
        current = to_check.pop()
        if current == "":
            return True
        for towel in towels:
            if current.startswith(towel):
                to_check.add(current[len(towel):])
    return False


def solution_day19_part2(data) -> int:
    return 0
