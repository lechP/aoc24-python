def split_games(data: str) -> list[str]:
    return data.split('\n\n')


def parse_game(data: str) -> list[list[int]]:
    a, b, goal = data.split('\n')
    a = parse_line(a, "+")
    b = parse_line(b, "+")
    goal = parse_line(goal, "=")
    return [a, b, goal]


def parse_line(line: str, delimiter: str) -> list[int]:
    """
    Given a line like "sth a: X+3, Y+4",
    extract the integers after the specified delimiter ('+' or '=').
    """
    values_str = line.split(": ")[1]
    items = values_str.split(", ")
    return [int(item.split(delimiter)[1]) for item in items]


def parse_game_v2(data: str) -> list[list[int]]:
    a, b, goal = parse_game(data)
    bignum = 10000000000000
    goal = [n + bignum for n in goal]
    return [a, b, goal]


# brute force solution
def cost_of_win_bf(a: list[int], b: list[int], goal: list[int]) -> int:
    ax, ay = a
    bx, by = b
    goalx, goaly = goal

    cost = 999

    for i in range(101):
        for j in range(101):
            if ax * i + bx * j == goalx and ay * i + by * j == goaly:
                cost = min(cost, 3 * i + j)

    if cost == 999:  # no solution so no cost
        return 0
    return cost


def cost_of_win(a: list[int], b: list[int], goal: list[int]) -> int:
    ax, ay = a
    bx, by = b
    goal_x, goal_y = goal

    if ax * by == bx * ay:
        return 0

    b = (goal_x - ax * goal_y / ay) / (bx - ax * by / ay)
    if is_fractional(b):
        return 0

    a = (goal_y - by * b) / ay
    if is_fractional(a):
        return 0

    if a < 0 or b < 0:
        return 0

    return 3 * int(round(a, 0)) + int(round(b, 0))

def is_fractional(n: float) -> bool:
    return 0.001 < n - int(n) < 0.999


def solution_day13(data) -> int:
    games = list(map(parse_game, split_games(data)))
    return sum(cost_of_win(*game) for game in games)


def solution_day13_part2(data) -> int:
    games = list(map(parse_game_v2, split_games(data)))
    return sum(cost_of_win(*game) for game in games)
