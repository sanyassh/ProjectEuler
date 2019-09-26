import euler


ANSWER = 402
LIMIT = 10 ** 6


CHAIN = [0 for i in range(10 ** 7)]
CHAIN[1] = 1
CHAIN[2] = 1
CHAIN[145] = 1
CHAIN[40585] = 1
CHAIN[169] = CHAIN[363601] = CHAIN[1454] = 3
CHAIN[871] = CHAIN[45361] = 2
CHAIN[872] = CHAIN[45362] = 2


def get_next(n):
    return sum(euler.FACTORIALS[int(digit)] for digit in str(n))


def get_chain(n):
    if not CHAIN[n]:
        CHAIN[n] = get_chain(get_next(n)) + 1
    return CHAIN[n]


def main():
    return sum(get_chain(i) == 60 for i in range(3, LIMIT))


if __name__ == '__main__':
    print(main())
