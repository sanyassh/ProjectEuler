import collections


ANSWER = 209566
LIMIT = 10 ** 6


def main():
    used = collections.defaultdict(int)
    squares = [i ** 2 for i in range(LIMIT // 4 + 2)]
    for i in range(3, LIMIT // 4 + 2):
        for j in range(i - 2, 0, -2):
            if squares[i] - squares[j] <= LIMIT:
                used[squares[i] - squares[j]] += 1
            else:
                break
    return sum(1 for use in used.values() if use <= 10)


if __name__ == '__main__':
    print(main())
