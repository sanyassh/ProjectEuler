import euler


ANSWER = 40886


def sqrt_digit_sum(n):
    sqrt = int(n ** 0.5)
    while len(str(sqrt)) < 100:
        n *= 100
        sqrt *= 10
        while sqrt ** 2 < n:
            sqrt += 1
        sqrt -= 1
    return euler.digit_sum(sqrt)


def main():
    squares = [i ** 2 for i in range(1, 11)]
    total = 0
    for i in range(1, 101):
        if i not in squares:
            total += sqrt_digit_sum(i)
    return total


if __name__ == '__main__':
    print(main())
