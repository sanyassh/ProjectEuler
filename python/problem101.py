from fractions import Fraction


ANSWER = 37076114526


def polynomial(n):
    return sum((-n) ** i for i in range(1, 11))


def square_approximation(x, y, n, weights=None):
    r = range(len(x))
    weights = weights or [1 for _ in r]
    matrix = [[0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        sum_b = 0
        for j in range(n):
            sum_a = 0
            for k in r:
                sum_a += x[k] ** i * x[k] ** j * weights[k]
            matrix[i][j] = sum_a
        for k in r:
            sum_b += y[k] * x[k] ** i * weights[k]
        matrix[i][n] = sum_b
    return matrix


def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]


def gauss(matrix):
    length = len(matrix)
    r = range(length)
    indices = list(r)
    result = [0 for _ in r]
    for i in r:
        for j in range(i + 1, length):
            if matrix[i][i] == 0:
                swap_rows(matrix, i, j)
                indices[i], indices[j] = indices[j], indices[i]
        if matrix[i][i] == 0:
            return result  # maybe raise some exception?
        for j in range(i + 1, length):
            q = Fraction(matrix[j][i], matrix[i][i])
            for k in range(length + 1):
                matrix[j][k] = matrix[j][k] - matrix[i][k] * q
    for i in range(length - 1, 0, -1):
        for j in range(i):
            q = Fraction(matrix[j][i], matrix[i][i])
            for k in range(length + 1):
                matrix[j][k] = matrix[j][k] - matrix[i][k] * q
    for i in r:
        result[indices[i]] = Fraction(matrix[i][-1], matrix[i][i])
    return result


def main():
    total = 0
    for n in range(1, 11):
        r = range(1, n + 1)
        x = list(r)
        y = [polynomial(i) for i in r]
        matrix = square_approximation(x, y, n)
        c = gauss(matrix)
        total += sum(c[j] * (n + 1) ** j for j in range(n))
    return total


if __name__ == '__main__':
    print(main())
