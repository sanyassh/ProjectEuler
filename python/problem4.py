import euler


ANSWER = 906609
DIGITS = 3


def main():
    maximum = 0
    for i in range(10 ** DIGITS - 1, 10 ** (DIGITS - 1) - 1, -1):
        for j in range(10 ** DIGITS - 1, i - 1, -1):
            prod = i * j
            if prod > maximum:
                if euler.is_palindrome(prod):
                    maximum = prod
            else:
                break
    return maximum


if __name__ == '__main__':
    print(main())
