from collections import defaultdict
from itertools import combinations


def solution_day08(data: list[str]) -> int:
    antennas, rows, cols = get_antennas(data)

    antinodes = set()

    for ants in antennas.values():
        # get all pairs of antennas
        pairs = list(combinations(ants, 2))
        for p in pairs:
            p1, p2 = p
            x1, y1 = p1
            x2, y2 = p2
            y_dist = y2 - y1
            x_dist = x2 - x1
            if 0 <= y1 - y_dist < rows and 0 <= x1 - x_dist < cols:
                antinodes.add((y1 - y_dist, x1 - x_dist))
            if 0 <= y2 + y_dist < rows and 0 <= x2 + x_dist < cols:
                antinodes.add((y2 + y_dist, x2 + x_dist))

    return len(antinodes)


def get_antennas(data: list[str]) -> tuple[dict[str, list[tuple[int, int]]], int, int]:
    data = [[x for x in line] for line in data]
    rows = len(data)
    cols = len(data[0])

    antennas = defaultdict(list)
    for y in range(rows):
        for x in range(cols):
            ch = data[y][x]
            if ch != '.':
                antennas[ch].append((x, y))
    return antennas, rows, cols


def solution_day08_part2(data: list[str]) -> int:
    antennas, rows, cols = get_antennas(data)

    antinodes = set()

    for ants in antennas.values():
        # get all pairs of antennas
        pairs = list(combinations(ants, 2))
        for p in pairs:
            p1, p2 = p
            antinodes.add(p1)
            antinodes.add(p2)
            x1, y1 = p1
            x2, y2 = p2
            y_dist = y2 - y1
            x_dist = x2 - x1

            yl = y1 - y_dist
            xl = x1 - x_dist
            while 0 <= xl < rows and 0 <= yl < cols:
                antinodes.add((xl, yl))
                yl -= y_dist
                xl -= x_dist

            yr = y2 + y_dist
            xr = x2 + x_dist
            while 0 <= xr < rows and 0 <= yr < cols:
                antinodes.add((xr, yr))
                yr += y_dist
                xr += x_dist

    return len(antinodes)