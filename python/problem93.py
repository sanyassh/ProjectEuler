import itertools


ANSWER = 1258


def two_combination(a, b):
    if a != 0:
        if b != 0:
            return {a + b, a - b, a * b, a / b, b - a, b / a}
    return {a + b, a - b, a * b, b - a}


def three_combination(a, b, c):
    two_combinations = (
        two_combination(*pair)
        for pair in itertools.combinations((a, b, c), 2)
    )
    three = set()
    for combination, single in zip(
            two_combinations, (c, b, a)
    ):
        for n in combination:
            three.update(two_combination(n, single))
    return three


def four_combination(a, b, c, d):
    four = set()
    two_combinations = tuple(
        two_combination(*pair)
        for pair in itertools.combinations((a, b, c, d), 2)
    )
    for i in range(len(two_combinations) // 2):
        for comb1 in two_combinations[i]:
            for comb2 in two_combinations[-1 - i]:
                four.update(two_combination(comb1, comb2))
    three_combinations = (
        three_combination(*trio)
        for trio in itertools.combinations((a, b, c, d), 3)
    )
    for combination, single in zip(
            three_combinations, (d, c, b, a)
    ):
        for n in combination:
            four.update(two_combination(n, single))
    return four


def clean(s):
    return set(round(i) for i in s if i >= 0 and abs(i - round(i)) < 1e-3)


def result(a, b, c, d):
    return clean(four_combination(a, b, c, d))


def length(res):
    i = 1
    while i in res:
        i += 1
    return i - 1


def main():
    n = 0
    maximum = 0
    for i in range(3, 10):
        for j in range(i + 1, 10):
            leng = length(result(1, 2, i, j))
            if leng > maximum:
                n = 1200 + 10 * i + j
                maximum = leng
    return n


if __name__ == '__main__':
    print(main())
