import itertools

import euler


ANSWER = 785478606870985
LIMIT = 10 ** 16


def main():
    prime_list = euler.prime_list(100)
    total = 0
    for combination in itertools.combinations(prime_list, 4):
        maximum = combination[-1]
        lst = [
            prime
            for prime in prime_list
            if prime < maximum and prime not in combination
        ]
        product = euler.product(combination)
        total += euler.is_not_divisible(LIMIT // product, lst, len(lst))
    return total


if __name__ == '__main__':
    print(main())
