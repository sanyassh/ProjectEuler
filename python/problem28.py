ANSWER = 669171001
LIMIT = 1001


def main():
    return round(2/3 * LIMIT ** 3 + 1/2 * LIMIT ** 2 + 4/3 * LIMIT - 3/2)


if __name__ == '__main__':
    print(main())
