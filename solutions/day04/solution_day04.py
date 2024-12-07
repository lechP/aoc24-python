def count_xmas(input: list[str]):
    rows = len(input)
    cols = len(input[0])

    found = 0

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "X":
                found = (found +
                         count_forward(input, i, j, rows, cols) +
                         count_backward(input, i, j, rows, cols) +
                         count_up(input, i, j, rows, cols) +
                         count_down(input, i, j, rows, cols) +
                         count_up_left(input, i, j, rows, cols) +
                         count_up_right(input, i, j, rows, cols) +
                         count_down_left(input, i, j, rows, cols) +
                         count_down_right(input, i, j, rows, cols))

    return found


def count_forward(input: list[str], i: int, j: int, rows: int, cols: int):
    if j + 3 < cols:
        if input[i][j + 1] == "M" and input[i][j + 2] == "A" and input[i][j + 3] == "S":
            return 1
    return 0


def count_backward(input: list[str], i: int, j: int, rows: int, cols: int):
    if j - 3 >= 0:
        if input[i][j - 1] == "M" and input[i][j - 2] == "A" and input[i][j - 3] == "S":
            return 1
    return 0


def count_up(input: list[str], i: int, j: int, rows: int, cols: int):
    if i - 3 >= 0:
        if input[i - 1][j] == "M" and input[i - 2][j] == "A" and input[i - 3][j] == "S":
            return 1
    return 0


def count_down(input: list[str], i: int, j: int, rows: int, cols: int):
    if i + 3 < rows:
        if input[i + 1][j] == "M" and input[i + 2][j] == "A" and input[i + 3][j] == "S":
            return 1
    return 0


def count_up_left(input: list[str], i: int, j: int, rows: int, cols: int):
    if i - 3 >= 0 and j - 3 >= 0:
        if input[i - 1][j - 1] == "M" and input[i - 2][j - 2] == "A" and input[i - 3][j - 3] == "S":
            return 1
    return 0


def count_up_right(input: list[str], i: int, j: int, rows: int, cols: int):
    if i - 3 >= 0 and j + 3 < cols:
        if input[i - 1][j + 1] == "M" and input[i - 2][j + 2] == "A" and input[i - 3][j + 3] == "S":
            return 1
    return 0


def count_down_left(input: list[str], i: int, j: int, rows: int, cols: int):
    if i + 3 < rows and j - 3 >= 0:
        if input[i + 1][j - 1] == "M" and input[i + 2][j - 2] == "A" and input[i + 3][j - 3] == "S":
            return 1
    return 0


def count_down_right(input: list[str], i: int, j: int, rows: int, cols: int):
    if i + 3 < rows and j + 3 < cols:
        if input[i + 1][j + 1] == "M" and input[i + 2][j + 2] == "A" and input[i + 3][j + 3] == "S":
            return 1
    return 0



def count_mas_cross(input: list[str]):
    rows = len(input)
    cols = len(input[0])

    found = 0

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "A":
                if is_mas_cross(input, i, j, rows, cols):
                    found += 1

    return found


def is_mas_cross(input: list[str], i: int, j: int, rows: int, cols: int):
    if i - 1 >= 0 and i + 1 < rows and j - 1 >= 0 and j + 1 < cols:
        if input[i - 1][j - 1] == "M" and input[i + 1][j + 1] == "S" and input[i - 1][j + 1] == "M" and input[i + 1][j - 1] == "S":
            return True
        if input[i - 1][j - 1] == "S" and input[i + 1][j + 1] == "M" and input[i - 1][j + 1] == "S" and input[i + 1][j - 1] == "M":
            return True
        if input[i - 1][j - 1] == "M" and input[i + 1][j + 1] == "S" and input[i - 1][j + 1] == "S" and input[i + 1][j - 1] == "M":
            return True
        if input[i - 1][j - 1] == "S" and input[i + 1][j + 1] == "M" and input[i - 1][j + 1] == "M" and input[i + 1][j - 1] == "S":
            return True
    return False