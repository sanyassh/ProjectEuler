ANSWER = 1.002322108633


def u(r, k):
    return (900 - 3 * k) * r ** (k - 1)


def s(n, r):
    result = 0
    for k in range(1, n + 1):
        result += u(r, k)
    return result


def main():
    result = 1
    ten = 0.1
    need = -600 * 10 ** 9
    while ten >= 1e-15:
        while s(5000, result) > need:
            result += ten
        result -= ten
        ten /= 10
    return round(result, 12)


if __name__ == '__main__':
    print(main())
