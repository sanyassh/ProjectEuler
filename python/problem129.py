import itertools


ANSWER = 1000023
LIMIT = 10 ** 6


def find(n):
    rest = 1
    i = 1
    while rest:
        rest = (rest * 10 + 1) % n
        i += 1
    return i


def main():
    return next(
        n
        for n in itertools.count(LIMIT)
        if n % 2 and n % 5 and find(n) > LIMIT
    )


if __name__ == '__main__':
    print(main())
