import euler


ANSWER = 7652413


def main():
    for prime in reversed(euler.prime_list(10 ** 7)):
        if euler.is_pandigital_1n(prime):
            return prime
    return 0


if __name__ == '__main__':
    print(main())
