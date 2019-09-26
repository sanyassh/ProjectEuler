import euler


ANSWER = 16695334890


def main():
    numbers = [
        str(i) for i in range((100 // 17 + 1) * 17, 1000, 17)
        if euler.is_pandigital(i)
    ]
    for i, prime in enumerate((13, 11, 7, 5, 3, 2, 1)):
        numbers = [
            str(n) + number for n in range(10) for number in numbers
        ]
        numbers = [
            number for number in numbers
            if (int(number) // 10 ** (i + 1)) % prime == 0
            and euler.is_pandigital(number)
        ]
    return sum(int(number) for number in numbers)


if __name__ == '__main__':
    print(main())
