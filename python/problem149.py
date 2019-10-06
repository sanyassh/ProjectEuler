import euler


ANSWER = 52852124


def extract_lists(matrix):
    length = len(matrix)
    for i in range(length):
        yield [matrix[i][j] for j in range(length)]
        yield [matrix[j][i] for j in range(length)]
        yield [matrix[i + j][j] for j in range(length - i)]
        yield [matrix[j][i + j] for j in range(length - i)]
        yield [matrix[length - j - 1][i + j] for j in range(length - i)]
        yield [matrix[length - i - j - 1][j] for j in range(length - i)]


def main():
    gen = euler.lagged_fibonacci_generator()
    matrix = [
        [next(gen) for _ in range(2000)] for _ in range(2000)
    ]
    return max(
        max_sum for _, _, max_sum in (
            euler.max_sum_sub_sequence(lst) for lst in extract_lists(matrix)
        )
    )


if __name__ == '__main__':
    print(main())
