import euler


ANSWER = 11762187201804552
LIMIT = 10 ** 8


def main():
    return (LIMIT * (LIMIT + 1) // 2 - sum(euler.totient_list(LIMIT + 1))) * 6


if __name__ == '__main__':
    print(main())
