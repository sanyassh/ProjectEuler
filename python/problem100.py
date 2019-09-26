ANSWER = 756872327473
LIMIT = 10 ** 12

SQ2 = 2 ** 0.5


def main():
    for a in range(1, LIMIT):
        b = int(a / SQ2)
        if a * a - 2 * b * b == 1:
            if 2 * b * (a + b) > LIMIT:
                return (a + b) * a
        b = int(a * SQ2)
        if 2 * a * a - b * b == 1:
            if 2 * a * (a + b) > LIMIT:
                return (a + b) * b + 1
    return 0


if __name__ == '__main__':
    print(main())
