def count_checksum(data: str) -> int:
    _left = 0
    _right = len(data) - 1
    disc_index = 0
    checksum = 0

    file_right_size = int(data[_right])
    file_right_id = int(_right/2)
    file_right_reminder = file_right_size

    while _left < _right:
        file_left_size = int(data[_left])
        file_left_id = int(_left/2)
        space_left = int(data[_left + 1])
        for i in range(file_left_size):
            checksum += disc_index * file_left_id
            disc_index += 1
        for i in range(space_left):
            checksum += disc_index * file_right_id
            file_right_reminder -= 1
            if file_right_reminder == 0 and _right -2 <= _left:
                break
            if file_right_reminder == 0:
                _right -= 2
                file_right_size = int(data[_right])
                file_right_id = int(_right/2)
                file_right_reminder = file_right_size
            disc_index += 1
        _left += 2

    if file_right_reminder > 0:
        for i in range(file_right_reminder):
            checksum += disc_index * file_right_id
            disc_index += 1

    return checksum


def count_checksum_v2(data: str) -> int:
    disc_elements = []
    for i in range(len(data)):
        disc_elements.append(to_disc_element(int(data[i]), i))

    while True:
        file_id = last_unchecked_file_id(disc_elements)
        if file_id == -1:
            break
        else:
            size, element, checked, index = disc_elements[file_id]
            space_found = False
            for i in range(file_id):
                space = disc_elements[i]
                if space[1] == "s" and space[0] >= size:
                    disc_elements.pop(file_id)
                    disc_elements.insert(file_id, (size, "s", False, 0))
                    disc_elements.pop(i)
                    disc_elements.insert(i, (size, "f", True, index))
                    if space[0] > size:
                        disc_elements.insert(i+1, (space[0]-size, "s", False, 0))
                    space_found = True
                    break
            if not space_found:
                disc_elements[file_id] = (size, element, True, index)

    return calculate_checksum(disc_elements)


def calculate_checksum(disc_elements: list[tuple[int, str, bool, int]]) -> int:
    checksum = 0
    index_on_disc = 0
    for i in range(len(disc_elements)):
        size, element, checked, index = disc_elements[i]
        for j in range(size):
            if element == "f":
                checksum += index_on_disc*index
            index_on_disc += 1
    return checksum

def print_disc_elements(disc_elements: list[tuple[int, str, bool, int]]):
    printout = ""
    for i in range(len(disc_elements)):
        size, element, checked, index = disc_elements[i]
        if element == "f":
            printout += str(index)*size
        if element == "s":
            printout += "."*size
    print(printout)

def to_disc_element(size: int, index: int) -> tuple[int, str, bool, int]:
    if index%2==0:
        return size, "f", False, int(index/2)
    else:
        return size, "s", False, 0

def last_unchecked_file_id(disc_elements: list[tuple[int, str, bool, int]]) -> int:
    for i in range(len(disc_elements)-1, 0, -1):
        size, element, checked, index = disc_elements[i]
        if element == "f" and not checked:
            return i
    return -1