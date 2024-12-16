def parse_input(string: str):
    lines = string.splitlines()
    bonds = parse_xy(lines.pop(0))
    return bonds, list(map(parse_robot, lines))


def parse_robot(string: str):
    pos, vel = string.split(" ")
    pos = parse_xy(pos)
    vel = parse_xy(vel)
    return pos, vel


def parse_xy(string: str):
    return tuple(map(int, string.split("=")[1].split(",")))


def solution_day14(data) -> int:
    bonds, robots = parse_input(data)
    bx, by = bonds
    final_positions = []
    for robot in robots:
        pos, vel = robot
        final_positions.append(robot_final_pos(pos[0], pos[1], vel[0], vel[1], bx, by, 100))

    mid_x = bx // 2
    mid_y = by // 2
    q1, q2, q3, q4 = 0, 0, 0, 0
    for fp in final_positions:
        x, y = fp
        if x > mid_x and y > mid_y:
            q1 += 1
        elif x < mid_x and y > mid_y:
            q2 += 1
        elif x < mid_x and y < mid_y:
            q3 += 1
        elif x > mid_x and y < mid_y:
            q4 += 1

    return q1 * q2 * q3 * q4


def robot_final_pos(init_x: int, init_y: int, vel_x: int, vel_y: int, bond_x: int, bond_y: int, moves: int):
    final_x = (init_x + vel_x * moves) % bond_x
    final_y = (init_y + vel_y * moves) % bond_y
    return final_x, final_y


def robot_next_pos(init_x: int, init_y: int, vel_x: int, vel_y: int, bond_x: int, bond_y: int):
    next_x = (init_x + vel_x) % bond_x
    next_y = (init_y + vel_y) % bond_y
    return next_x, next_y

# 6512 - solution ugly as hell, but works
def solution_day14_part2(data) -> int:
    bonds, robots = parse_input(data)
    bx, by = bonds
    lim = 8000  # 22672
    fr = 6000
    for i in range(lim):
        new_robots = []
        positions = set()
        for robot in robots:
            pos, vel = robot
            next_pos = robot_next_pos(pos[0], pos[1], vel[0], vel[1], bx, by)
            new_robots.append((next_pos, vel))
            positions.add(next_pos)
        robots = new_robots
        if i > fr and is_christmas_tree_candidate(positions):
            print(f"------STEP {i}------")
            print()
            for x in range(bx):
                for y in range(by):
                    if (x, y) in positions:
                        print("#", end="")
                    else:
                        print(" ", end="")
                print()
            print("\n\n")

    return 0


def is_christmas_tree_candidate(positions: set[tuple[int, int]]) -> bool:
    # 25% triangle in top left corner is empty
    x34 = len(list(filter(lambda p: p[0] == 34, positions)))
    x64 = len(list(filter(lambda p: p[0] == 34, positions)))
    return x34 > 26 and x64 > 26
