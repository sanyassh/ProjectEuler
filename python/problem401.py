import euler


ANSWER = 281632621
LIMIT = 10 ** 15
MODULUS = 10 ** 9
SLOW = True


def sum_n_2(n):
    return n * (n + 1) * (2 * n + 1) // 6


def main():
    result = LIMIT
    sq = euler.int_sqrt(LIMIT)
    for n in range(2, sq + 1):
        n_1 = n - 1
        inv_n = LIMIT // n
        inv_n_1 = LIMIT // n_1
        result += inv_n * n ** 2 + n_1 * (sum_n_2(inv_n_1) - sum_n_2(inv_n))
    inv_sq = LIMIT // sq
    result += sq * (sum_n_2(inv_sq) - sum_n_2(sq))
    return result % MODULUS


if __name__ == '__main__':
    print(main())
