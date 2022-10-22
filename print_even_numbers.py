from typing import List


def print_even_numbers(arr: List[int]) -> None:
    arr_length: int = len(arr)
    return print_even_numbers_recr(arr, 0, arr_length - 1)


def print_even_numbers_recr(arr: List[int], index: int, arr_length: int) -> None:
    if arr[index] % 2 == 0:
        print(arr[index], end=' ')

    if index >= arr_length:
        return None

    return print_even_numbers_recr(arr, index + 1, arr_length)

