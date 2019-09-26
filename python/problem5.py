import math

import euler


ANSWER = 232792560
LIMIT = 20


def main():
    return euler.product(
        prime ** int(math.log(LIMIT, prime))
        for prime in euler.prime_list(LIMIT + 1)
    )


if __name__ == '__main__':
    print(main())
