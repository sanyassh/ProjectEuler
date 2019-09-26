import itertools


ANSWER = 20313839404245
SLOW = True


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


def build(n):
    if n < 5:
        s = tuple(range(n, 0, -1))
    else:
        b = build(n - 1)
        s = (b[0] + 1,) + b
        s = tuple(a + b[-1] // 2 for a in s)
    ars = {s}
    while True:
        new_ars = set()
        for s in ars:
            if check(s):
                return s
            add = True
            if n > 5:
                for i in range(1, n):
                    if s[i - 1] - s[i] >= s[-1]:
                        add = False
                        break
            if add:
                new_ars.add((s[0] + 1,) + s[1:])
                for i in range(1, n):
                    if s[i - 1] - s[i] > 1:
                        new_ars.add(s[:i] + (s[i] + 1,) + s[i + 1:])
        ars = new_ars


def main():
    return int(''.join(str(n) for n in sorted(build(7))))


if __name__ == '__main__':
    print(main())
