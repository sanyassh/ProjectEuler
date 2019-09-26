ANSWER = 14234


def is_rectangular(sq1, sq2, sq3):
    sq_sum = sq1 + sq2 + sq3
    for sqr in (sq1, sq2, sq3):
        if abs(sq_sum - 2 * sqr) < 1e-5:
            return True
    return False


def main():
    squares = [
        [x ** 2 + y ** 2 for y in range(51)]
        for x in range(51)
    ]
    return sum(
        is_rectangular(
            squares[x1][y1],
            squares[x2][y2],
            squares[abs(x1 - x2)][abs(y1 - y2)]
        )
        for x1 in range(51) for y1 in range(51)
        for x2 in range(51) for y2 in range(51)
        if (x1 or y1) and (x2 or y2) and (x1 != x2 or y1 != y2)
    ) // 2


if __name__ == '__main__':
    print(main())
