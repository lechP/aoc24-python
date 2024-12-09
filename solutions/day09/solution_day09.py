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