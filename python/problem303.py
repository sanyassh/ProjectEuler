import array


ANSWER = 1111981904675169
POWER = 4
LIMIT = 10 ** POWER
SLOW = True


def main():
    lst = array.array('Q', (1, 2))
    s = set(range(1, LIMIT + 1))
    # important optimization, number for LIMIT - 1 is included in 'return' line
    s.discard(LIMIT - 1)
    total = 0
    while s:
        for k in s.copy():
            for n in lst:
                if not n % k:
                    s.discard(k)
                    total += n // k
                    break
        lst = array.array('Q', (n * 10 + i for n in lst for i in range(3)))
    return total + int('1' * POWER + '2' * POWER * 4) // (LIMIT - 1)


if __name__ == '__main__':
    print(main())
