import euler


ANSWER = 142913828922
LIMIT = 2 * 10 ** 6


def main():
    return sum(euler.prime_list(LIMIT))


if __name__ == '__main__':
    print(main())
