def parse_line(line: str):
    result, operands = line.split(": ")
    operands = operands.split(" ")
    return int(result), list(map(int, operands))


def total_calibration_result(data: list[str]):
    lines = list(map(parse_line, data))
    possible_lines = filter(lambda line: is_result_possible(*line), lines)
    return sum(map(lambda line: line[0], possible_lines))

# slow, takes ~35sec
def total_calibration_result_v2(data: list[str]):
    lines = list(map(parse_line, data))
    possible_lines = filter(lambda line: is_result_possible_v2(*line), lines)
    return sum(map(lambda line: line[0], possible_lines))

def is_result_possible(result: int, operands: list[int]):
    operators_count = 2 ** (len(operands) - 1)
    for i in range(operators_count):
        operators_binary = format(i, f"0{len(operands) - 1}b")
        if check_equation(result, operands, to_operators(operators_binary)):
            return True


def to_operators(binary: str):
    return list(map(lambda x: "+" if x == "0" else "*", binary))


def check_equation(result: int, operands: list[int], operators: list[str]):
    if len(operands) != len(operators) + 1:
        raise Exception("Invalid equation")
    tmp_sum = operands[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            tmp_sum += operands[i + 1]
        elif operators[i] == "*":
            tmp_sum *= operands[i + 1]
        else:
            raise Exception("Invalid operator")
        if tmp_sum > result:
            return False

    return result == tmp_sum

def is_result_possible_v2(result: int, operands: list[int]):
    operators_count = 3 ** (len(operands) - 1)
    for i in range(operators_count):
        operators_ternary = append_zeros(to_ternary(i), len(operands) - 1)
        if check_equation_v2(result, operands, to_operators_v2(operators_ternary)):
            return True
    return False

def append_zeros(binary: str, length: int):
    return "0" * (length - len(binary)) + binary

def to_ternary(number):
    if number == 0:
        return "0"

    ternary_digits = []
    while number > 0:
        ternary_digits.append(str(number % 3))  # Append the remainder
        number //= 3  # Integer division by 3

    # Reverse the digits to get the correct order
    return ''.join(reversed(ternary_digits))

def to_operator_v2(binary: str):
    if binary == "0":
        return "+"
    elif binary == "1":
        return "*"
    else:
        return "||"

def to_operators_v2(binary: str):
    return list(map(to_operator_v2, binary))

def check_equation_v2(result: int, operands: list[int], operators: list[str]):
    if len(operands) != len(operators) + 1:
        raise Exception("Invalid equation")
    tmp_sum = operands[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            tmp_sum += operands[i + 1]
        elif operators[i] == "*":
            tmp_sum *= operands[i + 1]
        elif operators[i] == "||":
            tmp_sum = int(f"{tmp_sum}{operands[i + 1]}")
        else:
            raise Exception("Invalid operator")
        if tmp_sum > result:
            return False

    return result == tmp_sum
