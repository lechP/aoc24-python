def parse_input(data: str) -> tuple[dict[tuple[int, int], str], tuple[int, int], str, int]:
    lines = data.split("\n")
    cells = {}
    starting_point = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            cell = lines[i][j]
            if cell == '.' or cell == end:
                cells[(i, j)] = lines[i][j]
            elif cell == start:
                starting_point = (i, j)
    return cells, starting_point, '>', 0

def end_position(data: str) -> tuple[int, int]:
    lines = data.split("\n")
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == end:
                return i, j

start = 'S'
end = 'E'
directions = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

def next_states(left_cells: dict[tuple[int, int], str], current: tuple[int, int], direction: str, score: int) -> list[tuple[dict[tuple[int, int], str], tuple[int, int], str, int]]:
    next_ = []
    for d in directions:
        new_position = (current[0] + directions[d][0], current[1] + directions[d][1])
        if new_position in left_cells:
            new_cells = left_cells.copy()
            new_cells.pop(new_position)
            if direction != d:
                new_score = score + 1001
            else:
                new_score = score + 1
            next_.append((new_cells, new_position, d, new_score))
    return next_

def solution_day16(data) -> int:
    states_to_check = [parse_input(data)]
    end_pos = end_position(data)
    scores = set()
    while states_to_check:
        state = states_to_check.pop()
        print(f"Steps left: {len(state[0])}")
        next_candidates = next_states(*state)
        next_states_to_check = []
        for n in next_candidates:
            if n[1] == end_pos:
                scores.add(n[3])
            else:
                next_states_to_check.append(n)
        states_to_check.extend(next_states_to_check)

    return min(scores)
    
def solution_day16_part2(data) -> int:
    return 0
