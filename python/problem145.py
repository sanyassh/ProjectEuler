import functools


ANSWER = 608720
LIMIT = 9


@functools.lru_cache(maxsize=None)
def odd_less():
    return sum(
        1
        for i in range(10) for j in range(10)
        if (i + j) % 2 == 1 and i + j < 10
    )


@functools.lru_cache(maxsize=None)
def odd_less_without_zero():
    return sum(
        1
        for i in range(1, 10) for j in range(1, 10)
        if (i + j) % 2 == 1 and i + j < 10
    )


@functools.lru_cache(maxsize=None)
def odd_more():
    return sum(
        1
        for i in range(10) for j in range(10)
        if (i + j) % 2 == 1 and i + j >= 10
    )


@functools.lru_cache(maxsize=None)
def odd_more_without_zero():
    return sum(
        1
        for i in range(1, 10) for j in range(1, 10)
        if (i + j) % 2 == 1 and i + j >= 10
    )


@functools.lru_cache(maxsize=None)
def even_less():
    return sum(
        1
        for i in range(10) for j in range(10)
        if (i + j) % 2 == 0 and i + j < 10
    )


def reversible(digits):
    if digits % 2 == 0:
        return odd_less_without_zero() * odd_less() ** (digits // 2 - 1)
    if digits % 4 == 1:
        return 0
    return 5 * odd_more_without_zero() * (odd_more() * even_less()) ** (
        (digits - 3) // 4
    )


def main():
    return sum(reversible(digits) for digits in range(1, LIMIT + 1))


if __name__ == '__main__':
    print(main())
