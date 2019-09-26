import itertools

import euler


ANSWER = 1259187438574927161
LIMIT = 999966663333


def main():
    total = 0
    prime_list = euler.prime_list(int(LIMIT ** 0.5) + 100)
    for i, prime in enumerate(prime_list):
        upper_limit = (
            prime_list[i + 1] if i != len(prime_list) - 1 else prime
        ) ** 2
        lower_limit = (
            prime_list[i - 1] if i != 0 else prime
        ) ** 2
        for n in itertools.count(prime + 1):
            product = prime * n
            if product >= upper_limit or product >= LIMIT:
                break
            if n == prime_list[i + 1]:
                continue
            total += product
        for n in range(prime - 1, -1, -1):
            product = prime * n
            if product <= lower_limit:
                break
            if n == prime_list[i - 1] or product > LIMIT:
                continue
            total += product
    return total


if __name__ == '__main__':
    print(main())
