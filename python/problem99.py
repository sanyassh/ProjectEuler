import euler


ANSWER = 709


def main():
    lst = [line.split(',') for line in euler.data(__file__)]
    result = [int(base) ** (int(exponent) / 10000) for base, exponent in lst]
    return result.index(max(result)) + 1


if __name__ == '__main__':
    print(main())
