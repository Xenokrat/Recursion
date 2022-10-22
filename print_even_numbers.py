from typing import List


def print_even_numbers(arr: List[int]):
    arr_copy = arr[:]
    return print_even_numbers_recr(arr_copy)


def print_even_numbers_recr(arr_copy: List[int]):
    if not arr_copy:
        return None

    element: int = arr_copy.pop(0)
    if element % 2 == 0:
        print(element, end=' ')
    return print_even_numbers(arr_copy)

