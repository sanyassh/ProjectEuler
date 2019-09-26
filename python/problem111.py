import itertools

import euler


ANSWER = 612407567715
LIMIT = 10
MASK = ['*' for _ in range(LIMIT)]


def s_func(digit):
    for m in range(LIMIT, -1, -1):
        result = 0
        for indices in itertools.combinations(range(LIMIT), m):
            mask = MASK.copy()
            for index in indices:
                mask[index] = digit
            for numbers in itertools.product(range(10), repeat=LIMIT - m):
                new_mask = mask.copy()
                for number in numbers:
                    new_mask[new_mask.index('*')] = number
                if new_mask[0] == 0 or new_mask.count(digit) != m:
                    continue
                n = 0
                for number in new_mask:
                    n = n * 10 + number
                if euler.miller_rabin(n):
                    result += n
        if result:
            return result
    return 0


def main():
    return sum(s_func(digit) for digit in range(10))


if __name__ == '__main__':
    print(main())
