import collections


ANSWER = 18522
LIMIT = 1000
BOUND = LIMIT * 20
HALF_BOUND = BOUND // 2


def cubes(a, b, c):
    abc_1 = a + b + c - 1
    double_sum_of_pairs = (a * b + a * c + b * c) << 1
    i = 0
    while True:
        value = double_sum_of_pairs + ((i * (abc_1 + i)) << 2)
        if value < BOUND:
            yield value
        else:
            return
        i += 1


def main():
    counts = collections.defaultdict(int)
    for a in range(1, HALF_BOUND):
        for b in range(1, a + 1):
            if a * b >= HALF_BOUND:
                break
            for c in range(1, b + 1):
                for value in cubes(a, b, c):
                    counts[value] += 1
    return min(value for value, count in counts.items() if count == LIMIT)


if __name__ == '__main__':
    print(main())
