def parse_input(data: str):
    rules, pages = data.split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    rules_dict = {}
    for rule in rules:
        key, value = rule
        key = int(key)
        value = int(value)
        if rules_dict.get(key):
            rules_dict[key].append(value)
        else:
            rules_dict[key] = [value]

    pages_lists = [list(map(int, line.split(","))) for line in pages.split("\n")]

    return rules_dict, pages_lists


def is_page_valid(rules_dict: dict[int, list[int]], page: list[int]):
    for i in range(len(page)):
        rules = rules_dict.get(page[i])
        if not rules:
            rules = []
        for n in page[i + 1:]:
            if n not in rules:
                return False

    return True


def sum_valid_pages(data: str):
    rules, pages = parse_input(data)
    _sum = 0
    for page in pages:
        if is_page_valid(rules, page):
            _sum += page[int((len(page) - 1) / 2)]
    return _sum

def sum_revalidated_pages(data: str):
    rules, pages = parse_input(data)
    _sum = 0
    invalid_pages = filter(lambda page: not is_page_valid(rules, page), pages)
    for invalid_page in invalid_pages:
        revalidated_page = revalidate(rules, invalid_page)
        _sum += revalidated_page[int((len(revalidated_page) - 1) / 2)]
    return _sum

def revalidate(rules_dict: dict[int, list[int]], page: list[int]) -> list[int]:
    i=0
    updated_page = page.copy()
    while i<len(updated_page):
        rules = rules_dict.get(updated_page[i])
        if not rules:
            rules = []
        in_rules = True
        j = i + 1
        while j < len(updated_page) and in_rules:
            if updated_page[j] not in rules:
                element = updated_page.pop(j)
                updated_page.insert(i, element)
                in_rules = False
            j += 1
        if in_rules:
            i += 1
    return updated_page