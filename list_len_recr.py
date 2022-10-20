def get_list_length(arr: list):
    return get_list_length_recr(arr, 0)


def get_list_length_recr(arr: list, length_counter: int):
    if not arr:
        return length_counter
    length_counter += 1
    arr.pop(0)
    return get_list_length_recr(arr, length_counter)
