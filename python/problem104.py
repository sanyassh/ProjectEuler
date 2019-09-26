ANSWER = 329468


DIGITS = {str(n) for n in range(1, 10)}
Q5 = 5 ** 0.5
A5 = (1 + Q5) / 2
B5 = (1 - Q5) / 2
TEN = 10 ** 14
TAB = [0, 1, 1]


def fib(n):  # первые 15 цифр
    a = TAB[1]
    b = TAB[2]
    for _ in range(n - TAB[0]):
        a *= A5
        b *= B5
        if a > TEN:
            a /= 10
        if b > TEN:
            b /= 10
    TAB[:] = [n, a, b]
    return round((a - b) / Q5)


def main():
    a, b = 1, 1
    i = 2
    while True:
        a, b = b, a + b
        i += 1
        str_b = str(b)[-9:]
        end = set(str_b)
        if end == DIGITS:
            begin = set(str(fib(i))[:9])
            if begin == DIGITS:
                return i
        b = int(str_b)


if __name__ == '__main__':
    print(main())
