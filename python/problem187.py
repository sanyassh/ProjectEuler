import array


ANSWER = 17427258
LIMIT = 10 ** 8


def prime_factors_count(n):
    lst = array.array('L', (0 for _ in range(n)))
    for i in range(2, n):
        if not lst[i]:
            power = i
            while power < n:
                for temp in range(power, n, power):
                    lst[temp] += 1
                power *= i
    return lst


def main():
    return prime_factors_count(LIMIT).count(2)


if __name__ == '__main__':
    print(main())
