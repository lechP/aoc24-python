# parse following input into values a,b,c and list of instructions:
# Register A: 729
# Register B: 0
# Register C: 0
#
# Program: 0,1,5,4,3,0
def parse_input(data: str):
    lines = data.split("\n")
    a = int(lines[0].split(" ")[-1])
    b = int(lines[1].split(" ")[-1])
    c = int(lines[2].split(" ")[-1])
    instructions = list(map(int, lines[4].split(" ")[1].split(",")))
    return a, b, c, instructions


# returns tuple of 5 values: a, b, c, nex_index, output or none
def process_instruction(opcode: int, operand: int, index: int, a: int, b: int, c: int) -> tuple[int, int, int, int, any]:
    next_index = index + 2
    if opcode == 0:
        # The adv instruction (opcode 0) performs division.
        # The numerator is the value in the A register.
        # The denominator is found by raising 2 to the power of the instruction's combo operand.
        # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
        # The result of the division operation is truncated to an integer and then written to the A register.
        result = a // (2 ** combo_value(operand, a, b, c))
        return result, b, c, next_index, None
    elif opcode == 1:
        # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
        result = b ^ operand
        return a, result, c, next_index, None
    elif opcode == 2:
        # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
        result = combo_value(operand, a, b, c) % 8
        return a, result, c, next_index, None
    elif opcode == 3:
        # The jnz instruction (opcode 3) does nothing if the A register is 0.
        # However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand;
        # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        if a == 0:
            return a, b, c, next_index, None
        else:
            return a, b, c, operand, None
    elif opcode == 4:
        # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B.
        # (For legacy reasons, this instruction reads an operand but ignores it.)
        return a, b ^ c, c, next_index, None
    elif opcode == 5:
        # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value.
        # (If a program outputs multiple values, they are separated by commas.)
        return a, b, c, next_index, combo_value(operand, a, b, c) % 8
    elif opcode == 6:
        # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register.
        # (The numerator is still read from the A register.)
        result = a // (2 ** combo_value(operand, a, b, c))
        return a, result, c, next_index, None
    elif opcode == 7:
        # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register.
        # (The numerator is still read from the A register.)
        result = a // (2 ** combo_value(operand, a, b, c))
        return a, b, result, next_index, None


def combo_value(operand: int, a: int, b: int, c: int) -> int:
    if operand <=3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        raise ValueError(f"Invalid operand value: {operand}")


def solution_day17(data) -> str:
    a, b, c, instructions = parse_input(data)
    index = 0
    outputs = []
    while index < len(instructions):
        opcode = instructions[index]
        operand = instructions[index + 1]
        a, b, c, index, output = process_instruction(opcode, operand, index, a, b, c)
        if output is not None:
            outputs.append(output)
    # return comma separated outputs
    return ",".join(map(str, outputs))



def solution_day17_part2(data) -> int:
    return 0


example = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

solution_day17(example)
