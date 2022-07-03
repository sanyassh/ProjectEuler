import euler


ANSWER = 2129970655314432
LIMIT = 10 ** 9


def not_divisible_by_7(n):
    if n < 7:
        return euler.triangular(n)
    result = 1
    tmp = 7
    while tmp <= n:
        tmp *= 7
        result *= 28
    tmp //= 7
    c = n // tmp
    return (
        result * euler.triangular(c) +
        (c + 1) * not_divisible_by_7(n - c * tmp)
    )


def main():
    return not_divisible_by_7(LIMIT)


if __name__ == '__main__':
    print(main())
