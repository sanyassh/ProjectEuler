import itertools


ANSWER = 2783915460
LIMIT = 10 ** 6


def main():
    for i, permutation in enumerate(itertools.permutations(range(10)), start=1):
        if i == LIMIT:
            return int(''.join(str(digit) for digit in permutation))
    return 0


if __name__ == '__main__':
    print(main())
