import math

import euler


ANSWER = 180180
PRIME_LIST = euler.prime_list(100)
LIMIT = 10 ** 3


def decisions(lst):
    result = 1
    for a in lst:
        if a == 0:
            break
        result *= (a << 1) | 1
    return (result >> 1) + 1


def number(lst):
    result = 1
    for i, power in enumerate(lst):
        if power == 0:
            break
        result *= PRIME_LIST[i] ** power
    return result


def new_arrays(lst):
    yield (lst[0] + 1,) + lst[1:]
    for i in range(1, len(lst)):
        if lst[i - 1] == 0:
            return
        if lst[i] < lst[i - 1]:
            yield lst[:i] + (lst[i] + 1,) + lst[i + 1:]


def main():
    result = math.inf
    lst = tuple(0 for _ in range(len(PRIME_LIST)))
    ars = {lst}
    while ars:
        new_ars = set()
        for lst in ars:
            n = number(lst)
            if n > result:
                continue
            if decisions(lst) > LIMIT:
                result = n
            new_ars.update(new_arrays(lst))
        ars = new_ars
    return result


if __name__ == '__main__':
    print(main())
