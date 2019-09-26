import euler


ANSWER = 7295372
LIMIT = 12000


def fraction(n):
    total = 0
    divisors = euler.divisors(n)
    divisors.remove(1)
    for i in range(n // 3 + 1, (n + 1) // 2):
        for d in divisors:
            if i % d == 0:
                break
        else:
            total += 1
    return total


def main():
    return sum(fraction(i) for i in range(2, LIMIT + 1))


if __name__ == '__main__':
    print(main())
