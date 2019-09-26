import itertools

import euler


ANSWER = 2209
LIMIT = 10 ** 9
PRIME_LIST = euler.prime_list(30)


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
        yield lst[:i] + (lst[i] + 1,) + lst[i + 1:]


def pseudo_fortunate_number(n):
    return next(
        2 + i
        for i in itertools.count()
        if euler.miller_rabin(n + 2 + i)
    )


def main():
    distinct_numbers = set()
    lst = tuple(0 for _ in range(len(PRIME_LIST)))
    ars = {lst}
    while ars:
        new_ars = set()
        for lst in ars:
            n = number(lst)
            if n > LIMIT:
                continue
            if n != 1:
                distinct_numbers.add(pseudo_fortunate_number(n))
            new_ars.update(new_arrays(lst))
        ars = new_ars
    return sum(distinct_numbers)


if __name__ == '__main__':
    print(main())
