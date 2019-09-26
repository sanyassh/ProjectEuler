import math

import euler


ANSWER = 892371480
LIMIT = 15499 / 94744
PRIME_LIST = euler.prime_list(100)


def resilience(n):
    return euler.totient(n, PRIME_LIST) / (n - 1)


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
            new_ars.update(new_arrays(lst))
            if n > 1 and resilience(n) < LIMIT:
                result = n
        ars = new_ars
    return result


if __name__ == '__main__':
    print(main())
