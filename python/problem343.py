import euler


ANSWER = 269533451410884183
LIMIT = 2 * 10 ** 6


def main():
    return sum(
        max(pair)
        for pair in zip(
            euler.max_divisors([n * n - n + 1 for n in range(1, LIMIT + 1)]),
            euler.max_divisors([n + 1 for n in range(1, LIMIT + 1)])
        )
    ) - LIMIT


if __name__ == '__main__':
    print(main())
