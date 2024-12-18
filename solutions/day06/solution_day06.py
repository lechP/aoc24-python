def solution_day06(data: list[str]) -> int:
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
    while (in_bounds(x + directions[_dir][0], y + directions[_dir][1], data)
           and data[x + directions[_dir][0]][y + directions[_dir][1]] == obstacle): # do turn as long as there is an obstacle
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


def solution_day06_part2(data: list[str]) -> int:
    initial_path = get_initial_path(data)
    loop_obstacles = set()
    init_pos = initial_position(data)
    for step in initial_path:
        x, y, _ = step
        if (x, y) != init_pos:
            data_copy = data.copy()
            data_copy[x] = data_copy[x][:y] + obstacle + data_copy[x][y + 1:]
            if falls_into_a_loop(data_copy):
                loop_obstacles.add((x, y))
    return len(loop_obstacles)


def falls_into_a_loop(data: list[str]) -> bool:
    visited = set()
    x, y = initial_position(data)
    _dir = initial_dir
    while in_bounds(x, y, data):
        x, y, _dir = move(x, y, _dir, data)
        if (x, y, _dir) in visited:
            return True
        visited.add((x, y, _dir))
    return False


def get_initial_path(data: list[str]):
    visited = []
    x, y = initial_position(data)
    _dir = initial_dir
    while in_bounds(x, y, data):
        x, y, _dir = move(x, y, _dir, data)
        if in_bounds(x, y, data):
            visited.append((x, y, _dir))
    return visited
