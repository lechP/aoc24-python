def parse_input(data: str) -> tuple[dict[tuple[int, int], str], list[tuple[int, int]], tuple[int, int], str, int]:
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
    return cells, [starting_point], starting_point, '>', 0

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

def next_states(
        left_cells: dict[tuple[int, int], str],
        visited: list[tuple[int, int]],
        current: tuple[int, int],
        direction: str,
        score: int,
        tmp_scores: dict[tuple[tuple[int, int], str], int]
) -> list[tuple[dict[tuple[int, int], str], list[tuple[int, int]], tuple[int, int], str, int]]:
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

            if (new_position, d) in tmp_scores:
                if tmp_scores[(new_position, d)] >= new_score: #current path is better
                    tmp_scores[(new_position, d)] = new_score
                    next_.append((new_cells, visited.copy() + [new_position], new_position, d, new_score))
                # if path is worse than existing one, abandon it
            else:
                tmp_scores[(new_position, d)] = new_score
                next_.append((new_cells, visited.copy() + [new_position], new_position, d, new_score))
    return next_

# suboptimal - took ~7min, DFS would be better
def solution_day16(data, known_min_score = None) -> tuple[int, int]:
    states_to_check = [parse_input(data)]
    end_pos = end_position(data)
    min_score = known_min_score
    tmp_scores = {}
    visited_cells_on_min_paths = set()
    i=0
    while states_to_check:
        state = states_to_check.pop()
        i+=1
        print(f"Steps left: {len(state[0])}")
        if min_score is None or state[4] < min_score: # otherwise no need to check
            next_candidates = next_states(*state, tmp_scores)
            next_states_to_check = []
            for n in next_candidates:
                if n[2] == end_pos:
                    if min_score is None:
                        min_score = n[4]
                    else:
                        if n[4] <= min_score:
                            min_score = n[4]
                            visited_cells_on_min_paths.update(set(n[1]))
                else:
                    next_states_to_check.append(n)
            states_to_check.extend(next_states_to_check)
    print(f"States checked: {i}")
    return min_score, len(visited_cells_on_min_paths)

def solution_day16_part2(data) -> int:
    return 0
