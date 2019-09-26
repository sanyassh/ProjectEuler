import itertools

import euler


ANSWER = 149253
LIMIT = 25


def find(n):
    rest = 1
    i = 1
    while rest:
        rest = (rest * 10 + 1) % n
        i += 1
    return i


def main():
    total = 0
    i = 0
    for n in itertools.count(4):
        if (
                n & 1 and
                n % 5 and
                not euler.miller_rabin(n) and
                not (n - 1) % find(n)
        ):
            i += 1
            total += n
            if i == LIMIT:
                break
    return total


if __name__ == '__main__':
    print(main())
