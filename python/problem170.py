import itertools

import euler


ANSWER = 9857164023
DIVISORS_DICT = {}
SLOW = True


def number(permutation):
    result = 0
    for digit in permutation:
        result = result * 10 + digit
    return result


def is_pandigital(a, b, n):
    str_abn = str(a) + str(b) + str(n)
    return len(str_abn) == len(set(str_abn)) == 10


def divisors(num):
    if num not in DIVISORS_DICT:
        DIVISORS_DICT[num] = euler.divisors(num)
    return DIVISORS_DICT[num]


def can_be_formed(permutation):
    for i in range(1, 10):
        if permutation[i] != 0:
            a, b = number(permutation[:i]), number(permutation[i:])
            div_a, div_b = divisors(a), divisors(b)
            intersection = div_a.intersection(div_b)
            intersection.discard(1)
            for n in intersection:
                a_n, b_n = a // n, b // n
                if is_pandigital(a_n, b_n, n):
                    return True
    return False


def main():
    return next(
        number(permutation)
        for permutation in itertools.permutations(reversed(range(10)))
        if can_be_formed(permutation)
    )


if __name__ == '__main__':
    print(main())
