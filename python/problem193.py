import euler


ANSWER = 684465067343069
POWER = 50


def main():
    squares = [p * p for p in euler.prime_list(2 ** (POWER // 2))]
    return euler.is_not_divisible(2 ** POWER, squares, len(squares))


if __name__ == '__main__':
    print(main())
