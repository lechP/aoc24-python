def parse_input(data: str) -> list[tuple[int, int]]:
    lines = data.split("\n")
    result = []
    for line in lines:
        ints = list(map(int, line.split(",")))
        result.append((ints[0], ints[1]))
    return result


def solution_day18(data: str, limit: int, size: int) -> int:
    fallen_bytes = set(parse_input(data)[:limit])
    print(size)

    draw_grid(fallen_bytes, size)
    return 0
    
def solution_day18_part2(data) -> int:
    return 0


def draw_grid(items: set[tuple[int, int]], size: int):
    for i in range(size):
        for j in range(size):
            if (j, i) in items:
                print("#", end="")
            else:
                print(".", end="")
        print()