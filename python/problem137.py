import euler


ANSWER = 1120149658760
LIMIT = 15


def main():
    i = 1
    m = 1
    ratio = 2
    while True:
        m += 1
        n = int(m * ratio)
        while True:
            divisor = n * n - m * n - m * m
            if divisor <= 0:
                break
            if euler.gcd1(m, n) and (m * n) % divisor == 0:
                i += 1
                if i == LIMIT:
                    return m * n // divisor
                ratio = n / m
                break
            n -= 1


if __name__ == '__main__':
    print(main())
