import euler


ANSWER = 661
LIMIT = 10 ** 3
LIMIT1 = LIMIT + 1


def main():
    squares = [i * i for i in range(40)]
    d_list = [i for i in range(LIMIT1) if i not in squares]
    length = len(d_list)
    x_list = [0 for _ in range(length)]
    y_list = [0 for _ in range(length)]
    for i in range(length):
        d = d_list[i]
        d_sqrt = d ** 0.5
        lst = euler.square_fraction(d, LIMIT1)
        for j in range(1, LIMIT1):
            x, y = euler.parse_fraction(lst[:j])
            if x / y < d_sqrt:
                x += 1
            if x * x - d * y * y == 1:
                x_list[i] = x
                y_list[i] = y
                break
    return d_list[x_list.index(max(x_list))]


if __name__ == '__main__':
    print(main())
