import re


def get_multiplies(string: str) -> list[str]:
    matches = re.finditer(r"mul\(\d+,\d+\)", string)
    return [match.group() for match in matches]


def eval_multiplier(string: str) -> int:
    matches = list(map(int, re.findall(r"\d+", string)))
    return matches[0] * matches[1]

def sum_multiplies(string: str) -> int:
    _mults = map(eval_multiplier, get_multiplies(string))
    return sum(_mults)


def sum_multiplies_v2(string: str) -> int:
    tokens = get_all_tokens(string)
    _mults = map(eval_multiplier, tokens)
    return sum(_mults)

def get_all_tokens(string: str) -> list[str]:
    matches =  re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", string)
    start_token = "do()"
    stop_token = "don't()"
    include = True
    tokens = []
    for match in matches:
        if match.group() == start_token:
            include = True
        elif match.group() == stop_token:
            include = False
        elif include:
            tokens.append(match.group())
    return tokens