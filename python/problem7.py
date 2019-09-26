import euler


ANSWER = 104743
LIMIT = 10001


def main():
    return euler.prime_list(LIMIT * 100)[LIMIT - 1]


if __name__ == '__main__':
    print(main())
