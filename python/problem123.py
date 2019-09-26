import euler


ANSWER = 21035
LIMIT = 10 ** 10


def main():
    return next(
        n
        for n, prime in enumerate(euler.prime_list(10 ** 6), 1)
        if n % 2 == 1 and 2 * prime * n % (prime * prime) > LIMIT
    )


if __name__ == '__main__':
    print(main())
