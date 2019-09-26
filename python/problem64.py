ANSWER = 1322


def period(n):
    sqrt = n ** 0.5
    int_sqrt = int(sqrt)
    start = diff = -int_sqrt
    denom = 1
    length = 0
    while True:
        length += 1
        denom = (n - diff ** 2) // denom
        a = int((sqrt - diff) / denom)
        diff = -diff - a * denom
        if denom == 1 and diff == start:
            break
    return length


def main():
    squares = [i*i for i in range(101)]
    not_squares = [i for i in range(1, 10001) if i not in squares]
    return sum(period(n) % 2 for n in not_squares)


if __name__ == '__main__':
    print(main())
