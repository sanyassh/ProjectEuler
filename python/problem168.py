ANSWER = 59206
LIMIT = 100


def main():
    result = 0
    for n in range(1, 10):
        n_10_1 = 10 * n - 1
        for last_digit in range(1, 10):
            n_last_digit = n * last_digit
            for power in range(1, LIMIT):
                magic = 10 ** power * last_digit - n_last_digit
                if magic % n_10_1 == 0:
                    num = (magic // n_10_1) * 10 + last_digit
                    rotation = num * n
                    if len(str(num)) == len(str(rotation)):
                        result += num
    return result % 10 ** 5


if __name__ == '__main__':
    print(main())
