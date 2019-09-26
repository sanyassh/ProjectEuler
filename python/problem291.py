import euler


ANSWER = 4037526
LIMIT = 5 * 10 ** 15


def main():
    return sum(
        1
        for n in range(1, (int((LIMIT / 2) ** 0.5)))
        if euler.miller_rabin(2 * n * n + 2 * n + 1)
    )


if __name__ == '__main__':
    print(main())
