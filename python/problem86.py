import euler


ANSWER = 1818


LIMIT = 10 ** 6


def shortest_path(a, b, c):
    return ((a + b) ** 2 + c ** 2) ** 0.5


def count_of_c(c, a_b):
    if a_b > c:
        if c < (a_b >> 1):
            return 0
        return c - ((a_b - 1) >> 1)
    return a_b >> 1


def main():
    pairs = []
    for a in range(1, 1000):
        for trio in euler.pythagorean_unique_trio(a):
            pairs.extend((trio[:2], trio[1::-1]))
    pairs.sort()
    count = 0
    c = 0
    while True:
        c += 1
        for pair in pairs:
            if pair[0] > c:
                break
            if c % pair[0] == 0:
                d = c // pair[0]
                count += count_of_c(c, pair[1] * d)
        if count > LIMIT:
            return c


if __name__ == '__main__':
    print(main())
