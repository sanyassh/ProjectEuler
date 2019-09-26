import euler


ANSWER = 3284144505


def main():
    last = 0
    for i in range(100000):
        s = str(i * 56789)
        if s.endswith('99999'):
            last = i
    last_digit_sum = sum((9 * i) % 10 for i in range(10))
    for i in range(
            int(round(1 / 0.00000000138, -5)) + last,
            int(round(1 / 0.00000000137, -5)),
            10 ** 5
    ):
        if euler.miller_rabin(i) and euler.prime_cycle_length(i) == i - 1:
            n = i - 1
            result = last_digit_sum * (n // 10)
            for j in range(n % 10):
                result += (9 * j) % 10
            return result
    return 0


if __name__ == '__main__':
    print(main())
