ANSWER = 4613732
LIMIT = 4 * 10 ** 6


def main():
    fib1, fib2, total = 1, 1, 0
    while fib2 < LIMIT:
        fib1, fib2, total = fib2, fib1 + fib2, total + fib2 * (fib2 % 2 == 0)
    return total


if __name__ == '__main__':
    print(main())
