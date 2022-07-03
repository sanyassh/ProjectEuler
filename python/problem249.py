import collections

import euler


ANSWER = 9275262564250418
LIMIT = 5000
SLOW = True


def main():
    prime_list = euler.prime_list(LIMIT)
    ways = collections.defaultdict(int)
    ways[0] = 1
    for prime in prime_list:
        new_ways = ways.copy()
        for n in ways:
            new_ways[prime + n] += ways[n]
        ways = new_ways
    return sum(
        ways[prime] for prime in euler.prime_list(sum(prime_list) + 1)
    ) % 10 ** 16


if __name__ == '__main__':
    print(main())
