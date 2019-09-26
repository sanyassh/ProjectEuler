import euler


ANSWER = 510510
LIMIT = 10 ** 6


def main():
    totient = euler.totient_list(LIMIT + 1)
    lst = [0] + [i / totient[i] for i in range(1, LIMIT + 1)]
    return lst.index(max(lst))


if __name__ == '__main__':
    print(main())
