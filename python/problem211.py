import array

import euler


ANSWER = 1922364685
LIMIT = 64 * 10 ** 6
SLOW = True


def main():
    lst = array.array('Q', (1 for _ in range(LIMIT)))
    lst[0] = 0
    for i in range(2, LIMIT):
        square = i * i
        for j in range(i, LIMIT, i):
            lst[j] += square
    return sum(i for i, n in enumerate(lst) if euler.is_square(n))


if __name__ == '__main__':
    print(main())
