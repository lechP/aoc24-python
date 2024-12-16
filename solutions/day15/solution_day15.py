def split_input(data: str):
    grid, steps = data.split("\n\n")
    grid = grid.split("\n")
    steps = steps.replace("\n","")
    return grid, steps

def parse_input(data: str):
    grid, steps = split_input(data)

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

def parse_input_v2(data: str):
    grid, steps = split_input(data)

    objects = {}
    botpos = None

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == box:
                objects[(i, 2*j)] = box_l
                objects[(i, 2*j+1)] = box_r
            elif grid[i][j] == wall:
                objects[(i, 2*j)] = wall
                objects[(i, 2*j+1)] = wall
            elif grid[i][j] == bot:
                botpos = (i, 2*j)

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

    return count_gps(objects, box)

def count_gps(objects: dict[tuple[int, int], str], shape: str) -> int:
    _sum = 0
    for (i, j) in objects:
        if objects[(i, j)] == shape:
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
    objects, botpos, steps = parse_input_v2(data)
    print_grid(objects, botpos)

    for step in steps:
        move = directions[step]
        newpos = (botpos[0] + move[0], botpos[1] + move[1])
        if newpos in objects:
            if move[0] == 0: # horizontal move ; easier case
                no_walls = True
                objnewpos = newpos
                to_shift = {}
                while objnewpos in objects and no_walls:
                    if objects[objnewpos] == wall:
                        no_walls = False
                    obj = objects[objnewpos]
                    objnewpos = (objnewpos[0], objnewpos[1] + move[1])
                    to_shift[objnewpos] = obj
                if no_walls:
                    botpos = newpos
                    for pos in to_shift: # remove the boxes from the previous positions
                        prev_pos = (pos[0], pos[1] - move[1])
                        objects.pop(prev_pos)
                    for pos in to_shift: # add the boxes to the new positions
                        objects[pos] = to_shift[pos]
            else: # vertical move ; more obstacles possible
                no_walls = True
                any_objects = True
                current_level = newpos[0]
                to_shift = { # dictionary: level -> dict: position -> object
                    newpos[0]: {newpos: bot}
                }
                while any_objects and no_walls:
                    current_objects = to_shift[current_level]
                    next_objects = {}
                    for co in current_objects:
                        next_pos = co
                        if next_pos in objects:
                            if objects[next_pos] == box_l:
                                next_objects[(next_pos[0]+move[0], next_pos[1])] = box_l
                                next_objects[(next_pos[0]+move[0], next_pos[1]+1)] = box_r
                            elif objects[next_pos] == box_r:
                                next_objects[(next_pos[0]+move[0], next_pos[1])] = box_r
                                next_objects[(next_pos[0]+move[0], next_pos[1]-1)] = box_l
                            elif objects[next_pos] == wall:
                                no_walls = False
                    if next_objects == {}:
                        any_objects = False
                    current_level += move[0]
                    to_shift[current_level] = next_objects

                if no_walls: # if there are no walls, move the bot and the boxes
                    botpos = newpos
                    to_shift.pop(newpos[0]) # do not include bot in the shifting

                    for level in to_shift: # remove the boxes from the previous positions
                        for pos in to_shift[level]:
                            prev_pos = (pos[0] - move[0], pos[1])
                            objects.pop(prev_pos)

                    for level in to_shift: # add the boxes to the new positions
                        for pos in to_shift[level]:
                            objects[pos] = to_shift[level][pos]
        else:
            botpos = newpos

    return count_gps(objects, box_l)
