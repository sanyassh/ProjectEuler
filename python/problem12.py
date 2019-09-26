import euler


ANSWER = 76576500
LIMIT = 500


def main():
    divisors2 = euler.count_divisors(3)
    i = 4
    while True:
        num = i * (i - 1) // 2
        divisors1 = divisors2
        divisors2 = euler.count_divisors(i)
        i += 1
        if divisors1 * divisors2 > LIMIT:
            if euler.count_divisors(num) > LIMIT:
                return num


if __name__ == '__main__':
    print(main())
