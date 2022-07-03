import euler


ANSWER = 1739023853137
LIMIT = 10 ** 8
LIMIT2 = LIMIT + 2
PRIME_LIST = euler.prime_list_with_zeros(LIMIT2)
SLOW = True


def check(n):
    sqrt = int(n ** 0.5) + 1
    for i in range(3, sqrt):
        if not n % i:
            if not PRIME_LIST[i + n // i]:
                return False
    return True


def main():
    total = 1
    for i in range(2, LIMIT // 2 + 3):
        q = 2 * i - 4
        if PRIME_LIST[i]:
            if PRIME_LIST[q + 1]:
                if check(q):
                    total += q
    return total


if __name__ == '__main__':
    print(main())
