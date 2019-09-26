ANSWER = 1125977393124310
STRING = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
LIMIT = 10 ** 15


def forward(n):
    result = ''
    while n > 1:
        if n % 3 == 0:
            result += 'D'
            n //= 3
            continue
        if n % 3 == 1:
            result += 'U'
            n = (4 * n + 2) // 3
            continue
        if n % 3 == 2:
            result += 'd'
            n = (2 * n - 1) // 3
    return result


def main():
    result = 0
    for i in range(1, len(STRING) + 1):
        for n in range(result, 3 ** (i + 1), 3 ** (i - 1)):
            if forward(n)[:i] == STRING[:i]:
                result = n
                break
    while result < LIMIT:
        result += 3 ** len(STRING)
    return result


if __name__ == '__main__':
    print(main())
