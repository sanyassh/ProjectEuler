import collections
import math

import euler


ANSWER = 3053105
LIMIT = 10 ** 6
SLOW = True


def main():
    powers_of_2 = [1]
    while powers_of_2[-1] < LIMIT // 2:
        powers_of_2.append(powers_of_2[-1] * 2)
    powers_of_3 = [1]
    while powers_of_3[-1] < LIMIT // 3:
        powers_of_3.append(powers_of_3[-1] * 3)
    matrix = [
        [n for n in (p2 * p3 for p3 in powers_of_3) if n < LIMIT]
        for p2 in powers_of_2
    ]
    prime_list = euler.prime_list(LIMIT)
    items = list(enumerate(matrix[0]))
    items.append((math.inf, 0))
    for i in range(1, len(matrix)):
        new_items = []
        for index, n in items:
            for j in range(min(index, len(matrix[i]))):
                new_n = n + matrix[i][j]
                if new_n > LIMIT:
                    break
                new_items.append((j, new_n))
        items += new_items
    d = collections.defaultdict(int)
    for _, n in items:
        d[n] += 1
    total = 0
    for prime in prime_list:
        if d[prime] == 1:
            total += prime
    return total


if __name__ == '__main__':
    print(main())
