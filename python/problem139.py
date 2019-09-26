ANSWER = 10057761
LIMIT = 100 * 10 ** 6


def main():
    total = 0
    a, b = 2, 1
    while True:
        perimeter = 2 * a * (a + b)
        if perimeter > LIMIT:
            break
        total += (LIMIT - 1) // perimeter
        a, b = 2 * a + b, a
    return total


if __name__ == '__main__':
    print(main())
