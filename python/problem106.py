import itertools


ANSWER = 21384


def pairs(n):
    s = set()
    for i in range(4, n + 1, 2):
        for combination in itertools.combinations(range(1, n + 1), i):
            for part1 in itertools.combinations(combination, i // 2):
                part2 = tuple(n for n in combination if n not in part1)
                if part1 > part2:
                    part1, part2 = part2, part1
                s.add((part1, part2))
    return s


def check(pair):
    return any(n > m for n, m in zip(*pair))


def main():
    return sum(check(pair) for pair in pairs(12))


if __name__ == '__main__':
    print(main())
