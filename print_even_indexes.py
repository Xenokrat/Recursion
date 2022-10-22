def print_even_indexes(arr: list) -> None:
    arr_length: int = len(arr)
    return print_even_indexes_recr(arr, 0, arr_length - 1)


def print_even_indexes_recr(arr: list, index: int, arr_length: int) -> None:
    if index % 2 == 0:
        print(arr[index], end=' ')

    if index >= arr_length:
        return None

    return print_even_indexes_recr(arr, index + 1, arr_length)

