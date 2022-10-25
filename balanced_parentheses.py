from typing import List


def gen_balanced_parenth(open_par_num: int) -> List[str]:
    if open_par_num == 0:
        return ['']

    result = []
    for i in range(open_par_num):
        for left in gen_balanced_parenth(i):
            for right in gen_balanced_parenth(open_par_num - 1 - i):
                result.append('(' + left + ')' + right)

    return result

