import euler

ANSWER = 260324


def iterate(lst, way, n):
    length = len(way)
    for _ in range(length):
        way[0][n] = min(way[0][n - 1], way[1][n]) + lst[0][n]
        for i in range(1, length - 1):
            way[i][n] = min(
                way[i - 1][n], way[i][n - 1], way[i + 1][n]
            ) + lst[i][n]
        way[length - 1][n] = min(
            way[length - 2][n], way[length - 1][n - 1]
        ) + lst[length - 1][n]


def main():
    lst = [
        [int(i) for i in line[:-1].split(',')]
        for line in euler.data(__file__)
    ]
    length = len(lst)
    way = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        way[i][0] = lst[i][0]
    for i in range(1, length):
        for j in range(length):
            way[j][i] = way[j][i - 1] + lst[j][i]
        iterate(lst, way, i)
    return min(k[-1] for k in way)


if __name__ == '__main__':
    print(main())
