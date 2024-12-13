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
    region_set = set(region)
    for position in region_set:
        for d in dirs(position):
            if d not in region_set:
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
    regions = get_regions(data)
    return sum([price_v2(region) for region in regions])

def price_v2(region: list[tuple[int, int]]) -> int:
    area = len(region)
    sides = 0
    borders = []
    # build list of borders as tuples (inside, outside)
    region_set = set(region)
    for position in region:
        for d in dirs(position):
            if d not in region_set:
                borders.append((position, d))

    while len(borders) > 0:
        border = borders.pop()
        inside, outside = border
        dx = outside[0] - inside[0]
        dy = outside[1] - inside[1]
        # check neighbours in line (either x or y) and if they occur in borders, remove them
        if dx != 0:
            candidate_plus = ((inside[0], inside[1]+dx), (outside[0], outside[1]+dx))
            candidate_minus = ((inside[0], inside[1]-dx), (outside[0], outside[1]-dx))
            while candidate_plus in borders:
                borders.remove(candidate_plus)
                inside, outside = candidate_plus
                candidate_plus = ((inside[0], inside[1]+dx), (outside[0], outside[1]+dx))
            while candidate_minus in borders:
                borders.remove(candidate_minus)
                inside, outside = candidate_minus
                candidate_minus = ((inside[0], inside[1]-dx), (outside[0], outside[1]-dx))
        if dy != 0:
            candidate_plus = ((inside[0]+dy, inside[1]), (outside[0]+dy, outside[1]))
            candidate_minus = ((inside[0]-dy, inside[1]), (outside[0]-dy, outside[1]))
            while candidate_plus in borders:
                borders.remove(candidate_plus)
                inside, outside = candidate_plus
                candidate_plus = ((inside[0]+dy, inside[1]), (outside[0]+dy, outside[1]))
            while candidate_minus in borders:
                borders.remove(candidate_minus)
                inside, outside = candidate_minus
                candidate_minus = ((inside[0]-dy, inside[1]), (outside[0]-dy, outside[1]))
        # increase number of sides after removal of all "members" of the side
        sides += 1
    return area * sides