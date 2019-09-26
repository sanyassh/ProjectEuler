ANSWER = 1572729
LIMIT = 10 ** 6


def main():
    total = 0
    squares = [i ** 2 for i in range(LIMIT // 4 + 2)]
    for i in range(3, LIMIT // 4 + 2):
        for j in range(i - 2, 0, -2):
            if squares[i] - squares[j] <= LIMIT:
                total += 1
            else:
                break
    return total


if __name__ == '__main__':
    print(main())
