def split_games(data: str) -> list[str]:
    return data.split('\n\n')

def parse_game(data: str) -> list[list[int]]:
    a, b, goal = data.split('\n')
    a = a.split(": ")[1].split(", ")
    a = [int(x.split("+")[1]) for x in a]
    b = b.split(": ")[1].split(", ")
    b = [int(x.split("+")[1]) for x in b]
    goal = goal.split(": ")[1].split(", ")
    goal = [int(x.split("=")[1]) for x in goal]
    return [a, b, goal]

def cost_of_win_bf(a: list[int], b: list[int], goal: list[int]) -> int:
    ax, ay = a
    bx, by = b
    goalx, goaly = goal

    cost = 999

    for i in range(101):
        for j in range(101):
            if ax*i + bx*j == goalx and ay*i + by*j == goaly:
                cost = min(cost, 3*i+j)

    if cost == 999: # no solution so no cost
        return 0
    return cost


def solution_day13(data) -> int:
    games = list(map(parse_game, split_games(data)))
    return sum(cost_of_win_bf(*game) for game in games)
    
def solution_day13_part2(data) -> int:
    return 0
