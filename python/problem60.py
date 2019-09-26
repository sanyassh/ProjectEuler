import functools

import euler


ANSWER = 26033
COUNT = 5
COUNT1 = COUNT - 1
LIMIT = 10 ** 7
SLOW = True


@functools.lru_cache(maxsize=None)
def check(a, b):
    return euler.miller_rabin(int(a + b)) and euler.miller_rabin(int(b + a))


def main():
    prime_list = euler.prime_list(LIMIT)
    prime_list.remove(2)
    prime_list.remove(5)
    str_prime_list = [str(n) for n in prime_list]
    sets = {}
    minimum = LIMIT * COUNT
    for prime in str_prime_list:
        int_prime = int(prime)
        if int_prime >= minimum:
            break
        for lowest, rest in list(sets.items()):
            int_lowest = int(lowest)
            if int_lowest + int_prime >= minimum:
                sets.pop(lowest)
            elif not check(prime, lowest):
                continue
            for lst in rest.copy():
                if (
                        sum(int(n) for n in lst) + int_lowest + int_prime
                ) >= minimum:
                    rest.remove(lst)
                elif all(check(prime, n) for n in lst):
                    rest.append(lst.copy())
                    lst.append(prime)
                    if len(lst) == COUNT1:
                        minimum = min(
                            minimum, sum(int(n) for n in lst) + int_lowest
                        )
                        rest.remove(lst)
            rest.append([prime])
        if int_prime < minimum // COUNT:
            sets[prime] = []
    return minimum


if __name__ == '__main__':
    print(main())
