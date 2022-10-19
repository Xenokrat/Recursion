def calc_recursive_power(number: int, power: int) -> int:
    assert (power > 0 and isinstance(power, int)), 'Агрумент power должен быть больше 0 и целым'
    if power == 1:
        return number
    return number * calc_recursive_power(number, power - 1)
