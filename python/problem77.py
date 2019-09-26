import itertools

import euler


ANSWER = 71
LIMIT = 5000


PRIME_LIST_WITH_ZEROS = euler.prime_list_with_zeros(LIMIT)
PRIME_LIST = euler.clean_zeros(PRIME_LIST_WITH_ZEROS)


def sum_two(n, index):
    result = 0
    prime = PRIME_LIST[index]
    n_2 = n // 2
    while prime <= n_2:
        if PRIME_LIST_WITH_ZEROS[n - prime]:
            result += 1
        index += 1
        prime = PRIME_LIST[index]
    return result


def sum_count(n, count, index=0):
    if n < count * 2:
        return 0
    if count == 2:
        return sum_two(n, index)
    prime = PRIME_LIST[index]
    smallest = n // count
    result = 0
    while prime <= smallest:
        result += sum_count(n - prime, count - 1, index)
        index += 1
        prime = PRIME_LIST[index]
    return result


def sum_all(n):
    return sum((sum_count(n, count) for count in range(2, n // 2)))


def main():
    return next(n for n in itertools.count(2) if sum_all(n) > LIMIT)


if __name__ == '__main__':
    print(main())
