def get_list_length(arr: list) -> int:
    arr_copy = arr[:]  # Создадим копию листа, иначе pop удалит значения из изначального списка
    return get_list_length_recr(arr_copy, 0)


def get_list_length_recr(arr: list, length_counter: int):
    if not arr:
        return length_counter
    arr.pop(0)
    return get_list_length_recr(arr, length_counter + 1)
