import euler


ANSWER = 983
LIMIT = 1000


def main():
    return next(
        prime
        for prime in reversed(euler.prime_list(LIMIT))
        if euler.prime_cycle_length(prime) == prime - 1
    )


if __name__ == '__main__':
    print(main())
