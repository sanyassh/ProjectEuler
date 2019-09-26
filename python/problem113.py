ANSWER = 51161058134250


POWER = 100


def main():
    increasing = [[1] for _ in range(9)]

    for i in range(1, POWER):
        for j in range(9):
            increasing[j].append(sum(increasing[n][i-1] for n in range(j, 9)))

    decreasing = [[1] for _ in range(9)]

    for i in range(1, POWER):
        for j in range(9):
            decreasing[j].append(1+sum(decreasing[n][i-1] for n in range(j+1)))

    total = 0
    for lst in increasing:
        total += sum(lst)
    for lst in decreasing:
        total += sum(lst)
    total -= 9 * POWER
    return total


if __name__ == '__main__':
    print(main())
