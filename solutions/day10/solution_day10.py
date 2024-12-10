def count_paths(data, x, y, rows, cols, v) -> set[tuple[int, int]]:
    if v == 9:
        return {(y, x)}
    else:
        paths = set()
        if x + 1 < cols and data[y][x + 1] == v + 1:
            paths.update(count_paths(data, x + 1, y, rows, cols, v + 1))
        if y + 1 < rows and data[y + 1][x] == v + 1:
            paths.update(count_paths(data, x, y + 1, rows, cols, v + 1))
        if x - 1 >= 0 and data[y][x - 1] == v + 1:
            paths.update(count_paths(data, x - 1, y, rows, cols, v + 1))
        if y - 1 >= 0 and data[y - 1][x] == v + 1:
            paths.update(count_paths(data, x, y - 1, rows, cols, v + 1))
        return paths


def solution_day10(data: list[str]) -> int:
    data = [[int(x) for x in line] for line in data]
    rows = len(data)
    cols = len(data[0])

    total = 0
    for y in range(rows):
        for x in range(cols):
            if data[y][x] == 0:
                res = count_paths(data, x, y, rows, cols, 0)
                total += len(res)
    return total


def count_paths_v2(data, x, y, rows, cols, v) -> int:
    if v == 9:
        return 1
    else:
        paths = 0
        if x + 1 < cols and data[y][x + 1] == v + 1:
            paths += count_paths_v2(data, x + 1, y, rows, cols, v + 1)
        if y + 1 < rows and data[y + 1][x] == v + 1:
            paths += count_paths_v2(data, x, y + 1, rows, cols, v + 1)
        if x - 1 >= 0 and data[y][x - 1] == v + 1:
            paths += count_paths_v2(data, x - 1, y, rows, cols, v + 1)
        if y - 1 >= 0 and data[y - 1][x] == v + 1:
            paths += count_paths_v2(data, x, y - 1, rows, cols, v + 1)
        return paths

def solution_day10_part2(data: list[str]) -> int:
    data = [[int(x) for x in line] for line in data]
    rows = len(data)
    cols = len(data[0])

    total = 0
    for y in range(rows):
        for x in range(cols):
            if data[y][x] == 0:
                res = count_paths_v2(data, x, y, rows, cols, 0)
                total += res
    return total