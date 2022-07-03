import itertools

import euler


ANSWER = 13938


def except_one(lst):
    return [lst[:i] + lst[i + 1:] for i in range(len(lst))]


def main():
    matrix = [
        [int(n) for n in line.split()]
        for line in euler.data(__file__)
    ]
    length = len(matrix)
    indices = [[] for _ in range(length)]
    indices[0] = [(i,) for i in range(length)]
    sums = [[] for _ in range(length)]
    sums[0] = [matrix[0][i] for i in range(length)]
    for i in range(1, length):
        indices[i] = list(itertools.combinations(range(length), i + 1))
        sums[i] = [0 for _ in indices[i]]
    for i in range(1, length):
        for j in range(len(indices[i])):
            last_indices = except_one(indices[i][j])
            sums[i][j] = max(
                (
                    sums[i - 1][indices[i - 1].index(last_index)] +
                    matrix[i][indices[i][j][k]]
                )
                for k, last_index in enumerate(last_indices)
            )
    return sums[length - 1][0]


if __name__ == '__main__':
    print(main())
