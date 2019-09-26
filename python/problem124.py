import euler


ANSWER = 21417
LIMIT = 100000
INDEX = 10000


def main():
    lst = [[1, n] for n in range(LIMIT + 1)]
    for prime in euler.prime_list(LIMIT + 1):
        for i in range(prime, LIMIT + 1, prime):
            lst[i][0] *= prime
    return lst.index(sorted(lst)[INDEX])


if __name__ == '__main__':
    print(main())
