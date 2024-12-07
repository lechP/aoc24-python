from collections import Counter


def read_two_lists_of_integers(lines: list[str]):
    first_list = []
    second_list = []
    for line in lines:
        first, second = line.split("   ")
        first_list.append(int(first))
        second_list.append(int(second))
    return first_list, second_list



def distance(list1: list[int], list2: list[int]):
    l1 = sorted(list1)
    l2 = sorted(list2)
    _distance = 0
    for i in range(len(list1)):
        _distance += abs(l1[i]-l2[i])
    return _distance

def solution_distance(lines: list[str]):
    list1, list2 = read_two_lists_of_integers(lines)
    return distance(list1, list2)


def solution_similarity(lines: list[str]):
    list1, list2 = read_two_lists_of_integers(lines)
    occurences1 = Counter(list1)
    occurences2 = Counter(list2)
    # for each number in occurences1 multiply it by its number of occurences and respective number of occurences on occurences2 or by 0
    _similarity_index = 0
    for _num in occurences1:
        _similarity_index += _num * occurences1[_num] * occurences2[_num]
    return _similarity_index
