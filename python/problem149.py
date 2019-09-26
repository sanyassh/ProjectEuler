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


def max_sum(lst):
    while 0 in lst:
        lst.remove(0)
    while lst:
        if lst[-1] <= 0:
            lst.pop()
        elif lst[0] <= 0:
            lst.pop(0)
        else:
            break
    i = 0
    while i < len(lst) - 1:
        if lst[i] * lst[i + 1] > 0:
            lst[i:i + 2] = [lst[i] + lst[i + 1]]
        else:
            i += 1
    if lst:
        result = 0
        while len(lst) > 1:
            result = max(result, lst[0])
            if lst[0] + lst[1] > 0:
                lst[2] += lst[0] + lst[1]
            lst[:2] = []
        result = max(result, lst[0])
        return result
    return 0


def main():
    gen = euler.lagged_fibonacci_generator()
    matrix = [
        [next(gen) for _ in range(2000)] for _ in range(2000)
    ]
    return max(max_sum(lst) for lst in extract_lists(matrix))


if __name__ == '__main__':
    print(main())
