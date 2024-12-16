def parse_input(data: str):
    grid, steps = data.split("\n\n")
    grid = grid.split("\n")
    steps = steps.replace("\n","")

    objects = {}
    botpos = None

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in [box, wall]:
                objects[(i, j)] = grid[i][j]
            if grid[i][j] == bot:
                botpos = (i, j)

    return objects, botpos, steps

directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

wall = '#'
box = 'O'
box_l = '['
box_r = ']'
bot = '@'

def solution_day15(data) -> int:
    objects, botpos, steps = parse_input(data)
    for step in steps:
        move = directions[step]
        newpos = (botpos[0] + move[0], botpos[1] + move[1])
        if newpos in objects:
            objnewpos = newpos
            no_walls = True
            while objnewpos in objects and no_walls:
                if objects[objnewpos] == wall:
                    no_walls = False
                objnewpos = (objnewpos[0] + move[0], objnewpos[1] + move[1])
            if no_walls:
                botpos = newpos
                objects.pop(newpos)
                objects[objnewpos] = box
        else:
            botpos = newpos

    # print_grid(objects, botpos)

    return count_gps(objects)

def count_gps(objects: dict[tuple[int, int], str]) -> int:
    _sum = 0
    for (i, j) in objects:
        if objects[(i, j)] == box:
            _sum += 100*i + j
    return _sum

def print_grid(objects: dict[tuple[int, int], str], botpos: tuple[int, int]):
    rows = max(key[0] for key in objects.keys())
    cols = max(key[1] for key in objects.keys())

    for i in range(rows+1):
        for j in range(cols+1):
            if (i, j) in objects:
                print(objects[(i, j)], end="")
            elif (i, j) == botpos:
                print(bot, end="")
            else:
                print(".", end="")
        print()

def solution_day15_part2(data) -> int:
    return 0
