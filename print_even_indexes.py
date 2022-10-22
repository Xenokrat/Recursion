def print_even_indexes(arr: list) -> None:
    arr_length: int = len(arr)
    return print_even_indexes_recr(arr, 0, arr_length)


def print_even_indexes_recr(arr: list, index: int, arr_length: int) -> None:
    if index < arr_length:
        if index % 2 == 0:
            print(arr[index], end=' ')

        return print_even_indexes_recr(arr, index + 1, arr_length)

