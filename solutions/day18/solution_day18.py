import sys


def parse_input(data: str) -> list[tuple[int, int]]:
    lines = data.split("\n")
    result = []
    for line in lines:
        ints = list(map(int, line.split(",")))
        result.append((ints[0], ints[1]))
    return result

def possible_moves(obstacles: set[tuple[int, int]], size: int) -> set[tuple[int, int]]:
    moves = set()
    for i in range(size):
        for j in range(size):
            if (j, i) not in obstacles:
                moves.add((j, i))
    moves.remove((0,0))
    return moves

def solution_day18(data: str, limit: int, size: int) -> int:
    sys.setrecursionlimit(1300)
    fallen_bytes = set(parse_input(data)[:limit])
    pos = (0, 0)
    end = (size - 1, size - 1)
    moves = possible_moves(fallen_bytes, size)
    score = 0
    cache = { pos: score }
    return get_min_score(cache, pos, moves, score, end)

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# recursive approach -> ~22s
def get_min_score(cache: dict[tuple[int, int], int], pos: tuple[int, int], moves: set[tuple[int, int]], score: int, end: tuple[int, int]) -> int:
    possible_next_scores = set()
    for d in dirs:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if new_pos in moves:
            if new_pos == end:
                return score + 1
            if new_pos not in cache or cache[new_pos] > score + 1:
                cache[new_pos] = score + 1
                moves_copy = moves.copy()
                moves_copy.remove(new_pos)
                possible_next_scores.add(get_min_score(cache, new_pos, moves_copy, score + 1, end))
    if len(possible_next_scores) == 0:
        return 999999999999
    else:
        return min(possible_next_scores)

def solution_day18_part2(data: str, size: int) -> tuple[int, int]:
    all_bytes = parse_input(data)
    pos = (0, 0)
    end = (size - 1, size - 1)
    grid = set()
    for i in range(size):
        for j in range(size):
                grid.add((j, i))
    grid.remove((0,0))
    i = 0
    byte = all_bytes[i]
    while True:
        grid.remove(byte)
        if not check_end_reachable(pos, grid.copy(), end):
            return byte
        i += 1
        byte = all_bytes[i]

def check_end_reachable(pos: tuple[int, int], grid: set[tuple[int, int]], end: tuple[int, int]) -> bool:
    reachable = set()
    to_visit = [pos]
    while len(to_visit) > 0:
        current = to_visit.pop()
        if current == end:
            return True
        reachable.add(current)
        for d in dirs:
            new_pos = (current[0] + d[0], current[1] + d[1])
            if new_pos in grid:
                to_visit.append(new_pos)
                grid.remove(new_pos)
    return False


def draw_grid(items: set[tuple[int, int]], size: int):
    for i in range(size):
        for j in range(size):
            if (j, i) in items:
                print("#", end="")
            else:
                print(".", end="")
        print()

def draw_grid_mirror(items: set[tuple[int, int]], size: int):
    for i in range(size):
        for j in range(size):
            if (j, i) in items:
                print(".", end="")
            else:
                print("#", end="")
        print()