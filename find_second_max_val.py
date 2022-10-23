def find_second_max_val(arr: list):
    # считаем, что у списка изначально нет second_max
    # если он из одного элемента
    if len(arr) < 2:
        return None

    first_max = arr[0]
    second_max = float('-inf')

    return find_second_max_recr(arr[1:], first_max, second_max)


def find_second_max_recr(arr, first_max, second_max):

    value = arr[0]

    if value > first_max:
        second_max = first_max
        first_max = value
    elif value > second_max:
        second_max = value

    if len(arr) < 2:
        return second_max

    return find_second_max_recr(arr[1:], first_max, second_max)

