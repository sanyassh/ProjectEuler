import euler


ANSWER = 303963552391
LIMIT = 10 ** 6


def main():
    return sum(euler.totient_list(LIMIT + 1)) - 1


if __name__ == '__main__':
    print(main())
