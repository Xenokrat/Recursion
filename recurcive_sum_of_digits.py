def calc_recr_sum_of_digits(number: int) -> int:
    if number < 10:
        return number
    return number % 10 + calc_recr_sum_of_digits(number // 10)
