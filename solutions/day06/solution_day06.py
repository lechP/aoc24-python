def count_visited(data: list[str]) -> int:
    visited = set()
    x, y = initial_position(data)
    _dir = initial_dir
    visited.add((x, y))
    while in_bounds(x, y, data):
        x, y, _dir = move(x, y, _dir, data)
        if in_bounds(x, y, data):
            visited.add((x, y))
    return len(visited)

def move(x: int, y: int, _dir: str, data: list[str]) -> tuple[int, int, str]:
    dx = x + directions[_dir][0]
    dy = y + directions[_dir][1]
    if not in_bounds(dx, dy, data):
        return dx, dy, _dir
    if data[dx][dy] == obstacle:
        _dir = dir_switches[_dir]
        dx = x + directions[_dir][0]
        dy = y + directions[_dir][1]
    return dx, dy, _dir

def in_bounds(x: int, y: int, data: list[str]) -> bool:
    return 0 <= x < len(data) and 0 <= y < len(data[0])

def initial_position(data: list[str]) -> tuple[int, int]:
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == initial_dir:
                return i, j
    raise Exception("Initial position not found")

directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

dir_switches = {
    ">": "v",
    "<": "^",
    "^": ">",
    "v": "<"
}

obstacle = '#'
initial_dir = '^'