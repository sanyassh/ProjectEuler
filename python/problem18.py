ANSWER = 1074


def main():
    lst = [
        [int(i) for i in l.split()]
        for l in open('../txt/problem018.txt')
    ]
    maximum = lst[0]
    for i in range(1, len(lst)):
        maximum = (
            [lst[i][0] + maximum[0]] +
            [
                lst[i][j] + max(maximum[j - 1], maximum[j])
                for j in range(1, i)
            ] +
            [lst[i][-1] + maximum[-1]]
        )
    return max(maximum)


if __name__ == '__main__':
    print(main())
