import array


ANSWER = 14316
LIMIT = 10 ** 6


def sum_divisors(n):
    result = array.array('L', (1 for _ in range(n + 1)))
    for i in range(2, n // 2):
        for j in range(2, n // i + 1):
            result[i * j] += i
    return result


LST = sum_divisors(LIMIT)


def length(start):
    leng = 1
    index = LST[start]
    while index > start:
        if leng > 100:
            break
        if index >= LIMIT:
            return 0
        index = LST[index]
        leng += 1
    if index == start:
        return leng
    return 0


def main():
    maximum = 0
    value = 0
    for i in range(1, LIMIT):
        leng = length(i)
        if leng > maximum:
            maximum = leng
            value = i
    return value


if __name__ == '__main__':
    print(main())
