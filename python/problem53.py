import euler


ANSWER = 4075
LIMIT = 10 ** 6


def main():
    return sum(
        (
            euler.FACTORIALS[n] /
            euler.FACTORIALS[r] /
            euler.FACTORIALS[n - r]
        ) > LIMIT
        for n in range(1, 101)
        for r in range(n + 1)
    )


if __name__ == '__main__':
    print(main())
