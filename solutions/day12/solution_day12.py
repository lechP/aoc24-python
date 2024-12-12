plants_to_visit = {}


def get_regions(data: list[str]) -> list[list[tuple[int, int]]]:
    regions = []
    for i in range(len(data)):
        for j, plant in enumerate(data[i]):
            plants_to_visit[(i, j)] = plant

    while len(plants_to_visit.items()) > 0:
        plant = plants_to_visit.popitem()
        regions.append(get_region(plant[0], plant[1]))

    return regions


def get_region(pos: tuple[int, int], kind: str) -> list[tuple[int, int]]:
    region = [pos]
    for d in dirs(pos):
        if plants_to_visit.get(d) == kind:
            next_plant = plants_to_visit.pop(d)
            region += get_region(d, next_plant)
    return region


def price(region: list[tuple[int, int]]) -> int:
    area = len(region)
    perimeter = 0
    for position in region:
        for d in dirs(position):
            if d not in region:
                perimeter += 1
    return area * perimeter


def dirs(position: tuple[int, int]) -> list[tuple[int, int]]:
    up = (position[0] - 1, position[1])
    down = (position[0] + 1, position[1])
    right = (position[0], position[1] + 1)
    left = (position[0], position[1] - 1)
    return [up, down, right, left]


def solution_day12(data) -> int:
    regions = get_regions(data)
    return sum([price(region) for region in regions])


def solution_day12_part2(data) -> int:
    return 0
