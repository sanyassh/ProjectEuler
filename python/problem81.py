import euler

ANSWER = 427337


def main():
    lst = [
        [int(i) for i in line[:-1].split(',')]
        for line in euler.data(__file__)
    ]
    length = len(lst)
    way = [[0 for _ in range(length)] for _ in range(length)]
    way[0][0] = lst[0][0]
    for i in range(1, length):
        way[0][i] = way[0][i - 1] + lst[0][i]
        way[i][0] = way[i - 1][0] + lst[i][0]
    for i in range(1, length):
        for j in range(1, length):
            way[i][j] = min(way[i - 1][j], way[i][j - 1]) + lst[i][j]
    return way[length - 1][length - 1]


if __name__ == '__main__':
    print(main())
