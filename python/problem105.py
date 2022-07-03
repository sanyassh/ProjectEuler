import itertools

import euler


ANSWER = 73702


def check(s):
    prev_max = s[0]
    for i in range(2, len(s)):
        combination_sums = set()
        for comb in itertools.combinations(s, i):
            combination_sum = sum(comb)
            if combination_sum <= prev_max:
                return False
            if combination_sum in combination_sums:
                return False
            combination_sums.add(combination_sum)
        prev_max = max(combination_sums)
    return True


def main():
    lst = [
        sorted([int(n) for n in line.split(',')], reverse=True)
        for line in euler.data(__file__)
    ]
    total = 0
    for s in lst:
        if check(s):
            total += sum(s)
    return total


if __name__ == '__main__':
    print(main())
