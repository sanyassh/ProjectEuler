import euler


ANSWER = 173
LIMIT = 10 ** 6


def main():
    return sum(
        euler.miller_rabin(3 * i * i + 3 * i + 1)
        for i in range(1, int((LIMIT // 3) ** 0.5))
    )


if __name__ == '__main__':
    print(main())
