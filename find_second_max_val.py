from typing import List


def find_second_max_val(arr: List):
    # считаем, что у списка изначально нет second_max если он из одного элемента
    if len(arr) < 2:
        return None

    first_max = arr[0]
    second_max = float('-inf')

    return find_second_max_recr(arr, 1, first_max, second_max)


def find_second_max_recr(arr: List, index: int, first_max, second_max):

    if index >= len(arr):
        return second_max

    value = arr[index]

    if value > first_max:
        second_max = first_max
        first_max = value

    elif value > second_max:
        second_max = value

    return find_second_max_recr(arr, index + 1, first_max, second_max)

