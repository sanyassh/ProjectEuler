ANSWER = 4782
LIMIT = 1000


def main():
    a, b, i = 1, 1, 2
    while b < 10 ** (LIMIT - 1):
        a, b, i = b, a + b, i + 1
    return i


if __name__ == '__main__':
    print(main())
