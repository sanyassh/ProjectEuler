import collections
import itertools

import euler


ANSWER = 121313


def i_masks(prime, i):
    str_prime = str(prime)
    str_i = str(i)
    count = str_prime.count(str_i)
    if count >= 3:
        for permutation in set(
                itertools.permutations(
                    [True for _ in range(3)] +
                    [False for _ in range(count - 3)]
                )
        ):
            j = 0
            mask = ''
            for symbol in str_prime:
                if symbol == str_i:
                    if permutation[j]:
                        mask += '*'
                    else:
                        mask += str_i
                    j += 1
                else:
                    mask += symbol
            yield mask


def all_masks(prime):
    for i in range(10):
        yield from i_masks(prime, i)


def main():
    prime_list = euler.prime_list(10 ** 6)
    masks = collections.defaultdict(int)
    for prime in prime_list:
        for mask in all_masks(prime):
            masks[mask] += 1
            if masks[mask] == 8:
                start = 1 if mask.startswith('*') else 0
                for i in range(start, 10):
                    n = int(mask.replace('*', str(i)))
                    if euler.miller_rabin(n):
                        return n
    return 0


if __name__ == '__main__':
    print(main())
