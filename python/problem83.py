import math

import euler


ANSWER = 425185


def iterate(lst, way):
    length = len(lst)
    for i in range(1, length):
        way[0][i] = min(way[0][i - 1], way[1][i]) + lst[0][i]
        way[i][0] = min(way[i - 1][0], way[i][1]) + lst[i][0]
    for i in range(1, length - 1):
        for j in range(1, length - 1):
            way[i][j] = min(
                way[i - 1][j], way[i][j - 1], way[i + 1][j], way[i][j + 1]
            ) + lst[i][j]
    for i in range(1, length):
        way[i][length - 1] = min(
            way[i - 1][length - 1], way[i][length - 2]
        ) + lst[i][length - 1]
        way[length - 1][i] = min(
            way[length - 1][i - 1], way[length - 2][i]
        ) + lst[length - 1][i]


def main():
    lst = [
        [int(i) for i in line[:-1].split(',')]
        for line in euler.data(__file__)
    ]
    length = len(lst)
    way = [[math.inf for _ in range(length)] for _ in range(length)]
    way[0][0] = lst[0][0]
    for _ in range(length):
        iterate(lst, way)
    return way[length - 1][length - 1]


if __name__ == '__main__':
    print(main())
