import euler


ANSWER = 95962097


PRIME_LIST = euler.prime_list(10 ** 4)


def hyper(a, b, c):
    if b == 1:
        return a % c
    if c == 2:
        return a % 2
    return pow(a, (hyper(a, b - 1, euler.totient(c, PRIME_LIST))), c)


def main():
    return hyper(1777, 1855, 10 ** 8)


if __name__ == '__main__':
    print(main())
