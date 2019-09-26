ANSWER = 2252639041804718029
LIMIT = 10 ** 17


def zeckendorf(n):
    if n < 5:
        return n-1
    fibonacci = [1, 2]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    result = [1, 1, 3]
    for i in range(len(fibonacci) - 4):
        result.append(result[-1] + result[-2] + fibonacci[i])
    if fibonacci[-1] == n:
        return sum(result)
    rest = n - fibonacci[-2]
    return sum(result[:-1]) + rest + zeckendorf(rest)


def main():
    return zeckendorf(LIMIT)


if __name__ == '__main__':
    print(main())
