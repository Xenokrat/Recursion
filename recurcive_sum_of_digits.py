def calc_recr_sum_of_digits(number: int) -> int:
    if number < 10:
        return number

    last_digit = number % 10
    number_no_last_digit = number // 10
    return last_digit + calc_recr_sum_of_digits(number_no_last_digit)
